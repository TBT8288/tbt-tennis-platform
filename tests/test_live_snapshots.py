"""Tests for local API snapshot capture, deduplication and receipt-time integrity."""
import tempfile
import unittest
from datetime import datetime, timedelta, timezone
from pathlib import Path

from atp_intelligence.api_tennis import normalize_match
from atp_intelligence.live_snapshots import LiveSnapshotStore


UTC = timezone.utc
NOW = datetime(2026, 11, 22, 18, 0, tzinfo=UTC)

SOURCE_RECORD = {
    "event_key": 123,
    "event_date": "2026-11-22",
    "event_first_player": "Player A",
    "event_second_player": "Player B",
    "first_player_key": 1,
    "second_player_key": 2,
    "event_serve": "First Player",
    "event_status": "Set 1",
    "pointbypoint": [{"set_number": "Set 1", "number_game": "1",
                      "points": [{"number_point": 1, "score": "15-0"}]}],
}


class LiveSnapshotsTests(unittest.TestCase):
    def test_insert_dedup_and_new_state(self):
        with tempfile.TemporaryDirectory() as td:
            path = Path(td) / "snapshot.sqlite3"
            store = LiveSnapshotStore(path)
            try:
                p = normalize_match(SOURCE_RECORD, received_at=NOW)
                self.assertTrue(store.ingest(p))
                self.assertFalse(store.ingest(normalize_match(SOURCE_RECORD, received_at=NOW + timedelta(seconds=5))))
                rows = store.history("123")
                self.assertEqual(len(rows), 1)
                self.assertEqual(rows[0][2], 2)
                self.assertEqual(rows[0][3], 1)
                self.assertEqual(rows[0][1], (NOW + timedelta(seconds=5)).isoformat())
                self.assertTrue(store.ingest(normalize_match(
                    {**SOURCE_RECORD, "event_status": "Set 2"}, received_at=NOW + timedelta(seconds=10)
                )))
                self.assertEqual(len(store.history("123")), 2)
                self.assertEqual(store.db.execute(
                    "SELECT count(*) FROM live_snapshots WHERE has_point_level_event_timestamps=0"
                ).fetchone()[0], 2)
            finally:
                store.close()
            reopened = LiveSnapshotStore(path)
            self.assertEqual(len(reopened.history("123")), 2)
            reopened.close()

    def test_snapshots_do_not_become_unverified_point_events(self):
        with LiveSnapshotStore(":memory:") as store:
            store.ingest(normalize_match(SOURCE_RECORD, received_at=NOW))
            self.assertEqual(
                store.db.execute("SELECT has_point_level_event_timestamps FROM live_snapshots").fetchone()[0], 0
            )


if __name__ == "__main__":
    unittest.main()

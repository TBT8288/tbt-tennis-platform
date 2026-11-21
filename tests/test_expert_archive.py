"""Top-100 scope, archival filtering, provenance and persistent-import tests."""
import csv
import unittest
from pathlib import Path
from tempfile import TemporaryDirectory

from atp_intelligence.archive import ExpertArchive
from atp_intelligence.roster import ATPTop100, DEFAULT_ROSTER_PATH

ROOT = Path(__file__).resolve().parents[1] / "research" / "expert_archives"


class ATPTop100Tests(unittest.TestCase):
    def test_roster_is_current_verified_exactly_100(self):
        roster = ATPTop100()
        self.assertEqual(len(roster.players), 100)
        self.assertEqual(roster.as_of, "2026-11-16")
        self.assertEqual(roster.players[0].name, "Alexander Zverev")
        self.assertEqual(roster.players[-1].rank, 100)
        self.assertTrue(roster.eligible("Jakub Mensik"))  # accent-insensitive
        self.assertFalse(roster.eligible("Dennis Novak"))
        self.assertFalse(roster.eligible("David Goffin"))

    def test_roster_rejects_unverified_season(self):
        with TemporaryDirectory() as td:
            bad = Path(td) / "bad.csv"
            with DEFAULT_ROSTER_PATH.open(encoding="utf-8", newline="") as f:
                rows = list(csv.DictReader(f))
            rows[0]["season_main_draw_verified"] = "false"
            with bad.open("w", encoding="utf-8", newline="") as f:
                writer = csv.DictWriter(f, fieldnames=list(rows[0]))
                writer.writeheader()
                writer.writerows(rows)
            with self.assertRaises(ValueError):
                ATPTop100(bad)


class ExpertArchiveTests(unittest.TestCase):
    def test_seed_import_filters_to_top_100_and_is_idempotent(self):
        archive = ExpertArchive()
        try:
            counts = archive.import_directory(ROOT)
            self.assertEqual(counts, {
                "roster": 100, "sources": 10, "player_mentions": 7,
                "observations": 13, "excluded_mentions": 14,
                "excluded_observations": 6
            })
            self.assertEqual(len(archive.get_roster()), 100)
            self.assertEqual(archive.get_roster()[0][1], "Alexander Zverev")
            self.assertEqual(archive.get_status("David Goffin"), [])
            self.assertEqual(archive.get_status("Dennis Novak"), [])
            self.assertEqual(archive.get_status("Brandon Nakashima")[0][0],
                             "competitive_2026_atp_or_challenger")
            self.assertEqual(len(archive.get_observations("Francisco Comesaña")), 0)
            self.assertEqual(len(archive.get_observations("Zizou Bergs")), 2)
            self.assertEqual(len(archive.get_observations("Alexander Zverev")), 3)
            self.assertEqual(len(archive.get_observations("Taylor Fritz")), 1)
            archive.import_directory(ROOT)
            self.assertEqual(archive.db.execute(
                "SELECT count(*) FROM expert_player_mentions").fetchone()[0], 7)
            self.assertEqual(archive.db.execute(
                "SELECT count(*) FROM expert_observations").fetchone()[0], 13)
        finally:
            archive.close()

    def test_sqlite_reopen_scope(self):
        with TemporaryDirectory() as td:
            path = str(Path(td) / "archive.sqlite3")
            archive = ExpertArchive(path)
            archive.import_directory(ROOT)
            archive.close()
            reopened = ExpertArchive(path)
            try:
                self.assertEqual(len(reopened.get_roster()), 100)
                self.assertEqual(len(reopened.get_observations("Zizou Bergs")), 2)
                self.assertEqual(reopened.get_status("Dennis Novak"), [])
            finally:
                reopened.close()


if __name__ == "__main__":
    unittest.main()

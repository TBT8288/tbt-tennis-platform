"""ATP top-150 roster accuracy, provenance, archive filtering, and migration."""
import csv
import sqlite3
import unittest
from pathlib import Path
from tempfile import TemporaryDirectory

from atp_intelligence.archive import ExpertArchive
from atp_intelligence.roster import ATPTop150, DEFAULT_ROSTER_PATH

ROOT = Path(__file__).resolve().parents[1] / "research" / "expert_archives"


class ATPTop150Tests(unittest.TestCase):
    def test_roster_has_150_players(self):
        roster = ATPTop150()
        self.assertEqual(len(roster.players), 150)
        self.assertEqual(roster.as_of, "2026-11-16")
        self.assertEqual(roster.players[0].name, "Alexander Zverev")
        self.assertEqual(roster.players[-1].rank, 150)
        self.assertTrue(roster.eligible("Jakub Mensik"))
        self.assertTrue(roster.eligible("Yibing Wu"))
        self.assertTrue(roster.eligible("Francisco Comesana"))
        self.assertTrue(roster.eligible("Giovanni Mpetshi Perricard"))
        self.assertFalse(roster.eligible("Dennis Novak"))
        self.assertFalse(roster.eligible("David Goffin"))
        self.assertFalse(roster.eligible("Joris De Loore"))
        self.assertEqual(roster.find("Yibing Wu").rank, 106)

    def test_unverified_season_stats_remain_missing(self):
        roster = ATPTop150()
        self.assertTrue(any(p.main_draw_wins is None for p in roster.players))
        self.assertTrue(any(p.main_draw_wins is not None for p in roster.players))

    def test_reject_invalid_provenance_and_missing_half_stat(self):
        with TemporaryDirectory() as td:
            output = Path(td) / "bad.csv"
            with DEFAULT_ROSTER_PATH.open(encoding="utf-8", newline="") as handle:
                source = list(csv.DictReader(handle))
            self.assertEqual(len(source), 150)
            cols = list(source[0])
            def assert_invalid(rows):
                with output.open("w", encoding="utf-8", newline="") as handle:
                    writer = csv.DictWriter(handle, fieldnames=cols)
                    writer.writeheader()
                    writer.writerows(rows)
                with self.assertRaises(ValueError):
                    ATPTop150(output)
            changed = [dict(x) for x in source]
            changed[0]["ranking_crosschecked"] = ""
            assert_invalid(changed)
            changed = [dict(x) for x in source]
            changed[0]["season_main_draw_wins"] = ""
            assert_invalid(changed)
            changed = [dict(x) for x in source]
            changed[0]["rank"] = "151"
            assert_invalid(changed)


class ExpertArchiveTests(unittest.TestCase):
    def test_import_filters_to_top_150_and_is_idempotent(self):
        archive = ExpertArchive()
        try:
            counts = archive.import_directory(ROOT)
            self.assertEqual(counts, {
                "roster": 150, "season_stats": 150,
                "season_stats_verified": 146,
                "sources": 10, "player_mentions": 12,
                "observations": 18, "excluded_mentions": 9,
                "excluded_observations": 1
            })
            self.assertEqual(len(archive.get_roster()), 150)
            self.assertEqual(archive.get_roster()[0][1], "Alexander Zverev")
            self.assertEqual(archive.get_status("David Goffin"), [])
            self.assertEqual(archive.get_status("Dennis Novak"), [])
            self.assertEqual(archive.get_status("Yibing Wu")[0][0],
                             "competitive_2026_atp_or_challenger")
            self.assertEqual(len(archive.get_observations("Francisco Comesaña")), 2)
            self.assertEqual(len(archive.get_observations("Giovanni Mpetshi Perricard")), 1)
            self.assertEqual(len(archive.get_observations("Zizou Bergs")), 2)
            self.assertEqual(len(archive.get_observations("Alexander Zverev")), 3)
            self.assertEqual(len(archive.get_observations("Taylor Fritz")), 1)
            archive.import_directory(ROOT)
            self.assertEqual(archive.db.execute(
                "SELECT count(*) FROM expert_player_mentions").fetchone()[0], 12)
            self.assertEqual(archive.db.execute(
                "SELECT count(*) FROM expert_observations").fetchone()[0], 18)
        finally:
            archive.close()

    def test_sqlite_persistence_and_old_schema_upgrade(self):
        with TemporaryDirectory() as td:
            db_path = str(Path(td) / "archive.sqlite3")
            with sqlite3.connect(db_path) as db:
                db.execute(
                    """CREATE TABLE atp_roster (
                       rank INTEGER PRIMARY KEY CHECK (rank BETWEEN 1 AND 100),
                       player TEXT NOT NULL UNIQUE,
                       country TEXT NOT NULL,
                       ranking_points INTEGER NOT NULL,
                       ranking_date TEXT NOT NULL,
                       main_draw_wins INTEGER NOT NULL,
                       main_draw_losses INTEGER NOT NULL)"""
                )
            archive = ExpertArchive(db_path)
            archive.import_directory(ROOT)
            archive.close()
            reopened = ExpertArchive(db_path)
            try:
                self.assertEqual(len(reopened.get_roster()), 150)
                self.assertEqual(len(reopened.get_observations("Zizou Bergs")), 2)
                self.assertEqual(reopened.get_status("Dennis Novak"), [])
            finally:
                reopened.close()


if __name__ == "__main__":
    unittest.main()

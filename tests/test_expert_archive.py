"""Tests for the archival import and provenance of historical player profiles."""
import unittest
from pathlib import Path
from tempfile import TemporaryDirectory

from atp_intelligence.archive import ExpertArchive

ROOT = Path(__file__).resolve().parents[1] / "research" / "expert_archives"


class ExpertArchiveTests(unittest.TestCase):
    def test_seed_archive_import_and_idempotence(self):
        archive = ExpertArchive()
        try:
            counts = archive.import_directory(ROOT)
            self.assertEqual(counts, {"sources": 5, "players": 21, "observations": 11})
            self.assertEqual(len(archive.get_status("Maxime Cressy")), 1)
            self.assertEqual(archive.get_status("David Goffin")[0][0], "retired_confirmed")
            self.assertEqual(archive.get_status("Brandon Nakashima")[0][0],
                             "competitive_2026_atp_or_challenger")
            obs = archive.get_observations("Francisco Comesaña")
            self.assertEqual(len(obs), 2)
            self.assertIn("2024-04-23", obs[0][0])
            self.assertIn("lastwordonsports.com", obs[0][3])
            archive.import_directory(ROOT)
            self.assertEqual(archive.db.execute(
                "SELECT count(*) FROM expert_player_mentions").fetchone()[0], 21)
            self.assertEqual(archive.db.execute(
                "SELECT count(*) FROM expert_observations").fetchone()[0], 11)
        finally:
            archive.close()

    def test_sqlite_reopen(self):
        with TemporaryDirectory() as d:
            path = str(Path(d) / "archive.sqlite3")
            archive = ExpertArchive(path)
            archive.import_directory(ROOT)
            archive.close()
            reopened = ExpertArchive(path)
            try:
                self.assertEqual(len(reopened.get_observations("Zizou Bergs")), 2)
                self.assertEqual(reopened.get_status("Dennis Novak")[0][0],
                                 "retired_confirmed")
            finally:
                reopened.close()


if __name__ == "__main__":
    unittest.main()

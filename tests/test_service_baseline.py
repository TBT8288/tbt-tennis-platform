"""Offline evidence-based B0 point prior tests."""
import unittest
from datetime import date

from atp_intelligence.service_baseline import ServiceBaselineArchive
from atp_intelligence.probability import game_win_probability


class TestServiceBaseline(unittest.TestCase):
    def test_known_2026_server_prior_and_hold(self):
        archive = ServiceBaselineArchive()
        player = archive.get("Jannik Sinner", as_of=date(2026, 11, 22))
        self.assertIsNotNone(player)
        self.assertEqual(player.source_year, 2026)
        self.assertGreater(player.sample_matches, 0)
        self.assertAlmostEqual(player.service_point_chance, 0.728766, places=6)
        self.assertGreater(game_win_probability(player.service_point_chance), 0.5)
        self.assertEqual(player.label, "unadjusted_archive_baseline_not_validated")

    def test_all_existing_data_never_invent_points(self):
        archive = ServiceBaselineArchive()
        self.assertEqual(len(archive._rows), 150)
        found = [archive.get(x["name"], as_of=date(2026, 11, 22))
                 for x in archive._rows.values()]
        self.assertGreaterEqual(sum(x is not None for x in found), 140)
        self.assertLessEqual(sum(x is not None for x in found), 150)
        for x in found:
            if x is not None:
                self.assertTrue(0 <= x.service_point_chance <= 1)

    def test_snapshot_no_lookahead(self):
        archive = ServiceBaselineArchive()
        with self.assertRaises(ValueError):
            archive.get("Jannik Sinner", as_of=date(2026, 1, 1))
        with self.assertRaises(ValueError):
            archive.get("Jannik Sinner", as_of=date(2026, 11, 15))
        self.assertIsNone(archive.get("Unknown Player", as_of=date(2026, 11, 22)))
        self.assertIsNone(archive.get("Jannik Sinner", as_of=date(2028, 1, 2)))


if __name__ == "__main__":
    unittest.main()

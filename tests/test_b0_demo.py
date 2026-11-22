"""ATP-DEV-001: pure, offline tests for the manual-input B0 demo."""
import unittest

from b0_demo import calculate_b0


class B0DemoTests(unittest.TestCase):
    def test_even_game_with_fifty_percent_point_chance(self):
        result = calculate_b0(0.5, 0, 0)
        self.assertAlmostEqual(result.server_game_win, 0.5)
        self.assertAlmostEqual(result.returner_break, 0.5)
        self.assertIsNone(result.completed_by)

    def test_server_advantage(self):
        result = calculate_b0(0.5, 4, 3)
        self.assertAlmostEqual(result.server_game_win, 0.75)
        self.assertAlmostEqual(result.returner_break, 0.25)
        self.assertIsNone(result.completed_by)

    def test_returner_advantage(self):
        result = calculate_b0(0.5, 3, 4)
        self.assertAlmostEqual(result.server_game_win, 0.25)
        self.assertAlmostEqual(result.returner_break, 0.75)
        self.assertIsNone(result.completed_by)

    def test_probabilities_are_complements(self):
        for p in (0.0, 0.2, 0.5, 0.65, 0.8, 1.0):
            for score in ((0, 0), (2, 3), (3, 3), (4, 3), (3, 4), (9, 9), (4, 0), (0, 4)):
                with self.subTest(p=p, score=score):
                    result = calculate_b0(p, *score)
                    self.assertGreaterEqual(result.server_game_win, 0.0)
                    self.assertLessEqual(result.server_game_win, 1.0)
                    self.assertGreaterEqual(result.returner_break, 0.0)
                    self.assertLessEqual(result.returner_break, 1.0)
                    self.assertAlmostEqual(result.server_game_win + result.returner_break, 1.0)

    def test_extreme_point_probabilities(self):
        self.assertEqual(calculate_b0(0, 0, 0).server_game_win, 0.0)
        self.assertEqual(calculate_b0(1, 0, 0).server_game_win, 1.0)

    def test_completed_game_status(self):
        finished_by_server = calculate_b0(0.2, 4, 1)
        self.assertEqual(finished_by_server.completed_by, "server")
        self.assertEqual(finished_by_server.server_game_win, 1.0)
        self.assertEqual(finished_by_server.returner_break, 0.0)

        finished_by_returner = calculate_b0(0.8, 1, 4)
        self.assertEqual(finished_by_returner.completed_by, "returner")
        self.assertEqual(finished_by_returner.server_game_win, 0.0)
        self.assertEqual(finished_by_returner.returner_break, 1.0)

    def test_invalid_probability_or_points_rejected(self):
        bad_inputs = (
            (-0.1, 0, 0),
            (1.1, 0, 0),
            (float("nan"), 0, 0),
            (float("inf"), 0, 0),
            (True, 0, 0),
            (0.5, -1, 0),
            (0.5, 0, -1),
            (0.5, 0.5, 0),
            (0.5, 0, True),
        )
        for args in bad_inputs:
            with self.subTest(args=args):
                with self.assertRaises(ValueError):
                    calculate_b0(*args)


if __name__ == "__main__":
    unittest.main()

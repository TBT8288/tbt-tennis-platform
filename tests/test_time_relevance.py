"""Regression tests for time-window gating, low-sample H2H, and leakage."""
import unittest
from datetime import date

from atp_intelligence.time_relevance import (
    h2h_shrunk_win_rate,
    in_predictive_window,
    relevance_weight,
)


class RelevanceWindowTests(unittest.TestCase):
    AS_OF = date(2026, 11, 21)

    def test_only_2026_and_2025_are_predictive(self):
        self.assertTrue(in_predictive_window(date(2026, 8, 1), self.AS_OF))
        self.assertTrue(in_predictive_window(date(2025, 1, 1), self.AS_OF))
        self.assertFalse(in_predictive_window(date(2024, 12, 31), self.AS_OF))
        self.assertFalse(in_predictive_window(date(2023, 11, 20), self.AS_OF))

    def test_current_day_and_future_results_are_not_visible(self):
        self.assertFalse(in_predictive_window(self.AS_OF, self.AS_OF))
        self.assertFalse(in_predictive_window(date(2026, 12, 1), self.AS_OF))
        self.assertEqual(relevance_weight(self.AS_OF, self.AS_OF), 0.0)

    def test_rolls_forward_with_calendar_year(self):
        as_of = date(2027, 1, 3)
        self.assertFalse(in_predictive_window(date(2025, 12, 31), as_of))
        self.assertTrue(in_predictive_window(date(2026, 12, 31), as_of))

    def test_recent_meetings_outweigh_old_ones(self):
        fresh = date(2026, 11, 1)
        old = date(2025, 2, 1)
        self.assertGreater(relevance_weight(fresh, self.AS_OF), relevance_weight(old, self.AS_OF))
        self.assertGreater(relevance_weight(fresh, self.AS_OF, "h2h"),
                           relevance_weight(old, self.AS_OF, "h2h"))
        self.assertEqual(relevance_weight(date(2024, 1, 1), self.AS_OF, "h2h"), 0.0)

    def test_invalid_feature_kind_rejected(self):
        with self.assertRaises(ValueError):
            relevance_weight(date(2026, 1, 1), self.AS_OF, "legacy")

    def test_no_h2h_history_returns_neutral_baseline_not_win_probability(self):
        rate, n = h2h_shrunk_win_rate([], "A", "B", self.AS_OF)
        self.assertEqual(rate, 0.5)
        self.assertEqual(n, 0.0)

    def test_old_h2h_is_kept_only_as_archive(self):
        rate, n = h2h_shrunk_win_rate(
            [(date(2024, 1, 15), "A"), (date(2023, 8, 1), "A")],
            "A", "B", self.AS_OF,
        )
        self.assertEqual(rate, 0.5)
        self.assertEqual(n, 0.0)

    def test_one_recent_h2h_is_shrunk_toward_neutral(self):
        rate, n = h2h_shrunk_win_rate(
            [(date(2026, 10, 30), "A")], "A", "B", self.AS_OF
        )
        self.assertGreater(rate, 0.5)
        self.assertLess(rate, 0.75)
        self.assertGreater(n, 0.0)

    def test_unknown_winner_is_not_silently_accepted(self):
        with self.assertRaises(ValueError):
            h2h_shrunk_win_rate([(date(2026, 5, 10), "C")],
                                 "A", "B", self.AS_OF)


if __name__ == "__main__":
    unittest.main()

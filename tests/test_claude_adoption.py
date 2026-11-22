"""Validation checks for the Claude-history adoption baseline.

Run: python -m unittest discover -s tests -v
"""
import math
import unittest

from atp_intelligence.legacy_research import (
    STYLE_CATEGORIES,
    binary_log_loss,
    brier_score,
    parse_style_label,
)


class ClaudeStyleTaxonomyTests(unittest.TestCase):
    def test_six_canonical_styles(self):
        self.assertEqual(len(STYLE_CATEGORIES), 6)
        for label in STYLE_CATEGORIES:
            self.assertEqual(parse_style_label(label), label)

    def test_no_style_must_remain_missing(self):
        self.assertIsNone(parse_style_label(None))
        self.assertIsNone(parse_style_label(" "))

    def test_unverified_or_new_style_does_not_get_guessed(self):
        with self.assertRaises(ValueError):
            parse_style_label("mental collapse")
        with self.assertRaises(TypeError):
            parse_style_label(3)


class ClaudeMetricsTests(unittest.TestCase):
    def test_brier_perfect_and_mixed(self):
        self.assertAlmostEqual(brier_score([1.0, 0.0], [1, 0]), 0)
        self.assertAlmostEqual(brier_score([0.8, 0.2], [1, 0]), 0.04)

    def test_log_loss_reference(self):
        self.assertAlmostEqual(binary_log_loss([0.5, 0.5], [1, 0]), math.log(2))
        self.assertTrue(math.isfinite(binary_log_loss([0, 1], [1, 0])))

    def test_invalid_samples_rejected(self):
        bad = [
            ([], []),
            ([0.5], [1, 0]),
            ([float("nan")], [1]),
            ([1.2], [1]),
            ([0.5], [2]),
        ]
        for ps, ys in bad:
            with self.subTest(ps=ps, ys=ys):
                with self.assertRaises(ValueError):
                    brier_score(ps, ys)

    def test_log_loss_invalid_eps(self):
        with self.assertRaises(ValueError):
            binary_log_loss([0.2], [1], eps=0)

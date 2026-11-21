"""Run with: python -m unittest discover -s tests -v"""
import tempfile
import unittest
from datetime import datetime, timedelta, timezone
from pathlib import Path
from atp_intelligence import (
    EventStore, PointEvent, Prediction, Observation,
    hold_probability, break_probability, game_win_probability
)


UTC = timezone.utc
NOW = datetime(2026, 11, 21, 14, 0, tzinfo=UTC)


class GameProbabilityTests(unittest.TestCase):
    def test_fair_point_even_game(self):
        self.assertAlmostEqual(hold_probability(0.5), 0.5)

    def test_extremes(self):
        self.assertEqual(hold_probability(0), 0)
        self.assertEqual(hold_probability(1), 1)

    def test_complement(self):
        for p in (0.1, 0.5, 0.65, 0.8):
            self.assertAlmostEqual(hold_probability(p)+break_probability(p), 1)

    def test_advantage(self):
        self.assertAlmostEqual(game_win_probability(0.5, 4, 3), 0.75)
        self.assertAlmostEqual(game_win_probability(0.5, 3, 4), 0.25)
        self.assertAlmostEqual(game_win_probability(0.5, 12, 12), 0.5)

    def test_terminal_states(self):
        self.assertEqual(game_win_probability(0.2, 4, 0), 1)
        self.assertEqual(game_win_probability(0.9, 1, 4), 0)

    def test_invalid_inputs(self):
        for p in (-0.1,1.1,float('nan'),float('inf'),True):
            with self.assertRaises(ValueError):
                hold_probability(p)
        with self.assertRaises(ValueError):
            game_win_probability(0.7, 0, -1)


class EventsTests(unittest.TestCase):
    def test_point_rejects_naive_timestamp(self):
        with self.assertRaises(ValueError):
            PointEvent("m","e","A","A",datetime(2026,11,21))

    def test_future_evidence_rejected(self):
        with self.assertRaises(ValueError):
            Prediction("p","m","next_game",0.3,"B0",created_at=NOW,
                       evidence_cutoff=NOW+timedelta(seconds=1))

    def test_observation_category_and_value(self):
        with self.assertRaises(ValueError):
            Observation("m","A","rhythm",0.3,NOW,"video","psychological")
        with self.assertRaises(ValueError):
            Observation("m","A","rhythm",float("nan"),NOW,"video","behavioral")


class StorageTests(unittest.TestCase):
    def test_point_deduplication_and_history(self):
        with tempfile.TemporaryDirectory() as tempdir:
            store = EventStore(str(Path(tempdir)/"test.db"))
            p = PointEvent("m","pt-1","A","B",NOW,source="fixture")
            self.assertTrue(store.add_point(p))
            self.assertFalse(store.add_point(p))
            self.assertEqual(len(store.points_for_match("m")), 1)
            store.close()

    def test_prediction_deduplication_and_history(self):
        store = EventStore()
        p = Prediction("pred-1","m","next_server_game",0.2,"B0",
                       created_at=NOW,evidence_cutoff=NOW-timedelta(seconds=1))
        self.assertTrue(store.add_prediction(p))
        self.assertFalse(store.add_prediction(p))
        self.assertEqual(store.predictions_for_match("m")[0][2], 0.2)
        store.close()


if __name__ == "__main__":
    unittest.main()

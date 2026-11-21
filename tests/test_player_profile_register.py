"""Data-quality contract for the current ATP Top150 unified research register.

No external paid APIs required. The checks guard that coach reports or
inferred psychology are not confused with verified physical attributes.
"""
import csv
import unittest
from datetime import date
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
REG = ROOT / "research/player_profiles/atp_top150_profile_register_2026_11_21.csv"
ROSTER = ROOT / "research/rosters/atp_top150_2026_11_16.csv"
SUMMARY = ROOT / "research/player_profiles/ATP_TOP150_ATTEKINTHETO_LISTA_2026_11_21.csv"


def rows(path, delimiter=","):
    with path.open(encoding="utf-8-sig", newline="") as stream:
        return list(csv.DictReader(stream, delimiter=delimiter))


class ATPTop150ProfileRegisterTests(unittest.TestCase):
    def test_all_ranked_players_exactly_once(self):
        roster = rows(ROSTER)
        data = rows(REG)
        self.assertEqual(len(roster), 150)
        self.assertEqual(len(data), 150)
        self.assertEqual(
            [(int(x["rank"]), x["player"]) for x in data],
            [(int(x["rank"]), x["player"]) for x in roster],
        )

    def test_biographies_are_source_backed_and_age_matches_birth_date(self):
        data = rows(REG)
        missing_weight = 0
        for p in data:
            self.assertTrue(p["biography_source"], p["player"])
            self.assertIn(p["dominant_hand"], {"Jobb", "Bal"})
            birth = date.fromisoformat(p["date_of_birth"])
            age = 2026 - birth.year - ((11, 21) < (birth.month, birth.day))
            self.assertEqual(int(p["age_as_of_2026_11_21"]), age, p["player"])
            if p["height_cm"]:
                self.assertTrue(160 <= int(p["height_cm"]) <= 215, p["player"])
            if p["weight_kg"]:
                self.assertTrue(50 <= int(p["weight_kg"]) <= 130, p["player"])
            else:
                missing_weight += 1
        self.assertEqual(missing_weight, 16)
        self.assertEqual(next(x for x in data if x["player"] == "Flavio Cobolli")["height_cm"], "183")

    def test_surface_elo_is_present_and_attributed_for_all(self):
        data = rows(REG)
        for p in data:
            self.assertTrue(p["surface_elo_source"], p["player"])
            for col in ("overall_elo_pythia_2026_11_20", "hard_elo_2026_11_20",
                        "clay_elo_2026_11_20"):
                self.assertTrue(p[col], (p["player"], col))
                self.assertGreater(int(p[col]), 1000)
            self.assertIn(p["surface_elo_verification"], {"source_name_match", "alias_name_verified"})

    def test_season_discrepancies_are_not_fabricated(self):
        data = rows(REG)
        excluded = [x for x in data if x["season_verification"] == "not_verified"]
        self.assertEqual({int(x["rank"]) for x in excluded}, {107, 116, 130, 132})
        for p in excluded:
            self.assertFalse(p["year_2026_wins"])
            self.assertFalse(p["year_2026_losses"])
            self.assertFalse(p["year_2026_elo"])

    def test_tactical_classifications_are_sourced_and_mental_labels_not_fabricated(self):
        data = rows(REG)
        sourced = 0
        for p in data:
            self.assertIn("nem minősített", p["mental_pressure_profile"])
            if p["playing_style_source"]:
                sourced += 1
                self.assertTrue(p["playing_style_source"].startswith("https://"))
                self.assertTrue(p["strength_source"].startswith("https://"))
                self.assertTrue(p["weakness_source"].startswith("https://"))
                self.assertTrue(p["playing_style"].startswith("Előzetes történeti: "))
            else:
                self.assertIn("nincs még forrásolt", p["playing_style"])
            self.assertEqual(p["profile_status"], "alapadatok és statisztika; edzői dosszié fejlesztés alatt")
        self.assertEqual(sourced, 7)

    def test_readable_list_matches_main_register(self):
        main = rows(REG)
        friendly = rows(SUMMARY, delimiter=";")
        self.assertEqual(len(friendly), 150)
        for a, b in zip(main, friendly):
            self.assertEqual(a["rank"], b["ATP hely"])
            self.assertEqual(a["player"], b["Játékos"])
            self.assertEqual(a["weight_kg"], b["Testsúly kg"])
            self.assertEqual(a["hard_elo_2026_11_20"], b["Hard Elo"])


if __name__ == "__main__":
    unittest.main()

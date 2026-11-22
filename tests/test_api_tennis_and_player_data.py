"""Offline integration/regression tests for research data and API-Tennis adapter.

No credentials and no external network are required; fixtures are synthetic.
"""
import json
import unittest
from datetime import date, datetime, timezone
from urllib.error import HTTPError, URLError
from urllib.parse import parse_qs

from atp_intelligence.api_tennis import (
    API_BASE_URL, TennisAPIClient, TennisAPIError,
    normalize_match, verified_main_draw_matches,
)
from atp_intelligence.player_data import Top150Profiles, TwoSeasonH2H, parse_record_date


class TestTop150Data(unittest.TestCase):
    def test_all_profiles_and_provenance(self):
        profiles = Top150Profiles()
        report = profiles.audit()
        self.assertEqual(report["players"], 150)
        self.assertEqual(report["height_cm_master"], 134)
        self.assertEqual(report["weight_kg_master"], 134)
        self.assertEqual(report["backhand_master"], 104)
        self.assertEqual(report["year_2026_wins_master"], 146)
        self.assertEqual(report["height_cm_with_candidates"], 150)
        self.assertEqual(report["weight_kg_with_candidates"], 150)
        self.assertEqual(report["backhand_with_candidates"], 150)

        self.assertEqual(profiles.find("Alexander Zverev").field("height_cm"), ("198", "master_snapshot"))
        kouame = profiles.find("Moïse Kouamé")
        self.assertIsNotNone(kouame)
        self.assertEqual(kouame.field("height_cm")[1], "candidate_only")
        self.assertTrue(kouame.candidates["height_cm"].source_url.startswith("https://"))
        self.assertIsNone(profiles.find("Unknown Unranked Player"))

    def test_candidate_does_not_override_master(self):
        p = Top150Profiles().find("Flavio Cobolli")
        self.assertEqual(p.field("height_cm"), ("183", "master_snapshot"))

    def test_h2h_date_normalization(self):
        self.assertEqual(parse_record_date("20251027"), date(2025, 10, 27))
        self.assertEqual(parse_record_date("2026-07-12T15:10:00Z"), date(2026, 7, 12))
        with self.assertRaises(ValueError):
            parse_record_date("broken-date")

    def test_h2h_asof_and_reverse(self):
        archive = TwoSeasonH2H()
        self.assertEqual(len(archive.rows), 2809)
        a = archive.for_match("Alexander Zverev", "Jannik Sinner", as_of=date(2026, 11, 22))
        self.assertEqual((a.wins_a, a.wins_b, a.matches), (0, 9, 9))
        self.assertEqual(a.archive_cutoff, date(2026, 11, 15))
        b = archive.for_match("Jannik Sinner", "Alexander Zverev", as_of=date(2027, 1, 2))
        self.assertEqual((b.wins_a, b.wins_b, b.matches), (5, 0, 5))
        missing = archive.for_match("Fictitious First", "Fictitious Second", as_of=date(2026, 11, 22))
        self.assertEqual(missing.matches, 0)

    def test_no_lookahead_on_aggregate(self):
        archive = TwoSeasonH2H()
        with self.assertRaises(ValueError):
            archive.for_match("Alexander Zverev", "Jannik Sinner", as_of=date(2026, 7, 1))
        with self.assertRaises(ValueError):
            archive.for_match("Alexander Zverev", "Jannik Sinner", as_of=date(2026, 11, 15))


class FakeResponse:
    def __init__(self, body):
        self.body = body

    def __enter__(self):
        return self

    def __exit__(self, *_):
        return None

    def read(self):
        return self.body


class TestTennisAPIAdapter(unittest.TestCase):
    EXAMPLE = {
        "event_key": 11997372,
        "event_date": "2026-11-22",
        "event_first_player": "Test A",
        "event_second_player": "Test B",
        "first_player_key": 11,
        "second_player_key": 22,
        "event_type_type": "Atp Singles",
        "tournament_key": 777,
        "event_qualification": 0,
        "event_serve": "First Player",
        "event_status": "Set 1",
        "pointbypoint": [{"number_game": "1", "points": [{"number_point": "1", "score": "15 - 0"}]}],
        "statistics": [],
    }

    def test_form_encoded_secret_not_in_url(self):
        seen = []
        def fake_opener(req, timeout):
            self.assertEqual(req.full_url, API_BASE_URL)
            self.assertNotIn("secret-for-test", req.full_url)
            params = parse_qs(req.data.decode())
            seen.append(params)
            return FakeResponse(json.dumps({"success": 1, "result": [{"event_type_key": 265}]}).encode())

        client = TennisAPIClient(api_key="secret-for-test", opener=fake_opener)
        self.assertEqual(client.events()[0]["event_type_key"], 265)
        self.assertEqual(seen[0]["method"], ["get_events"])
        self.assertEqual(seen[0]["APIkey"], ["secret-for-test"])

    def test_observed_match_and_scope(self):
        m = normalize_match(self.EXAMPLE, received_at=datetime(2026, 11, 22, tzinfo=timezone.utc))
        self.assertEqual(m.server, "first")
        self.assertEqual(m.match_key, "11997372")
        self.assertEqual(m.first_player_key, "11")
        self.assertFalse(m.stats_available)
        self.assertEqual(m.received_at.year, 2026)
        self.assertEqual(len(m.point_games), 1)
        self.assertEqual(verified_main_draw_matches([m], approved_tournament_keys={"777"}), [m])
        self.assertEqual(verified_main_draw_matches([m], approved_tournament_keys=set()), [])
        q = normalize_match({**self.EXAMPLE, "event_qualification": None})
        self.assertEqual(verified_main_draw_matches([q], approved_tournament_keys={"777"}), [])

    def test_live_and_h2h_endpoints(self):
        calls = []
        def opener(req, timeout):
            params = parse_qs(req.data.decode())
            calls.append(params["method"][0])
            method = params["method"][0]
            data = ([self.EXAMPLE] if method == "get_livescore" else
                    {"H2H": [], "firstPlayerResults": [], "secondPlayerResults": []})
            return FakeResponse(json.dumps({"success": 1, "result": data}).encode())
        c = TennisAPIClient("testing", opener=opener)
        self.assertEqual(c.livescore()[0].first_player, "Test A")
        self.assertEqual(c.h2h("11", "22")["H2H"], [])
        self.assertEqual(calls, ["get_livescore", "get_H2H"])

    def test_failures_and_no_key_exposure(self):
        def broken(_req, timeout):
            raise URLError("secret-for-test leaked by transport")
        c = TennisAPIClient("secret-for-test", opener=broken, max_attempts=1)
        with self.assertRaises(TennisAPIError) as ctx:
            c.events()
        self.assertNotIn("secret-for-test", str(ctx.exception))
        with self.assertRaises(ValueError):
            c.fixtures(date(2026, 11, 23), date(2026, 11, 22))
        with self.assertRaises(ValueError):
            c._call("get_events", APIkey="overridden")
        with self.assertRaises(ValueError):
            c.h2h("22", "22")

    def test_429_retries_without_exposing_url(self):
        calls = []
        def flaky(req, timeout):
            calls.append(1)
            if len(calls) == 1:
                raise HTTPError(req.full_url, 429, "rate-limit", None, None)
            return FakeResponse(b'{"success":1,"result":[]}')
        c = TennisAPIClient("secret-for-test", opener=flaky, sleeper=lambda _: None, max_attempts=2)
        self.assertEqual(c.events(), [])
        self.assertEqual(len(calls), 2)

    def test_invalid_response_not_accepted(self):
        c = TennisAPIClient("test", opener=lambda req, timeout: FakeResponse(b'{"success":1,"data":[]}'))
        with self.assertRaises(TennisAPIError):
            c.events()


if __name__ == "__main__":
    unittest.main()

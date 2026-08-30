"""
tennis_api_client.py
---------------------
A Tennis API (ATP WTA ITF, RapidAPI) klienskódja.
"""

from __future__ import annotations

import os
import time
from dataclasses import dataclass, field
from typing import Optional

import requests


API_HOST = "tennis-api-atp-wta-itf.p.rapidapi.com"
LIVE_EVENTS_URL = f"https://{API_HOST}/tennis/v2/extend/api/events/live"


@dataclass
class MatchState:
    player1: Optional[str] = None
    player2: Optional[str] = None
    score: Optional[str] = None
    status: Optional[str] = None
    raw: dict = field(default_factory=dict)

    def is_complete(self) -> bool:
        return bool(self.player1 and self.player2 and self.score)


def _get_api_key() -> str:
    api_key = os.environ.get("RAPIDAPI_KEY")
    if not api_key:
        raise RuntimeError(
            "Hiányzik a RAPIDAPI_KEY környezeti változó. "
            "Állítsd be, mielőtt futtatod a programot."
        )
    return api_key


def fetch_live_matches() -> list[dict]:
    """
    Lekéri az API-tól az összes jelenleg élő meccset, 
    és kiírja a nyers darabszámot a terminálra.
    """
    headers = {
        "X-RapidAPI-Key": _get_api_key(),
        "X-RapidAPI-Host": API_HOST,
    }
    
    for attempt in range(2):
        try:
            response = requests.get(LIVE_EVENTS_URL, headers=headers, timeout=30)
            response.raise_for_status()
            data = response.json()
            
            raw_list = []
            if isinstance(data, list):
                raw_list = data
            else:
                for key in ("results", "events", "data", "result", "matches", "live"):
                    if isinstance(data, dict) and key in data and isinstance(data[key], list):
                        raw_list = data[key]
                        break
                if not raw_list and isinstance(data, dict):
                    raw_list = [data]

            print(f"-> [API Debug] A RapidAPI összesen {len(raw_list)} nyers meccseseményt adott vissza.")
            return raw_list
            
        except requests.exceptions.Timeout:
            if attempt == 0:
                time.sleep(1)
                continue
            print("Figyelem: A RapidAPI válasza túl sokáig tartott (időtúllépés).")
            return []
        except requests.exceptions.RequestException as e:
            print(f"Hiba történt a hálózati kérés közben: {e}")
            return []
            
    return []


def _extract_name(player_obj) -> Optional[str]:
    if isinstance(player_obj, str):
        return player_obj
    if isinstance(player_obj, dict):
        for key in ("name", "player_name", "full_name", "shortName"):
            if key in player_obj:
                return player_obj[key]
    return None


def parse_match(raw: dict) -> MatchState:
    match_obj = raw.get("match", raw)

    player1 = (
        _extract_name(match_obj.get("player1"))
        or _extract_name(match_obj.get("participant1"))
        or _extract_name(match_obj.get("player_1"))
        or _extract_name(match_obj.get("home"))
    )
    player2 = (
        _extract_name(match_obj.get("player2"))
        or _extract_name(match_obj.get("participant2"))
        or _extract_name(match_obj.get("player_2"))
        or _extract_name(match_obj.get("away"))
    )
    score = (
        match_obj.get("score")
        or raw.get("score")
        or match_obj.get("current_score")
    )
    status = (
        raw.get("status")
        or match_obj.get("status")
        or raw.get("round")
    )

    return MatchState(
        player1=player1,
        player2=player2,
        score=str(score) if score is not None else None,
        status=str(status) if status is not None else None,
        raw=raw,
    )


def find_match(name_query: str) -> Optional[MatchState]:
    query = name_query.lower()
    for raw in fetch_live_matches():
        state = parse_match(raw)
        names = f"{state.player1 or ''} {state.player2 or ''}".lower()
        if query in names:
            return state
    return None


def list_live_matches() -> list[MatchState]:
    return [parse_match(raw) for raw in fetch_live_matches()]
"""
tennis_api_client.py
---------------------
Sportscore Tennis API klienskód (RapidAPI).
"""

from __future__ import annotations

import os
import time
from dataclasses import dataclass, field
from typing import Optional

import requests


API_HOST = "sportscore1.p.rapidapi.com"
LIVE_EVENTS_URL = f"https://{API_HOST}/tennis/matches/live"


@dataclass
class MatchState:
    player1: Optional[str] = None
    player2: Optional[str] = None
    score: Optional[str] = None
    status: Optional[str] = None
    raw: dict = field(default_factory=dict)

    def is_complete(self) -> bool:
        return bool(self.player1 and self.player2)


def _get_api_key() -> str:
    api_key = os.environ.get("RAPIDAPI_KEY")
    if not api_key:
        raise RuntimeError(
            "Hiányzik a RAPIDAPI_KEY környezeti változó. "
            "Állítsd be a Streamlit Secrets-ben!"
        )
    return api_key


def fetch_live_matches() -> list[dict]:
    """
    Lekéri a Sportscore API-tól az összes jelenleg élő teniszmeccset.
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
            elif isinstance(data, dict):
                for key in ("data", "results", "events", "matches"):
                    if key in data and isinstance(data[key], list):
                        raw_list = data[key]
                        break
                if not raw_list:
                    raw_list = [data]

            print(f"-> [API Debug] A Sportscore összesen {len(raw_list)} nyers meccset adott vissza.")
            return raw_list
            
        except requests.exceptions.Timeout:
            if attempt == 0:
                time.sleep(1)
                continue
            print("Figyelem: A Sportscore válasza túl sokáig tartott (időtúllépés).")
            return []
        except requests.exceptions.RequestException as e:
            print(f"Hiba történt a hálózati kérés közben: {e}")
            return []
            
    return []


def _extract_name(obj) -> Optional[str]:
    if isinstance(obj, str):
        return obj
    if isinstance(obj, dict):
        for key in ("name", "player_name", "full_name", "short_name"):
            if key in obj:
                return obj[key]
    return None


def parse_match(raw: dict) -> MatchState:
    # Sportscore strukturális mezők kezelése
    home = raw.get("home_team", raw.get("home", {}))
    away = raw.get("away_team", raw.get("away", {}))

    player1 = _extract_name(home) or raw.get("player1")
    player2 = _extract_name(away) or raw.get("player2")

    # Score kinyerése Sportscore formátumból
    home_score = raw.get("home_score", {})
    away_score = raw.get("away_score", {})
    
    # Ha objektum vagy szám, formázzuk át olvashatóvá
    score = raw.get("score") or f"H: {home_score} | A: {away_score}"
    
    status = raw.get("status_string") or raw.get("status") or "Live"

    return MatchState(
        player1=player1,
        player2=player2,
        score=str(score),
        status=str(status),
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

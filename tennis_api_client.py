"""
tennis_api_client.py
---------------------
Sportscore Tennis API klienskód a Streamlit dashboardhoz.
"""

from __future__ import annotations

import os
import time
from dataclasses import dataclass, field
from typing import Optional
import streamlit as st
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
    try:
        if "RAPIDAPI_KEY" in st.secrets:
            return st.secrets["RAPIDAPI_KEY"]
    except Exception:
        pass
    
    api_key = os.environ.get("RAPIDAPI_KEY")
    if not api_key:
        raise RuntimeError("Hiányzik a RAPIDAPI_KEY a Streamlit Secrets-ből!")
    return api_key


def fetch_live_matches() -> list[dict]:
    headers = {
        "X-RapidAPI-Key": _get_api_key(),
        "X-RapidAPI-Host": API_HOST,
    }
    
    try:
        response = requests.get(LIVE_EVENTS_URL, headers=headers, timeout=30)
        
        if response.status_code != 200:
            st.error(f"API Hiba! Státuszkód: {response.status_code} - Válasz: {response.text[:200]}")
            return []
            
        data = response.json()
        
        # Itt látni fogjuk a képernyőn, hogy mit küldött pontosan a Sportscore
        st.write("🔍 DEBUG - Sportscore nyers válasz:", data)
        
        raw_list = []
        if isinstance(data, list):
            raw_list = data
        elif isinstance(data, dict):
            for key in ("data", "results", "events", "matches", "response"):
                if key in data and isinstance(data[key], list):
                    raw_list = data[key]
                    break
            if not raw_list:
                raw_list = [data]

        return raw_list
        
    except Exception as e:
        st.error(f"Hálózati vagy feldolgozási hiba: {e}")
        return []


def _extract_name(obj) -> Optional[str]:
    if isinstance(obj, str):
        return obj
    if isinstance(obj, dict):
        for key in ("name", "player_name", "full_name", "short_name", "slug"):
            if key in obj:
                return obj[key]
    return None


def parse_match(raw: dict) -> MatchState:
    home = raw.get("home_team", raw.get("home", {}))
    away = raw.get("away_team", raw.get("away", {}))

    player1 = _extract_name(home) or raw.get("player1") or "Ismeretlen játékos 1"
    player2 = _extract_name(away) or raw.get("player2") or "Ismeretlen játékos 2"

    home_score = raw.get("home_score", {})
    away_score = raw.get("away_score", {})
    score = raw.get("score") or f"Home: {home_score} | Away: {away_score}"
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
    raw_matches = fetch_live_matches()
    return [parse_match(raw) for raw in raw_matches]

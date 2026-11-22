"""API-Tennis adapter for the private ATP Intelligence research app.

- Mockable; never performs network calls during import.
- Uses POST form data, keeping APIkey out of URL and routine request logs.
- Never raises provider exception bodies or URLs (they may contain secrets).
- No claim that individual points carry a provider event-time timestamp.
- Provider-specific identifiers are NOT ATP ranking IDs.
"""
from __future__ import annotations

import json
import os
import time
from dataclasses import dataclass
from datetime import date, datetime, timezone
from typing import Any, Callable, Mapping
from urllib.error import HTTPError, URLError
from urllib.parse import urlencode
from urllib.request import Request, urlopen

API_BASE_URL = "https://api.api-tennis.com/tennis/"
SUPPORTED_METHODS = frozenset({
    "get_events", "get_tournaments", "get_fixtures",
    "get_livescore", "get_players", "get_H2H", "get_live_odds",
})
ALLOWED_PARAMETERS = frozenset({
    "event_type_key", "tournament_key", "tournament_season", "date_start",
    "date_stop", "match_key", "player_key", "first_player_key",
    "second_player_key", "timezone",
})


class TennisAPIError(RuntimeError):
    """Sanitized provider/transport error; does not expose credentials."""


@dataclass(frozen=True)
class ObservedMatch:
    """Observed snapshot, NOT a confirmed/validated point-by-point event log."""

    match_key: str
    first_player_key: str | None
    second_player_key: str | None
    first_player: str
    second_player: str
    tournament_key: str | None
    event_type: str
    qualification: bool | None
    server: str | None  # first / second / None
    status: str
    event_date: str | None  # provider's match date, not the current point time
    received_at: datetime
    point_games: tuple[dict[str, Any], ...]
    stats_available: bool
    raw: dict[str, Any]


def _optional_id(value: Any) -> str | None:
    if value is None or str(value).strip() == "":
        return None
    return str(value).strip()


def _qualification(value: Any) -> bool | None:
    if value is None or value == "":
        return None
    if str(value).casefold() in {"1", "true", "yes"}:
        return True
    if str(value).casefold() in {"0", "false", "no"}:
        return False
    return None


def normalize_match(raw: Mapping[str, Any], *, received_at: datetime | None = None) -> ObservedMatch:
    """Normalize provider fields, preserve raw data and observation timestamp."""
    if not isinstance(raw, Mapping):
        raise ValueError("match record must be a mapping")
    when = received_at or datetime.now(timezone.utc)
    if when.tzinfo is None or when.utcoffset() is None:
        raise ValueError("received_at must be timezone-aware")
    match_key = _optional_id(raw.get("event_key"))
    if not match_key:
        raise ValueError("missing event_key")
    served = str(raw.get("event_serve") or "").casefold().strip()
    server = ("first" if served in {"first player", "first"} else
              "second" if served in {"second player", "second"} else None)
    pbp = raw.get("pointbypoint")
    stats = raw.get("statistics")
    return ObservedMatch(
        match_key=match_key,
        first_player_key=_optional_id(raw.get("first_player_key")),
        second_player_key=_optional_id(raw.get("second_player_key")),
        first_player=str(raw.get("event_first_player") or ""),
        second_player=str(raw.get("event_second_player") or ""),
        tournament_key=_optional_id(raw.get("tournament_key")),
        event_type=str(raw.get("event_type_type") or ""),
        qualification=_qualification(raw.get("event_qualification")),
        server=server,
        status=str(raw.get("event_status") or ""),
        event_date=_optional_id(raw.get("event_date")),
        received_at=when.astimezone(timezone.utc),
        point_games=tuple(x for x in pbp if isinstance(x, dict)) if isinstance(pbp, list) else (),
        stats_available=bool(stats) if isinstance(stats, list) else False,
        raw=dict(raw),
    )


def verified_main_draw_matches(
    matches: list[ObservedMatch],
    *, approved_tournament_keys: set[str],
) -> list[ObservedMatch]:
    """Fail-closed ATP/GS scope filter requiring independently approved tournament keys.

    API's 'Atp Singles' alone does not identify ATP250/500/M1000/Finals/Slams.
    Missing qualification flags are NOT proof of a main-draw match; include them
    only if a separate validated match-level main-draw flag is later provided.
    """
    return [
        m for m in matches
        if m.tournament_key in approved_tournament_keys
        and m.event_type.casefold().strip() == "atp singles"
        and m.qualification is False
    ]


class TennisAPIClient:
    """Synchronous, retry-limited REST client with injectable transport."""

    def __init__(
        self, api_key: str | None = None, *,
        opener: Callable[..., Any] | None = None,
        sleeper: Callable[[float], None] | None = None,
        timeout: float = 15.0,
        max_attempts: int = 2,
    ):
        self._api_key = api_key if api_key is not None else os.environ.get("API_TENNIS_KEY", "")
        if not self._api_key or not self._api_key.strip():
            raise TennisAPIError("API_TENNIS_KEY is not configured on the server")
        if timeout <= 0 or max_attempts not in (1, 2, 3):
            raise ValueError("Invalid timeout or max_attempts")
        self.timeout = timeout
        self.max_attempts = max_attempts
        self._opener = opener or urlopen
        self._sleep = sleeper or time.sleep

    def _call(self, method: str, **params: Any) -> Any:
        if method not in SUPPORTED_METHODS:
            raise ValueError("Unrecognized API-Tennis method")
        unknown = set(params) - ALLOWED_PARAMETERS
        if unknown:
            raise ValueError("Unrecognized API-Tennis parameters")
        form = {"method": method, "APIkey": self._api_key}
        for key, value in params.items():
            if value is not None:
                form[key] = str(value)
        request = Request(
            API_BASE_URL,
            data=urlencode(form).encode("utf-8"),
            headers={"Content-Type": "application/x-www-form-urlencoded", "Accept": "application/json"},
            method="POST",
        )
        for attempt in range(self.max_attempts):
            try:
                with self._opener(request, timeout=self.timeout) as response:
                    payload = response.read()
                try:
                    document = json.loads(payload)
                except (ValueError, UnicodeError):
                    raise TennisAPIError("API-Tennis sent invalid JSON") from None
                if not isinstance(document, dict) or document.get("success") not in (1, "1", True):
                    raise TennisAPIError("API-Tennis request unsuccessful or unexpected schema")
                if "result" not in document:
                    raise TennisAPIError("API-Tennis response missing result")
                return document["result"]
            except TennisAPIError:
                raise
            except HTTPError as exc:
                if exc.code not in (429, 500, 502, 503, 504) or attempt + 1 == self.max_attempts:
                    raise TennisAPIError("API-Tennis HTTP request failed") from None
            except (URLError, TimeoutError, OSError):
                if attempt + 1 == self.max_attempts:
                    raise TennisAPIError("API-Tennis transport failed") from None
            self._sleep(0.5 * 2**attempt)
        raise TennisAPIError("API-Tennis request failed")

    def events(self) -> list[dict[str, Any]]:
        result = self._call("get_events")
        return self._list(result)

    def tournaments(self, event_type_key: str | None = None) -> list[dict[str, Any]]:
        return self._list(self._call("get_tournaments", event_type_key=event_type_key))

    def fixtures(
        self, start: date, stop: date, *,
        event_type_key: str | None = None, match_key: str | None = None,
    ) -> list[dict[str, Any]]:
        if not isinstance(start, date) or not isinstance(stop, date) or stop < start:
            raise ValueError("Invalid date interval")
        return self._list(self._call(
            "get_fixtures", date_start=start.isoformat(), date_stop=stop.isoformat(),
            event_type_key=event_type_key, match_key=match_key,
        ))

    def livescore(self, *, event_type_key: str | None = None, match_key: str | None = None) -> list[ObservedMatch]:
        observed = datetime.now(timezone.utc)
        raw = self._list(self._call("get_livescore", event_type_key=event_type_key, match_key=match_key))
        return [normalize_match(m, received_at=observed) for m in raw]

    def players(self, player_key: str) -> list[dict[str, Any]]:
        if not str(player_key).strip():
            raise ValueError("player_key is required")
        return self._list(self._call("get_players", player_key=player_key))

    def h2h(self, first_player_key: str, second_player_key: str) -> dict[str, Any]:
        if not first_player_key or not second_player_key or first_player_key == second_player_key:
            raise ValueError("Two different provider player keys required")
        result = self._call("get_H2H", first_player_key=first_player_key, second_player_key=second_player_key)
        if not isinstance(result, dict):
            raise TennisAPIError("API-Tennis H2H schema mismatch")
        return result

    def live_odds(self, *, match_key: str | None = None) -> Any:
        """Optional: provider plan may not include live odds."""
        return self._call("get_live_odds", match_key=match_key)

    @staticmethod
    def _list(result: Any) -> list[dict[str, Any]]:
        if not isinstance(result, list) or any(not isinstance(x, dict) for x in result):
            raise TennisAPIError("API-Tennis list response schema mismatch")
        return result

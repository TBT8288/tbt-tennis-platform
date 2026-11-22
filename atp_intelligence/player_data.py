"""Read-only, source-preserving ATP Top150 profile and two-season H2H loaders.

The historical roster and scouting files are a DATE-LOCKED snapshot, not a
live feed. Missing values remain missing; PR #13 candidates are not approved
master values. Aggregated H2H cannot be used for look-ahead-safe backtesting
before its source cutoff.
"""
from __future__ import annotations

import csv
from dataclasses import dataclass
from datetime import date
from pathlib import Path

from .roster import normalize_name

ROOT = Path(__file__).resolve().parents[1]
MASTER_PATH = ROOT / "research/player_profiles/atp_top150_profile_register_2026_11_21.csv"
PHYSICAL_CANDIDATES = ROOT / "research/player_profiles/ATP_TOP150_2026_11_22_PHYSICAL_MISSING_CANDIDATES.csv"
BACKHAND_CANDIDATES = ROOT / "research/player_profiles/ATP_TOP150_2026_11_22_BACKHAND_MISSING_CANDIDATES.csv"
H2H_PATH = ROOT / "research/player_profiles/TOP150_H2H_2025_2026_THROUGH_2026_11_15.csv"
H2H_CUTOFF = date(2026, 11, 15)


def _read_csv(path: Path) -> list[dict[str, str]]:
    with path.open(encoding="utf-8-sig", newline="") as f:
        return list(csv.DictReader(f))


def parse_record_date(raw: str) -> date:
    """Accept ISO-date, ISO datetime or legacy YYYYMMDD, reject guesswork."""
    if len(raw) == 8 and raw.isascii() and raw.isdigit():
        return date(int(raw[:4]), int(raw[4:6]), int(raw[6:8]))
    if len(raw) >= 10 and raw[4] == "-" and raw[7] == "-":
        return date.fromisoformat(raw[:10])
    raise ValueError("Unrecognized match date format")


@dataclass(frozen=True)
class CandidateValue:
    value: str
    source_url: str
    checked_on: str
    status: str = "PROPOSED_NOT_VERIFIED"


@dataclass(frozen=True)
class PlayerView:
    rank: int
    name: str
    snapshot: dict[str, str]
    candidates: dict[str, CandidateValue]

    def field(self, key: str) -> tuple[str | None, str]:
        """(value, provenance): master_verified / candidate_only / missing."""
        current = self.snapshot.get(key, "")
        if current != "":
            return current, "master_snapshot"
        candidate = self.candidates.get(key)
        if candidate:
            return candidate.value, "candidate_only"
        return None, "missing"


class Top150Profiles:
    """Immutable-ish read-only snapshot; never mutates source CSVs."""

    def __init__(
        self, path: Path = MASTER_PATH, *,
        physical: Path = PHYSICAL_CANDIDATES,
        backhand: Path = BACKHAND_CANDIDATES,
    ):
        records = _read_csv(Path(path))
        if len(records) != 150:
            raise ValueError("Top150 master must contain exactly 150 records")
        ranks = {int(x["rank"]) for x in records}
        if ranks != set(range(1, 151)):
            raise ValueError("Top150 master ranks are not unique and contiguous")
        self.players: dict[str, PlayerView] = {}
        pending: dict[str, dict[str, CandidateValue]] = {}
        for extra_path, columns in ((physical, ("height_cm", "weight_kg")), (backhand, ("backhand",))):
            if not Path(extra_path).exists():
                continue
            seen_overlay: set[str] = set()
            for row in _read_csv(Path(extra_path)):
                key = normalize_name(row["player"])
                if key in seen_overlay:
                    raise ValueError("Duplicate candidate row")
                seen_overlay.add(key)
                if not row["source_url"].startswith("https://"):
                    raise ValueError("Missing candidate source URL")
                date.fromisoformat(row["checked_on"])
                for field in columns:
                    value = row.get(field, "").strip()
                    if value:
                        pending.setdefault(key, {})[field] = CandidateValue(
                            value=value, source_url=row["source_url"],
                            checked_on=row["checked_on"]
                        )
        for row in records:
            key = normalize_name(row["player"])
            if not key or key in self.players:
                raise ValueError("Duplicate player identity")
            self.players[key] = PlayerView(
                rank=int(row["rank"]), name=row["player"], snapshot=dict(row),
                candidates=pending.get(key, {}),
            )
        if set(pending) - set(self.players):
            raise ValueError("Candidate references a player outside the Top150 snapshot")

    def find(self, name: str) -> PlayerView | None:
        return self.players.get(normalize_name(name))

    def audit(self) -> dict[str, int]:
        result: dict[str, int] = {"players": len(self.players)}
        for field in ("height_cm", "weight_kg", "backhand", "year_2026_wins", "year_2026_losses"):
            result[field + "_master"] = sum(bool(p.snapshot.get(field)) for p in self.players.values())
            result[field + "_with_candidates"] = sum(p.field(field)[0] is not None for p in self.players.values())
        return result


@dataclass(frozen=True)
class H2HSnapshot:
    player_a: str
    player_b: str
    wins_a: int
    wins_b: int
    matches: int
    last_observed_match: date | None
    archive_cutoff: date
    data_stale: bool
    """Historical observed counts, NOT estimated match-win probabilities."""


class TwoSeasonH2H:
    """Aggregated counts from the 2025/26 archive, never same-day live data."""

    def __init__(self, path: Path = H2H_PATH, *, cutoff: date = H2H_CUTOFF):
        self.cutoff = cutoff
        self.rows: dict[tuple[str, str], dict[str, str]] = {}
        for row in _read_csv(Path(path)):
            a, b = normalize_name(row["player_a"]), normalize_name(row["player_b"])
            if a == b or not a or not b:
                raise ValueError("Invalid pair in H2H archive")
            pair = tuple(sorted((a, b)))
            if pair in self.rows:
                raise ValueError("Duplicate pair in H2H archive")
            if parse_record_date(row["latest_event_date_observed"]) > cutoff:
                raise ValueError("H2H event occurred after recorded source cutoff")
            self.rows[pair] = row

    def for_match(self, player_a: str, player_b: str, *, as_of: date) -> H2HSnapshot:
        """Report counts known strictly BEFORE prediction day.

        For historical times on/before archive cutoff the aggregate is unsafe:
        we cannot know which of its matches had happened at that time.
        """
        if not isinstance(as_of, date):
            raise TypeError("as_of must be a date")
        if as_of <= self.cutoff:
            raise ValueError("Aggregate H2H risks future leakage before source cutoff; use raw dated matches")
        a, b = normalize_name(player_a), normalize_name(player_b)
        if not a or not b or a == b:
            raise ValueError("Two different players required")
        row = self.rows.get(tuple(sorted((a, b))))
        if row is None:
            return H2HSnapshot(player_a, player_b, 0, 0, 0, None, self.cutoff, True)
        reverse = a != normalize_name(row["player_a"])
        wa = wb = 0
        for year in (2025, 2026):
            if as_of.year - 1 <= year <= as_of.year:
                wa += int(row["a_w_2025"] if year == 2025 else row["a_w_2026_to_nov15"])
                wb += int(row["b_w_2025"] if year == 2025 else row["b_w_2026_to_nov15"])
        if reverse:
            wa, wb = wb, wa
        last = parse_record_date(row["latest_event_date_observed"])
        return H2HSnapshot(
            player_a, player_b, wa, wb, wa + wb, last,
            self.cutoff, self.cutoff < as_of,
        )

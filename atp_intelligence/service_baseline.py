"""Transparent B0 server-point prior from historical first/second serve statistics.

This is a descriptive/engineering baseline, not a calibrated opponent-adjusted
prediction. The source CSV cutoff is 2026-11-15; predictions on/before that
date must NOT use those aggregated full-cutoff statistics (look-ahead).
"""
from __future__ import annotations

import csv
from dataclasses import dataclass
from datetime import date
from pathlib import Path

from .roster import normalize_name

DEFAULT_EVIDENCE = (
    Path(__file__).resolve().parents[1] /
    "research/player_profiles/TOP150_EVIDENCE_PROFILE_REGISTER_2026_11_21.csv"
)
CUTOFF = date(2026, 11, 15)


def _percent(s: str) -> float | None:
    if not s:
        return None
    try:
        x = float(s.strip().rstrip("%")) / 100.0
    except ValueError:
        return None
    return x if 0 <= x <= 1 else None


@dataclass(frozen=True)
class ServerPointPrior:
    player: str
    source_year: int
    service_point_chance: float
    first_serve_in: float
    first_serve_points_won: float
    second_serve_points_won: float
    sample_matches: int
    source_cutoff: date
    label: str = "unadjusted_archive_baseline_not_validated"


class ServiceBaselineArchive:
    def __init__(self, path: str | Path = DEFAULT_EVIDENCE, *, cutoff: date = CUTOFF):
        self.cutoff = cutoff
        with Path(path).open(encoding="utf-8-sig", newline="") as f:
            entries = list(csv.DictReader(f))
        if len(entries) != 150:
            raise ValueError("Expected 150 evidence profiles")
        self._rows = {}
        for row in entries:
            key = normalize_name(row["name"])
            if not key or key in self._rows:
                raise ValueError("Duplicate / invalid player")
            self._rows[key] = row

    def get(self, player: str, *, as_of: date) -> ServerPointPrior | None:
        if not isinstance(as_of, date):
            raise TypeError("as_of must be a date")
        if as_of <= self.cutoff:
            raise ValueError("Snapshot statistics could include future results: use dated raw match data")
        row = self._rows.get(normalize_name(player))
        if row is None:
            return None
        for year in (2026, 2025):
            if not as_of.year - 1 <= year <= as_of.year:
                continue
            if year == 2026:
                fields = ("first_serve_in_pct_2026", "first_won_pct_2026", "second_won_pct_2026")
                sample_field = "serve_stat_sample_2026"
            else:
                fields = ("first_in_2025", "first_won_2025", "second_won_2025")
                sample_field = "serve_sample_2025"
            vals = [_percent(row.get(key, "")) for key in fields]
            if any(v is None for v in vals):
                continue
            try:
                matches = int(row.get(sample_field, "") or 0)
            except ValueError:
                continue
            if matches <= 0:
                continue
            first_in, win_first, win_second = vals
            p = first_in * win_first + (1.0 - first_in) * win_second
            return ServerPointPrior(
                player=row["name"], source_year=year,
                service_point_chance=p, first_serve_in=first_in,
                first_serve_points_won=win_first,
                second_serve_points_won=win_second,
                sample_matches=matches,
                source_cutoff=self.cutoff
            )
        return None

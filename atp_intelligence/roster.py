"""Scope gate for the private ATP Intelligence player database.

Top-150 ATP singles rank is the profile criterion; season main-draw statistics may be unavailable.
Ranks, points and wins/losses are a dated snapshot, not live player status.
"""
from __future__ import annotations

import csv
import unicodedata
from dataclasses import dataclass
from datetime import date
from pathlib import Path

DEFAULT_ROSTER_PATH = (
    Path(__file__).resolve().parents[1] / "research" / "rosters" / "atp_top150_2026_11_16.csv"
)


def normalize_name(name: str) -> str:
    plain = unicodedata.normalize("NFKD", name)
    return "".join(c for c in plain.casefold() if c.isascii() and c.isalnum())


@dataclass(frozen=True)
class RankedPlayer:
    rank: int
    name: str
    country: str
    ranking_points: int
    ranking_date: str
    main_draw_wins: int | None
    main_draw_losses: int | None


class ATPTop150:
    """Dated list of 150 ranked ATP male singles players with verified source metadata."""

    def __init__(self, path: str | Path = DEFAULT_ROSTER_PATH):
        self.path = Path(path)
        with self.path.open("r", encoding="utf-8-sig", newline="") as f:
            records = list(csv.DictReader(f))
        if len(records) != 150:
            raise ValueError(f"Expected exactly 150 ranked players, got {len(records)}")
        self.players: list[RankedPlayer] = []
        self._lookup: dict[str, RankedPlayer] = {}
        snapshot_dates = set()
        ranks: set[int] = set()
        for row in records:
            rank = int(row["rank"])
            raw_wins, raw_losses = row["season_main_draw_wins"], row["season_main_draw_losses"]
            if bool(raw_wins) != bool(raw_losses):
                raise ValueError(f"Incomplete season statistics for rank {rank}")
            wins = int(raw_wins) if raw_wins else None
            losses = int(raw_losses) if raw_losses else None
            if not 1 <= rank <= 150 or rank in ranks:
                raise ValueError("Top-150 ranks must be unique between 1 and 150")
            if row["ranking_crosschecked"] not in {"verified", "single_rank_source"}:
                raise ValueError(f"Untraceable ranking provenance at rank {rank}")
            if row["season_stats_verified"] == "verified":
                if wins is None or losses is None or wins < 0 or losses < 0:
                    raise ValueError(f"Incorrect verified season statistics at rank {rank}")
            elif row["season_stats_verified"] == "not_yet_verified":
                if wins is not None or losses is not None:
                    raise ValueError(f"Unverified season statistics must be blank at rank {rank}")
            else:
                raise ValueError(f"Invalid season statistics status at rank {rank}")
            date.fromisoformat(row["ranking_date"])
            if int(row["ranking_points"]) < 0:
                raise ValueError("Ranking points cannot be negative")
            p = RankedPlayer(
                rank=rank,
                name=row["player"],
                country=row["country"],
                ranking_points=int(row["ranking_points"]),
                ranking_date=row["ranking_date"],
                main_draw_wins=wins,
                main_draw_losses=losses,
            )
            normalized = normalize_name(p.name)
            if not normalized or normalized in self._lookup:
                raise ValueError(f"Invalid or duplicate player name: {p.name}")
            self._lookup[normalized] = p
            self.players.append(p)
            ranks.add(rank)
            snapshot_dates.add(p.ranking_date)
        if ranks != set(range(1, 151)) or len(snapshot_dates) != 1:
            raise ValueError("Ranking must be an uninterrupted top 150 from a single snapshot")
        self.players.sort(key=lambda p: p.rank)
        self.as_of = next(iter(snapshot_dates))

    def find(self, name: str) -> RankedPlayer | None:
        return self._lookup.get(normalize_name(name))

    def eligible(self, name: str) -> bool:
        return self.find(name) is not None

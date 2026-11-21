"""Source-backed expert observations for CURRENT ATP Top-100 players only.

Historical articles/podcasts are research leads. Never treat past opinions as
today's player abilities, internal mental states or validated predictions.
Only reviewed CSV metadata and brief attributed paraphrases are imported.
"""
from __future__ import annotations

import argparse
import csv
import sqlite3
from datetime import date
from pathlib import Path

from .roster import ATPTop100, DEFAULT_ROSTER_PATH

VALID_STATUSES = frozenset({
    "competitive_2026_atp_or_challenger",
    "retired_confirmed",
    "on_break_not_retired",
    "limited_2026_activity_atp_status_uncertain",
})


def _iso_date(value: str) -> str:
    return date.fromisoformat(value).isoformat()


def _load_rows(path: Path) -> list[dict[str, str]]:
    with path.open("r", encoding="utf-8-sig", newline="") as f:
        rows = list(csv.DictReader(f))
    if not rows:
        raise ValueError(f"empty archive CSV: {path}")
    return rows


class ExpertArchive:
    """SQLite: validated Top100 roster plus historical, attributed observations."""

    def __init__(self, db_path: str = ":memory:") -> None:
        if db_path != ":memory:":
            Path(db_path).parent.mkdir(parents=True, exist_ok=True)
        self.db = sqlite3.connect(db_path)
        self.db.execute("PRAGMA foreign_keys = ON")
        self.db.executescript("""
            CREATE TABLE IF NOT EXISTS atp_roster (
                rank INTEGER PRIMARY KEY CHECK (rank BETWEEN 1 AND 100),
                player TEXT NOT NULL UNIQUE,
                country TEXT NOT NULL,
                ranking_points INTEGER NOT NULL,
                ranking_date TEXT NOT NULL,
                main_draw_wins INTEGER NOT NULL,
                main_draw_losses INTEGER NOT NULL
            );
            CREATE TABLE IF NOT EXISTS expert_sources (
                source_id TEXT PRIMARY KEY,
                published_date TEXT NOT NULL,
                author TEXT NOT NULL,
                type TEXT NOT NULL,
                title TEXT NOT NULL,
                url TEXT NOT NULL,
                content_access TEXT NOT NULL,
                rights_note TEXT NOT NULL
            );
            CREATE TABLE IF NOT EXISTS expert_player_mentions (
                player TEXT NOT NULL,
                source_id TEXT NOT NULL REFERENCES expert_sources(source_id),
                status TEXT NOT NULL,
                status_evidence TEXT NOT NULL,
                status_source_url TEXT NOT NULL,
                note TEXT NOT NULL,
                status_as_of TEXT NOT NULL,
                PRIMARY KEY (player, source_id)
            );
            CREATE INDEX IF NOT EXISTS expert_mention_status
                ON expert_player_mentions (status, status_as_of);
            CREATE TABLE IF NOT EXISTS expert_observations (
                observation_id TEXT PRIMARY KEY,
                source_id TEXT NOT NULL REFERENCES expert_sources(source_id),
                player TEXT NOT NULL,
                observation_date TEXT NOT NULL,
                category TEXT NOT NULL,
                paraphrase_hu TEXT NOT NULL,
                attribution TEXT NOT NULL,
                verification TEXT NOT NULL,
                usable_as_hypothesis TEXT NOT NULL,
                recency TEXT NOT NULL
            );
            CREATE INDEX IF NOT EXISTS expert_obs_player
                ON expert_observations(player, observation_date);
        """)
        self.db.commit()

    def import_directory(
        self,
        folder: str | Path,
        roster_path: str | Path = DEFAULT_ROSTER_PATH,
    ) -> dict[str, int]:
        """Import only players allowed by a dated, checked Top-100 roster.

        Additional source references are permitted, but ONLY eligible players
        receive a persistent player mention or observation record.
        """
        folder = Path(folder)
        roster = ATPTop100(roster_path)
        sources = _load_rows(folder / "sources.csv")
        players = _load_rows(folder / "player_mentions_2026_11_21.csv")
        observations = _load_rows(folder / "historical_observations.csv")
        extra_sources = folder / "current_sources.csv"
        extra_observations = folder / "current_atp_observations.csv"
        if extra_sources.exists() and extra_observations.exists():
            sources += _load_rows(extra_sources)
            observations += _load_rows(extra_observations)
        elif extra_sources.exists() != extra_observations.exists():
            raise ValueError("Current sources and observations must be imported together")

        accepted_players = [p for p in players if roster.eligible(p["player"])]
        accepted_obs = [o for o in observations if roster.eligible(o["player"])]
        accepted_names = {p["player"] for p in accepted_players} | {
            o["player"] for o in accepted_obs
        }

        with self.db:
            # Rebuild scope on every import. This also removes legacy records
            # for now-ineligible players from an existing persistent DB.
            self.db.execute("DELETE FROM expert_observations")
            self.db.execute("DELETE FROM expert_player_mentions")
            self.db.execute("DELETE FROM atp_roster")
            for player in roster.players:
                self.db.execute(
                    """INSERT INTO atp_roster VALUES (?,?,?,?,?,?,?)""",
                    (
                        player.rank, player.name, player.country, player.ranking_points,
                        player.ranking_date, player.main_draw_wins, player.main_draw_losses
                    )
                )
            for row in sources:
                _iso_date(row["published_date"])
                self.db.execute(
                    """INSERT OR IGNORE INTO expert_sources VALUES (?,?,?,?,?,?,?,?)""",
                    tuple(row[k] for k in (
                        "source_id", "published_date", "author", "type", "title", "url",
                        "content_access", "rights_note"
                    ))
                )
            for row in accepted_players:
                _iso_date(row["status_as_of"])
                if row["status"] not in VALID_STATUSES:
                    raise ValueError(f"unknown status for {row['player']}: {row['status']}")
                self.db.execute(
                    """INSERT INTO expert_player_mentions VALUES (?,?,?,?,?,?,?)""",
                    tuple(row[k] for k in (
                        "player", "source_id", "status", "status_evidence",
                        "status_source_url", "note", "status_as_of"
                    ))
                )
            for row in accepted_obs:
                _iso_date(row["observation_date"])
                self.db.execute(
                    """INSERT INTO expert_observations VALUES (?,?,?,?,?,?,?,?,?,?)""",
                    tuple(row[k] for k in (
                        "observation_id", "source_id", "player", "observation_date",
                        "category", "paraphrase_hu", "attribution", "verification",
                        "usable_as_hypothesis", "recency"
                    ))
                )
        return {
            "roster": len(roster.players),
            "sources": len(sources),
            "player_mentions": len(accepted_players),
            "observations": len(accepted_obs),
            "excluded_mentions": len(players) - len(accepted_players),
            "excluded_observations": len(observations) - len(accepted_obs),
        }

    def get_roster(self) -> list[tuple[int, str, int, str]]:
        return self.db.execute(
            """SELECT rank,player,ranking_points,ranking_date
               FROM atp_roster ORDER BY rank"""
        ).fetchall()

    def get_status(self, player: str) -> list[tuple[str, str, str, str]]:
        """Snapshot labels, not present-day career determinations."""
        return self.db.execute(
            """SELECT status,status_evidence,status_source_url,status_as_of
               FROM expert_player_mentions WHERE player=? ORDER BY status_as_of DESC""",
            (player,)
        ).fetchall()

    def get_observations(self, player: str) -> list[tuple[str, str, str, str]]:
        """Attributed historical notes, their uncertainty and original link."""
        return self.db.execute(
            """SELECT o.observation_date,o.paraphrase_hu,o.verification,s.url
               FROM expert_observations o
               JOIN expert_sources s ON s.source_id=o.source_id
               WHERE o.player=? ORDER BY o.observation_date DESC""",
            (player,)
        ).fetchall()

    def close(self) -> None:
        self.db.close()


def main() -> None:
    parser = argparse.ArgumentParser(description="Import source-backed ATP Top-100 expert archive")
    parser.add_argument("--folder", default="research/expert_archives")
    parser.add_argument("--roster", default=str(DEFAULT_ROSTER_PATH))
    parser.add_argument("--db", default="data/expert_archive.sqlite3")
    args = parser.parse_args()
    store = ExpertArchive(args.db)
    try:
        counts = store.import_directory(args.folder, args.roster)
        print("Imported: " + ", ".join(f"{k}={v}" for k, v in counts.items()))
        print("Only current Top-100 ATP players are eligible for player records.")
    finally:
        store.close()


if __name__ == "__main__":
    main()

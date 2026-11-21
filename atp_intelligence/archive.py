"""Minimal sourced-expert-archive importer. No analysis or player status inference.

The canonical reviewed seed files live in research/expert_archives/. Database
tables preserve all provenance and date/status labels, and must not be treated
as an automatically refreshed injury, psychological or current-form feed.
"""
from __future__ import annotations

import argparse
import csv
import sqlite3
from datetime import date
from pathlib import Path

VALID_STATUSES = frozenset({
    "competitive_2026_atp_or_challenger",
    "retired_confirmed",
    "on_break_not_retired",
    "limited_2026_activity_atp_status_uncertain",
})


def _iso_date(value: str) -> str:
    # Fail closed rather than accept malformed or untraceable historical dates.
    return date.fromisoformat(value).isoformat()


def _load_rows(path: Path) -> list[dict[str, str]]:
    with path.open("r", encoding="utf-8-sig", newline="") as f:
        rows = list(csv.DictReader(f))
    if not rows:
        raise ValueError(f"empty archive CSV: {path}")
    return rows


class ExpertArchive:
    """Local SQLite archive for source-linked historical tennis observations."""

    def __init__(self, db_path: str = ":memory:") -> None:
        if db_path != ":memory:":
            Path(db_path).parent.mkdir(parents=True, exist_ok=True)
        self.db = sqlite3.connect(db_path)
        self.db.execute("PRAGMA foreign_keys = ON")
        self.db.executescript("""
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

    def import_directory(self, folder: str | Path) -> dict[str, int]:
        folder = Path(folder)
        sources = _load_rows(folder / "sources.csv")
        players = _load_rows(folder / "player_mentions_2026_11_21.csv")
        observations = _load_rows(folder / "historical_observations.csv")
        with self.db:
            for row in sources:
                _iso_date(row["published_date"])
                self.db.execute(
                    """INSERT OR REPLACE INTO expert_sources VALUES (?,?,?,?,?,?,?,?)""",
                    tuple(row[k] for k in (
                        "source_id", "published_date", "author", "type", "title", "url",
                        "content_access", "rights_note"
                    ))
                )
            for row in players:
                _iso_date(row["status_as_of"])
                if row["status"] not in VALID_STATUSES:
                    raise ValueError(f"unknown status for {row['player']}: {row['status']}")
                self.db.execute(
                    """INSERT OR REPLACE INTO expert_player_mentions VALUES (?,?,?,?,?,?,?)""",
                    tuple(row[k] for k in (
                        "player", "source_id", "status", "status_evidence",
                        "status_source_url", "note", "status_as_of"
                    ))
                )
            for row in observations:
                _iso_date(row["observation_date"])
                self.db.execute(
                    """INSERT OR REPLACE INTO expert_observations VALUES (?,?,?,?,?,?,?,?,?,?)""",
                    tuple(row[k] for k in (
                        "observation_id", "source_id", "player", "observation_date",
                        "category", "paraphrase_hu", "attribution", "verification",
                        "usable_as_hypothesis", "recency"
                    ))
                )
        return {"sources": len(sources), "players": len(players), "observations": len(observations)}

    def get_status(self, player: str) -> list[tuple[str, str, str, str]]:
        """Snapshot labels, not present-day career determinations."""
        return self.db.execute(
            """SELECT status, status_evidence, status_source_url, status_as_of
               FROM expert_player_mentions WHERE player=? ORDER BY status_as_of DESC""",
            (player,)
        ).fetchall()

    def get_observations(self, player: str) -> list[tuple[str, str, str, str]]:
        """Return attributed notes with date, verification and original source URL."""
        return self.db.execute(
            """SELECT o.observation_date, o.paraphrase_hu, o.verification, s.url
               FROM expert_observations o
               JOIN expert_sources s ON s.source_id=o.source_id
               WHERE o.player=? ORDER BY o.observation_date DESC""",
            (player,)
        ).fetchall()

    def close(self) -> None:
        self.db.close()


def main() -> None:
    parser = argparse.ArgumentParser(description="Import historic cited tennis expert archives")
    parser.add_argument(
        "--folder", default="research/expert_archives",
        help="Folder containing the reviewed expert CSV files",
    )
    parser.add_argument(
        "--db", default="data/expert_archive.sqlite3",
        help="Output local SQLite DB (gitignored, never commit credentials)",
    )
    args = parser.parse_args()
    store = ExpertArchive(args.db)
    try:
        counts = store.import_directory(args.folder)
        print(f"Imported {counts['sources']} sources, {counts['players']} player mentions, "
              f"{counts['observations']} historical observations into {args.db}")
    finally:
        store.close()


if __name__ == "__main__":
    main()

"""Store successive API match snapshots with RECEIPT timestamps, not invented point event times.

An API result may contain many points but no trustworthy point-level timestamps.
We save immutable raw-version snapshots; repeated snapshots update last_seen only.
No secret or API request URL is persisted. This local store is not an inference
engine and does not convert old points into fake realtime point events.
"""
from __future__ import annotations

import hashlib
import json
import sqlite3
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

from .api_tennis import ObservedMatch

DEFAULT_DB = Path(__file__).resolve().parents[1] / "data/private/atp_live_snapshots.sqlite3"


class LiveSnapshotStore:
    def __init__(self, path: str | Path = DEFAULT_DB):
        if str(path) != ":memory:":
            Path(path).parent.mkdir(parents=True, exist_ok=True)
        self.db = sqlite3.connect(str(path))
        self.db.execute("PRAGMA foreign_keys=ON")
        self.db.executescript("""
            CREATE TABLE IF NOT EXISTS live_snapshots (
                match_key TEXT NOT NULL,
                fingerprint TEXT NOT NULL,
                first_received_at TEXT NOT NULL,
                last_received_at TEXT NOT NULL,
                observations INTEGER NOT NULL DEFAULT 1,
                first_player_key TEXT,
                second_player_key TEXT,
                status TEXT NOT NULL,
                provider_event_date TEXT,
                has_point_level_event_timestamps INTEGER NOT NULL DEFAULT 0,
                point_game_count INTEGER NOT NULL,
                payload_json TEXT NOT NULL,
                PRIMARY KEY (match_key, fingerprint)
            );
            CREATE INDEX IF NOT EXISTS idx_snapshots_time
              ON live_snapshots(match_key, first_received_at);
        """)
        self.db.commit()

    @staticmethod
    def _fingerprint(raw: dict[str, Any]) -> tuple[str, str]:
        # Schema may contain sensitive supplemental fields; only ingest the
        # standardized, documented match payload—not outgoing client headers.
        payload = json.dumps(raw, ensure_ascii=False, sort_keys=True, separators=(",", ":"), default=str)
        return hashlib.sha256(payload.encode("utf-8")).hexdigest(), payload

    def ingest(self, match: ObservedMatch) -> bool:
        """Return True only on a genuinely new snapshot content version."""
        if match.received_at.tzinfo is None or match.received_at.utcoffset() is None:
            raise ValueError("received_at requires timezone")
        stamp = match.received_at.astimezone(timezone.utc).isoformat()
        fingerprint, payload = self._fingerprint(match.raw)
        with self.db:
            cursor = self.db.execute("""
                INSERT OR IGNORE INTO live_snapshots (
                    match_key, fingerprint, first_received_at, last_received_at,
                    observations, first_player_key, second_player_key, status,
                    provider_event_date, has_point_level_event_timestamps,
                    point_game_count, payload_json
                ) VALUES (?,?,?,?,1,?,?,?,?,0,?,?)
            """, (
                match.match_key, fingerprint, stamp, stamp, match.first_player_key,
                match.second_player_key, match.status, match.event_date,
                len(match.point_games), payload,
            ))
            inserted = cursor.rowcount == 1
            if not inserted:
                self.db.execute("""
                    UPDATE live_snapshots
                    SET observations=observations+1,
                        last_received_at=CASE WHEN last_received_at < ? THEN ? ELSE last_received_at END
                    WHERE match_key=? AND fingerprint=?
                """, (stamp, stamp, match.match_key, fingerprint))
        return inserted

    def history(self, match_key: str) -> list[tuple[str, str, int, int, str]]:
        """Receipt-first metadata: (first, last, observations, games, status)."""
        return self.db.execute("""
            SELECT first_received_at,last_received_at,observations,point_game_count,status
            FROM live_snapshots WHERE match_key=?
            ORDER BY first_received_at, fingerprint
        """, (str(match_key),)).fetchall()

    def close(self):
        self.db.close()

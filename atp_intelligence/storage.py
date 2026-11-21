"""SQLite event/prediction history with UTC timestamps and idempotent event IDs.

Local prototype only. The application needs a controlled API ingestion process
before this history can be used as evidence of live predictive performance.
"""
import sqlite3
from pathlib import Path
from .events import PointEvent, Prediction


class EventStore:
    def __init__(self, path: str = ":memory:"):
        if path != ":memory:":
            Path(path).parent.mkdir(parents=True, exist_ok=True)
        self.connection = sqlite3.connect(path)
        self.connection.execute("PRAGMA foreign_keys=ON")
        self.connection.executescript("""
            CREATE TABLE IF NOT EXISTS point_events (
                match_id TEXT NOT NULL,
                event_id TEXT NOT NULL,
                server_id TEXT NOT NULL,
                winner_id TEXT NOT NULL,
                event_time TEXT NOT NULL,
                ingested_at TEXT NOT NULL,
                source TEXT NOT NULL,
                PRIMARY KEY (match_id, event_id)
            );
            CREATE INDEX IF NOT EXISTS idx_points_time ON point_events(match_id, event_time);
            CREATE TABLE IF NOT EXISTS predictions (
                prediction_id TEXT PRIMARY KEY,
                match_id TEXT NOT NULL,
                target TEXT NOT NULL,
                probability REAL NOT NULL CHECK (probability BETWEEN 0 AND 1),
                model_version TEXT NOT NULL,
                created_at TEXT NOT NULL,
                evidence_cutoff TEXT,
                source TEXT NOT NULL
            );
            CREATE INDEX IF NOT EXISTS idx_preds_time ON predictions(match_id, created_at);
        """)
        self.connection.commit()

    def add_point(self, point: PointEvent) -> bool:
        with self.connection:
            result = self.connection.execute(
                """INSERT OR IGNORE INTO point_events
                   (match_id,event_id,server_id,winner_id,event_time,ingested_at,source)
                   VALUES (?,?,?,?,?,?,?)""",
                (point.match_id,point.event_id,point.server_id,point.winner_id,
                 point.event_time.isoformat(),point.ingested_at.isoformat(),point.source)
            )
        return result.rowcount == 1

    def add_prediction(self, prediction: Prediction) -> bool:
        with self.connection:
            result = self.connection.execute(
                """INSERT OR IGNORE INTO predictions
                   (prediction_id,match_id,target,probability,model_version,created_at,evidence_cutoff,source)
                   VALUES (?,?,?,?,?,?,?,?)""",
                (prediction.prediction_id,prediction.match_id,prediction.target,
                 prediction.probability,prediction.model_version,prediction.created_at.isoformat(),
                 prediction.evidence_cutoff.isoformat() if prediction.evidence_cutoff else None,
                 prediction.source)
            )
        return result.rowcount == 1

    def points_for_match(self, match_id: str) -> list[tuple]:
        return self.connection.execute(
            """SELECT event_id,server_id,winner_id,event_time,ingested_at,source
               FROM point_events WHERE match_id=? ORDER BY event_time,event_id""", (match_id,)
        ).fetchall()

    def predictions_for_match(self, match_id: str) -> list[tuple]:
        return self.connection.execute(
            """SELECT prediction_id,target,probability,model_version,created_at,evidence_cutoff,source
               FROM predictions WHERE match_id=? ORDER BY created_at,prediction_id""", (match_id,)
        ).fetchall()

    def close(self) -> None:
        self.connection.close()

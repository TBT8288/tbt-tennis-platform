"""Typed observations and immutable, UTC-time-stamped prediction records."""
from dataclasses import dataclass, field
from datetime import datetime, timezone
from math import isfinite
from typing import Optional


def utc_now() -> datetime:
    return datetime.now(timezone.utc)


def _valid_time(value: datetime) -> None:
    if not isinstance(value, datetime) or value.tzinfo is None or value.utcoffset() is None:
        raise ValueError("timestamps must be timezone-aware")
    if value.utcoffset().total_seconds() != 0:
        raise ValueError("timestamps must be in UTC")


@dataclass(frozen=True)
class PointEvent:
    match_id: str
    event_id: str
    server_id: str
    winner_id: str
    event_time: datetime
    ingested_at: datetime = field(default_factory=utc_now)
    source: str = "unknown"

    def __post_init__(self):
        if not all([self.match_id, self.event_id, self.server_id, self.winner_id, self.source]):
            raise ValueError("identifiers and source cannot be empty")
        _valid_time(self.event_time)
        _valid_time(self.ingested_at)


@dataclass(frozen=True)
class Observation:
    match_id: str
    player_id: str
    feature: str
    measured_value: float
    observed_at: datetime
    source: str
    category: str  # technical | tactical | behavioral | context
    note: str = ""

    def __post_init__(self):
        _valid_time(self.observed_at)
        if self.category not in {"technical", "tactical", "behavioral", "context"}:
            raise ValueError("invalid observation category")
        if not isfinite(self.measured_value):
            raise ValueError("measurement must be finite")
        if not all([self.match_id, self.player_id, self.feature, self.source]):
            raise ValueError("missing observation identifiers")


@dataclass(frozen=True)
class Prediction:
    prediction_id: str
    match_id: str
    target: str
    probability: float
    model_version: str
    created_at: datetime = field(default_factory=utc_now)
    evidence_cutoff: Optional[datetime] = None
    source: str = "model"

    def __post_init__(self):
        _valid_time(self.created_at)
        if self.evidence_cutoff is not None:
            _valid_time(self.evidence_cutoff)
            if self.evidence_cutoff > self.created_at:
                raise ValueError("evidence_cutoff cannot be after prediction time")
        if not isfinite(self.probability) or not (0 <= self.probability <= 1):
            raise ValueError("probability must be in [0, 1]")
        if not all([self.prediction_id, self.match_id, self.target, self.model_version, self.source]):
            raise ValueError("missing prediction identifiers")

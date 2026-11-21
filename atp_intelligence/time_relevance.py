"""Date-locked relevance policy for ATP Intelligence (current + previous season).

This module is a FEATURE SELECTION / RESEARCH utility, not a trained model.
It does not alter the event API or live match predictions on its own.

Selection rule:
- Pre-match historical performance and H2H may use ONLY matches from the
  current calendar season and the immediately preceding one.
- A match on or after the prediction timestamp's DATE is excluded in this
  day-granular version to prevent outcome leakage.
- Older facts remain in archival research, not active matchup features.
- Never treat a career/all-history Elo as a two-season recent-form metric.
- Illustrative decay half-lives below MUST be learned/calibrated by backtests.
"""
from __future__ import annotations

from datetime import date
from math import isfinite
from typing import Iterable, Literal

FeatureKind = Literal["performance", "h2h", "short_form"]

# Preliminary engineering defaults, NOT experimentally validated.
HALF_LIFE_DAYS: dict[str, int] = {
    "performance": 270,
    "h2h": 180,
    "short_form": 45,
}


def in_predictive_window(event_date: date, as_of: date) -> bool:
    """Only completed PRIOR-day matches in current or previous season.

    Same-day matches are excluded without known finish timestamps.
    This is intentional anti-leakage conservatism.
    """
    if not isinstance(event_date, date) or not isinstance(as_of, date):
        raise TypeError("event_date and as_of must be dates")
    return (
        as_of.year - 1 <= event_date.year <= as_of.year
        and event_date < as_of
    )


def relevance_weight(
    event_date: date, as_of: date, kind: FeatureKind = "performance"
) -> float:
    """0 outside the two seasons; within them decay with age in days.

    The half-life is only an initial *hyperparameter* for backtesting.
    """
    if kind not in HALF_LIFE_DAYS:
        raise ValueError(f"Unknown relevance kind: {kind}")
    if not in_predictive_window(event_date, as_of):
        return 0.0
    age_days = (as_of - event_date).days
    return 0.5 ** (age_days / HALF_LIFE_DAYS[kind])


def h2h_shrunk_win_rate(
    meetings: Iterable[tuple[date, str]],
    player_a: str,
    player_b: str,
    as_of: date,
    *,
    smoothing_matches: float = 3.0,
) -> tuple[float, float]:
    """H2H A share with low-sample shrinkage toward 50%.

    Accepts only pre-match meetings with exactly one of the two winners.
    Returns (shrunk_rate, effective_meeting_count). A 0-meeting matchup
    returns neutral 0.5 with effective count 0, NOT a forecast probability.

    Surface and fitness contexts must be separate validated model features.
    """
    if player_a == player_b or not player_a or not player_b:
        raise ValueError("Two distinct player names are required")
    if not isfinite(smoothing_matches) or smoothing_matches <= 0:
        raise ValueError("smoothing_matches must be positive and finite")

    weighted_total = 0.0
    weighted_a = 0.0
    for played_on, winner in meetings:
        if winner not in {player_a, player_b}:
            raise ValueError("A meeting's winner must be one of the two players")
        w = relevance_weight(played_on, as_of, "h2h")
        weighted_total += w
        if winner == player_a:
            weighted_a += w

    rate = (weighted_a + 0.5 * smoothing_matches) / (
        weighted_total + smoothing_matches
    )
    return rate, weighted_total

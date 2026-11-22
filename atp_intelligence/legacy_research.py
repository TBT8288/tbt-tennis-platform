"""Small, explicitly uncalibrated components adopted from historical Claude research.

Only the six *labels* are adopted. No player is automatically classified by this
module, and style labels are not a psychological diagnosis.
"""
from __future__ import annotations

from math import isfinite, log
from typing import Sequence

STYLE_CATEGORIES: tuple[str, ...] = (
    "Big Server",
    "Serve and Volleyer",
    "All-Court",
    "Attacking Baseliner",
    "Solid Baseliner",
    "Counter Puncher",
)


def parse_style_label(label: str | None) -> str | None:
    """Check a candidate label without asserting evidence for any player."""
    if label is None:
        return None
    if not isinstance(label, str):
        raise TypeError("style label must be a string or None")
    label = label.strip()
    if not label:
        return None
    if label not in STYLE_CATEGORIES:
        raise ValueError("unknown or unsupported style category")
    return label


def _validated_samples(
    probabilities: Sequence[float], outcomes: Sequence[int]
) -> tuple[list[float], list[int]]:
    if len(probabilities) != len(outcomes):
        raise ValueError("probabilities and outcomes must have the same length")
    if not probabilities:
        raise ValueError("a nonempty evaluation sample is required")
    ps: list[float] = []
    ys: list[int] = []
    for p, y in zip(probabilities, outcomes):
        if isinstance(p, bool) or not isinstance(p, (float, int)) or not isfinite(p):
            raise ValueError("each probability must be a finite number in [0, 1]")
        if not 0 <= p <= 1:
            raise ValueError("each probability must be in [0, 1]")
        if isinstance(y, bool) or not isinstance(y, int) or y not in (0, 1):
            raise ValueError("each outcome must be exactly 0 or 1")
        ps.append(float(p))
        ys.append(y)
    return ps, ys


def brier_score(probabilities: Sequence[float], outcomes: Sequence[int]) -> float:
    """Mean squared probabilistic error for binary outcomes; lower is better."""
    ps, ys = _validated_samples(probabilities, outcomes)
    return sum((p - y) ** 2 for p, y in zip(ps, ys)) / len(ps)


def binary_log_loss(
    probabilities: Sequence[float], outcomes: Sequence[int], *, eps: float = 1e-15
) -> float:
    """Binary log loss, using clipping solely for numerical stability."""
    if isinstance(eps, bool) or not isinstance(eps, (float, int)):
        raise ValueError("eps must be numeric")
    if not isfinite(eps) or not 0 < eps < 0.5:
        raise ValueError("eps must lie strictly between 0 and 0.5")
    ps, ys = _validated_samples(probabilities, outcomes)
    total = 0.0
    for p, y in zip(ps, ys):
        p = min(1 - eps, max(eps, p))
        total += -(y * log(p) + (1 - y) * log(1 - p))
    return total / len(ps)

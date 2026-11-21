"""Tennis game probabilities from an assumed independent, stationary point model.

p is the probability the SERVER wins the next point. This is a transparent
baseline, not a momentum detector and not a calibrated live prediction.
"""
from functools import lru_cache
from math import isfinite


def _check_probability(p: float) -> float:
    if isinstance(p, bool) or not isinstance(p, (int, float)) or not isfinite(p):
        raise ValueError("p must be a finite number in [0, 1]")
    p = float(p)
    if not 0.0 <= p <= 1.0:
        raise ValueError("p must be in [0, 1]")
    return p


def _check_point_score(server_points: int, returner_points: int) -> None:
    if any(isinstance(x, bool) or not isinstance(x, int) or x < 0 for x in (server_points, returner_points)):
        raise ValueError("point counts must be nonnegative integers")


def game_win_probability(p_server_point: float, server_points: int = 0, returner_points: int = 0) -> float:
    """Chance server wins the CURRENT standard (advantage-scoring) game.

    Counts are numeric point counts (0,1,2,3,4...), NOT displayed 0/15/30/40.
    Tie-breaks, no-ad, penalties and match tie-breaks are not supported.
    """
    p = _check_probability(p_server_point)
    _check_point_score(server_points, returner_points)
    a, b = server_points, returner_points
    if a >= 4 and a-b >= 2:
        return 1.0
    if b >= 4 and b-a >= 2:
        return 0.0
    # At 3-3, or any later deuce, the same two-point cycle applies.
    q = 1.0-p
    deuce = p*p/(p*p+q*q) if p*p+q*q > 0 else 0.0

    @lru_cache(None)
    def walk(x: int, y: int) -> float:
        if x >= 4 and x-y >= 2:
            return 1.0
        if y >= 4 and y-x >= 2:
            return 0.0
        if x >= 3 and y >= 3:
            if x == y:
                return deuce
            if x > y:  # server advantage
                return p + (1-p)*deuce
            return p*deuce  # returner advantage
        return p*walk(x+1,y) + (1-p)*walk(x,y+1)

    return walk(a,b)


def hold_probability(p_server_point: float) -> float:
    return game_win_probability(p_server_point)


def break_probability(p_server_point: float, server_points: int = 0, returner_points: int = 0) -> float:
    return 1.0 - game_win_probability(p_server_point, server_points, returner_points)

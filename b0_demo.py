"""ATP-DEV-001: offline B0 probability demo. No feed, model training, or API access.

The underlying B0 model assumes independent points with an unchanged,
hypothetical server-point win probability for the *rest of the current game*.
"""
from __future__ import annotations

from dataclasses import dataclass
from math import isclose

from atp_intelligence.probability import break_probability, game_win_probability


@dataclass(frozen=True)
class B0DemoResult:
    server_game_win: float
    returner_break: float
    completed_by: str | None  # "server", "returner", or None


def calculate_b0(
    p_server_point: float, server_points: int, returner_points: int
) -> B0DemoResult:
    """Compute the CURRENT standard advantage game's outcomes from manual inputs.

    Point counts are numeric points, not display scores (0/15/30/40).
    Input validation is delegated to the existing probability module.
    This is not a live or calibrated prediction.
    """
    p_hold = game_win_probability(p_server_point, server_points, returner_points)
    p_break = break_probability(p_server_point, server_points, returner_points)

    if not (0.0 <= p_hold <= 1.0 and 0.0 <= p_break <= 1.0):
        raise ArithmeticError("B0: probability is outside [0, 1]")
    if not isclose(p_hold + p_break, 1.0, abs_tol=1e-12):
        raise ArithmeticError("B0: game-win and break probabilities must sum to 1")

    if server_points >= 4 and server_points - returner_points >= 2:
        completed_by = "server"
    elif returner_points >= 4 and returner_points - server_points >= 2:
        completed_by = "returner"
    else:
        completed_by = None

    return B0DemoResult(
        server_game_win=p_hold,
        returner_break=p_break,
        completed_by=completed_by,
    )


def main() -> None:
    # Import inside main so pure B0 calculations and unit tests require no UI packages.
    import streamlit as st

    st.set_page_config(page_title="ATP – B0 offline demó", page_icon="🎾")
    st.title("🎾 ATP Intelligence – B0 offline demó")
    st.warning(
        "DEMO – minden bemenet kézzel megadott, feltételezett adat. "
        "NEM élő mérkőzés-előrejelzés, NEM edzői momentumdetektor, "
        "és NEM bizonyított predikciós előny."
    )
    st.markdown(
        "A modell azt számolja ki, mekkora eséllyel nyeri meg a **szerváló "
        "az aktuális gémet**, illetve mekkora eséllyel **brékel a fogadó**. "
        "A szervapont megnyerésének esélyét az összes hátralévő pontra "
        "változatlannak feltételezi."
    )

    p_percent = st.slider(
        "Szerváló feltételezett pontnyerési esélye (%)",
        min_value=0.0,
        max_value=100.0,
        value=50.0,
        step=0.5,
        help="Nem mért játékoserősség: kézzel megadott, végig állandónak feltételezett esély.",
    )
    left, right = st.columns(2)
    with left:
        server_points = st.number_input(
            "Szerváló megnyert pontjai az aktuális gémben",
            min_value=0,
            value=0,
            step=1,
        )
    with right:
        returner_points = st.number_input(
            "Fogadó megnyert pontjai az aktuális gémben",
            min_value=0,
            value=0,
            step=1,
        )

    st.caption(
        "Pontok **darabszáma**: 0 = 0, 1 = 15, 2 = 30, 3 = 40; "
        "4:3 = szerválóelőny, 3:4 = fogadóelőny, 4:4 = egyenlő. "
        "Nem az eredményjelzőn látható 0/15/30/40 értékeket kell beírni."
    )

    result = calculate_b0(p_percent / 100.0, server_points, returner_points)

    if result.completed_by == "server":
        st.info("Ez a gém már befejeződött: a szerváló nyert.")
    elif result.completed_by == "returner":
        st.info("Ez a gém már befejeződött: a fogadó brékelt.")

    a, b = st.columns(2)
    a.metric("Szerváló gémnyerési esélye", f"{result.server_game_win:.1%}")
    b.metric("Fogadó brékelési esélye", f"{result.returner_break:.1%}")

    st.caption(
        "Ellenőrzés: a két kimenet összege mindig 100%. "
        "Csak hagyományos, előnyös (advantage) gém; a tie-break, no-ad, "
        "büntetőpontok és a meccstie-break nem támogatott. "
        "Nincs API-hívás, élő játékosadat, odds vagy automatikus jelzés."
    )


if __name__ == "__main__":
    main()

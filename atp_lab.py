"""ATP Intelligence – offline-first, Magyar Streamlit research lab.

Start: streamlit run atp_lab.py
The research UI works without external API credentials.
This is not an empirically validated live-prediction or mental-state detector.
"""
from __future__ import annotations

import os
import sqlite3
from datetime import date

import streamlit as st

from atp_intelligence.api_tennis import TennisAPIClient, TennisAPIError
from atp_intelligence.player_data import Top150Profiles, TwoSeasonH2H
from atp_intelligence.probability import game_win_probability
from atp_intelligence.live_snapshots import LiveSnapshotStore

st.set_page_config(page_title="ATP Intelligence – Privát Lab", page_icon="🎾", layout="wide")
st.title("🎾 ATP Intelligence – Privát teniszlabor")
st.caption("2026.11.16-i Top150 pillanatkép · 2025–2026 statisztika · H2H 2026.11.15-ig")

@st.cache_resource
def load_research():
    return Top150Profiles(), TwoSeasonH2H()

try:
    profiles, h2h = load_research()
except (OSError, ValueError, KeyError) as exc:
    st.error(f"Nem sikerült betölteni a kutatási adatokat: {type(exc).__name__}")
    st.stop()

names = [p.name for p in sorted(profiles.players.values(), key=lambda p: p.rank)]
st.subheader("1. Játékosok összehasonlítása")
a_col, b_col = st.columns(2)
a_name = a_col.selectbox("A játékos", names, index=0)
b_name = b_col.selectbox("B játékos", names, index=1)
a = profiles.find(a_name)
b = profiles.find(b_name)

def show_player(panel, player):
    with panel:
        st.markdown(f"#### {player.rank}. {player.name}")
        data = player.snapshot
        st.write(f"Ország: **{data['country']}** · kéz: **{data['dominant_hand']}**")
        for label, field in [
            ("Életkor (2026.11.21.)", "age_as_of_2026_11_21"),
            ("Magasság", "height_cm"),
            ("Testsúly", "weight_kg"),
            ("Fonák", "backhand"),
            ("2026 győzelem", "year_2026_wins"),
            ("2026 vereség", "year_2026_losses"),
            ("Hard Elo – történeti", "hard_elo_2026_11_20"),
            ("Salak Elo – történeti", "clay_elo_2026_11_20"),
            ("Fű Elo – történeti", "grass_elo_2026_11_20"),
        ]:
            value, provenance = player.field(field)
            unit = (" cm" if field == "height_cm" else " kg" if field == "weight_kg" else "")
            shown = (str(value) + unit) if value is not None else "Nincs igazolt adat"
            if provenance == "candidate_only":
                shown += " ⚠️ kutatási jelölt"
            st.write(f"**{label}:** {shown}")
            if provenance == "candidate_only":
                st.caption(f"Jelölt forrás: {player.candidates[field].source_url}")
        with st.expander("Forrásolt játékstílus / bizonyíték korlátai"):
            st.write(data.get("playing_style") or "Nincs forrásolt egyéni stílus")
            st.caption("A stílusjelzés lehet előzetes/történeti; a mentális állapot nem állapítható meg pusztán eredményekből.")

show_player(a_col, a)
show_player(b_col, b)

if a_name == b_name:
    st.warning("Válassz két különböző játékost a H2H összehasonlításhoz.")
else:
    st.subheader("2. Kétidényes H2H – megfigyelt eredmények, nem előrejelzés")
    try:
        compared = h2h.for_match(a_name, b_name, as_of=date.today())
        left, center, right = st.columns(3)
        left.metric(a_name, compared.wins_a)
        center.metric("2025–2026 összes találkozó a rendelkezésre álló archívumban", compared.matches)
        right.metric(b_name, compared.wins_b)
        st.caption("Archív forrászárás: 2026.11.15. · 2024 és régebbi H2H közvetlen súlya nulla. "
                   "A hiányzó vagy régi találkozó nem jelent negatív minősítést.")
        if compared.data_stale:
            st.info("Ez történeti pillanatkép. A legújabb mérkőzések nem szerepelnek benne.")
    except ValueError:
        st.info("Történeti időpontra az összesített H2H nem biztonságos. "
                "Az időpont előtti, külön dátumozott mérkőzésekből kell újraszámolni.")

st.subheader("3. B0 – matematikai szervagém-kalkulátor")
st.caption("Kísérleti, állandó pontnyerési esélyt feltételező matematikai példa; nem valódi élő predikció.")
with st.container():
    p = st.slider("Szerváló feltételezett pontnyerési esélye", min_value=0.0, max_value=1.0, value=0.60, step=0.01)
    point_a = st.number_input("Szerváló megnyert pontjai ebben a gémben (0,1,2,3,4…)", min_value=0, max_value=100, value=0)
    point_b = st.number_input("Fogadó megnyert pontjai ebben a gémben (0,1,2,3,4…)", min_value=0, max_value=100, value=0)
    chance = game_win_probability(p, int(point_a), int(point_b))
    c1, c2 = st.columns(2)
    c1.metric("Szerváló gémnyerési esély – B0", f"{chance:.1%}")
    c2.metric("Fogadó brékelési esély – B0", f"{1.0-chance:.1%}")
    st.caption("Csak standard előnyös gémekre. Tie-break/no-ad nem támogatott.")

st.subheader("4. API-Tennis – opcionális, kézi élő adatlekérés")
st.caption("Csak kattintásra kér adatot; a fogadási időbélyeggel ellátott pillanatképet helyi, Gitből kizárt SQLite-ba menti. Az API-kulcs a szerveren marad.")
if st.button("ATP férfi egyes élő mérkőzések lekérése", type="primary"):
    if not os.environ.get("API_TENNIS_KEY"):
        st.warning("Nincs szerveroldali API_TENNIS_KEY. Az offline játékosprofilok és a B0 továbbra is használhatók.")
    else:
        try:
            client = TennisAPIClient()
            types = client.events()
            found = next((e for e in types
                          if str(e.get("event_type_type", "")).casefold().strip() == "atp singles"), None)
            if not found:
                st.warning("A csomag válaszában nem található ATP férfi egyes eseménytípus.")
            else:
                matches = client.livescore(event_type_key=str(found["event_type_key"]))
                try:
                    with LiveSnapshotStore() as snapshot_store:
                        new_versions = sum(snapshot_store.ingest(m) for m in matches)
                    st.success(f"ATP-adatpillanatképek helyileg mentve: {len(matches)} rekord, {new_versions} új állapotverzió.")
                except (OSError, sqlite3.Error):
                    st.warning("A helyi pillanatkép-mentés sikertelen; ellenőrizd a data/private könyvtár írhatóságát.")
                st.write(f"ATP Singles API-rekord: {len(matches)}")
                st.caption("Ez még nem jelent ellenőrzött ATP250/500/Masters/GS főtábla-besorolást. "
                           "A selejtezők és egyéb kategóriák későbbi ellenőrzést igényelnek.")
                for m in matches[:30]:
                    st.write(f"**{m.first_player} – {m.second_player}** · {m.status} "
                             f"· meccsazonosító {m.match_key} · "
                             f"pontonkénti gémtömbök: {len(m.point_games)}")
                if len(matches) > 30:
                    st.info("Az első 30 rekord látható.")
        except (TennisAPIError, ValueError, KeyError):
            st.error("Az élő adatkapcsolat vagy válaszséma ellenőrzést igényel. "
                     "API-kulcsot és nyers szolgáltatói hibaüzenetet nem jelenítünk meg.")

st.divider()
st.caption("Privát V1 kutatási kezelőfelület · nincs állított momentum-előny, mentális diagnózis vagy valós fogadási javaslat.")

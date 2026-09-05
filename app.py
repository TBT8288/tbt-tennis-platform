"""
app.py
------
Streamlit web dashboard for TBT Tennis Intelligence Platform.
Zen Minimalist Edition with robust error handling.
"""

from __future__ import annotations

import streamlit as st

# Page configuration
st.set_page_config(
    page_title="TBT - Zen Tennis Intelligence",
    page_icon="🌿",
    layout="wide"
)

# --- JAPANESE MINIMALIST / ZEN CSS INJECTION ---
st.markdown("""
<style>
    .stApp {
        background-color: #F9F8F6;
        color: #2C2C2C;
        font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Helvetica, Arial, sans-serif;
    }
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}
    h1, h2, h3 {
        color: #1A1A1A !important;
        font-weight: 400 !important;
        letter-spacing: -0.02em;
    }
    h1 {
        font-size: 1.8rem !important;
        border-bottom: 1px solid #E2DDD5;
        padding-bottom: 0.5rem;
        margin-bottom: 1.5rem !important;
    }
    .stCaption, p {
        color: #6E6863 !important;
    }
    div[data-testid="stExpander"] {
        background-color: #FFFFFF;
        border: 1px solid #E0DBD0;
        border-radius: 6px;
        margin-bottom: 1rem;
    }
    div.stButton > button {
        background-color: #EFECE6 !important;
        color: #2C2C2C !important;
        border: 1px solid #D6D0C4 !important;
        border-radius: 6px !important;
    }
</style>
""", unsafe_allow_html=True)

st.title("🌿 TBT — Tennis Intelligence")
st.caption("Contemplative live tracking & automated tactical analysis.")

# Safe imports to prevent blank screen crashes
try:
    from tennis_api_client import list_live_matches, find_match
    from gemini_client import GeminiClient
    from discord_client import send_discord_message
    IMPORTS_OK = True
except Exception as e:
    IMPORTS_OK = False
    st.error(f"Modul betöltési hiba: {e}")

if IMPORTS_OK:
    @st.cache_resource
    def get_ai_client():
        try:
            return GeminiClient()
        except Exception:
            return None

    ai_client = get_ai_client()

    if ai_client is None:
        st.warning("Figyelem: A GEMINI_API_KEY hiányzik vagy érvénytelen a Streamlit Secrets-ben.")

    st.markdown("### 01. Live Match Selection")

    @st.fragment(run_every=120)
    def render_dashboard():
        if "saved_analyses" not in st.session_state:
            st.session_state.saved_analyses = {}

        try:
            matches = list_live_matches()
        except Exception as e:
            st.error(f"API hiba a meccsek lekérdezésekor: {e}")
            matches = []
        
        if not matches:
            st.info("Jelenleg nincsenek aktív élő meccsek az API-n keresztül (vagy kimerült a RapidAPI kvóta).")
            return
        
        match_options = {f"{m.player1} vs {m.player2} — [{m.status}]": m for m in matches}
        
        selected_match_keys = st.multiselect(
            "Válassz meccseket megfigyelésre:",
            options=list(match_options.keys()),
            key="active_matches_multiselect"
        )

        if selected_match_keys and ai_client:
            st.markdown("---")
            st.markdown("### 02. Synchronized TBT Feed")
            
            for key in selected_match_keys:
                match_info = match_options[key]
                try:
                    state = find_match(match_info.player1)
                except Exception:
                    state = None
                
                if state and state.is_complete():
                    last_analysis = st.session_state.saved_analyses.get(key)
                    score_changed = last_analysis and last_analysis["state"].score != state.score
                    not_analyzed_yet = key not in st.session_state.saved_analyses
                    
                    if not_analyzed_yet or score_changed:
                        with st.spinner(f"Elemzés generálása: {state.player1} vs {state.player2}..."):
                            commentary = ai_client.get_commentary(state)
                        
                        st.session_state.saved_analyses[key] = {
                            "state": state,
                            "commentary": commentary
                        }
                        
                        try:
                            discord_msg = (
                                f"🌿 **TBT Zen Analysis Feed**\n"
                                f"──────────────────────────────\n"
                                f"👤 **{state.player1}** vs **{state.player2}**\n"
                                f"📊 **Score:** `{state.score}`\n"
                                f"📌 **Status:** {state.status}\n\n"
                                f"🤖 **Tactical Assessment:**\n{commentary}"
                            )
                            send_discord_message(discord_msg)
                        except Exception:
                            pass

        if st.session_state.saved_analyses:
            st.markdown("---")
            st.markdown("### 03. Active Observations")
            for key, data in list(st.session_state.saved_analyses.items()):
                state = data["state"]
                commentary = data["commentary"]
                
                with st.expander(f"📊 {state.player1} vs {state.player2}  |  {state.score}", expanded=True):
                    st.caption(f"Status: {state.status}")
                    st.markdown(commentary)
                    if st.button(f"Megfigyelés befejezése", key=f"clear_{key}"):
                        del st.session_state.saved_analyses[key]
                        st.rerun()

    render_dashboard()

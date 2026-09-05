"""
app.py
------
Streamlit web dashboard for TBT Tennis Intelligence Platform.
Design theme: Japanese Minimalist / Zen Interior (Warm neutrals, whitespace, clean typography).
"""

from __future__ import annotations

import streamlit as st
from tennis_api_client import list_live_matches, find_match
from gemini_client import GeminiClient
from discord_client import send_discord_message


# Page configuration
st.set_page_config(
    page_title="TBT - Zen Tennis Intelligence",
    page_icon="🌿",
    layout="wide"
)

# --- JAPANESE MINIMALIST / ZEN CSS INJECTION ---
st.markdown("""
<style>
    /* Global background and typography (Warm rice-paper off-white & soft charcoal) */
    .stApp {
        background-color: #F9F8F6;
        color: #2C2C2C;
        font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Helvetica, Arial, sans-serif;
    }
    
    /* Hide default Streamlit branding & header clutter for clean zen whitespace */
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}
    
    /* Headers - Clean, subtle, elegant */
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
    
    h2 {
        font-size: 1.3rem !important;
        margin-top: 1.5rem !important;
    }

    /* Subtext and captions */
    .stCaption, p {
        color: #6E6863 !important;
    }

    /* Cards / Expanders - Styled like shoji screens / natural wood frames */
    .streamlit-expanderHeader {
        background-color: #F2EFE9 !important;
        border: 1px solid #E0DBD0 !important;
        border-radius: 6px !important;
        color: #2C2C2C !important;
        font-weight: 500 !important;
    }
    
    div[data-testid="stExpander"] {
        background-color: #FFFFFF;
        border: 1px solid #E0DBD0;
        border-radius: 6px;
        margin-bottom: 1rem;
        box-shadow: 0 1px 3px rgba(0,0,0,0.02);
    }

    /* Inputs and Multiselect - Clean stone/paper boxes */
    .stMultiSelect div[data-baseweb="select"] {
        background-color: #FFFFFF !important;
        border: 1px solid #D9D2C7 !important;
        border-radius: 6px !important;
    }

    /* Buttons - Soft, tactile, stone-like feedback */
    div.stButton > button {
        background-color: #EFECE6 !important;
        color: #2C2C2C !important;
        border: 1px solid #D6D0C4 !important;
        border-radius: 6px !important;
        padding: 0.4rem 1rem !important;
        font-weight: 400 !important;
        transition: all 0.2s ease;
    }
    
    div.stButton > button:hover {
        background-color: #E2DDD5 !important;
        border-color: #B5AB9B !important;
        color: #1A1A1A !important;
    }

    /* Info boxes / Alerts */
    .stAlert {
        background-color: #F2EFE9 !important;
        border: 1px solid #E0DBD0 !important;
        color: #2C2C2C !important;
        border-radius: 6px !important;
    }
</style>
""", unsafe_allow_html=True)

# App Header
st.title("🌿 TBT — Tennis Intelligence")
st.caption("Contemplative live tracking & automated tactical analysis. Refreshes quietly every 2 minutes.")

# Initialize Gemini Client safely
@st.cache_resource
def get_ai_client():
    try:
        return GeminiClient()
    except Exception:
        return None

ai_client = get_ai_client()

if ai_client is None:
    st.error("System Notice: GEMINI_API_KEY is missing or invalid in your environment configuration.")

st.markdown("### 01. Live Match Selection")

# Auto-refreshing fragment optimized to 120s (quota-safe)
@st.fragment(run_every=120)
def render_dashboard():
    # Initialize session state for stored analyses
    if "saved_analyses" not in st.session_state:
        st.session_state.saved_analyses = {}

    matches = list_live_matches()
    
    if not matches:
        st.info("No active live matches available at this moment.")
        return
    
    match_options = {f"{m.player1} vs {m.player2} — [{m.status}]": m for m in matches}
    
    selected_match_keys = st.multiselect(
        "Select matches for observation:",
        options=list(match_options.keys()),
        key="active_matches_multiselect"
    )

    if selected_match_keys:
        st.markdown("---")
        st.markdown("### 02. Synchronized TBT Feed")
        
        for key in selected_match_keys:
            match_info = match_options[key]
            state = find_match(match_info.player1)
            
            if state and state.is_complete():
                last_analysis = st.session_state.saved_analyses.get(key)
                score_changed = last_analysis and last_analysis["state"].score != state.score
                not_analyzed_yet = key not in st.session_state.saved_analyses
                
                if not_analyzed_yet or score_changed:
                    with st.spinner(f"Synthesizing analysis for {state.player1} vs {state.player2}..."):
                        commentary = ai_client.get_commentary(state)
                    
                    st.session_state.saved_analyses[key] = {
                        "state": state,
                        "commentary": commentary
                    }
                    
                    discord_msg = (
                        f"🌿 **TBT Zen Analysis Feed**\n"
                        f"──────────────────────────────\n"
                        f"👤 **{state.player1}** vs **{state.player2}**\n"
                        f"📊 **Score:** `{state.score}`\n"
                        f"📌 **Status:** {state.status}\n\n"
                        f"🤖 **Tactical Assessment:**\n{commentary}"
                    )
                    
                    send_discord_message(discord_msg)

    # Display persistent observations
    if st.session_state.saved_analyses:
        st.markdown("---")
        st.markdown("### 03. Active Observations")
        for key, data in list(st.session_state.saved_analyses.items()):
            state = data["state"]
            commentary = data["commentary"]
            
            with st.expander(f"📊 {state.player1} vs {state.player2}  |  {state.score}", expanded=True):
                st.caption(f"Status: {state.status}")
                st.markdown(commentary)
                if st.button(f"Conclude Observation", key=f"clear_{key}"):
                    del st.session_state.saved_analyses[key]
                    st.rerun()

render_dashboard()

"""
app.py
------
Streamlit web dashboard for TBT Tennis Intelligence Platform with auto-refresh.
"""

from __future__ import annotations

import streamlit as st
from tennis_api_client import list_live_matches, find_match
from openai_client import OpenAIClient
from discord_client import send_discord_message


st.set_page_config(
    page_title="TBT Tennis Dashboard",
    page_icon="🎾",
    layout="wide"
)

st.title("🎾 TBT - Tennis Intelligence Platform")
st.markdown("Select live matches from the auto-refreshing list below, run tactical analysis, and stream insights directly to Discord.")

# Initialize OpenAI Client safely
@st.cache_resource
def get_ai_client():
    try:
        return OpenAIClient()
    except Exception:
        return None

ai_client = get_ai_client()

if ai_client is None:
    st.error("Error: OPENAI_API_KEY is missing or invalid. Please check your environment variables.")

st.header("1. Live Matches Feed & Analysis")

# Auto-refreshing fragment containing both the list and the analysis execution button
@st.fragment(run_every=30)
def render_dashboard():
    st.caption("⚡ Live feed automatically syncs every 30 seconds.")
    matches = list_live_matches()
    
    if not matches:
        st.info("No live matches currently available via API.")
        return
    
    match_options = {f"{m.player1} vs {m.player2} ({m.status})": m for m in matches}
    
    selected_match_keys = st.multiselect(
        "Select matches to monitor & analyze:",
        options=list(match_options.keys()),
        key="active_matches_multiselect"
    )

    if selected_match_keys:
        st.markdown("---")
        st.subheader("2. TBT Analysis & Discord Push")
        
        if st.button("🚀 Run Analysis for Selected Matches", key="run_analysis_btn"):
            for key in selected_match_keys:
                match_info = match_options[key]
                state = find_match(match_info.player1)
                
                if state and state.is_complete():
                    st.markdown(f"### 👤 {state.player1} vs {state.player2}")
                    st.write(f"**Score:** `{state.score}` | **Status:** {state.status}")
                    
                    with st.spinner(f"Analyzing {state.player1} vs {state.player2} via OpenAI..."):
                        commentary = ai_client.get_commentary(state)
                        
                    st.markdown("**TBT Commentary:**")
                    st.markdown(commentary)
                    
                    # Format message for Discord
                    discord_msg = (
                        f"🎾 **Live Tennis Analysis (TBT Dashboard)**\n"
                        f"──────────────────────────────\n"
                        f"👤 **{state.player1}** vs **{state.player2}**\n"
                        f"📊 **Score:** `{state.score}`\n"
                        f"📌 **Status:** {state.status}\n\n"
                        f"🤖 **TBT Analysis:**\n{commentary}"
                    )
                    
                    # Send to Discord
                    send_discord_message(discord_msg)
                    st.success(f"Analysis completed and sent to Discord for {state.player1} vs {state.player2}!")
                    st.markdown("---")
                else:
                    st.warning(f"Could not retrieve complete live data for: {key}")

render_dashboard()
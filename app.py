"""
app.py
------
Streamlit web dashboard for TBT Tennis Intelligence Platform with Gemini AI,
automated live tracking, and Discord integration.
"""

from __future__ import annotations

import streamlit as st
from tennis_api_client import list_live_matches, find_match
from gemini_client import GeminiClient
from discord_client import send_discord_message


st.set_page_config(
    page_title="TBT Tennis Dashboard",
    page_icon="🎾",
    layout="wide"
)

st.title("🎾 TBT - Tennis Intelligence Platform (Gemini Edition)")
st.markdown("Select live matches below to monitor them automatically. The app refreshes every 30 seconds and triggers Gemini AI analysis on score changes.")

# Initialize Gemini Client safely
@st.cache_resource
def get_ai_client():
    try:
        return GeminiClient()
    except Exception:
        return None

ai_client = get_ai_client()

if ai_client is None:
    st.error("Error: GEMINI_API_KEY is missing or invalid. Please check your Streamlit Secrets.")

st.header("1. Live Matches Feed & Automated Analysis")

# Auto-refreshing fragment containing both the list and automated execution loop
@st.fragment(run_every=30)
def render_dashboard():
    st.caption("⚡ Live feed & automated sync running every 30 seconds.")
    
    # Initialize session state for stored analyses
    if "saved_analyses" not in st.session_state:
        st.session_state.saved_analyses = {}

    matches = list_live_matches()
    
    if not matches:
        st.info("No live matches currently available via API.")
        return
    
    match_options = {f"{m.player1} vs {m.player2} ({m.status})": m for m in matches}
    
    selected_match_keys = st.multiselect(
        "Select matches to monitor & analyze automatically:",
        options=list(match_options.keys()),
        key="active_matches_multiselect"
    )

    if selected_match_keys:
        st.markdown("---")
        st.subheader("2. Automated TBT Analysis & Discord Feed")
        
        for key in selected_match_keys:
            match_info = match_options[key]
            state = find_match(match_info.player1)
            
            if state and state.is_complete():
                # Check if already analyzed or if the score has updated
                last_analysis = st.session_state.saved_analyses.get(key)
                score_changed = last_analysis and last_analysis["state"].score != state.score
                not_analyzed_yet = key not in st.session_state.saved_analyses
                
                if not_analyzed_yet or score_changed:
                    with st.spinner(f"🤖 Automatikus Gemini TBT elemzés fut: {state.player1} vs {state.player2}..."):
                        commentary = ai_client.get_commentary(state)
                    
                    # Save to session state so it persists across refreshes
                    st.session_state.saved_analyses[key] = {
                        "state": state,
                        "commentary": commentary
                    }
                    
                    # Format message for Discord
                    discord_msg = (
                        f"🎾 **Automated TBT Tennis Analysis (Gemini)**\n"
                        f"──────────────────────────────\n"
                        f"👤 **{state.player1}** vs **{state.player2}**\n"
                        f"📊 **Score:** `{state.score}`\n"
                        f"📌 **Status:** {state.status}\n\n"
                        f"🤖 **TBT Analysis:**\n{commentary}"
                    )
                    
                    send_discord_message(discord_msg)

    # Display persistent and auto-updating analyses on screen
    if st.session_state.saved_analyses:
        st.markdown("---")
        st.subheader("📋 Live Monitored Matches")
        for key, data in list(st.session_state.saved_analyses.items()):
            state = data["state"]
            commentary = data["commentary"]
            
            with st.expander(f"📊 {state.player1} vs {state.player2} | Score: {state.score}", expanded=True):
                st.write(f"**Status:** {state.status}")
                st.markdown("**TBT Commentary:**")
                st.markdown(commentary)
                if st.button(f"🗑️ Stop & Remove", key=f"clear_{key}"):
                    del st.session_state.saved_analyses[key]
                    st.rerun()

render_dashboard()

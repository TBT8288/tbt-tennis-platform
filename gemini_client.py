"""
gemini_client.py
----------------
Gemini API kliens a TBT Tennis Intelligence Platformhoz a google-genai SDK-val,
szigorú tényalapú elemzéssel (hallucinációk nélkül).
"""

from __future__ import annotations

import os
import streamlit as st
from google import genai


class GeminiClient:
    def __init__(self):
        # API kulcs lekérése a Streamlit Secrets-ből vagy a környezeti változókból
        api_key = self._get_api_key()
        # Inicializálás a hivatalos google-genai SDK-val
        self.client = genai.Client(api_key=api_key)
        # Ingyenesen és hibamentesen a Flash modellt használjuk a kártya bekapcsolásáig
        self.model_name = "gemini-2.5-flash"

    def _get_api_key(self) -> str:
        try:
            if "GEMINI_API_KEY" in st.secrets:
                return st.secrets["GEMINI_API_KEY"]
        except Exception:
            pass
        
        api_key = os.environ.get("GEMINI_API_KEY")
        if not api_key:
            raise RuntimeError("Hiányzik a GEMINI_API_KEY a Streamlit Secrets-ből vagy a környezeti változókból!")
        return api_key

    def get_commentary(self, state) -> str:
        # Szigorú System Instruction / Prompt a hallucinációk megakadályozására
        prompt = f"""
        You are a professional tennis tactical analyst following the rigorous TBT methodology (Tennis Intelligence Platform).
        
        CRITICAL RULES:
        1. Analyze the live match data STRICTLY based on the provided score and status.
        2. DO NOT invent, hallucinate, or assume any events (such as breaks, specific momentum shifts, or game outcomes) that are not explicitly proven by the numerical score. If a set or game score is 0-0 or just starting, do not claim someone broke serve early.
        3. Keep the analysis professional, structured, and focused on tactical patterns derived purely from the given numbers.

        Match Context:
        - Player 1: {state.player1}
        - Player 2: {state.player2}
        - Current Score: {state.score}
        - Match Status: {state.status}

        Provide a concise TBT tactical evaluation covering Dominance, Momentum, and Strategic Outlook based exclusively on these facts.
        """
        
        try:
            response = self.client.models.generate_content(
                model=self.model_name,
                contents=prompt,
            )
            return response.text
        except Exception as e:
            return f"Hiba a Gemini elemzés generálása közben: {e}"

"""
openai_client.py
----------------
OpenAI API client that analyzes live match states from RapidAPI according 
to the TBT methodology (Tennis Intelligence Platform), generating structured, 
professional match commentaries and insights in English.
"""

from __future__ import annotations

import os
from openai import OpenAI
from tennis_api_client import MatchState


class OpenAIClient:
    def __init__(self) -> None:
        api_key = os.environ.get("OPENAI_API_KEY")
        if not api_key:
            raise RuntimeError(
                "Missing OPENAI_API_KEY environment variable. "
                "Please set it before running the program."
            )
        # Official modern OpenAI SDK initialization
        self.client = OpenAI(api_key=api_key)

    def get_commentary(self, state: MatchState) -> str:
        """
        Generates tactical analysis and commentary based on MatchState using the TBT methodology.
        """
        # System Prompt tuned to TBT methodology, instructing OpenAI to respond in English
        system_prompt = (
            "You are a professional tennis analysis AI who analyzes live matches "
            "according to the principles of the Tennis Intelligence Platform and the TBT methodology.\n"
            "Your task based on the provided data (players, current score, sets, status) is:\n"
            "1. Tactical and momentum analysis (who is in control, where are the match turning points).\n"
            "2. Structured evaluation according to TBT methodology (dominance, weight of break points, mental factors).\n"
            "3. Realistic odds/prospects estimation for upcoming games/sets.\n"
            "Style: Professional, analytical, concise, yet engaging sports broadcasting style. Answer exclusively in English!"
        )

        user_content = (
            f"Please analyze the following live tennis match based on the TBT methodology:\n"
            f"- Player 1: {state.player1}\n"
            f"- Player 2: {state.player2}\n"
            f"- Current score / sets: {state.score}\n"
            f"- Status: {state.status}\n"
            f"- Raw data: {state.raw}"
        )

        try:
            response = self.client.chat.completions.create(
                model="gpt-4o-mini",  # Fast, cost-effective, and highly capable analysis model
                messages=[
                    {"role": "system", "content": system_prompt},
                    {"role": "user", "content": user_content},
                ],
                temperature=0.7,
                max_tokens=300,
            )
            return response.choices[0].message.content.strip()
        except Exception as e:
            return f"Error occurred during OpenAI API call: {e}"
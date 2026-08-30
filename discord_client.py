"""
discord_client.py
-----------------
A Discord webhook client that sends generated TBT analyses 
and match states to the specified Discord channel.
"""

from __future__ import annotations

import os
import requests


def send_discord_message(message: str) -> None:
    """
    Sends a text message to the Discord channel specified in the DISCORD_WEBHOOK_URL environment variable.
    """
    webhook_url = os.environ.get("DISCORD_WEBHOOK_URL")
    if not webhook_url:
        print("-> [Discord] Error: DISCORD_WEBHOOK_URL is not set.")
        return

    payload = {
        "content": message
    }

    try:
        response = requests.post(webhook_url, json=payload, timeout=10)
        response.raise_for_status()
        print("-> [Discord] Message successfully sent to Discord channel!")
    except requests.exceptions.RequestException as e:
        print(f"-> [Discord] Failed to send message: {e}")
        if hasattr(e, 'response') and e.response is not None:
            print(f"-> [Discord Response Code/Text]: {e.response.status_code} - {e.response.text}")
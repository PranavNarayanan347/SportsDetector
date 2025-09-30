# notifier.py

import requests
import os
from dotenv import load_dotenv

# ─── Load environment variables from .env ────────────────────────────────────
load_dotenv()

BOT_TOKEN = os.getenv('TELEGRAM_BOT_TOKEN')   # from your .env
CHAT_ID   = os.getenv('TELEGRAM_CHAT_ID')     # from your .env

def send_telegram(message: str):
    """
    Send a message via Telegram Bot API to your chat_id.
    """
    if not BOT_TOKEN or not CHAT_ID:
        raise ValueError(
            "Please set TELEGRAM_BOT_TOKEN and TELEGRAM_CHAT_ID "
            "in your .env (or environment) before running."
        )

    # Telegram API endpoint to send a message
    url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
    payload = {
        "chat_id": CHAT_ID,
        "text": message
    }

    response = requests.post(url, data=payload)
    # If something goes wrong (e.g., bad token or chat_id), raise an exception
    response.raise_for_status()

if __name__ == '__main__':
    # Quick test — you should see this message in your Telegram within a few seconds
    send_telegram("Test alert from SportsBetterNotifier via Telegram!")
    print("Telegram test sent.")

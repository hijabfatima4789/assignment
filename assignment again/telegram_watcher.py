import requests
import time
from pathlib import Path
from datetime import datetime

TOKEN = "YOUR_BOT_TOKEN"
BASE_URL = f"https://api.telegram.org/bot{TOKEN}"

VAULT = Path("vault")
NEEDS_ACTION = VAULT / "Needs_Action"

# Auto-create directory
NEEDS_ACTION.mkdir(parents=True, exist_ok=True)

last_update_id = None


def get_updates():
    global last_update_id
    url = f"{BASE_URL}/getUpdates"

    params = {}
    if last_update_id:
        params["offset"] = last_update_id + 1

    try:
        response = requests.get(url, params=params, timeout=30)
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"[ERROR] Failed to get updates: {e}")
        return {"result": []}


def create_file(message):
    text = message.get("text", "")
    chat_id = message["chat"]["id"]
    msg_id = message["message_id"]

    content = f"""---
type: telegram
chat_id: {chat_id}
message_id: {msg_id}
received: {datetime.now()}
status: pending
---

## Message
{text}
"""

    file = NEEDS_ACTION / f"TELEGRAM_{msg_id}.md"
    file.write_text(content)


def run():
    global last_update_id

    while True:
        try:
            data = get_updates()

            for update in data.get("result", []):
                last_update_id = update["update_id"]

                if "message" in update:
                    create_file(update["message"])
                    print(f"Saved message {update['message']['message_id']}")

        except Exception as e:
            print(f"Error: {e}")

        time.sleep(5)


if __name__ == "__main__":
    run()

import os
from pathlib import Path
import json
from send_telegram import send

APPROVED = Path("vault/Approved")
DONE = Path("vault/Done")


def process_approved():
    for file in APPROVED.glob("*.md"):
        content = file.read_text()

        # extract chat_id and message (simple parsing)
        lines = content.split("\n")
        chat_id = None
        message = None

        for l in lines:
            if "chat_id:" in l:
                chat_id = l.split(":")[1].strip()
            if "message:" in l:
                message = l.split(":",1)[1].strip()

        if chat_id and message:
            send(chat_id, message)

        file.rename(DONE / file.name)


def run():
    os.system('claude -p "Process Needs_Action and create plans and approvals"')
    process_approved()


run()

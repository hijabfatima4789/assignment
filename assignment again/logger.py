import json
from datetime import datetime
from pathlib import Path

def log_action(action, status):
    log = {
        "time": str(datetime.now()),
        "action": action,
        "status": status
    }

    file = Path("vault/Logs/log.json")
    file.parent.mkdir(parents=True, exist_ok=True)

    if file.exists():
        data = json.loads(file.read_text())
    else:
        data = []

    data.append(log)
    file.write_text(json.dumps(data, indent=2))

log_action("telegram_reply", "success")

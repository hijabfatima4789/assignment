import time
import subprocess

while True:
    print("[DAEMON] Running orchestrator...")
    subprocess.run(["python", "orchestrator.py"])
    print("[DAEMON] Sleeping 5 minutes...\n")
    time.sleep(300)

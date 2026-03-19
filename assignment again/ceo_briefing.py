from pathlib import Path
from datetime import datetime

DONE = Path("vault/Done")
BRIEFINGS = Path("vault/Briefings")

def generate_report():
    # Ensure directories exist
    DONE.mkdir(parents=True, exist_ok=True)
    BRIEFINGS.mkdir(parents=True, exist_ok=True)

    files = list(DONE.glob("*.md"))
    total_tasks = len(files)

    # Capture timestamp once
    now = datetime.now()

    summary = ""
    for f in files:
        content = f.read_text()
        if "invoice" in content.lower():
            summary += "- Invoice task completed\n"
        elif "urgent" in content.lower():
            summary += "- Urgent request handled\n"
        else:
            summary += "- General task completed\n"

    report = f"""# CEO Weekly Briefing

Date: {now}

## Summary
Total tasks completed: {total_tasks}

## Activities
{summary}

## Suggestion
System is working normally. Consider adding more automation.
"""

    file = BRIEFINGS / f"briefing_{now.date()}.md"
    file.write_text(report)

generate_report()

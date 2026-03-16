"""
Telegram Watcher - Monitors Telegram messages and creates vault tasks
Saves messages containing keywords to Needs_Action folder

Setup:
1. Get token from @BotFather on Telegram
2. Set TELEGRAM_BOT_TOKEN=your_token_here
3. Run: python telegram_watcher.py
"""

import os
import asyncio
import logging
from pathlib import Path
from datetime import datetime
from telegram import Update
from telegram.ext import Application, MessageHandler, filters, ContextTypes

# Setup logging
logging.basicConfig(
    format="%(asctime)s - %(message)s",
    level=logging.INFO
)
logger = logging.getLogger(__name__)

# Configuration
VAULT = Path("AI_Employee_Vault")
NEEDS_ACTION = VAULT / "Needs_Action"

# Keywords to trigger task creation
KEYWORDS = ["invoice", "urgent", "payment", "help", "task", "todo", "action", "asap"]


async def watch(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Process incoming Telegram messages"""
    message = update.message.text
    user = update.message.from_user.username or update.message.from_user.first_name or "unknown"
    chat_id = update.message.chat_id

    # Check if message contains keywords
    if any(k in message.lower() for k in KEYWORDS):
        # Create filename with timestamp
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        filename = f"TELEGRAM_{timestamp}.md"
        filepath = NEEDS_ACTION / filename

        # Create task content
        content = f"""---
type: telegram
from: {user}
chat_id: {chat_id}
priority: high
received: {datetime.now().isoformat()}
status: pending
---

## Message
{message}

## Actions
- [ ] Review and respond
- [ ] Take necessary action
"""

        # Ensure directory exists and write file
        NEEDS_ACTION.mkdir(parents=True, exist_ok=True)
        filepath.write_text(content, encoding='utf-8')

        logger.info(f"Created task: {filepath}")

        # Confirm to user
        await update.message.reply_text(
            f"Task created from your message!\nSaved to: {filename}"
        )
    else:
        # Optional: reply that no keywords were found
        await update.message.reply_text(
            "I heard you. Use keywords like: invoice, urgent, payment, help, task, todo, action, asap\nto create a task automatically."
        )


def main():
    """Start the bot"""
    token = os.environ.get("TELEGRAM_BOT_TOKEN")

    if not token:
        print("ERROR: Set TELEGRAM_BOT_TOKEN environment variable")
        print("   set TELEGRAM_BOT_TOKEN=your_token_here")
        return

    # Build application
    app = Application.builder().token(token).build()

    # Add handler for text messages
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, watch))

    logger.info("Bot started! Listening for messages...")
    logger.info(f"Keywords: {', '.join(KEYWORDS)}")
    logger.info("Press Ctrl+C to stop")

    # Run
    app.run_polling(allowed_updates=Update.ALL_TYPES)


if __name__ == "__main__":
    main()

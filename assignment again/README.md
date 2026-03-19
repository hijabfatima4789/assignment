# 🤖 Personal AI Employee (Digital FTE)

## 📌 Overview

This project implements a **Digital Full-Time Employee (FTE)** that can autonomously:

* Monitor Telegram messages
* Analyze incoming requests
* Generate plans using AI
* Request human approval
* Execute actions (reply via Telegram)
* Maintain logs and generate reports

---

## 🧠 System Architecture

### 1. Perception Layer

* Telegram Watcher (`telegram_watcher.py`)
* Converts messages into `.md` files in `/Needs_Action`

---

### 2. Memory Layer

* Obsidian Vault (`/vault`)
* Stores tasks, plans, approvals, logs

---

### 3. Reasoning Layer

* Claude processes tasks
* Generates plans in `/Plans`
* Creates approval requests in `/Pending_Approval`

---

### 4. Action Layer

* Telegram API (`send_telegram.py`)
* Sends messages after approval

---

## 🔄 Workflow

1. User sends message via Telegram
2. Watcher saves message in `/Needs_Action`
3. Claude generates plan
4. If action required → file created in `/Pending_Approval`
5. User approves → moved to `/Approved`
6. System executes action
7. Task moved to `/Done`
8. Logs and reports updated

---

## 🥉 Bronze Features

* Telegram watcher
* File-based task system
* Claude plan generation

---

## 🥈 Silver Features

* Approval system
* Automated orchestration
* Telegram reply action
* Scheduling

---

## 🥇 Gold Features

* Weekly CEO Briefing
* Logging system
* Autonomous execution loop

---

## ⚙️ Technologies Used

* Python
* Obsidian
* Telegram Bot API
* Claude Code

---

## 🎯 Conclusion

This system demonstrates a working **autonomous AI employee** capable of perception, reasoning, and action.

@echo off
:loop
python orchestrator.py
timeout /t 300 /nobreak >nul
goto loop

@echo off
title SecureAI PolicyGuard – Auto Start

echo ============================================
echo   Starting SecureAI PolicyGuard System...
echo ============================================

set PROJECT_PATH=%~dp0
cd /d "%PROJECT_PATH%"

set PYTHON=python

echo [+] Launching API Server...
start "SecureAI API" cmd /k "%PYTHON% -m uvicorn api.server:app --reload"
echo [+] Waiting for API initialization...

set /a retries=0

:wait_for_api
powershell -command ^
  "try { $r = Invoke-WebRequest 'http://127.0.0.1:8000/health' -UseBasicParsing -TimeoutSec 2; if ($r.StatusCode -eq 200) { exit 0 } } catch { exit 1 }"

if %errorlevel% neq 0 (
    set /a retries+=1
    if %retries% GEQ 15 (
        echo [X] API failed to start! Aborting.
        pause
        exit /b
    )
    timeout /t 1 >nul
    goto wait_for_api
)

echo [✓] API is online!

start "" http://127.0.0.1:8000/health
start "" http://127.0.0.1:8000/docs

echo [+] Launching SecureAI GUI...
start "SecureAI GUI" cmd /k "%PYTHON% main.py & pause"

echo --------------------------------
echo [✓] All systems running!
echo --------------------------------

pause
@echo off
title Magenta CTkButton Demo
echo ========================================
echo   Magenta CTkButton Demo
echo ========================================
echo.

REM Change to the script's directory
cd /d "%~dp0"

REM Check if Python is installed
python --version >nul 2>&1
if %errorlevel% neq 0 (
    echo ERROR: Python is not installed or not in PATH
    echo Please install Python and make sure it's accessible from the command line
    echo.
    pause
    exit /b 1
)

REM Check if CustomTkinter is installed
python -c "import customtkinter" >nul 2>&1
if %errorlevel% neq 0 (
    echo Installing CustomTkinter...
    python -m pip install customtkinter
    if %errorlevel% neq 0 (
        echo ERROR: Failed to install CustomTkinter
        echo Please make sure you have pip installed and internet connection
        echo.
        pause
        exit /b 1
    )
)

echo Starting Magenta CTkButton Demo...
echo.

python demo_ctk_buttons.py

pause
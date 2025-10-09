@echo off
title Kill PWD Tools Hub Processes
echo ========================================
echo   Killing PWD Tools Hub Processes
echo ========================================
echo.

echo Killing any running Streamlit processes...
taskkill /f /im streamlit.exe >nul 2>&1
taskkill /f /fi "imagename eq python.exe" /fi "windowtitle eq PWD Tools Hub*" >nul 2>&1

echo Killing any Python processes running app.py...
for /f "tokens=2 delims=," %%a in ('tasklist /fi "imagename eq python.exe" /fo csv /v ^| findstr /i "app.py"') do (
    taskkill /f /pid %%a >nul 2>&1
)

echo.
echo All PWD Tools Hub processes have been terminated.
echo.
timeout /t 2 >nul
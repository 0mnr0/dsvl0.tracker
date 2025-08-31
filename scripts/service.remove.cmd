@echo off
chcp 1251 > nul
set SRC=dsvl0.tracker.exe
set DST=%APPDATA%\dsvl0
set VBS=%DST%\run_silent.vbs
set STARTUP=%APPDATA%\Microsoft\Windows\Start Menu\Programs\Startup\run_silent.vbs

taskkill /f /im dsvl0.tracker.exe
timeout /t 1 > nul

if exist "%STARTUP%" (
    del "%STARTUP%"
    echo [OK] removed.
)

if exist "%VBS%" del "%VBS%"
if exist "%DST%\%SRC%" del "%DST%\%SRC%"

if exist "%DST%" rd /s /q "%DST%"

echo [OK] dsvl0.tracker removed.
pause

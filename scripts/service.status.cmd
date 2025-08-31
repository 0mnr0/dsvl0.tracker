@echo off
chcp 1251 > nul
set SRC=dsvl0.tracker.exe
set DST=%APPDATA%\dsvl0
set VBS=%DST%\run_silent.vbs
set STARTUP=%APPDATA%\Microsoft\Windows\Start Menu\Programs\Startup
cls

if not exist "%DST%" (
	color 04
	echo [FAIL] Service is not installed!
	echo [REASON] Destination folder is not found
	echo.
	pause
	exit
)

if not exist "%DST%\secret.key" (
	color 04
	echo [FAIL] Service is not installed!
	echo [REASON] secret.key is not found
	echo.
	pause
	exit
)

if not exist "%STARTUP%\run_silent.vbs" (
	color 06
	echo [WARN] Service is not starting from AutoRun!
	echo [REASON] run_silent.vbs is not located in Startup folder
	echo.
	pause
	exit
)

tasklist /fi "ImageName eq %SRC%" /fo csv 2>NUL | find /I "%SRC%">NUL
if "%ERRORLEVEL%"=="0" (
	color 02
	echo [OK] Service is setuped and launched!
	echo.
	pause
	exit
)

color 06
echo [Warn] Service is setuped BUT NOT LAUNCHED
echo.
pause
exit
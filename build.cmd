@echo off
chcp 1251 > nul
cls

echo Building exe...
echo.
timeout /t 1 > nul

taskkill /f /im main.exe > nul
cls
echo Building exe...
echo.

rmdir /s /q build > nul
rmdir /s /q dist > nul
pyinstaller --onefile --clean --noconfirm main.py
copy secret.key dist

rmdir /s /q build
rmdir /s /q __pycache__

cls
timeout /t 1 > nul

echo Building ZIP file ...
echo.

xcopy scripts dist

if exist dist/build.zip del /f /q dist/build.zip
if exist dist/build.zip.tmp del /f /q dist/build.zip.tmp
rename dist\main.exe dsvl0.tracker.exe

setlocal enabledelayedexpansion
set "SEVENZIP_PATH=C:\Program Files\7-Zip\7z.exe"
if not exist "%SEVENZIP_PATH%" (
    powershell -command "Add-Type -AssemblyName PresentationFramework; [System.Windows.MessageBox]::Show('7-Zip [%SEVENZIP_PATH%] not detected','Error',[System.Windows.MessageBoxButton]::OK,[System.Windows.MessageBoxImage]::Error)"
    exit /b 1
)

cd dist
"%SEVENZIP_PATH%" a -tzip "build.zip" "dsvl0.tracker.exe" "service.remove.cmd" "service.install.cmd" "service.start.cmd" "service.stop.cmd"
cd ..
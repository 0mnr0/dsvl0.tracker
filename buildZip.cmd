@echo off
chcp 1251 > nul
cls

echo Building ZIP file ...
echo.

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
"%SEVENZIP_PATH%" a -tzip "build.zip" "dsvl0.tracker.exe" "service.remove.cmd" "service.install.cmd" "service.start.cmd" "service.stop.cmd" "service.status.cmd"
cd ..

timeout /t 1 > nul
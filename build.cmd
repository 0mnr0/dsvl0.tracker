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
xcopy scripts dist

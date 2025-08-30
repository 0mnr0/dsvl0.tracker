@echo off
chcp 1251 > nul
taskkill /f /im dsvl0.tracker.exe
msg %username% "Service stopped!"
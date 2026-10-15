@echo off
cd /d "%~dp0"
powershell.exe -NoProfile -ExecutionPolicy Bypass -File "%~dp0upload-to-github.ps1"
if errorlevel 1 (
 echo.
 echo Upload failed. Read the error above.
)
pause

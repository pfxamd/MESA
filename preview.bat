@echo off
setlocal
cd /d "%~dp0"
where py >nul 2>&1
if %errorlevel%==0 (
 start "" "http://127.0.0.1:8075/MESA/"
 py -3 serve.py
) else (
 where python >nul 2>&1
 if %errorlevel% neq 0 (
  echo Python 3 is required for this local preview.
  pause
  exit /b 1
 )
 start "" "http://127.0.0.1:8075/MESA/"
 python serve.py
)
pause

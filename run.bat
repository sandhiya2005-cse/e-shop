@echo off
echo ==========================================
echo Starting E-Commerce Application Backend
echo ==========================================

REM Check if Python is installed
python --version >nul 2>&1
IF %ERRORLEVEL% NEQ 0 (
    echo Python is not installed or not in PATH!
    pause
    exit /b
)

REM Setup virtual environment if it doesn't exist
IF NOT EXIST "venv" (
    echo Creating virtual environment...
    python -m venv venv
)

REM Activate venv
echo Activating virtual environment...
call venv\Scripts\activate.bat

REM Install dependencies
echo Installing dependencies...
cd backend
pip install -r requirements.txt

REM Seed database
echo Initializing database...
python seed.py

REM Run FastAPI server with Uvicorn
echo Starting server...
echo You can access the API docs at: http://127.0.0.1:8000/docs
echo To view the frontend, just double-click 'frontend/index.html' in your browser!
uvicorn main:app --reload

pause

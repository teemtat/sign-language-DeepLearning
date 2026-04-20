@echo off
REM ============================================================
REM Sign Language Deep Learning - Automated Setup Script (Windows)
REM ============================================================
REM This script creates a conda environment and installs all
REM dependencies needed to run the notebooks.
REM
REM Usage:
REM   setup.bat
REM
REM For macOS/Linux: Use setup.sh
REM ============================================================

setlocal enabledelayedexpansion

echo.
echo 🚀 Sign Language Deep Learning - Environment Setup
echo ==================================================

REM Check if conda is installed
where conda >nul 2>nul
if errorlevel 1 (
    echo.
    echo ❌ ERROR: Conda not found in PATH!
    echo Please install Anaconda or Miniconda first:
    echo    https://www.conda.io/projects/conda/en/latest/user-guide/install/
    echo.
    pause
    exit /b 1
)

set ENV_NAME=sign-language

echo.
echo 📦 Step 1: Creating conda environment '%ENV_NAME%' with Python 3.11...
call conda create -n %ENV_NAME% python=3.11 -y

echo.
echo 🔧 Step 2: Activating environment...
call conda activate %ENV_NAME%

echo.
echo 📚 Step 3: Installing dependencies from requirements.txt...
call python -m pip install --upgrade pip
call pip install -r requirements.txt

echo.
echo ✅ SETUP COMPLETE!
echo.
echo 📝 Next steps:
echo    1. Activate the environment:
echo       conda activate %ENV_NAME%
echo.
echo    2. Open Jupyter Notebook:
echo       jupyter notebook
echo.
echo    3. Start with: main.ipynb ^> baselineCNN.ipynb ^> camera_detect.ipynb
echo.
echo For more details, see README.md
echo.
pause

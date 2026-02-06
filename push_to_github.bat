@echo off
color 0A
echo ========================================
echo   PUSH TO GITHUB - Prabhav AI
echo ========================================
echo.

REM Check if git is installed
git --version >nul 2>&1
if errorlevel 1 (
    echo [ERROR] Git is not installed!
    echo Please install Git from: https://git-scm.com/download/win
    pause
    exit /b 1
)

echo [1/7] Initializing Git repository...
git init
if errorlevel 1 (
    echo Git already initialized or error occurred
)

echo.
echo [2/7] Adding files to staging...
git add .

echo.
echo [3/7] Creating commit...
set /p commit_msg="Enter commit message (or press Enter for default): "
if "%commit_msg%"=="" set commit_msg=Initial commit - Prabhav AI Causal Reasoning System

git commit -m "%commit_msg%"

echo.
echo [4/7] Setting up remote repository...
echo.
echo Please enter your GitHub repository URL
echo Example: https://github.com/username/prabhav-ai.git
set /p repo_url="Repository URL: "

if "%repo_url%"=="" (
    echo [ERROR] Repository URL is required!
    pause
    exit /b 1
)

git remote remove origin 2>nul
git remote add origin %repo_url%

echo.
echo [5/7] Renaming branch to main...
git branch -M main

echo.
echo [6/7] Pushing to GitHub...
echo.
echo NOTE: You may be prompted for GitHub credentials
echo If using token authentication, use your Personal Access Token as password
echo.
git push -u origin main

if errorlevel 1 (
    echo.
    echo [ERROR] Push failed!
    echo.
    echo Common solutions:
    echo 1. Check your GitHub credentials
    echo 2. Ensure repository exists on GitHub
    echo 3. Check internet connection
    echo 4. Use Personal Access Token instead of password
    echo.
    echo To create a token: GitHub Settings ^> Developer settings ^> Personal access tokens
    pause
    exit /b 1
)

echo.
echo ========================================
echo   SUCCESS! Project pushed to GitHub
echo ========================================
echo.
echo Repository: %repo_url%
echo.
echo Next steps:
echo 1. Visit your GitHub repository
echo 2. Add large files (models, data) to releases
echo 3. Update README with download links
echo 4. Add collaborators if needed
echo.
pause

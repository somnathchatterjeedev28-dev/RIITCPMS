@echo off
echo ========================================================
echo  BB COLLEGE STUDENT PORTAL MANAGEMENT SYSTEM (BBCSPMS)
echo  Banwarilal Bhalotia College • KNU Affiliated
echo ========================================================
echo.
echo Launching Backend Service on http://localhost:5000...
start "BBCSPMS Backend" cmd /c "%~dp0start-backend.bat"

echo Waiting 3 seconds for backend database initialization...
timeout /t 3 /nobreak >nul

echo Launching Frontend Web Portal on http://localhost:3000...
start "BBCSPMS Frontend" cmd /c "%~dp0start-frontend.bat"

echo.
echo ========================================================
echo System Services Initialized Successfully!
echo Frontend Portal: http://localhost:3000
echo Backend API:     http://localhost:5000/api
echo ========================================================
pause

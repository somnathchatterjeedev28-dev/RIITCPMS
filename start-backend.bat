@echo off
echo ========================================================
echo  Starting BB College Portal (BBCSPMS) Backend Server
echo  Port: 5000
echo ========================================================
cd /d "%~dp0backend"
cmd /c npm start
pause

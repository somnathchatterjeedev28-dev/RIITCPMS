@echo off
echo ========================================================
echo  Starting BB College Portal (BBCSPMS) Frontend Dev Server
echo  Port: 3000
echo ========================================================
cd /d "%~dp0frontend"
cmd /c npm run dev
pause

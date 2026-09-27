@echo off
echo ========================================================
echo  Running BBCSPMS Enterprise Test Suite
echo ========================================================
cd /d "%~dp0backend"
cmd /c npm run test
pause

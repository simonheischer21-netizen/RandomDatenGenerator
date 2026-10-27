@echo off
title RandomDaten-Generator - Installation
echo ============================================
echo   RandomDaten-Generator - Installation
echo ============================================
echo.

REM --- Python pruefen ---
where python >nul 2>nul
if %errorlevel% neq 0 (
    echo [FEHLER] Python wurde nicht gefunden!
    echo Bitte Python von https://python.org installieren
    echo (Haken bei "Add Python to PATH" setzen!)
    pause
    exit /b 1
)

REM --- Shortcut auf dem Desktop erstellen ---
set "SCRIPT=%~dp0app\generator_gui.py"
set "ICON=%~dp0app\generator_gui.py"

for /f "usebackq delims=" %%D in (`powershell -NoProfile -Command "[Environment]::GetFolderPath('Desktop)"`) do set "DESKTOP=%%D"

powershell -NoProfile -Command ^
  "$ws = New-Object -ComObject WScript.Shell; ^
   $sc = $ws.CreateShortcut('%DESKTOP%\RandomDaten-Generator.lnk'); ^
   $sc.TargetPath = 'pythonw.exe'; ^
   $sc.Arguments = '\"%SCRIPT%\"'; ^
   $sc.WorkingDirectory = '%~dp0'; ^
   $sc.Description = 'RandomDaten-Generator'; ^
   $sc.Save()"

echo.
echo [OK] Desktop-Verknuepfung erstellt!
echo [OK] Installation abgeschlossen.
echo.
pause

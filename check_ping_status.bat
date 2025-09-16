@echo off
set IP=%1
REM echo Argument received: %IP%

REM Check if IP is empty
REM if "%IP%"=="" (
REM    echo No IP address provided.
REM    exit /b 1
REM )

REM Run ping and show output
REM #echo Running: ping -n 1 %IP%

ping -n 1 %IP%

REM Show errorlevel
REM echo Errorlevel after ping: %errorlevel%

REM Check ping result
if %errorlevel%==0 (
    echo Ping to %IP% successful.
    echo %errorlevel%
    exit /b 0
) else (
    echo Ping to %IP% failed.
    echo %errorlevel%
    exit /b 1
)

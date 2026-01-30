@echo off
title Abstract Chain Claimer v2.4 - Inicializando...
echo ======================================================
echo   Abstract Chain Genesis Allocation Tool (Brasil)
echo ======================================================
echo.
echo Verificando ambiente Python...
python --version >nul 2>&1
if %errorlevel% neq 0 (
    echo [ERRO] Python nao encontrado. Por favor, instale o Python 3.10 ou superior.
    pause
    exit /b
)
echo Instalando dependencias necessarias...
pip install -r requirements.txt --quiet
echo.
echo Iniciando validador de alocacao...
python main.py
pause

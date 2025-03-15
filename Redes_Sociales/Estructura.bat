@echo off
set PROJECT_NAME=Redes_Sociales

REM Crear directorios principales
mkdir Redes_Sociales
cd Redes_Sociales
mkdir data data\raw data\processed data\external
mkdir notebooks notebooks\exploracion notebooks\limpieza notebooks\modelado
mkdir scripts
mkdir reports reports\figures

REM Crear archivos vacíos
type nul > requirements.txt
type nul > README.md
type nul > .gitignore

REM Mensaje final
echo Estructura del proyecto creada exitosamente!
pause
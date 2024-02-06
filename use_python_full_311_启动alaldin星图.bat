@echo off
set PYTHON_PATH=E:\python\python_full_311
set python_SITE_PATH=E:\python\python_full_311\Scripts

echo Setting Python path to %PYTHON_PATH%
set PATH=%PYTHON_PATH%;%python_SITE_PATH%;%PATH%

echo Python path has been set.
cd E:\github\xmo_planner
start python manage.py runserver 8000
start "" "http://localhost:8000/"


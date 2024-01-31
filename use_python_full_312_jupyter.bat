@echo off
set PYTHON_PATH=E:\python\python_full_312
set python_SITE_PATH=E:\python\python_full_312\Scripts

echo Setting Python path to %PYTHON_PATH%
set PATH=%PYTHON_PATH%;%python_SITE_PATH%;%PATH%

echo Python path has been set.
cd src_root_312
jupyter lab


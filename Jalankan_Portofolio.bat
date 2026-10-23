@echo off
title Portofolio Muhammad Mirza Wibisono
echo ========================================================
echo   Menjalankan Web Portofolio Muhammad Mirza Wibisono
echo   PWK ITS - Transportasi, GIS & Perencanaan Kota
echo ========================================================
echo.
echo Membuka browser ke http://127.0.0.1:8000 ...
start "" http://127.0.0.1:8000
echo.
echo Server aktif di http://127.0.0.1:8000
echo Tekan Ctrl+C di terminal ini untuk menghentikan server.
echo ========================================================
python -m uvicorn main:app --host 127.0.0.1 --port 8000 --reload
pause

@echo off
title Pulihkan Portofolio ke Versi Stabil
color 0A
echo ========================================================
echo   PULIHKAN PORTOFOLIO KE VERSI STABIL (21 OKT 2026)
echo ========================================================
echo.
echo Perhatian: Tindakan ini akan mengembalikan seluruh template,
echo CSS, JS, dan skrip ke kondisi saat portofolio stabil.
echo.
set /p confirm="Lanjutkan pemulihan? Ketik Y lalu Enter (atau N untuk batal): "
if /i not "%confirm%"=="Y" (
    echo.
    echo Pemulihan dibatalkan. File Anda tidak diubah.
    pause
    exit /b
)

echo.
echo Memulihkan file dari folder _backup_versi_stabil_terkunci ...
xcopy /E /I /Y "_backup_versi_stabil_terkunci\*" "."

echo.
echo ========================================================
echo   SUKSES: Seluruh file berhasil dipulihkan ke Versi Stabil!
echo   Silakan jalankan Jalankan_Portofolio.bat untuk membuka web.
echo ========================================================
pause
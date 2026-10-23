import os
import sys

# Ensure root directory is in sys.path
sys.path.insert(0, os.path.abspath("."))

from fastapi.testclient import TestClient
from main import app, load_content

client = TestClient(app)

def test_home():
    res = client.get("/")
    assert res.status_code == 200, f"Expected 200, got {res.status_code}"
    assert "Muhammad Mirza Wibisono" in res.text
    assert "Perencanaan Transportasi Wonokromo" in res.text
    assert "Terbuka untuk peluang magang" in res.text
    print("[PASS] AT01 & Home page: Passed")

def test_catalog_and_filter():
    # 1. Base catalog
    res = client.get("/karya")
    assert res.status_code == 200
    assert "Seluruh Karya" in res.text
    assert "P01" in res.text
    
    # 2. Category filter: transportasi
    res = client.get("/karya?kategori=transportasi")
    assert res.status_code == 200
    assert "Wonokromo" in res.text
    assert "Suroboyo Bus" in res.text
    
    # 3. Empty filter
    res = client.get("/karya?q=nonexistentkeywordxyz")
    assert res.status_code == 200
    assert "Belum ada karya pada pilihan ini" in res.text
    print("[PASS] AT03 & Catalog filters: Passed")

def test_project_detail_wonokromo():
    res = client.get("/karya/perencanaan-transportasi-wonokromo")
    assert res.status_code == 200
    assert "Perencanaan Transportasi Wonokromo" in res.text
    assert "PTV Visum" in res.text
    assert "Kondisi Eksisting" in res.text
    assert "Skenario Rencana" in res.text
    assert "Kontribusi Pribadi Mirza" in res.text
    print("[PASS] AT02 & Project Detail Wonokromo: Passed")

def test_cv_page():
    res = client.get("/cv")
    assert res.status_code == 200
    assert "Curriculum Vitae Resmi" in res.text
    assert "Dinas Perhubungan Sidoarjo" in res.text
    assert "ITS Eco Campus" in res.text
    assert "Unduh CV PDF" in res.text
    
    # Filtered CV
    res = client.get("/cv?filter=gis")
    assert res.status_code == 200
    assert "Sistem Informasi Perencanaan" in res.text
    print("[PASS] AT04 & CV Interactive: Passed")

def test_cv_download():
    res = client.get("/CV_Muhammad_Mirza_Wibisono.pdf")
    assert res.status_code == 200
    assert res.headers["content-type"] == "application/pdf"
    assert len(res.content) > 10000
    
    res2 = client.get("/download/cv")
    assert res2.status_code == 200
    assert res2.headers["content-type"] == "application/pdf"
    print("[PASS] AT05 & CV PDF Download: Passed")

def test_auth_protection():
    # Unauthenticated GET /admin should redirect to /admin/login
    res = client.get("/admin", follow_redirects=False)
    assert res.status_code == 303
    assert "/admin/login" in res.headers["location"]
    
    # Bad login
    res = client.post("/admin/login", data={"password": "wrongpassword"}, follow_redirects=False)
    assert res.status_code == 303
    assert "Kata+sandi+tidak+cocok" in res.headers["location"]
    
    # Good login
    session_client = TestClient(app)
    res = session_client.post("/admin/login", data={"password": "mirzawibi2026"}, follow_redirects=False)
    assert res.status_code == 303
    assert res.headers["location"] == "/admin"
    
    # Authenticated access to dashboard
    res = session_client.get("/admin")
    assert res.status_code == 200
    assert "Panel Admin Tanpa Coding" in res.text
    assert "Ringkasan Dasbor" in res.text

    # Tab projects
    res_proj = session_client.get("/admin?tab=projects")
    assert res_proj.status_code == 200
    assert "Daftar Studi Kasus" in res_proj.text
    print("[PASS] AT08 & AT11: Auth Protection and Admin Login Passed")

def test_custom_404():
    res = client.get("/karya/slug-yang-tidak-ada")
    assert res.status_code == 404
    assert "Rute Jalur Tidak Ditemukan" in res.text
    print("[PASS] AT12 & Custom 404: Passed")

if __name__ == "__main__":
    print("Running PRD verification test suite...")
    test_home()
    test_catalog_and_filter()
    test_project_detail_wonokromo()
    test_cv_page()
    test_cv_download()
    test_auth_protection()
    test_custom_404()
    print("\nALL VERIFICATION TESTS PASSED SUCCESSFULLY!")

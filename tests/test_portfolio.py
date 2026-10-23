"""
Portofolio Muhammad Mirza Wibisono - Automated Verification Suite
Follows Superpowers (TDD & Verification) + Ponytail (Lean, High-Signal) standards.
"""

import os
import sys

# Ensure project root is in sys.path
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_landing_page():
    res = client.get("/")
    assert res.status_code == 200
    assert "Muhammad Mirza Wibisono" in res.text
    assert "halte-intro.js" in res.text
    assert "Putar Ulang Intro" in res.text

def test_cv_page_and_competencies():
    res = client.get("/cv")
    assert res.status_code == 200
    assert "Matriks Kompetensi" in res.text
    assert "Pemodelan transportasi empat tahap" in res.text
    assert "Aktivitas Pembicara" in res.text
    assert "cv-filter-btn" in res.text

def test_cv_filtering():
    res = client.get("/cv?filter=transportasi-gis")
    assert res.status_code == 200
    assert "Transportasi & GIS" in res.text

def test_karya_catalog_and_slug_routing():
    res_catalog = client.get("/karya")
    assert res_catalog.status_code == 200
    assert "Katalog Studi Kasus" in res_catalog.text or "Studi Kasus" in res_catalog.text

    # Test routing by ID (P01, P02) and slug
    res_id = client.get("/karya/P01")
    assert res_id.status_code == 200
    assert "Wonokromo" in res_id.text

    res_slug = client.get("/karya/perencanaan-transportasi-wonokromo")
    assert res_slug.status_code == 200
    assert "Wonokromo" in res_slug.text

def test_static_halte_intro_assets():
    res_js = client.get("/static/halte-intro/halte-intro.js")
    assert res_js.status_code == 200
    assert len(res_js.content) > 1000

    res_css = client.get("/static/halte-intro/halte-intro.css")
    assert res_css.status_code == 200

if __name__ == "__main__":
    test_landing_page()
    test_cv_page_and_competencies()
    test_cv_filtering()
    test_karya_catalog_and_slug_routing()
    test_static_halte_intro_assets()
    print("ALL TESTS PASSED SUCCESSFULLY (5/5). Portfolio is healthy and verified!")

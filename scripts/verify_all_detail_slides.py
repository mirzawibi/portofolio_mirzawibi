import urllib.request

targets = [
    ("analisis-lokasi-sma-temanggung", ["cover-studi", "gambaran-topsis", "kontribusi-pembobotan", "slide_14", "slide_15", "slide_16"]),
    ("analisis-kekompakan-kota-malang", ["cover-studi", "gambaran-kegiatan", "kontribusi-analisis", "slide_3", "slide_4", "slide_5"]),
    ("aksesibilitas-halte-suroboyo-bus", ["cover-studi", "gambaran-umum", "kontribusi-spasial", "luaran-rekomendasi", "slide_10", "slide_11", "slide_12", "slide_13"]),
    ("analisis-urban-heat-island-surabaya", ["cover-studi", "gambaran-temporal", "kontribusi-pengolahan", "luaran-storymaps", "slide_6", "slide_7", "slide_8", "slide_9"]),
    ("perencanaan-transportasi-wonokromo", ["cover-studi", "gambaran-fourstep", "kontribusi-visum", "slide_17", "slide_18", "slide_19"]),
    ("perencanaan-kota-kebomas", ["cover-studi", "gambaran-rdtr", "kontribusi-webgis", "slide_20", "slide_21", "slide_22"]),
    ("studi-kasus-pelatihan-lokasolution", ["cover-studi", "studi-kasus", "slide_23", "slide_24"]),
]

for slug, expected_tokens in targets:
    url = f"http://127.0.0.1:8000/karya/{slug}"
    with urllib.request.urlopen(url) as res:
        assert res.status == 200
        html = res.read().decode('utf-8')
        for token in expected_tokens:
            assert token in html, f"Token {token} not found in {slug}!"
        print(f"Verified {slug}: 200 OK, all {len(expected_tokens)} slide tokens present!")

print("\nALL PROJECT DETAIL SLIDES AND SVGs ARE LIVE AND VERIFIED!")

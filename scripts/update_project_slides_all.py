import json

# Define the complete, accurately titled scenarios for all 7 projects
PROJECT_SLIDES_CONFIG = {
    "analisis-kekompakan-kota-malang": {
        "source_pages": [3, 4, 5],
        "cover_image": "/static/assets/slides/slide_3_thumb.webp",
        "scenarios": [
            {
                "id": "cover-studi",
                "label": "Judul & Konsep",
                "title": "Analisis Kekompakan Kota Malang Berdasarkan Variabel Urban Compactness",
                "image": "/static/assets/slides/slide_3.webp",
                "large_image": "/static/assets/slides/slide_3_large.webp",
                "description": "Studi evaluasi morfologi perkotaan Kota Malang untuk mengukur tingkat kekompakan wilayah di lima kecamatan berbasis variabel kepadatan, guna lahan campuran, intensifikasi, dan aksesibilitas."
            },
            {
                "id": "gambaran-kegiatan",
                "label": "Gambaran & Peta Skor",
                "title": "Gambaran Kegiatan & Peta Tingkat Kekompakan 5 Kecamatan",
                "image": "/static/assets/slides/slide_4.webp",
                "large_image": "/static/assets/slides/slide_4_large.webp",
                "description": "Pemetaan komparatif tingkat kekompakan lima kecamatan Kota Malang dengan hasil skor: Lowokwaru (33.2), Sukun (32.8), Klojen (31.9), Blimbing (29.7), dan Kedungkandang (27.4), menyoroti disparitas antara kawasan inti dan pinggiran."
            },
            {
                "id": "kontribusi-analisis",
                "label": "Analisis & Tipologi",
                "title": "Kontribusi Saya: Analisis Spasial, Skoring Sturges, Matriks SWOT & Peta Tipologi",
                "image": "/static/assets/slides/slide_5.webp",
                "large_image": "/static/assets/slides/slide_5_large.webp",
                "description": "Pengolahan data kuesioner sembilan indikator menggunakan rumus Sturges, kuantifikasi matriks IFAS-EFAS SWOT, serta transformasi hasil numerik ke dalam peta delineasi dan tipologi kekompakan spasial di ArcGIS."
            }
        ]
    },
    "analisis-urban-heat-island-surabaya": {
        "source_pages": [6, 7, 8, 9],
        "cover_image": "/static/assets/slides/slide_6_thumb.webp",
        "scenarios": [
            {
                "id": "cover-studi",
                "label": "Judul & Kerangka",
                "title": "Analisis Pola UHI Berdasarkan LST dan NDVI Citra Landsat 8 di Kota Surabaya",
                "image": "/static/assets/slides/slide_6.webp",
                "large_image": "/static/assets/slides/slide_6_large.webp",
                "description": "Kajian spasio-temporal dinamika pulau panas perkotaan (Urban Heat Island) Kota Surabaya dengan memanfaatkan data penginderaan jauh satelit Landsat 8."
            },
            {
                "id": "gambaran-temporal",
                "label": "Data Landsat Temporal",
                "title": "Gambaran Kegiatan & Data Landsat 8 Temporal Multi-Tahun (2015-2024)",
                "image": "/static/assets/slides/slide_7.webp",
                "large_image": "/static/assets/slides/slide_7_large.webp",
                "description": "Kompilasi dan pemotongan citra Landsat 8 OLI/TIRS USGS periode September 2015, 2018, 2021, dan 2024 untuk memetakan alih fungsi lahan dan kenaikan suhu mikro kawasan perkotaan."
            },
            {
                "id": "kontribusi-pengolahan",
                "label": "Pengolahan Spektral",
                "title": "Kontribusi Saya: Pemrosesan Citra Landsat (NDVI, LST, dan UHI) di ArcGIS",
                "image": "/static/assets/slides/slide_8.webp",
                "large_image": "/static/assets/slides/slide_8_large.webp",
                "description": "Peran ketua tim dalam kalkulasi indeks vegetasi (NDVI) Band 4 & 5, konversi radiometrik Band 10 menjadi Land Surface Temperature (LST), serta pemodelan anomali UHI berbasis standar deviasi."
            },
            {
                "id": "luaran-storymaps",
                "label": "Luaran & StoryMaps",
                "title": "Tahapan Kegiatan & Luaran Penelitian: WebGIS ArcGIS StoryMaps",
                "image": "/static/assets/slides/slide_9.webp",
                "large_image": "/static/assets/slides/slide_9_large.webp",
                "description": "Alur kalkulasi spektral TOA hingga penyajian perbandingan spasial UHI 2015 vs 2024 yang diintegrasikan ke dalam media interaktif ArcGIS StoryMaps untuk edukasi publik dan rekomendasi RTH."
            }
        ]
    },
    "aksesibilitas-halte-suroboyo-bus": {
        "source_pages": [10, 11, 12, 13],
        "cover_image": "/static/assets/slides/slide_10_thumb.webp",
        "scenarios": [
            {
                "id": "cover-studi",
                "label": "Judul & Koridor",
                "title": "Analisis Aksesibilitas Evaluasi & Optimalisasi Penempatan Halte Suroboyo Bus",
                "image": "/static/assets/slides/slide_10.webp",
                "large_image": "/static/assets/slides/slide_10_large.webp",
                "description": "Studi evaluasi komprehensif keterjangkauan halte Suroboyo Bus di Surabaya Timur untuk mendorong integrasi antarmoda dan peningkatan keterpilihan angkutan massal."
            },
            {
                "id": "gambaran-umum",
                "label": "Sebaran 77 Halte",
                "title": "Gambaran Umum & Evaluasi Jangkauan 77 Halte Eksisting Surabaya Timur",
                "image": "/static/assets/slides/slide_11.webp",
                "large_image": "/static/assets/slides/slide_11_large.webp",
                "description": "Pemetaan sebaran 77 titik halte eksisting rute R1 dan SBT di koridor arteri Jl. Pucang Anom serta identifikasi ketimpangan aksesibilitas fisik bagi permukiman di kawasan pinggiran timur."
            },
            {
                "id": "kontribusi-spasial",
                "label": "Metode UNA & TOD",
                "title": "Kontribusi Saya: Integrasi Dasymetric, UNA, Huff Model, dan OD Cost Matrix",
                "image": "/static/assets/slides/slide_12.webp",
                "large_image": "/static/assets/slides/slide_12_large.webp",
                "description": "Kepemimpinan tim dalam membangun model keterjangkauan nyata melalui Urban Network Analysis (UNA), pemodelan gravitasi Huff, matriks biaya asal-tujuan (OD Cost Matrix), serta integrasi prinsip TOD."
            },
            {
                "id": "luaran-rekomendasi",
                "label": "Peta Rekomendasi Halte",
                "title": "Luaran Kegiatan: Peta Indeks Aksesibilitas & Indeks Kebutuhan Halte",
                "image": "/static/assets/slides/slide_13.webp",
                "large_image": "/static/assets/slides/slide_13_large.webp",
                "description": "Diagram alir tahapan analisis spasial dan perumusan zona prioritas penambahan halte baru pada kawasan berkepadatan tinggi namun beraksesibilitas rendah di Surabaya Timur."
            }
        ]
    },
    "analisis-lokasi-sma-temanggung": {
        "source_pages": [14, 15, 16],
        "cover_image": "/static/assets/slides/slide_14_thumb.webp",
        "scenarios": [
            {
                "id": "cover-studi",
                "label": "Judul & Peta Tematik",
                "title": "Analisis Lokasi Fasilitas Pendidikan SMA di Kabupaten Temanggung",
                "image": "/static/assets/slides/slide_14.webp",
                "large_image": "/static/assets/slides/slide_14_large.webp",
                "description": "Studi penentuan prioritas lokasi pembangunan SMA baru di Kabupaten Temanggung guna menjawab disparitas aksesibilitas pendidikan menengah atas antarwilayah kecamatan."
            },
            {
                "id": "gambaran-topsis",
                "label": "Metodologi & TOPSIS",
                "title": "Gambaran Kegiatan, Alur Delphi-AHP-TOPSIS, & Hasil Pemeringkatan 8 Alternatif",
                "image": "/static/assets/slides/slide_15.webp",
                "large_image": "/static/assets/slides/slide_15_large.webp",
                "description": "Alur metodologi Delphi, AHP 11 kriteria, dan evaluasi TOPSIS yang menetapkan Kecamatan Ngadirejo sebagai lokasi prioritas terbaik (ranking 1 dengan skor 0.6766) disusul Kedu dan Parakan."
            },
            {
                "id": "kontribusi-pembobotan",
                "label": "Pembobotan & 9 Peta",
                "title": "Kontribusi Saya: Pembobotan Delphi/AHP 11 Variabel & Analisis 9 Peta Tematik",
                "image": "/static/assets/slides/slide_16.webp",
                "large_image": "/static/assets/slides/slide_16_large.webp",
                "description": "Peran ketua tim dalam merumuskan bobot 11 kriteria Delphi/AHP, mengarahkan quality control tim, dan mengeksekusi sembilan peta tematik spasial (lereng, kerawanan bencana, kemiskinan, demografi, pola ruang) menggunakan Kernel Density dan SNA."
            }
        ]
    },
    "perencanaan-transportasi-wonokromo": {
        "source_pages": [17, 18, 19],
        "cover_image": "/static/assets/slides/slide_17_thumb.webp",
        "scenarios": [
            {
                "id": "cover-studi",
                "label": "Judul & Koridor",
                "title": "Perencanaan Transportasi Wilayah Wonokromo",
                "image": "/static/assets/slides/slide_17.webp",
                "large_image": "/static/assets/slides/slide_17_large.webp",
                "description": "Kajian rekayasa dan pemodelan transportasi multi-moda kawasan Wonokromo Surabaya berbasis Four-Step Model dan simulasi mikrosimulasi lalu lintas."
            },
            {
                "id": "gambaran-fourstep",
                "label": "Four-Step Model",
                "title": "Gambaran Kegiatan, Pemodelan 4-Step Model, & Trip Assignment Rencana",
                "image": "/static/assets/slides/slide_18.webp",
                "large_image": "/static/assets/slides/slide_18_large.webp",
                "description": "Aplikasi Four-Step Model (Trip Generation, Trip Distribution, Mode Choice, Trip Assignment) untuk mengidentifikasi 8 ruas jalan kritis dan merancang 5 rute feeder serta 25 halte transit."
            },
            {
                "id": "kontribusi-visum",
                "label": "Pemodelan PTV Visum",
                "title": "Kontribusi Saya: Pemodelan TAZ & Simulasi Trip Assignment PTV Visum",
                "image": "/static/assets/slides/slide_19.webp",
                "large_image": "/static/assets/slides/slide_19_large.webp",
                "description": "Peran ketua tim dalam membangun basemap TAZ, kalibrasi matriks asal-tujuan (OD Matrix), dan simulasi pembebanan jaringan pada 3 skenario (eksisting, proyeksi, rencana) menggunakan PTV Visum dan ArcGIS."
            }
        ]
    },
    "perencanaan-kota-kebomas": {
        "source_pages": [20, 21, 22],
        "cover_image": "/static/assets/slides/slide_20_thumb.webp",
        "scenarios": [
            {
                "id": "cover-studi",
                "label": "Judul & Skyline",
                "title": "Perencanaan Kota Wilayah Kebomas",
                "image": "/static/assets/slides/slide_20.webp",
                "large_image": "/static/assets/slides/slide_20_large.webp",
                "description": "Penyusunan Rencana Detail Tata Ruang (RDTR) Kecamatan Kebomas Gresik sebagai simpul pertumbuhan industri, hunian, dan warisan budaya yang terintegrasi."
            },
            {
                "id": "gambaran-rdtr",
                "label": "Struktur & Pola Ruang",
                "title": "Gambaran Kegiatan: Rencana Struktur Ruang, Pola Ruang, & Kawasan Prioritas",
                "image": "/static/assets/slides/slide_21.webp",
                "large_image": "/static/assets/slides/slide_21_large.webp",
                "description": "Formulasi arahan hierarki pusat pelayanan (SWP A sebagai PPK), jaringan prasarana transportasi, alokasi pola ruang zona lindung dan budidaya, serta visi-misi pembangunan terpadu."
            },
            {
                "id": "kontribusi-webgis",
                "label": "Fisik Dasar & WebGIS",
                "title": "Kontribusi Saya: Analisis Fisik Dasar, Mitigasi Multibencana, & WebGIS",
                "image": "/static/assets/slides/slide_22.webp",
                "large_image": "/static/assets/slides/slide_22_large.webp",
                "description": "Kepemimpinan 10 anggota lintas 8 bidang keahlian, analisis daya dukung lahan dan zonasi rawan bencana di 21 desa/kelurahan, perhitungan KDB/KLB/KDH/GSB, serta perancangan WebGIS interaktif."
            }
        ]
    },
    "studi-kasus-pelatihan-lokasolution": {
        "source_pages": [23, 24],
        "cover_image": "/static/assets/slides/slide_23_thumb.webp",
        "scenarios": [
            {
                "id": "cover-studi",
                "label": "Judul & Identitas",
                "title": "Student Analyst LokaSolution - ITB",
                "image": "/static/assets/slides/slide_23.webp",
                "large_image": "/static/assets/slides/slide_23_large.webp",
                "description": "Program intensif pelatihan analisis konsultasi manajemen dan perencanaan strategis untuk pemecahan masalah bisnis serta tata ruang."
            },
            {
                "id": "studi-kasus",
                "label": "Kasus & Rekomendasi",
                "title": "Studi Kasus Nyata: PT Jasa Marga & Nusantara Living (MECE & Issue Tree)",
                "image": "/static/assets/slides/slide_24.webp",
                "large_image": "/static/assets/slides/slide_24_large.webp",
                "description": "Penyelesaian 6 studi kasus menggunakan kerangka kerja MECE, dekomposisi Issue Tree, analisis kelayakan investasi (NPV, ROI, TAM-SAM-SOM), serta perumusan rekomendasi konsultasi berstandar industri."
            }
        ]
    }
}

with open('data/content.json', 'r', encoding='utf-8') as f:
    content = json.load(f)

for project in content['projects']:
    slug = project.get('slug')
    if slug in PROJECT_SLIDES_CONFIG:
        cfg = PROJECT_SLIDES_CONFIG[slug]
        project['source_pages'] = cfg['source_pages']
        project['cover_image'] = cfg['cover_image']
        project['scenarios'] = cfg['scenarios']
        print(f"Updated project {slug}: {len(cfg['scenarios'])} scenarios, source_pages={cfg['source_pages']}")

with open('data/content.json', 'w', encoding='utf-8') as f:
    json.dump(content, f, ensure_ascii=False, indent=2)

print("\nSUCCESS: data/content.json updated with complete and accurately titled slides!")

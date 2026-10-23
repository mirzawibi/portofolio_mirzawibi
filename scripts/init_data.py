import json
import os
import shutil
from datetime import datetime

data = {
    "profile": {
        "name": "Muhammad Mirza Wibisono",
        "short_name": "Mirza",
        "title": "Mahasiswa Perencanaan Wilayah dan Kota (PWK)",
        "institution": "Institut Teknologi Sepuluh Nopember (ITS)",
        "status": "Mahasiswa semester 5",
        "location": "Surabaya, Indonesia",
        "field": "Analisis Spasial, Transportasi, dan Perencanaan Kota",
        "hero_headline": "Saya memadukan analisis spasial, pemodelan transportasi, dan kepemimpinan tim untuk memahami persoalan kota serta menyusun rekomendasi perencanaan.",
        "bio": "Mahasiswa Perencanaan Wilayah dan Kota ITS semester 5 yang mendalami analisis spasial geospasial, pemodelan transportasi empat tahap, formulasi rencana detail tata ruang, serta kepemimpinan tim lintas bidang. Menggabungkan penguasaan teknis software analisis wilayah dengan pengalaman kepemimpinan organisasi kemahasiswaan dan asisten laboratorium.",
        "internship_status": "Terbuka untuk peluang magang",
        "internship_period": "Fleksibel / Penugasan Magang 2026",
        "avatar_url": "/static/assets/slides/slide_2_thumb.webp",
        "hero_cover_url": "/static/assets/slides/slide_1_large.webp",
        "updated_at": "2026-10-21"
    },
    "contact": {
        "email": "mirzawibi@gmail.com",
        "linkedin": "https://www.linkedin.com/in/mirzawibi",
        "phone": "0895367056584",
        "whatsapp_enabled": False,
        "location": "Surabaya, Jawa Timur, Indonesia"
    },
    "resume_asset": {
        "file_path": "/CV_Muhammad_Mirza_Wibisono.pdf",
        "filename": "CV_Muhammad_Mirza_Wibisono.pdf",
        "filesize_str": "81 KB",
        "updated_at": "20 Oktober 2026",
        "version": "1.0",
        "is_synced": True
    },
    "categories": [
        {"id": "semua", "label": "Semua Karya", "count": 7},
        {"id": "transportasi", "label": "Transportasi & Mobilitas", "count": 2},
        {"id": "gis", "label": "GIS & Analisis Spasial", "count": 6},
        {"id": "perencanaan-kota", "label": "Perencanaan Kota / Wilayah", "count": 2},
        {"id": "konsultasi", "label": "Konsultasi & Problem Solving", "count": 1}
    ],
    "projects": [
        {
            "id": "P01",
            "slug": "perencanaan-transportasi-wonokromo",
            "title": "Perencanaan Transportasi Wonokromo",
            "categories": ["transportasi", "gis"],
            "project_type": "Proyek Akademik",
            "location": "Wonokromo, Surabaya",
            "year": "2025–2026",
            "featured": True,
            "sort_order": 1,
            "status": "published",
            "cover_image": "/static/assets/slides/slide_17_thumb.webp",
            "source_pages": [17, 18, 19],
            "role_summary": "Ketua Tim & Analisis Pemodelan Transportasi (TAZ & Trip Assignment)",
            "my_contributions": [
                "Memimpin tim studi transportasi kawasan Wonokromo: manajemen jadwal kerja, alur pembagian tugas, dan penjaminan mutu analisis.",
                "Menentukan pembagian Traffic Analysis Zone (TAZ) dan menyiapkan basemap jaringan jalan presisi tinggi.",
                "Mengoperasikan software PTV Visum untuk menjalankan pemodelan 4 tahap: trip generation, distribution, mode choice, dan trip assignment.",
                "Membandingkan hasil pembebanan volume jalan pada skenario Eksisting, Proyeksi pertumbuhan tanpa intervensi, dan Skenario Rencana intervensi.",
                "Menyusun indikasi program teknis: penanganan 8 ruas kritis, usulan 5 rute feeder transit, dan 25 titik halte integrasi."
            ],
            "team_deliverables": [
                "Laporan komprehensif kajian perencanaan transportasi terpadu simpul Wonokromo.",
                "Matriks Asal-Tujuan (OD Matrix) dan peta sebaran bangkitan/tarikan pergerakan.",
                "Album peta hasil pembebanan jaringan lalu lintas (VCR) pada berbagai skenario.",
                "Konsep penataan transit oriented circulation menghubungkan stasiun kereta, terminal bus, dan halte feeder."
            ],
            "tools": ["PTV Visum", "QGIS", "ArcGIS", "Microsoft Excel"],
            "summary": "Menyusun skenario pengembangan jaringan transportasi Wonokromo dan membandingkan hasil pembebanan perjalanan (trip assignment) menggunakan model empat tahap pada PTV Visum untuk merumuskan penanganan 8 ruas kritis serta jaringan feeder transit.",
            "problem_statement": "Wonokromo merupakan pintu gerbang mobilitas komuter Surabaya selatan dengan konflik pergerakan tinggi antara kendaraan pribadi dan angkutan umum, kepadatan kapasitas jalan mendekati jenuh pada jam puncak, dan perlunya integrasi antarmoda transportasi perkotaan.",
            "methodology": "Pendekatan Model Transportasi 4 Tahap: 1) Bangkitan perjalanan (trip generation) berbasis parameter sosio-ekonomi zona TAZ; 2) Distribusi pergerakan dengan Model Gravitasi berkendala ganda; 3) Pemilihan moda (mode choice) mengestimasi peralihan angkutan umum; 4) Pembebanan jaringan (trip assignment) pada software PTV Visum.",
            "scenarios": [
                {
                    "id": "eksisting",
                    "label": "Kondisi Eksisting",
                    "title": "Pembebanan Jaringan Eksisting Kawasan Wonokromo",
                    "image": "/static/assets/slides/slide_17.webp",
                    "large_image": "/static/assets/slides/slide_17_large.webp",
                    "description": "Peta pembebanan jalan eksisting memperlihatkan 8 ruas kritis dengan rasio volume terhadap kapasitas (V/C Ratio) tinggi dan antrean panjang pada simpul persimpangan utama."
                },
                {
                    "id": "proyeksi",
                    "label": "Proyeksi Pertumbuhan",
                    "title": "Proyeksi Beban Jaringan Tanpa Intervensi",
                    "image": "/static/assets/slides/slide_18.webp",
                    "large_image": "/static/assets/slides/slide_18_large.webp",
                    "description": "Simulasi proyeksi beban masa depan apabila tidak dilakukan perbaikan jaringan (do-nothing scenario), yang mengakibatkan kemacetan meluas ke koridor jalan penghubung sekunder."
                },
                {
                    "id": "rencana",
                    "label": "Skenario Rencana",
                    "title": "Skenario Rencana: Integrasi Feeder & Rekayasa Jaringan",
                    "image": "/static/assets/slides/slide_19.webp",
                    "large_image": "/static/assets/slides/slide_19_large.webp",
                    "description": "Hasil pemodelan intervensi skenario rencana: penambahan 5 rute feeder penghubung stasiun, penataan 25 titik halte, serta perbaikan geometri simpang yang meratakan beban lalu lintas."
                }
            ],
            "metrics": [
                {"label": "Ruas Jalan Kritis", "value": "8 Koridor", "context": "Hasil pemodelan VCR"},
                {"label": "Rute Feeder Usulan", "value": "5 Trayek", "context": "Konektivitas antarmoda"},
                {"label": "Halte Direkomendasikan", "value": "25 Titik", "context": "Jangkauan pejalan kaki"}
            ],
            "recommendations": "Memprioritaskan penataan koridor intermoda di sekitar Stasiun Wonokromo, implementasi feeder terdedikasi, serta revitalisasi trotoar dan fasilitas transit pejalan kaki.",
            "related_project_ids": ["P02", "P03"]
        },
        {
            "id": "P02",
            "slug": "aksesibilitas-halte-suroboyo-bus",
            "title": "Aksesibilitas Halte Suroboyo Bus di Surabaya Timur",
            "categories": ["transportasi", "gis"],
            "project_type": "Proyek Riset Spasial",
            "location": "Surabaya Timur, Jawa Timur",
            "year": "2025",
            "featured": True,
            "sort_order": 2,
            "status": "published",
            "cover_image": "/static/assets/slides/slide_10_thumb.webp",
            "source_pages": [10, 11, 12, 13],
            "role_summary": "Ketua Tim & Analis Spasial Integratif (UNA, Dasymetric, OD Cost Matrix)",
            "my_contributions": [
                "Memimpin integrasi metodologi evaluasi aksesibilitas angkutan umum massal Surabaya Timur.",
                "Mengolah pemetaan dasimetrik (Dasymetric Mapping) untuk mendistribusikan data kependudukan ke blok terbangun secara akurat.",
                "Melakukan pemodelan spasial Urban Network Analysis (UNA) dan Origin-Destination Cost Matrix untuk menghitung jangkauan berjalan kaki ke 77 halte eksisting.",
                "Merumuskan indeks kebutuhan halte baru melalui normalisasi indikator dan spatial multi-criteria overlay.",
                "Menghasilkan peta rekomendasi prioritas relokasi dan penambahan halte baru pada koridor pelayanan rendah."
            ],
            "team_deliverables": [
                "Album peta catchment area dan jangkauan berjalan kaki 400m–800m dari 77 halte eksisting.",
                "Peta sebaran indeks aksesibilitas halte di wilayah Surabaya Timur.",
                "Peta sintesis indeks kebutuhan dan lokasi prioritas penambahan halte baru.",
                "Laporan rekomendasi kebijakan optimalisasi rute dan fasilitas transit Suroboyo Bus."
            ],
            "tools": ["ArcGIS Pro", "Urban Network Analysis (UNA)", "QGIS", "Model Huff", "Excel"],
            "summary": "Mengevaluasi kesesuaian penempatan 77 halte Suroboyo Bus eksisting di Surabaya Timur terhadap distribusi populasi dan jaringan jalan menggunakan Urban Network Analysis (UNA), Dasymetric Mapping, dan OD Cost Matrix guna merumuskan indeks kebutuhan halte baru.",
            "problem_statement": "Distribusi halte angkutan umum kerap tidak sejalan dengan kepadatan penduduk riil dan pola jaringan jalan pejalan kaki, memunculkan gap aksesibilitas di kawasan permukiman padat Surabaya Timur.",
            "methodology": "Kombinasi dasymetric mapping kepadatan penduduk, pemodelan jangkauan jaringan UNA (Reach & Gravity Index), dan analisis jarak tempuh riil menggunakan Network Analyst OD Cost Matrix yang dioverlay dengan model gravitasi Huff.",
            "scenarios": [
                {
                    "id": "aksesibilitas",
                    "label": "Indeks Aksesibilitas Halte",
                    "title": "Peta Indeks Aksesibilitas Jaringan Halte Eksisting",
                    "image": "/static/assets/slides/slide_10.webp",
                    "large_image": "/static/assets/slides/slide_10_large.webp",
                    "description": "Visualisasi jangkauan 77 halte eksisting Surabaya Timur menggunakan model jarak jaringan pejalan kaki, menunjukkan area berjarak tempuh memadai dan zona blank spot."
                },
                {
                    "id": "kebutuhan",
                    "label": "Indeks Kebutuhan Halte",
                    "title": "Peta Indeks Kebutuhan & Prioritas Penambahan Halte",
                    "image": "/static/assets/slides/slide_12.webp",
                    "large_image": "/static/assets/slides/slide_12_large.webp",
                    "description": "Hasil pembobotan spasial antara kepadatan penduduk dasimetrik dan jarak aksesibilitas halte, mengidentifikasi titik prioritas tinggi untuk penempatan halte pengumpan baru."
                }
            ],
            "metrics": [
                {"label": "Objek Halte Eksisting", "value": "77 Halte", "context": "Dievaluasi di Surabaya Timur"},
                {"label": "Metode Analisis", "value": "UNA + Huff + Dasymetric", "context": "Pemodelan jaringan spasial"}
            ],
            "recommendations": "Menambah titik perhentian bus di zona prioritas tinggi Surabaya Timur dan menata jalur pejalan kaki yang aman menuju halte dalam radius 400 meter.",
            "related_project_ids": ["P01", "P04"]
        },
        {
            "id": "P03",
            "slug": "perencanaan-kota-kebomas",
            "title": "Perencanaan Kota Kebomas",
            "categories": ["perencanaan-kota", "gis"],
            "project_type": "Proyek Studio Perencanaan",
            "location": "Kecamatan Kebomas, Kabupaten Gresik",
            "year": "2025",
            "featured": True,
            "sort_order": 3,
            "status": "published",
            "cover_image": "/static/assets/slides/slide_20_thumb.webp",
            "source_pages": [20, 21, 22],
            "role_summary": "Ketua Tim Studio Perencanaan (10 Anggota, 8 Bidang Sektoral, 16 Minggu)",
            "my_contributions": [
                "Memimpin dan mengkoordinasikan 10 anggota tim lintas 8 bidang analisis selama 16 minggu pengerjaan studio perencanaan wilayah dan kota.",
                "Melakukan analisis fisik dasar, tutupan vegetasi, dan permodelan kerentanan multibencana (banjir, penurunan tanah) menggunakan GIS dan Google Earth Engine.",
                "Mengintegrasikan seluruh hasil analisis sektoral (demografi, ekonomi, fisik, kebencanaan, transportasi) ke dalam formulasi Struktur Ruang dan Pola Ruang.",
                "Menyusun konsep pusat pelayanan berjenjang dan alokasi zonasi peruntukan ruang untuk 21 desa/kelurahan di Kecamatan Kebomas.",
                "Mempersiapkan visualisasi kartografis dan data spasial geodatabase untuk kebutuhan WebGIS."
            ],
            "team_deliverables": [
                "Dokumen komprehensif usulan Rencana Tata Ruang Kawasan Perkotaan Kebomas (21 desa/kelurahan).",
                "Album peta perencanaan resolusi tinggi: Peta Analisis Fisik & Bencana, Peta Struktur Ruang, dan Peta Pola Ruang.",
                "Matriks rencana aksi dan pentahapan program pembangunan berjangka 20 tahun.",
                "Materi presentasi sidang studio di hadapan tim penguji dan dosen pembimbing."
            ],
            "tools": ["ArcGIS Pro", "Google Earth Engine", "QGIS", "AutoCAD", "Excel"],
            "summary": "Memimpin tim 10 orang selama 16 minggu dalam penyusunan rencana detail tata ruang untuk 21 desa/kelurahan di Kebomas Gresik, memetakan risiko multibencana dan fisik dasar, serta merumuskan arahan struktur ruang dan pola ruang yang berkelanjutan.",
            "problem_statement": "Kecamatan Kebomas mengalami tekanan urbanisasi dan industrialisasi pesat yang memicu alih fungsi lahan resapan, potensi risiko banjir dan kerentanan lingkungan, serta ketidakseimbangan sistem transportasi perkotaan.",
            "methodology": "Pendekatan perencanaan tata ruang berbasis daya dukung lingkungan: sintesis analisis fisik dasar & kebencanaan, pemodelan proyeksi kebutuhan ruang 20 tahun, dan perumusan arahan struktur pusat pelayanan serta zonasi pola ruang ramah lingkungan.",
            "scenarios": [
                {
                    "id": "analisis",
                    "label": "Analisis Wilayah & Bencana",
                    "title": "Peta Analisis Fisik Dasar & Kerentanan Multibencana",
                    "image": "/static/assets/slides/slide_20.webp",
                    "large_image": "/static/assets/slides/slide_20_large.webp",
                    "description": "Pemetaan spasial geologi, hidrologi, kelerengan lahan, dan zonasi risiko multibencana di seluruh 21 desa/kelurahan Kecamatan Kebomas."
                },
                {
                    "id": "struktur",
                    "label": "Rencana Struktur Ruang",
                    "title": "Arahan Struktur Ruang & Pusat Pelayanan",
                    "image": "/static/assets/slides/slide_21.webp",
                    "large_image": "/static/assets/slides/slide_21_large.webp",
                    "description": "Konsep hierarki sistem pusat pelayanan perkotaan (PKL, PPK, PaL) dan jaringan infrastruktur jalan arteri, kolektor, dan lokal."
                },
                {
                    "id": "pola",
                    "label": "Rencana Pola Ruang",
                    "title": "Arahan Pola Ruang (Zona Lindung & Budi Daya)",
                    "image": "/static/assets/slides/slide_22.webp",
                    "large_image": "/static/assets/slides/slide_22_large.webp",
                    "description": "Alokasi peruntukan ruang zonasi permukiman, industri ramah lingkungan, ruang terbuka hijau perlindungan sempadan, dan fasilitas umum."
                }
            ],
            "metrics": [
                {"label": "Cakupan Studi", "value": "21 Desa/Kelurahan", "context": "Kecamatan Kebomas, Gresik"},
                {"label": "Durasi Studio", "value": "16 Minggu", "context": "10 anggota, 8 bidang analisis"}
            ],
            "recommendations": "Menerapkan pembatasan pembangunan pada zona kerentanan bencana tinggi, mengembangkan koridor hijau sempadan, serta memperkuat konektivitas antar-pusat permukiman dan zona kerja industri.",
            "related_project_ids": ["P01", "P04"]
        },
        {
            "id": "P04",
            "slug": "analisis-urban-heat-island-surabaya",
            "title": "Analisis Urban Heat Island Surabaya",
            "categories": ["gis", "lingkungan"],
            "project_type": "Riset Penginderaan Jauh Lingkungan",
            "location": "Kota Surabaya, Jawa Timur",
            "year": "2024–2025",
            "featured": False,
            "sort_order": 4,
            "status": "published",
            "cover_image": "/static/assets/slides/slide_6_thumb.webp",
            "source_pages": [6, 7, 8, 9],
            "role_summary": "Ketua Tim Riset Penginderaan Jauh & WebGIS Lingkungan",
            "my_contributions": [
                "Merancang arsitektur pengolahan citra satelit Landsat 8 TIRS/OLI multitemporal di Google Earth Engine (GEE).",
                "Menghitung Normalized Difference Vegetation Index (NDVI) untuk mendeteksi dinamika tutupan kanopi vegetasi perkotaan.",
                "Mengekstraksi Land Surface Temperature (LST) melalui kalibrasi radiometrik, emisivitas permukaan, dan konversi suhu kecerahan termal.",
                "Memetakan intensitas fenomena Urban Heat Island (UHI) dan menganalisis korelasi spasial spasial-temporal antara kepadatan bangunan dengan peningkatan temperatur mikro.",
                "Mengembangkan purwarupa dashboard WebGIS untuk memvisualisasikan dinamika suhu kota kepada publik."
            ],
            "team_deliverables": [
                "Seri peta spasial multitemporal NDVI, LST, dan hotspot UHI Kota Surabaya.",
                "Model regresi spasial hubungan kerapatan vegetasi terhadap variasi suhu permukaan.",
                "Platform WebGIS interaktif pemantauan iklim mikro perkotaan."
            ],
            "tools": ["Google Earth Engine", "Landsat 8 OLI/TIRS", "QGIS", "Python", "WebGIS"],
            "summary": "Membaca dinamika hubungan pola vegetasi (NDVI), suhu permukaan (LST), dan fenomena Urban Heat Island (UHI) di Kota Surabaya dari citra satelit multitemporal menggunakan Google Earth Engine dan WebGIS.",
            "problem_statement": "Perkembangan kawasan terbangun di Kota Surabaya memicu penurunan drastis luas ruang terbuka hijau dan meningkatkan akumulasi panas perkotaan yang berdampak pada kenyamanan termal dan konsumsi energi warga.",
            "methodology": "Pemrosesan citra satelit Landsat 8 di GEE: kalibrasi TOA, perhitungan indeks vegetasi NDVI, estimasi emisivitas permukaan tanah, ekstraksi suhu permukaan tanah (LST) dari saluran termal, dan deteksi anomali UHI di atas rata-rata suhu wilayah.",
            "scenarios": [
                {
                    "id": "ndvi",
                    "label": "Kerapatan Vegetasi (NDVI)",
                    "title": "Peta Kerapatan Vegetasi (NDVI) Multitemporal Surabaya",
                    "image": "/static/assets/slides/slide_6.webp",
                    "large_image": "/static/assets/slides/slide_6_large.webp",
                    "description": "Visualisasi sebaran indeks vegetasi NDVI yang memperlihatkan degradasi ruang hijau di kawasan pusat kota dan pemusatan kanopi vegetasi di kawasan pinggiran."
                },
                {
                    "id": "lst",
                    "label": "Suhu Permukaan (LST)",
                    "title": "Peta Distribusi Suhu Permukaan Tanah (LST)",
                    "image": "/static/assets/slides/slide_7.webp",
                    "large_image": "/static/assets/slides/slide_7_large.webp",
                    "description": "Peta sebaran suhu permukaan termal yang mengidentifikasi konsentrasi suhu tinggi pada kawasan industri, pergudangan, dan perumahan beratap seng/padat."
                },
                {
                    "id": "uhi",
                    "label": "Zona Hotspot UHI",
                    "title": "Peta Anomali Urban Heat Island (UHI)",
                    "image": "/static/assets/slides/slide_9.webp",
                    "large_image": "/static/assets/slides/slide_9_large.webp",
                    "description": "Hasil klasifikasi tingkat keparahan pulau panas perkotaan, membuktikan secara kuantitatif efektivitas koridor vegetasi dalam mereduksi suhu lingkungan."
                }
            ],
            "metrics": [
                {"label": "Resolusi Sensor Citra", "value": "30 Meter (Landsat 8)", "context": "Saluran optik & termal TIRS"},
                {"label": "Engine Pengolahan", "value": "Google Earth Engine", "context": "Cloud raster computing"}
            ],
            "recommendations": "Meningkatkan rasio RTH pada zona hotspot UHI kritis di Surabaya pusat/timur dan menerapkan strategi atap sejuk (cool roofs) pada bangunan industri/komersial.",
            "related_project_ids": ["P02", "P03"]
        },
        {
            "id": "P05",
            "slug": "analisis-lokasi-sma-temanggung",
            "title": "Analisis Lokasi SMA di Kabupaten Temanggung",
            "categories": ["perencanaan-wilayah", "gis"],
            "project_type": "Proyek Analisis Kebijakan Spasial",
            "location": "Kabupaten Temanggung, Jawa Tengah",
            "year": "2024–2025",
            "featured": False,
            "sort_order": 5,
            "status": "published",
            "cover_image": "/static/assets/slides/slide_14_thumb.webp",
            "source_pages": [14, 15, 16],
            "role_summary": "Ketua Tim & Analis Spasial Multikriteria (Delphi, AHP, TOPSIS)",
            "my_contributions": [
                "Mengarahkan metodologi penetapan prioritas lokasi fasilitas pendidikan menengah atas di Kabupaten Temanggung.",
                "Menyusun variabel kriteria: kepadatan populasi usia sekolah, jangkauan SMA eksisting, kelerengan kontur, dan aksesibilitas jaringan jalan.",
                "Menghitung pembobotan hirarki Analytic Hierarchy Process (AHP) dari konsensus pakar metode Delphi.",
                "Mengoperasikan model pemeringkatan multi-kriteria spasial TOPSIS (Technique for Order Preference by Similarity to Ideal Solution).",
                "Menyajikan hasil rekomendasi alternatif prioritas lokasi di Kecamatan Ngadirejo dengan kedekatan solusi ideal 0,6766."
            ],
            "team_deliverables": [
                "Peta jangkauan layanan SMA eksisting dengan analisis service area jaringan jalan.",
                "Peta kesesuaian lahan spasial untuk fasilitas pendidikan menengah baru.",
                "Matriks AHP pembobotan kriteria dan tabel skor preferensi TOPSIS per kecamatan."
            ],
            "tools": ["ArcGIS Pro", "Super Decisions (AHP)", "Microsoft Excel", "QGIS"],
            "summary": "Menentukan prioritas lokasi pembangunan SMA baru di Kabupaten Temanggung melalui integrasi metode Delphi, Analytic Hierarchy Process (AHP), dan pemeringkatan TOPSIS berbasis analisis spasial GIS.",
            "problem_statement": "Distribusi fasilitas SMA di Kabupaten Temanggung belum merata, menyebabkan beberapa kecamatan berada di luar jangkauan standar pelayanan minimal pendidikan zonasi.",
            "methodology": "Integrasi Spatial Multi-Criteria Evaluation (SMCE): survei konsensus Delphi, pembobotan prioritas AHP pada Super Decisions, pemodelan kesesuaian spasial pada ArcGIS, dan perankingan alternatif lokasi menggunakan algoritma TOPSIS.",
            "scenarios": [
                {
                    "id": "kriteria",
                    "label": "Peta Kriteria Spasial",
                    "title": "Peta Pembobotan Kriteria Kesesuaian Lahan & Demografi",
                    "image": "/static/assets/slides/slide_14.webp",
                    "large_image": "/static/assets/slides/slide_14_large.webp",
                    "description": "Overlay spasial berbagai kriteria: buffer radius jangkauan SMA eksisting, kepadatan usia 15-18 tahun, lereng fisik, dan aksesibilitas jalan arteri/kolektor."
                },
                {
                    "id": "topsis",
                    "label": "Rekomendasi TOPSIS",
                    "title": "Hasil Pemeringkatan Alternatif Lokasi Baru TOPSIS",
                    "image": "/static/assets/slides/slide_15.webp",
                    "large_image": "/static/assets/slides/slide_15_large.webp",
                    "description": "Visualisasi ranking nilai preferensi kedekatan solusi ideal: Kecamatan Ngadirejo menempati ranking 1 dengan skor relatif 0,6766 sebagai prioritas tertinggi."
                }
            ],
            "metrics": [
                {"label": "Lokasi Terpilih", "value": "Kecamatan Ngadirejo", "context": "Skor TOPSIS 0,6766 (Tertinggi)"},
                {"label": "Metode Terpadu", "value": "Delphi + AHP + TOPSIS", "context": "SMCE Multikriteria Spasial"}
            ],
            "recommendations": "Memprioritaskan pengadaan lahan sekolah baru di koridor strategis Kecamatan Ngadirejo dan memperluas layanan transportasi perdesaan menuju sentra pendidikan.",
            "related_project_ids": ["P03", "P06"]
        },
        {
            "id": "P06",
            "slug": "analisis-kekompakan-kota-malang",
            "title": "Analisis Kekompakan Kota Malang",
            "categories": ["analisis-perkotaan", "gis"],
            "project_type": "Proyek Riset Morfologi Perkotaan",
            "location": "Kota Malang, Jawa Timur",
            "year": "2024",
            "featured": False,
            "sort_order": 6,
            "status": "published",
            "cover_image": "/static/assets/slides/slide_3_thumb.webp",
            "source_pages": [3, 4, 5],
            "role_summary": "Analis Spasial & Pengolah Data Kuantitatif IFAS-EFAS",
            "my_contributions": [
                "Mengumpulkan dan menyusun tabulasi data kuesioner primer serta data statistik spasial 5 kecamatan di Kota Malang.",
                "Mengklasifikasikan indikator kota kompak: kepadatan permukiman, keragaman tata guna lahan, aksesibilitas angkutan kota, dan ketersediaan ruang publik.",
                "Melakukan kuantifikasi faktor internal (IFAS) dan eksternal (EFAS) SWOT untuk mengukur daya saing spasial tiap kecamatan.",
                "Membuat visualisasi peta tematik tipologi kekompakan morfologi kota pada platform GIS."
            ],
            "team_deliverables": [
                "Peta sebaran tingkat kekompakan morfologi perkotaan Kota Malang.",
                "Tabel matriks komparasi indikator kompak perkotaan antar-kecamatan.",
                "Diagram kuadran SWOT strategi peremajaan kota kompak berkelanjutan."
            ],
            "tools": ["ArcGIS", "SPSS", "Microsoft Excel", "QGIS"],
            "summary": "Membandingkan tingkat kekompakan morfologi lima kecamatan di Kota Malang melalui klasifikasi indikator bentuk perkotaan, pemetaan tematik spasial, dan kuantifikasi faktor strategis IFAS-EFAS SWOT.",
            "problem_statement": "Pertumbuhan perkotaan Kota Malang menghadapi gejala peri-urban sprawl yang menurunkan efisiensi infrastruktur dan memperpanjang jarak komuter perjalanan harian.",
            "methodology": "Analisis morfologi kota berbasis Compact City Framework: scoring indikator spasial (kepadatan, guna lahan campuran, konektivitas transit) dipadukan dengan analisis SWOT kuantitatif berbobot.",
            "scenarios": [
                {
                    "id": "indikator",
                    "label": "Peta Morfologi & Indikator",
                    "title": "Peta Tematik Indikator Kota Kompak Kota Malang",
                    "image": "/static/assets/slides/slide_3.webp",
                    "large_image": "/static/assets/slides/slide_3_large.webp",
                    "description": "Pemetaan spasial variasi intensitas guna lahan, kepadatan penduduk, dan akses simpul transportasi pada 5 kecamatan (Klojen, Lowokwaru, Blimbing, Sukun, Kedungkandang)."
                },
                {
                    "id": "swot",
                    "label": "Evaluasi IFAS-EFAS SWOT",
                    "title": "Matriks Faktor Strategis Internal & Eksternal",
                    "image": "/static/assets/slides/slide_4.webp",
                    "large_image": "/static/assets/slides/slide_4_large.webp",
                    "description": "Perbandingan bobot dan rating faktor kekuatan, kelemahan, peluang, dan ancaman untuk menentukan arahan konsolidasi tata ruang kota."
                }
            ],
            "metrics": [
                {"label": "Kecamatan Dianalisis", "value": "5 Kecamatan", "context": "Wilayah Kota Malang"},
                {"label": "Fokus Kajian", "value": "Compact City Index", "context": "Efisiensi ruang & mobilitas"}
            ],
            "recommendations": "Mendorong intensifikasi pembangunan vertikal di kawasan pusat dan subpusat kota serta membatasi konversi lahan pertanian di koridor pinggiran timur Malang.",
            "related_project_ids": ["P03", "P05"]
        },
        {
            "id": "P07",
            "slug": "studi-kasus-pelatihan-lokasolution",
            "title": "Studi Kasus Pelatihan LokaSolution",
            "categories": ["konsultasi", "analisis"],
            "project_type": "Studi Kasus Pelatihan Konsultasi",
            "location": "Surabaya & Simulasi Studi Kasus",
            "year": "2026",
            "featured": False,
            "sort_order": 7,
            "status": "published",
            "cover_image": "/static/assets/slides/slide_23_thumb.webp",
            "source_pages": [23, 24],
            "role_summary": "Peserta Pelatihan & Strategic Problem Solver",
            "my_contributions": [
                "Menyelesaikan 6 sesi pelatihan intensif pemecahan masalah berbasis standar industri konsultasi manajemen dan perencanaan strategis.",
                "Mengaplikasikan prinsip Mutually Exclusive, Collectively Exhaustive (MECE) dan pohon isu (Issue Tree) dalam menstrukturkan persoalan bisnis kawasan.",
                "Melakukan analisis kelayakan lokasi, estimasi potensi pasar, dan kajian spasial berbasis data pada studi kasus simulasi (Jasa Marga & Nusantara Living).",
                "Menyusun dan mempresentasikan dek rekomendasi eksekutif di hadapan mentor profesional."
            ],
            "team_deliverables": [
                "Deck presentasi pemecahan masalah strategis untuk studi kasus simulasi infrastruktur jalan tol & properti hunian.",
                "Pohon masalah (Issue Tree) terstruktur dengan hipotesis kerja yang teruji.",
                "Rekomendasi implementasi bertahap disertai mitigasi risiko."
            ],
            "tools": ["MECE Framework", "Issue Tree Analysis", "Financial & Spatial Modeling", "Figma / Slides"],
            "summary": "Menyelesaikan simulasi 6 studi kasus pelatihan pemecahan masalah bersama LokaSolution menggunakan pendekatan MECE dan issue tree untuk merumuskan rekomendasi strategi bisnis dan penataan kawasan berbasis bukti spasial.",
            "problem_statement": "Pengambilan keputusan investasi dan pengembangan wilayah memerlukan struktur pemecahan masalah yang ketat, berbasis bukti data pasar serta kelayakan spasial.",
            "methodology": "Framework konsultasi manajemen: diagnosis masalah, dekomposisi isu dengan prinsip MECE, perumusan hipotesis kerja, pengujian data spasial & finansial, serta sintesis rekomendasi yang dapat ditindaklanjuti.",
            "scenarios": [
                {
                    "id": "framework",
                    "label": "Kerangka MECE & Issue Tree",
                    "title": "Dekomposisi Masalah dengan Kerangka MECE",
                    "image": "/static/assets/slides/slide_23.webp",
                    "large_image": "/static/assets/slides/slide_23_large.webp",
                    "description": "Struktur logis pemecahan masalah investasi yang memastikan tidak ada aspek yang terlewatkan dan tidak ada tumpang tindih analisis."
                },
                {
                    "id": "rekomendasi",
                    "label": "Sintesis Rekomendasi Spasial",
                    "title": "Paparan Solusi & Rekomendasi Eksekutif",
                    "image": "/static/assets/slides/slide_24.webp",
                    "large_image": "/static/assets/slides/slide_24_large.webp",
                    "description": "Rangkuman formulasi rekomendasi aksi nyata dan pentahapan implementasi yang disajikan dalam simulasi konsultasi profesional."
                }
            ],
            "metrics": [
                {"label": "Modul Simulasi Kasus", "value": "6 Sesi Pelatihan", "context": "Studi kasus infrastruktur & properti"},
                {"label": "Pendekatan Kerja", "value": "MECE + Issue Tree", "context": "Konsultasi strategis berbasis data"}
            ],
            "recommendations": "Menerapkan struktur analisis berbasis bukti dalam setiap penilaian kelayakan proyek wilayah dan investasi infrastruktur perkotaan.",
            "related_project_ids": ["P01", "P03"]
        }
    ],
    "experiences": [
        {
            "id": "exp_01",
            "org": "Dinas Perhubungan Sidoarjo",
            "role": "Surveyor Operasional & Wawancara Penumpang",
            "period": "Nov 2025 – Des 2025",
            "tags": ["transportasi"],
            "summary": "Survei operasional angkutan perdesaan dan wawancara penumpang angkutan umum/Transjatim.",
            "contributions": [
                "Melakukan survei operasional lapangan rute angkutan perdesaan di Kabupaten Sidoarjo.",
                "Mengumpulkan data primer melalui wawancara terstruktur kepada penumpang Transjatim dan angkutan pengumpan mengenai waktu tunggu, tarif, dan kenyamanan perjalanan.",
                "Merekapitulasi dan membersihkan data survei harian untuk analisis load factor dan kinerja operasional trayek."
            ],
            "status": "published",
            "confirmed_project_id": None
        },
        {
            "id": "exp_02",
            "org": "ITS Eco Campus",
            "role": "Surveyor Traffic Count",
            "period": "Apr 2026 – Mei 2026",
            "tags": ["transportasi"],
            "summary": "Traffic count manual pada 3 lokasi strategis sebagai masukan analisis bangkitan perjalanan kampus.",
            "contributions": [
                "Melakukan pencacahan volume lalu lintas (traffic count) manual terklasifikasi pada 3 gerbang utama ITS.",
                "Mencatat fluktuasi volume kendaraan bermotor pada jam puncak pagi, siang, dan sore hari.",
                "Menyusun dataset bangkitan dan tarikan perjalanan sivitas akademika sebagai masukan perencanaan mobilitas ramah lingkungan kampus."
            ],
            "status": "published",
            "confirmed_project_id": None
        },
        {
            "id": "exp_03",
            "org": "Departemen PWK ITS",
            "role": "Asisten Dosen Sistem Informasi Perencanaan (SIP)",
            "period": "Mar 2026 – Jul 2026",
            "tags": ["gis", "kepemimpinan"],
            "summary": "Pendampingan praktikum GIS, analisis raster, dan pengenalan WebGIS untuk 45 mahasiswa.",
            "contributions": [
                "Mendampingi 45 mahasiswa dalam 14 sesi praktikum laboratorium software GIS (ArcGIS dan QGIS).",
                "Membimbing modul analisis spasial vektor, interpolasi raster, spatial multi-criteria evaluation, dan WebGIS.",
                "Mengevaluasi penugasan peta tematik dan memberikan feedback teknis kartografi kepada praktikan."
            ],
            "status": "published",
            "confirmed_project_id": "P04"
        },
        {
            "id": "exp_04",
            "org": "Departemen PWK ITS",
            "role": "Asisten Dosen Metode Analisis Perencanaan (MAP)",
            "period": "Agu 2026 – Sekarang",
            "tags": ["gis", "analisis", "kepemimpinan"],
            "summary": "Pendampingan 15 modul metode kuantitatif untuk 43 mahasiswa menggunakan Excel, SPSS, dan Super Decisions.",
            "contributions": [
                "Memfasilitasi 15 modul praktikum analisis kuantitatif perencanaan untuk 43 mahasiswa.",
                "Membimbing materi statistik parametrik & non-parametrik (SPSS), Analytic Hierarchy Process (Super Decisions), dan pemodelan proyeksi data (Excel).",
                "Menyelenggarakan asistensi tugas besar analisis spasial dan perumusan rekomendasi kebijakan."
            ],
            "status": "published",
            "confirmed_project_id": "P05"
        },
        {
            "id": "exp_05",
            "org": "Planopolis 2026",
            "role": "Project Officer (Ketua Pelaksana)",
            "period": "Mei 2026 – Sekarang",
            "tags": ["kepemimpinan"],
            "summary": "Penyusunan grand design dan memimpin struktur kerja 8 divisi serta 10 subdivisi acara tahunan PWK ITS.",
            "contributions": [
                "Merumuskan grand design, tema strategis, dan roadmap operasional Planopolis 2026, acara berskala nasional Departemen PWK ITS.",
                "Memimpin dan mengkoordinasikan 8 divisi utama dan 10 subdivisi dengan lebih dari 80 panitia mahasiswa.",
                "Mengawasi manajemen risiko, budgeting, penjadwalan, dan relasi pemangku kepentingan eksternal."
            ],
            "status": "published",
            "confirmed_project_id": None
        },
        {
            "id": "exp_06",
            "org": "IMAGITS",
            "role": "Ketua Umum",
            "period": "Jan 2025 – Feb 2026",
            "tags": ["kepemimpinan"],
            "summary": "Menetapkan visi, program kerja, dan koordinasi organisasi kemahasiswaan dengan 30 anggota aktif.",
            "contributions": [
                "Memimpin organisasi kemahasiswaan dengan 30 anggota aktif, mengarahkan arah gerak strategis dan program kerja.",
                "Menginisiasi program pengembangan kapasitas anggota di bidang keahlian perencanaan dan kepemimpinan.",
                "Mengelola koordinasi internal, evaluasi kinerja bulanan, dan advokasi kolaborasi lintas organisasi kampus."
            ],
            "status": "published",
            "confirmed_project_id": None
        },
        {
            "id": "exp_07",
            "org": "INI LHO ITS 2026",
            "role": "Kepala Subdivisi Media Production",
            "period": "Sep 2025 – Mar 2026",
            "tags": ["media", "kepemimpinan"],
            "summary": "Memimpin produksi 84 motion graphics, 18 visual editing, dan 8 live production, total 110 keluaran tim.",
            "contributions": [
                "Memimpin tim kreatif dalam memproduksi total 110 keluaran media: 84 motion graphics, 18 karya editing visual, dan 8 sesi produksi live.",
                "Menetapkan standar panduan visual (brand guidelines) dan kendali mutu teknis konten sebelum publikasi.",
                "Mengelola timeline produksi cepat dengan koordinasi terpadu antar editor, animator, dan penata kamera."
            ],
            "status": "published",
            "confirmed_project_id": None
        },
        {
            "id": "exp_08",
            "org": "Planopolis 2025",
            "role": "Expert Staff Media Production",
            "period": "Agu 2025 – Feb 2026",
            "tags": ["media", "kepemimpinan"],
            "summary": "Merumuskan kerangka kerja tugas, standardisasi alur kerja, dan pendampingan teknis staf produksi media.",
            "contributions": [
                "Menyusun standar operasional prosedur (SOP) dan task framework untuk staf media produksi.",
                "Memberikan pelatihan dan supervisi teknis software desain dan video editing kepada staf junior.",
                "Memastikan seluruh aset promosi acara terdistribusi tepat waktu dan sesuai identitas visual acara."
            ],
            "status": "published",
            "confirmed_project_id": None
        },
        {
            "id": "exp_09",
            "org": "Plan-A",
            "role": "Kepala Divisi Branding dan Marketing",
            "period": "Agu 2025 – Okt 2025",
            "tags": ["media", "kepemimpinan"],
            "summary": "Menyusun Work Breakdown Structure (WBS), supervisi 3 subdivisi dan 23 staf anggota.",
            "contributions": [
                "Menyusun Work Breakdown Structure (WBS) komprehensif untuk membedah target pemasaran strategis ke dalam rencana kerja konkret.",
                "Mensupervisi 3 subdivisi (konten, desain, dan publikasi) dengan total 23 staf anggota.",
                "Mengawal pencapaian target engagement publikasi dan awareness kampanye program."
            ],
            "status": "published",
            "confirmed_project_id": None
        },
        {
            "id": "exp_10",
            "org": "LokaSolution",
            "role": "Anggota Tim Konsultasi",
            "period": "Jun 2026 – Sekarang",
            "tags": ["konsultasi", "analisis"],
            "summary": "Analisis pengembangan strategis dan perumusan rekomendasi berbasis data spasial dan kelayakan investasi.",
            "contributions": [
                "Terlibat dalam perumusan solusi bisnis berbasis data spasial dan metodologi konsultasi terstruktur.",
                "Menyusun kajian awal kelayakan pengembangan kawasan dan positioning strategis klien.",
                "Mempersiapkan materi rekomendasi dan visualisasi presentasi konsultatif."
            ],
            "status": "published",
            "confirmed_project_id": "P07"
        },
        {
            "id": "exp_11",
            "org": "HMPL ITS",
            "role": "Staf Human Resource Development (HRD)",
            "period": "Apr 2026 – Sekarang",
            "tags": ["kepemimpinan"],
            "summary": "Koordinasi pelatihan kepemimpinan dan manajemen sumber daya mahasiswa Departemen PWK ITS.",
            "contributions": [
                "Mengorganisir program pelatihan manajerial dan kepemimpinan kreatif mahasiswa perencanaan wilayah.",
                "Melakukan pemantauan dinamika dan iklim organisasi kemahasiswaan himpunan.",
                "Memfasilitasi sesi evaluasi dan upgrading kapasitas pengurus himpunan."
            ],
            "status": "published",
            "confirmed_project_id": None
        },
        {
            "id": "exp_12",
            "org": "INI LHO ITS 2025",
            "role": "Staf Media Production",
            "period": "Okt 2024 – Mar 2025",
            "tags": ["media"],
            "summary": "Peran Director of Photography (DoP), asisten DoP, asisten kamera, serta PIC produksi siaran penutup.",
            "contributions": [
                "Bertindak sebagai Director of Photography (DoP) dan asisten kamera dalam shooting video narasi dan teaser profil kampus.",
                "Mengatur tata cahaya, komposisi kamera sinematik, dan audio recorder di lapangan.",
                "Menjadi Person in Charge (PIC) siaran visual multi-kamera pada acara malam penutupan besar."
            ],
            "status": "published",
            "confirmed_project_id": None
        }
    ],
    "education": [
        {
            "institution": "Institut Teknologi Sepuluh Nopember (ITS)",
            "program": "S1 Perencanaan Wilayah dan Kota (PWK)",
            "period": "Agustus 2024 – September 2028 (Perkiraan)",
            "gpa": "3.58 / 4.00",
            "location": "Surabaya, Indonesia",
            "highlights": "Fokus pada Analisis Spasial Geografis, Pemodelan Sistem Transportasi, Perencanaan Ruang Kota, dan Studio Wilayah."
        },
        {
            "institution": "SMA Negeri 1 Magetan",
            "program": "Pendidikan Menengah Atas (MIPA)",
            "period": "2021 – 2024",
            "gpa": None,
            "location": "Magetan, Jawa Timur",
            "highlights": "Peminatan Matematika dan Ilmu Pengetahuan Alam, aktif dalam organisasi kepemimpinan siswa."
        }
    ],
    "skills": [
        {
            "group": "Sistem Informasi Geografis & Spasial",
            "icon": "map",
            "items": ["QGIS", "ArcGIS Pro / ArcMap", "Google Earth Engine", "WebGIS", "Spatial Analyst", "Network Analyst"]
        },
        {
            "group": "Transportasi & Mobilitas",
            "icon": "navigation",
            "items": ["PTV Visum", "Pemodelan 4 Tahap", "Urban Network Analysis (UNA)", "Dasymetric Mapping", "Model Gravitasi & OD Matrix"]
        },
        {
            "group": "Metode Analisis Kuantitatif",
            "icon": "bar-chart-2",
            "items": ["Super Decisions (AHP)", "SPSS Statistics", "TOPSIS Multicriteria", "Microsoft Excel Lanjutan", "Analisis Regresi"]
        },
        {
            "group": "Desain, Media & Visualisasi",
            "icon": "layout",
            "items": ["Adobe Premiere Pro", "After Effects", "Photoshop", "Lightroom", "Figma", "SketchUp & Enscape", "Canva"]
        }
    ],
    "achievements": [
        {
            "title": "Top 50 Finalis MAPID WebGIS Competition (MWGC 2026)",
            "organizer": "MAPID & Asosiasi Geospasial Indonesia",
            "year": "2026",
            "description": "Pengembangan aplikasi peta interaktif WebGIS analisis kerentanan lingkungan dan aksesibilitas perkotaan.",
            "certificate_file": "/static/assets/certificates/sertifikat_mapid_mwgc.pdf"
        },
        {
            "title": "Semifinalis 180 Degrees Consulting (180DC) ITS BCC",
            "organizer": "180 Degrees Consulting ITS",
            "year": "2025",
            "description": "Kompetisi Business Case penyusunan rekomendasi strategis pemecahan masalah operasional dan pengembangan pasar berbasis data."
        }
    ],
    "site_settings": {
        "theme": "urban-transit",
        "default_motion": "standard",
        "primary_color": "#315C37",
        "hero_bg": "#14211C",
        "content_bg": "#F6F7F2",
        "accent_path": "#A7C66A",
        "border_color": "#DCE2D7",
        "version": "1.0.0",
        "last_published": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    }
}

os.makedirs("data", exist_ok=True)
with open("data/content.json", "w", encoding="utf-8") as f:
    json.dump(data, f, indent=2, ensure_ascii=False)

# create backup
shutil.copyfile("data/content.json", "data/backups/content_init.json")
print("content.json created successfully with full data!")

# PRD Web Portofolio Muhammad Mirza Wibisono

| Metadata | Nilai |
| --- | --- |
| Versi | 0.2 |
| Tanggal | 21 Oktober 2026 |
| Pemilik produk | Muhammad Mirza Wibisono |
| Tujuan | Mendukung lamaran magang melalui portofolio yang mudah dinilai HRD dan pembimbing teknis |
| Format acuan | Markdown |
| Status | Spesifikasi produk untuk desain dan implementasi; beberapa data publikasi masih perlu dilengkapi |
| Bahasa awal | Bahasa Indonesia; struktur konten disiapkan untuk versi Inggris |

## 1 Ringkasan keputusan

Bangun portofolio pribadi untuk mahasiswa Perencanaan Wilayah dan Kota ITS semester 5, dengan karakter visual transportasi dan perkotaan. Pengunjung harus dapat mengenali profil Mirza, memeriksa kontribusi pada proyek, membaca CV interaktif, mengunduh CV PDF, dan menghubungi pemilik tanpa login.

Target magang beragam. Situs menampilkan kemampuan transportasi, GIS, perencanaan kota, analisis, konsultasi, serta kepemimpinan tanpa mengunci profil pada satu lowongan. Karya transportasi Wonokromo menjadi unggulan pertama sebagai interpretasi operasional atas perhatian pemilik terhadap halaman 18–19; urutannya dapat diubah melalui admin.

Keputusan dari arahan pemilik:

- Gunakan karya dalam 25 SVG sebagai sumber konten. Tata letak slide bukan rancangan web yang wajib disalin.
- Prioritaskan karakter transportasi dan perkotaan pada landing page, transisi, dan keadaan loading.
- Ubah CV menjadi pengalaman web interaktif sambil mempertahankan PDF yang dapat diunduh.
- Sediakan pengelolaan karya tanpa coding sejak rilis awal.
- Gunakan referensi situs profesional untuk menyusun pengalaman web yang lebih sesuai dengan kebutuhan perekrut.
- Serahkan PRD dalam Markdown. Dokumen ini memperbarui spesifikasi versi 0.1.

**Makna prioritas:** P0 wajib tersedia saat rilis awal; P1 dikembangkan setelah fungsi inti stabil; P2 hanya dikerjakan bila kebutuhan dan asetnya sudah jelas. Durasi animasi, anggaran aset, urutan karya, serta target pengujian di bawah merupakan keputusan desain yang diusulkan, bukan hasil pengukuran situs yang sudah dibangun.

## 2 Tujuan produk dan pengguna

### 2.1 Tujuan

1. Membantu HRD memahami bidang minat, pendidikan, pengalaman, serta ketersediaan magang dengan cepat.
2. Membantu penilai teknis melihat masalah, metode, kontribusi pribadi, dan keluaran setiap proyek.
3. Menampilkan identitas visual yang khas sekaligus menjaga keterbacaan peta, teks, dan CV.
4. Memberi pemilik satu alamat portofolio yang mudah dibagikan dan diperbarui.

### 2.2 Pengguna utama

| Pengguna | Tugas yang ingin diselesaikan | Respons produk |
| --- | --- | --- |
| HRD atau perekrut | Menilai kecocokan awal dan menemukan CV serta kontak | Ringkasan profil, tiga karya unggulan, CV, kontak selalu mudah dijangkau |
| Pembimbing magang atau tim teknis | Memahami kedalaman metode dan peran kandidat | Studi kasus terstruktur, peta beresolusi cukup, penjelasan kontribusi, tautan bukti |
| Pemilik portofolio | Memperbarui proyek, pengalaman, CV, dan ketersediaan | Admin dengan formulir, unggah aset, pratinjau, terbitkan, dan pemulihan versi |

### 2.3 Target validasi awal

- Dalam uji kepada 5 calon pembaca, sedikitnya 4 dapat menjelaskan bidang utama Mirza dan menemukan karya relevan dalam 60 detik. Angka ini target uji, bukan klaim umum tentang perilaku HRD.
- CV dan kontak dapat dicapai dalam maksimal 2 tindakan dari halaman publik mana pun.
- Semua studi kasus yang terbit membedakan kontribusi Mirza, hasil kelompok, serta status hasil analisis atau implementasi.
- Dalam uji pengelolaan, pemilik dapat menambah satu karya dan mengganti CV tanpa mengedit kode atau meminta bantuan pengembang.
- Animasi tidak menunda akses ke informasi atau tombol utama.

## 3 Profil dan cara memperkenalkan pemilik

### 3.1 Data dasar

| Informasi | Nilai dari sumber | Penggunaan |
| --- | --- | --- |
| Nama | Muhammad Mirza Wibisono | Judul halaman, profil, CV, metadata |
| Pendidikan | Perencanaan Wilayah dan Kota, Institut Teknologi Sepuluh Nopember | Identitas utama |
| Status | Mahasiswa semester 5, berdasarkan arahan pemilik | Dapat diperbarui melalui admin; jangan dihitung otomatis dari tahun masuk |
| Lokasi | Surabaya, Indonesia | Profil dan kontak; tidak perlu alamat rinci |
| Studi | Agustus 2024–September 2028, perkiraan selesai menurut CV | Bagian pendidikan dengan label perkiraan |
| IPK | 3,58/4,00 pada CV | Opsional pada CV web; tanggal pembaruan tercatat |
| Email | mirzawibi@gmail.com | Email utama; cocok pada CV dan SVG 25 |
| LinkedIn | https://www.linkedin.com/in/mirzawibi | Tautan profesional utama |
| Telepon | Tersedia dalam CV | Jangan otomatis dijadikan WhatsApp aktif sebelum nomor dan pilihan publikasi dikonfirmasi |

Pendidikan SMA Negeri 1 Magetan dapat dimasukkan pada rincian pendidikan, bukan informasi utama hero. Instagram tersedia pada SVG 25, tetapi menjadi tautan tambahan hanya jika pemilik ingin menampilkan akun tersebut untuk kepentingan profesional.

### 3.2 Usulan teks hero

**Nama:** Muhammad Mirza Wibisono  
**Identitas:** Mahasiswa PWK ITS · Surabaya  
**Bidang:** Analisis Spasial, Transportasi, dan Perencanaan Kota

**Ringkasan:**

> Saya memadukan analisis spasial, pemodelan transportasi, dan kepemimpinan tim untuk memahami persoalan kota serta menyusun rekomendasi perencanaan.

Tombol utama: **Lihat Karya**. Tombol pendamping: **Jelajahi CV** dan **Hubungi Saya**. Status magang cukup “Terbuka untuk peluang magang”; tanggal mulai, durasi, lokasi tujuan, dan mode kerja ditambahkan setelah diisi pemilik.

### 3.3 Tiga kelompok bukti kemampuan

| Bidang | Bukti yang dapat ditautkan |
| --- | --- |
| Analisis spasial dan perencanaan | Kebomas, UHI Surabaya, fasilitas SMA Temanggung, kekompakan Malang |
| Transportasi dan mobilitas | Wonokromo, aksesibilitas Suroboyo Bus, survei Dishub Sidoarjo, traffic count ITS Eco Campus |
| Kepemimpinan dan komunikasi | Ketua tim proyek, asisten dosen, Planopolis, IMAGITS, produksi media, dan pelatihan LokaSolution |

Keterampilan diberi label “digunakan pada proyek” atau “tercantum dalam CV”. Jangan membuat skor kemampuan berupa persentase, menambahkan gelar profesional, atau menyatakan keahlian senior yang tidak tersedia dalam sumber.

## 4 Inventaris karya dan urutan awal

ZIP memuat `1.svg` sampai `25.svg`. Pengelompokan berikut menghasilkan **7 studi kasus**, bukan 25 proyek. Nomor halaman mengacu pada nama berkas SVG.

| Urutan | ID dan judul web | Halaman | Peran yang didukung sumber | Kelompok |
| --- | --- | --- | --- | --- |
| 1 | P01 Perencanaan Transportasi Wonokromo | 17–19 | Ketua tim; analisis TAZ, persiapan basemap, trip assignment, dan indikasi program | Transportasi, GIS |
| 2 | P02 Aksesibilitas Halte Suroboyo Bus di Surabaya Timur | 10–13 | Ketua tim; integrasi analisis, UNA, OD Cost Matrix, dan indeks kebutuhan halte | Transportasi, GIS |
| 3 | P03 Perencanaan Kota Kebomas | 20–22 | Ketua tim; analisis fisik dasar dan multibencana; integrasi hasil ke rencana ruang dan WebGIS | Perencanaan Kota, GIS |
| 4 | P04 Analisis Urban Heat Island Surabaya | 6–9 | Ketua tim; pengolahan Landsat 8, NDVI, LST, UHI, dan integrasi WebGIS | GIS, Lingkungan Perkotaan |
| 5 | P05 Analisis Lokasi SMA di Kabupaten Temanggung | 14–16 | Ketua tim; pengarahan analisis lokasi; analisis spasial pendukung pemilihan lokasi | Perencanaan Wilayah, GIS |
| 6 | P06 Analisis Kekompakan Kota Malang | 3–5 | Analis spasial dan data; pengolahan indikator, klasifikasi, IFAS–EFAS, dan peta tematik | Analisis Perkotaan, GIS |
| 7 | P07 Studi Kasus Pelatihan LokaSolution | 23–24 | Peserta pelatihan; penyelesaian studi kasus dan presentasi rekomendasi | Konsultasi, Analisis |

Halaman 1 adalah sampul, halaman 2 profil, dan halaman 25 penutup/kontak. Tiga kartu unggulan awal: P01, P02, dan P03. Semua tujuh karya tetap dapat ditemukan melalui katalog.

Tahun pada peta dan periode data tidak otomatis menjadi tahun pelaksanaan proyek. Jenis mata kuliah, periode pengerjaan, anggota kelompok, dan tautan keluaran diisi bila sumbernya tersedia. Default `project_type` untuk proyek perencanaan adalah “Proyek akademik” sebagai usulan klasifikasi yang perlu diperiksa pemilik sebelum terbit.

### 4.1 P01 Wonokromo sebagai studi kasus utama

**Inti cerita:** memahami masalah pergerakan di Wonokromo melalui pemodelan empat tahap, kemudian membandingkan kondisi eksisting, proyeksi, dan skenario rencana.

Struktur halaman:

1. Ringkasan masalah, wilayah studi, peran Mirza, dan perangkat.
2. Penjelasan ringkas empat tahap: bangkitan, distribusi, pemilihan moda, dan pembebanan perjalanan.
3. Kontribusi pribadi: pembagian tugas, timeline, kendali kualitas, penentuan TAZ, persiapan basemap, trip assignment menggunakan PTV Visum, serta indikasi program.
4. Tiga tampilan hasil: **Eksisting**, **Proyeksi**, dan **Skenario Rencana**.
5. Rekomendasi dan keterbatasan model.

**Interaksi P0:** tiga tombol memilih gambar peta yang tersedia. Legenda, judul, dan keterangan mengikuti pilihan. Perbandingan ini menampilkan hasil pekerjaan yang sudah ada; situs tidak menjalankan ulang model transportasi.

**Angka dari halaman 18:** 8 ruas kritis, 5 rute feeder, 25 halte, serta pangsa angkutan umum 9,6% menjadi 26,3% dapat menjadi calon ringkasan hasil setelah skenario dan dasar perhitungannya dikonfirmasi. Label wajib “hasil skenario pemodelan”. Angka penurunan kendaraan pribadi 30% tidak ditampilkan sebagai fakta implementasi atau dihitung ulang dari persentase pangsa moda; definisi dan basisnya belum dijelaskan dalam slide.

Teks publik yang aman untuk rancangan awal: “Menyusun skenario pengembangan jaringan transportasi dan membandingkan hasil pembebanan perjalanan untuk mendukung rekomendasi penanganan ruas prioritas.”

### 4.2 P02 Aksesibilitas Suroboyo Bus

- Cerita: kesesuaian penempatan halte terhadap penduduk dan jaringan jalan di Surabaya Timur.
- Metode yang dicantumkan sumber: dasymetric mapping, Urban Network Analysis, Model Huff, OD Cost Matrix, normalisasi, dan overlay.
- Bedakan peran memimpin integrasi metode dari pekerjaan analisis pribadi yang dinyatakan pada halaman 12.
- Keluaran utama: peta indeks aksesibilitas, peta kebutuhan halte, serta rekomendasi lokasi prioritas.
- Interaksi P0: pilihan peta “Aksesibilitas” dan “Kebutuhan Halte”. Keterangan menjelaskan apa yang dibandingkan; warna peta tidak diubah tanpa mempertahankan legenda.
- Angka 77 halte adalah jumlah objek eksisting pada materi, bukan jumlah halte yang dibangun Mirza.

### 4.3 P03 Kebomas

- Cerita: mengintegrasikan analisis wilayah menjadi arahan struktur dan pola ruang.
- Bukti kepemimpinan pada halaman 22: koordinasi 10 anggota, lintas 8 bidang, dalam rencana kerja 16 minggu. Jangan mengubahnya menjadi klaim 8 gelar atau sertifikasi keahlian pribadi.
- Kontribusi teknis: pemetaan fisik dasar, vegetasi, dan multibencana menggunakan GIS/Google Earth Engine; hasil digunakan dalam penyusunan arahan ruang.
- Lingkup 21 desa/kelurahan dinyatakan sebagai cakupan studi.
- Interaksi P0: galeri bertopik “Analisis Wilayah”, “Struktur Ruang”, dan “Pola Ruang”. Peta interaktif eksternal ditautkan hanya setelah URL asli diperoleh dan diperiksa.
- Status keluaran: usulan perencanaan/studi, bukan kebijakan tata ruang yang dinyatakan sudah disahkan.

### 4.4 P04 UHI Surabaya

- Cerita: membaca hubungan pola vegetasi, suhu permukaan, dan UHI dari citra multitemporal.
- Tampilkan NDVI, LST, dan UHI sebagai indikator berbeda, masing-masing dengan legenda dan penjelasan singkat.
- Tahun pengamatan menurut halaman 7: 2015, 2018, 2021, dan 2024. Pada halaman 9 ada label “2014–2024”, berbeda dari uraian “2015–2024”. Tahun awal harus dikonfirmasi sebelum terbit.
- Interaksi P0: pilih indikator untuk melihat peta yang benar-benar tersedia. Pemilih tahun hanya muncul untuk tahun yang asetnya lengkap.
- Sajikan temuan sebagai hasil analisis pada studi tersebut; hindari memperluasnya menjadi bukti kausal yang melampaui metode dan data.

### 4.5 P05 Temanggung

- Cerita: penentuan prioritas lokasi SMA berdasarkan kebutuhan dan kondisi wilayah.
- Tampilkan alur seleksi kriteria, pembobotan, analisis spasial, dan penilaian alternatif sesuai materi.
- Delphi, AHP, serta TOPSIS adalah metode proyek; kontribusi Mirza dijelaskan terpisah sesuai halaman 16.
- Hasil Ngadirejo dan nilai TOPSIS 0,6766 ditulis sebagai rekomendasi model pada studi, bukan keputusan pembangunan pemerintah.
- Interaksi P0: galeri peta kriteria dan tabel ringkas alternatif. Jangan membuat kalkulator TOPSIS sebelum data lengkap dan rumus terverifikasi tersedia.

### 4.6 P06 Malang

- Cerita: membandingkan kekompakan lima kecamatan melalui indikator dan pemetaan spasial.
- Peran: pengolahan data kuesioner, klasifikasi, kuantifikasi SWOT IFAS–EFAS, serta penyajian peta tematik.
- Halaman 4 menyebut skor Lowokwaru 33,2; tabel halaman 5 menampilkan 32,36. Angka kecamatan lain juga berbeda. Tahan tabel angka ringkasan sampai versi hasil final ditetapkan.
- Judul, masalah, metode, dan kontribusi dapat dirancang tanpa memilih salah satu tabel sebagai kebenaran final.

### 4.7 P07 LokaSolution

- Halaman 24 menyatakan pelatihan/simulasi 6 pertemuan dan penyelesaian 6 studi kasus. Contoh yang terlihat mencakup Jasa Marga dan Nusantara Living.
- Tampilkan label **Studi Kasus Pelatihan**. Logo atau nama perusahaan dalam contoh tidak boleh menyiratkan kontrak langsung.
- Bahas penyusunan masalah, MECE, issue tree, kajian spasial, kelayakan, dan presentasi rekomendasi sesuai materi.
- CV menyebut pengalaman sebagai anggota LokaSolution dan Vice Project Leader pada proyek PT Mitra Pengembang Kawasan. Simpan sebagai entri pengalaman terpisah; materi pelatihan tidak otomatis menjadi bukti proyek klien tersebut.
- Nama klien dan materi detail proyek klien ditayangkan setelah pemilik memastikan hubungan, peran, dan materi yang boleh dibagikan.

## 5 CV interaktif

### 5.1 Konsep

Halaman `/cv` berisi teks HTML terstruktur, bukan sekadar penampil PDF. Linimasa menggunakan garis dan simpul yang mengingatkan pada jaringan transit. Setiap simpul tetap berupa entri pengalaman dengan nama organisasi, posisi, rentang waktu, dan ringkasan. Pengalaman yang waktunya beririsan ditampilkan sesuai tanggalnya; ilustrasi tidak menyiratkan semua posisi dijalani berurutan.

Bagian CV:

1. Profil dan tombol **Unduh CV PDF**.
2. Ringkasan kemampuan yang ditautkan ke bukti proyek.
3. Pengalaman profesional, pengajaran, dan organisasi.
4. Pendidikan.
5. Perangkat dan metode.
6. Prestasi serta kegiatan sebagai pembicara.

### 5.2 Interaksi P0

- Filter pengalaman: Semua, Transportasi, GIS dan Analisis, Kepemimpinan, Media, serta Konsultasi. Satu pengalaman dapat memiliki beberapa tag.
- Tampilan awal memuat ringkasan; tombol “Lihat kontribusi” membuka uraian tanpa memindahkan pengguna ke halaman baru.
- Semua rentang waktu tetap terlihat saat uraian ditutup.
- Tombol “Lihat karya terkait” hanya muncul bila hubungan pengalaman dan karya memang didukung sumber atau dikonfirmasi pemilik.
- Tidak mengaitkan proyek Suroboyo Bus dengan pekerjaan Dishub Sidoarjo hanya karena sama-sama bertema transportasi.
- “Buka semua” tersedia untuk pembacaan menyeluruh. Tampilan cetak membuka seluruh uraian, menghapus dekorasi dan menu, serta mempertahankan URL penting.
- Mode tanpa animasi tetap menyajikan seluruh isi dengan urutan yang sama.
- PDF asli dan CV web adalah dua keluaran yang perlu diselaraskan; mengubah satu tidak diam-diam dianggap memperbarui yang lain.

### 5.3 Data pengalaman awal dari CV

Urutan tampilan default mengutamakan pengalaman relevan dan terbaru dalam setiap kelompok. Tabel ini inventaris sumber, bukan klaim bahwa semua status “sekarang” sudah diverifikasi ulang pada hari publikasi.

| Pengalaman | Periode pada CV | Ringkasan yang dapat dipakai |
| --- | --- | --- |
| Dinas Perhubungan Sidoarjo — Surveyor | Nov–Des 2025 | Survei operasional angkutan perdesaan dan wawancara penumpang angkutan umum/Transjatim |
| ITS Eco Campus — Surveyor | Apr–Mei 2026 | Traffic count manual pada 3 lokasi sebagai masukan analisis bangkitan perjalanan |
| ITS — Asisten Dosen Sistem Informasi Perencanaan | Mar–Jul 2026 | Pendampingan GIS, analisis raster, dan WebGIS untuk 45 mahasiswa |
| ITS — Asisten Dosen Metode Analisis Perencanaan | Agu 2026–sekarang | Pendampingan 15 modul untuk 43 mahasiswa menggunakan Excel, SPSS, dan Super Decisions |
| INI LHO ITS 2025 — Staf Media Production | Okt 2024–Mar 2025 | Peran DoP, asisten DoP, asisten kamera, serta PIC produksi acara penutup |
| IMAGITS — Ketua | Jan 2025–Feb 2026 | Visi, program kerja, dan koordinasi organisasi dengan 30 anggota |
| Gerigi x UKM EXPO ITS 2025 — Staf Media Production | Jul 2025–Feb 2026 | Konsep narasi, arah visual, kamera live, dan dokumentasi; label tahun perlu dicocokkan dengan SVG 2 |
| Plan-A — Kepala Divisi Branding dan Marketing | Agu–Okt 2025 | WBS, supervisi 3 subdivisi dan 23 staf |
| Planopolis 2025 — Expert Staff Media Production | Agu 2025–Feb 2026 | Kerangka kerja, uraian tugas, pendampingan, dan pemantauan hasil staf |
| INI LHO ITS 2026 — Kepala Subdivisi Media Production | Sep 2025–Mar 2026 | Memimpin produksi 84 motion graphics, 18 visual editing, dan 8 produksi, total 110 keluaran tim |
| HMPL ITS — Staf Human Resource Development | Apr 2026–sekarang | Koordinasi pelatihan dan kepemimpinan kreatif pada 2 proyek; status persiapan acara perlu diperbarui |
| Planopolis 2026 — Project Officer | Mei 2026–sekarang | Grand design dan struktur kerja 8 divisi serta 10 subdivisi |
| LokaSolution — Anggota | Jun 2026–sekarang | Analisis dan presentasi pengembangan; rincian peran Vice Project Leader dipisahkan dari program pelatihan |

Aturan ringkasan angka:

- Tulis **“memimpin produksi 110 keluaran tim”**, bukan “membuat sendiri 110 karya”.
- Jangan menjumlahkan dua kelas menjadi mahasiswa unik tanpa data peserta.
- Klaim “video dengan tayangan terbanyak” pada CV baru menjadi sorotan angka bila periode, kanal, dan bukti analitik tersedia.
- Prestasi yang boleh dicatat dari CV: Semifinalis 180DC ITS BCC serta Top 50 Finalis kompetisi WebGIS MAPID. Label prestasi harus mengikuti status yang tertulis, bukan dinaikkan menjadi juara.

### 5.4 Perangkat dan bukti

| Kelompok | Perangkat yang disebut sumber | Penempatan |
| --- | --- | --- |
| Geospasial | QGIS, ArcGIS/ArcMap, Google Earth Engine | Profil keahlian dan studi kasus terkait |
| Transportasi | PTV Visum; analisis TAZ dan trip assignment | Terutama P01 |
| Analisis | Excel, SPSS, Super Decisions; Google Sheets | Pengalaman pengajaran dan proyek analisis |
| Media dan desain | Premiere Pro, Photoshop, Lightroom, After Effects, Canva, Figma, CapCut pada SVG 2 | Bagian perangkat; contoh karya media menyusul bila tersedia |
| Visualisasi | SketchUp dan Enscape pada SVG 2 | Dicantumkan sebagai perangkat yang disebut pemilik, tanpa skor kemahiran |

## 6 Struktur situs dan perjalanan pengguna

### 6.1 Halaman

| Rute | Fungsi | Prioritas |
| --- | --- | --- |
| `/` | Landing page, profil singkat, tiga karya unggulan, ringkasan pengalaman, kontak | P0 |
| `/karya` | Seluruh studi kasus, filter, pencarian judul/tag | P0 |
| `/karya/{slug}` | Detail satu studi kasus dan interaksi berbasis aset | P0 |
| `/cv` | CV HTML interaktif, cetak, buka dan unduh PDF | P0 |
| `/#tentang` | Bagian profil pada beranda | P0 |
| `/#kontak` | Email, LinkedIn, status magang, kontak tambahan terpilih | P0 |
| `/admin` | Pintu masuk pemilik dan pengelolaan konten | P0 |
| Halaman tidak ditemukan | Penjelasan singkat, tautan karya dan beranda | P0 |

Menu utama memakai label jelas: **Tentang, Karya, CV, Kontak**. Label tidak diganti menjadi istilah stasiun yang sulit dipahami. Motif transit mendukung navigasi melalui garis, nomor, atau penanda aktif.

### 6.2 Perjalanan utama

| Skenario | Perjalanan | Hasil yang diharapkan |
| --- | --- | --- |
| HRD dari tautan lamaran | Beranda → ringkasan → karya unggulan → CV/kontak | Memahami profil dan mengakses dokumen tanpa hambatan |
| Penilai teknis | Tautan P01 → ringkasan peran → perbandingan peta → metode → CV | Menilai kedalaman kerja dan kontribusi pribadi |
| Perekrut dengan bidang tertentu | Katalog → filter → studi kasus → CV | Menemukan bukti relevan tanpa membaca semua proyek |
| Pembaca yang fokus pengalaman | CV → filter → rincian pengalaman → bukti terkait → kontak | Menghubungkan klaim pengalaman dengan bukti yang tersedia |
| Pemilik memperbarui situs | Login → edit draf → pratinjau → validasi → terbitkan | Pembaruan aman tanpa mengubah kode |

Pintu masuk ke detail karya langsung harus berfungsi tanpa melewati intro beranda. Tombol kembali mempertahankan filter dan posisi katalog bila pengguna datang dari katalog.

## 7 Arah visual dan referensi

### 7.1 Konsep visual

Gunakan suasana **kota dan jaringan mobilitas**: garis rute, simpul persimpangan, blok kota, kontur peta, serta penanda lokasi. Identitas Mirza dan karya nyata menjadi pusat komposisi.

- Hero memakai warna gelap arang, teks terang, dan satu ilustrasi jaringan kota yang bergerak singkat.
- Bagian isi memakai latar terang agar peta, teks panjang, dan CV nyaman dibaca.
- Hijau dari materi portofolio dipertahankan sebagai aksen, dengan pasangan warna yang diuji kontrasnya.
- Kartu karya memakai cuplikan keluaran nyata, judul, peran, dan ringkasan; tidak memakai satu screenshot seluruh slide sebagai kartu utama.
- Fotografi kota umum dapat menjadi atmosfer bila asal dan hak penggunaannya jelas. Jangan menampilkan foto kota lain sebagai hasil proyek Mirza.
- Ilustrasi rute hero boleh bersifat skematis dan tidak merepresentasikan jaringan nyata. Jika memakai peta faktual, lokasi, sumber, dan atribusi harus benar.

Usulan token awal:

| Fungsi | Nilai awal | Catatan |
| --- | --- | --- |
| Hero dan teks utama | `#14211C` | Arang kehijauan |
| Latar isi | `#F6F7F2` | Putih hangat |
| Tombol utama | `#315C37` | Uji kontras teks putih |
| Aksen jalur | `#A7C66A` | Dekorasi atau pasangan teks gelap; bukan teks kecil pada putih |
| Garis pemisah | `#DCE2D7` | Tidak menjadi satu-satunya pembeda status |
| Tipografi | Sans serif yang jelas; satu keluarga utama | Body mobile minimal 16 px; angka peta memakai bentuk yang mudah dibedakan |

Grid desktop 12 kolom, tablet 8, mobile 4. Galeri: 3 kolom desktop, 2 tablet, 1 mobile. Lebar teks panjang sekitar 65–75 karakter per baris. Nilai ini panduan desain dan dapat disesuaikan setelah pengujian visual.

### 7.2 Referensi yang diteliti

| Referensi | Hal yang ditemukan pada sumber | Adaptasi untuk portofolio |
| --- | --- | --- |
| [Gehl Projects](https://www.gehlpeople.com/projects/) | Direktori proyek dengan filter layanan/sektor/wilayah dan pilihan grid/list | Kategori yang mudah dipahami dan ringkasan proyek yang konsisten; jumlah filter disederhanakan untuk 7 studi kasus |
| [Applied — Legible London](https://appliedinformation.group/projects/legible-london) | Studi kasus wayfinding dengan konteks, lokasi, sistem informasi, dan visual pendukung | Label navigasi jelas, penanda posisi konsisten, serta peta yang membantu orientasi |
| [Applied — TransLink Vancouver](https://appliedinformation.group/projects/translink) | Identitas bersama untuk beragam moda dan penjelasan jaringan yang terhubung | Satu sistem garis dan simpul untuk menghubungkan bidang proyek serta pengalaman |
| [MVRDV Projects](https://www.mvrdv.com/projects) | Pengelompokan proyek seperti Urbanism, Research, dan Sustainability | Struktur katalog yang memungkinkan satu profil menampilkan bidang beragam |

Referensi di atas dipakai untuk struktur informasi dan gagasan navigasi. Durasi, perilaku loading, dan koreografi gerak dalam PRD ini merupakan rancangan khusus, bukan klaim bahwa efek tersebut telah diamati atau disalin dari situs referensi. Logo, foto, dan ilustrasi referensi tidak menjadi aset situs Mirza.

## 8 Landing page dan sistem gerak

### 8.1 Urutan landing page

1. **Hero:** nama, bidang, status magang, tiga tombol utama, ilustrasi jaringan kota.
2. **Karya unggulan:** Wonokromo, Suroboyo Bus, dan Kebomas; akses ke katalog lengkap.
3. **Kemampuan berbasis bukti:** transportasi, GIS/perencanaan, kepemimpinan; setiap kelompok menuju karya atau pengalaman terkait.
4. **Tentang Mirza:** foto, ringkasan pendek, pendidikan dan lokasi.
5. **Pengalaman terpilih:** pengajaran, survei transportasi, serta kepemimpinan; tombol membuka CV lengkap.
6. **Kontak:** email, LinkedIn, status magang dan tautan tambahan yang diaktifkan pemilik.

### 8.2 Spesifikasi gerak P0

| Elemen | Efek yang diusulkan | Durasi/perilaku | Alternatif ringan |
| --- | --- | --- | --- |
| Hero | Garis jaringan terbentuk, satu penanda bergerak melewati simpul, blok kota muncul halus | 700–900 ms, sekali pada kunjungan pertama dalam sesi; kemudian diam | Ilustrasi statis |
| Intro merek | Identitas Mirza muncul seperti papan informasi perjalanan di dalam area hero | Berjalan bersamaan dengan hero; tanpa layar wajib yang menutup semua konten | Nama langsung terlihat |
| Loading halaman | Garis rute kecil dan teks “Memuat karya” saat data benar-benar belum siap | Muncul setelah penundaan sekitar 300 ms; hilang segera setelah siap | Pesan teks dan placeholder statis |
| Navigasi antarhalaman | Perubahan gambar/konten dengan crossfade dan pergeseran pendek | 180–300 ms; tidak memutar ulang intro | Navigasi biasa |
| Kartu ke detail | Sampul berkembang ke area visual detail bila dukungan peramban memungkinkan | 220–350 ms; identitas halaman tetap segera dapat dipahami | Detail terbuka langsung |
| Bagian beranda | Penanda bagian aktif mengikuti posisi gulir; isi muncul dengan jarak kecil | 180–240 ms; hanya sekali per bagian | Isi langsung terlihat |
| CV | Simpul pengalaman disorot ketika entri dipilih; rincian terbuka | 160–220 ms; tinggi konten tetap wajar | Buka/tutup instan |
| Peta studi kasus | Crossfade antarhasil dengan judul dan legenda ikut berubah | 150–200 ms; tidak mengubah data peta | Pergantian instan |

Semua durasi adalah batas desain awal. Kurangi efek bila perangkat atau uji kinerja menunjukkan gangguan respons.

### 8.3 Aturan loading dan akses cepat

- Teks hero, CV, dan kontak tidak menunggu animasi selesai. Tidak ada jeda minimum untuk memaksa pengunjung menonton intro.
- Jangan menggunakan persentase pemuatan palsu. Jika progres aset tidak terukur, gunakan indikator tanpa angka.
- Loading terjadi pada area yang sedang membutuhkan data; navigasi dan konten yang sudah tersedia tetap dapat digunakan.
- Jika permintaan data gagal, tampilkan pesan dan tombol coba lagi. Setelah batas waktu 8 detik tanpa hasil, tampilkan pilihan coba lagi atau kembali, bukan animasi yang berputar tanpa penjelasan.
- Gambar peta resolusi tinggi baru dimuat saat dibuka. Kegagalan gambar besar tidak menghilangkan penjelasan tekstual.
- Gunakan scroll alami; tidak ada scroll yang diambil alih, suara otomatis, atau kewajiban menyelesaikan animasi untuk berpindah halaman.
- Tema transportasi harus tetap terasa melalui komposisi statis saat seluruh animasi dimatikan.

### 8.4 Preferensi gerak

Hormati `prefers-reduced-motion` dan sediakan kontrol “Kurangi animasi”. Preferensi perangkat menjadi default; pilihan eksplisit pengguna disimpan lokal. Mode pengurangan gerak menghapus penelusuran jalur, pergeseran kamera, parallax, dan animasi dekoratif; perubahan status tetap terbaca. [R5]

View Transition API dapat dipakai sebagai peningkatan visual melalui pemeriksaan dukungan, dengan navigasi normal sebagai fallback. Fokus dan riwayat browser harus tetap benar. Pemilihan API tidak mengubah kebutuhan produk atau mengharuskan framework tertentu. [R6]

## 9 Persyaratan fungsional dan kriteria penerimaan

### FR01 Profil dan beranda — P0

**Kebutuhan:** identitas, ringkasan, karya unggulan, status magang, dan tiga pintu utama ke karya/CV/kontak.

- Nama dan bidang tersedia sebagai teks yang dapat dipilih dan dibaca pembaca layar.
- Seluruh tombol utama dapat dipakai ketika animasi hero masih berjalan atau gagal.
- Foto gagal memuat tidak merusak layout atau menghilangkan identitas.
- Bidang minat dan ketersediaan dapat diperbarui melalui admin.

### FR02 Katalog karya — P0

**Kebutuhan:** tujuh studi kasus awal, dengan filter kategori dan pencarian sederhana berdasarkan judul/tag.

- Kategori utama: Semua, Transportasi, GIS dan Lingkungan, Perencanaan Kota/Wilayah, serta Konsultasi.
- Proyek dapat berada pada beberapa kategori, tetapi tidak diduplikasi dalam hasil.
- Kartu memuat sampul, judul, wilayah, peran, serta label jenis proyek. Tahun hanya tampil bila telah diisi dengan benar.
- Filter dicatat pada URL, misalnya `/karya?kategori=transportasi`; URL langsung dan tombol Back mempertahankan keadaan.
- Hasil kosong menampilkan “Belum ada karya pada pilihan ini” dan tombol reset.
- Urutan default mengikuti tabel inventaris dan dapat diubah pemilik.

### FR03 Detail studi kasus — P0

**Kebutuhan:** konteks, tujuan, metode, peran pribadi, hasil, refleksi, dan aset.

- Ringkasan awal menyebut peran Mirza dan status keluaran sebelum pengunjung membaca metode panjang.
- Pisahkan “Kontribusi saya”, “Hasil tim”, serta “Rekomendasi/skenario” bila relevan.
- URL unik bekerja saat dibuka langsung dan dimuat ulang.
- Gambar memiliki keterangan, teks alternatif, dan sumber/kredit bila relevan.
- Studi kasus menyediakan CV, kontak, kembali ke katalog, serta maksimal dua karya terkait.
- Tautan laporan/WebGIS hanya tampil jika URL asli tersedia; logo Linktree pada SVG tidak dianggap sebagai tautan aktif.

### FR04 Galeri dan perbandingan peta — P0

**Kebutuhan:** pembesaran gambar dan pemilihan keluaran yang tersedia.

- Modal gambar dapat dibuka lewat keyboard, ditutup dengan Escape, dan mengembalikan fokus ke pemicu.
- Peta tidak terpotong pada legenda atau orientasinya; pembesaran mempertahankan rasio.
- Pilihan peta memperbarui judul, legenda, keterangan skenario/tahun, dan teks alternatif secara bersamaan.
- P01 memakai tab Eksisting/Proyeksi/Skenario Rencana; P02 dan P04 memakai indikator yang tersedia.
- Perbandingan dengan slider tumpang tindih adalah P1 dan hanya dipakai bila extent, skala, serta ukuran peta cocok. Tab terpisah adalah fallback yang selalu tersedia.

### FR05 CV interaktif — P0

**Kebutuhan:** CV HTML, filter, rincian pengalaman, pendidikan, perangkat, prestasi, dan tautan bukti.

- Semua pengalaman pada inventaris tersedia dalam data; entri belum siap publik tetap menjadi draf.
- Setiap filter menghasilkan entri relevan dan dapat direset. Pembaca tetap dapat membuka seluruh isi.
- Ekspansi uraian tidak menyembunyikan jabatan, organisasi, atau tanggal.
- Link karya terkait tidak dibuat melalui dugaan kesamaan topik.
- Mode cetak memuat semua entri publik dengan urutan jelas dan tanpa animasi.
- Pada JavaScript gagal, ringkasan dan entri publik tetap tersedia sebagai dokumen yang dapat dibaca.

### FR06 CV PDF — P0

**Kebutuhan:** buka dan unduh berkas PDF aktif.

- Sumber awal adalah CV yang dilampirkan; pratinjau PDF tidak menggantikan CV HTML.
- Tombol menampilkan tanggal pembaruan dan ukuran berkas; nama publik disarankan `CV_Muhammad_Mirza_Wibisono.pdf`.
- Unduhan tidak meminta login. Jika peramban membuka PDF, pengguna tetap dapat menyimpannya.
- Hanya satu versi PDF aktif; penggantian dilakukan setelah berkas baru berhasil diunggah dan divalidasi.
- Jika unggah gagal, berkas lama tetap aktif. Pratinjau gagal tetap menyediakan link langsung.
- Admin menandai apakah perubahan CV HTML sudah dicocokkan dengan PDF sebelum memperbarui tanggal “CV diperbarui”.

### FR07 Kontak — P0

**Kebutuhan:** email, LinkedIn, status magang, dan kanal tambahan opsional.

- Email utama menggunakan `mirzawibi@gmail.com`; tersedia tindakan buka email dan salin alamat.
- Jika Clipboard API gagal, alamat tetap terlihat dan dapat disalin manual.
- LinkedIn menuju URL yang tercantum pada CV.
- WhatsApp tidak aktif secara default; aktif setelah pemilik memilih nomor publik dan mengonfirmasi kanal tersebut.
- Klik kontak hanya memulai tindakan pengguna; situs tidak menyatakan pesan sudah terkirim.

### FR08 Bagikan portofolio — P0 dasar dan P1 tambahan

- P0: tautan publik stabil, salin URL halaman, metadata judul/deskripsi/gambar pratinjau yang sesuai.
- P1: tombol berbagi sistem dengan fallback salin tautan, serta QR untuk domain final.
- QR, bila dibuat, harus diuji melalui pemindaian; URL teks tetap dicantumkan.
- Kegagalan berbagi tidak mengganggu navigasi atau CV.

### FR09 Admin tanpa coding — P0

**Kebutuhan:** satu akun pemilik; tidak ada pendaftaran pengunjung.

- Kelola profil, ketersediaan, kategori, studi kasus, pengalaman, pendidikan, perangkat, prestasi, kontak, dan CV PDF.
- Tambah/ubah draf, unggah sampul dan galeri, isi alt text/keterangan, atur urutan dan unggulan, pratinjau, terbitkan, atau tarik dari publik.
- Pengurutan menyediakan tombol naik/turun selain drag-and-drop.
- Pratinjau draf hanya dapat diakses pemilik atau melalui mekanisme pratinjau terbatas; URL publik tidak membuka draf.
- Tombol terbitkan menolak isian wajib yang belum lengkap dan menunjukkan letak masalah.
- Simpan gagal mempertahankan isian; terbitkan gagal mempertahankan versi publik sebelumnya.
- Sediakan riwayat perubahan dan pemulihan versi. Arsipkan lebih dahulu; penghapusan permanen memerlukan konfirmasi yang menyebut nama konten.
- Perubahan slug proyek yang sudah terbit membuat pengalihan dari URL lama agar tautan lamaran tetap berguna.

### FR10 Akses pemilik dan unggahan — P0

- Otorisasi dibuktikan pada sisi server untuk baca draf, perubahan data, dan unggahan; menyembunyikan tombol admin tidak cukup.
- Gunakan penyedia autentikasi yang mendukung login pemilik dan pemulihan akun; rahasia tidak disimpan di kode frontend.
- Validasi tipe, ukuran, dan isi unggahan. Format media publik P0: JPEG/PNG/WebP/AVIF dan PDF.
- SVG publik hanya dari aset yang telah dibersihkan; hapus skrip, event handler, referensi eksternal, serta markup aktif yang tidak diperlukan. Arsip SVG sumber tidak perlu dapat diunggah langsung oleh pengunjung.
- Pemulihan backup harus mencakup data dan aset, bukan hanya halaman HTML.

### FR11 Bahasa dan keadaan situs — P0 dasar, P1 Inggris

- P0 menggunakan bahasa Indonesia yang konsisten; istilah teknis dijelaskan pada penggunaan pertama.
- Nama resmi kegiatan atau perangkat dapat mempertahankan bahasa aslinya.
- P1 menambah versi Inggris setelah seluruh bagian utama diterjemahkan; jangan menampilkan tombol bahasa yang menghasilkan campuran acak.
- Halaman tidak ditemukan, data gagal, gambar hilang, kategori kosong, serta draf ditarik memiliki pesan dan jalan lanjut yang jelas.

### FR12 Statistik — P1

- Statistik hanya untuk pemilik, bukan penghitung popularitas di halaman publik.
- Lihat kunjungan, proyek yang dibuka, interaksi CV, dan klik kontak per periode.
- Keadaan tanpa data menampilkan “Belum ada data”; tidak memakai angka contoh seolah hasil nyata.
- Pencatatan tidak boleh mengirim isi formulir admin, pesan, email pengunjung, atau data draf.

## 10 Model konten

Konten disimpan terstruktur agar admin, halaman web, dan fitur filter memakai sumber yang sama. Berkas SVG menjadi referensi sumber, bukan basis data produksi.

| Entitas | Bidang utama |
| --- | --- |
| Profile | nama, nama pendek, headline, bio, pendidikan singkat, lokasi, foto, status dan periode magang, tanggal pembaruan |
| Project | id, slug, judul, ringkasan, kategori, jenis proyek, wilayah, tahun pengerjaan opsional, periode data terpisah, masalah, tujuan, metode, peran pribadi, hasil tim, keterbatasan, urutan, unggulan, status |
| ProjectMetric | label, nilai, satuan, konteks, tipe hasil, sumber, status verifikasi; misalnya hasil model atau lingkup studi |
| MediaAsset | id, file publik teroptimasi, original privat, jenis, dimensi, alt text, keterangan, kredit, halaman sumber, kelompok skenario, status kesiapan |
| Experience | organisasi, jabatan, tanggal mulai, tanggal akhir, masih berjalan, ringkasan, kontribusi, tag, project_ids yang dikonfirmasi, sumber, status |
| Education | institusi, program, tanggal, perkiraan selesai, IPK opsional, informasi tambahan |
| Skill | nama, kelompok, sumber, project_ids atau experience_ids sebagai bukti, urutan |
| Achievement | judul, tingkat capaian, tahun, penyelenggara bila diketahui, bukti URL opsional |
| ResumeAsset | PDF aktif, nama unduhan, ukuran, tanggal unggah, versi, tanggal sinkronisasi dengan CV HTML |
| ContactSettings | email utama, LinkedIn, WhatsApp opsional, kanal aktif |
| SiteSettings | bahasa, metadata, preferensi motion default, tautan kanonis, konfigurasi analitik |

Status editorial: `draft → ready_for_review → published → archived`. Perubahan pada konten terbit membuat revisi draf; versi publik tetap ada sampai pemilik menerbitkan revisi.

Bidang minimum sebelum proyek dapat diterbitkan: judul, slug unik, ringkasan, kategori, jenis proyek, peran pribadi, metode/proses, hasil dengan konteks, satu media valid dengan alt text, serta sumber internal. Metrik yang belum terverifikasi boleh disimpan pada draf, tetapi tidak boleh muncul pada halaman publik.

Contoh data P01, tanpa memasukkan angka skenario yang masih perlu diperiksa:

```json
{
  "id": "P01",
  "slug": "perencanaan-transportasi-wonokromo",
  "title": "Perencanaan Transportasi Wonokromo",
  "categories": ["transportasi", "gis"],
  "location": "Wonokromo, Surabaya",
  "project_type": "Proyek akademik",
  "project_type_verified": false,
  "project_year": null,
  "role_summary": "Ketua tim dan analisis TAZ serta trip assignment",
  "tools": ["PTV Visum"],
  "source_pages": [17, 18, 19],
  "featured": true,
  "sort_order": 1,
  "result_type": "model_scenario",
  "comparison_labels": ["Eksisting", "Proyeksi", "Skenario Rencana"],
  "metrics": [],
  "status": "draft"
}
```

## 11 Pengolahan aset SVG dan PDF

### 11.1 Temuan sumber

- 25 SVG berukuran total sekitar 153 MB, dengan ukuran individual sekitar 1,48–14,94 MB.
- Dokumen menggunakan dimensi presentasi 1920 × 1080. Pemeriksaan XML tidak menemukan node teks atau hyperlink eksternal yang dapat langsung dipakai sebagai konten web.
- Teks, logo tautan, dan layout presentasi perlu diubah menjadi komponen web serta konten HTML. Bentuk visual Linktree/Sheets pada slide bukan alamat yang dapat diekstrak sebagai link aktif.
- PDF CV memiliki 2 halaman dan 4 hyperlink bukti prestasi/pembicara. URL tersebut dapat diambil dari PDF, tetapi akses publiknya tetap diperiksa sebelum tombol bukti diaktifkan.

### 11.2 Keluaran pengolahan untuk implementasi

1. Susun teks studi kasus dari isi slide dan periksa kembali nama, angka, serta kontribusi pribadi.
2. Ambil gambar peta/foto yang relevan sebagai aset terpisah. Prioritaskan ekspor asli jika tersedia; hasil potongan slide menjadi solusi sementara bila masih terbaca.
3. Buat sampul bersih per proyek tanpa seluruh paragraf slide.
4. Simpan versi responsif untuk tampilan normal dan versi lebih tinggi untuk pembesaran peta.
5. Tulis ulang teks sebagai HTML; jangan mengubah seluruh SVG menjadi gambar halaman web.
6. Simpan sumber asli secara privat; situs hanya memuat aset publik yang diperlukan.
7. Periksa sumber foto, kredit peta, serta informasi pribadi pada foto kelompok atau tabel sebelum publikasi.

Anggaran awal yang diusulkan: sampul kartu ≤150 KB, visual hero ≤300 KB, gambar detail normal ≤350 KB, dan aset peta besar dimuat berdasarkan tindakan pengguna. Ukuran tersebut dapat dilonggarkan untuk keterbacaan peta dengan tetap mempertahankan pemuatan sesuai kebutuhan. Jangan memasukkan arsip 153 MB ke bundle publik.

## 12 Kebutuhan teknis dan mutu

### 12.1 Arsitektur yang diusulkan

- Halaman publik menggunakan HTML yang dirender di server atau dibuat statis agar profil, proyek, dan CV tetap terbaca sebelum JavaScript interaktif siap.
- Gunakan CMS atau admin berbasis formulir yang sudah mendukung autentikasi, draf, media, dan versi. Nama penyedia ditetapkan setelah anggaran dan lingkungan hosting jelas; tidak perlu membangun sistem CMS dari nol untuk memenuhi kebutuhan ini.
- Animasi memakai CSS dan SVG ringan, dengan JavaScript hanya untuk interaksi yang memerlukannya. Kanvas atau 3D penuh bukan prasyarat.
- Pisahkan aset publik, sumber privat, dan pratinjau draf. Backend hanya memaparkan data terbit kepada pengunjung.
- Penerbitan konten harus memperbarui halaman yang terdampak, menghapus cache lama bila perlu, dan menjaga URL CV/proyek tetap konsisten.
- Semua data profil dan proyek dapat diekspor dalam format terstruktur beserta aset untuk mengurangi ketergantungan pada satu platform.

### 12.2 Target kualitas

| Aspek | Target dan metode pemeriksaan |
| --- | --- |
| Responsif | Uji lebar 360, 768, 1024, dan 1440 px; pembesaran 200%; tidak ada gulir horizontal pada konten utama |
| Kinerja lapangan | Target persentil ke-75: LCP ≤2,5 detik, INP ≤200 ms, CLS ≤0,1; pisahkan mobile dan desktop. [R8] |
| Kinerja sebelum rilis | Jalankan 3 uji laboratorium mobile pada beranda, katalog, detail P01, dan CV; laporkan kondisi dan median. Hasil laboratorium bukan bukti kelulusan metrik lapangan |
| Anggaran awal | Target transfer awal beranda ≤1 MB termasuk media kritis; JavaScript awal terkompresi ≤200 KB, dengan pemisahan fitur nonkritis. Ini anggaran proyek, bukan ketentuan standar eksternal |
| Aksesibilitas | Target WCAG 2.2 AA; keyboard, fokus terlihat, label kontrol, alt text, heading, pembesaran, dan kontras teks biasa ≥4,5:1 diperiksa. Daftar ini bukan pengganti audit seluruh kriteria yang berlaku. [R7] |
| Sentuh | Target produk 44 × 44 CSS px untuk tombol utama; semua interaksi tersedia tanpa hover |
| Motion | Uji pengaturan reduced motion perangkat dan kontrol situs; isi serta navigasi tidak berubah atau hilang |
| Ketahanan | Profil dan CV HTML terbaca saat skrip animasi gagal; gambar gagal memiliki penjelasan; dokumen publik tidak meminta izin akses |
| Browser | Uji versi stabil saat rilis pada Chrome, Edge, Firefox, Safari, Android Chrome, dan iOS Safari; catat versi yang diuji |
| Penelusuran | Judul, deskripsi, canonical, sitemap, dan metadata berbagi sesuai halaman; nama proyek serta profil tersedia sebagai teks |
| Admin | Akses tanpa izin gagal pada UI dan permintaan langsung; draf serta aset privat tidak menjadi publik |

Statistik, domain, framework, penyedia CMS, dan hosting belum dipilih; jangan menampilkan klaim “gratis selamanya” atau estimasi biaya tanpa memeriksa paket yang akan digunakan.

## 13 Keadaan kosong dan kegagalan

| Keadaan | Respons yang diwajibkan |
| --- | --- |
| Tidak ada hasil filter | Penjelasan singkat, reset filter, tetap tampilkan navigasi |
| Peta resolusi tinggi gagal | Pertahankan preview dan uraian; tawarkan coba lagi |
| Tautan WebGIS belum tersedia | Sembunyikan tombol; jangan membuat URL contoh |
| PDF gagal dipratinjau | Berikan tautan PDF langsung dan CV HTML |
| Salin tautan gagal | Tampilkan URL yang dapat dipilih manual |
| Data lambat/gagal | Loading lokal, batas waktu, coba lagi, jalan kembali |
| Pengalaman tanpa bukti proyek | Tetap tampilkan informasi yang didukung CV; jangan membuat tautan bukti palsu |
| Proyek diarsipkan | Halaman menjelaskan karya tidak tersedia dan menawarkan katalog; tidak membocorkan draf |
| Slug proyek berubah | Alihkan URL lama ke URL baru |
| Simpan/unggah admin gagal | Pertahankan isian dan versi publik lama; tampilkan status yang jelas |

## 14 Pengukuran setelah rilis

Pengukuran adalah P1. Nama pengunjung atau status mereka sebagai HRD tidak dapat ditentukan hanya dari kunjungan situs.

| Event | Kapan dicatat | Data minimal |
| --- | --- | --- |
| `page_view` | Navigasi ke halaman publik selesai | path, jenis halaman |
| `project_view` | Detail proyek ditampilkan | project_id, kategori |
| `project_filter_change` | Pengunjung mengubah filter | kategori terpilih |
| `project_map_select` | Memilih indikator atau skenario peta | project_id, label pilihan |
| `resume_view` | CV HTML dibuka | path |
| `cv_pdf_open` | Klik buka PDF | versi CV |
| `cv_download_click` | Klik unduh PDF | versi CV; bukan konfirmasi unduhan selesai |
| `contact_click` | Klik kanal kontak | jenis kanal; bukan konfirmasi pesan terkirim |

KPI evaluasi: karya yang paling sering dibuka, proporsi sesi yang mengakses CV, dan proporsi sesi yang mengklik kontak. Gunakan jumlah **sesi dengan tindakan**, bukan jumlah seluruh klik, untuk rasio berbasis sesi. Definisi sesi dan estimasi pengunjung unik mengikuti penyedia secara konsisten dan dijelaskan pada dasbor.

Tentukan retensi, pemberitahuan privasi, dan pilihan penyedia sebelum analitik diaktifkan. Pada trafik kecil, gunakan hasil sebagai petunjuk eksplorasi dan padukan dengan umpan balik pembaca.

## 15 Tahap implementasi dan batas rilis

| Tahap | Keluaran | Syarat lanjut |
| --- | --- | --- |
| A Konten | Inventaris 7 proyek, data CV, aset terpisah, daftar angka yang perlu dikonfirmasi | Satu studi kasus P01 lengkap dan bahan dasar semua karya siap |
| B Desain | Beranda, katalog, detail P01, CV, admin, serta spesifikasi mobile/reduced motion | Pemilik menilai alur dan karakter visual dengan isi nyata |
| C Implementasi inti | FR01–FR11 sesuai cakupan P0, admin, pemuatan aset, dan navigasi | Semua alur utama dapat digunakan tanpa data contoh |
| D Pemeriksaan | Pengujian tugas, aksesibilitas, browser, konten, keamanan admin, dan kinerja | Masalah yang menghalangi pembacaan, kontak, unduhan, atau pembaruan diselesaikan |
| E Publikasi | Domain/URL final, sitemap, CV aktif, sumber konten, backup, panduan admin | Pemilik memeriksa informasi akhir dan keputusan penerbitan |
| F Penyempurnaan | Analitik, versi Inggris, tombol berbagi sistem, QR, perbandingan peta lanjutan | Ada kebutuhan nyata dan data/aset pendukung |

Di luar P0: akun HRD, chatbot, formulir lamaran, backend simulasi transportasi, data lalu lintas live, pengolahan GIS dari unggahan publik, 3D kota penuh, serta kalkulator kelayakan/TOPSIS. Peta interaktif yang sudah dibuat pemilik dapat ditautkan tanpa membangun ulang seluruh platformnya.

Tanggal dan anggaran implementasi ditentukan setelah lingkungan pengembangan, hosting, serta kesiapan aset diketahui. Penetapan PRD tidak berarti situs sudah dibangun atau diterbitkan.

## 16 Pengujian penerimaan

| ID | Skenario uji | Hasil yang wajib |
| --- | --- | --- |
| AT01 | Buka beranda di ponsel dengan koneksi dibatasi | Nama dan tombol tersedia; animasi tidak menghalangi penggunaan |
| AT02 | Buka P01 langsung, lalu ganti 3 skenario peta | URL berfungsi; label dan legenda sesuai; tidak ada angka simulasi yang disajikan sebagai hasil implementasi |
| AT03 | Filter transportasi, buka karya, lalu tekan Back | Kategori dan posisi katalog dipertahankan |
| AT04 | Baca CV dengan filter, buka semua, lalu cetak | Informasi publik lengkap; filter dapat direset; cetak tidak memotong uraian |
| AT05 | Unduh CV dan gunakan kontak tanpa login | PDF dapat diakses; email dan LinkedIn benar; kegagalan clipboard punya alternatif |
| AT06 | Aktifkan reduced motion dan matikan JavaScript | Gerak berkurang sesuai preferensi; HTML inti tetap terbaca tanpa skrip |
| AT07 | Gunakan keyboard untuk menu, filter, dan modal | Fokus terlihat dan berurutan; Escape menutup modal; fokus kembali |
| AT08 | Login admin, tambah karya, pratinjau, terbitkan | Pemilik berhasil tanpa kode; draf tidak terlihat sebelum diterbitkan |
| AT09 | Gagalkan simpan admin atau unggah PDF | Isian tidak hilang; konten/PDF publik sebelumnya tetap aktif |
| AT10 | Ubah slug, arsipkan karya, lalu pulihkan revisi | URL lama ditangani; versi yang sesuai dipulihkan; draf tetap privat |
| AT11 | Minta data draf atau operasi tulis tanpa otorisasi | Server menolak; tidak ada kebocoran data/aset privat |
| AT12 | Uji gambar hilang, PDF preview gagal, filter kosong, URL salah | Ada pesan dan jalan lanjut; tidak ada halaman buntu |
| AT13 | Pemilik menambah karya dan mengganti CV | Selesai tanpa coding; metadata, urutan, dan sumber CV konsisten |

**Definisi selesai P0:** seluruh skenario P0 lulus; tidak ada placeholder publik; nama, kontak, peran, dan angka telah ditinjau; seluruh peta memiliki label yang terbaca; sumber asli dan backup tersedia; pemilik dapat memperbarui konten. Status rilis baru ditetapkan setelah pemeriksaan tersebut, bukan hanya setelah tampilan beranda selesai.

## 17 Keputusan yang masih terbuka

Hal berikut tidak menghalangi penyusunan rancangan. Data yang belum jelas disimpan sebagai draf atau dihilangkan dari tampilan publik sampai dikonfirmasi.

| Hal | Temuan | Keputusan sementara |
| --- | --- | --- |
| Penekanan halaman 18–19 | Memuat Wonokromo | Jadikan unggulan pertama; pemilik dapat mengubah urutan |
| Periode UHI | 2015–2024 pada uraian, 2014–2024 pada satu label SVG 9 | Gunakan judul multitemporal tanpa rentang tahun sampai final |
| Skor Malang | Uraian SVG 4 berbeda dari tabel SVG 5 | Jangan tampilkan ringkasan angka sebelum tabel final dipilih |
| Hasil Wonokromo | Angka skenario belum disertai lampiran dasar perhitungan | Gunakan uraian hasil model; angka sorotan menunggu pemeriksaan |
| Gerigi x UKM Expo | CV menyebut 2025, profil SVG 2 menyebut 2026 | Jadikan entri draf sampai tahun/rentang kegiatan dikonfirmasi |
| Proyek LokaSolution | CV memuat pengalaman proyek, SVG 24 memuat pelatihan/simulasi | Pisahkan pengalaman organisasi/proyek dari studi kasus pelatihan |
| Periode dan mode magang | Belum disebutkan | Status umum terbuka untuk peluang; jangan menebak tanggal/lokasi tujuan |
| Status pengalaman berjalan | Beberapa entri CV menggunakan “sekarang” atau “persiapan” | Pemilik memeriksa status pada saat publikasi |
| URL laporan dan WebGIS | Logo tautan terlihat, tetapi URL tidak tertanam pada SVG | Tombol bukti tidak diaktifkan sampai URL asli diberikan |
| Tahun dan jenis proyek | Tidak semua proyek mencantumkan periode/konteks lengkap | Sediakan bidang opsional; klasifikasi akademik diperiksa sebelum terbit |
| Kanal WhatsApp | Nomor telepon ada pada CV; pilihan kanal belum eksplisit | Default nonaktif; email dan LinkedIn aktif |
| Bahasa | Belum ada pilihan eksplisit | Indonesia P0, Inggris P1 |
| Hosting, domain, dan anggaran | Belum ditetapkan | Arsitektur tetap dapat dipindah; penyedia dipilih saat implementasi |
| Subfitur flow yang terlipat | Tiga modul awal diagram menampilkan “Lihat semua (4)” | Jangan mengarang subfitur keempat; rekonsiliasi saat flow lengkap tersedia |

## 18 Sumber dan penelusuran

### 18.1 Sumber pemilik

- **S1 — Diagram alur awal:** PNG yang disertakan pada percakapan; delapan modul dari profil hingga statistik.
- **S2 — `Portofolio.zip`:** 25 berkas SVG. Rujukan halaman pada dokumen ini memakai nomor nama berkas, bukan nomor halaman browser.
- **S3 — `Muhammad Mirza Wibisono-resume (1)(3).pdf`:** CV 2 halaman, sumber pendidikan, pengalaman, kontak, perangkat, dan prestasi.
- **S4 — Arahan pemilik pada 21 Oktober 2026:** target magang beragam, perhatian pada halaman 18–19, SVG sebagai referensi materi, tema transportasi/perkotaan, CV interaktif, pengelolaan tanpa coding, dan keluaran Markdown.

Penelusuran publik menemukan profil LinkedIn dengan URL yang sama dengan CV dan ringkasan jabatan yang konsisten. Halaman lengkap tidak dapat diambil, sehingga tidak ada fakta baru tentang pemilik yang ditambahkan berdasarkan asumsi atau profil orang lain.

### 18.2 Referensi web

Referensi diperiksa pada 21 Oktober 2026. Gagasan penerapan dalam PRD merupakan penilaian desain untuk kebutuhan situs ini.

- **R1 — Gehl Projects:** https://www.gehlpeople.com/projects/
- **R2 — Applied Legible London:** https://appliedinformation.group/projects/legible-london
- **R3 — Applied TransLink Vancouver:** https://appliedinformation.group/projects/translink
- **R4 — MVRDV Projects:** https://www.mvrdv.com/projects
- **R5 — MDN prefers-reduced-motion:** https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@media/prefers-reduced-motion
- **R6 — MDN View Transition API:** https://developer.mozilla.org/en-US/docs/Web/API/View_Transition_API
- **R7 — W3C WCAG 2.2 Quick Reference:** https://www.w3.org/WAI/WCAG22/quickref/
- **R8 — Google web.dev Web Vitals:** https://web.dev/articles/vitals

### 18.3 Riwayat perubahan

| Versi | Perubahan |
| --- | --- |
| 0.1 | Kebutuhan awal berdasarkan diagram; dokumen Word |
| 0.2 | Format Markdown; identitas dan CV aktual; inventaris 7 studi kasus dari 25 SVG; Wonokromo sebagai unggulan; desain dan motion transportasi/perkotaan; CV interaktif; admin tanpa coding P0; referensi web; aturan pengolahan aset; serta catatan perbedaan data |

# Halte Menuju Dunia Saya — paket intro portofolio

Animasi pembuka 8 detik (kota padat sore hari → bus datang → naik → halaman portofolio).
Murni canvas 2D + JavaScript biasa: **tanpa library, tanpa gambar/video**, total ± 60 KB.

## Isi paket
| File | Fungsi |
| --- | --- |
| `halte-intro.js` | Seluruh animasi, suara (dibuat lewat Web Audio), layar sambutan, dan API `HalteIntro` |
| `halte-intro.css` | Gaya layar sambutan & tombol. Memakai token PRD Anda bila ada (`--color-hero-bg`, `--color-primary`, dst.) |
| `demo.html` | Contoh halaman jalan sendiri. Buka lewat server lokal untuk mencoba |

## Pasang di project (HTML / CSS / JS biasa) — 3 langkah
1. Salin folder ini ke project, misalnya `assets/halte-intro/`.
2. Di `<head>` halaman utama (`index.html`), tambahkan **setelah** `main.css`:
   ```html
   <link rel="stylesheet" href="assets/halte-intro/halte-intro.css">
   <script src="assets/halte-intro/halte-intro.js" data-auto></script>
   ```
   `data-auto` membuat intro jalan otomatis dan menyembunyikan halaman di baliknya, jadi tidak ada kedipan hero.
3. (Opsional) Animasikan hero Anda setelah intro selesai. Saat intro usai, `<html>` mendapat class `hi-done`:
   ```css
   .hero-title{opacity:0;transform:translateY(14px);transition:opacity .6s,transform .6s}
   html.hi-done .hero-title{opacity:1;transform:none}
   ```
   Atau dengarkan event: `window.addEventListener('halte-intro:done', () => { /* ... */ })`.

Selesai. Bagian akhir animasi memudar ke warna `--color-hero-bg` (otomatis dibaca; cadangan `#14211C`), sehingga menyatu dengan hero asli Anda.

## Pasang manual (kontrol penuh)
```html
<script src="assets/halte-intro/halte-intro.js"></script>
<script>
  HalteIntro.init({
    greeting: 'Hai, aku Mirza!',
    busLabel: 'ST-05 · PORTOFOLIO',
    once: true,                       // tampil sekali per sesi tab
    onDone: () => console.log('intro selesai')
  });
</script>
```
Tanpa `data-auto`, tambahkan sendiri `html.hi-pending body>*:not(.hi-root){visibility:hidden}` bila ingin mencegah kedipan, atau biarkan saja.

### React / Vite / Next.js
```js
import './halte-intro/halte-intro.css';
import './halte-intro/halte-intro.js';   // mendaftarkan window.HalteIntro

useEffect(() => { window.HalteIntro.init(); }, []);   // client-side saja
```
Di Next.js, panggil di komponen client (`'use client'`) lewat `useEffect`.

## Opsi
| Opsi | Bawaan | Keterangan |
| --- | --- | --- |
| `greeting` | `Hai, aku Mirza!` | Judul layar sambutan |
| `tag` | `PORTOFOLIO · PWK ITS` | Teks kecil di atas judul |
| `description` | (lihat file) | Kalimat penjelas di layar sambutan |
| `btnSound` / `btnMute` / `skipText` | teks tombol | Tombol mulai dengan suara, tanpa suara, dan tautan lewati |
| `busLabel` | `ST-05 · PORTOFOLIO` | Teks LED berjalan di papan tujuan bus |
| `busDecal` | `URBAN TRANSIT · PWK ITS` | Tulisan di badan bus |
| `gate` | `true` | `false` = langsung putar tanpa layar sambutan (suara mati) |
| `once` | `true` | Hanya tampil sekali per sesi tab (`sessionStorage`) |
| `storageKey` | `halteIntroSeen` | Kunci penyimpanan untuk `once` |
| `lockScroll` | `true` | Kunci scroll selama intro |
| `heroBg` | otomatis | Warna latar akhir (hex). Bawaan membaca `--color-hero-bg` |
| `onStart` / `onDone` | `null` | Callback |

API: `HalteIntro.init(opts)`, `HalteIntro.replay()`, `HalteIntro.skip()`.
Event: `halte-intro:start`, `halte-intro:done`.

## Perilaku yang sudah ditangani
- **Tidak mengagetkan:** layar sambutan menjelaskan isi intro; pengunjung memilih dengan/tanpa suara; intro dan suara muncul perlahan.
- **Suara:** hanya menyala setelah klik tombol (aturan autoplay browser), dan bisa dimatikan kapan saja.
- **Bisa dilewati:** tombol "Lewati intro", tautan di layar sambutan, dan tombol `Esc`.
- **Aksesibilitas:** pengguna dengan "kurangi gerakan" (`prefers-reduced-motion`) langsung masuk ke portofolio; fokus keyboard terlihat; dialog diberi label.
- **Kinerja:** latar digambar sekali dan di-cache; jika perangkat lambat, asap dan kabut dikurangi otomatis.
- **Sekali per sesi:** kunjungan berikutnya dalam tab yang sama langsung ke portofolio. Untuk menguji ulang, jalankan `sessionStorage.removeItem('halteIntroSeen')` di konsol atau panggil `HalteIntro.replay()`.

## Kustomisasi lebih dalam
- Warna kendaraan, bus, dan kota ada di bagian atas `halte-intro.js` (objek `K`, larik `CC`, `JK`, `HL`, `PL`).
- Durasi total 8 detik. Titik waktu utama: bus datang 2,6 dtk, pintu terbuka 4,2 dtk, kamera masuk 5,1–6,4 dtk, memudar ke hero 6,1–7,3 dtk.
- Klakson dan efek suara ada pada larik `HORNS` dan `EV`.

## Pemecahan masalah
- **Layar sambutan tidak muncul:** mungkin sudah pernah dilihat di tab ini (`once`). Hapus kuncinya atau buka tab privat baru.
- **Warna akhir tidak sama dengan hero:** pastikan `--color-hero-bg` didefinisikan di `:root` dengan format `#RRGGBB`, atau berikan `heroBg`.
- **Halaman tetap tersembunyi:** pastikan file JS termuat (periksa path). Sebagai pengaman, class `hi-pending` dilepas otomatis setelah 6 detik pada mode `data-auto`.
- **Dibuka lewat `file://`:** sebagian browser membatasi penyimpanan sesi. Gunakan server lokal (`npx serve`).

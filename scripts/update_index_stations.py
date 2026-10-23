with open('templates/index.html', 'r', encoding='utf-8') as f:
    html = f.read()

start_marker = '<!-- Stasiun 1: INI LHO ITS 2026'
end_marker = '    </div>\n\n    <div style="text-align:center;margin-top:3rem;" class="reveal">'

idx_start = html.find(start_marker)
idx_end = html.find(end_marker)

assert idx_start != -1, "start_marker not found"
assert idx_end != -1, "end_marker not found"

new_stations_html = """<!-- Stasiun 1: INI LHO ITS 2026 (Sep 2025 - Mar 2026) -->
      <div class="metro-timeline-item" data-station="st-01" id="exp-station-1">
        <div class="metro-station-badge-node">
          <div class="metro-badge-core badge-media badge-metro-media">
            <span class="station-code-pill">ST-01</span>
          </div>
        </div>
        <div class="timeline-content exp-thematic-card" data-theme="media">
          <div style="display:flex;justify-content:space-between;align-items:flex-start;flex-wrap:wrap;gap:0.5rem;margin-bottom:0.35rem;">
            <h3 style="font-size:1.15rem;font-weight:700;color:var(--color-text-main);margin:0;">INI LHO ITS 2026!</h3>
            <span style="font-family:var(--font-mono);font-size:0.8rem;font-weight:600;color:var(--color-text-light);">Sep 2025 &ndash; Mar 2026</span>
          </div>
          <div style="font-size:0.95rem;font-weight:600;color:var(--color-primary);margin-bottom:0.5rem;">
            Ketua Subdivisi Media Production
          </div>
          <p style="font-size:0.925rem;color:var(--color-text-muted);line-height:1.6;margin:0;">
            Saat menjadi Ketua Subdivisi Media Production, berhasil memimpin tim dalam memproduksi 84 motion graphics, 18 visual editing, dan 8 proyek video siaran (total 110 karya visual tim) untuk menjangkau puluhan ribu calon mahasiswa baru ITS.
          </p>
        </div>
      </div>

      <!-- Stasiun 2: Dinas Perhubungan Kabupaten Sidoarjo (Nov 2025 - Des 2025) -->
      <div class="metro-timeline-item" data-station="st-02" id="exp-station-2">
        <div class="metro-station-badge-node">
          <div class="metro-badge-core badge-transit badge-metro-transit">
            <span class="station-code-pill">ST-02</span>
          </div>
        </div>
        <div class="timeline-content exp-thematic-card" data-theme="transit">
          <div style="display:flex;justify-content:space-between;align-items:flex-start;flex-wrap:wrap;gap:0.5rem;margin-bottom:0.35rem;">
            <h3 style="font-size:1.15rem;font-weight:700;color:var(--color-text-main);margin:0;">Dinas Perhubungan Kabupaten Sidoarjo</h3>
            <span style="font-family:var(--font-mono);font-size:0.8rem;font-weight:600;color:var(--color-text-light);">Nov 2025 &ndash; Des 2025</span>
          </div>
          <div style="font-size:0.95rem;font-weight:600;color:var(--color-primary);margin-bottom:0.5rem;">
            Surveyor Operasional Angkutan Pedesaan & Transjatim
          </div>
          <p style="font-size:0.925rem;color:var(--color-text-muted);line-height:1.6;margin:0;">
            Melakukan survei lapangan kondisi armada angkutan pedesaan, evaluasi cakupan trayek, serta wawancara langsung kepada penumpang angkot dan Transjatim untuk penyusunan laporan mobilitas wilayah Dishub Sidoarjo.
          </p>
        </div>
      </div>

      <!-- Stasiun 3: Laboratorium PWK ITS (Mar 2026 - Sekarang) -->
      <div class="metro-timeline-item" data-station="st-03" id="exp-station-3">
        <div class="metro-station-badge-node">
          <div class="metro-badge-core badge-spatial badge-metro-spatial">
            <span class="station-code-pill">ST-03</span>
          </div>
        </div>
        <div class="timeline-content exp-thematic-card" data-theme="spatial">
          <div style="display:flex;justify-content:space-between;align-items:flex-start;flex-wrap:wrap;gap:0.5rem;margin-bottom:0.35rem;">
            <h3 style="font-size:1.15rem;font-weight:700;color:var(--color-text-main);margin:0;">Laboratorium PWK ITS</h3>
            <span style="font-family:var(--font-mono);font-size:0.8rem;font-weight:600;color:var(--color-text-light);">Mar 2026 &ndash; Sekarang</span>
          </div>
          <div style="font-size:0.95rem;font-weight:600;color:var(--color-primary);margin-bottom:0.5rem;">
            Asisten Dosen Sistem Informasi Perencanaan & Metode Analisis (MAP)
          </div>
          <p style="font-size:0.925rem;color:var(--color-text-muted);line-height:1.6;margin:0;">
            Membimbing langsung 45 mahasiswa dalam 15 modul praktikum laboratorium: pengolahan raster & vektor GIS, WebGIS interaktif, serta metode kuantitatif analisis wilayah menggunakan Excel dan SPSS.
          </p>
        </div>
      </div>

      <!-- Stasiun 4: Planopolis 2026 (Mei 2026 - Sekarang) -->
      <div class="metro-timeline-item" data-station="st-04" id="exp-station-4">
        <div class="metro-station-badge-node">
          <div class="metro-badge-core badge-leadership badge-metro-leadership">
            <span class="station-code-pill">ST-04</span>
          </div>
        </div>
        <div class="timeline-content exp-thematic-card" data-theme="leadership">
          <div style="display:flex;justify-content:space-between;align-items:flex-start;flex-wrap:wrap;gap:0.5rem;margin-bottom:0.35rem;">
            <h3 style="font-size:1.15rem;font-weight:700;color:var(--color-text-main);margin:0;">Planopolis 2026</h3>
            <span style="font-family:var(--font-mono);font-size:0.8rem;font-weight:600;color:var(--color-text-light);">Mei 2026 &ndash; Sekarang</span>
          </div>
          <div style="font-size:0.95rem;font-weight:600;color:var(--color-primary);margin-bottom:0.5rem;">
            Project Officer (Pimpinan Tertinggi)
          </div>
          <p style="font-size:0.925rem;color:var(--color-text-muted);line-height:1.6;margin:0;">
            Pimpinan tertinggi perhelatan akbar PWK ITS berskala nasional: mengarahkan visi dan memimpin langsung koordinasi strategis 100+ staf panitia yang tersebar di 8 divisi operasional.
          </p>
        </div>
      </div>

      <!-- Stasiun 5: PT Mitra Pengembang Kawasan x LokaSolution (Jun 2026 - Sekarang) -->
      <div class="metro-timeline-item" data-station="st-05" id="exp-station-5">
        <div class="metro-station-badge-node">
          <div class="metro-badge-core badge-consulting badge-metro-consulting">
            <span class="station-code-pill">ST-05</span>
          </div>
        </div>
        <div class="timeline-content exp-thematic-card" data-theme="consulting">
          <div style="display:flex;justify-content:space-between;align-items:flex-start;flex-wrap:wrap;gap:0.5rem;margin-bottom:0.35rem;">
            <h3 style="font-size:1.15rem;font-weight:700;color:var(--color-text-main);margin:0;">PT Mitra Pengembang Kawasan x LokaSolution</h3>
            <span style="font-family:var(--font-mono);font-size:0.8rem;font-weight:600;color:var(--color-text-light);">Jun 2026 &ndash; Sekarang</span>
          </div>
          <div style="font-size:0.95rem;font-weight:600;color:var(--color-primary);margin-bottom:0.5rem;">
            Vice Project Leader & Konsultan Tata Ruang
          </div>
          <p style="font-size:0.925rem;color:var(--color-text-muted);line-height:1.6;margin:0;">
            Memimpin perumusan kajian spasial, riset potensi pasar kawasan, analisis benchmarking kompetitor, serta penyusunan rekomendasi kelayakan bisnis untuk mitra pengembang real estate.
          </p>
        </div>
      </div>
"""

html = html[:idx_start] + new_stations_html + html[idx_end:]

with open('templates/index.html', 'w', encoding='utf-8') as f:
    f.write(html)

print("SUCCESS: templates/index.html updated cleanly!")

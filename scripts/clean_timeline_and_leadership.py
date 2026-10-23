with open('templates/index.html', 'r', encoding='utf-8') as f:
    c = f.read()

# 1. Fix leadership pill text contrast
old_lead_strip = """        <!-- Highlight Proyek Kepemimpinan Nyata -->
        <div class="leadership-projects-strip" style="margin:0.85rem 0;display:flex;flex-direction:column;gap:0.4rem;">
          <div class="lead-project-pill" style="font-size:0.8rem;background:rgba(255,255,255,0.04);border:1px solid rgba(132,169,80,0.22);border-radius:var(--radius-md);padding:0.4rem 0.65rem;color:var(--color-hero-text);display:flex;align-items:center;gap:0.5rem;">
            <span style="color:#84A950;font-weight:800;">⚡</span>
            <span><strong>Project Officer Planopolis 2026:</strong> Pimpinan tertinggi perhelatan akbar PWK ITS (100+ panitia lintas 8 divisi)</span>
          </div>
          <div class="lead-project-pill" style="font-size:0.8rem;background:rgba(255,255,255,0.04);border:1px solid rgba(132,169,80,0.22);border-radius:var(--radius-md);padding:0.4rem 0.65rem;color:var(--color-hero-text);display:flex;align-items:center;gap:0.5rem;">
            <span style="color:#D97736;font-weight:800;">⚡</span>
            <span><strong>Ketua Subdivisi Media Production:</strong> Memimpin tim kreatif menghasilkan 110 karya visual</span>
          </div>
          <div class="lead-project-pill" style="font-size:0.8rem;background:rgba(255,255,255,0.04);border:1px solid rgba(132,169,80,0.22);border-radius:var(--radius-md);padding:0.4rem 0.65rem;color:var(--color-hero-text);display:flex;align-items:center;gap:0.5rem;">
            <span style="color:#2F86C9;font-weight:800;">⚡</span>
            <span><strong>Vice Project Leader LokaSolution:</strong> Memimpin konsultasi perencanaan dan analisis tata ruang</span>
          </div>
        </div>"""

new_lead_strip = """        <!-- Highlight Proyek Kepemimpinan Nyata (Warna Kontras Jelas & Rapi) -->
        <div class="leadership-projects-strip" style="margin:1rem 0;display:flex;flex-direction:column;gap:0.55rem;">
          <div class="lead-project-pill" style="font-size:0.85rem;background:#F4F7F4;border:1px solid rgba(49,92,55,0.22);border-radius:var(--radius-md);padding:0.55rem 0.85rem;display:flex;align-items:flex-start;gap:0.6rem;line-height:1.5;">
            <span style="color:#D97736;font-size:1rem;line-height:1.2;flex-shrink:0;">⚡</span>
            <span style="color:#14211C;"><strong style="color:#315C37;">Project Officer Planopolis 2026:</strong> Pimpinan tertinggi perhelatan akbar PWK ITS (100+ panitia lintas 8 divisi)</span>
          </div>
          <div class="lead-project-pill" style="font-size:0.85rem;background:#F4F7F4;border:1px solid rgba(49,92,55,0.22);border-radius:var(--radius-md);padding:0.55rem 0.85rem;display:flex;align-items:flex-start;gap:0.6rem;line-height:1.5;">
            <span style="color:#D97736;font-size:1rem;line-height:1.2;flex-shrink:0;">⚡</span>
            <span style="color:#14211C;"><strong style="color:#315C37;">Ketua Subdivisi Media Production:</strong> Memimpin tim kreatif menghasilkan 110 karya visual</span>
          </div>
          <div class="lead-project-pill" style="font-size:0.85rem;background:#F4F7F4;border:1px solid rgba(49,92,55,0.22);border-radius:var(--radius-md);padding:0.55rem 0.85rem;display:flex;align-items:flex-start;gap:0.6rem;line-height:1.5;">
            <span style="color:#2F6F9E;font-size:1rem;line-height:1.2;flex-shrink:0;">⚡</span>
            <span style="color:#14211C;"><strong style="color:#315C37;">Vice Project Leader LokaSolution:</strong> Memimpin konsultasi perencanaan dan analisis tata ruang</span>
          </div>
        </div>"""

c_norm = c.replace('\r\n', '\n')
old_lead_norm = old_lead_strip.replace('\r\n', '\n')
new_lead_norm = new_lead_strip.replace('\r\n', '\n')

assert old_lead_norm in c_norm, "old_lead_strip not found"
c_norm = c_norm.replace(old_lead_norm, new_lead_norm, 1)

# 2. Replace the timeline container with clean, simplified cards (no poin-poin clutter)
start_marker = '<div class="transit-metro-timeline reveal" id="metro-timeline-container">'
end_marker = '<!-- Station 5: PT Mitra Pengembang Kawasan x LokaSolution'
# Let's find end of station 5
station5_end = c_norm.find('</div>\n      </div>\n\n    </div>\n\n    <div style="text-align:center;margin-top:3rem;"', c_norm.find(start_marker))

if station5_end != -1:
    station5_end += len('</div>\n      </div>\n\n    </div>')
    
    clean_timeline_html = """<div class="transit-metro-timeline reveal" id="metro-timeline-container">

      <!-- Stasiun 1: INI LHO ITS 2026 (Sep 2025 - Mar 2026) -->
      <div class="metro-timeline-item" data-station="st-01" id="exp-station-1">
        <div class="metro-station-badge-node">
          <div class="metro-badge-core badge-media">
            <span class="station-code-pill">ST-01</span>
          </div>
        </div>
        <div class="timeline-content exp-thematic-card" data-theme="media">
          <div style="display:flex;justify-content:space-between;align-items:flex-start;flex-wrap:wrap;gap:0.5rem;margin-bottom:0.35rem;">
            <h3 style="font-size:1.15rem;font-weight:700;color:var(--color-text-main);margin:0;">INI LHO ITS 2026!</h3>
            <span style="font-family:var(--font-mono);font-size:0.8rem;font-weight:600;color:var(--color-text-light);">Sep 2025 – Mar 2026</span>
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
          <div class="metro-badge-core badge-transit">
            <span class="station-code-pill">ST-02</span>
          </div>
        </div>
        <div class="timeline-content exp-thematic-card" data-theme="transit">
          <div style="display:flex;justify-content:space-between;align-items:flex-start;flex-wrap:wrap;gap:0.5rem;margin-bottom:0.35rem;">
            <h3 style="font-size:1.15rem;font-weight:700;color:var(--color-text-main);margin:0;">Dinas Perhubungan Kabupaten Sidoarjo</h3>
            <span style="font-family:var(--font-mono);font-size:0.8rem;font-weight:600;color:var(--color-text-light);">Nov 2025 – Des 2025</span>
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
          <div class="metro-badge-core badge-spatial">
            <span class="station-code-pill">ST-03</span>
          </div>
        </div>
        <div class="timeline-content exp-thematic-card" data-theme="spatial">
          <div style="display:flex;justify-content:space-between;align-items:flex-start;flex-wrap:wrap;gap:0.5rem;margin-bottom:0.35rem;">
            <h3 style="font-size:1.15rem;font-weight:700;color:var(--color-text-main);margin:0;">Laboratorium PWK ITS</h3>
            <span style="font-family:var(--font-mono);font-size:0.8rem;font-weight:600;color:var(--color-text-light);">Mar 2026 – Sekarang</span>
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
          <div class="metro-badge-core badge-leadership">
            <span class="station-code-pill">ST-04</span>
          </div>
        </div>
        <div class="timeline-content exp-thematic-card" data-theme="leadership">
          <div style="display:flex;justify-content:space-between;align-items:flex-start;flex-wrap:wrap;gap:0.5rem;margin-bottom:0.35rem;">
            <h3 style="font-size:1.15rem;font-weight:700;color:var(--color-text-main);margin:0;">Planopolis 2026</h3>
            <span style="font-family:var(--font-mono);font-size:0.8rem;font-weight:600;color:var(--color-text-light);">Mei 2026 – Sekarang</span>
          </div>
          <div style="font-size:0.95rem;font-weight:600;color:var(--color-primary);margin-bottom:0.5rem;">
            Project Officer (Ketua Pelaksana Utama)
          </div>
          <p style="font-size:0.925rem;color:var(--color-text-muted);line-height:1.6;margin:0;">
            Memimpin perhelatan akbar tahunan PWK ITS tingkat nasional. Menyusun Grand Design operasional dan memimpin koordinasi lebih dari 100 panitia dan staf operasional lintas 8 divisi serta 10 subdivisi.
          </p>
        </div>
      </div>

      <!-- Stasiun 5: PT Mitra Pengembang Kawasan x LokaSolution (Jun 2026 - Sekarang) -->
      <div class="metro-timeline-item" data-station="st-05" id="exp-station-5">
        <div class="metro-station-badge-node">
          <div class="metro-badge-core badge-consulting">
            <span class="station-code-pill">ST-05</span>
          </div>
        </div>
        <div class="timeline-content exp-thematic-card" data-theme="consulting">
          <div style="display:flex;justify-content:space-between;align-items:flex-start;flex-wrap:wrap;gap:0.5rem;margin-bottom:0.35rem;">
            <h3 style="font-size:1.15rem;font-weight:700;color:var(--color-text-main);margin:0;">PT Mitra Pengembang Kawasan x LokaSolution</h3>
            <span style="font-family:var(--font-mono);font-size:0.8rem;font-weight:600;color:var(--color-text-light);">Jun 2026 – Sekarang</span>
          </div>
          <div style="font-size:0.95rem;font-weight:600;color:var(--color-primary);margin-bottom:0.5rem;">
            Vice Project Leader & Konsultan Tata Ruang
          </div>
          <p style="font-size:0.925rem;color:var(--color-text-muted);line-height:1.6;margin:0;">
            Memimpin perumusan kajian spasial, riset potensi pasar kawasan, analisis benchmarking kompetitor, serta penyusunan rekomendasi kelayakan bisnis untuk mitra pengembang real estate.
          </p>
        </div>
      </div>

    </div>"""

    start_pos = c_norm.find(start_marker)
    c_norm = c_norm[:start_pos] + clean_timeline_html + c_norm[station5_end:]
    print("SUCCESS: Simplified timeline cards and removed all poin-poin/badges clutter!")
else:
    print("WARNING: Could not find station 5 end marker")

with open('templates/index.html', 'w', encoding='utf-8') as f:
    f.write(c_norm)

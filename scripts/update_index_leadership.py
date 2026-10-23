with open('templates/index.html', 'r', encoding='utf-8') as f:
    c = f.read()

# 1. Update Hero intro text
c = c.replace(
    "Project Officer Planopolis 2026 (koordinasi 8 divisi & 10 subdivisi), Asisten Dosen 2 Laboratorium PWK ITS, hingga memimpin 110 karya visual media.",
    "Project Officer Planopolis 2026 (memimpin 100+ staf & panitia lintas 8 divisi), Ketua Subdivisi Media Production INI LHO ITS 2026 (berhasil memimpin 110 karya visual tim), dan Founder LokaSolution."
)

# 2. Update Leadership USP Card
old_lead_card = """        <h3 class="usp-feature-title">Konsisten Dipercaya Menjadi Pemimpin</h3>
        <p class="usp-feature-desc">
          Terbukti berulang kali dipercaya sebagai Ketua Pelaksana, Koordinator Tim Studio, Project Leader, dan Kepala Subdivisi. Mahir merumuskan Work Breakdown Structure (WBS), mengelola dinamika tim lintas disiplin, serta mengambil keputusan solutif di bawah tenggat waktu ketat.
        </p>

        <!-- Fun Interactive Leadership Impact Counters -->
        <div class="leadership-impact-bar" title="Rekam Jejak Kepemimpinan Mirza">
          <div class="impact-stat-item">
            <span class="impact-stat-num">8</span>
            <span class="impact-stat-lbl">Divisi Tim</span>
          </div>
          <div class="impact-stat-divider"></div>
          <div class="impact-stat-item">
            <span class="impact-stat-num">45</span>
            <span class="impact-stat-lbl">Mhs Praktikum</span>
          </div>
          <div class="impact-stat-divider"></div>
          <div class="impact-stat-item">
            <span class="impact-stat-num">110+</span>
            <span class="impact-stat-lbl">Karya Visual</span>
          </div>
        </div>

        <div class="usp-feature-tags" style="margin-top:auto;">
          <span class="usp-subtag">WBS & Action Plan</span>
          <span class="usp-subtag">Komunikasi Artikulatif</span>
          <span class="usp-subtag">Manajemen Konflik</span>
        </div>"""

new_lead_card = """        <h3 class="usp-feature-title">Konsisten Dipercaya Memimpin Proyek Nyata</h3>
        <p class="usp-feature-desc">
          Terbukti berulang kali dipercaya sebagai Project Officer tingkat nasional, Ketua Subdivisi, Koordinator Tim Studio, dan Founder inisiatif konsultasi. Mahir merumuskan Work Breakdown Structure (WBS), menyelaraskan dinamika tim multi-divisi, serta mengambil keputusan strategis di bawah tenggat waktu ketat.
        </p>

        <!-- Leadership Impact Counters (100+ Staf & Proyek Nyata) -->
        <div class="leadership-impact-bar" title="Rekam Jejak Kepemimpinan Mirza">
          <div class="impact-stat-item">
            <span class="impact-stat-num">100+</span>
            <span class="impact-stat-lbl">Staf & Panitia Dipimpin</span>
          </div>
          <div class="impact-stat-divider"></div>
          <div class="impact-stat-item">
            <span class="impact-stat-num">4+</span>
            <span class="impact-stat-lbl">Proyek Strategis Dipimpin</span>
          </div>
          <div class="impact-stat-divider"></div>
          <div class="impact-stat-item">
            <span class="impact-stat-num">110+</span>
            <span class="impact-stat-lbl">Karya Tim Terealisasi</span>
          </div>
        </div>

        <!-- Highlight Proyek Kepemimpinan Nyata -->
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
        </div>

        <div class="usp-feature-tags" style="margin-top:auto;padding-top:0.4rem;">
          <span class="usp-subtag">WBS & Action Plan</span>
          <span class="usp-subtag">Strategic Delegation</span>
          <span class="usp-subtag">Cross-functional Team</span>
        </div>"""

c_norm = c.replace('\r\n', '\n')
old_lead_norm = old_lead_card.replace('\r\n', '\n')
new_lead_norm = new_lead_card.replace('\r\n', '\n')

assert old_lead_norm in c_norm, "old_lead_card not found in templates/index.html"
c_norm = c_norm.replace(old_lead_norm, new_lead_norm, 1)

# 3. Update software chip for Adobe
c_norm = c_norm.replace(
    'data-output="INI LHO ITS 2026: Mengarahkan Produksi 110 Konten Video Edukasi & Motion Graphics"',
    'data-output="INI LHO ITS 2026: Saat menjadi Ketua Subdivisi Media Production, berhasil memimpin produksi 110 karya visual tim (84 motion graphics, 18 video visual editing, 8 siaran utama)."'
)

# 4. Update Card 3 active role description
c_norm = c_norm.replace(
    '<p>Memimpin perhelatan akbar nasional PWK ITS (koordinasi 8 divisi & 10 subdivisi).</p>',
    '<p>Pimpinan tertinggi perhelatan akbar nasional PWK ITS (memimpin 100+ panitia & staf lintas 8 divisi).</p>'
)

# 5. Update ST-01 in Timeline
c_norm = c_norm.replace(
    '<div class="timeline-role">Head of Media Production Subdivision</div>\n          <p class="timeline-desc">\n            Memimpin produksi 84 motion graphics, 18 visual editing, dan 8 proyek video (total 110 karya visual media) untuk menjangkau puluhan ribu calon mahasiswa baru ITS.\n          </p>\n          <div class="timeline-tags">\n            <span class="tag-transit-badge">Pimpinan Tim 110 Karya Media Visual</span>',
    '<div class="timeline-role">Ketua Subdivisi Media Production</div>\n          <p class="timeline-desc">\n            Saat menjadi Ketua Subdivisi Media Production, berhasil memimpin tim dalam memproduksi 84 motion graphics, 18 visual editing, dan 8 proyek video siaran (total 110 karya visual media) untuk menjangkau puluhan ribu calon mahasiswa baru ITS.\n          </p>\n          <div class="timeline-tags">\n            <span class="tag-transit-badge">Ketua Subdivisi Media</span>\n            <span class="tag-transit-badge">Memimpin 110 Karya Visual Tim</span>'
)

# 6. Update ST-04 in Timeline
c_norm = c_norm.replace(
    'Menyusun Grand Design operasional perhelatan akbar tahunan departemen, memimpin koordinasi lintas 8 divisi dan 10 subdivisi, serta menjamin eksekusi program berskala nasional berjalan presisi.',
    'Menyusun Grand Design operasional perhelatan akbar tahunan departemen, memimpin koordinasi lebih dari 100 panitia dan staf operasional lintas 8 divisi serta 10 subdivisi untuk menjamin eksekusi program berskala nasional berjalan presisi.'
)
c_norm = c_norm.replace(
    '<span class="tag-transit-badge">Ketua Pelaksana · Koordinasi 8 Divisi Tim</span>',
    '<span class="tag-transit-badge">Project Officer · Memimpin 100+ Panitia & Staf</span>'
)

with open('templates/index.html', 'w', encoding='utf-8') as f:
    f.write(c_norm)

print("SUCCESS: Updated templates/index.html with refined leadership and 110 works!")

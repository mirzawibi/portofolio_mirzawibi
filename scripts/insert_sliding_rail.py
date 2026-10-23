with open('templates/index.html', 'r', encoding='utf-8') as f:
    c = f.read()

target = '<div class="transit-metro-timeline reveal" id="metro-timeline-container">\n\n      <!-- Stasiun 1: INI LHO ITS 2026'

replacement = """<div class="transit-metro-timeline reveal" id="metro-timeline-container">

      <!-- Simple & High-Clarity Sliding Progress Rail System (Rombak Bersih & Jelas) -->
      <div class="metro-timeline-rail-system" aria-hidden="true">
        <div class="metro-rail-track-line">
          <div class="metro-rail-fill-bar" id="metro-progress-fill"></div>
          <div class="metro-sliding-capsule" id="metro-sliding-capsule" title="Indikator Kemajuan Scroll">
            <span class="capsule-core"></span>
            <span class="capsule-beacon"></span>
          </div>
        </div>
      </div>

      <!-- Stasiun 1: INI LHO ITS 2026"""

c_norm = c.replace('\r\n', '\n')
target_norm = target.replace('\r\n', '\n')
replacement_norm = replacement.replace('\r\n', '\n')

assert target_norm in c_norm, "target not found in templates/index.html"
c_norm = c_norm.replace(target_norm, replacement_norm, 1)

with open('templates/index.html', 'w', encoding='utf-8') as f:
    f.write(c_norm)

print("SUCCESS: Inserted high-clarity sliding rail system into templates/index.html")

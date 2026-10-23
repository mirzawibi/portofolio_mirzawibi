with open('templates/index.html', 'r', encoding='utf-8') as f:
    c = f.read()

target = """      <!-- Sleek Modern Transit Progress Spine (Clean & Interactive, No Railroad Clutter) -->
      <div class="timeline-clean-spine" id="timeline-clean-spine" aria-hidden="true">
        <div class="timeline-progress-fill" id="timeline-progress-fill"></div>
        <div class="timeline-sliding-indicator" id="timeline-sliding-indicator">
          <span class="scroller-pulse"></span>
          <span class="scroller-badge" id="train-dock-badge">ST-01</span>
        </div>
      </div>"""

replacement = """      <!-- Sleek Minimalist Sliding Progress Spine (Simple & Clean) -->
      <div class="timeline-clean-spine" id="timeline-clean-spine" aria-hidden="true">
        <div class="timeline-progress-fill" id="timeline-progress-fill"></div>
        <div class="timeline-sliding-indicator" id="timeline-sliding-indicator" title="Posisi Penelusuran">
          <span class="timeline-slider-dot"></span>
          <span class="timeline-slider-pulse"></span>
        </div>
      </div>"""

c_norm = c.replace('\r\n', '\n')
target_norm = target.replace('\r\n', '\n')
replacement_norm = replacement.replace('\r\n', '\n')

assert target_norm in c_norm, "Target sliding bar not found in templates/index.html"
c_norm = c_norm.replace(target_norm, replacement_norm, 1)

with open('templates/index.html', 'w', encoding='utf-8') as f:
    f.write(c_norm)

print("SUCCESS: Updated timeline sliding indicator in templates/index.html")

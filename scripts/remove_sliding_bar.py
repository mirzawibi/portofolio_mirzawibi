with open('templates/index.html', 'r', encoding='utf-8') as f:
    c = f.read()

# Remove the entire sliding bar block
old_spine_block = """      <!-- Sleek Minimalist Sliding Progress Spine (Simple & Clean) -->
      <div class="timeline-clean-spine" id="timeline-clean-spine" aria-hidden="true">
        <div class="timeline-progress-fill" id="timeline-progress-fill"></div>
        <div class="timeline-sliding-indicator" id="timeline-sliding-indicator" title="Posisi Penelusuran">
          <span class="timeline-slider-dot"></span>
          <span class="timeline-slider-pulse"></span>
        </div>
      </div>"""

c_norm = c.replace('\r\n', '\n')
old_spine_norm = old_spine_block.replace('\r\n', '\n')

if old_spine_norm in c_norm:
    c_norm = c_norm.replace(old_spine_norm, "", 1)
    print("SUCCESS: Removed sliding bar from templates/index.html")
else:
    print("WARNING: old_spine_norm not found directly, checking variations...")
    # Search for timeline-clean-spine
    start_idx = c_norm.find('<div class="timeline-clean-spine"')
    if start_idx != -1:
        end_idx = c_norm.find('</div>\n      </div>', start_idx)
        if end_idx != -1:
            end_idx += len('</div>\n      </div>')
            c_norm = c_norm[:start_idx] + c_norm[end_idx:]
            print("SUCCESS: Sliced out timeline-clean-spine block")

with open('templates/index.html', 'w', encoding='utf-8') as f:
    f.write(c_norm)

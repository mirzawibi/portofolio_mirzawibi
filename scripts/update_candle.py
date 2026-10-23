with open('templates/base.html', 'r', encoding='utf-8') as f:
    c = f.read()

target = """              <!-- 3D Organic Wax Drips running down sides -->
              <div class="wax-drip-flow drip-primary-left"></div>
              <div class="wax-drip-flow drip-secondary-left"></div>
              <div class="wax-drip-flow drip-main-center"></div>
              <div class="wax-drip-flow drip-primary-right"></div>
              <div class="wax-drip-flow drip-secondary-right"></div>
              
              <!-- Subsurface Scattering & Cylindrical Highlight -->
              <div class="wax-cylindrical-highlight"></div>
              <div class="wax-body-texture"></div>
            </div>

            <!-- Antique Cast Brass / Bronze Saucer Stand with Rim Reflection -->
            <div class="antique-brass-stand" aria-hidden="true">
              <div class="brass-saucer-rim"></div>
              <div class="brass-flame-reflection"></div>
              <div class="brass-pedestal-base"></div>
            </div>"""

replacement = """            </div>

            <!-- Minimalist Elegant Saucer Plate -->
            <div class="minimal-saucer-dish" aria-hidden="true"></div>"""

c_norm = c.replace('\r\n', '\n')
target_norm = target.replace('\r\n', '\n')
replacement_norm = replacement.replace('\r\n', '\n')

if target_norm in c_norm:
    c_norm = c_norm.replace(target_norm, replacement_norm, 1)
    with open('templates/base.html', 'w', encoding='utf-8') as f:
        f.write(c_norm)
    print("SUCCESS: Updated templates/base.html")
else:
    print("WARNING: target not found")

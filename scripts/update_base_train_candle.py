with open('templates/base.html', 'r', encoding='utf-8') as f:
    c = f.read()

# 1. Update MRT carriage SVG with multiple liveries & fine transit details
old_svg_chunk = """          <!-- Aerodynamic Train SVG with Illuminating Headlights & Warm Cabin Glow -->
          <svg class="mrt-train-svg" width="380" height="90" viewBox="0 0 380 90" fill="none">
            <defs>
              <linearGradient id="trainBodyGrad" x1="0" y1="0" x2="1" y2="0">
                <stop offset="0%" stop-color="#14211C" />
                <stop offset="40%" stop-color="#1B2C25" />
                <stop offset="80%" stop-color="#315C37" />
                <stop offset="100%" stop-color="#84A950" />
              </linearGradient>
              <linearGradient id="headlightBeam" x1="0" y1="0" x2="1" y2="0">
                <stop offset="0%" stop-color="rgba(254, 240, 138, 0.95)" />
                <stop offset="40%" stop-color="rgba(254, 240, 138, 0.45)" />
                <stop offset="100%" stop-color="rgba(254, 240, 138, 0)" />
              </linearGradient>
              <linearGradient id="speedStreak" x1="0" y1="0" x2="1" y2="0">
                <stop offset="0%" stop-color="rgba(132, 169, 80, 0)" />
                <stop offset="100%" stop-color="rgba(132, 169, 80, 0.7)" />
              </linearGradient>
            </defs>

            <!-- Light Stream Speed Trails behind Train -->
            <path d="M0 32 L40 32" stroke="url(#speedStreak)" stroke-width="2" stroke-dasharray="4 4" />
            <path d="M5 45 L50 45" stroke="url(#speedStreak)" stroke-width="3" stroke-dasharray="6 3" />
            <path d="M10 58 L55 58" stroke="url(#speedStreak)" stroke-width="2" stroke-dasharray="5 5" />

            <!-- Long Headlight Beam Cone illuminating the track ahead -->
            <polygon points="350,48 480,18 480,78 350,56" fill="url(#headlightBeam)" />

            <!-- Main Locomotive Body (Sleek Bullet Nose) -->
            <path d="M30 58 L42 22 C45 15 52 11 62 11 L310 11 C338 11 358 24 368 44 L372 56 C372 63 368 67 360 67 L42 67 C35 67 30 63 30 58 Z" fill="url(#trainBodyGrad)" stroke="#A7C66A" stroke-width="2"/>
            
            <!-- Roof Fairing / Pantograph Base -->
            <rect x="90" y="7" width="180" height="4" rx="2" fill="#284036" />
            <path d="M150 7 L165 1 L185 1 L200 7" stroke="#A7C66A" stroke-width="1.5" fill="none" />

            <!-- Streamline Orange Brand Accent Stripe -->
            <path d="M48 42 L338 42 C348 42 358 47 362 53 L366 59 L35 59 L48 42 Z" fill="#D97736" opacity="0.95" />

            <!-- Windows with Warm Passenger Cabin Glow -->
            <rect x="65" y="22" width="42" height="15" rx="3" fill="#0F172A" stroke="#84A950" stroke-width="1.2"/>
            <rect x="115" y="22" width="52" height="15" rx="3" fill="#0F172A" stroke="#84A950" stroke-width="1.2"/>
            <rect x="175" y="22" width="52" height="15" rx="3" fill="#0F172A" stroke="#84A950" stroke-width="1.2"/>
            <rect x="235" y="22" width="52" height="15" rx="3" fill="#0F172A" stroke="#84A950" stroke-width="1.2"/>
            
            <!-- Panoramic Aerodynamic Driver Windshield -->
            <path d="M298 22 L338 22 C348 26 355 33 359 40 L298 40 Z" fill="#0B1310" stroke="#A7C66A" stroke-width="1.5"/>

            <!-- High-Intensity LED Headlights -->
            <circle cx="362" cy="50" r="4" fill="#FEF08A"/>
            <circle cx="362" cy="50" r="8" fill="rgba(254, 240, 138, 0.45)"/>

            <!-- Bogies & Wheels -->
            <rect x="68" y="67" width="62" height="6" rx="2" fill="#0E1713" />
            <circle cx="82" cy="74" r="5.5" fill="#1B2C25" stroke="#9BB0A3" stroke-width="1.5"/>
            <circle cx="116" cy="74" r="5.5" fill="#1B2C25" stroke="#9BB0A3" stroke-width="1.5"/>
            <rect x="252" y="67" width="62" height="6" rx="2" fill="#0E1713" />
            <circle cx="266" cy="74" r="5.5" fill="#1B2C25" stroke="#9BB0A3" stroke-width="1.5"/>
            <circle cx="300" cy="74" r="5.5" fill="#1B2C25" stroke="#9BB0A3" stroke-width="1.5"/>
          </svg>"""

new_svg_chunk = """          <!-- High-Detail Multi-Livery Commuter / MRT / LRT Train SVG -->
          <svg class="mrt-train-svg" width="380" height="90" viewBox="0 0 380 90" fill="none">
            <defs>
              <!-- Model 1: KRL Commuter Emerald & Gold -->
              <linearGradient id="trainBodyGradKRL" x1="0" y1="0" x2="1" y2="0">
                <stop offset="0%" stop-color="#14211C" />
                <stop offset="35%" stop-color="#1B2C25" />
                <stop offset="75%" stop-color="#315C37" />
                <stop offset="100%" stop-color="#84A950" />
              </linearGradient>
              <!-- Model 2: MRT Metro Navy & Sapphire Blue -->
              <linearGradient id="trainBodyGradMetro" x1="0" y1="0" x2="1" y2="0">
                <stop offset="0%" stop-color="#0B132B" />
                <stop offset="35%" stop-color="#1C2541" />
                <stop offset="75%" stop-color="#1E3E62" />
                <stop offset="100%" stop-color="#0284C7" />
              </linearGradient>
              <!-- Model 3: LRT Rapid Crimson & Platinum -->
              <linearGradient id="trainBodyGradLRT" x1="0" y1="0" x2="1" y2="0">
                <stop offset="0%" stop-color="#3A0808" />
                <stop offset="35%" stop-color="#7F1D1D" />
                <stop offset="75%" stop-color="#B91C1C" />
                <stop offset="100%" stop-color="#EF4444" />
              </linearGradient>
              <linearGradient id="headlightBeam" x1="0" y1="0" x2="1" y2="0">
                <stop offset="0%" stop-color="rgba(254, 240, 138, 0.95)" />
                <stop offset="40%" stop-color="rgba(254, 240, 138, 0.45)" />
                <stop offset="100%" stop-color="rgba(254, 240, 138, 0)" />
              </linearGradient>
              <linearGradient id="speedStreak" x1="0" y1="0" x2="1" y2="0">
                <stop offset="0%" stop-color="rgba(132, 169, 80, 0)" />
                <stop offset="100%" stop-color="rgba(132, 169, 80, 0.85)" />
              </linearGradient>
            </defs>

            <!-- Light Stream Speed Trails behind Train -->
            <path d="M0 30 L45 30" stroke="url(#speedStreak)" stroke-width="2.5" stroke-dasharray="5 4" />
            <path d="M4 44 L55 44" stroke="url(#speedStreak)" stroke-width="3.5" stroke-dasharray="7 3" />
            <path d="M8 58 L60 58" stroke="url(#speedStreak)" stroke-width="2.5" stroke-dasharray="6 4" />

            <!-- Long Headlight Beam Cone illuminating the track ahead -->
            <polygon points="350,48 480,18 480,78 350,56" fill="url(#headlightBeam)" />

            <!-- Main Locomotive Body (Sleek Bullet Nose) with dynamic fill class -->
            <path id="svg-train-body" class="mrt-body-shape" d="M30 58 L42 22 C45 15 52 11 62 11 L310 11 C338 11 358 24 368 44 L372 56 C372 63 368 67 360 67 L42 67 C35 67 30 63 30 58 Z" fill="url(#trainBodyGradKRL)" stroke="#A7C66A" stroke-width="2"/>
            
            <!-- Roof Fairing & Detailed High-Voltage Pantograph -->
            <rect x="90" y="7" width="180" height="4" rx="2" fill="#284036" />
            <path d="M145 7 L162 1 L182 1 L198 7" stroke="#A7C66A" stroke-width="1.8" fill="none" />
            <circle cx="172" cy="1" r="2.2" fill="#FEF08A" opacity="0.9" />

            <!-- Dynamic Streamline Brand Accent Stripe -->
            <path id="svg-train-stripe" d="M48 42 L338 42 C348 42 358 47 362 53 L366 59 L35 59 L48 42 Z" fill="#D97736" opacity="0.95" />

            <!-- Locomotive Fleet Call-Sign Number -->
            <rect x="74" y="44" width="46" height="11" rx="2" fill="#0B1310" stroke="rgba(255,255,255,0.2)" stroke-width="0.8" />
            <text x="97" y="52.5" fill="#FEF08A" font-size="7.5" font-family="monospace" font-weight="800" text-anchor="middle" id="mrt-loco-callsign">KA-2026</text>

            <!-- Passenger Cabin Windows with Ambient Lighting -->
            <rect x="130" y="22" width="48" height="15" rx="3" fill="#0F172A" stroke="#84A950" stroke-width="1.2"/>
            <rect x="188" y="22" width="48" height="15" rx="3" fill="#0F172A" stroke="#84A950" stroke-width="1.2"/>
            <rect x="246" y="22" width="48" height="15" rx="3" fill="#0F172A" stroke="#84A950" stroke-width="1.2"/>
            
            <!-- Panoramic Aerodynamic Driver Windshield with Wiper -->
            <path d="M304 22 L342 22 C350 26 357 33 361 40 L304 40 Z" fill="#0B1310" stroke="#A7C66A" stroke-width="1.5"/>
            <line x1="322" y1="36" x2="336" y2="28" stroke="#FEF08A" stroke-width="1.2" opacity="0.85" />

            <!-- High-Intensity LED Headlights with Optical Corona Flare -->
            <circle cx="362" cy="50" r="4" fill="#FEF08A"/>
            <circle cx="362" cy="50" r="9" fill="rgba(254, 240, 138, 0.5)"/>
            <circle cx="362" cy="50" r="14" fill="rgba(254, 240, 138, 0.2)"/>

            <!-- Heavy Bogies, Suspension Springs & Steel Wheels -->
            <rect x="68" y="67" width="62" height="6" rx="2" fill="#0E1713" />
            <circle cx="82" cy="74" r="5.8" fill="#1B2C25" stroke="#9BB0A3" stroke-width="1.6"/>
            <circle cx="82" cy="74" r="2.2" fill="#D97736" />
            <circle cx="116" cy="74" r="5.8" fill="#1B2C25" stroke="#9BB0A3" stroke-width="1.6"/>
            <circle cx="116" cy="74" r="2.2" fill="#D97736" />
            <rect x="252" y="67" width="62" height="6" rx="2" fill="#0E1713" />
            <circle cx="266" cy="74" r="5.8" fill="#1B2C25" stroke="#9BB0A3" stroke-width="1.6"/>
            <circle cx="266" cy="74" r="2.2" fill="#D97736" />
            <circle cx="300" cy="74" r="5.8" fill="#1B2C25" stroke="#9BB0A3" stroke-width="1.6"/>
            <circle cx="300" cy="74" r="2.2" fill="#D97736" />
          </svg>"""

c_norm = c.replace('\r\n', '\n')
old_svg_norm = old_svg_chunk.replace('\r\n', '\n')
new_svg_norm = new_svg_chunk.replace('\r\n', '\n')

assert old_svg_norm in c_norm, "old_svg_chunk not found in templates/base.html"
c_norm = c_norm.replace(old_svg_norm, new_svg_norm, 1)

# 2. Update Candle hint in base.html
old_candle_msg = """          <!-- Deep Golden Revelation Message Badge -->
          <div class="candle-revelation-message" id="candle-revelation-message">
            <span class="rev-spark">✦</span>
            <span class="rev-text">“Kita hidup karena kita bermanfaat.”</span>
            <span class="rev-spark">✦</span>
          </div>"""

new_candle_msg = """          <!-- Deep Golden Revelation Message Badge (Muncul saat mouse di-hover) -->
          <div class="candle-revelation-message" id="candle-revelation-message">
            <span class="rev-spark">✦</span>
            <span class="rev-text">“Kita hidup karena kita bermanfaat.”</span>
            <span class="rev-spark">✦</span>
          </div>
          <div class="candle-hover-hint" id="candle-hover-hint" aria-hidden="true">
            <span class="hint-pulse"></span> Dekatkan kursor untuk menyalakan lentera
          </div>"""

old_candle_norm = old_candle_msg.replace('\r\n', '\n')
new_candle_norm = new_candle_msg.replace('\r\n', '\n')

assert old_candle_norm in c_norm, "old_candle_msg not found in templates/base.html"
c_norm = c_norm.replace(old_candle_norm, new_candle_norm, 1)

with open('templates/base.html', 'w', encoding='utf-8') as f:
    f.write(c_norm)

print("SUCCESS: Updated templates/base.html with multi-livery train SVG and hover hint!")

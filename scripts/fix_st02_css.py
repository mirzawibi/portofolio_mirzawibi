with open('static/css/main.css', 'r', encoding='utf-8') as f:
    css = f.read()

# Fix 1: Line 388 badge-transit -> .badge.badge-transit
old_388 = """.badge-transit {
  background-color: rgba(167, 198, 106, 0.18);
  color: var(--color-accent-path-light);
  border: 1px solid rgba(167, 198, 106, 0.35);
}"""

new_388 = """.badge.badge-transit {
  background-color: rgba(167, 198, 106, 0.18);
  color: var(--color-accent-path-light);
  border: 1px solid rgba(167, 198, 106, 0.35);
}"""

assert old_388 in css, "old_388 not found"
css = css.replace(old_388, new_388, 1)

# Fix 2: Line 6247 badge-transit -> .badge.badge-transit, .cv-badge.badge-transit
old_6247 = """.badge-transit {
  background: rgba(49, 92, 55, 0.09) !important;
  color: var(--color-primary) !important;
  border: 1px solid rgba(49, 92, 55, 0.22) !important;
  font-size: 0.72rem;
  font-weight: 600;
  padding: 0.2rem 0.55rem;
  border-radius: var(--radius-full);
  display: inline-flex;
  align-items: center;
  gap: 0.3rem;
  white-space: nowrap;
}"""

new_6247 = """.badge.badge-transit,
.cv-badge.badge-transit {
  background: rgba(49, 92, 55, 0.09) !important;
  color: var(--color-primary) !important;
  border: 1px solid rgba(49, 92, 55, 0.22) !important;
  font-size: 0.72rem;
  font-weight: 600;
  padding: 0.2rem 0.55rem;
  border-radius: var(--radius-full);
  display: inline-flex;
  align-items: center;
  gap: 0.3rem;
  white-space: nowrap;
}"""

assert old_6247 in css, "old_6247 not found"
css = css.replace(old_6247, new_6247, 1)

# Fix 3: Bulletproof metro-badge-core styles around line 3954
old_badges = """.badge-leadership { border-color: #84A950; }
.badge-spatial { border-color: #2F6F9E; box-shadow: 0 6px 20px rgba(0,0,0,0.7), 0 0 15px rgba(47, 111, 158, 0.4); }
.badge-consulting { border-color: #D97736; box-shadow: 0 6px 20px rgba(0,0,0,0.7), 0 0 15px rgba(217, 119, 54, 0.4); }
.badge-transit { border-color: #A7C66A; }
.badge-media { border-color: #E11D48; box-shadow: 0 6px 20px rgba(0,0,0,0.7), 0 0 15px rgba(225, 29, 72, 0.4); }"""

new_badges = """.metro-badge-core {
  width: 52px !important;
  height: 52px !important;
  min-width: 52px !important;
  min-height: 52px !important;
  max-width: 52px !important;
  max-height: 52px !important;
  border-radius: 50% !important;
  background: #0E1713 !important;
  border: 3px solid #84A950 !important;
  box-shadow: 0 6px 20px rgba(0, 0, 0, 0.7), 0 0 15px rgba(132, 169, 80, 0.4) !important;
  display: flex !important;
  flex-direction: column !important;
  align-items: center !important;
  justify-content: center !important;
  padding: 0 !important;
  margin: 0 !important;
  box-sizing: border-box !important;
  transition: transform 0.25s ease, box-shadow 0.25s ease, border-color 0.25s ease !important;
}

.metro-badge-core .station-code-pill {
  font-family: var(--font-mono) !important;
  font-size: 0.68rem !important;
  font-weight: 800 !important;
  color: #FEF08A !important;
  line-height: 1 !important;
  text-align: center !important;
  display: block !important;
  padding: 0 !important;
  margin: 0 !important;
  background: transparent !important;
  border: none !important;
}

.metro-badge-core.badge-transit,
.metro-badge-core.badge-metro-transit {
  border-color: #A7C66A !important;
  box-shadow: 0 6px 20px rgba(0, 0, 0, 0.7), 0 0 15px rgba(167, 198, 106, 0.45) !important;
  background: #0E1713 !important;
}
.metro-badge-core.badge-media,
.metro-badge-core.badge-metro-media {
  border-color: #E11D48 !important;
  box-shadow: 0 6px 20px rgba(0, 0, 0, 0.7), 0 0 15px rgba(225, 29, 72, 0.45) !important;
  background: #0E1713 !important;
}
.metro-badge-core.badge-spatial,
.metro-badge-core.badge-metro-spatial {
  border-color: #2F6F9E !important;
  box-shadow: 0 6px 20px rgba(0, 0, 0, 0.7), 0 0 15px rgba(47, 111, 158, 0.45) !important;
  background: #0E1713 !important;
}
.metro-badge-core.badge-leadership,
.metro-badge-core.badge-metro-leadership {
  border-color: #84A950 !important;
  box-shadow: 0 6px 20px rgba(0, 0, 0, 0.7), 0 0 15px rgba(132, 169, 80, 0.45) !important;
  background: #0E1713 !important;
}
.metro-badge-core.badge-consulting,
.metro-badge-core.badge-metro-consulting {
  border-color: #D97736 !important;
  box-shadow: 0 6px 20px rgba(0, 0, 0, 0.7), 0 0 15px rgba(217, 119, 54, 0.45) !important;
  background: #0E1713 !important;
}"""

assert old_badges in css, "old_badges not found"
css = css.replace(old_badges, new_badges, 1)

with open('static/css/main.css', 'w', encoding='utf-8') as f:
    f.write(css)

print("SUCCESS: static/css/main.css updated cleanly!")

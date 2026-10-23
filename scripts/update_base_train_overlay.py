with open('templates/base.html', 'r', encoding='utf-8') as f:
    c = f.read()

# 1. Update SVG dimensions & viewBox to prevent any top clipping
old_svg_tag = '<svg class="mrt-train-svg" width="380" height="90" viewBox="0 0 380 90" fill="none">'
new_svg_tag = '<svg class="mrt-train-svg" width="440" height="115" viewBox="0 -18 440 115" fill="none">'

assert old_svg_tag in c, "old_svg_tag not found in base.html"
c = c.replace(old_svg_tag, new_svg_tag, 1)

# 2. Expand headlight cone for full-screen illumination effect
old_cone = '<polygon points="350,48 480,18 480,78 350,56" fill="url(#headlightBeam)" />'
new_cone = '<polygon points="362,50 780,5 780,95 362,56" fill="url(#headlightBeam)" />'

assert old_cone in c, "old_cone not found in base.html"
c = c.replace(old_cone, new_cone, 1)

# 3. Add speed tunnel atmosphere right before track line
old_track = '<div class="transit-track-line">'
new_track = """<!-- Atmospheric High-Speed Glow Beam -->
      <div class="transit-speed-tunnel" aria-hidden="true"></div>
      <div class="transit-track-line">"""

assert old_track in c, "old_track not found in base.html"
c = c.replace(old_track, new_track, 1)

with open('templates/base.html', 'w', encoding='utf-8') as f:
    f.write(c)

print("SUCCESS: Updated templates/base.html with unclipped train viewBox and full-screen speed tunnel!")

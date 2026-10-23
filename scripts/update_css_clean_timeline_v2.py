with open('static/css/main.css', 'r', encoding='utf-8') as f:
    css = f.read()

# 1. Update line 4349 candle rule
old_candle_block = """.candle-revelation-message {
  margin-top: 1.25rem;
  background: rgba(14, 23, 19, 0.95);
  border: 1.5px solid #FEF08A;
  border-radius: var(--radius-full);
  padding: 0.5rem 1.4rem;
  font-size: 0.925rem;
  font-weight: 800;
  color: #FEF08A;
  box-shadow: 0 8px 28px rgba(0, 0, 0, 0.7), 0 0 20px rgba(254, 240, 138, 0.35);
  display: flex;
  align-items: center;
  gap: 0.5rem;
  opacity: 0.85;
  transform: translateY(0);
  transition: all 0.3s ease;
  z-index: 5;
}
.grand-candle-interactive-zone:hover .candle-revelation-message {
  opacity: 1;
  transform: translateY(-4px) scale(1.04);
  border-color: #FFFFFF;
  box-shadow: 0 12px 35px rgba(0, 0, 0, 0.9), 0 0 30px rgba(254, 240, 138, 0.6);
}"""

new_candle_block = """.candle-revelation-message {
  margin-top: 1.25rem;
  background: rgba(14, 23, 19, 0.95);
  border: 1.5px solid #FEF08A;
  border-radius: var(--radius-full);
  padding: 0.5rem 1.4rem;
  font-size: 0.925rem;
  font-weight: 800;
  color: #FEF08A;
  box-shadow: 0 8px 28px rgba(0, 0, 0, 0.7), 0 0 20px rgba(254, 240, 138, 0.35);
  display: flex;
  align-items: center;
  gap: 0.5rem;
  opacity: 0 !important;
  visibility: hidden !important;
  pointer-events: none !important;
  transform: translateY(14px) scale(0.95) !important;
  transition: opacity 0.35s ease, transform 0.35s cubic-bezier(0.34, 1.56, 0.64, 1), visibility 0.35s !important;
  z-index: 5;
}
.grand-candle-interactive-zone:hover .candle-revelation-message,
.grand-candle-interactive-zone:focus-within .candle-revelation-message,
.grand-candle-interactive-zone.active .candle-revelation-message,
.grand-candle-interactive-zone.candle-revealed .candle-revelation-message {
  opacity: 1 !important;
  visibility: visible !important;
  pointer-events: auto !important;
  transform: translateY(0) scale(1) !important;
  border-color: #FFFFFF !important;
  box-shadow: 0 12px 35px rgba(0, 0, 0, 0.9), 0 0 30px rgba(254, 240, 138, 0.6) !important;
}"""

css_norm = css.replace('\r\n', '\n')
old_cd_norm = old_candle_block.replace('\r\n', '\n')
new_cd_norm = new_candle_block.replace('\r\n', '\n')

if old_cd_norm in css_norm:
    css_norm = css_norm.replace(old_cd_norm, new_cd_norm, 1)
    print("SUCCESS: Replaced old candle block at line 4349")

# 2. Slice out the old timeline rail spine and replace with clean line
start_marker = "/* 6. Metro Interchange Rail Spine Sidebar (Request 4: Eksperimen Jalur Transit) */"
end_marker = "transition: transform 0.12s cubic-bezier(0.2, 0.8, 0.2, 1);\n}"

start_pos = css_norm.find(start_marker)
end_pos = css_norm.find(end_marker, start_pos)

if start_pos != -1 and end_pos != -1:
    end_pos += len(end_marker)
    clean_tl = """/* --- Clean Modern Timeline Spine (Clean, Simple & Pristine) --- */
.transit-metro-timeline {
  position: relative;
  padding-left: 90px;
  margin: 3rem 0;
}
.transit-metro-timeline::before {
  content: "";
  position: absolute;
  left: 42px;
  top: 36px;
  bottom: 50px;
  width: 2.5px;
  background: linear-gradient(180deg, #D97736 0%, #84A950 25%, #2F6F9E 50%, #84A950 75%, #315C37 100%);
  border-radius: 999px;
  opacity: 0.55;
  z-index: 1;
}"""
    css_norm = css_norm[:start_pos] + clean_tl + css_norm[end_pos:]
    print("SUCCESS: Replaced timeline rail spine block with clean modern spine")
else:
    print(f"DEBUG: start_pos={start_pos}, end_pos={end_pos}")

with open('static/css/main.css', 'w', encoding='utf-8') as f:
    f.write(css_norm)

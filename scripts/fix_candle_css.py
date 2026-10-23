# Update static/css/main.css
with open('static/css/main.css', 'r', encoding='utf-8') as f:
    css = f.read()

# 1. Clean the primary candle revelation block
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

new_candle_block = """.candle-revelation-message {
  margin-top: 1.25rem;
  background: rgba(14, 23, 19, 0.96);
  border: 1.5px solid #FEF08A;
  border-radius: var(--radius-full);
  padding: 0.55rem 1.4rem;
  font-size: 0.925rem;
  font-weight: 800;
  color: #FEF08A;
  box-shadow: 0 8px 28px rgba(0, 0, 0, 0.7), 0 0 20px rgba(254, 240, 138, 0.35);
  display: flex;
  align-items: center;
  gap: 0.5rem;
  opacity: 0;
  pointer-events: none;
  transform: translateY(14px) scale(0.95);
  transition: opacity 0.28s ease, transform 0.28s ease;
  z-index: 10;
}
.grand-candle-interactive-zone:hover .candle-revelation-message,
.grand-candle-interactive-zone:focus-within .candle-revelation-message,
.grand-candle-interactive-zone.active .candle-revelation-message,
.grand-candle-interactive-zone.candle-revealed .candle-revelation-message {
  opacity: 1 !important;
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

# 2. Remove the second duplicate block at end of css
duplicate_block = """/* --- Candle Revelation on Hover Only (User Request 5) --- */
.candle-revelation-message {
  opacity: 0 !important;
  transform: translateY(14px) scale(0.96) !important;
  pointer-events: none !important;
  transition: opacity 0.35s ease, transform 0.35s cubic-bezier(0.34, 1.56, 0.64, 1), box-shadow 0.35s ease !important;
}
.grand-candle-interactive-zone:hover .candle-revelation-message,
.grand-candle-interactive-zone:focus-within .candle-revelation-message,
.grand-candle-interactive-zone.active .candle-revelation-message {
  opacity: 1 !important;
  transform: translateY(0) scale(1) !important;
  pointer-events: auto !important;
  border-color: #FFFFFF !important;
  box-shadow: 0 12px 35px rgba(0, 0, 0, 0.9), 0 0 30px rgba(254, 240, 138, 0.6) !important;
}"""

dup_norm = duplicate_block.replace('\r\n', '\n')
if dup_norm in css_norm:
    css_norm = css_norm.replace(dup_norm, "/* Candle revelation consolidated above */", 1)

with open('static/css/main.css', 'w', encoding='utf-8') as f:
    f.write(css_norm)

print("SUCCESS: Updated static/css/main.css candle revelation styling!")

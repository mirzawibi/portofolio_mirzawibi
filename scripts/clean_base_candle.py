with open('templates/base.html', 'r', encoding='utf-8') as f:
    c = f.read()

old_str = '<div class="candle-revelation-message" id="candle-revelation-message" style="opacity:0;visibility:hidden;pointer-events:none;">'
new_str = '<div class="candle-revelation-message" id="candle-revelation-message">'

assert old_str in c, "old_str not found in base.html"
c = c.replace(old_str, new_str, 1)

with open('templates/base.html', 'w', encoding='utf-8') as f:
    f.write(c)

print("SUCCESS: Cleaned candle element in templates/base.html")

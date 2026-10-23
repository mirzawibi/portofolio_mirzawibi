with open('templates/base.html', 'r', encoding='utf-8') as f:
    c = f.read()

old_msg = '<div class="candle-revelation-message" id="candle-revelation-message">'
new_msg = '<div class="candle-revelation-message" id="candle-revelation-message" style="opacity:0;visibility:hidden;pointer-events:none;">'

assert old_msg in c, "old_msg not found in base.html"
c = c.replace(old_msg, new_msg, 1)

with open('templates/base.html', 'w', encoding='utf-8') as f:
    f.write(c)

print("SUCCESS: Added explicit inline hidden style to candle message in templates/base.html")

with open('templates/karya_detail.html', 'r', encoding='utf-8') as f:
    h = f.read()

import re
matches = [line.strip() for line in h.splitlines() if 'source_pages' in line or 'slide' in line or 'svg' in line or 'image' in line or 'gallery' in line]
for m in matches:
    print(m)

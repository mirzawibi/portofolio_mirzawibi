with open('scripts/init_data.py', 'r', encoding='utf-8') as f:
    code = f.read()

import re
matches = re.findall(r'"slug":\s*"([^"]+)".*?"scenarios":\s*(\[[^\]]+\])', code, re.DOTALL)
for slug, sc in matches:
    print(f"=== {slug} ===")
    print(sc)

with open('templates/index.html', 'rb') as f:
    raw = f.read()

import re
matches = re.findall(b'data-station="st-0[0-9]".*?</span>', raw, re.DOTALL)
for i, m in enumerate(matches):
    print(f"Station {i+1}:", m[:120])

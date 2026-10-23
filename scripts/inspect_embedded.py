import os
import re
import base64
from io import BytesIO
from PIL import Image

output_dir = "scripts/extracted_sample"
os.makedirs(output_dir, exist_ok=True)

for i in [1, 2, 6, 7, 10, 11, 17, 18, 19, 20]:
    svg_path = f"Portofolio/{i}.svg"
    if not os.path.exists(svg_path):
        continue
    with open(svg_path, "r", encoding="utf-8", errors="ignore") as f:
        content = f.read()
    
    matches = re.findall(r'<image[^>]+xlink:href="data:image/([a-zA-Z]+);base64,([^"]+)"', content)
    print(f"\n{i}.svg has {len(matches)} embedded images")
    for idx, (fmt, b64) in enumerate(matches[:4]):
        raw = base64.b64decode(b64)
        try:
            im = Image.open(BytesIO(raw))
            print(f"  Img #{idx+1}: format={im.format}, size={im.size}, raw_bytes={len(raw)}")
            if i in [1, 17, 18] and idx < 2:
                sample_file = os.path.join(output_dir, f"slide_{i}_img_{idx+1}.jpg")
                im.convert("RGB").save(sample_file, "JPEG", quality=85)
                print(f"    Saved sample to {sample_file}")
        except Exception as e:
            print(f"  Img #{idx+1}: error {e}")

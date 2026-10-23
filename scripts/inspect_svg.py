import os
import re

svg_dir = 'Portofolio'
files = sorted([f for f in os.listdir(svg_dir) if f.endswith('.svg')], key=lambda x: int(x.split('.')[0]))

for f in files:
    path = os.path.join(svg_dir, f)
    with open(path, 'r', encoding='utf-8', errors='ignore') as fp:
        content = fp.read()
    
    # find images
    imgs = re.findall(r'<image[^>]+width="([^"]+)"[^>]+height="([^"]+)"', content)
    data_imgs = re.findall(r'data:image/([a-zA-Z]+);base64,', content)
    print(f"{f}: {len(data_imgs)} data images, sample dimensions: {imgs[:3]}")

import os
import subprocess
import time
from PIL import Image

svg_dir = "Portofolio"
out_dir = "static/assets/slides"
os.makedirs(out_dir, exist_ok=True)

edge = r"C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe"
temp_png = os.path.abspath("scripts/temp_render.png")

print("Starting render of 25 slides...")
start_time = time.time()

for i in range(1, 26):
    svg_file = os.path.join(svg_dir, f"{i}.svg")
    if not os.path.exists(svg_file):
        print(f"Skipping {svg_file} (not found)")
        continue
    
    large_webp = os.path.join(out_dir, f"slide_{i}_large.webp")
    normal_webp = os.path.join(out_dir, f"slide_{i}.webp")
    thumb_webp = os.path.join(out_dir, f"slide_{i}_thumb.webp")
    
    if os.path.exists(normal_webp) and os.path.exists(thumb_webp) and os.path.exists(large_webp):
        print(f"Slide {i} already rendered, skipping.")
        continue
    
    if os.path.exists(temp_png):
        os.remove(temp_png)
        
    cmd = [
        edge,
        "--headless",
        "--disable-gpu",
        "--no-sandbox",
        f"--screenshot={temp_png}",
        "--window-size=1920,1080",
        "file:///" + os.path.abspath(svg_file).replace("\\", "/")
    ]
    
    res = subprocess.run(cmd, capture_output=True, text=True, timeout=30)
    if not os.path.exists(temp_png):
        print(f"Failed to render slide {i}: {res.stderr[:200]}")
        continue
    
    with Image.open(temp_png) as im:
        # 1. Large WebP (1920x1080, quality 88)
        im.save(large_webp, "WEBP", quality=88)
        
        # 2. Normal WebP (1440x810, quality 84)
        norm = im.copy()
        norm.thumbnail((1440, 810), Image.Resampling.LANCZOS)
        norm.save(normal_webp, "WEBP", quality=84)
        
        # 3. Thumb WebP (800x450, quality 80)
        thumb = im.copy()
        thumb.thumbnail((800, 450), Image.Resampling.LANCZOS)
        thumb.save(thumb_webp, "WEBP", quality=80)
        
    print(f"Slide {i}/25 rendered successfully. (Large: {os.path.getsize(large_webp)//1024}KB, Norm: {os.path.getsize(normal_webp)//1024}KB, Thumb: {os.path.getsize(thumb_webp)//1024}KB)")

if os.path.exists(temp_png):
    os.remove(temp_png)

print(f"Finished rendering all slides in {time.time() - start_time:.1f}s")

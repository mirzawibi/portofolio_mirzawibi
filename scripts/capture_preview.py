import subprocess
import os
import time

edge_path = r"C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe"
artifact_dir = r"C:\Users\User\.gemini\antigravity\brain\5dfb1928-4f07-46b8-84bd-e62d15786eb5"
os.makedirs(artifact_dir, exist_ok=True)

targets = [
    ("http://127.0.0.1:8000/", os.path.join(artifact_dir, "preview_dark_urban_home.png")),
    ("http://127.0.0.1:8000/karya", os.path.join(artifact_dir, "preview_dark_urban_karya.png")),
    ("http://127.0.0.1:8000/cv", os.path.join(artifact_dir, "preview_dark_urban_cv.png")),
    ("http://127.0.0.1:8000/karya/perencanaan-transportasi-wonokromo", os.path.join(artifact_dir, "preview_dark_urban_wonokromo.png"))
]

for url, out_path in targets:
    print(f"Capturing {url} -> {out_path} ...")
    cmd = [
        edge_path,
        "--headless=new",
        "--disable-gpu",
        "--hide-scrollbars",
        "--window-size=1280,1400",
        f"--screenshot={out_path}",
        url
    ]
    subprocess.run(cmd, check=True)
    time.sleep(1)

print("All screenshots captured successfully!")

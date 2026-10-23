import subprocess
import os

edge_path = r"C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe"
artifact_dir = r"C:\Users\User\.gemini\antigravity\brain\5dfb1928-4f07-46b8-84bd-e62d15786eb5"

targets = [
    ("http://127.0.0.1:8000/#karya", os.path.join(artifact_dir, "preview_dark_urban_bento.png")),
    ("http://127.0.0.1:8000/#atlas", os.path.join(artifact_dir, "preview_dark_urban_atlas.png")),
    ("http://127.0.0.1:8000/#kontak", os.path.join(artifact_dir, "preview_dark_urban_footer.png"))
]

for url, out_path in targets:
    cmd = [
        edge_path,
        "--headless=new",
        "--disable-gpu",
        "--hide-scrollbars",
        "--window-size=1280,1200",
        f"--screenshot={out_path}",
        url
    ]
    subprocess.run(cmd, check=True)

print("Section screenshots captured!")

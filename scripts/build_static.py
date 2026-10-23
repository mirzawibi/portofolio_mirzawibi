import sys, os
sys.path.insert(0, os.path.abspath("."))

from fastapi.testclient import TestClient
from main import app, load_content
import shutil

client = TestClient(app)
content = load_content()

out_dir = "docs"
if os.path.exists(out_dir):
    shutil.rmtree(out_dir)
os.makedirs(out_dir, exist_ok=True)

# 1. Generate / -> docs/index.html
r = client.get("/")
assert r.status_code == 200
with open(os.path.join(out_dir, "index.html"), "w", encoding="utf-8") as f:
    f.write(r.text)
print("Generated index.html (size:", len(r.text), ")")

# 2. Generate /karya -> docs/karya/index.html
os.makedirs(os.path.join(out_dir, "karya"), exist_ok=True)
r_karya = client.get("/karya")
assert r_karya.status_code == 200
with open(os.path.join(out_dir, "karya", "index.html"), "w", encoding="utf-8") as f:
    f.write(r_karya.text)
print("Generated karya/index.html (size:", len(r_karya.text), ")")

# 3. Generate /cv -> docs/cv/index.html
os.makedirs(os.path.join(out_dir, "cv"), exist_ok=True)
r_cv = client.get("/cv")
assert r_cv.status_code == 200
with open(os.path.join(out_dir, "cv", "index.html"), "w", encoding="utf-8") as f:
    f.write(r_cv.text)
print("Generated cv/index.html (size:", len(r_cv.text), ")")

# 4. Generate all project pages /karya/{slug} -> docs/karya/{slug}/index.html
for p in content["projects"]:
    slug = p["slug"]
    p_dir = os.path.join(out_dir, "karya", slug)
    os.makedirs(p_dir, exist_ok=True)
    r_p = client.get(f"/karya/{slug}")
    assert r_p.status_code == 200
    with open(os.path.join(p_dir, "index.html"), "w", encoding="utf-8") as f:
        f.write(r_p.text)
    print(f"Generated karya/{slug}/index.html (size: {len(r_p.text)})")

# 5. Copy static assets
shutil.copytree("static", os.path.join(out_dir, "static"))
print("Copied static/ directory")

# 6. Copy PDF
if os.path.exists("CV_Muhammad_Mirza_Wibisono.pdf"):
    shutil.copy2("CV_Muhammad_Mirza_Wibisono.pdf", os.path.join(out_dir, "CV_Muhammad_Mirza_Wibisono.pdf"))
    print("Copied CV PDF")

# 7. Add .nojekyll so GitHub Pages does not ignore files starting with underscore
with open(os.path.join(out_dir, ".nojekyll"), "w") as f:
    pass

print("\nSTATIC BUILD SUCCESSFUL! All pages and assets ready in docs/ for GitHub Pages!")

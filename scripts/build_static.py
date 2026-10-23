import sys, os
sys.path.insert(0, os.path.abspath("."))

from fastapi.testclient import TestClient
from main import app, load_content
import shutil
import re

client = TestClient(app)
content = load_content()

out_dir = "docs"
if os.path.exists(out_dir):
    shutil.rmtree(out_dir)
os.makedirs(out_dir, exist_ok=True)

# ID to slug mapping
id_to_slug = {p["id"]: p["slug"] for p in content.get("projects", [])}

def transform_html(html: str, depth: int) -> str:
    """
    Transforms absolute URLs into clean relative URLs so the static site
    renders flawlessly on any base path (e.g. GitHub Pages https://<user>.github.io/<repo>/
    as well as custom domains and local filesystem).
    
    depth = 0: docs/index.html (prefix './')
    depth = 1: docs/karya/index.html, docs/cv/index.html (prefix '../')
    depth = 2: docs/karya/{slug}/index.html (prefix '../../')
    """
    prefix = ("../" * depth) if depth > 0 else "./"
    
    # 1. Map ID-based project links (e.g. /karya/P01 -> prefix + karya/perencanaan-transportasi-wonokromo/)
    for pid, slug in id_to_slug.items():
        html = re.sub(rf'href=[\x22\x27]/karya/{pid}/?[\x22\x27]', f'href="{prefix}karya/{slug}/"', html)
        html = re.sub(rf'href=[\x22\x27]/karya/{pid}\?([^\x22\x27]*)[\x22\x27]', f'href="{prefix}karya/{slug}/?\\1"', html)

    # 2. Map slug project links (/karya/{slug} -> prefix + karya/{slug}/)
    html = re.sub(r'href=[\x22\x27]/karya/([a-zA-Z0-9_\-]+)/?[\x22\x27]', rf'href="{prefix}karya/\1/"', html)

    # 3. Map /karya catalog links with query parameters or anchors
    html = re.sub(r'href=[\x22\x27]/karya\?([^\x22\x27]*)[\x22\x27]', rf'href="{prefix}karya/?\1"', html)
    html = re.sub(r'href=[\x22\x27]/karya#([^\x22\x27]*)[\x22\x27]', rf'href="{prefix}karya/#\1"', html)
    html = re.sub(r'href=[\x22\x27]/karya/?[\x22\x27]', rf'href="{prefix}karya/"', html)

    # 4. Map /cv links
    html = re.sub(r'href=[\x22\x27]/cv#([^\x22\x27]*)[\x22\x27]', rf'href="{prefix}cv/#\1"', html)
    html = re.sub(r'href=[\x22\x27]/cv/?[\x22\x27]', rf'href="{prefix}cv/"', html)

    # 5. Map root anchors (/#tentang, /#kontak, etc.)
    html = re.sub(r'href=[\x22\x27]/#([a-zA-Z0-9_\-]+)[\x22\x27]', rf'href="{prefix}#\1"', html)

    # 6. Map root home link href="/"
    html = re.sub(r'href=[\x22\x27]/[\x22\x27]', rf'href="{prefix}"', html)

    # 7. Map static asset URLs (CSS, JS, WebP, SVG, certificates, etc.)
    html = re.sub(r'href=[\x22\x27]/static/([^\x22\x27]*)[\x22\x27]', rf'href="{prefix}static/\1"', html)
    html = re.sub(r'src=[\x22\x27]/static/([^\x22\x27]*)[\x22\x27]', rf'src="{prefix}static/\1"', html)
    html = re.sub(r'content=[\x22\x27]/static/([^\x22\x27]*)[\x22\x27]', rf'content="{prefix}static/\1"', html)

    # 8. Map CV PDF file
    html = re.sub(r'href=[\x22\x27]/CV_Muhammad_Mirza_Wibisono\.pdf[\x22\x27]', rf'href="{prefix}CV_Muhammad_Mirza_Wibisono.pdf"', html)

    return html

# 1. Generate / -> docs/index.html (depth 0)
r = client.get("/")
assert r.status_code == 200
html_root = transform_html(r.text, depth=0)
with open(os.path.join(out_dir, "index.html"), "w", encoding="utf-8") as f:
    f.write(html_root)
print("Generated index.html (size:", len(html_root), ")")

# Also generate 404.html from root so any deep refresh on GitHub Pages stays functional
with open(os.path.join(out_dir, "404.html"), "w", encoding="utf-8") as f:
    f.write(html_root)
print("Generated 404.html")

# 2. Generate /karya -> docs/karya/index.html (depth 1)
os.makedirs(os.path.join(out_dir, "karya"), exist_ok=True)
r_karya = client.get("/karya")
assert r_karya.status_code == 200
html_karya = transform_html(r_karya.text, depth=1)
with open(os.path.join(out_dir, "karya", "index.html"), "w", encoding="utf-8") as f:
    f.write(html_karya)
print("Generated karya/index.html (size:", len(html_karya), ")")

# 3. Generate /cv -> docs/cv/index.html (depth 1)
os.makedirs(os.path.join(out_dir, "cv"), exist_ok=True)
r_cv = client.get("/cv")
assert r_cv.status_code == 200
html_cv = transform_html(r_cv.text, depth=1)
with open(os.path.join(out_dir, "cv", "index.html"), "w", encoding="utf-8") as f:
    f.write(html_cv)
print("Generated cv/index.html (size:", len(html_cv), ")")

# 4. Generate all project pages /karya/{slug} -> docs/karya/{slug}/index.html (depth 2)
for p in content.get("projects", []):
    slug = p["slug"]
    p_dir = os.path.join(out_dir, "karya", slug)
    os.makedirs(p_dir, exist_ok=True)
    r_p = client.get(f"/karya/{slug}")
    assert r_p.status_code == 200
    html_p = transform_html(r_p.text, depth=2)
    with open(os.path.join(p_dir, "index.html"), "w", encoding="utf-8") as f:
        f.write(html_p)
    print(f"Generated karya/{slug}/index.html (size: {len(html_p)})")
    
    # Also generate alias for ID (e.g. docs/karya/P01/index.html)
    pid = p.get("id")
    if pid and pid != slug:
        pid_dir = os.path.join(out_dir, "karya", pid)
        os.makedirs(pid_dir, exist_ok=True)
        with open(os.path.join(pid_dir, "index.html"), "w", encoding="utf-8") as f:
            f.write(html_p)

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

print("\nSTATIC BUILD SUCCESSFUL! All pages and assets ready in docs/ with clean relative paths for GitHub Pages!")

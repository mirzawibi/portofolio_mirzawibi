import os
import json
import shutil
import time
from datetime import datetime
from typing import Optional, List
from fastapi import FastAPI, Request, Form, UploadFile, File, Depends, HTTPException, status
from fastapi.responses import HTMLResponse, RedirectResponse, FileResponse, JSONResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from starlette.middleware.sessions import SessionMiddleware

app = FastAPI(title="Portofolio Muhammad Mirza Wibisono", version="1.0.0")

# Session secret
SECRET_KEY = os.getenv("PORTFOLIO_SECRET_KEY", "mirza-pwk-portfolio-secret-2026")
app.add_middleware(SessionMiddleware, secret_key=SECRET_KEY, max_age=86400 * 7)

# Mount static directories
os.makedirs("static", exist_ok=True)
app.mount("/static", StaticFiles(directory="static"), name="static")

templates = Jinja2Templates(directory="templates")

def render_template(request: Request, name: str, context: dict = None, status_code: int = 200):
    if context is None:
        context = {}
    return templates.TemplateResponse(request=request, name=name, context=context, status_code=status_code)

DATA_FILE = os.path.abspath("data/content.json")
BACKUPS_DIR = os.path.abspath("data/backups")
CV_PDF_PATH = os.path.abspath("CV_Muhammad_Mirza_Wibisono.pdf")
ADMIN_PASSWORD = os.getenv("ADMIN_PASSWORD", "mirzawibi2026")

def load_content() -> dict:
    if not os.path.exists(DATA_FILE):
        raise RuntimeError("content.json does not exist. Please run init_data.py first.")
    with open(DATA_FILE, "r", encoding="utf-8") as f:
        return json.load(f)

def save_content(data: dict, backup_note: str = "Pembaruan Konten"):
    os.makedirs(BACKUPS_DIR, exist_ok=True)
    ts = datetime.now().strftime("%Y%m%d_%H%M%S")
    clean_note = "".join(c for c in backup_note if c.isalnum() or c in (" ", "_", "-")).strip()
    backup_path = os.path.join(BACKUPS_DIR, f"backup_{ts}_{clean_note}.json")
    
    # Save backup of current version if exists
    if os.path.exists(DATA_FILE):
        shutil.copyfile(DATA_FILE, backup_path)
    
    data["site_settings"]["last_published"] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open(DATA_FILE, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2, ensure_ascii=False)

def get_backups() -> list:
    if not os.path.exists(BACKUPS_DIR):
        return []
    files = []
    for f in os.listdir(BACKUPS_DIR):
        if f.endswith(".json"):
            fp = os.path.join(BACKUPS_DIR, f)
            stat = os.stat(fp)
            files.append({
                "filename": f,
                "created_at": datetime.fromtimestamp(stat.st_mtime).strftime("%Y-%m-%d %H:%M:%S"),
                "size_kb": round(stat.st_size / 1024, 1)
            })
    files.sort(key=lambda x: x["created_at"], reverse=True)
    return files

def is_authenticated(request: Request) -> bool:
    return request.session.get("authenticated") is True

def require_admin(request: Request):
    if not is_authenticated(request):
        raise HTTPException(status_code=status.HTTP_303_SEE_OTHER, headers={"Location": "/admin/login"})

# Context processor for templates
def get_base_context(request: Request):
    data = load_content()
    # Check CV file size and modified time
    cv_size_str = "81 KB"
    cv_date_str = "20 Oktober 2026"
    if os.path.exists(CV_PDF_PATH):
        stat = os.stat(CV_PDF_PATH)
        cv_size_str = f"{round(stat.st_size / 1024)} KB"
        cv_date_str = datetime.fromtimestamp(stat.st_mtime).strftime("%d %B %Y")
    
    data["resume_asset"]["filesize_str"] = cv_size_str
    data["resume_asset"]["updated_at"] = cv_date_str
    
    return {
        "request": request,
        "profile": data.get("profile", {}),
        "contact": data.get("contact", {}),
        "categories": data.get("categories", []),
        "resume_asset": data.get("resume_asset", {}),
        "site_settings": data.get("site_settings", {}),
        "is_admin": is_authenticated(request)
    }

# --- PUBLIC ROUTES ---

@app.get("/", response_class=HTMLResponse)
async def home(request: Request):
    ctx = get_base_context(request)
    data = load_content()
    
    # Filter published projects
    published_projects = [p for p in data.get("projects", []) if p.get("status") == "published"]
    published_projects.sort(key=lambda x: x.get("sort_order", 99))
    
    featured_projects = [p for p in published_projects if p.get("featured") is True][:3]
    if not featured_projects and published_projects:
        featured_projects = published_projects[:3]
        
    experiences = [e for e in data.get("experiences", []) if e.get("status") == "published"]
    
    ctx.update({
        "featured_projects": featured_projects,
        "selected_experiences": experiences[:6],
        "all_projects_count": len(published_projects),
        "skills": data.get("skills", []),
        "active_nav": "home"
    })
    return render_template(request, "index.html", ctx)

@app.get("/karya", response_class=HTMLResponse)
async def catalog(request: Request, kategori: Optional[str] = None, q: Optional[str] = None):
    ctx = get_base_context(request)
    data = load_content()
    
    published_projects = [p for p in data.get("projects", []) if p.get("status") == "published"]
    published_projects.sort(key=lambda x: x.get("sort_order", 99))
    
    selected_kategori = kategori.strip().lower() if kategori else "semua"
    search_query = q.strip().lower() if q else ""
    
    filtered_projects = []
    for p in published_projects:
        # Category check
        cats = [c.lower() for c in p.get("categories", [])]
        if selected_kategori != "semua" and selected_kategori not in cats:
            continue
        
        # Search query check
        if search_query:
            match = (
                search_query in p.get("title", "").lower()
                or search_query in p.get("summary", "").lower()
                or search_query in p.get("location", "").lower()
                or any(search_query in t.lower() for t in p.get("tools", []))
            )
            if not match:
                continue
        
        filtered_projects.append(p)
    
    ctx.update({
        "projects": filtered_projects,
        "selected_category": selected_kategori,
        "search_query": search_query,
        "total_results": len(filtered_projects),
        "total_all": len(published_projects),
        "active_nav": "karya"
    })
    return render_template(request, "karya.html", ctx)

@app.get("/karya/{slug}", response_class=HTMLResponse)
async def project_detail(request: Request, slug: str, preview: Optional[int] = None):
    ctx = get_base_context(request)
    data = load_content()
    admin_auth = is_authenticated(request)
    
    project = None
    for p in data.get("projects", []):
        if p.get("slug") == slug or p.get("id", "").lower() == slug.lower():
            project = p
            break
            
    if not project:
        raise HTTPException(status_code=404, detail="Studi kasus tidak ditemukan")
    
    # Check published vs draft
    if project.get("status") != "published":
        if not (admin_auth or preview == 1):
            raise HTTPException(status_code=404, detail="Karya ini belum diterbitkan.")
            
    # Find related projects
    all_published = [p for p in data.get("projects", []) if p.get("status") == "published" and p.get("slug") != slug]
    related_ids = project.get("related_project_ids", [])
    related_projects = [p for p in all_published if p.get("id") in related_ids]
    
    # Fallback to category match if needed
    if len(related_projects) < 2:
        for p in all_published:
            if p not in related_projects and any(c in p.get("categories", []) for c in project.get("categories", [])):
                related_projects.append(p)
            if len(related_projects) >= 2:
                break
                
    ctx.update({
        "project": project,
        "related_projects": related_projects[:2],
        "is_preview": project.get("status") != "published",
        "active_nav": "karya"
    })
    return render_template(request, "karya_detail.html", ctx)

@app.get("/cv", response_class=HTMLResponse)
async def cv_view(request: Request, filter: Optional[str] = None):
    ctx = get_base_context(request)
    data = load_content()
    
    experiences = [e for e in data.get("experiences", []) if e.get("status") == "published"]
    cv_filters = data.get("cv_filters", [])
    
    selected_filter = filter.strip().lower() if filter else "semua"
    active_filter_tags = []
    for f_item in cv_filters:
        if f_item.get("id") == selected_filter:
            active_filter_tags = [t.lower() for t in f_item.get("tags", [])]
            break
            
    if selected_filter != "semua":
        if active_filter_tags:
            filtered_exp = [
                e for e in experiences 
                if any(t.lower() in active_filter_tags for t in e.get("tags", []))
            ]
        else:
            filtered_exp = [
                e for e in experiences 
                if selected_filter in [t.lower() for t in e.get("tags", [])]
            ]
    else:
        filtered_exp = experiences
        
    ctx.update({
        "experiences": filtered_exp,
        "all_experiences": experiences,
        "selected_filter": selected_filter,
        "cv_filters": cv_filters,
        "competencies": data.get("competencies", {}),
        "speaking": data.get("speaking", []),
        "education": data.get("education", []),
        "skills": data.get("skills", []),
        "achievements": data.get("achievements", []),
        "projects": data.get("projects", []),
        "active_nav": "cv"
    })
    return render_template(request, "cv.html", ctx)

@app.get("/CV_Muhammad_Mirza_Wibisono.pdf")
@app.get("/download/cv")
async def download_cv():
    if not os.path.exists(CV_PDF_PATH):
        raise HTTPException(status_code=404, detail="Berkas CV PDF tidak ditemukan.")
    return FileResponse(
        CV_PDF_PATH,
        media_type="application/pdf",
        filename="CV_Muhammad_Mirza_Wibisono.pdf"
    )

# --- ADMIN ROUTES ---

@app.get("/admin/login", response_class=HTMLResponse)
async def admin_login_page(request: Request, error: Optional[str] = None):
    if is_authenticated(request):
        return RedirectResponse(url="/admin", status_code=303)
    ctx = get_base_context(request)
    ctx.update({"error": error})
    return render_template(request, "admin/login.html", ctx)

@app.post("/admin/login")
async def admin_login(request: Request, password: str = Form(...)):
    if password == ADMIN_PASSWORD:
        request.session["authenticated"] = True
        return RedirectResponse(url="/admin", status_code=303)
    return RedirectResponse(url="/admin/login?error=Kata+sandi+tidak+cocok", status_code=303)

@app.get("/admin/logout")
async def admin_logout(request: Request):
    request.session.clear()
    return RedirectResponse(url="/", status_code=303)

@app.get("/admin", response_class=HTMLResponse)
async def admin_dashboard(request: Request, tab: Optional[str] = "overview", msg: Optional[str] = None):
    require_admin(request)
    ctx = get_base_context(request)
    data = load_content()
    
    projects = data.get("projects", [])
    projects.sort(key=lambda x: x.get("sort_order", 99))
    
    ctx.update({
        "data": data,
        "projects": projects,
        "experiences": data.get("experiences", []),
        "backups": get_backups(),
        "active_tab": tab,
        "success_msg": msg,
        "active_nav": "admin"
    })
    return render_template(request, "admin/dashboard.html", ctx)

@app.post("/admin/profile/update")
async def admin_update_profile(
    request: Request,
    name: str = Form(...),
    short_name: str = Form(...),
    title: str = Form(...),
    field: str = Form(...),
    hero_headline: str = Form(...),
    bio: str = Form(...),
    internship_status: str = Form(...),
    internship_period: str = Form(...),
    email: str = Form(...),
    linkedin: str = Form(...),
    phone: str = Form(...),
    location: str = Form(...)
):
    require_admin(request)
    data = load_content()
    
    data["profile"]["name"] = name.strip()
    data["profile"]["short_name"] = short_name.strip()
    data["profile"]["title"] = title.strip()
    data["profile"]["field"] = field.strip()
    data["profile"]["hero_headline"] = hero_headline.strip()
    data["profile"]["bio"] = bio.strip()
    data["profile"]["internship_status"] = internship_status.strip()
    data["profile"]["internship_period"] = internship_period.strip()
    data["profile"]["updated_at"] = datetime.now().strftime("%Y-%m-%d")
    
    data["contact"]["email"] = email.strip()
    data["contact"]["linkedin"] = linkedin.strip()
    data["contact"]["phone"] = phone.strip()
    data["contact"]["location"] = location.strip()
    
    save_content(data, "Pembaruan Profil dan Kontak")
    return RedirectResponse(url="/admin?tab=profile&msg=Profil+berhasil+diperbarui", status_code=303)

@app.get("/admin/projects/new", response_class=HTMLResponse)
async def admin_new_project_page(request: Request):
    require_admin(request)
    ctx = get_base_context(request)
    data = load_content()
    
    new_p = {
        "id": f"P{len(data.get('projects', [])) + 1:02d}",
        "slug": "",
        "title": "",
        "categories": ["transportasi"],
        "project_type": "Proyek Akademik",
        "location": "Surabaya, Jawa Timur",
        "year": "2026",
        "featured": False,
        "sort_order": len(data.get("projects", [])) + 1,
        "status": "draft",
        "cover_image": "/static/assets/slides/slide_1_thumb.webp",
        "role_summary": "",
        "my_contributions": [],
        "team_deliverables": [],
        "tools": [],
        "summary": "",
        "problem_statement": "",
        "methodology": "",
        "recommendations": "",
        "scenarios": [],
        "metrics": []
    }
    ctx.update({
        "project": new_p,
        "is_new": True,
        "active_nav": "admin"
    })
    return render_template(request, "admin/project_edit.html", ctx)

@app.get("/admin/projects/{project_id}/edit", response_class=HTMLResponse)
async def admin_edit_project_page(request: Request, project_id: str):
    require_admin(request)
    ctx = get_base_context(request)
    data = load_content()
    
    project = next((p for p in data.get("projects", []) if p.get("id") == project_id), None)
    if not project:
        raise HTTPException(status_code=404, detail="Proyek tidak ditemukan")
        
    ctx.update({
        "project": project,
        "is_new": False,
        "active_nav": "admin"
    })
    return render_template(request, "admin/project_edit.html", ctx)

@app.post("/admin/projects/save")
async def admin_save_project(
    request: Request,
    id: str = Form(...),
    is_new: bool = Form(False),
    title: str = Form(...),
    slug: str = Form(...),
    categories: str = Form(...),
    project_type: str = Form(...),
    location: str = Form(...),
    year: str = Form(...),
    status: str = Form(...),
    featured: bool = Form(False),
    sort_order: int = Form(1),
    cover_image: str = Form(...),
    role_summary: str = Form(...),
    summary: str = Form(...),
    problem_statement: str = Form(...),
    methodology: str = Form(...),
    recommendations: str = Form(...),
    my_contributions_text: str = Form(...),
    team_deliverables_text: str = Form(...),
    tools_text: str = Form(...)
):
    require_admin(request)
    data = load_content()
    
    clean_slug = slug.strip().lower()
    if not clean_slug:
        clean_slug = "".join(c if c.isalnum() else "-" for c in title.lower()).strip("-")
        
    cats = [c.strip() for c in categories.split(",") if c.strip()]
    tools = [t.strip() for t in tools_text.split(",") if t.strip()]
    my_contribs = [c.strip() for c in my_contributions_text.split("\n") if c.strip()]
    team_delivs = [d.strip() for d in team_deliverables_text.split("\n") if d.strip()]
    
    project_dict = {
        "id": id.strip(),
        "slug": clean_slug,
        "title": title.strip(),
        "categories": cats,
        "project_type": project_type.strip(),
        "location": location.strip(),
        "year": year.strip(),
        "status": status.strip(),
        "featured": featured,
        "sort_order": sort_order,
        "cover_image": cover_image.strip(),
        "role_summary": role_summary.strip(),
        "summary": summary.strip(),
        "problem_statement": problem_statement.strip(),
        "methodology": methodology.strip(),
        "recommendations": recommendations.strip(),
        "my_contributions": my_contribs,
        "team_deliverables": team_delivs,
        "tools": tools
    }
    
    # Preserve existing scenarios and metrics if editing
    existing_idx = None
    for idx, p in enumerate(data.get("projects", [])):
        if p.get("id") == id:
            existing_idx = idx
            break
            
    if existing_idx is not None:
        project_dict["scenarios"] = data["projects"][existing_idx].get("scenarios", [])
        project_dict["metrics"] = data["projects"][existing_idx].get("metrics", [])
        project_dict["source_pages"] = data["projects"][existing_idx].get("source_pages", [])
        project_dict["related_project_ids"] = data["projects"][existing_idx].get("related_project_ids", [])
        data["projects"][existing_idx] = project_dict
    else:
        project_dict["scenarios"] = []
        project_dict["metrics"] = []
        data["projects"].append(project_dict)
        
    save_content(data, f"Simpan Proyek {id} - {title}")
    return RedirectResponse(url=f"/admin?tab=projects&msg=Proyek+{id}+berhasil+disimpan", status_code=303)

@app.post("/admin/projects/{project_id}/move")
async def admin_move_project(request: Request, project_id: str, direction: str = Form(...)):
    require_admin(request)
    data = load_content()
    projects = data.get("projects", [])
    projects.sort(key=lambda x: x.get("sort_order", 99))
    
    idx = next((i for i, p in enumerate(projects) if p.get("id") == project_id), None)
    if idx is not None:
        if direction == "up" and idx > 0:
            projects[idx]["sort_order"], projects[idx - 1]["sort_order"] = (
                projects[idx - 1]["sort_order"],
                projects[idx]["sort_order"]
            )
        elif direction == "down" and idx < len(projects) - 1:
            projects[idx]["sort_order"], projects[idx + 1]["sort_order"] = (
                projects[idx + 1]["sort_order"],
                projects[idx]["sort_order"]
            )
            
    save_content(data, f"Ubah urutan proyek {project_id}")
    return RedirectResponse(url="/admin?tab=projects&msg=Urutan+proyek+diperbarui", status_code=303)

@app.post("/admin/projects/{project_id}/toggle-status")
async def admin_toggle_project_status(request: Request, project_id: str):
    require_admin(request)
    data = load_content()
    for p in data.get("projects", []):
        if p.get("id") == project_id:
            new_status = "draft" if p.get("status") == "published" else "published"
            p["status"] = new_status
            break
    save_content(data, f"Ubah status publikasi {project_id}")
    return RedirectResponse(url="/admin?tab=projects&msg=Status+publikasi+diperbarui", status_code=303)

@app.post("/admin/projects/{project_id}/toggle-featured")
async def admin_toggle_project_featured(request: Request, project_id: str):
    require_admin(request)
    data = load_content()
    for p in data.get("projects", []):
        if p.get("id") == project_id:
            p["featured"] = not p.get("featured", False)
            break
    save_content(data, f"Ubah status unggulan {project_id}")
    return RedirectResponse(url="/admin?tab=projects&msg=Status+unggulan+diperbarui", status_code=303)

@app.post("/admin/experiences/save")
async def admin_save_experience(
    request: Request,
    id: Optional[str] = Form(None),
    org: str = Form(...),
    role: str = Form(...),
    period: str = Form(...),
    tags_text: str = Form(...),
    summary: str = Form(...),
    contributions_text: str = Form(...)
):
    require_admin(request)
    data = load_content()
    tags = [t.strip().lower() for t in tags_text.split(",") if t.strip()]
    contribs = [c.strip() for c in contributions_text.split("\n") if c.strip()]
    
    if not id or id == "new":
        exp_id = f"exp_{len(data.get('experiences', [])) + 1:02d}"
        new_exp = {
            "id": exp_id,
            "org": org.strip(),
            "role": role.strip(),
            "period": period.strip(),
            "tags": tags,
            "summary": summary.strip(),
            "contributions": contribs,
            "status": "published",
            "confirmed_project_id": None
        }
        data["experiences"].insert(0, new_exp)
    else:
        for e in data.get("experiences", []):
            if e.get("id") == id:
                e["org"] = org.strip()
                e["role"] = role.strip()
                e["period"] = period.strip()
                e["tags"] = tags
                e["summary"] = summary.strip()
                e["contributions"] = contribs
                break
                
    save_content(data, f"Simpan Pengalaman {org}")
    return RedirectResponse(url="/admin?tab=experiences&msg=Pengalaman+berhasil+disimpan", status_code=303)

@app.post("/admin/cv/upload")
async def admin_upload_cv(request: Request, cv_file: UploadFile = File(...)):
    require_admin(request)
    if not cv_file.filename.endswith(".pdf"):
        return RedirectResponse(url="/admin?tab=cv&msg=Hanya+berkas+PDF+yang+diizinkan", status_code=303)
        
    content = await cv_file.read()
    # Write to target path
    with open(CV_PDF_PATH, "wb") as f:
        f.write(content)
        
    data = load_content()
    data["resume_asset"]["updated_at"] = datetime.now().strftime("%d %B %Y")
    data["resume_asset"]["filesize_str"] = f"{round(len(content) / 1024)} KB"
    data["resume_asset"]["is_synced"] = True
    save_content(data, "Upload CV PDF Baru")
    
    return RedirectResponse(url="/admin?tab=cv&msg=Berkas+CV+PDF+berhasil+diunggah", status_code=303)

@app.post("/admin/backups/create")
async def admin_create_backup(request: Request, note: str = Form("Manual Snapshot")):
    require_admin(request)
    data = load_content()
    save_content(data, f"Manual: {note}")
    return RedirectResponse(url="/admin?tab=backups&msg=Cadangan+data+berhasil+dibuat", status_code=303)

@app.post("/admin/backups/restore")
async def admin_restore_backup(request: Request, filename: str = Form(...)):
    require_admin(request)
    backup_file = os.path.join(BACKUPS_DIR, filename)
    if not os.path.exists(backup_file):
        raise HTTPException(status_code=404, detail="Berkas cadangan tidak ditemukan.")
        
    with open(backup_file, "r", encoding="utf-8") as f:
        restored_data = json.load(f)
        
    save_content(restored_data, f"Pemulihan dari {filename}")
    return RedirectResponse(url="/admin?tab=backups&msg=Data+berhasil+dipulihkan+dari+cadangan", status_code=303)

# --- ERROR HANDLERS ---

@app.exception_handler(404)
async def custom_404_handler(request: Request, exc: HTTPException):
    ctx = get_base_context(request)
    ctx.update({"status_code": 404, "detail": str(exc.detail) if exc.detail else "Halaman tidak ditemukan"})
    return render_template(request, "404.html", ctx, status_code=404)

@app.exception_handler(500)
async def custom_500_handler(request: Request, exc: Exception):
    ctx = get_base_context(request)
    ctx.update({"status_code": 500, "detail": "Terjadi kesalahan pada server."})
    return render_template(request, "404.html", ctx, status_code=500)

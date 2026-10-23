import json, shutil, os

# 1. Backup current content.json
os.makedirs("data/backups", exist_ok=True)
shutil.copy2("data/content.json", "data/backups/content_backup_pre_cv_pdf_update.json")

with open("data/content.json", "r", encoding="utf-8") as f:
    d = json.load(f)

# Update contact
d["contact"]["phone"] = "0895367056584"
d["contact"]["email"] = "mirzawibi@gmail.com"
d["contact"]["linkedin"] = "https://www.linkedin.com/in/mirzawibi"
d["contact"]["location"] = "Surabaya, Indonesia"

# Update profile bio summary to match CV
d["profile"]["phone"] = "0895367056584"
d["profile"]["email"] = "mirzawibi@gmail.com"
d["profile"]["linkedin"] = "https://www.linkedin.com/in/mirzawibi"
d["profile"]["location"] = "Surabaya, Indonesia"

# Update Education strictly to match PDF
d["education"] = [
    {
        "institution": "Institut Teknologi Sepuluh Nopember - Surabaya, Indonesia",
        "program": "Bachelor of Urban and Regional Planning",
        "degree": "S1 PWK",
        "period": "Aug 2024 - Sep 2028 (Perkiraan)",
        "gpa": "3.58",
        "gpa_scale": "4.00",
        "location": "Surabaya, Indonesia",
        "highlights": [
            "Bachelor of Urban and Regional Planning, 3.58/4.00",
            "Appointed as Vice Year Class President"
        ]
    },
    {
        "institution": "SMA Negeri 1 Magetan - Magetan, Indonesia",
        "program": "High School Diploma in Mathematics and Science",
        "degree": "MIPA",
        "period": "Jul 2021 - May 2024",
        "gpa": "93.48",
        "gpa_scale": "100.00",
        "location": "Magetan, Indonesia",
        "highlights": [
            "High School Diploma in Mathematics and Science, 93.48/100.00",
            "Appointed as a class president"
        ]
    }
]

# Update Experiences strictly to match PDF (13 items, 4 Profesional + 9 Other Experience)
d["experiences"] = [
    # --- PENGALAMAN PROFESIONAL (4 items) ---
    {
        "id": "exp_dishub_sidoarjo",
        "org": "Dinas Perhubungan Sidoarjo",
        "location": "Sidoarjo",
        "role": "Surveyor",
        "period": "Nov 2025 - Dec 2025",
        "section": "profesional",
        "group": "Pengalaman Profesional",
        "tags": ["transportasi", "survei", "kebijakan"],
        "anchor": {
            "value": "77+",
            "label": "armada & trayek angkutan pedesaan disurvei"
        },
        "featured": True,
        "summary": "Conducted field surveys assessing operational status of rural public transportation and interviewed passengers to gather ridership data.",
        "contributions": [
            "Conducted field surveys assessing operational status of rural public transportation in Sidoarjo, producing data covering vehicle conditions, route coverage, and service indicators.",
            "Interviewed public transportation and Transjatim passengers to gather firsthand ridership data, contributing to a comprehensive mobility assessment report for the local transportation authority."
        ],
        "status": "published",
        "confirmed_project_id": None
    },
    {
        "id": "exp_its_eco_campus",
        "org": "ITS ECO CAMPUS",
        "location": "Surabaya",
        "role": "Surveyor",
        "period": "Apr 2026 - May 2026",
        "section": "profesional",
        "group": "Pengalaman Profesional",
        "tags": ["transportasi", "survei", "analisis"],
        "anchor": {
            "value": "3",
            "label": "lokasi strategis traffic count ITS"
        },
        "featured": True,
        "summary": "Executed manual traffic counts across 3 strategic locations within ITS campus for trip generation analysis.",
        "contributions": [
            "Executed manual traffic counts across 3 strategic locations within ITS campus, collecting structured volume data as the primary input for trip generation analysis."
        ],
        "status": "published",
        "confirmed_project_id": "P01"
    },
    {
        "id": "exp_asdos_sip",
        "org": "Institut Teknologi Sepuluh Nopember",
        "location": "Surabaya, Indonesia",
        "role": "Assistant Lecture System Information Planning",
        "period": "Mar 2026 - Jul 2026",
        "section": "profesional",
        "group": "Pengalaman Profesional",
        "tags": ["gis", "analisis", "pengajaran"],
        "anchor": {
            "value": "45",
            "label": "mahasiswa praktikum GIS didampingi"
        },
        "featured": True,
        "summary": "Delivered hands-on teaching assistance for Planning Information Systems course covering GIS, Raster Analysis, and Web GIS to 45 students.",
        "contributions": [
            "Delivered hands-on teaching assistance for Planning Information Systems course covering GIS, Raster Analysis, and Web GIS to 45 students, improving student comprehension of spatial analysis tools."
        ],
        "status": "published",
        "confirmed_project_id": "P02"
    },
    {
        "id": "exp_asdos_map",
        "org": "Institut Teknologi Sepuluh Nopember",
        "location": "Surabaya, Indonesia",
        "role": "Assistant Lecturer Planning Analysis Methods",
        "period": "Aug 2026 - Sekarang",
        "section": "profesional",
        "group": "Pengalaman Profesional",
        "tags": ["analisis", "kebijakan", "pengajaran"],
        "anchor": {
            "value": "43",
            "label": "mahasiswa didampingi melalui 15 modul"
        },
        "featured": True,
        "summary": "Delivered 15 course modules to a cohort of 43 students, guiding practical applications of Excel, SPSS, and Super Decisions.",
        "contributions": [
            "Delivered 15 course modules to a cohort of 43 students, guiding practical applications of Excel, SPSS, and Super Decisions to solve complex analytical problems"
        ],
        "status": "published",
        "confirmed_project_id": "P05"
    },

    # --- OTHER EXPERIENCE (9 items) ---
    {
        "id": "exp_ilits_2025",
        "org": "INI LHO ITS 2025!",
        "location": "Surabaya, Indonesia",
        "role": "Staff Media Production",
        "period": "Oct 2024 - Mar 2025",
        "section": "organisasi",
        "group": "Other Experience",
        "tags": ["media", "kepanitiaan"],
        "anchor": {
            "value": "3",
            "label": "peran produksi utama (DoP, Asisten DoP, Kamera)"
        },
        "featured": False,
        "summary": "Served in triple production roles in ILITS 2025 and coordinated all media production deliverables for the farewell event as PIC.",
        "contributions": [
            "Served in triple production roles (Director of Photography, Assistant DoP, and Assistant Camera) in ILITS 2025, contributing to cohesive visual storytelling across the entire production.",
            "Coordinated all media production deliverables for the INI LHO ITS 2025 farewell event as PIC, ensuring on-time completion of visual content for the closing ceremony."
        ],
        "status": "published",
        "confirmed_project_id": None
    },
    {
        "id": "exp_imagits",
        "org": "IMAGITS",
        "location": "Magetan, Indonesia",
        "role": "Chairman",
        "period": "Jan 2025 - Feb 2026",
        "section": "kepemimpinan",
        "group": "Other Experience",
        "tags": ["kepemimpinan", "organisasi"],
        "anchor": {
            "value": "30",
            "label": "anggota organisasi dipimpin"
        },
        "featured": True,
        "summary": "Established organizational vision, mission, and annual work program, and led an organization of 30 members.",
        "contributions": [
            "Established the organizational vision, mission, and annual work program for IMAGITS, providing strategic direction that aligned the team's efforts throughout the period.",
            "Led an organization of 30 members, overseeing recruitment, coordination, and program execution to strengthen the regional network of ITS students from Magetan."
        ],
        "status": "published",
        "confirmed_project_id": None
    },
    {
        "id": "exp_gerigi_2025",
        "org": "Gerigi x UKM EXPO ITS 2025",
        "location": "Surabaya, Indonesia",
        "role": "Staff Media Production",
        "period": "Jul 2025 - Feb 2026",
        "section": "organisasi",
        "group": "Other Experience",
        "tags": ["media", "kepanitiaan"],
        "anchor": None,
        "featured": False,
        "summary": "Conceptualized the narrative and visual direction for GEREX 2025 video production and operated live camera on event day.",
        "contributions": [
            "Conceptualized the narrative and visual direction for GEREX 2025 video production, establishing the creative foundation that guided the entire production team.",
            "Operated live camera and managed full event documentation on event day."
        ],
        "status": "published",
        "confirmed_project_id": None
    },
    {
        "id": "exp_plan_a",
        "org": "Plan - A",
        "location": "Surabaya, Indonesia",
        "role": "Head of Branding and Marketing Division",
        "period": "Aug 2025 - Oct 2025",
        "section": "kepemimpinan",
        "group": "Other Experience",
        "tags": ["kepemimpinan", "media"],
        "anchor": {
            "value": "23",
            "label": "staf lintas 3 subdivisi disupervisi"
        },
        "featured": True,
        "summary": "Built comprehensive Work Breakdown Structure (WBS) and supervised 3 subdivisions with 23 staff members.",
        "contributions": [
            "Built a comprehensive Work Breakdown Structure (WBS) for the Branding & Marketing division, translating strategic goals into actionable task plans for each subdivision.",
            "Supervised 3 subdivisions with 23 staff members, ensuring quality control to meet all division targets on schedule"
        ],
        "status": "published",
        "confirmed_project_id": None
    },
    {
        "id": "exp_planopolis_2025",
        "org": "Planopolis 2025",
        "location": "Surabaya, Indonesia",
        "role": "Expert Staff of Media Production",
        "period": "Aug 2025 - Feb 2026",
        "section": "organisasi",
        "group": "Other Experience",
        "tags": ["media", "kepanitiaan"],
        "anchor": None,
        "featured": False,
        "summary": "Formulated detailed job descriptions, standardized workflows, and mentored media production staff performance.",
        "contributions": [
            "Formulated detailed job descriptions and task frameworks for media production staff to standardize workflow and ensure consistent output quality",
            "Mentored and monitored staff performance against established production standards, providing real-time feedback that maintained output quality across all assigned projects."
        ],
        "status": "published",
        "confirmed_project_id": None
    },
    {
        "id": "exp_ilits_2026",
        "org": "INI LHO ITS 2026!",
        "location": "Surabaya, Indonesia",
        "role": "Head of Media Production Subdivision",
        "period": "Sep 2025 - Mar 2026",
        "section": "kepemimpinan",
        "group": "Other Experience",
        "tags": ["kepemimpinan", "media", "kepanitiaan"],
        "anchor": {
            "value": "110",
            "label": "karya visual & video terpopuler diproduksi"
        },
        "featured": True,
        "summary": "Designed detailed WBS and successfully led the production of 110 visual works in a single period, producing the most-viewed video.",
        "contributions": [
            "Designed a detailed Work Breakdown Structure (WBS) that distributed tasks across the team, ensuring all production timelines were met within a single event period.",
            "Successfully led the production of 84 motion graphics, 18 visual editing projects, and 8 production projects—a total of 110 works in a single period—and produced the video with the most views on INI LHO ITS!"
        ],
        "status": "published",
        "confirmed_project_id": None
    },
    {
        "id": "exp_hmpl_its",
        "org": "HMPL ITS",
        "location": "Surabaya, Indonesia",
        "role": "Staff of Human Resource Development",
        "period": "Apr 2026 - Sekarang",
        "section": "organisasi",
        "group": "Other Experience",
        "tags": ["organisasi", "kepemimpinan"],
        "anchor": {
            "value": "2",
            "label": "proyek divisi kreatif diarahkan"
        },
        "featured": False,
        "summary": "Managing pre-event coordination for HMPL Future Leaders and led the Creative Division across 2 projects.",
        "contributions": [
            "Managing pre-event coordination for the HMPL Future Leaders training program, currently in preparation phase",
            "Led the Creative Division across 2 projects, directing concept development and visual output"
        ],
        "status": "published",
        "confirmed_project_id": None
    },
    {
        "id": "exp_planopolis_2026",
        "org": "Planopolis 2026",
        "location": "Surabaya, Indonesia",
        "role": "Project Officer",
        "period": "May 2026 - Sekarang",
        "section": "kepemimpinan",
        "group": "Other Experience",
        "tags": ["kepemimpinan", "kepanitiaan"],
        "anchor": {
            "value": "100+",
            "label": "panitia lintas 8 divisi & 10 subdivisi dipimpin"
        },
        "featured": True,
        "summary": "Developed Grand Design document and structured the organizational framework of 8 divisions and 10 subdivisions.",
        "contributions": [
            "Developed the Grand Design document as the primary operational blueprint for the event, aligning objectives, timelines, and deliverables across all divisions.",
            "Structured the organizational framework of 8 divisions and 10 subdivisions, establishing clear roles and workflows to support cohesive event execution."
        ],
        "status": "published",
        "confirmed_project_id": None
    },
    {
        "id": "exp_lokasolution",
        "org": "Lokasolution",
        "location": "Surabaya, Indonesia",
        "role": "Member",
        "period": "Jun 2026 - Sekarang",
        "section": "konsultasi",
        "group": "Other Experience",
        "tags": ["konsultasi", "kepemimpinan", "analisis"],
        "anchor": {
            "value": "Vice Project Leader",
            "label": "PT Mitra Pengembang Kawasan (Jababeka)"
        },
        "featured": True,
        "summary": "Vice Project Leader for PT Mitra Pengembang Kawasan (under Jababeka Group), delivering data-driven development strategies.",
        "contributions": [
            "Appointed as Vice Project Leader for PT Mitra Pengembang Kawasan (under Jababeka Group), overseeing team execution and delivering data-driven development strategies.",
            "Conduct structured problem-solving and rigorous market intelligence for diverse development projects, synthesizing macroeconomic trends, target market segmentation, and financial feasibility into executive-level consulting presentations."
        ],
        "status": "published",
        "confirmed_project_id": "P07"
    }
]

# Update Skills strictly to match PDF
d["skills"] = [
    {
        "group": "Hard Skills: GIS Analysis & Spasial",
        "basis_label": "Inti Keilmuan",
        "items": [
            "QGIS",
            "ArcGIS / ArcMap",
            "Google Earth Engine"
        ]
    },
    {
        "group": "Hard Skills: Google Workspace & Produktivitas",
        "basis_label": "Produktivitas",
        "items": [
            "Google Docs",
            "Google Sheets",
            "Google Slides",
            "Google Drive"
        ]
    },
    {
        "group": "Pemodelan Transportasi & Analisis Lanjutan",
        "basis_label": "Keahlian Riset",
        "items": [
            "PTV Visum",
            "Four-Step Transportation Modeling",
            "Urban Network Analysis (UNA)",
            "OD Cost Matrix",
            "Dasymetric Mapping",
            "Trip Generation Analysis"
        ]
    },
    {
        "group": "Metode Kuantitatif & Pemecahan Masalah",
        "basis_label": "Metode Analisis",
        "items": [
            "SPSS",
            "Super Decisions (AHP/Delphi)",
            "Microsoft Excel",
            "MECE Framework",
            "Issue Tree"
        ]
    },
    {
        "group": "Produksi Media & Visual Storytelling",
        "basis_label": "Media Kreatif",
        "items": [
            "Director of Photography (DoP)",
            "Video Production",
            "Motion Graphics",
            "Adobe Premiere Pro",
            "Adobe Photoshop",
            "Adobe Lightroom",
            "Adobe After Effects",
            "CapCut"
        ]
    },
    {
        "group": "Soft Skills: Kepemimpinan & Manajemen Proyek",
        "basis_label": "Interpersonal",
        "items": [
            "Cross-functional team leadership",
            "Work under pressure & tight deadlines",
            "Adaptability across diverse project environments",
            "Work Breakdown Structure (WBS)",
            "Grand Design Architecture"
        ]
    }
]

# Update Speaking strictly to match PDF
d["speaking"] = [
    {
        "title": "Speakers on Basic Media Schooling",
        "year": "2026",
        "organizer": "ITS",
        "topic": "Creative Media Production & Visual Direction"
    },
    {
        "title": "Speaker on Event Management",
        "year": "2026",
        "organizer": "ITS",
        "topic": "Work Breakdown Structure (WBS) & Organizational Framework"
    },
    {
        "title": "Speaker on Understanding Planning Analysis Methods",
        "year": "2026",
        "organizer": "PWK ITS",
        "topic": "Practical Applications of Excel, SPSS, & Multi-Criteria Decision Making"
    }
]

# Update Achievements strictly to match PDF
d["achievements"] = [
    {
        "id": "180dc",
        "title": "Semifinalist 180DC ITS BCC",
        "year": "2026",
        "organizer": "180 Degrees Consulting ITS",
        "description": "Business Case Competition (BCC) pemecahan masalah strategis terstruktur berbasis kerangka MECE dan intelijen pasar."
    },
    {
        "id": "mapid",
        "title": "TOP 50 Finalist in Mapid Webgis Competiton",
        "year": "2026",
        "organizer": "MAPID",
        "description": "Kompetisi inovasi sistem informasi geografis berbasis web (WebGIS) tingkat nasional."
    }
]

# Update resume asset
d["resume_asset"] = {
    "file_path": "/static/assets/resume/CV_Muhammad_Mirza_Wibisono.pdf",
    "filename": "CV_Muhammad_Mirza_Wibisono.pdf",
    "filesize_str": "85 KB",
    "updated_at": "Oktober 2026",
    "version": "2026.10",
    "is_synced": True
}

with open("data/content.json", "w", encoding="utf-8") as f:
    json.dump(d, f, ensure_ascii=False, indent=2)

print("SUCCESS: content.json updated with latest CV from PDF!")

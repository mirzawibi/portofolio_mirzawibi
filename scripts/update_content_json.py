import json

# 1. Update data/content.json
with open('data/content.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

# Update stat_anchors if present
if 'stat_anchors' in data:
    for s in data['stat_anchors']:
        if s.get('value') == '8' and 'divisi' in s.get('label', '').lower():
            s['value'] = '100+'
            s['label'] = 'panitia & staf dipimpin'
            s['detail'] = 'Project Officer Planopolis 2026 (8 divisi & 10 subdivisi)'

# Update experiences
for exp in data.get('experiences', []):
    if exp.get('id') == 'exp_07':
        exp['role'] = 'Ketua Subdivisi Media Production'
        exp['summary'] = 'Saat menjadi Ketua Subdivisi Media Production, berhasil memimpin produksi 110 karya visual tim (84 motion graphics, 18 visual editing, dan 8 materi produksi siaran).'
        exp['contributions'] = [
            'Menyusun Work Breakdown Structure (WBS) operasional divisi dan mengoordinasikan pembagian tugas ke seluruh tim sehingga semua target publikasi tercapai tepat waktu.',
            'Sebagai Ketua Subdivisi Media Production, berhasil memimpin produksi 84 motion graphics, 18 visual editing, dan 8 materi siaran, menghasilkan total 110 karya tim berkualitas tinggi.'
        ]
    elif exp.get('id') == 'exp_05':
        exp['anchor'] = {'value': '100+', 'label': 'panitia & staf dipimpin'}
        exp['summary'] = 'Sebagai Project Officer tertinggi, memimpin koordinasi lintas 8 divisi dan 10 subdivisi dengan lebih dari 100 panitia serta staf operasional.'
        exp['contributions'] = [
            'Menyusun dokumen Grand Design sebagai cetak biru operasional acara nasional PWK ITS yang menyelaraskan sasaran strategis, timeline, dan output seluruh divisi.',
            'Memimpin struktur organisasi 8 divisi dan 10 subdivisi dengan alur kerja, pengawasan WBS, dan pendelegasian wewenang yang terukur bagi 100+ panitia.'
        ]

# Update education in data/content.json to be clean and structured
data['education'] = [
    {
        "institution": "Institut Teknologi Sepuluh Nopember (ITS)",
        "program": "Sarjana (S1) Perencanaan Wilayah dan Kota",
        "degree": "S1 PWK",
        "period": "2024 – 2028 (Mahasiswa Aktif)",
        "gpa": "3.58",
        "gpa_scale": "4.00",
        "location": "Surabaya, Jawa Timur",
        "highlights": [
            "Wakil Ketua Angkatan PWK ITS (Vice Class President) 2024",
            "Fokus keilmuan: Pemodelan Transportasi Makro, Sistem Informasi Geospasial (GIS), dan Analisis Tata Ruang Wilayah",
            "Aktif sebagai Asisten Laboratorium Perencanaan Wilayah dan terlibat dalam berbagai studi kebijakan perkotaan"
        ]
    },
    {
        "institution": "SMA Negeri 1 Magetan",
        "program": "Pendidikan Menengah Atas – Peminatan MIPA",
        "degree": "MIPA",
        "period": "2021 – 2024",
        "gpa": "93.48",
        "gpa_scale": "100.00",
        "location": "Magetan, Jawa Timur",
        "highlights": [
            "Ketua Kelas dan aktif dalam organisasi kesiswaan",
            "Lulusan peminatan Matematika dan Ilmu Pengetahuan Alam dengan predikat akademik sangat memuaskan"
        ]
    }
]

with open('data/content.json', 'w', encoding='utf-8') as f:
    json.dump(data, f, ensure_ascii=False, indent=2)

print("SUCCESS: Updated data/content.json with refined leadership, 110 works, and education")

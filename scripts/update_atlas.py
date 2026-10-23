import json

def update_atlas():
    with open('data/content.json', 'r', encoding='utf-8') as f:
        d = json.load(f)

    d['atlas'] = [
      {
        'id': 'A01',
        'title': 'Peta Jaringan & Skenario Pembebanan Lalu Lintas Wonokromo',
        'project_id': 'P01',
        'project_title': 'Perencanaan Transportasi Wonokromo',
        'project_slug': 'perencanaan-transportasi-wonokromo',
        'category': 'Pemodelan Makro',
        'year': '2024',
        'image_url': '/static/assets/slides/slide_17_large.webp',
        'thumb_url': '/static/assets/slides/slide_17_thumb.webp',
        'caption': 'Simulasi 4-step model pada 8 ruas koridor Wonokromo menggunakan PTV Visum.'
      },
      {
        'id': 'A02',
        'title': 'Peta Indeks Aksesibilitas Halte Suroboyo Bus Surabaya Timur',
        'project_id': 'P02',
        'project_title': 'Aksesibilitas Halte Suroboyo Bus di Surabaya Timur',
        'project_slug': 'aksesibilitas-halte-suroboyo-bus',
        'category': 'Urban Network Analysis',
        'year': '2024',
        'image_url': '/static/assets/slides/slide_10_large.webp',
        'thumb_url': '/static/assets/slides/slide_10_thumb.webp',
        'caption': 'Evaluasi catchment area 77 halte eksisting dan jangkauan pedestrian walking distance.'
      },
      {
        'id': 'A03',
        'title': 'Peta Rencana Struktur & Pola Ruang RDTR Kebomas',
        'project_id': 'P03',
        'project_title': 'Perencanaan Kota Kebomas',
        'project_slug': 'perencanaan-kota-kebomas',
        'category': 'Studio Rencana Kota',
        'year': '2025',
        'image_url': '/static/assets/slides/slide_20_large.webp',
        'thumb_url': '/static/assets/slides/slide_20_thumb.webp',
        'caption': 'Penyusunan materi teknis arahan intensitas ruang dan zonasi 21 desa/kelurahan.'
      },
      {
        'id': 'A04',
        'title': 'Peta Distribusi Suhu Permukaan (LST) & Urban Heat Island Surabaya',
        'project_id': 'P04',
        'project_title': 'Analisis Urban Heat Island Surabaya',
        'project_slug': 'analisis-urban-heat-island-surabaya',
        'category': 'Penginderaan Jauh',
        'year': '2024',
        'image_url': '/static/assets/slides/slide_6_large.webp',
        'thumb_url': '/static/assets/slides/slide_6_thumb.webp',
        'caption': 'Ekstraksi suhu Land Surface Temperature (LST) dari citra multitemporal Landsat 8/9 TIRS.'
      },
      {
        'id': 'A05',
        'title': 'Peta Kesesuaian Lahan & Prioritas Lokasi SMA Temanggung',
        'project_id': 'P05',
        'project_title': 'Analisis Lokasi SMA di Kabupaten Temanggung',
        'project_slug': 'analisis-lokasi-sma-temanggung',
        'category': 'AHP & TOPSIS Spasial',
        'year': '2024',
        'image_url': '/static/assets/slides/slide_14_large.webp',
        'thumb_url': '/static/assets/slides/slide_14_thumb.webp',
        'caption': 'Pemodelan Multi-Criteria Evaluation dan perbandingan berpasangan penentuan zonasi sekolah.'
      },
      {
        'id': 'A06',
        'title': 'Peta Analisis Kekompakan Morfologi 5 Kecamatan Kota Malang',
        'project_id': 'P06',
        'project_title': 'Analisis Kekompakan Kota Malang',
        'project_slug': 'analisis-kekompakan-kota-malang',
        'category': 'Morfologi Kota',
        'year': '2024',
        'image_url': '/static/assets/slides/slide_3_large.webp',
        'thumb_url': '/static/assets/slides/slide_3_thumb.webp',
        'caption': 'Analisis indeks kekompakan bentuk kota, konektivitas jaringan jalan, dan densitas perkotaan.'
      }
    ]

    with open('data/content.json', 'w', encoding='utf-8') as f:
        json.dump(d, f, indent=2, ensure_ascii=False)
    print('Atlas successfully written to content.json')

if __name__ == '__main__':
    update_atlas()

import json

with open('data/content.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

for p in data['projects']:
    print(f"\n==========================================")
    print(f"Slug: {p.get('slug')}")
    print(f"Title: {p.get('title')}")
    print(f"Cover image: {p.get('cover_image')}")
    print(f"Source pages ({len(p.get('source_pages', []))}):")
    for sp in p.get('source_pages', []):
        print("  ", sp)

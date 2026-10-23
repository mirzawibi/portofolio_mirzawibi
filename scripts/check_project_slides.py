import json

with open('data/content.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

for p in data['projects']:
    print(f"=== Slug: {p.get('slug')} ===")
    print("  Title:", p.get('title'))
    print("  Hero image:", p.get('hero_image'))
    print("  Thumbnail:", p.get('thumbnail'))
    if 'slides' in p:
        print(f"  Slides count: {len(p['slides'])}")
        for s in p['slides']:
            print("    -", s)
    if 'gallery' in p:
        print(f"  Gallery count: {len(p['gallery'])}")
        for g in p['gallery']:
            print("    -", g)

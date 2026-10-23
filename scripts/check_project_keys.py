import json

with open('data/content.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

for p in data['projects']:
    print(f"Slug: {p.get('slug')}")
    print("  Keys:", list(p.keys()))
    for k, v in p.items():
        if isinstance(v, (list, dict)):
            print(f"    {k}: len {len(v)}")
        elif 'slide' in str(v).lower() or 'webp' in str(v).lower() or 'svg' in str(v).lower() or 'asset' in str(v).lower():
            print(f"    {k}: {v}")

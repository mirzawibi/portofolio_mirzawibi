import json

with open('data/content.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

for p in data['projects']:
    print(f"\n==========================================")
    print(f"Slug: {p.get('slug')}")
    print(f"Title: {p.get('title')}")
    print(f"Scenarios ({len(p.get('scenarios', []))}):")
    for sc in p.get('scenarios', []):
        print("  - title:", sc.get('title'))
        print("    image:", sc.get('image'))
        print("    large_image:", sc.get('large_image'))
        print("    caption:", sc.get('caption'))

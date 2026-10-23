import json

with open('data/content.json', 'r', encoding='utf-8') as f:
    curr = json.load(f)

with open(r'c:\Users\User\Downloads\content.json', 'r', encoding='utf-8') as f:
    new_d = json.load(f)

print("=== PROFILE CHANGES ===")
for k in curr['profile']:
    c_val = curr['profile'][k]
    n_val = new_d['profile'].get(k)
    if c_val != n_val:
        print(f"[{k}]")
        print("  OLD:", c_val)
        print("  NEW:", n_val)

print("\n=== SAMPLE EXPERIENCES CHANGES ===")
for i in range(min(3, len(curr['experiences']))):
    ce = curr['experiences'][i]
    ne = new_d['experiences'][i]
    print(f"Exp {i+1} ({ce.get('role')} at {ce.get('organization')}):")
    if ce.get('contribution') != ne.get('contribution'):
        print("  OLD contrib:", ce.get('contribution')[:120])
        print("  NEW contrib:", ne.get('contribution')[:120])

with open('templates/karya_detail.html', 'r', encoding='utf-8') as f:
    h = f.read()

idx = h.find('class="scenario-panel')
print(h[idx:idx+800])

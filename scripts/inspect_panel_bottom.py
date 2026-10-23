with open('templates/karya_detail.html', 'r', encoding='utf-8') as f:
    h = f.read()

idx = h.find('zoom-overlay-hint')
print(h[idx:idx+800])

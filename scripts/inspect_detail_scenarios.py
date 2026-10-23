with open('templates/karya_detail.html', 'r', encoding='utf-8') as f:
    h = f.read()

idx = h.find('scenarios')
print(h[idx-100:idx+1500])

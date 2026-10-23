with open('templates/cv.html', 'r', encoding='utf-8') as f:
    h = f.read()

idx = h.find('{% for exp in all_experiences %}')
idx_end = h.find('{% endfor %}', idx)
print(h[idx+200:idx_end+100])

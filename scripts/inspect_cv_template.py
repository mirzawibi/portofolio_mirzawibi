with open('templates/cv.html', 'r', encoding='utf-8') as f:
    h = f.read()

print("Length of cv.html:", len(h))
for line in h.splitlines():
    if 'experiences' in line or 'education' in line or 'skills' in line or 'competencies' in line:
        print(line.strip())

import sys
sys.stdout.reconfigure(encoding='utf-8')

with open('templates/cv.html', 'r', encoding='utf-8') as f:
    lines = f.readlines()

for i in range(430, min(len(lines), 485)):
    print(f"{i+1}: {lines[i]}", end='')

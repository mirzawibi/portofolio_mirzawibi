with open('templates/index.html', 'r', encoding='utf-8') as f:
    html = f.read()

start_marker = '<div class="metro-timeline-item" data-station="st-01"'
end_marker = '</div>\n      </div>\n\n      <!-- Micro-interaction'
idx_start = html.find(start_marker)
idx_end = html.find('<!-- Micro-interaction', idx_start)

print("Found block from", idx_start, "to", idx_end)
print(html[idx_start:idx_end])

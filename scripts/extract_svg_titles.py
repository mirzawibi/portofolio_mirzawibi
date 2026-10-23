import os, re
import xml.etree.ElementTree as ET

def extract_text_from_svg(svg_path):
    try:
        with open(svg_path, 'r', encoding='utf-8', errors='ignore') as f:
            content = f.read()
        
        # Extract text elements
        texts = re.findall(r'<text[^>]*>(.*?)</text>', content, re.DOTALL)
        clean_texts = []
        for t in texts:
            # remove inner tags like <tspan>
            clean = re.sub(r'<[^>]+>', ' ', t).strip()
            # clean extra whitespace
            clean = re.sub(r'\s+', ' ', clean)
            if clean and len(clean) > 2:
                clean_texts.append(clean)
        return clean_texts
    except Exception as e:
        return [f"Error: {e}"]

for i in range(1, 26):
    svg_path = f"Portofolio/{i}.svg"
    if os.path.exists(svg_path):
        txts = extract_text_from_svg(svg_path)
        print(f"=== SLIDE {i}.svg ===")
        # Print first few prominent lines
        for t in txts[:8]:
            print("  *", t[:100])

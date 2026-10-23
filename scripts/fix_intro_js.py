with open('static/halte-intro/halte-intro.js', 'r', encoding='utf-8') as f:
    c = f.read()

# Change once:true to once:false in DEF
c = c.replace("once:true,storageKey:'halteIntroSeen'", "once:false,storageKey:'halteIntroSeen'")
# Also ensure seenKey doesn't block if once is false
c = c.replace("if(!reduce()&&!seenKey())H.classList.add('hi-pending');", "if(!reduce())H.classList.add('hi-pending');")

with open('static/halte-intro/halte-intro.js', 'w', encoding='utf-8') as f:
    f.write(c)

print("SUCCESS: Updated static/halte-intro/halte-intro.js")

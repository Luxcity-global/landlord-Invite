from PIL import Image, ImageDraw, ImageFilter

src_path = r"C:\Users\ESMIS 2601\.gemini\antigravity\scratch\proptii-30day-motion\assets\hero-box.jpg"
out_cutout = r"C:\Users\ESMIS 2601\.gemini\antigravity\scratch\proptii-30day-motion\assets\gift-box-cutout.png"
preview_path = r"C:\Users\ESMIS 2601\.gemini\antigravity\brain\613858a4-7b73-4a34-bfa4-af3bec7a516a\scratch\box_cutout_preview.png"

im = Image.open(src_path).convert("RGBA")
w, h = im.size
px = im.load()

# Let's find exact boundary pixels at key cross-sections so our polygon is 100% pixel-accurate:
# 1. Left edge of white box (y=520..745):
for y in [512, 515, 520, 600, 745, 752]:
    for x in range(200, 235):
        r, g, b, _ = px[x, y]
        if r > 80:
            print(f"Left white edge at y={y}: x={x} (rgb={r},{g},{b})")
            break

# 2. Left edge of blue rim (y=480..508):
for y in [478, 480, 483, 495, 505]:
    for x in range(215, 240):
        r, g, b, _ = px[x, y]
        if b > 95 or r > 40:
            print(f"Left blue rim at y={y}: x={x} (rgb={r},{g},{b})")
            break

# 3. Top-left slant of blue rim (x=230..432):
for x in [230, 300, 380, 430, 434]:
    for y in range(390, 490):
        r, g, b, _ = px[x, y]
        if r > 48 or g > 78 or b > 105:
            print(f"Top-left rim at x={x}: y={y} (rgb={r},{g},{b})")
            break

# 4. Top-right slant of blue rim (x=434..585):
for x in [450, 500, 550, 585]:
    for y in range(395, 450):
        r, g, b, _ = px[x, y]
        if r > 60 and g > 75:
            print(f"Top-right rim at x={x}: y={y} (rgb={r},{g},{b})")
            break

# 5. Lid top-left & top-right & right edge:
for y in [340, 342, 345, 370, 376, 400, 425, 500, 600, 695, 700, 740, 745]:
    xs = [x for x in range(540, 950) if px[x, y][0] > 65]
    if xs:
        print(f"Lid at y={y}: x_min={min(xs)}, x_max={max(xs)}")

# 6. Box right vertical edge & bottom edges:
for y in [650, 700, 712, 716]:
    xs = [x for x in range(700, 760) if px[x, y][0] > 45]
    if xs:
        print(f"Box right edge at y={y}: x_max={max(xs)}")

for x in [230, 350, 500, 535, 540, 600, 700, 740]:
    ys = [y for y in range(700, 850) if px[x, y][0] > 45]
    if ys:
        print(f"Box bottom at x={x}: y_max={max(ys)}")

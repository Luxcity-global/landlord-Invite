from PIL import Image, ImageDraw

src_path = r"C:\Users\ESMIS 2601\.gemini\antigravity\scratch\proptii-30day-motion\assets\hero-box.jpg"
out_cutout = r"C:\Users\ESMIS 2601\.gemini\antigravity\scratch\proptii-30day-motion\assets\gift-box-cutout.png"
preview_path = r"C:\Users\ESMIS 2601\.gemini\antigravity\brain\613858a4-7b73-4a34-bfa4-af3bec7a516a\scratch\box_cutout_preview.png"

im = Image.open(src_path).convert("RGBA")
w, h = im.size
px = im.load()

# Find the exact y of the top-left blue rim at x=240..430 by max vertical derivative:
for x in [235, 260, 300, 350, 400, 430, 460, 500, 540, 580]:
    best_y, best_diff = 0, 0
    for y in range(385, 495):
        r1, g1, b1, _ = px[x, y-2]
        r2, g2, b2, _ = px[x, y+2]
        diff = abs(r2 - r1) + abs(g2 - g1) + abs(b2 - b1)
        if diff > best_diff:
            best_diff = diff
            best_y = y
    print(f"Rim edge at x={x}: y={best_y} (diff={best_diff})")

# Find the exact x of the lid left-top edge at y=340..430:
for y in [345, 360, 376, 395, 415, 430]:
    best_x, best_diff = 0, 0
    for x in range(550, 625):
        r1, g1, b1, _ = px[x-2, y]
        r2, g2, b2, _ = px[x+2, y]
        diff = abs(r2 - r1) + abs(g2 - g1) + abs(b2 - b1)
        if diff > best_diff:
            best_diff = diff
            best_x = x
    print(f"Lid left edge at y={y}: x={best_x} (diff={best_diff})")

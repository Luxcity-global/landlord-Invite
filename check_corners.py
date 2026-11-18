from PIL import Image, ImageDraw, ImageFilter

src_path = r"C:\Users\ESMIS 2601\.gemini\antigravity\scratch\proptii-30day-motion\assets\hero-box.jpg"
out_cutout = r"C:\Users\ESMIS 2601\.gemini\antigravity\scratch\proptii-30day-motion\assets\gift-box-cutout.png"
preview_path = r"C:\Users\ESMIS 2601\.gemini\antigravity\brain\613858a4-7b73-4a34-bfa4-af3bec7a516a\scratch\box_cutout_preview.png"

im = Image.open(src_path).convert("RGBA")
w, h = im.size
px = im.load()

# Let's check exact bottom corner around x=530..560, y=820..860 and lid bottom around x=860..945, y=700..765
for x in range(525, 565, 5):
    best_y, best_diff = 0, 0
    for y in range(820, 865):
        r1, g1, b1, _ = px[x, y-2]
        r2, g2, b2, _ = px[x, y+2]
        diff = abs(r2 - r1) + abs(g2 - g1) + abs(b2 - b1)
        if diff > best_diff:
            best_diff = diff
            best_y = y
    print(f"Front corner x={x}: y={best_y} (diff={best_diff})")

for x in range(745, 945, 20):
    best_y, best_diff = 0, 0
    for y in range(640, 765):
        r1, g1, b1, _ = px[x, y-2]
        r2, g2, b2, _ = px[x, y+2]
        diff = abs(r2 - r1) + abs(g2 - g1) + abs(b2 - b1)
        if diff > best_diff:
            best_diff = diff
            best_y = y
    print(f"Lid bottom x={x}: y={best_y} (diff={best_diff})")

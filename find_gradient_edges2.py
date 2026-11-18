from PIL import Image

src_path = r"C:\Users\ESMIS 2601\.gemini\antigravity\scratch\proptii-30day-motion\assets\hero-box.jpg"
im = Image.open(src_path).convert("RGBA")
px = im.load()

for y in [360, 390, 425, 460, 520, 600, 680, 695, 710, 730, 743]:
    best_x, best_diff = 0, 0
    for x in range(620, 955):
        r1, g1, b1, _ = px[x-2, y]
        r2, g2, b2, _ = px[x+2, y]
        diff = abs(r2 - r1) + abs(g2 - g1) + abs(b2 - b1)
        if diff > best_diff:
            best_diff = diff
            best_x = x
    print(f"Lid right at y={y}: x={best_x} (diff={best_diff})")

for x in [225, 280, 350, 450, 535, 580, 650, 720, 745]:
    best_y, best_diff = 0, 0
    for y in range(700, 845):
        r1, g1, b1, _ = px[x, y-2]
        r2, g2, b2, _ = px[x, y+2]
        diff = abs(r2 - r1) + abs(g2 - g1) + abs(b2 - b1)
        if diff > best_diff:
            best_diff = diff
            best_y = y
    print(f"Box bottom at x={x}: y={best_y} (diff={best_diff})")

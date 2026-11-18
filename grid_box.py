from PIL import Image, ImageDraw

im = Image.open(r"C:\Users\ESMIS 2601\.gemini\antigravity\scratch\proptii-30day-motion\assets\hero-box.jpg").convert("RGB")
draw = ImageDraw.Draw(im)
w, h = im.size
for x in range(0, w, 50):
    color = (255, 255, 0) if x % 100 == 0 else (100, 150, 200)
    draw.line([(x, 0), (x, h)], fill=color, width=1)
    if x % 100 == 0:
        draw.text((x+2, 10), str(x), fill=(255, 255, 0))
for y in range(0, h, 50):
    color = (255, 255, 0) if y % 100 == 0 else (100, 150, 200)
    draw.line([(0, y), (w, y)], fill=color, width=1)
    if y % 100 == 0:
        draw.text((10, y+2), str(y), fill=(255, 255, 0))

out = r"C:\Users\ESMIS 2601\.gemini\antigravity\brain\613858a4-7b73-4a34-bfa4-af3bec7a516a\scratch\box_grid.png"
im.save(out)
print("Saved grid")

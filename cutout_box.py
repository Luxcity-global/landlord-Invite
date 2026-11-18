from PIL import Image, ImageFilter, ImageChops
from collections import deque
import math

src_path = r"C:\Users\ESMIS 2601\.gemini\antigravity\scratch\proptii-30day-motion\assets\hero-box.jpg"
out_cutout = r"C:\Users\ESMIS 2601\.gemini\antigravity\scratch\proptii-30day-motion\assets\gift-box-cutout.png"
preview_path = r"C:\Users\ESMIS 2601\.gemini\antigravity\brain\613858a4-7b73-4a34-bfa4-af3bec7a516a\scratch\box_cutout_preview.png"

im = Image.open(src_path).convert("RGBA")
w, h = im.size
px = im.load()

# Wait: what makes a pixel "outer background" vs "gift box"?
# On the gift box:
# 1. White box walls/lid: R, G, B are fairly close (low saturation) and bright, or warm shadow where R >= B - 12.
# 2. Orange ribbon: R > B.
# 3. Blue inner rim of the box: Wait! The blue inner rim is bounded on the outside by the white rim lip or the dark navy background on the top-left / top-right!
# Let's check the exact RGB values along the top edge of the blue inner rim!
for y in range(380, 540, 10):
    row_str = f"y={y}: "
    for x in range(200, 720, 40):
        r, g, b, _ = px[x, y]
        row_str += f"({x}:{r},{g},{b}) "
    print(row_str)

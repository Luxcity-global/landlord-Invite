from PIL import Image, ImageFilter
import math

im = Image.open(r"C:\Users\ESMIS 2601\.gemini\antigravity\scratch\proptii-30day-motion\assets\hero-box.jpg").convert("RGBA")
w, h = im.size
pixels = im.load()

# Sample background color from corners and top edges
# In hero-box.jpg, the background is dark navy blue (around R=7..18, G=42..60, B=70..95)
# Wait, the box itself is white/cream, burnt orange ribbon, and a medium-blue inner rim.
# Let's inspect pixel values around the image first to see what the background gradient is!
for y in [10, 200, 400, 600, 800, 1000]:
    row_samples = [pixels[x, y][:3] for x in [10, 100, 512, 900, 1010]]
    print(f"y={y}: {row_samples}")

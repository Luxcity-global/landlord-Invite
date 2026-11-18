from PIL import Image
import os

out_dir = r"C:\Users\ESMIS 2601\.gemini\antigravity\brain\613858a4-7b73-4a34-bfa4-af3bec7a516a\scratch"
im = Image.open(os.path.join(out_dir, "v2_full.png"))
# The hero stage bottom right area
crop = im.crop((700, 500, 1300, 750))
zoom_path = os.path.join(out_dir, "bottom_zoom.png")
crop.save(zoom_path)
print("Saved zoom to:", zoom_path)

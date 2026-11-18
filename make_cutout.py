from PIL import Image, ImageDraw

src_path = r"C:\Users\ESMIS 2601\.gemini\antigravity\scratch\proptii-30day-motion\assets\hero-box.jpg"
out_cutout = r"C:\Users\ESMIS 2601\.gemini\antigravity\scratch\proptii-30day-motion\assets\gift-box-cutout.png"
preview_path = r"C:\Users\ESMIS 2601\.gemini\antigravity\brain\613858a4-7b73-4a34-bfa4-af3bec7a516a\scratch\box_cutout_preview.png"

im = Image.open(src_path).convert("RGBA")
w, h = im.size
px = im.load()

scale = 4
mask_hi = Image.new("L", (w * scale, h * scale), 0)
draw_hi = ImageDraw.Draw(mask_hi)

poly = [
    (213, 524),
    (228, 529),
    (230, 495),
    (433, 415),
    (591, 435),
    (569, 385),
    (572, 381),
    (619, 353),
    (624, 352),
    (760, 429),
    (934, 701),
    (933, 706),
    (883, 744),
    (876, 744),
    (746, 646),
    (746, 714),
    (544, 833),
    (532, 834),
    (224, 754),
    (220, 749),
    (213, 524),
]

poly_scaled = [(x * scale, y * scale) for (x, y) in poly]
draw_hi.polygon(poly_scaled, fill=255)
mask = mask_hi.resize((w, h), Image.Resampling.LANCZOS)

mask_px = mask.load()
out_im = Image.new("RGBA", (w, h), (0, 0, 0, 0))
out_px = out_im.load()

for y in range(h):
    for x in range(w):
        r, g, b, _ = px[x, y]
        a = mask_px[x, y]
        if a > 0:
            out_px[x, y] = (r, g, b, a)

bbox = out_im.getbbox()
pad = 8
crop_box = (max(0, bbox[0] - pad), max(0, bbox[1] - pad), min(w, bbox[2] + pad), min(h, bbox[3] + pad))
cropped = out_im.crop(crop_box)
cropped.save(out_cutout)

bg = Image.new("RGBA", cropped.size, (234, 244, 253, 255))
bg.alpha_composite(cropped)
bg.save(preview_path)
print("Saved perfected cutout:", cropped.size)

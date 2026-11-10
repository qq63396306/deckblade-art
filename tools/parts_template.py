# The parts template: one cell per part, the part upright (or, for a foot and a weapon, pointing right), on a grey
# mannequin of the game skeleton's own size at 64 px tall, with its pivot (red) and its end (blue).
# python -I parts_template.py <out dir>   (writes parts-template.png at 1x and 8x, and parts.json)
import sys, json, math
from PIL import Image, ImageDraw
out = sys.argv[1]
# name: cell w, h; pivot and end in the cell; mannequin radii at pivot and at end; joints it spans in the skeleton
PARTS = [
  ("head",     22, 22, (10, 17), (10, 6),  4.6, 5.0, "neck",      "crown"),
  ("torso",    26, 34, (13, 27), (13, 9),  5.0, 6.0, "pelvis",    "neck"),
  ("upperArm", 14, 24, (7, 5),   (7, 17),  3.4, 2.6, "shoulder",  "elbow"),
  ("foreArm",  14, 24, (7, 5),   (7, 16),  2.6, 3.0, "elbow",     "hand"),
  ("thigh",    18, 28, (9, 7),   (9, 21),  5.2, 3.6, "hip",       "knee"),
  ("shin",     16, 26, (8, 5),   (8, 18),  3.6, 2.4, "knee",      "ankle"),
  ("foot",     18, 12, (5, 4),   (12, 6),  2.6, 2.2, "ankle",     "toe"),
  ("cape",     30, 46, (15, 7),  (15, 35), 5.0, 9.0, "neck",      "pelvis"),
  ("sword",    62, 18, (7, 9),   (54, 9),  2.0, 3.6, "hand",      "tip"),
]
GAP = 4
# a row each: body; limbs; cape and weapon
ROWS = [["head", "torso", "upperArm", "foreArm"], ["thigh", "shin", "foot"], ["cape", "sword"]]
spec, x, y, rects = {}, 0, 0, {}
by = {p[0]: p for p in PARTS}
W = H = 0; yy = GAP
for row in ROWS:
  xx, rh = GAP, 0
  for n in row:
    _, w, h, *_ = by[n]
    rects[n] = (xx, yy, w, h); xx += w + GAP; rh = max(rh, h)
  W = max(W, xx); yy += rh + GAP
H = yy
sheet = Image.new("RGBA", (W, H), (0, 0, 0, 0)); d = ImageDraw.Draw(sheet)
for n, w, h, pv, en, r0, r1, a, b in PARTS:
  X, Y, _, _ = rects[n]
  d.rectangle([X - 1, Y - 1, X + w, Y + h], outline=(70, 70, 86, 255))
  # the mannequin: a capsule from pivot to end, the radii given (the foot a wedge, the head a ball, the sword a bar)
  steps = 40
  for i in range(steps + 1):
    u = i / steps; cx = X + pv[0] + (en[0] - pv[0]) * u; cy = Y + pv[1] + (en[1] - pv[1]) * u; r = r0 + (r1 - r0) * u
    d.ellipse([cx - r, cy - r, cx + r, cy + r], fill=(118, 118, 132, 255))
  d.point((X + pv[0], Y + pv[1]), fill=(255, 40, 40, 255)); d.point((X + en[0], Y + en[1]), fill=(40, 120, 255, 255))
  spec[n] = {"rect": [X, Y, w, h], "pivot": list(pv), "end": list(en), "from": a, "to": b}
sheet.save(f"{out}/parts-template.png")
big = sheet.resize((W * 8, H * 8), Image.NEAREST); lab = Image.new("RGBA", big.size, (30, 30, 38, 255)); lab.alpha_composite(big); dl = ImageDraw.Draw(lab)
for n, (X, Y, w, h) in rects.items(): dl.text((X * 8 + 6, Y * 8 + 4), n, fill=(255, 230, 160, 255))
lab.save(f"{out}/parts-template-labelled.png")
sheet.resize((W * 8, H * 8), Image.NEAREST).save(f"{out}/parts-template-8x.png")
json.dump({"scale": "native px; the 8x sheet is the same at 8 x 8 blocks", "size": [W, H], "parts": spec}, open(f"{out}/parts.json", "w"), indent=1)
print(W, H)

# Put a parts sheet (in the layout of parts/parts.json) on real move poses of the game's skeleton, to see it move.
# python -I assemble.py <parts sheet.png> <parts.json> <poses.json> <out.png>
# The far arm and leg use the same parts, darker and behind. 62 px from sole to crown, like the standing sprites.
import sys, json, math
from PIL import Image, ImageDraw
sheet_f, spec_f, poses_f, out_f = sys.argv[1:5]
sheet = Image.open(sheet_f).convert("RGBA")
if sheet.width > 400: sheet = sheet.resize((sheet.width // 8, sheet.height // 8), Image.NEAREST)
spec = json.load(open(spec_f))["parts"]; poses = json.load(open(poses_f))
K = 62 / 37.5; INK = (14, 12, 20, 255); CW, CH = 170, 120
parts = {}
for n, s in spec.items():
  X, Y, w, h = s["rect"]; px = sheet.load()
  pix = {(x, y): px[X + x, Y + y] for y in range(h) for x in range(w) if px[X + x, Y + y][3] > 127}
  parts[n] = (pix, s["pivot"], s["end"], s["from"], s["to"])
def joint(J, name, side):
  for cand in (name + side, name):
    if cand in J: return cand
  return name
def place(cp, pix, pv, en, ta, tb, dark):
  v = (en[0] - pv[0], en[1] - pv[1]); w = (tb[0] - ta[0], tb[1] - ta[1])
  ls, lt = math.hypot(*v) or 1e-6, math.hypot(*w) or 1e-6
  s = max(0.8, min(1.2, lt / ls)); th = math.atan2(w[1], w[0]) - math.atan2(v[1], v[0])
  ux, uy = v[0] / ls, v[1] / ls; c, si = math.cos(-th), math.sin(-th); cf, sf = math.cos(th), math.sin(th)
  fwd = []
  for (x, y) in pix:
    rx, ry = x + 0.5 - pv[0], y + 0.5 - pv[1]; al, pe = (rx * ux + ry * uy) * s, -rx * uy + ry * ux
    qx, qy = al * ux - pe * uy, al * uy + pe * ux; fwd.append((ta[0] + qx * cf - qy * sf, ta[1] + qx * sf + qy * cf))
  if not fwd: return
  layer = {}
  for dy in range(max(0, int(min(p[1] for p in fwd)) - 1), min(CH, int(max(p[1] for p in fwd)) + 2)):
    for dx in range(max(0, int(min(p[0] for p in fwd)) - 1), min(CW, int(max(p[0] for p in fwd)) + 2)):
      rx, ry = dx + 0.5 - ta[0], dy + 0.5 - ta[1]; qx, qy = rx * c - ry * si, rx * si + ry * c
      al, pe = (qx * ux + qy * uy) / s, -qx * uy + qy * ux
      src = (math.floor(pv[0] + al * ux - pe * uy), math.floor(pv[1] + al * uy + pe * ux))
      if src in pix:
        col = pix[src]; layer[(dx, dy)] = tuple(int(ch * 0.72) for ch in col[:3]) + (255,) if dark else col
  for (x, y) in list(layer):
    for ex, ey in ((1,0),(-1,0),(0,1),(0,-1)):
      q = (x + ex, y + ey)
      if q not in layer and 0 <= q[0] < CW and 0 <= q[1] < CH: cp[q] = INK
  for q, col in layer.items(): cp[q] = col
def frame(fr):
  J = fr["joints"]; ox, oy = CW // 2, CH - 10
  T = {k: (ox + v[0] * K, oy + (v[1] + fr.get("y", 0)) * K) for k, v in J.items()}; Z = {k: v[2] for k, v in J.items()}
  sa, wl = fr.get("sa", 0), fr.get("wl", 1); sp = spec["sword"]; Ls = math.dist(sp["pivot"], sp["end"])
  T["tip"] = (T["handN"][0] + math.cos(sa) * wl * Ls, T["handN"][1] + math.sin(sa) * wl * Ls); Z["tip"] = Z["handN"] + 0.2
  jobs = [(-99, "cape", "", False)]
  for n in ("head", "torso"): jobs.append((0, n, "", False))
  for n in ("upperArm", "foreArm", "thigh", "shin", "foot"):
    for side in ("N", "F"):
      a, b = joint(J, parts[n][3], side), joint(J, parts[n][4], side)
      jobs.append(((Z[a] + Z[b]) / 2, n, side, side == "F"))
  if fr.get("weapon"): jobs.append((Z["handN"] + 0.3, "sword", "N", False))
  img = Image.new("RGBA", (CW, CH), (0, 0, 0, 0)); cp = img.load()
  for z, n, side, dark in sorted(jobs, key=lambda j: j[0]):
    pix, pv, en, a, b = parts[n]
    if not pix: continue
    a, b = (joint(J, a, side), joint(J, b, side)) if b != "tip" else ("handN", "tip")
    place(cp, pix, pv, en, T[a], T[b], dark)
  return img.transpose(Image.FLIP_LEFT_RIGHT) if fr.get("face", 1) == -1 else img
rows = [(k, v) for k, v in poses.items()]
cols = max(len(v) for _, v in rows); k = 3
out = Image.new("RGBA", (cols * CW * k, len(rows) * (CH * k + 18)), (58, 62, 74, 255)); d = ImageDraw.Draw(out)
for r, (name, frames) in enumerate(rows):
  d.text((6, r * (CH * k + 18) + 3), name, fill=(255, 230, 160, 255))
  for i, fr in enumerate(frames): out.alpha_composite(frame(fr).resize((CW * k, CH * k), Image.NEAREST), (i * CW * k, r * (CH * k + 18) + 18))
out.save(out_f); print(out.size)

import math, sys
from PIL import Image, ImageDraw, ImageFilter
W, H = 2560, 1600
stops = [(0.0, (34, 10, 58)), (0.32, (92, 28, 112)), (0.62, (214, 66, 128)), (0.86, (246, 128, 104)), (1.0, (250, 170, 96))]
def color(t):
    for (a, ca), (b, cb) in zip(stops, stops[1:]):
        if t <= b:
            k = (t - a) / (b - a)
            return tuple(round(x + (y - x) * k) for x, y in zip(ca, cb))
    return stops[-1][1]
sky = Image.new("RGB", (W, H))
d = ImageDraw.Draw(sky)
for y in range(H):
    d.line([(0, y), (W, y)], fill=color(y / (H - 1)))
# soft sun glow near the bottom center
glow = Image.new("L", (W, H), 0)
ImageDraw.Draw(glow).ellipse((W*0.30, H*0.70, W*0.70, H*1.35), fill=110)
glow = glow.filter(ImageFilter.GaussianBlur(160))
sky = Image.composite(Image.new("RGB", (W, H), (255, 196, 120)), sky, glow)

palms = Image.new("RGBA", (W, H), (0, 0, 0, 0))
p = ImageDraw.Draw(palms)
INK = (22, 6, 36, 215)
def frond(x0, y0, angle, length, droop, width=26, leaves=26):
    pts = []
    for i in range(41):
        t = i / 40
        a = math.radians(angle) + droop * t * t
        pts.append((x0 + math.cos(a) * length * t, y0 + math.sin(a) * length * t))
    for i in range(len(pts) - 1):
        t = i / 40
        w = max(2, width * (1 - t))
        p.line([pts[i], pts[i + 1]], fill=INK, width=int(w * 0.35) + 2)
    for k in range(1, leaves):
        t = k / leaves
        i = int(t * 40)
        (x, y), (nx, ny) = pts[i], pts[min(i + 1, 40)]
        dir_ = math.atan2(ny - y, nx - x)
        size = length * 0.28 * math.sin(math.pi * min(1, t * 1.15)) + 8
        for side in (-1, 1):
            a = dir_ + side * math.radians(62) + droop * 0.15
            tip = (x + math.cos(a) * size, y + math.sin(a) * size + size * 0.35)
            b1 = (x + math.cos(dir_) * 10, y + math.sin(dir_) * 10)
            p.polygon([(x, y), tip, b1], fill=INK)
def crown(cx, cy, specs):
    for angle, length, droop in specs:
        frond(cx, cy, angle, length, droop)
crown(-60, -40, [(10, 760, 0.9), (35, 820, 1.1), (60, 700, 1.0), (85, 560, 0.6), (-5, 600, 0.7)])
crown(W + 60, -40, [(170, 760, -0.9), (145, 820, -1.1), (120, 700, -1.0), (95, 560, -0.6), (185, 600, -0.7)])
crown(-80, H + 60, [(-20, 640, -0.5), (-45, 560, -0.3), (-70, 420, -0.2)])
crown(W + 80, H + 60, [(200, 640, 0.5), (225, 560, 0.3), (250, 420, 0.2)])
palms = palms.filter(ImageFilter.GaussianBlur(1.2))
out = Image.alpha_composite(sky.convert("RGBA"), palms).convert("RGB")
out.save(sys.argv[1], optimize=True)
print(out.size)

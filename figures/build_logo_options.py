"""Build five logo alternatives for ZwiCoat into site/public/logo-options/.

Every wordmark is converted to outlines with fontTools, so no SVG depends on
a font being installed. Shapes use only the brand blues (#0A68A6, #08507F,
#4FA3D8) and white: no gradients, no shadows.

  A  Public Sans Bold, the current two-swoosh idea rebalanced
  B  Public Sans SemiBold, one wave that ripples under the "w"
  C  Manrope ExtraBold, "Zwi" blue and "Coat" deep blue over a tapering rule
  D  Coated-device cross-section mark plus Public Sans Bold; square icon too
  E  Bahnschrift SemiBold, lowercase "zwicoat", the dot of the i is a drop

PNGs (1400 px wide, transparent) are rendered with sharp from the site's
node_modules, so run this from anywhere with Node available:
    python figures/build_logo_options.py

The site fonts ship as .woff2. If the Python brotli module is missing, the
decompression is handed to Node's built-in zlib instead.
"""
import json
import math
import subprocess
from pathlib import Path

from fontTools.ttLib import TTFont
import fontTools.ttLib.woff2 as _woff2
from fontTools.varLib import instancer
from fontTools.pens.recordingPen import RecordingPen
from fontTools.pens.transformPen import TransformPen
from fontTools.pens.svgPathPen import SVGPathPen
from fontTools.pens.boundsPen import BoundsPen

ROOT = Path(__file__).resolve().parent.parent
SITE = ROOT / "site"
OUT = SITE / "public" / "logo-options"
FS = SITE / "node_modules" / "@fontsource-variable"
PUBLIC_SANS = FS / "public-sans" / "files" / "public-sans-latin-wght-normal.woff2"
MANROPE = FS / "manrope" / "files" / "manrope-latin-wght-normal.woff2"
BAHNSCHRIFT = Path(r"C:\Windows\Fonts\bahnschrift.ttf")

BLUE = "#0A68A6"
DEEP = "#08507F"
MID = "#4FA3D8"
WHITE = "#FFFFFF"

# --------------------------------------------------------------- fonts ----
if not _woff2.haveBrotli:
    class _NodeBrotli:
        """Stand-in for the brotli module: decompress with Node's zlib."""
        @staticmethod
        def decompress(data):
            js = ("process.stdout.write(require('zlib')"
                  ".brotliDecompressSync(require('fs').readFileSync(0)))")
            return subprocess.run(["node", "-e", js], input=data,
                                  capture_output=True, check=True).stdout
    _woff2.brotli = _NodeBrotli
    _woff2.haveBrotli = True


def load(path, **axes):
    f = TTFont(str(path))
    if axes and "fvar" in f:
        instancer.instantiateVariableFont(f, axes, inplace=True)
    return f


def kern_fn(font):
    """Pair kerning from the GPOS 'kern' feature (PairPos formats 1 and 2)."""
    if "GPOS" not in font:
        return lambda a, b: 0
    t = font["GPOS"].table
    idx = set()
    for fr in t.FeatureList.FeatureRecord:
        if fr.FeatureTag == "kern":
            idx.update(fr.Feature.LookupListIndex)
    subs = []
    for li in sorted(idx):
        lk = t.LookupList.Lookup[li]
        group = []
        for st in lk.SubTable:
            if lk.LookupType == 9:
                if st.ExtensionLookupType != 2:
                    continue
                st = st.ExtSubTable
            elif lk.LookupType != 2:
                continue
            group.append(st)
        subs.append(group)

    def xadv(v):
        return getattr(v, "XAdvance", 0) or 0 if v is not None else 0

    def kern(a, b):
        total = 0
        for group in subs:
            for st in group:
                cov = st.Coverage.glyphs
                if a not in cov:
                    continue
                if st.Format == 1:
                    ps = st.PairSet[cov.index(a)]
                    hit = [r for r in ps.PairValueRecord if r.SecondGlyph == b]
                    if hit:
                        total += xadv(hit[0].Value1)
                        break
                elif st.Format == 2:
                    c1 = st.ClassDef1.classDefs.get(a, 0)
                    c2 = st.ClassDef2.classDefs.get(b, 0)
                    total += xadv(st.Class1Record[c1].Class2Record[c2].Value1)
                    break
        return total
    return kern


def fmt(v):
    s = f"{v:.2f}".rstrip("0").rstrip(".")
    return "0" if s in ("-0", "") else s


def d_of(rec):
    pen = SVGPathPen(None, ntos=fmt)
    rec.replay(pen)
    return pen.getCommands()


def bounds_of(rec):
    bp = BoundsPen(None)
    rec.replay(bp)
    return bp.bounds


def layout(font, text, track=0.0, glyph_names=None):
    """Lay out text with cap height = 100 units, baseline at y = 0 (SVG y down).

    Returns per-glyph RecordingPens (already in SVG coordinates, first ink at
    x = 0) and their ink boxes.
    """
    gs = font.getGlyphSet()
    cmap = font.getBestCmap()
    upm = font["head"].unitsPerEm
    cap = font["OS/2"].sCapHeight or 0.7 * upm
    S = 100.0 / cap
    kern = kern_fn(font)
    names = glyph_names or [cmap[ord(c)] for c in text]
    # left side bearing of the first glyph
    bp = BoundsPen(gs)
    gs[names[0]].draw(bp)
    lsb = bp.bounds[0]
    x = -lsb
    recs, boxes = [], []
    for i, gn in enumerate(names):
        rec = RecordingPen()
        tp = TransformPen(rec, (S, 0, 0, -S, x * S, 0))
        gs[gn].draw(tp)
        recs.append(rec)
        boxes.append(bounds_of(rec))
        x += gs[gn].width + track * upm
        if i + 1 < len(names):
            x += kern(gn, names[i + 1])
    return recs, boxes


def merge(recs):
    out = RecordingPen()
    for r in recs:
        out.value.extend(r.value)
    return out


def union(boxes):
    boxes = [b for b in boxes if b]
    return (min(b[0] for b in boxes), min(b[1] for b in boxes),
            max(b[2] for b in boxes), max(b[3] for b in boxes))


# -------------------------------------------------------------- shapes ----
K = 0.5522847498  # cubic circle constant


def circle(pen, cx, cy, r, clockwise=True):
    k = K * r
    pen.moveTo((cx + r, cy))
    if clockwise:  # clockwise on screen (SVG y down)
        pen.curveTo((cx + r, cy + k), (cx + k, cy + r), (cx, cy + r))
        pen.curveTo((cx - k, cy + r), (cx - r, cy + k), (cx - r, cy))
        pen.curveTo((cx - r, cy - k), (cx - k, cy - r), (cx, cy - r))
        pen.curveTo((cx + k, cy - r), (cx + r, cy - k), (cx + r, cy))
    else:
        pen.curveTo((cx + r, cy - k), (cx + k, cy - r), (cx, cy - r))
        pen.curveTo((cx - k, cy - r), (cx - r, cy - k), (cx - r, cy))
        pen.curveTo((cx - r, cy + k), (cx - k, cy + r), (cx, cy + r))
        pen.curveTo((cx + k, cy + r), (cx + r, cy + k), (cx + r, cy))
    pen.closePath()


def ring(cx, cy, r_out, r_in):
    rec = RecordingPen()
    circle(rec, cx, cy, r_out, True)
    circle(rec, cx, cy, r_in, False)
    return rec


def disc(cx, cy, r):
    rec = RecordingPen()
    circle(rec, cx, cy, r)
    return rec


def path_from(spec, sx=1.0, sy=1.0, dx=0.0, dy=0.0):
    """A closed shape from a list of cubic segments: [p0, (c1, c2, p), ...]."""
    tr = lambda p: (p[0] * sx + dx, p[1] * sy + dy)
    rec = RecordingPen()
    rec.moveTo(tr(spec[0]))
    for c1, c2, p in spec[1:]:
        rec.curveTo(tr(c1), tr(c2), tr(p))
    rec.closePath()
    return rec


def ribbon(xs, ys, half):
    """A filled ribbon around a centreline, half-thickness per sample, with
    Catmull-Rom smoothing on both edges. Ends taper to the given half value."""
    n = len(xs)
    # normals
    top, bot = [], []
    for i in range(n):
        a = max(i - 1, 0)
        b = min(i + 1, n - 1)
        tx, ty = xs[b] - xs[a], ys[b] - ys[a]
        L = math.hypot(tx, ty) or 1
        nx, ny = -ty / L, tx / L
        top.append((xs[i] + nx * half[i], ys[i] + ny * half[i]))
        bot.append((xs[i] - nx * half[i], ys[i] - ny * half[i]))
    rec = RecordingPen()

    def cr(points, first):
        if first:
            rec.moveTo(points[0])
        else:
            rec.lineTo(points[0])
        for i in range(len(points) - 1):
            p0 = points[max(i - 1, 0)]
            p1 = points[i]
            p2 = points[i + 1]
            p3 = points[min(i + 2, len(points) - 1)]
            c1 = (p1[0] + (p2[0] - p0[0]) / 6, p1[1] + (p2[1] - p0[1]) / 6)
            c2 = (p2[0] - (p3[0] - p1[0]) / 6, p2[1] - (p3[1] - p1[1]) / 6)
            rec.curveTo(c1, c2, p2)

    cr(top, True)
    cr(bot[::-1], False)
    rec.closePath()
    return rec


def drop(cx, cy, r, h):
    """Water drop: round bottom (centre cx, cy, radius r), point h above cy."""
    k = K * r
    tip = (cx, cy - h)
    rec = RecordingPen()
    rec.moveTo(tip)
    rec.curveTo((cx + 0.18 * r, cy - h + 0.55 * r), (cx + r, cy - 0.95 * r), (cx + r, cy))
    rec.curveTo((cx + r, cy + k), (cx + k, cy + r), (cx, cy + r))
    rec.curveTo((cx - k, cy + r), (cx - r, cy + k), (cx - r, cy))
    rec.curveTo((cx - r, cy - 0.95 * r), (cx - 0.18 * r, cy - h + 0.55 * r), tip)
    rec.closePath()
    return rec


# ----------------------------------------------------------------- svg ----
def write_svg(name, label, layers, pad=4, box=None, png_width=1400):
    """layers: list of (RecordingPen, fill[, extra attrs])."""
    if box is None:
        box = union([bounds_of(l[0]) for l in layers])
    x0, y0, x1, y1 = box
    vb = (x0 - pad, y0 - pad, (x1 - x0) + 2 * pad, (y1 - y0) + 2 * pad)
    body = []
    for layer in layers:
        rec, fill = layer[0], layer[1]
        extra = layer[2] if len(layer) > 2 else ""
        body.append(f'  <path fill="{fill}"{extra} d="{d_of(rec)}"/>')
    svg = (f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="{" ".join(fmt(v) for v in vb)}" '
           f'role="img" aria-label="{label}">\n  <title>{label}</title>\n'
           + "\n".join(body) + "\n</svg>\n")
    p = OUT / f"{name}.svg"
    p.write_text(svg, encoding="utf-8")
    jobs.append({"svg": str(p), "png": str(OUT / f"{name}.png"),
                 "w": png_width, "vbw": vb[2]})
    print(f"{name}.svg  aspect {vb[2] / vb[3]:.3f}")
    return vb


jobs = []
OUT.mkdir(parents=True, exist_ok=True)

ps_bold = load(PUBLIC_SANS, wght=700)
ps_semi = load(PUBLIC_SANS, wght=600)
manrope = load(MANROPE, wght=800)
bahn = load(BAHNSCHRIFT, wght=600, wdth=100)

# ------------------------------------------------------------ option A ----
# Current idea, rebalanced: a clearly visible light-blue upper swoosh that
# rises to the right, and a thinner long wave close under the baseline.
recs, boxes = layout(ps_bold, "ZwiCoat", track=0.01)
text = merge(recs)
W = union(boxes)[2]
k = W / 700.0
G = 16  # baseline to the top of the swoosh box


def taper(t, a=0.5):
    """0 at both ends, 1 in the middle; a < 1 gives fuller shoulders."""
    return math.sin(math.pi * min(max(t, 0.0), 1.0)) ** a


# upper swoosh: light blue, sweeps up to the right, thick enough to read
ux = [200 + i * 500 / 40 for i in range(41)]
uy = [30 - 34 * ((x - 200) / 500) ** 2.2 for x in ux]
uh = [10.0 * taper((x - 200) / 500, 0.55) ** 1.0 * (1 - 0.35 * (x - 200) / 500) for x in ux]
upper = ribbon([x * k for x in ux], [y * k + G for y in uy], [h * k for h in uh])
# long wave: thin, full width, a soft crest on the left and a long low tail
xs = [i * 700 / 60 for i in range(61)]
ys = [60 - 9 * math.sin(2 * math.pi * (x / 700) * 0.85 + 0.25) for x in xs]
half = [4.6 * taper(x / 700, 0.45) for x in xs]
wave = ribbon([x * k for x in xs], [y * k + G for y in ys], [h * k for h in half])
write_svg("option-a", "ZwiCoat", [(text, BLUE), (upper, MID), (wave, BLUE)])

# ------------------------------------------------------------ option B ----
# One wave in one colour. Flat under the word, it ripples under the "w" with
# its two troughs under the two points of the letter, like a water film.
recs, boxes = layout(ps_semi, "ZwiCoat", track=0.01)
text = merge(recs)
W = union(boxes)[2]
wx0, _, wx1, _ = boxes[1]
ww = wx1 - wx0
v1, v2 = wx0 + 0.25 * ww, wx0 + 0.75 * ww  # under the two bottom points
P = v2 - v1
base = 24
amp = 7.0
lo, hi = v1 - 1.25 * P, v2 + 1.25 * P
n = int(W / (P / 16)) + 1
xs = [W * i / n for i in range(n + 1)]


def env(x):
    if x <= lo or x >= hi:
        return 0.0
    return math.sin(math.pi * (x - lo) / (hi - lo)) ** 2


ys = [base + amp * env(x) * math.cos(2 * math.pi * (x - v1) / P) for x in xs]
half = []
for x in xs:
    t = x / W
    half.append(4.0 * min(1.0, t / 0.06) ** 0.6 * min(1.0, (1 - t) / 0.2) ** 0.7 + 0.2)
wave = ribbon(xs, ys, half)
write_svg("option-b", "ZwiCoat", [(text, BLUE), (wave, BLUE)])

# ------------------------------------------------------------ option C ----
# Two blues, no swoosh. A thin rule under the word is the coating: full
# weight at the left, tapering to a point past the "t" (a taper, not a gradient).
recs, boxes = layout(manrope, "ZwiCoat", track=0.0)
zwi, coat = merge(recs[:3]), merge(recs[3:])
W = union(boxes)[2]
g, t0 = 18, 7.0
rule = RecordingPen()
rule.moveTo((0, g))
rule.lineTo((W * 0.45, g))
rule.curveTo((W * 0.75, g), (W * 0.95, g + t0 * 0.45), (W * 1.04, g + t0 * 0.5))
rule.curveTo((W * 0.95, g + t0 * 0.55), (W * 0.75, g + t0), (W * 0.45, g + t0))
rule.lineTo((0, g + t0))
rule.closePath()
write_svg("option-c", "ZwiCoat", [(zwi, BLUE), (coat, DEEP), (rule, BLUE)])

# ------------------------------------------------------------ option D ----
# A cross-section of a coated device: a solid core (the device) inside a thin
# ring (the coating), then the wordmark. Plus a square icon for the favicon.
recs, boxes = layout(ps_bold, "ZwiCoat", track=0.01)
R = 64           # outer radius of the mark, cap height is 100
cx, cy = R, -50  # centred on the cap height
gap_after = 34
dx = 2 * R + gap_after
text = RecordingPen()
tp = TransformPen(text, (1, 0, 0, 1, dx, 0))
merge(recs).replay(tp)
ring_w, gap_w = 8, 8
mark_ring = ring(cx, cy, R, R - ring_w)
mark_core = disc(cx, cy, R - ring_w - gap_w)
write_svg("option-d", "ZwiCoat",
          [(mark_ring, BLUE, ' fill-rule="evenodd"'), (mark_core, BLUE), (text, BLUE)])

# square icon: white mark on a brand-blue square, 64 units
sq = RecordingPen()
sq.moveTo((0, 0)); sq.lineTo((64, 0)); sq.lineTo((64, 64)); sq.lineTo((0, 64)); sq.closePath()
ir, irw, igw = 25, 4, 4.5
icon_ring = ring(32, 32, ir, ir - irw)
icon_core = disc(32, 32, ir - irw - igw)
write_svg("option-d-icon", "ZwiCoat",
          [(sq, BLUE), (icon_ring, WHITE, ' fill-rule="evenodd"'), (icon_core, WHITE)],
          pad=0, box=(0, 0, 64, 64), png_width=512)
jobs.append({"svg": str(OUT / "option-d-icon.svg"), "png": str(OUT / "option-d-favicon-64.png"),
             "w": 64, "vbw": 64})

# ------------------------------------------------------------ option E ----
# Lowercase Bahnschrift SemiBold; the dot of the "i" becomes a water drop.
cmap = bahn.getBestCmap()
names = [cmap[ord(c)] for c in "zwicoat"]
i_recs, _ = layout(bahn, "zwicoat", track=0.02, glyph_names=names)
# find the dot of the i: the contour with the highest top in glyph 2
contours, cur = [], []
for op, args in i_recs[2].value:
    cur.append((op, args))
    if op in ("closePath", "endPath"):
        contours.append(cur)
        cur = []


def cbox(c):
    r = RecordingPen()
    r.value = c
    return bounds_of(r)


dot = min(contours, key=lambda c: cbox(c)[1])
dx0, dy0, dx1, dy1 = cbox(dot)
stem = RecordingPen()
stem.value = [op for c in contours if c is not dot for op in c]
i_recs[2] = stem
text = merge(i_recs)
stem_top = min(cbox(c)[1] for c in contours if c is not dot)
r = (dx1 - dx0) * 0.6
dcx = (dx0 + dx1) / 2
dcy = dy1 + 0.25 * (stem_top - dy1) - r  # bottom of the drop just below the old dot
wdrop = drop(dcx, dcy, r, r * 1.95)
write_svg("option-e", "zwicoat", [(text, BLUE), (wdrop, MID)])

# ----------------------------------------------------------------- png ----
JS = r"""
const sharp = require('sharp');
const jobs = JSON.parse(require('fs').readFileSync(0, 'utf8'));
(async () => {
  for (const j of jobs) {
    const density = Math.min(100000, 72 * j.w / j.vbw);
    await sharp(j.svg, { density }).resize({ width: j.w }).png().toFile(j.png);
    console.log('png', require('path').basename(j.png));
  }
})().catch((e) => { console.error(e); process.exit(1); });
"""
subprocess.run(["node", "-e", JS], input=json.dumps(jobs).encode(), cwd=str(SITE), check=True)

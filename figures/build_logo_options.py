"""Build ten logo alternatives for ZwiCoat into site/public/logo-options/.

Every wordmark is converted to outlines with fontTools, so no SVG depends on
a font being installed. Shapes use only the brand blues (#0A68A6, #08507F,
#4FA3D8) and white: no gradients, no shadows.

Round two (owner, 2026-11-02): "spacing between letters is too large in every
single one". Every wordmark now uses the font's own pair kerning (GPOS 'kern')
with no added tracking, and the Bold and heavier wordmarks are tightened a
further 2 percent of the em (optical tightening). The values are in TRACK.

  A  Public Sans Bold, the current two-swoosh idea rebalanced
  B  Public Sans SemiBold, one wave that ripples under the "w"
  C  Manrope ExtraBold, "Zwi" blue and "Coat" deep blue over a tapering rule
  D  Coated-device cross-section mark plus Public Sans Bold; square icon too
  E  Bahnschrift SemiBold, lowercase "zwicoat", the dot of the i is a drop
  F  Hybrid of A and B: B's single tapered wave in deep blue plus a short
     light-blue swoosh from A rising at the right
  G  A's two swooshes under Public Sans SemiBold, "Coat" in deep blue
  H  The "o" of "Coat" drawn as a coated cross-section (core, gap, ring)
  I  Stacked "Zwi" over "Coat" for square uses, plus a wide version
  J  Lowercase "zwicoat"; a thin line rises through the counter of the "o"
     into one short wave at the right

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

# ------------------------------------------------------------ tracking ----
# Added tracking in em, on top of the font's own pair kerning. Round one used
# +0.01 (A, B, D) and +0.02 (E); the owner found every option too loose.
# Every wordmark here is a display weight (SemiBold to ExtraBold), so each
# gets the same optical tightening: -0.02 em. Zero added tracking left B and
# E (SemiBold) visibly looser than the Bold ones, which is the complaint.
TIGHT = -0.02
TRACK = {
    "A": TIGHT,  # Public Sans Bold
    "B": TIGHT,  # Public Sans SemiBold
    "C": TIGHT,  # Manrope ExtraBold
    "D": TIGHT,  # Public Sans Bold
    "E": TIGHT,  # Bahnschrift SemiBold
    "F": TIGHT,  # Public Sans Bold
    "G": TIGHT,  # Public Sans SemiBold, asked for tight
    "H": TIGHT,  # Public Sans Bold
    "I": TIGHT,  # Public Sans Bold
    "J": TIGHT,  # Public Sans Bold, lowercase
}


def taper(t, a=0.5):
    """0 at both ends, 1 in the middle; a < 1 gives fuller shoulders."""
    return math.sin(math.pi * min(max(t, 0.0), 1.0)) ** a


def moved(rec, dx=0.0, dy=0.0, s=1.0):
    out = RecordingPen()
    rec.replay(TransformPen(out, (s, 0, 0, s, dx, dy)))
    return out


def a_swooshes(W, G=16):
    """Option A's pair: a light upper swoosh rising to the right and a long
    thin wave, laid out on a 700-unit grid and scaled to the word width W."""
    k = W / 700.0
    ux = [200 + i * 500 / 40 for i in range(41)]
    uy = [30 - 34 * ((x - 200) / 500) ** 2.2 for x in ux]
    uh = [10.0 * taper((x - 200) / 500, 0.55) * (1 - 0.35 * (x - 200) / 500) for x in ux]
    upper = ribbon([x * k for x in ux], [y * k + G for y in uy], [h * k for h in uh])
    xs = [i * 700 / 60 for i in range(61)]
    ys = [60 - 9 * math.sin(2 * math.pi * (x / 700) * 0.85 + 0.25) for x in xs]
    half = [4.6 * taper(x / 700, 0.45) for x in xs]
    wave = ribbon([x * k for x in xs], [y * k + G for y in ys], [h * k for h in half])
    return upper, wave


def short_swoosh(x0, x1, y_left, rise, thick, n=40):
    """A's upper swoosh as a free piece: from x0 to x1, centreline at y_left
    on the left, rising by `rise` at the right; fuller on the left."""
    xs = [x0 + (x1 - x0) * i / n for i in range(n + 1)]
    ts = [(x - x0) / (x1 - x0) for x in xs]
    ys = [y_left - rise * t ** 2.2 for t in ts]
    hs = [thick * taper(t, 0.55) * (1 - 0.35 * t) for t in ts]
    return ribbon(xs, ys, hs)


def b_wave(boxes, W, base=24, amp=7.0, thick=4.0):
    """Option B's single wave: flat under the word, rippling under the "w"
    (glyph 1) with its troughs under the letter's two points; tapered ends."""
    wx0, _, wx1, _ = boxes[1]
    ww = wx1 - wx0
    v1, v2 = wx0 + 0.25 * ww, wx0 + 0.75 * ww
    P = v2 - v1
    lo, hi = v1 - 1.25 * P, v2 + 1.25 * P
    n = int(W / (P / 16)) + 1
    xs = [W * i / n for i in range(n + 1)]

    def env(x):
        if x <= lo or x >= hi:
            return 0.0
        return math.sin(math.pi * (x - lo) / (hi - lo)) ** 2

    ys = [base + amp * env(x) * math.cos(2 * math.pi * (x - v1) / P) for x in xs]
    half = [thick * min(1.0, (x / W) / 0.06) ** 0.6 * min(1.0, (1 - x / W) / 0.2) ** 0.7 + 0.2
            for x in xs]
    return ribbon(xs, ys, half)


def contours_of(rec):
    out, cur = [], []
    for op, args in rec.value:
        cur.append((op, args))
        if op in ("closePath", "endPath"):
            out.append(cur)
            cur = []
    return out


def cbox(c):
    r = RecordingPen()
    r.value = c
    return bounds_of(r)


def square(size):
    sq = RecordingPen()
    sq.moveTo((0, 0)); sq.lineTo((size, 0)); sq.lineTo((size, size)); sq.lineTo((0, size))
    sq.closePath()
    return sq


def spline(pts, per=24):
    """Sample a Catmull-Rom curve through pts (a centreline for ribbon())."""
    xs, ys = [], []
    for i in range(len(pts) - 1):
        p0 = pts[max(i - 1, 0)]; p1 = pts[i]; p2 = pts[i + 1]; p3 = pts[min(i + 2, len(pts) - 1)]
        for j in range(per):
            t = j / per
            t2, t3 = t * t, t * t * t
            for arr, a in ((xs, 0), (ys, 1)):
                arr.append(0.5 * ((2 * p1[a]) + (-p0[a] + p2[a]) * t
                                  + (2 * p0[a] - 5 * p1[a] + 4 * p2[a] - p3[a]) * t2
                                  + (-p0[a] + 3 * p1[a] - 3 * p2[a] + p3[a]) * t3))
    xs.append(pts[-1][0]); ys.append(pts[-1][1])
    return xs, ys


# ------------------------------------------------------------ option A ----
# Current idea, rebalanced: a clearly visible light-blue upper swoosh that
# rises to the right, and a thinner long wave close under the baseline.
recs, boxes = layout(ps_bold, "ZwiCoat", track=TRACK["A"])
upper, wave = a_swooshes(union(boxes)[2])
write_svg("option-a", "ZwiCoat", [(merge(recs), BLUE), (upper, MID), (wave, BLUE)])

# ------------------------------------------------------------ option B ----
# One wave in one colour. Flat under the word, it ripples under the "w" with
# its two troughs under the two points of the letter, like a water film.
recs, boxes = layout(ps_semi, "ZwiCoat", track=TRACK["B"])
wave = b_wave(boxes, union(boxes)[2])
write_svg("option-b", "ZwiCoat", [(merge(recs), BLUE), (wave, BLUE)])

# ------------------------------------------------------------ option C ----
# Two blues, no swoosh. A thin rule under the word is the coating: full
# weight at the left, tapering to a point past the "t" (a taper, not a gradient).
recs, boxes = layout(manrope, "ZwiCoat", track=TRACK["C"])
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
recs, boxes = layout(ps_bold, "ZwiCoat", track=TRACK["D"])
R = 64           # outer radius of the mark, cap height is 100
cx, cy = R, -50  # centred on the cap height
gap_after = 34
text = moved(merge(recs), dx=2 * R + gap_after)
ring_w, gap_w = 8, 8
mark_ring = ring(cx, cy, R, R - ring_w)
mark_core = disc(cx, cy, R - ring_w - gap_w)
write_svg("option-d", "ZwiCoat",
          [(mark_ring, BLUE, ' fill-rule="evenodd"'), (mark_core, BLUE), (text, BLUE)])

# square icon: white mark on a brand-blue square, 64 units
ir, irw, igw = 25, 4, 4.5
icon_ring = ring(32, 32, ir, ir - irw)
icon_core = disc(32, 32, ir - irw - igw)
write_svg("option-d-icon", "ZwiCoat",
          [(square(64), BLUE), (icon_ring, WHITE, ' fill-rule="evenodd"'), (icon_core, WHITE)],
          pad=0, box=(0, 0, 64, 64), png_width=512)
jobs.append({"svg": str(OUT / "option-d-icon.svg"), "png": str(OUT / "option-d-favicon-64.png"),
             "w": 64, "vbw": 64})

# ------------------------------------------------------------ option E ----
# Lowercase Bahnschrift SemiBold; the dot of the "i" becomes a water drop.
cmap = bahn.getBestCmap()
names = [cmap[ord(c)] for c in "zwicoat"]
i_recs, _ = layout(bahn, "zwicoat", track=TRACK["E"], glyph_names=names)
contours = contours_of(i_recs[2])  # the dot is the contour with the highest top
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

# ------------------------------------------------------------ option F ----
# Hybrid of A and B. B's single tapered wave, in deep blue, sits lower; A's
# light-blue upper swoosh comes back short, under "oat", rising at the right.
recs, boxes = layout(ps_bold, "ZwiCoat", track=TRACK["F"])
W = union(boxes)[2]
wave = b_wave(boxes, W, base=38, amp=6.5, thick=4.2)
sw = short_swoosh(W * 0.56, W * 1.0, y_left=22, rise=17, thick=5.2)
write_svg("option-f", "ZwiCoat", [(merge(recs), BLUE), (sw, MID), (wave, DEEP)])

# ------------------------------------------------------------ option G ----
# A's two swooshes under a lighter wordmark: Public Sans SemiBold, "Zwi" in
# brand blue and "Coat" in deep blue.
recs, boxes = layout(ps_semi, "ZwiCoat", track=TRACK["G"])
upper, wave = a_swooshes(union(boxes)[2])
write_svg("option-g", "ZwiCoat",
          [(merge(recs[:3]), BLUE), (merge(recs[3:]), DEEP), (upper, MID), (wave, BLUE)])

# ------------------------------------------------------------ option H ----
# The "o" of "Coat" is a coated cross-section: a solid core, a thin gap and an
# outer ring, in brand blue. The rest of the word is plain deep blue.
recs, boxes = layout(ps_bold, "ZwiCoat", track=TRACK["H"])
ox0, oy0, ox1, oy1 = boxes[4]
ocx, ocy = (ox0 + ox1) / 2, (oy0 + oy1) / 2
oR = ((ox1 - ox0) + (oy1 - oy0)) / 4
stem_w = boxes[2][2] - boxes[2][0]  # the stem of the "i"
h_ring_w, h_gap_w = 0.55 * stem_w, 0.38 * stem_w


def coated_o(cx, cy, R, rw, gw):
    return ring(cx, cy, R, R - rw), disc(cx, cy, R - rw - gw)


h_ring, h_core = coated_o(ocx, ocy, oR, h_ring_w, h_gap_w)
rest = merge(recs[:4] + recs[5:])
write_svg("option-h", "ZwiCoat",
          [(rest, DEEP), (h_ring, BLUE, ' fill-rule="evenodd"'), (h_core, BLUE)])
# icon: the coated "o" alone, brand blue on transparent, same proportions
s = 30 / oR
hi_ring, hi_core = coated_o(32, 32, 30, h_ring_w * s, h_gap_w * s)
write_svg("option-h-icon", "ZwiCoat",
          [(hi_ring, BLUE, ' fill-rule="evenodd"'), (hi_core, BLUE)],
          pad=0, box=(0, 0, 64, 64), png_width=512)
jobs.append({"svg": str(OUT / "option-h-icon.svg"), "png": str(OUT / "option-h-favicon-64.png"),
             "w": 64, "vbw": 64})

# ------------------------------------------------------------ option I ----
# A compact stacked lockup for square uses: "Zwi" over "Coat", left-aligned,
# tight leading, with A's light-blue swoosh under. Plus the wide version.
LEAD = 128  # baseline to baseline, cap height is 100
zr, zb = layout(ps_bold, "Zwi", track=TRACK["I"])
cr, cb = layout(ps_bold, "Coat", track=TRACK["I"])
zwi = merge(zr)
coat = moved(merge(cr), dy=LEAD)
SW = max(union(zb)[2], union(cb)[2])
i_sw = short_swoosh(SW * 0.08, SW * 1.0, y_left=LEAD + 24, rise=14, thick=6.5)
stack = [(zwi, BLUE), (coat, BLUE), (i_sw, MID)]
write_svg("option-i", "ZwiCoat", stack)
# wide: the same word on one line, the same swoosh scaled to the word
recs, boxes = layout(ps_bold, "ZwiCoat", track=TRACK["I"])
W = union(boxes)[2]
iw_sw = short_swoosh(W * 0.08, W * 1.0, y_left=24, rise=14, thick=6.5)
write_svg("option-i-wide", "ZwiCoat", [(merge(recs), BLUE), (iw_sw, MID)])
# icon: the stacked lockup in white on a brand-blue square
sb = union([bounds_of(l[0]) for l in stack])
pad_i = 9
fit = (64 - 2 * pad_i) / max(sb[2] - sb[0], sb[3] - sb[1])
offx = (64 - (sb[2] - sb[0]) * fit) / 2 - sb[0] * fit
offy = (64 - (sb[3] - sb[1]) * fit) / 2 - sb[1] * fit
write_svg("option-i-icon", "ZwiCoat",
          [(square(64), BLUE),
           (moved(zwi, offx, offy, fit), WHITE), (moved(coat, offx, offy, fit), WHITE),
           (moved(i_sw, offx, offy, fit), MID)],
          pad=0, box=(0, 0, 64, 64), png_width=512)
jobs.append({"svg": str(OUT / "option-i-icon.svg"), "png": str(OUT / "option-i-favicon-64.png"),
             "w": 64, "vbw": 64})

# ------------------------------------------------------------ option J ----
# Lowercase, restrained. A thin light-blue line starts just below the
# baseline left of the "o", rises through its counter, runs behind "a" and the
# stem of the "t", and leaves the right end of the t's crossbar as one short
# wave. The letters sit on top, so the line shows only in the counter, the
# narrow gaps and the wave.
recs, boxes = layout(ps_bold, "zwicoat", track=TRACK["J"])
W = union(boxes)[2]
o_cs = contours_of(recs[4])
inner = min(o_cs, key=lambda c: (cbox(c)[2] - cbox(c)[0]))
ix0, iy0, ix1, iy1 = cbox(inner)
ccx, ccy = (ix0 + ix1) / 2, (iy0 + iy1) / 2
ox0, oy0, ox1, oy1 = boxes[4]
ow = ox1 - ox0
t_x0, t_top, t_x1, _ = boxes[6]
# the t's crossbar: the y range of its outline points near the right edge,
# upper half only (the hook of the t's foot also reaches the right edge)
bar = [pt[1] for op, args in recs[6].value for pt in args
       if pt[0] > t_x1 - 1.5 and pt[1] < t_top / 2]
ybar = (min(bar) + max(bar)) / 2
xs, ys = spline([(ox0 - 0.45 * ow, 7), (ccx, ccy + 2), (t_x0, ybar), (t_x1 - 2, ybar)], per=30)
L, amp, m = 48.0, 8.5, 40
for i in range(1, m + 1):
    u = i / m
    xs.append(t_x1 - 2 + L * u)
    ys.append(ybar - amp * math.sin(2 * math.pi * u) * math.sin(math.pi * u))
n = len(xs) - 1
half = [2.6 * min(1.0, (i / n) / 0.08) ** 0.7 * min(1.0, (1 - i / n) / 0.12) ** 0.8 + 0.15
        for i in range(n + 1)]
jline = ribbon(xs, ys, half)
write_svg("option-j", "zwicoat", [(jline, MID), (merge(recs), BLUE)])

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

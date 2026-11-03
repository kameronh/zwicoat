"""Build logo round three for ZwiCoat into site/public/logo-options/.

Owner, 2026-11-02: "by 1 and 2 I mean Current and A: show me hybrids between
Current and A with varying boldness of font. Remove all other options. Also
try 1 or 2 with a softer font."

Every wordmark is converted to outlines with fontTools, with the font's own
GPOS pair kerning on, so no SVG depends on a font being installed. Shapes use
only the brand blues (#0A68A6 and #4FA3D8): no gradients, no shadows.

  Current  site/public/logo-v2-arialblack.svg (the Arial Black logo live before
           H1 replaced it), shown on the page as is (not rebuilt here)
  A        Public Sans Bold (700), -0.02 em, A's rebalanced swooshes
  H1       Public Sans ExtraBold (800), -0.02 em, Current's swooshes
  H2       Public Sans Bold (700), -0.02 em, Current's swooshes
  H3       Public Sans SemiBold (600), -0.02 em, Current's swooshes
  H4       Arial Black, -0.03 em, A's swooshes
  H5       Public Sans Bold (700), -0.01 em, A's swooshes
  S1       Segoe UI Bold, -0.02 em, Current's swooshes (softer font)
  S2       Softer font on A's swooshes, -0.02 em. Calibri Bold and Bahnschrift
           SemiBold were both tried; S2_FONT holds the pick, Calibri Bold (set
           the S2_FONT environment variable to "bahnschrift" for the other).

"Current's swooshes" are read from site/public/logo-v2-arialblack.svg. The two swoosh paths
keep their exact heights and positions relative to the baseline and the cap
height, and are stretched horizontally only, by the ratio of the new word
width to the current word width, so they still start under the Z and end at
the t. "A's swooshes" are the a_swooshes() pair, scaled to the word width.

PNGs (1400 px wide, transparent) are rendered with sharp from the site's
node_modules, so run this from anywhere with Node available:
    python figures/build_logo_options.py

The site fonts ship as .woff2. If the Python brotli module is missing, the
decompression is handed to Node's built-in zlib instead.
"""
import json
import math
import os
import re
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
# The Arial Black logo that was live before H1 replaced it (2026-11-02).
CURRENT = SITE / "public" / "logo-v2-arialblack.svg"
FS = SITE / "node_modules" / "@fontsource-variable"
PUBLIC_SANS = FS / "public-sans" / "files" / "public-sans-latin-wght-normal.woff2"
WINFONTS = Path(r"C:\Windows\Fonts")
ARIAL_BLACK = WINFONTS / "ariblk.ttf"
SEGOE_BOLD = WINFONTS / "segoeuib.ttf"
CALIBRI_BOLD = WINFONTS / "calibrib.ttf"
BAHNSCHRIFT = WINFONTS / "bahnschrift.ttf"

BLUE = "#0A68A6"
MID = "#4FA3D8"

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


def layout(font, text, track=0.0):
    """Lay out text with cap height = 100 units, baseline at y = 0 (SVG y down).

    Returns per-glyph RecordingPens (already in SVG coordinates, first ink at
    x = 0) and their ink boxes. track is added space per glyph, in em.
    """
    gs = font.getGlyphSet()
    cmap = font.getBestCmap()
    upm = font["head"].unitsPerEm
    cap = font["OS/2"].sCapHeight or 0.7 * upm
    S = 100.0 / cap
    kern = kern_fn(font)
    names = [cmap[ord(c)] for c in text]
    bp = BoundsPen(gs)
    gs[names[0]].draw(bp)
    x = -bp.bounds[0]  # left side bearing of the first glyph
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
def ribbon(xs, ys, half):
    """A filled ribbon around a centreline, half-thickness per sample, with
    Catmull-Rom smoothing on both edges. Ends taper to the given half value."""
    n = len(xs)
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


def taper(t, a=0.5):
    """0 at both ends, 1 in the middle; a < 1 gives fuller shoulders."""
    return math.sin(math.pi * min(max(t, 0.0), 1.0)) ** a


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


# Current's swooshes, read from logo-v2-arialblack.svg. That file uses the same frame as
# layout() (cap height 100, baseline y = 0). Its first path is the Arial Black
# wordmark, then the light upper swoosh and the long deep-blue wave, each
# written as "M x,y C ... Z" in absolute numbers.
_NUM = r"-?\d+(?:\.\d+)?"
_paths = re.findall(r'<path fill="(#[0-9A-Fa-f]{6})" d="([^"]+)"',
                    CURRENT.read_text(encoding="utf-8"))
_text_d = [d for f, d in _paths if f.upper() == BLUE][0]
CUR_WAVE = [float(v) for v in re.findall(_NUM, [d for f, d in _paths if f.upper() == BLUE][-1])]
CUR_UPPER = [float(v) for v in re.findall(_NUM, next(d for f, d in _paths if f.upper() == MID))]
# The current word ends at the right edge of its t: the largest x among the
# text path's absolute M, L, H and Q points (V carries only a y).
_xs = []
for cmd, args in re.findall(r"([MLHVQZ])([^MLHVQZ]*)", _text_d):
    v = [float(a) for a in re.findall(_NUM, args)]
    if cmd == "H":
        _xs += v
    elif cmd in "ML":
        _xs += v[0::2]
    elif cmd == "Q":
        _xs += v[0::2]
CUR_W = max(_xs)


def _curve_path(nums, sx):
    """Rebuild an "M x,y C (6 numbers)... Z" path with x scaled by sx."""
    rec = RecordingPen()
    rec.moveTo((nums[0] * sx, nums[1]))
    for i in range(2, len(nums) - 5, 6):
        c = nums[i:i + 6]
        rec.curveTo((c[0] * sx, c[1]), (c[2] * sx, c[3]), (c[4] * sx, c[5]))
    rec.closePath()
    return rec


def current_swooshes(W):
    """Current's upper swoosh and long wave, stretched to the word width W."""
    sx = W / CUR_W
    return _curve_path(CUR_UPPER, sx), _curve_path(CUR_WAVE, sx)


# ----------------------------------------------------------------- svg ----
def write_svg(name, label, layers, pad=4, png_width=1400):
    """layers: list of (RecordingPen, fill)."""
    x0, y0, x1, y1 = union([bounds_of(l[0]) for l in layers])
    vb = (x0 - pad, y0 - pad, (x1 - x0) + 2 * pad, (y1 - y0) + 2 * pad)
    body = [f'  <path fill="{fill}" d="{d_of(rec)}"/>' for rec, fill in layers]
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


def build(name, font, track, swooshes, note):
    recs, boxes = layout(font, "ZwiCoat", track=track)
    W = union(boxes)[2]
    upper, wave = swooshes(W)
    print(f"{name}: {note}, track {track} em, word width {W:.1f} (Current {CUR_W:.1f})")
    write_svg(name, "ZwiCoat", [(merge(recs), BLUE), (upper, MID), (wave, BLUE)])


def main():
    ps_semi = load(PUBLIC_SANS, wght=600)
    ps_bold = load(PUBLIC_SANS, wght=700)
    ps_xbold = load(PUBLIC_SANS, wght=800)
    arial_black = load(ARIAL_BLACK)
    segoe_bold = load(SEGOE_BOLD)

    # S2: both candidates were rendered at 40 px. Calibri Bold holds up there and
    # is the softer of the two: rounded strokes and open, humanist letters.
    # Bahnschrift SemiBold reads squarer and more technical (a DIN design), which
    # is the opposite of the request, so Calibri Bold is the pick.
    S2_FONT = os.environ.get("S2_FONT", "calibri")
    if S2_FONT == "bahnschrift":
        s2_font, s2_note = load(BAHNSCHRIFT, wght=600, wdth=100), "Bahnschrift SemiBold"
    else:
        s2_font, s2_note = load(CALIBRI_BOLD), "Calibri Bold"

    build("option-a", ps_bold, -0.02, a_swooshes, "Public Sans Bold 700, A's swooshes")
    build("option-h1", ps_xbold, -0.02, current_swooshes, "Public Sans ExtraBold 800, Current's swooshes")
    build("option-h2", ps_bold, -0.02, current_swooshes, "Public Sans Bold 700, Current's swooshes")
    build("option-h3", ps_semi, -0.02, current_swooshes, "Public Sans SemiBold 600, Current's swooshes")
    build("option-h4", arial_black, -0.03, a_swooshes, "Arial Black, A's swooshes")
    build("option-h5", ps_bold, -0.01, a_swooshes, "Public Sans Bold 700, A's swooshes")
    build("option-s1", segoe_bold, -0.02, current_swooshes, "Segoe UI Bold, Current's swooshes")
    build("option-s2", s2_font, -0.02, a_swooshes, s2_note + ", A's swooshes")
    render_pngs(jobs)


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


def render_pngs(job_list):
    """Render each SVG job to a PNG with sharp from the site's node_modules."""
    subprocess.run(["node", "-e", JS], input=json.dumps(job_list).encode(), cwd=str(SITE), check=True)


if __name__ == "__main__":
    main()

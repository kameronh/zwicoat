"""Build site/public/logo.svg (and logo.png, favicon.png) for ZwiCoat.

Wordmark "ZwiCoat" is converted to outlines with fontTools (Arial Black by
default), so the SVG has no font dependency. Two swooshes sit under the text.
Run:  python figures/build_logo.py [fontfile]
"""
import sys
from pathlib import Path
from fontTools.ttLib import TTFont
from fontTools.pens.svgPathPen import SVGPathPen
from fontTools.pens.transformPen import TransformPen
from fontTools.pens.boundsPen import BoundsPen

ROOT = Path(__file__).resolve().parent.parent
PUB = ROOT / "site" / "public"
FONT = sys.argv[1] if len(sys.argv) > 1 else r"C:\Windows\Fonts\ariblk.ttf"
TEXT = "ZwiCoat"
BLUE = "#0A68A6"
MID = "#4FA3D8"
TRACK = 0.035  # letter spacing, fraction of em

font = TTFont(FONT)
gs = font.getGlyphSet()
cmap = font.getBestCmap()
upm = font["head"].unitsPerEm
cap = font["OS/2"].sCapHeight or 0.716 * upm

# lay out glyphs, scale so cap height = 100 units
S = 100.0 / cap
x = 0.0
pieces = []
for ch in TEXT:
    gn = cmap[ord(ch)]
    pen = SVGPathPen(gs)
    tp = TransformPen(pen, (S, 0, 0, -S, x * S, 0))  # flip y, baseline y=0
    gs[gn].draw(tp)
    pieces.append(pen.getCommands())
    x += gs[gn].width + TRACK * upm
x -= TRACK * upm
# trim side bearings: measure ink bounds
bp = BoundsPen(gs)
first = gs[cmap[ord(TEXT[0])]]
first.draw(bp)
lsb = bp.bounds[0]
bp = BoundsPen(gs)
last = gs[cmap[ord(TEXT[-1])]]
last.draw(bp)
rsb = last.width - bp.bounds[2]
ink_w = (x - lsb - rsb) * S
xoff = -lsb * S
W = ink_w
text_d = ""
# rebuild with xoff applied
pieces = []
x = 0.0
for ch in TEXT:
    gn = cmap[ord(ch)]
    pen = SVGPathPen(gs, ntos=lambda v: f"{v:.2f}".rstrip("0").rstrip("."))
    tp = TransformPen(pen, (S, 0, 0, -S, x * S + xoff, 0))
    gs[gn].draw(tp)
    pieces.append(pen.getCommands())
    x += gs[gn].width + TRACK * upm
text_d = " ".join(pieces)

# swooshes drawn in a 700-wide box, scaled to W; y origin = baseline + gap
k = W / 700.0
GAP = 22          # space between baseline and swoosh box top (svg units)
def sc(path):
    """scale numbers in a path written for the 700-wide box (pairs x,y)."""
    out = []
    for tok in path.split():
        if tok[0].isalpha():
            out.append(tok)
        else:
            xx, yy = tok.split(",")
            out.append(f"{float(xx)*k:.2f},{float(yy)*k+GAP:.2f}")
    return " ".join(out)

# long wave: rises from the left tip to a crest, then a long tail to the right tip
wave = ("M 4,66 C 50,30 140,18 270,40 C 410,64 560,80 696,66 "
        "C 590,92 440,98 300,86 C 170,76 70,80 4,66 Z")
# upper swoosh: thinner, sweeps up on the right above the wave
swoosh = ("M 370,34 C 490,42 610,20 698,-16 "
          "C 655,22 570,48 480,50 C 435,51 395,46 370,34 Z")

top = -100.0 - 0.0
bottom = GAP + 100 * k
H = bottom - top
pad = 4
vb = f"{-pad:.2f} {top-pad:.2f} {W+2*pad:.2f} {H+2*pad:.2f}"
svg = f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="{vb}" role="img" aria-label="ZwiCoat">
  <title>ZwiCoat</title>
  <path fill="{BLUE}" d="{text_d}"/>
  <path fill="{MID}" d="{sc(swoosh)}"/>
  <path fill="{BLUE}" d="{sc(wave)}"/>
</svg>
'''
(PUB / "logo.svg").write_text(svg, encoding="utf-8")
vbw, vbh = W + 2 * pad, H + 2 * pad
print("viewBox", vb, "aspect", round(vbw / vbh, 4), "text w / cap", round(W / 100, 2))

# PNG export via PIL-free route: use matplotlib-less renderer if cairosvg exists
try:
    import cairosvg
    cairosvg.svg2png(bytestring=svg.encode(), write_to=str(PUB / "logo.png"), output_width=1400)
    print("png via cairosvg")
except Exception as e:
    print("cairosvg unavailable:", e)

"""Build the site logo and favicon for ZwiCoat (option H1, thin wave).

Owner, 2026-11-02: the logo is option H1 from figures/build_logo_options.py
(Public Sans ExtraBold 800 wordmark, -0.02 em tracking, the previous logo's
two swooshes stretched to the new word width), with the long deep-blue wave
about 35 percent thinner. The light upper swoosh is unchanged.

How the wave is thinned: its top edge and bottom edge are sampled along x
(both edges are monotonic in x and meet at the two tips). At each x the
centreline c = (top + bottom) / 2 is kept and the half-thickness is scaled by
WAVE_SCALE, so the wave stays where it was under the baseline and its tips
still taper to points. The new edges are re-fitted with Catmull-Rom cubics on
cosine-spaced samples (dense near the tips).

Outputs (every glyph converted to outlines, so nothing depends on a font):
  site/public/logo.svg      the logo
  site/public/logo.png      1400 px wide, transparent
  site/public/favicon.svg   the "Z" of the wordmark, square viewBox
  site/public/favicon.png   64 px, transparent
The previous Arial Black logo is kept as site/public/logo-v2-arialblack.svg
(build_logo_options.py reads its swooshes from there).

Run:  python figures/build_logo.py
"""
import math

from fontTools.pens.recordingPen import RecordingPen

import build_logo_options as L

PUB = L.SITE / "public"
WAVE_SCALE = 0.65  # new wave thickness / H1 wave thickness
TRACK = -0.02


def _bez(p0, p1, p2, p3, t):
    u = 1 - t
    return tuple(u ** 3 * a + 3 * u * u * t * b + 3 * u * t * t * c + t ** 3 * d
                 for a, b, c, d in zip(p0, p1, p2, p3))


def _sample_edge(segs, n=400):
    """Dense (x, y) samples along a list of cubic segments, sorted by x."""
    pts = []
    for s in segs:
        pts += [_bez(*s, i / n) for i in range(n + 1)]
    return sorted(pts)


def _interp(pts, x):
    lo, hi = 0, len(pts) - 1
    while hi - lo > 1:
        mid = (lo + hi) // 2
        if pts[mid][0] <= x:
            lo = mid
        else:
            hi = mid
    (x0, y0), (x1, y1) = pts[lo], pts[hi]
    return y0 if x1 == x0 else y0 + (y1 - y0) * (x - x0) / (x1 - x0)


def _catmull(rec, points, first):
    """Catmull-Rom cubics through points. first: start with a moveTo;
    otherwise the pen is assumed to sit at points[0] already."""
    if first:
        rec.moveTo(points[0])
    for i in range(len(points) - 1):
        p0 = points[max(i - 1, 0)]
        p1, p2 = points[i], points[i + 1]
        p3 = points[min(i + 2, len(points) - 1)]
        c1 = (p1[0] + (p2[0] - p0[0]) / 6, p1[1] + (p2[1] - p0[1]) / 6)
        c2 = (p2[0] - (p3[0] - p1[0]) / 6, p2[1] - (p3[1] - p1[1]) / 6)
        rec.curveTo(c1, c2, p2)


def thin_wave(wave, scale, n=48):
    """Scale the vertical thickness of the wave about its centreline.

    wave is the RecordingPen from current_swooshes(): moveTo, two cubics for
    the top edge (left tip to right tip), two for the bottom edge (back to the
    left tip), closePath.
    """
    ops = wave.value
    start = ops[0][1][0]
    curves = [op[1] for op in ops if op[0] == "curveTo"]
    assert len(curves) == 4, curves
    segs, prev = [], start
    for c in curves:
        segs.append((prev, c[0], c[1], c[2]))
        prev = c[2]
    top = _sample_edge(segs[:2])
    bot = _sample_edge(segs[2:])
    xl, xr = start[0], segs[1][3][0]
    yl, yr = start[1], segs[1][3][1]
    xs = [xl + (xr - xl) * (1 - math.cos(math.pi * i / n)) / 2 for i in range(n + 1)]
    new_top, new_bot = [], []
    for i, x in enumerate(xs):
        if i == 0:
            new_top.append((x, yl)); new_bot.append((x, yl)); continue
        if i == n:
            new_top.append((x, yr)); new_bot.append((x, yr)); continue
        yt, yb = _interp(top, x), _interp(bot, x)
        c, h = (yt + yb) / 2, (yb - yt) / 2
        new_top.append((x, c - scale * h))
        new_bot.append((x, c + scale * h))
    rec = RecordingPen()
    _catmull(rec, new_top, True)          # left tip to right tip
    _catmull(rec, new_bot[::-1], False)   # right tip back to the left tip
    rec.closePath()
    old_max = max(_interp(bot, x) - _interp(top, x) for x in xs[1:-1])
    return rec, old_max


def main():
    font = L.load(L.PUBLIC_SANS, wght=800)
    recs, boxes = L.layout(font, "ZwiCoat", track=TRACK)
    W = L.union(boxes)[2]
    upper, wave = L.current_swooshes(W)
    thin, old_max = thin_wave(wave, WAVE_SCALE)
    tb, nb = L.bounds_of(wave), L.bounds_of(thin)
    print(f"word width {W:.1f}; wave max thickness {old_max:.2f} -> {old_max * WAVE_SCALE:.2f} "
          f"(x{WAVE_SCALE}); wave bbox y {tb[1]:.2f}..{tb[3]:.2f} -> {nb[1]:.2f}..{nb[3]:.2f}")

    # logo.svg and logo.png (write_svg writes into L.OUT, so point it at public)
    L.OUT = PUB
    L.jobs.clear()
    L.write_svg("logo", "ZwiCoat", [(L.merge(recs), L.BLUE), (upper, L.MID), (thin, L.BLUE)])

    # favicon: the Z alone, centred in a square viewBox with a small margin
    z = recs[0]
    x0, y0, x1, y1 = L.bounds_of(z)
    side = max(x1 - x0, y1 - y0) + 12
    cx, cy = (x0 + x1) / 2, (y0 + y1) / 2
    vb = (cx - side / 2, cy - side / 2, side, side)
    fav = (f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="{" ".join(L.fmt(v) for v in vb)}">'
           f'<path fill="{L.BLUE}" d="{L.d_of(z)}"/></svg>\n')
    (PUB / "favicon.svg").write_text(fav, encoding="utf-8")
    L.jobs.append({"svg": str(PUB / "favicon.svg"), "png": str(PUB / "favicon.png"),
                   "w": 64, "vbw": side})
    L.render_pngs(L.jobs)


if __name__ == "__main__":
    main()

# Round 8 lab media: native extraction of "tissue expander figs.pptx"

Source: `G:\My Drive\9 Zwitterion\Claude Code projects and misc files\misc transfer files\For website\tissue expander figs.pptx`
(six slides; slide 6 is the owner's new final slide). Extracted 2026-11-02 with python-pptx,
image blobs written byte for byte (no re-encoding, no slide-level cropping on any picture).
Credit for every image: ZwiCoat, 2026.

| File | Slide | Shape (name) | Native size (px) | Slide text |
|---|---|---|---|---|
| s01_shape00.jpg | 1 | 0 (Back before) | 2000 x 1000 | "Before impact:" / "After impact:" |
| s01_shape01.png | 1 | 1 (Back after) | 2000 x 1000 | "Before impact:" / "After impact:" |
| s02_shape00.png | 2 | 0 (Picture 6) | 447 x 394 | none |
| s02_shape01.png | 2 | 1 (Picture 8) | 364 x 382 | none |
| s03_shape00.png | 3 | 0 (Picture 2) | 2464 x 1242 | "100 cc tissue expander inflated to 300 cc -> No tearing" |
| s03_shape01.png | 3 | 1 (Picture 4) | 2460 x 1244 | same |
| s04_shape00.png | 4 | 0 (Picture 1) | 965 x 523 | "1-year mouse study" / "Acta biomaterialia 166 (2023): 212-223" |
| s05_shape00.png | 5 | 0 (Picture 3) | 2380 x 1034 | none |
| s05_shape01.png | 5 | 1 (Picture 5) | 2404 x 1058 | none |
| s06_shape00.png | 6 | 0 (Picture 5) | 2224 x 560 | none (three coated PEEK photos on grid paper, no labels) |

## Site crops made from this round (`site/public/images/lab/`, JPEG q88, longest side <= 1200 px)

Each slide 3 picture holds two rounded-corner photo panels on a #F5F6F3 background; slide 6
holds three photos on white. Panels were split at the background column run (the gutter), the
photo box found from rows and columns that are at least 80 percent photo (slide 6: row and column
means darker than the pure-white gutter, since one photo has an overexposed top edge), then
trimmed until no edge row or column holds background, then inset 3 px. Boxes are (x0, y0, x1, y1),
inclusive, in source pixels. Script: scratchpad `crop_r8.py`.

| Output | Source | Gutter (bg column run) | Crop box | Output size |
|---|---|---|---|---|
| expander-150pct.jpg | s03_shape00 left | 1198-1258 | (32, 42, 1182, 1192) | 1151 x 1151 |
| expander-200pct.jpg | s03_shape00 right | 1198-1258 | (1274, 42, 2424, 1192) | 1151 x 1151 |
| expander-250pct.jpg | s03_shape01 left | 1194-1255 | (29, 37, 1178, 1185) | 1150 x 1149 |
| expander-300pct.jpg | s03_shape01 right | 1194-1255 | (1271, 37, 2420, 1185) | 1150 x 1149 |
| peek-coated-01.jpg | s06_shape00 left | 732-755 | (11, 11, 728, 549) | 718 x 539 |
| peek-coated-02.jpg | s06_shape00 middle | 732-755, 1474-1504 | (759, 15, 1470, 546) | 712 x 532 |
| peek-coated-03.jpg | s06_shape00 right | 1474-1504 | (1508, 11, 2214, 543) | 707 x 533 |

Percent order (150, 200, 250, 300 of rated volume) is the owner's, panel order left to right,
picture order left to right on slide 3. The blue area grows panel to panel (22, 24, 31, 34
percent of the frame), consistent with that order. The PEEK photos keep the grid paper as scale;
none of the three carries a label on the slide.

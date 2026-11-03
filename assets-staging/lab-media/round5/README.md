# Round 5 deck extraction

Source: `G:\My Drive\9 Zwitterion\Claude Code projects and misc files\misc transfer files\For website\tissue expander figs.pptx`
(5 slides, 16:9). Every picture was saved at native resolution from `shape.image.blob` with python-pptx. No picture had a PowerPoint crop applied. All PNGs have a fully opaque alpha channel.

| File | Slide | Shape name | Slide text | Pixel size | Notes |
|---|---|---|---|---|---|
| slide1-pic1.jpg | 1 | Back before | "Before impact:" | 2000x1000 | Byte-identical to `../expander-mentor125-before-back.jpg` (Mentor 125 cc, back face) |
| slide1-pic2.png | 1 | Back after | "After impact:" | 2000x1000 | Same expander after impact. Not identical to `../expander-mentor125-after-back.jpg` (mean pixel difference 17/255, a different export or edit) |
| slide2-pic1.png | 2 | Picture 6 | none | 447x394 | Inflated expander in a dye bath (right side of the slide) |
| slide2-pic2.png | 2 | Picture 8 | none | 364x382 | Deflated expander in a dye bath (left side of the slide) |
| slide3-pic1.png | 3 | Picture 2 | "100 cc tissue expander inflated to 300 cc -> No tearing" | 2464x1242 | Left picture on the slide. Two photo panels inside, no labels |
| slide3-pic2.png | 3 | Picture 4 | (same) | 2460x1244 | Right picture on the slide. Two photo panels inside, no labels; expander visibly larger |
| slide4-pic1.png | 4 | Picture 1 | "1-year mouse study"; "Acta biomaterialia 166 (2023): 212-223" | 965x523 | H&E section, uncoated vs coated PDMS, capsule outline. Horne et al. 2023 |
| slide5-pic1.png | 5 | Picture 3 | none | 2380x1034 | Horne 2023 Fig. 4 top row: a "Uncoated PDMS", b "Coated PMDS" (typo in source) |
| slide5-pic2.png | 5 | Picture 5 | none | 2404x1058 | Horne 2023 Fig. 4 bottom row: c "Uncoated Pt", d "Coated Pt" |
| slide5-pic1-typofix-check.png | derived | | | 2380x1034 | slide5-pic1 with the "PMDS" header glyphs swapped to "PDMS" (M and D glyphs moved, no new text drawn) |

No speaker notes. No monomer names or "ZwiGuard" text appear in any picture.

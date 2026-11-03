# Round five checklist (Kam, 2026-11-02 evening)

Verify each item in `site/dist` and on staging with a proving snippet.

## Evidence page

| # | Item | Status |
|---|---|---|
| R1 | Section 1 order: (top) interactive W04 scar chart (built like the antifouling chart: bars, filters by species and paper, tooltip with paper link), (middle) histology photo from the new deck slide 4 (`histology-scar-01.png`, Horne 2023 one-year mouse), (bottom) W27 Horne bar-chart takeaways | DONE: interactive W04 (fibrosis.ts), then histology-scar-01 photo, then W27 |
| R2 | Long source lines gone: every figure shows citation plus figure numbers only (short source); full sources kept in code as `sourceFull` (commented or unused field) | DONE: every displayed source is the short form (source-short.ts); full `source` kept in code |
| R3 | Insertion force and friction section order: W28 first, then the two interactive force-profile viewers, then W07 beneath | DONE: W28, cochlear viewer, ETT viewer, W07 |
| R4 | Trace viewers (cochlear and ETT): side-by-side panels, uncoated left and coated right, shared y-axis scale, no overlay | DONE: two panels, uncoated left, coated right, shared x and y ranges |
| R5 | W07 shows three studies (Bennion, Peel, synthetic cochlea) | DONE: W07 three studies; caption updated site-wide |
| R6 | W06 durability timeline is interactive everywhere it appears (evidence, durability, any application page): hover a checkpoint for the finding, click to open the paper; includes the dual-network study | DONE: interactive on evidence, durability, technology, ent-tubes, indwelling catheters, vascular access; Barrera 2026 included |
| R7 | In-vivo interactive chart includes the human cadaver ETT insertion rows (and the synthetic cochlea rows) | DONE: 50 of 50 rows; larynx and synthetic cochlea legend entries |
| R8 | "Every number" tiles removed from the evidence page | DONE: tiles removed from evidence |

## Neural interfaces

| # | Item | Status |
|---|---|---|
| R9 | Horne 2023 Figure 4 as four separate images (silicone uncoated and coated; platinum uncoated and coated) in an interactive 2 x 2 panel component (toggle or hover between coated and uncoated per material; caption states the 47 to 18 micrometer, about 60 percent result) placed as the page lead | DONE: CapsulePanels.astro as the neural lead ({{panels:capsule}}) |

## Home

| # | Item | Status |
|---|---|---|
| R10 | The hero chart (W04) is interactive (same component as R1) with the static PNG fallback | DONE: hero uses the interactive W04, PNG fallback |
| R11 | Applications heading reworded: no "nine device families"; the coating applies to any medical elastomer and many device types (proposed: "Nine places to start. ZwiCoat bonds to the elastomers and plastics most devices are made of.") | DONE: home and /applications |
| R12 | Tiles: "3 dissertations" and "more patents pending" replaced by "~60%" thinner fibrotic capsule (Horne 2023, one year, mice) and "~50%" less insertion force (three studies); tiles moved below "Ten years of published work" | DONE: ~60% and ~50% tiles, below the timeline; W12 JSON and build_figures.py data updated |

## Durability

| # | Item | Status |
|---|---|---|
| R13 | Before and after impact photos (deck slide 1) placed to the right of the pendulum video; caption cites 45 J | DONE: ImpactBlock, photos right of the clip, 45 J caption |
| R14 | Pendulum video cropped to remove the bottom 25 percent (lab floor); poster matches | DONE (assets from the lead): 540 x 810 clip and poster, aspect 540/810 everywhere |
| R15 | "The gel tears before the bond lets go" section has a side panel showing current bond strength versus 2019 (W39, if the database supports about 200 kPa; otherwise the numbers in text) | DONE: side panel with ~105, ~94 and ~60 to 100 kPa; W39 not drawn |

## Tissue expanders

| # | Item | Status |
|---|---|---|
| R16 | W17 rendered smaller | DONE: W17 at 640 px |
| R17 | Photos from slide 2 (deflated and inflated) and slide 3 (100 to 300 percent of rated volume, "no tearing") placed in the page | DONE: slide 2 and slide 3 pairs in "What ZwiCoat does here" |
| R18 | Pendulum video with before and after photos at the bottom of the page; 45 J cited | DONE: "Takes a hit" block before "How to start" |

## Site-wide

| # | Item | Status |
|---|---|---|
| R19 | Figure sizing screened on every page: no chart rendered so small its text is unreadable at 1280 px, none oversized; `width` props adjusted per figure | DONE: sizing table in VERIFY.md; charts capped at design width, wide rows for static charts |
| R20 | All "values are approximate, read from the figure" style disclaimers removed from displayed source lines site-wide (kept in code) | DONE: 0 disclaimers in displayed source lines (PNG subtitles still carry some, see VERIFY open points) |
| R21 | Logo alternatives page `/logo-options` with five proposals plus current | DONE: /logo-options, current plus five; favicon row now wraps at 375 px |

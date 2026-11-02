# Feedback checklist: Kam's "New Materials" message (2026-11-02) plus his answers

Every item must be verified in the BUILT html (`site/dist`) and on
`https://staging.zwicoat.com`, with the proving snippet quoted in VERIFY.md.
Status column: TODO, DONE (verified), or OPEN (needs Kam, with the reason).

## New materials

| # | Item | Status |
|---|---|---|
| N1 | Durability report highlights replotted in site style on /durability (W35 wear, W36 dry and re-wet; nothing customer-specific) | DONE |
| N2 | Cranioplasty: PEEK lap-shear online (W34 on PEEK page); rat result stated in one general sentence (answer 16); paper figures NOT posted | DONE |
| N3 | Market research and grants: each application page states the key problem and argument with citations (neural, expanders, airway, vascular, indwelling, PEEK, sensors, ENT, GI) using `figures/published/site-materials-2026.md` and `references-resolved.md`; nothing from the do-not-broadcast list | DONE (final pass: argument paragraphs with new cited numbers on expanders (Kraenzlin 2022), indwelling (Murray 2022), sensors (Zaharieva 2019, Gough 2010), ENT (Kim 2014, Jirawatnotai 2019); argument-only paragraphs on vascular and GI (no citable new number in the sources); PEEK Li 2017 corrected; airway stenosis and VAP from the ready-to-paste block (Dorris 2021, Schweiger 2013, Stoler 2025, Yin 2019, Chastre 2002); neural 'about 4 removals per 10 implanted (Jones 2022)'. Proof: VERIFY.md, Final pass) |
| N4 | Provisionals: site says only "further patent applications are pending"; no titles | DONE |

## Technology page

| # | Item | Status |
|---|---|---|
| T1 | First sentence: "ZwiCoat is a zwitterionic hydrogel that dramatically lowers friction, infection, inflammation and biofouling." | DONE |
| T2 | No SBMA or CBMA in prominent copy anywhere; never in the first sentence of the home page | DONE |
| T3 | About: "The company is based near Iowa City, Iowa, and is 100 percent founder owned." | DONE |
| T4 | Fifth sentence: "It covalently bonds the coating to the device surface. The same light crosslinks the network." | DONE |
| T5 | "Silicone is published. Your material is the feasibility round." gone; substrates block makes sense | DONE |
| T6 | Kam's "How it works" wording (answer 6): dipole sentence, hydration barrier paragraph, PEG comparison | DONE |
| T7 | W04: hollow basal-turn bar removed and its sentence removed | DONE |
| T8 | No "benzophenone" anywhere; W31 axis "Grafting agent concentration (mg/mL)" in the image | DONE |
| T9 | W30 shows both SBMA and CBMA series | DONE |
| T10 | Process video block hidden on home and technology | DONE |
| T11 | Regulatory section ("The partner files. ZwiCoat supports.") deleted; no regulatory text on home or technology | DONE |
| T12 | Regulatory on application pages only: one brief optimistic line each | DONE |

## Evidence page

| # | Item | Status |
|---|---|---|
| E1 | Horne dissertation year 2024 everywhere: publications, about timeline list, W24 chart image, W24 json | DONE |
| E2 | "The record" (timeline) moved to the bottom of /about; not on /evidence | DONE |
| E3 | Section order: scar tissue first, protein/cells/bacteria/friction second | DONE |
| E4 | Tile "4 weeks" is now "6 months" (functional human arrays in sheep) | DONE |
| E5 | "And in the archive" tiles removed | DONE |
| E6 | Archive source line moved to the bottom and reads "ZwiCoat Data archive" (no "E-report method tags (built ...)") | DONE |
| E7 | W26 not on /evidence and not on the home page (neural page only) | DONE |
| E8 | Histology photo header reads "Coated", not "CBMA" (image file) | DONE |
| E9 | Electrode impedance section sits below insertion force and friction | DONE |
| E10 | W08 rendered at a reasonable size (about 640 px, not full width) | DONE |
| E11 | Synthetic cochlea insertion-force chart (W37, from the Zenodo dataset) on evidence and neural | DONE (final pass: W37 and W38 on /evidence after W07 as interactive trace viewers with PNG fallback; W37 static on neural after the insertion-force paragraph; sanitized source 'NIH SBIR Phase I dataset, ZwiCoat Materials Innovations, Zenodo, doi:10.5281/zenodo.10459478'. Proof: VERIFY.md, Final pass. Build-note caveat on the 66 vs 38 percent remains for Kam) |

## Durability page

| # | Item | Status |
|---|---|---|
| D1 | Highlights from the report (N1) | DONE |
| D2 | "What we have not shown yet / Aging and shelf life come next" removed | DONE |
| D3 | Friction-after-implantation chart wide enough to read (W28a) | DONE |
| D4 | Pendulum video shows the close-up only | DONE |
| D5 | Mechanical section: x-axis "grafting agent concentration (mg/mL)"; no "benzophenone"; (a "then vs now" bond chart was not supported by the data: current silicone bond is capped by the gel tearing, so the page says that instead) | DONE |
| D6 | Header "Compatible with multiple sterilization methods" (not "Seven of eight ..."); W11 title the same; all eight tiles kept; wet e-beam tile says "failed" | DONE |
| D7 | "intact" replaced in sterilization contexts | DONE |
| D8 | Only panel A of the friction chart on this page | DONE |

## Universal

| # | Item | Status |
|---|---|---|
| U1 | Internal citations minimal: no "Kyle Ruby", no "CIVCO", no scientist or customer names in source lines | DONE |
| U2 | ZwiGuard replaced by ZwiCoat everywhere (titles, meta, footer, alt text, json) | DONE |
| U3 | Logo: "ZwiCoat" wordmark with visible top swoosh, on every page (nav and footer) and favicon | DONE |
| U4 | Application order: neural, expanders, airway, vascular, indwelling, PEEK, sensors, ENT, GI (nav, footer, index, home grid) | DONE |
| U5 | No sample-overlap sentence about the two insertion-force studies | DONE |
| U6 | No p values, "not significant" (W25 caption excepted), "read from the figure" in body copy | DONE |

## Neural interfaces

| # | Item | Status |
|---|---|---|
| NI1 | Leads with histology (sheep histology as lead until Horne originals exist; Kam has no originals) | DONE |
| NI2 | Explains: conceals platinum, thinner capsule, raises surface capacitance so impedance falls and contacts can be smaller, nanotexturing possible; written in confident company voice (answer 23) | DONE |
| NI3 | "The problem" paragraph has varied sentence length; no long run of identical short sentences | DONE |

## Airway

| # | Item | Status |
|---|---|---|
| A1 | Leads with the cuff inflate/deflate clip | DONE |
| A2 | Stenosis argument before VAP, with resolved citations from ZCMI_References.pdf | DONE |
| A3 | ETT insertion-force chart (W38, from the ETT paper workup) on the page; card stat is the ETT number | DONE |
| A4 | Standfirst: "ZwiCoat is a drug-free coating that enhances mucus flow, resists bacteria and lowers friction, and it has been tested on endotracheal tubes." | DONE |

## Misc

| # | Item | Status |
|---|---|---|
| M1 | "prestigious" removed; NSF Graduate Research Fellowship wording | DONE |
| M2 | Contact form materials list covers common medical elastomers and metals | DONE |
| M3 | "PEEK: none published" replaced by the rats, cranioplasty wording | DONE |
| M4 | PEEK page: lap-shear chart (W34, simplified) and a hand-drawn SVG of the grafting pathway on PEEK (ketone in the backbone takes part in the grafting step, no primer); no monomer names, no "benzophenone" | DONE (final pass: `PeekPathway.astro` inline SVG in 'How it fits your process' via `{{diagram:peek-pathway}}`, labels PEEK backbone, UV light, the ketone in the backbone starts the graft, hydrogel bonded to the surface, no primer. Proof: VERIFY.md, Final pass) |
| M5 | PEEK page position in the order (sixth) | DONE |
| M6 | Expander sentence: 300 percent of rated volume (answer 12) | DONE |
| M7 | Home subhead with "scarring" (answer 1); keep "Every number on this site comes from ..." (2); archive line removed (3); "Friction was unchanged ..." kept (4); "largest device markets" kept (5) | DONE |
| M8 | Technology: original "not a thin tethered brush ..." sentence kept (7); sterilization paragraph (8) | DONE |
| M9 | Cards: airway ETT force (9), indwelling friction (10), PEEK 635 kPa (11) | DONE |
| M10 | Sensors standfirst (14); PEEK standfirst (15); publications h1 (18); patent 12,116,498 note (19) | DONE |
| M11 | W27 without the PEG bar (20); W25 keeps "not significant" (21); founder owned kept (24) | DONE |

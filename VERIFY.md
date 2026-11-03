# VERIFY: zwicoat.com v2, owner's feedback round (2026-11-02)

Every line below was checked by script against the BUILT site (`site/dist`, after `npm run build`), and the home, technology, evidence, about, neural and airway pages again against https://staging.zwicoat.com after `bash server/deploy-staging.sh --no-build`. The proof column quotes the built HTML (entities decoded, Astro `data-astro-cid` attributes stripped). Checker: banned terms are classified by context (source line, W30 figure, reference title, body copy); only body-copy hits fail.

## Summary

- Built site, page and asset checks: **326 PASS, 0 FAIL**.
- Staging (home, technology, evidence, about, neural, plus airway because its card and chart changed; plus the chart SVGs, JSON, timeline bundle, logo and histology image they use): **166 PASS, 0 FAIL**.
- FEEDBACK-CHECKLIST.md (N1 to M11, 59 items): **56 DONE, 2 TODO, 1 OPEN**. TODO items are assigned to a later worker (N3, M4 grafting-pathway SVG). OPEN: E11 (W37 held for review, see below).
- `npm run build`: 20 pages, no errors or warnings.
- Final pass (N3, M4, E11, trace viewer; section at the end of this file): built site 386 PASS, 0 FAIL; staging (ten changed pages, trace JSON, W37/W38 PNGs) 210 PASS, 0 FAIL. FEEDBACK-CHECKLIST.md now 59 of 59 DONE.

## What changed this pass (source files, so a rebuild keeps it)

- `figures/build_figures.py` (existing functions only): Horne dissertation 2024 (DISSERTATIONS, W12 and W24 source strings); W11 wet e-beam tile 'failed'; W25 four-week polarization pair '(not significant)' restored; W27 PEG-type bar dropped, labels 'Uncoated' / 'Coated', bracket '-67%, p = 0.010'; W34 footnotes and long annotation removed, one 'gel tears before the bond lets go' annotation on the dry PEEK bar, subtitle shortened; W12 tiles '6 months' (sheep) and 'patent applications pending'. Re-ran the script; copied `figures/png`, `figures/svg` into `site/public/figures` and the JSON files the site already publishes into `site/public/data` (copy only; the internal-only `ETT_insertion_trials.json`, `W01_people.json` and `W02_lapshear_groups.json` were deliberately not copied to public).
- `site/public/images/histology-sheep.png`: the lead's 'Coated' overpaint was about 10 percent smaller than 'Uncoated'; redrawn with Pillow (white box, Arial Bold 54 px, matched cap height 40 px and baseline).
- `site/src/data/figure-text.ts`: new shared `W27` text (no PEG control, 'coated'), new `W34` alt and caption; home, technology and evidence now use it.
- Home: hero subhead (answer 1), sources sentence restored (2), archive line and its source clause removed (3), 'Less scar' row now W27 with mouse capsule text (W26 removed).
- Technology: How it works (6). Durability: title (4) and sterilization paragraph (8). Publications: h1 (18). `publications.json`: 12,116,498 note (19). `team.json`: NSF fellowship (17).
- Applications: cards (9, 10, 11) and expander alt (12) in `applications-index.json` and the markdown frontmatter; airway (13), sensors (14), PEEK (15, 16) standfirsts and copy; expanders 300 percent sentence (12) and two neighbouring sentences adjusted so the page does not contradict itself ('Every result below comes from published ...' and 'Whether the film stretches ... is measured in the feasibility round'); neural opener removed (23); W26 removed from sensors; W27 caption and alt updated on neural, sensors, expanders.
- Airway: W38 ETT insertion-force chart placed with its caption and a minimal internal source; card stat ~60%; opening line and spec-strip evidence updated; cochlear insertion paragraph now introduced as published work showing the same effect.
- Nav, Footer, Base: `/logo.svg?v=2`, `/favicon.png?v=2`. Nav label 'Partner with us' shortened to 'Partner' to match Kam's nav list.
- Body-copy cleanups found by the grep: evidence footnote no longer says 'read from the printed figures'; PEEK body sentence reworded to 'In every PEEK test, the gel tore before the bond let go.'; FCOI policy had five em-dashes (rule 7), replaced by commas.

## Pages (owner's order)

### Home (/)

| Status | Item | Proof (built HTML) |
|---|---|---|
| PASS | Logo uses the cache-busting query | `href="/" aria-label="ZwiCoat home"><img class="brand-logo" src="/logo.svg?v=2" alt="ZwiCoat" width="119" height="40" decoding="async"></a>` |
| PASS | Favicon uses the cache-busting query | `ef="https://zwicoat.com/"><link rel="icon" type="image/png" href="/favicon.png?v=2"><meta property="og:type" content="website"><meta property="` |
| PASS | No unversioned logo reference | `no match: src="/logo\.svg"` |
| PASS | Nav order Technology, Evidence, Durability, Applications, Partner, About | `>Technology</a></li><li><a href="/evidence">Evidence</a></li><li><a href="/durability">Durability</a></li><li class="has-sub" data-sub><button type="button" cla ...` |
| PASS | P1 hero subhead | `to the device, that keeps protein, cells and bacteria off. It means less scarring, lower impedance, easier insertion and fewer bacteria, from a single coating step. The evidence spans ten years of published work.</p><div class="he ...` |
| PASS | P1 old fragment subhead gone | `absent: One coating step. Ten years of evidence.` |
| PASS | P2 sources sentence kept | `ilm have no foothold.</span></li></ul><p class="tiles-note">Every number on this site comes from a published paper, dissertation or issued patent.</p><p class="tiles-note tiles-src label">Sources: the ten j` |
| PASS | P2 replacement sentence absent | `absent: Every number has its source listed under it.` |
| PASS | P3 archive line removed | `absent: 182 archived experiments` |
| PASS | P3 rewritten archive line removed | `absent: 182 documented experiments` |
| PASS | P4 It-stays-on title | `xt"><p class="label">It stays on</p><h2 class="claim-title">Friction was unchanged after three weeks in mice.</h2><div class="claim-body"><p>Coated silicone was implante` |
| PASS | W26 not on home | `absent: W26_sheep_histology` |
| PASS | Less scar row uses rebuilt W27 | `Less scar</p><h2 class="claim-title">A thinner scar capsule around coated implants.</h2><div class="claim-body"><p>In mice, the scar capsule was 67 percent thin ...` |
| PASS | W27 caption has no PEG control | `absent: non-zwitterionic` |
| PASS | Card order neural first, GI last | `<ul class="grid" role="list"><li><a class="card" href="/applications/neural-interfaces"><div class="media media-photo fit-contain"><img src="/images/lab/ci-arra ...` |
| PASS | P9 airway card | `bes</h3><p class="stat">~60%</p><p class="stat-label label">less force to intubate with coated endotracheal tubes in a cadaveric larynx (ZwiCoat internal study, 2026)</p></div></a></li><li><a class="card compact" href="/applic` |
| PASS | P10 indwelling card | `ers</h3><p class="stat">~90%</p><p class="stat-label label">lower friction on coated silicone, still in place after three weeks in mice (Peel 2024)</p></div></a></li><li><a class="card compact" href="/applic` |
| PASS | P11 PEEK card | `/h3><p class="stat">~635 kPa</p><p class="stat-label label">bond strength of the coating on PEEK, dry (ZwiCoat internal tests)</p></div></a></li><li><a class="card compact" href="/applic` |
| PASS | P12 expander card alt | `pct-01.jpg" alt="A tissue expander coated in blue hydrogel, inflated to 300 percent of its rated volume, with the blue coating covering the whole shell." loading="` |
| PASS | No 200 percent wording | `absent: 200 percent` |
| PASS | No regulatory wording on home | `no match: (?i)510\(k\)/\bPMA\b/Master File` |
| PASS | No monomer names on home | `no match: SBMA/CBMA/sulfobetaine/carboxybetaine` |
| PASS | CTA band kept on home | `<div class="band"><div class="band-text"><h2 id="cta-title">Bring us a device with a fouling, scar or friction problem.</h2><p>We coat it free, with no cap on quantity, and return` |
| PASS | U4 footer application order neural first, GI last | `col-apps"><h2 class="label">Applications</h2><ul role="list"><li><a href="/applications/neural-interfaces">Neural interfaces</a></li><li><a href="/applications/ ...` |
| PASS | U4 nav application menu order neural first, GI last | `apps-menu" data-sub-toggle>Applications<svg width="10" height="10" viewBox="0 0 10 10" fill="none" stroke="currentColor" stroke-width="1.6" aria-hidden="true">< ...` |
| PASS | U3 wordmark logo in nav and footer | `brand-logo" src="/logo.svg?v=2" alt="ZwiCoat" width="119" height="40" decoding="async"></a><button class="menu-toggle" type="button" aria-expanded="false" aria- ...` |
| PASS | N4 tile: further patent applications pending, no titles | `tent applications pending</span><span class="tile-takeaway">Further patent applications are pending.</span></li><li class="tile"><span class="tile-value">1 year` |
| PASS | N4 no provisional wording | `absent: provisional` |
| PASS | T2 first sentence of the hero has no monomer name | `<p class="lead">ZwiCoat is a zwitterionic hydrogel coating, covalently bonded to the device` |
| PASS | T10 no process-video element | `no match: process-video/<video[^>]*dipcoat` |
| PASS | E4 tile reads 6 months for sheep | `6 months</span><span class="tile-label label">functional human arrays in sheep` |
| PASS | A3 airway card stat is the ETT number (~60%) | `~60%</p><p class="stat-label label">less force to intubate with coated endotracheal tubes` |
| PASS | Banned-term grep (ZwiGuard, benzophenone, monomer names, scientist/partner names, prestigious, hover or focus, UK spelling, not significant, p values outside sources, em-dash, coming next) | `no hits outside allowed contexts; allowed: read from the in source/reference` |

### Technology

| Status | Item | Proof (built HTML) |
|---|---|---|
| PASS | Logo uses the cache-busting query | `href="/" aria-label="ZwiCoat home"><img class="brand-logo" src="/logo.svg?v=2" alt="ZwiCoat" width="119" height="40" decoding="async"></a>` |
| PASS | Favicon uses the cache-busting query | `/zwicoat.com/technology/"><link rel="icon" type="image/png" href="/favicon.png?v=2"><meta property="og:type" content="website"><meta property="` |
| PASS | No unversioned logo reference | `no match: src="/logo\.svg"` |
| PASS | Nav order Technology, Evidence, Durability, Applications, Partner, About | `>Technology</a></li><li><a href="/evidence">Evidence</a></li><li><a href="/durability">Durability</a></li><li class="has-sub" data-sub><button type="button" cla ...` |
| PASS | P6 first sentence kept | `r that nothing can displace.</h2><div class="claim-body"><p>ZwiCoat is a zwitterionic hydrogel that dramatically lowers friction, infection, inflammation and biofouling.</p><p>Each repeat unit carries a strong dipole. The dipole` |
| PASS | P6 dipole sentences | `ers friction, infection, inflammation and biofouling.</p><p>Each repeat unit carries a strong dipole. The dipole binds tightly to water, creating a hydration barrier between the device and body.</p><p>Proteins, cells and bacteria  ...` |
| PASS | P6 new paragraph | `reating a hydration barrier between the device and body.</p><p>Proteins, cells and bacteria cannot displace that hydration barrier, so they do not stick. The barrier is far stronger than the hydrogen-bonded hydration of PEG, the u ...` |
| PASS | P6 old water-shell sentence removed | `absent: The dipole binds a tightly ordered shell of water.` |
| PASS | P6 old 'hold is stronger' sentence removed | `absent: The hold is stronger` |
| PASS | P6 UV sentences kept | `l., Nature Biotechnology).</p><p>One UV step does two jobs. It covalently bonds the coating to the device surface. The same light crosslinks the network.</p><p>The result is a crosslinked hydrogel anchored to the` |
| PASS | P7 tethered-brush sentence kept | `he result is a crosslinked hydrogel anchored to the device. It is not a thin tethered brush, an adsorbed layer that can wash off, or an additive blended into the polymer.</p></div></div><div class="claim-figure"><figure class="sch` |
| PASS | P8 sterilization paragraph | `by six weeks. The ZwiCoat film did not (Horne 2023).</p><p>The coating is compatible with steam, ethylene oxide, gamma, UV and dry e-beam sterilization, and bond strength held after sterilization and shipping. We validate on your  ...` |
| PASS | W11 chart on page | `, about 5 per group.</span></p><img class="figure-img" src="/figures/W11_sterilization.png" alt="Two panels. Left: the coating was unchanged after ste` |
| PASS | W27 rebuilt text | `of scar capsule thickness in mice, uncoated against coated. Panel A, six weeks on flat silicone sheets: 82 micrometers uncoated and 27 coated. Panel B, one year on human cochlear implant arrays: 47 micr` |
| PASS | No regulatory section | `no match: (?i)510\(k\)/Master File/>Regulatory<` |
| PASS | No visible process-video slot | `no match: (?i)process video: coming` |
| PASS | CTA band kept | `<div class="band"><div class="band-text"><h2 id="cta-title">Bring us a device with a fouling, scar or friction problem.</h2><p>We coat it free, with no cap on quantity, and return` |
| PASS | U4 footer application order neural first, GI last | `col-apps"><h2 class="label">Applications</h2><ul role="list"><li><a href="/applications/neural-interfaces">Neural interfaces</a></li><li><a href="/applications/ ...` |
| PASS | U4 nav application menu order neural first, GI last | `apps-menu" data-sub-toggle>Applications<svg width="10" height="10" viewBox="0 0 10 10" fill="none" stroke="currentColor" stroke-width="1.6" aria-hidden="true">< ...` |
| PASS | U3 wordmark logo in nav and footer | `brand-logo" src="/logo.svg?v=2" alt="ZwiCoat" width="119" height="40" decoding="async"></a><button class="menu-toggle" type="button" aria-expanded="false" aria- ...` |
| PASS | T5 'Silicone is published' block gone | `absent: Silicone is published` |
| PASS | T5 substrates block reads cleanly | `of.</h2></div><div class="block-body"><div class="prose"><p>ZwiCoat has been grafted to silicone, PVC, PEEK, parylene-C and polyurethane, and across platinum contacts. On silicone the bond is stronger than the gel itself: in pu` |
| PASS | T7 W04 hollow-bar sentence gone | `no match: (?i)hollow` |
| PASS | T9 W30 chart on page | `biomaterials.1c00852</span></p><img class="figure-img" src="/figures/W30_crosslinker_tradeoff.png" alt="Charts against crosslinker percentage for the coating` |
| PASS | T8 W31 chart on page | `acs.langmuir.8b00838</span></p><img class="figure-img" src="/figures/W31_bond_strength_vs_grafting_agent.png" alt="Shear bond strength of the zwitterionic film on silic` |
| PASS | T10 no process-video element | `no match: process-video/<video[^>]*dipcoat` |
| PASS | T11 'The partner files' section gone | `absent: The partner files` |
| PASS | Banned-term grep (ZwiGuard, benzophenone, monomer names, scientist/partner names, prestigious, hover or focus, UK spelling, not significant, p values outside sources, em-dash, coming next) | `no hits outside allowed contexts; allowed: SBMA in W30 figure; read from the in source/reference` |

### Evidence

| Status | Item | Proof (built HTML) |
|---|---|---|
| PASS | Logo uses the cache-busting query | `href="/" aria-label="ZwiCoat home"><img class="brand-logo" src="/logo.svg?v=2" alt="ZwiCoat" width="119" height="40" decoding="async"></a>` |
| PASS | Favicon uses the cache-busting query | `://zwicoat.com/evidence/"><link rel="icon" type="image/png" href="/favicon.png?v=2"><meta property="og:type" content="website"><meta property="` |
| PASS | No unversioned logo reference | `no match: src="/logo\.svg"` |
| PASS | Nav order Technology, Evidence, Durability, Applications, Partner, About | `>Technology</a></li><li><a href="/evidence" aria-current="page">Evidence</a></li><li><a href="/durability">Durability</a></li><li class="has-sub" data-sub><butt ...` |
| PASS | Horne dissertation 2024 | `Ryan R. Horne, University of Iowa, 2024` |
| PASS | No Horne 2023 dissertation | `no match: Horne, University of Iowa, 2023` |
| PASS | W26 not on evidence | `absent: W26_sheep_histology` |
| PASS | W27 rebuilt on evidence | `j.actbio.2023.05.011</span></p><img class="figure-img" src="/figures/W27_capsule_thickness_mice.png" alt="Two bar charts of scar capsule thickness in mice, unc` |
| PASS | W27 no PEG control text | `absent: non-zwitterionic` |
| PASS | W25 on evidence | `j.heares.2026.109606</span></p><img class="figure-img" src="/figures/W25_sheep_impedance_components.png" alt="Three bar charts for sheep: total impedance, polariza` |
| PASS | P5 largest device markets tile | `akeaway">United States, Australia, China, Japan and Mexico: the largest device markets.</span></li><li class="tile"><span class="tile-value">More<` |
| PASS | P19 patent note | `/patent/US12116498">US 12,116,498</a><span class="pub-meta">Coated-device system, continuation of the 11,814,526 family: a medical device carrying a covalently grafted zwitterionic hydrogel film.</span></li></ul></div></div></sect ...` |
| PASS | Archive tiles removed | `absent: 182 archived` |
| PASS | CTA band kept | `<div class="band"><div class="band-text"><h2 id="cta-title">Bring us a device with a fouling, scar or friction problem.</h2><p>We coat it free, with no cap on quantity, and return` |
| PASS | U4 footer application order neural first, GI last | `col-apps"><h2 class="label">Applications</h2><ul role="list"><li><a href="/applications/neural-interfaces">Neural interfaces</a></li><li><a href="/applications/ ...` |
| PASS | U4 nav application menu order neural first, GI last | `apps-menu" data-sub-toggle>Applications<svg width="10" height="10" viewBox="0 0 10 10" fill="none" stroke="currentColor" stroke-width="1.6" aria-hidden="true">< ...` |
| PASS | U3 wordmark logo in nav and footer | `brand-logo" src="/logo.svg?v=2" alt="ZwiCoat" width="119" height="40" decoding="async"></a><button class="menu-toggle" type="button" aria-expanded="false" aria- ...` |
| PASS | E2 timeline not on evidence | `absent: W24_publication_timeline` |
| PASS | E3 section order: scar first, antifouling second | `id="scar" aria-labelledby="scar-h"><div class="ev-head"><p class="label ev-num">01</p><h2 id="scar-h">Scar tissue</h2><p class="ev-text">Capsules were thinner a ...` |
| PASS | E9 impedance below insertion and friction | `id="insertion-friction" aria-labelledby="insertion-friction-h"><div class="ev-head"><p class="label ev-num">03</p><h2 id="insertion-friction-h">Insertion force  ...` |
| PASS | E10 W08 rendered at 640 px | `W08_impedance_sheep.png" alt="Bar chart of total electrode impedance in sheep for coated and uncoated cochlear implant arrays, at implantation and at four weeks ...` |
| PASS | E4 tile reads 6 months for sheep | `6 months</span><span class="tile-label label">functional human arrays in sheep` |
| PASS | E5 archive tiles removed | `absent: 1,056` |
| PASS | E6 archive source line, plain wording, last line of the page body | `Archive counts: ZwiCoat Data archive.</p></div>` |
| PASS | E6 no E-report method-tag wording | `absent: E-report method tags` |
| PASS | E8 sheep histology photo on evidence | `frame fit-cover" style="aspect-ratio: 1750/1150;"><img src="/images/histology-sheep.png" alt="Four tissue sections of a sheep cochlea. The top row` |
| PASS | N4 no provisional wording | `absent: provisional` |
| PASS | T7 no hollow-bar wording | `no match: (?i)hollow` |
| PASS | E11 W37 not placed (held for review, see VERIFY) | `absent: W37_ci_insertion_synthetic` |
| PASS | Banned-term grep (ZwiGuard, benzophenone, monomer names, scientist/partner names, prestigious, hover or focus, UK spelling, not significant, p values outside sources, em-dash, coming next) | `no hits outside allowed contexts; allowed: SBMA in W30 figure; read from the in source/reference` |

### Durability

| Status | Item | Proof (built HTML) |
|---|---|---|
| PASS | Logo uses the cache-busting query | `href="/" aria-label="ZwiCoat home"><img class="brand-logo" src="/logo.svg?v=2" alt="ZwiCoat" width="119" height="40" decoding="async"></a>` |
| PASS | Favicon uses the cache-busting query | `/zwicoat.com/durability/"><link rel="icon" type="image/png" href="/favicon.png?v=2"><meta property="og:type" content="website"><meta property="` |
| PASS | No unversioned logo reference | `no match: src="/logo\.svg"` |
| PASS | Nav order Technology, Evidence, Durability, Applications, Partner, About | `>Technology</a></li><li><a href="/evidence">Evidence</a></li><li><a href="/durability" aria-current="page">Durability</a></li><li class="has-sub" data-sub><butt ...` |
| PASS | P4 title restored | `xt"><p class="label">In the body</p><h2 class="claim-title">Friction was unchanged after three weeks in mice.</h2><div class="claim-body"><p>Coated silicone was implante` |
| PASS | P4 replacement title absent | `absent: Friction stayed about 90 percent lower` |
| PASS | P8 sterilization paragraph | `tiple sterilization methods.</h2><div class="claim-body"><p>The coating is compatible with steam, ethylene oxide, gamma, UV and dry e-beam sterilization, and bond strength held after sterilization and shipping. We validate on your ...` |
| PASS | Old tally sentence gone | `absent: Wet e-beam did not pass` |
| PASS | Positive sterilization header | `abel">Sterilization and shipping</p><h2 class="claim-title">Compatible with multiple sterilization methods.</h2><div class="claim-body"><p>The coating is compatible wi` |
| PASS | W11 chart (8 tiles, wet e-beam failed in image) | `, about 5 per group.</span></p><img class="figure-img" src="/figures/W11_sterilization.png" alt="Two panels. Left: the coating was unchanged after ste` |
| PASS | U4 footer application order neural first, GI last | `col-apps"><h2 class="label">Applications</h2><ul role="list"><li><a href="/applications/neural-interfaces">Neural interfaces</a></li><li><a href="/applications/ ...` |
| PASS | U4 nav application menu order neural first, GI last | `apps-menu" data-sub-toggle>Applications<svg width="10" height="10" viewBox="0 0 10 10" fill="none" stroke="currentColor" stroke-width="1.6" aria-hidden="true">< ...` |
| PASS | U3 wordmark logo in nav and footer | `brand-logo" src="/logo.svg?v=2" alt="ZwiCoat" width="119" height="40" decoding="async"></a><button class="menu-toggle" type="button" aria-expanded="false" aria- ...` |
| PASS | N1/D1 W35 wear chart | `.1021/acsabm.4c00156</span></p><img class="figure-img" src="/figures/W35_wear_2500_passes.png" alt="Bar chart of friction relative to bare silicone, firs` |
| PASS | N1/D1 W36 dry and re-wet chart | `.1021/acsabm.4c00156</span></p><img class="figure-img" src="/figures/W36_dry_and_rewet.png" alt="Two charts. Panel A: minutes to the first crack when` |
| PASS | D2 'not shown yet' block gone | `no match: (?i)not shown yet/come next` |
| PASS | D3 W28a at full row width | `W28a_friction_after_explant.png" alt="Bar chart of the friction coefficient of uncoated and coated silicone, before and after three weeks implanted in mice. Coa ...` |
| PASS | D4 pendulum close-up clip | `pendulum-loop.webm"` |
| PASS | D5 W31 chart with grafting-agent axis | `acs.langmuir.8b00838</span></p><img class="figure-img" src="/figures/W31_bond_strength_vs_grafting_agent.png" alt="Shear bond strength of the zwitterionic film on silic` |
| PASS | D7 no 'intact' in the sterilization row | `no match: Sterilization and shipping.{0,1500}?intact` |
| PASS | D8 only panel A friction chart (W28a), not the two-panel W28 | `absent: W28_durability_peel` |
| PASS | Banned-term grep (ZwiGuard, benzophenone, monomer names, scientist/partner names, prestigious, hover or focus, UK spelling, not significant, p values outside sources, em-dash, coming next) | `no hits outside allowed contexts; allowed: read from the in source/reference` |

### Applications index

| Status | Item | Proof (built HTML) |
|---|---|---|
| PASS | Logo uses the cache-busting query | `href="/" aria-label="ZwiCoat home"><img class="brand-logo" src="/logo.svg?v=2" alt="ZwiCoat" width="119" height="40" decoding="async"></a>` |
| PASS | Favicon uses the cache-busting query | `wicoat.com/applications/"><link rel="icon" type="image/png" href="/favicon.png?v=2"><meta property="og:type" content="website"><meta property="` |
| PASS | No unversioned logo reference | `no match: src="/logo\.svg"` |
| PASS | Nav order Technology, Evidence, Durability, Applications, Partner, About | `>Technology</a></li><li><a href="/evidence">Evidence</a></li><li><a href="/durability">Durability</a></li><li class="has-sub" data-sub><button type="button" cla ...` |
| PASS | Card order neural first, GI last | `<ul class="grid" role="list"><li><a class="card" href="/applications/neural-interfaces"><div class="media media-photo fit-contain"><img src="/images/lab/ci-arra ...` |
| PASS | P9 airway card | `bes</h3><p class="stat">~60%</p><p class="stat-label label">less force to intubate with coated endotracheal tubes in a cadaveric larynx (ZwiCoat internal study, 2026)</p></div></a></li><li><a class="card compact" href="/applic` |
| PASS | P10 indwelling card | `ers</h3><p class="stat">~90%</p><p class="stat-label label">lower friction on coated silicone, still in place after three weeks in mice (Peel 2024)</p></div></a></li><li><a class="card compact" href="/applic` |
| PASS | P11 PEEK card | `/h3><p class="stat">~635 kPa</p><p class="stat-label label">bond strength of the coating on PEEK, dry (ZwiCoat internal tests)</p></div></a></li><li><a class="card compact" href="/applic` |
| PASS | P12 expander card alt | `pct-01.jpg" alt="A tissue expander coated in blue hydrogel, inflated to 300 percent of its rated volume, with the blue coating covering the whole shell." loading="` |
| PASS | No 200 percent wording | `absent: 200 percent` |
| PASS | U4 footer application order neural first, GI last | `col-apps"><h2 class="label">Applications</h2><ul role="list"><li><a href="/applications/neural-interfaces">Neural interfaces</a></li><li><a href="/applications/ ...` |
| PASS | U4 nav application menu order neural first, GI last | `apps-menu" data-sub-toggle>Applications<svg width="10" height="10" viewBox="0 0 10 10" fill="none" stroke="currentColor" stroke-width="1.6" aria-hidden="true">< ...` |
| PASS | U3 wordmark logo in nav and footer | `brand-logo" src="/logo.svg?v=2" alt="ZwiCoat" width="119" height="40" decoding="async"></a><button class="menu-toggle" type="button" aria-expanded="false" aria- ...` |
| PASS | A3 airway card stat is the ETT number (~60%) | `~60%</p><p class="stat-label label">less force to intubate with coated endotracheal tubes` |
| PASS | Banned-term grep (ZwiGuard, benzophenone, monomer names, scientist/partner names, prestigious, hover or focus, UK spelling, not significant, p values outside sources, em-dash, coming next) | `no hits outside allowed contexts` |

### 1. Neural interfaces

| Status | Item | Proof (built HTML) |
|---|---|---|
| PASS | Logo uses the cache-busting query | `href="/" aria-label="ZwiCoat home"><img class="brand-logo" src="/logo.svg?v=2" alt="ZwiCoat" width="119" height="40" decoding="async"></a>` |
| PASS | Favicon uses the cache-busting query | `tions/neural-interfaces/"><link rel="icon" type="image/png" href="/favicon.png?v=2"><meta property="og:type" content="website"><meta property="` |
| PASS | No unversioned logo reference | `no match: src="/logo\.svg"` |
| PASS | Nav order Technology, Evidence, Durability, Applications, Partner, About | `>Technology</a></li><li><a href="/evidence">Evidence</a></li><li><a href="/durability">Durability</a></li><li class="has-sub" data-sub><button type="button" cla ...` |
| PASS | P23 opener removed | `absent: What follows is our design rationale` |
| PASS | P23 rationale in plain voice | `0156.</p></figcaption></figure></div><div class="prose"> <p><strong>Why this matters for the next generation of electrodes.</strong> A zwitterionic hydrogel is wet, ion-rich and tightly bound to the metal. At the contact it raises ...` |
| PASS | W26 stays on neural | `j.heares.2026.109606</span></p><img class="figure-img" src="/figures/W26_sheep_histology.png" alt="Three small charts comparing uncoated and coated arra` |
| PASS | W25 on neural | `j.heares.2026.109606</span></p><img class="figure-img" src="/figures/W25_sheep_impedance_components.png" alt="Three small bar charts of electrode impedance in kilo` |
| PASS | Sheep histology photo (Coated label repainted) | `frame fit-cover" style="aspect-ratio: 1750/1150;"><img src="/images/histology-sheep.png" alt="Tissue sections from the base of a sheep cochlea at t` |
| PASS | W27 rebuilt text | `against coated. Panel A, six weeks on flat silicone sheets: 82 micrometers uncoated and 27 coated. Panel B, one year on human cochlear implant arrays: 47 mic` |
| PASS | U4 footer application order neural first, GI last | `col-apps"><h2 class="label">Applications</h2><ul role="list"><li><a href="/applications/neural-interfaces">Neural interfaces</a></li><li><a href="/applications/ ...` |
| PASS | U4 nav application menu order neural first, GI last | `apps-menu" data-sub-toggle>Applications<svg width="10" height="10" viewBox="0 0 10 10" fill="none" stroke="currentColor" stroke-width="1.6" aria-hidden="true">< ...` |
| PASS | U3 wordmark logo in nav and footer | `brand-logo" src="/logo.svg?v=2" alt="ZwiCoat" width="119" height="40" decoding="async"></a><button class="menu-toggle" type="button" aria-expanded="false" aria- ...` |
| PASS | NI1 leads with sheep histology | `class="lead-media"><div class="fig"><figure class="photo" style="--ratio: 1.5217;"><div class="photo-box"><p class="fig-tag" aria-hidden="true"><span class="fig ...` |
| PASS | NI2 conceals the platinum, texturing | `voltage and a smaller contact can deliver the same charge. Because the coating conceals the platinum from tissue, contact surfaces can be textured for even more surface area without inviting more scar.</p> <p>Lower impedance, smal ...` |
| PASS | NI2 capacitance and smaller contacts | `c hydrogel is wet, ion-rich and tightly bound to the metal. At the contact it raises the capacity to store charge at the electrode surface, so the same stimulus needs less voltage and a smaller contact can deliver the same charge. ...` |
| PASS | NI3 problem paragraph | `ph pending Kam --> <h2 id="the-problem">The problem</h2> <p>A neural electrode works or fails at one place: the interface between the device and tissue. Within seconds of implantation, proteins coat the array, an` |
| PASS | E11 W37 not placed (held for review, see VERIFY) | `absent: W37_ci_insertion_synthetic` |
| PASS | T12 regulatory: exactly one line, in the spec strip | `Regulatory path PMA supplement with our Master File behind your submission Evidence mice, one year; sheep, four weeks (six months in preparation); human cadaveric cochlea [spec-strip count=1; regulatory mentions in the article bod ...` |
| PASS | Banned-term grep (ZwiGuard, benzophenone, monomer names, scientist/partner names, prestigious, hover or focus, UK spelling, not significant, p values outside sources, em-dash, coming next) | `no hits outside allowed contexts; allowed: read from the in source/reference` |

### 2. Tissue expanders and breast implants

| Status | Item | Proof (built HTML) |
|---|---|---|
| PASS | Logo uses the cache-busting query | `href="/" aria-label="ZwiCoat home"><img class="brand-logo" src="/logo.svg?v=2" alt="ZwiCoat" width="119" height="40" decoding="async"></a>` |
| PASS | Favicon uses the cache-busting query | `ations/tissue-expanders/"><link rel="icon" type="image/png" href="/favicon.png?v=2"><meta property="og:type" content="website"><meta property="` |
| PASS | No unversioned logo reference | `no match: src="/logo\.svg"` |
| PASS | Nav order Technology, Evidence, Durability, Applications, Partner, About | `>Technology</a></li><li><a href="/evidence">Evidence</a></li><li><a href="/durability">Durability</a></li><li class="has-sub" data-sub><button type="button" cla ...` |
| PASS | P12 300 percent sentence | `ted at day 21 (Shen 2021).</p> <p><strong>Stretch.</strong> A coated expander inflated to 300 percent of its rated volume kept the coating across the whole shell (ZwiCoat internal test, 2026).</p> <h2 id="how-it-fits-your-process" ...` |
| PASS | No 200 percent wording | `absent: 200 percent` |
| PASS | Contradicting 'whether the film stretches' line removed | `absent: Whether the film stretches` |
| PASS | W27 rebuilt text | `against coated. Panel A, six weeks on flat silicone sheets: 82 micrometers uncoated and 27 coated. Panel B, one year on human cochlear implant arrays: 47 mic` |
| PASS | U4 footer application order neural first, GI last | `col-apps"><h2 class="label">Applications</h2><ul role="list"><li><a href="/applications/neural-interfaces">Neural interfaces</a></li><li><a href="/applications/ ...` |
| PASS | U4 nav application menu order neural first, GI last | `apps-menu" data-sub-toggle>Applications<svg width="10" height="10" viewBox="0 0 10 10" fill="none" stroke="currentColor" stroke-width="1.6" aria-hidden="true">< ...` |
| PASS | U3 wordmark logo in nav and footer | `brand-logo" src="/logo.svg?v=2" alt="ZwiCoat" width="119" height="40" decoding="async"></a><button class="menu-toggle" type="button" aria-expanded="false" aria- ...` |
| PASS | T12 regulatory: exactly one line, in the spec strip | `Regulatory path 510(k) for expanders and PMA supplement for implants, with our Master File behind each submission Evidence mice, six weeks to one year; rats, 21 days; lab [spec-strip count=1; regulatory mentions in the article bod ...` |
| PASS | Banned-term grep (ZwiGuard, benzophenone, monomer names, scientist/partner names, prestigious, hover or focus, UK spelling, not significant, p values outside sources, em-dash, coming next) | `no hits outside allowed contexts; allowed: p < 0 in source line; p = 0 in source line; read from the in source/reference` |

### 3. Airway tubes

| Status | Item | Proof (built HTML) |
|---|---|---|
| PASS | Logo uses the cache-busting query | `href="/" aria-label="ZwiCoat home"><img class="brand-logo" src="/logo.svg?v=2" alt="ZwiCoat" width="119" height="40" decoding="async"></a>` |
| PASS | Favicon uses the cache-busting query | `com/applications/airway/"><link rel="icon" type="image/png" href="/favicon.png?v=2"><meta property="og:type" content="website"><meta property="` |
| PASS | No unversioned logo reference | `no match: src="/logo\.svg"` |
| PASS | Nav order Technology, Evidence, Durability, Applications, Partner, About | `>Technology</a></li><li><a href="/evidence">Evidence</a></li><li><a href="/durability">Durability</a></li><li class="has-sub" data-sub><button type="button" cla ...` |
| PASS | P13 standfirst | `ay tubes / ZwiCoat</title><meta name="description" content="ZwiCoat is a drug-free coating that enhances mucus flow, resists bacteria and lowers friction, and it has been tested on endotracheal tubes."><link rel="canonical" href=" ...` |
| PASS | U4 footer application order neural first, GI last | `col-apps"><h2 class="label">Applications</h2><ul role="list"><li><a href="/applications/neural-interfaces">Neural interfaces</a></li><li><a href="/applications/ ...` |
| PASS | U4 nav application menu order neural first, GI last | `apps-menu" data-sub-toggle>Applications<svg width="10" height="10" viewBox="0 0 10 10" fill="none" stroke="currentColor" stroke-width="1.6" aria-hidden="true">< ...` |
| PASS | U3 wordmark logo in nav and footer | `brand-logo" src="/logo.svg?v=2" alt="ZwiCoat" width="119" height="40" decoding="async"></a><button class="menu-toggle" type="button" aria-expanded="false" aria- ...` |
| PASS | A1 leads with the cuff clip | `class="lead-media"><div class="fig pair"><div class="pair-item"><figure class="vl" style="--ratio: 0.5625;"><div class="vl-box"><p class="fig-tag" aria-hidden=" ...` |
| PASS | A3 W38 ETT insertion-force chart on the page | `0459478 (CC BY 4.0).</span></p><img class="figure-img" src="/figures/W38_ett_insertion_force.png" alt="Four panels of endotracheal tube insertion force in a` |
| PASS | A3 W38 caption | `surgeons intubated a cadaveric human larynx on a load cell. Coated endotracheal tubes needed 62 percent (Surgeon 1) and 61 percent (Surgeon 2) less integrated insertion force than the uncoated tube.</p><p class="figure-source labe ...` |
| PASS | A3 W38 internal source, minimal citation | `Source: ZwiCoat internal study, 2026 (1 uncoated and 3 coated tubes per surgeon` |
| PASS | A3 ETT result in the body copy | `ed a cadaveric human larynx with coated and uncoated tubes. Coated tubes needed about 60 percent less insertion force, for both surgeons (ZwiCoat internal study, 2026).</p> </div><div class="fig"><figure class="figure"><div clas` |
| PASS | A2 stenosis before pneumonia | `Stenosis comes first. A rigid tube scrapes the larynx on the way in, and the airway reacts to it for as long as the tube stays. In a review of nine studies, 83  ...` |
| PASS | A2 stenosis citations resolved in references | `<li>Brodsky MB, Levy MJ, Jedlanek E, et al. Laryngeal injury and upper airway symptoms after oral endotracheal intubation with mechanical ventilation during cri ...` |
| PASS | T12 regulatory: exactly one line, in the spec strip | `Regulatory path 510(k) path with our Master File behind your submission Evidence coated endotracheal tubes in a cadaveric larynx (ZwiCoat internal study, 2026); mucus-flo [spec-strip count=1; regulatory mentions in the article bod ...` |
| PASS | Banned-term grep (ZwiGuard, benzophenone, monomer names, scientist/partner names, prestigious, hover or focus, UK spelling, not significant, p values outside sources, em-dash, coming next) | `no hits outside allowed contexts; allowed: p < 0 in source line; read from the in source/reference` |

### 4. Vascular access

| Status | Item | Proof (built HTML) |
|---|---|---|
| PASS | Logo uses the cache-busting query | `href="/" aria-label="ZwiCoat home"><img class="brand-logo" src="/logo.svg?v=2" alt="ZwiCoat" width="119" height="40" decoding="async"></a>` |
| PASS | Favicon uses the cache-busting query | `cations/vascular-access/"><link rel="icon" type="image/png" href="/favicon.png?v=2"><meta property="og:type" content="website"><meta property="` |
| PASS | No unversioned logo reference | `no match: src="/logo\.svg"` |
| PASS | Nav order Technology, Evidence, Durability, Applications, Partner, About | `>Technology</a></li><li><a href="/evidence">Evidence</a></li><li><a href="/durability">Durability</a></li><li class="has-sub" data-sub><button type="button" cla ...` |
| PASS | Page builds with references | `l="References"><details class="refs"><summary class="label">References (13)</summary><ol class="refs-list"><li>Leigh BL, Cheng E, Xu` |
| PASS | U4 footer application order neural first, GI last | `col-apps"><h2 class="label">Applications</h2><ul role="list"><li><a href="/applications/neural-interfaces">Neural interfaces</a></li><li><a href="/applications/ ...` |
| PASS | U4 nav application menu order neural first, GI last | `apps-menu" data-sub-toggle>Applications<svg width="10" height="10" viewBox="0 0 10 10" fill="none" stroke="currentColor" stroke-width="1.6" aria-hidden="true">< ...` |
| PASS | U3 wordmark logo in nav and footer | `brand-logo" src="/logo.svg?v=2" alt="ZwiCoat" width="119" height="40" decoding="async"></a><button class="menu-toggle" type="button" aria-expanded="false" aria- ...` |
| PASS | T12 regulatory: exactly one line, in the spec strip | `Regulatory path 510(k) path with our Master File behind your submission Evidence in vitro; rats, up to 21 days; mice, one year under the skin FIG W05 Leigh BL, et al. Bi [spec-strip count=1; regulatory mentions in the article body ...` |
| PASS | Banned-term grep (ZwiGuard, benzophenone, monomer names, scientist/partner names, prestigious, hover or focus, UK spelling, not significant, p values outside sources, em-dash, coming next) | `no hits outside allowed contexts; allowed: p < 0 in source line; read from the in source/reference; sulfobetaine in title of a published reference` |

### 5. Indwelling catheters

| Status | Item | Proof (built HTML) |
|---|---|---|
| PASS | Logo uses the cache-busting query | `href="/" aria-label="ZwiCoat home"><img class="brand-logo" src="/logo.svg?v=2" alt="ZwiCoat" width="119" height="40" decoding="async"></a>` |
| PASS | Favicon uses the cache-busting query | `ns/indwelling-catheters/"><link rel="icon" type="image/png" href="/favicon.png?v=2"><meta property="og:type" content="website"><meta property="` |
| PASS | No unversioned logo reference | `no match: src="/logo\.svg"` |
| PASS | Nav order Technology, Evidence, Durability, Applications, Partner, About | `>Technology</a></li><li><a href="/evidence">Evidence</a></li><li><a href="/durability">Durability</a></li><li class="has-sub" data-sub><button type="button" cla ...` |
| PASS | Page builds with references | `l="References"><details class="refs"><summary class="label">References (10)</summary><ol class="refs-list"><li>Centers for Disease C` |
| PASS | U4 footer application order neural first, GI last | `col-apps"><h2 class="label">Applications</h2><ul role="list"><li><a href="/applications/neural-interfaces">Neural interfaces</a></li><li><a href="/applications/ ...` |
| PASS | U4 nav application menu order neural first, GI last | `apps-menu" data-sub-toggle>Applications<svg width="10" height="10" viewBox="0 0 10 10" fill="none" stroke="currentColor" stroke-width="1.6" aria-hidden="true">< ...` |
| PASS | U3 wordmark logo in nav and footer | `brand-logo" src="/logo.svg?v=2" alt="ZwiCoat" width="119" height="40" decoding="async"></a><button class="menu-toggle" type="button" aria-expanded="false" aria- ...` |
| PASS | T12 regulatory: exactly one line, in the spec strip | `Regulatory path 510(k) path with our Master File behind your submission Evidence in vitro; rats, up to 21 days; mice, one year under the skin FIG W18 Pickard R, Lam T, Ma [spec-strip count=1; regulatory mentions in the article bod ...` |
| PASS | Banned-term grep (ZwiGuard, benzophenone, monomer names, scientist/partner names, prestigious, hover or focus, UK spelling, not significant, p values outside sources, em-dash, coming next) | `no hits outside allowed contexts; allowed: read from the in source/reference` |

### 6. PEEK and orthopedic

| Status | Item | Proof (built HTML) |
|---|---|---|
| PASS | Logo uses the cache-busting query | `href="/" aria-label="ZwiCoat home"><img class="brand-logo" src="/logo.svg?v=2" alt="ZwiCoat" width="119" height="40" decoding="async"></a>` |
| PASS | Favicon uses the cache-busting query | `ons/peek-and-orthopedic/"><link rel="icon" type="image/png" href="/favicon.png?v=2"><meta property="og:type" content="website"><meta property="` |
| PASS | No unversioned logo reference | `no match: src="/logo\.svg"` |
| PASS | Nav order Technology, Evidence, Durability, Applications, Partner, About | `>Technology</a></li><li><a href="/evidence">Evidence</a></li><li><a href="/durability">Durability</a></li><li class="has-sub" data-sub><button type="button" cla ...` |
| PASS | P15 standfirst | `<p class="lead">ZwiCoat is a drug-free coating that grafts directly to PEEK with no primer.</p>` |
| PASS | P16 rat cranioplasty sentence | `id="what-zwicoat-does-here">What ZwiCoat does here</h2> <p>In a rat cranioplasty model, animals with coated PEEK implants recovered balance-beam performance faster than those with uncoated implants (manuscript in preparation). The ...` |
| PASS | P16 'under way' removed | `absent: under way` |
| PASS | W34 short caption | `gth of the coating on PEEK is among the highest we measure. PEEK takes part in the grafting step, so no primer is needed, and the gel tears before the bond lets go.</p><p class="figure-source label">Source: ZwiCoat internal` |
| PASS | W34 old long annotation text gone | `absent: Every PEEK test ended` |
| PASS | U4 footer application order neural first, GI last | `col-apps"><h2 class="label">Applications</h2><ul role="list"><li><a href="/applications/neural-interfaces">Neural interfaces</a></li><li><a href="/applications/ ...` |
| PASS | U4 nav application menu order neural first, GI last | `apps-menu" data-sub-toggle>Applications<svg width="10" height="10" viewBox="0 0 10 10" fill="none" stroke="currentColor" stroke-width="1.6" aria-hidden="true">< ...` |
| PASS | U3 wordmark logo in nav and footer | `brand-logo" src="/logo.svg?v=2" alt="ZwiCoat" width="119" height="40" decoding="async"></a><button class="menu-toggle" type="button" aria-expanded="false" aria- ...` |
| PASS | M3 'PEEK: none published' gone | `absent: none published` |
| PASS | M3 rats, cranioplasty wording | `</dt><dd>silicone: in vitro; rats, 21 days; mice, one year; PEEK: rats, cranioplasty model (manuscript in preparation); bench adhesion on PEEK</dd></d` |
| PASS | N2 W34 on the PEEK page | `tests, 2025 to 2026</span></p><img class="figure-img" src="/figures/W34_peek_bond_strength.png" alt="Two bar charts of lap-shear bond strength of the coat` |
| PASS | N2 no cranioplasty paper figures posted | `no match: (?i)src="/(figures/images)[^"]*cranio` |
| PASS | T12 regulatory: exactly one line, in the spec strip | `Regulatory path 510(k) or PMA supplement path with our Master File behind your submission Evidence silicone: in vitro; rats, 21 days; mice, one year; PEEK: rats, craniopl [spec-strip count=1; regulatory mentions in the article bod ...` |
| PASS | Banned-term grep (ZwiGuard, benzophenone, monomer names, scientist/partner names, prestigious, hover or focus, UK spelling, not significant, p values outside sources, em-dash, coming next) | `no hits outside allowed contexts; allowed: read from the in source/reference` |

### 7. Sensors

| Status | Item | Proof (built HTML) |
|---|---|---|
| PASS | Logo uses the cache-busting query | `href="/" aria-label="ZwiCoat home"><img class="brand-logo" src="/logo.svg?v=2" alt="ZwiCoat" width="119" height="40" decoding="async"></a>` |
| PASS | Favicon uses the cache-busting query | `om/applications/sensors/"><link rel="icon" type="image/png" href="/favicon.png?v=2"><meta property="og:type" content="website"><meta property="` |
| PASS | No unversioned logo reference | `no match: src="/logo\.svg"` |
| PASS | Nav order Technology, Evidence, Durability, Applications, Partner, About | `>Technology</a></li><li><a href="/evidence">Evidence</a></li><li><a href="/durability">Durability</a></li><li class="has-sub" data-sub><button type="button" cla ...` |
| PASS | P14 standfirst trimmed | `<p class="lead">ZwiCoat is a drug-free coating tested for scar capsule thickness on silicone and implant arrays.</p>` |
| PASS | P14 'still to be measured' removed | `absent: still to be measured` |
| PASS | W26 removed from sensors | `absent: W26_sheep_histology` |
| PASS | U4 footer application order neural first, GI last | `col-apps"><h2 class="label">Applications</h2><ul role="list"><li><a href="/applications/neural-interfaces">Neural interfaces</a></li><li><a href="/applications/ ...` |
| PASS | U4 nav application menu order neural first, GI last | `apps-menu" data-sub-toggle>Applications<svg width="10" height="10" viewBox="0 0 10 10" fill="none" stroke="currentColor" stroke-width="1.6" aria-hidden="true">< ...` |
| PASS | U3 wordmark logo in nav and footer | `brand-logo" src="/logo.svg?v=2" alt="ZwiCoat" width="119" height="40" decoding="async"></a><button class="menu-toggle" type="button" aria-expanded="false" aria- ...` |
| PASS | T12 regulatory: exactly one line, in the spec strip | `Regulatory path 510(k) or PMA supplement path with our Master File behind your submission Evidence mice, six weeks to one year (silicone and arrays) FIG W20 McClatchey P [spec-strip count=1; regulatory mentions in the article body ...` |
| PASS | Banned-term grep (ZwiGuard, benzophenone, monomer names, scientist/partner names, prestigious, hover or focus, UK spelling, not significant, p values outside sources, em-dash, coming next) | `no hits outside allowed contexts; allowed: SBMA in W30 figure; read from the in source/reference` |

### 8. ENT and feeding tubes

| Status | Item | Proof (built HTML) |
|---|---|---|
| PASS | Logo uses the cache-busting query | `href="/" aria-label="ZwiCoat home"><img class="brand-logo" src="/logo.svg?v=2" alt="ZwiCoat" width="119" height="40" decoding="async"></a>` |
| PASS | Favicon uses the cache-busting query | `/applications/ent-tubes/"><link rel="icon" type="image/png" href="/favicon.png?v=2"><meta property="og:type" content="website"><meta property="` |
| PASS | No unversioned logo reference | `no match: src="/logo\.svg"` |
| PASS | Nav order Technology, Evidence, Durability, Applications, Partner, About | `>Technology</a></li><li><a href="/evidence">Evidence</a></li><li><a href="/durability">Durability</a></li><li class="has-sub" data-sub><button type="button" cla ...` |
| PASS | Page builds with references | `l="References"><details class="refs"><summary class="label">References (9)</summary><ol class="refs-list"><li>Horne R, Escudero C, E` |
| PASS | U4 footer application order neural first, GI last | `col-apps"><h2 class="label">Applications</h2><ul role="list"><li><a href="/applications/neural-interfaces">Neural interfaces</a></li><li><a href="/applications/ ...` |
| PASS | U4 nav application menu order neural first, GI last | `apps-menu" data-sub-toggle>Applications<svg width="10" height="10" viewBox="0 0 10 10" fill="none" stroke="currentColor" stroke-width="1.6" aria-hidden="true">< ...` |
| PASS | U3 wordmark logo in nav and footer | `brand-logo" src="/logo.svg?v=2" alt="ZwiCoat" width="119" height="40" decoding="async"></a><button class="menu-toggle" type="button" aria-expanded="false" aria- ...` |
| PASS | T12 regulatory: exactly one line, in the spec strip | `Regulatory path 510(k) path with our Master File behind your submission Evidence mucus-flow bench model (published); in vitro; rats, 21 days FIG W21 Horne R, Escudero C,  [spec-strip count=1; regulatory mentions in the article bod ...` |
| PASS | Banned-term grep (ZwiGuard, benzophenone, monomer names, scientist/partner names, prestigious, hover or focus, UK spelling, not significant, p values outside sources, em-dash, coming next) | `no hits outside allowed contexts; allowed: p < 0 in source line; read from the in source/reference` |

### 9. GI stents

| Status | Item | Proof (built HTML) |
|---|---|---|
| PASS | Logo uses the cache-busting query | `href="/" aria-label="ZwiCoat home"><img class="brand-logo" src="/logo.svg?v=2" alt="ZwiCoat" width="119" height="40" decoding="async"></a>` |
| PASS | Favicon uses the cache-busting query | `/applications/gi-stents/"><link rel="icon" type="image/png" href="/favicon.png?v=2"><meta property="og:type" content="website"><meta property="` |
| PASS | No unversioned logo reference | `no match: src="/logo\.svg"` |
| PASS | Nav order Technology, Evidence, Durability, Applications, Partner, About | `>Technology</a></li><li><a href="/evidence">Evidence</a></li><li><a href="/durability">Durability</a></li><li class="has-sub" data-sub><button type="button" cla ...` |
| PASS | Page builds with references | `l="References"><details class="refs"><summary class="label">References (12)</summary><ol class="refs-list"><li>Donelli G, Guaglianon` |
| PASS | U4 footer application order neural first, GI last | `col-apps"><h2 class="label">Applications</h2><ul role="list"><li><a href="/applications/neural-interfaces">Neural interfaces</a></li><li><a href="/applications/ ...` |
| PASS | U4 nav application menu order neural first, GI last | `apps-menu" data-sub-toggle>Applications<svg width="10" height="10" viewBox="0 0 10 10" fill="none" stroke="currentColor" stroke-width="1.6" aria-hidden="true">< ...` |
| PASS | U3 wordmark logo in nav and footer | `brand-logo" src="/logo.svg?v=2" alt="ZwiCoat" width="119" height="40" decoding="async"></a><button class="menu-toggle" type="button" aria-expanded="false" aria- ...` |
| PASS | T12 regulatory: exactly one line, in the spec strip | `Regulatory path 510(k) path with our Master File behind your submission Evidence mucus-flow bench model; in vitro; rats, 21 days; mice, one year under the skin FIG W29 Sh [spec-strip count=1; regulatory mentions in the article bod ...` |
| PASS | Banned-term grep (ZwiGuard, benzophenone, monomer names, scientist/partner names, prestigious, hover or focus, UK spelling, not significant, p values outside sources, em-dash, coming next) | `no hits outside allowed contexts; allowed: read from the in source/reference` |

### Partner

| Status | Item | Proof (built HTML) |
|---|---|---|
| PASS | Logo uses the cache-busting query | `href="/" aria-label="ZwiCoat home"><img class="brand-logo" src="/logo.svg?v=2" alt="ZwiCoat" width="119" height="40" decoding="async"></a>` |
| PASS | Favicon uses the cache-busting query | `s://zwicoat.com/partner/"><link rel="icon" type="image/png" href="/favicon.png?v=2"><meta property="og:type" content="website"><meta property="` |
| PASS | No unversioned logo reference | `no match: src="/logo\.svg"` |
| PASS | Nav order Technology, Evidence, Durability, Applications, Partner, About | `>Technology</a></li><li><a href="/evidence">Evidence</a></li><li><a href="/durability">Durability</a></li><li class="has-sub" data-sub><button type="button" cla ...` |
| PASS | P8 sterilization paragraph | `ter-h">Sterilization and shipping</h2><div class="prose"><p>The coating is compatible with steam, ethylene oxide, gamma, UV and dry e-beam sterilization, and bond strength held after sterilization and shipping. We validate on your ...` |
| PASS | U4 footer application order neural first, GI last | `col-apps"><h2 class="label">Applications</h2><ul role="list"><li><a href="/applications/neural-interfaces">Neural interfaces</a></li><li><a href="/applications/ ...` |
| PASS | U4 nav application menu order neural first, GI last | `apps-menu" data-sub-toggle>Applications<svg width="10" height="10" viewBox="0 0 10 10" fill="none" stroke="currentColor" stroke-width="1.6" aria-hidden="true">< ...` |
| PASS | U3 wordmark logo in nav and footer | `brand-logo" src="/logo.svg?v=2" alt="ZwiCoat" width="119" height="40" decoding="async"></a><button class="menu-toggle" type="button" aria-expanded="false" aria- ...` |
| PASS | Banned-term grep (ZwiGuard, benzophenone, monomer names, scientist/partner names, prestigious, hover or focus, UK spelling, not significant, p values outside sources, em-dash, coming next) | `no hits outside allowed contexts` |

### About

| Status | Item | Proof (built HTML) |
|---|---|---|
| PASS | Logo uses the cache-busting query | `href="/" aria-label="ZwiCoat home"><img class="brand-logo" src="/logo.svg?v=2" alt="ZwiCoat" width="119" height="40" decoding="async"></a>` |
| PASS | Favicon uses the cache-busting query | `tps://zwicoat.com/about/"><link rel="icon" type="image/png" href="/favicon.png?v=2"><meta property="og:type" content="website"><meta property="` |
| PASS | No unversioned logo reference | `no match: src="/logo\.svg"` |
| PASS | Nav order Technology, Evidence, Durability, Applications, Partner, About | `>Technology</a></li><li><a href="/evidence">Evidence</a></li><li><a href="/durability">Durability</a></li><li class="has-sub" data-sub><button type="button" cla ...` |
| PASS | P17 NSF fellowship wording | `ublications, the Cheves T. Walling Graduate Research Award, and a National Science Foundation Graduate Research Fellowship. His proposal for applying zwitterionic coatings to medical` |
| PASS | P17 GRFP wording gone | `absent: GRFP` |
| PASS | P24 founder owned | `am.</p><p>The company is based near Iowa City, Iowa, and is 100 percent founder owned.</p><p class="collab"><span class="label">Collaborators</sp` |
| PASS | Timeline alt has dissertations 2018, 2023 and 2024 | `m 2017 to 2026, three University of Iowa dissertations were completed in 2018, 2023 and 2024, and three US patents were issued in 2022, 2023 and 2024."` |
| PASS | Timeline source lists Horne 2024 dissertation | `aring Research; Barrera 2026 ACS Applied Polymer Materials; dissertations Leigh 2018, Peel 2023, Horne 2024 (University of Iowa); US patents 11,525,069 (2022), 11,814,` |
| PASS | U4 footer application order neural first, GI last | `col-apps"><h2 class="label">Applications</h2><ul role="list"><li><a href="/applications/neural-interfaces">Neural interfaces</a></li><li><a href="/applications/ ...` |
| PASS | U4 nav application menu order neural first, GI last | `apps-menu" data-sub-toggle>Applications<svg width="10" height="10" viewBox="0 0 10 10" fill="none" stroke="currentColor" stroke-width="1.6" aria-hidden="true">< ...` |
| PASS | U3 wordmark logo in nav and footer | `brand-logo" src="/logo.svg?v=2" alt="ZwiCoat" width="119" height="40" decoding="async"></a><button class="menu-toggle" type="button" aria-expanded="false" aria- ...` |
| PASS | Banned-term grep (ZwiGuard, benzophenone, monomer names, scientist/partner names, prestigious, hover or focus, UK spelling, not significant, p values outside sources, em-dash, coming next) | `no hits outside allowed contexts` |

### Contact

| Status | Item | Proof (built HTML) |
|---|---|---|
| PASS | Logo uses the cache-busting query | `href="/" aria-label="ZwiCoat home"><img class="brand-logo" src="/logo.svg?v=2" alt="ZwiCoat" width="119" height="40" decoding="async"></a>` |
| PASS | Favicon uses the cache-busting query | `s://zwicoat.com/contact/"><link rel="icon" type="image/png" href="/favicon.png?v=2"><meta property="og:type" content="website"><meta property="` |
| PASS | No unversioned logo reference | `no match: src="/logo\.svg"` |
| PASS | Nav order Technology, Evidence, Durability, Applications, Partner, About | `>Technology</a></li><li><a href="/evidence">Evidence</a></li><li><a href="/durability">Durability</a></li><li class="has-sub" data-sub><button type="button" cla ...` |
| PASS | Contact form present | `<form` |
| PASS | U4 footer application order neural first, GI last | `col-apps"><h2 class="label">Applications</h2><ul role="list"><li><a href="/applications/neural-interfaces">Neural interfaces</a></li><li><a href="/applications/ ...` |
| PASS | U4 nav application menu order neural first, GI last | `apps-menu" data-sub-toggle>Applications<svg width="10" height="10" viewBox="0 0 10 10" fill="none" stroke="currentColor" stroke-width="1.6" aria-hidden="true">< ...` |
| PASS | U3 wordmark logo in nav and footer | `brand-logo" src="/logo.svg?v=2" alt="ZwiCoat" width="119" height="40" decoding="async"></a><button class="menu-toggle" type="button" aria-expanded="false" aria- ...` |
| PASS | M2 materials list: elastomers and metals | `<option value="Silicone">Silicone</option><option value="PVC">PVC</option><option value="Polyurethane">Polyurethane</option><option value="PEEK">PEEK</option><o ...` |
| PASS | Banned-term grep (ZwiGuard, benzophenone, monomer names, scientist/partner names, prestigious, hover or focus, UK spelling, not significant, p values outside sources, em-dash, coming next) | `no hits outside allowed contexts` |

### Publications

| Status | Item | Proof (built HTML) |
|---|---|---|
| PASS | Logo uses the cache-busting query | `href="/" aria-label="ZwiCoat home"><img class="brand-logo" src="/logo.svg?v=2" alt="ZwiCoat" width="119" height="40" decoding="async"></a>` |
| PASS | Favicon uses the cache-busting query | `wicoat.com/publications/"><link rel="icon" type="image/png" href="/favicon.png?v=2"><meta property="og:type" content="website"><meta property="` |
| PASS | No unversioned logo reference | `no match: src="/logo\.svg"` |
| PASS | Nav order Technology, Evidence, Durability, Applications, Partner, About | `>Technology</a></li><li><a href="/evidence">Evidence</a></li><li><a href="/durability">Durability</a></li><li class="has-sub" data-sub><button type="button" cla ...` |
| PASS | P18 h1 | `><header class="page-head"><p class="label">Publications</p><h1>The published work behind ZwiCoat.</h1><p class="lead">Results on this site come from the papers, d` |
| PASS | P19 patent note | `atent/US12116498">US 12,116,498</a></p><p class="item-meta">Coated-device system, continuation of the 11,814,526 family: a medical device carrying a covalently grafted zwitterionic hydrogel film.</p></li></ul><p class="intro">Coun ...` |
| PASS | Horne dissertation 2024 | `hotografted zwitterionic thin films</p><p class="item-meta">Ryan R. Horne, 2024. University of Iowa.</p></li></ul></section><section class="` |
| PASS | In-preparation section not shown | `absent: Manuscripts in preparation` |
| PASS | U4 footer application order neural first, GI last | `col-apps"><h2 class="label">Applications</h2><ul role="list"><li><a href="/applications/neural-interfaces">Neural interfaces</a></li><li><a href="/applications/ ...` |
| PASS | U4 nav application menu order neural first, GI last | `apps-menu" data-sub-toggle>Applications<svg width="10" height="10" viewBox="0 0 10 10" fill="none" stroke="currentColor" stroke-width="1.6" aria-hidden="true">< ...` |
| PASS | U3 wordmark logo in nav and footer | `brand-logo" src="/logo.svg?v=2" alt="ZwiCoat" width="119" height="40" decoding="async"></a><button class="menu-toggle" type="button" aria-expanded="false" aria- ...` |
| PASS | Banned-term grep (ZwiGuard, benzophenone, monomer names, scientist/partner names, prestigious, hover or focus, UK spelling, not significant, p values outside sources, em-dash, coming next) | `no hits outside allowed contexts` |

### FCOI

| Status | Item | Proof (built HTML) |
|---|---|---|
| PASS | Logo uses the cache-busting query | `href="/" aria-label="ZwiCoat home"><img class="brand-logo" src="/logo.svg?v=2" alt="ZwiCoat" width="119" height="40" decoding="async"></a>` |
| PASS | Favicon uses the cache-busting query | `ttps://zwicoat.com/fcoi/"><link rel="icon" type="image/png" href="/favicon.png?v=2"><meta property="og:type" content="website"><meta property="` |
| PASS | No unversioned logo reference | `no match: src="/logo\.svg"` |
| PASS | Nav order Technology, Evidence, Durability, Applications, Partner, About | `>Technology</a></li><li><a href="/evidence">Evidence</a></li><li><a href="/durability">Durability</a></li><li class="has-sub" data-sub><button type="button" cla ...` |
| PASS | FCOI policy linked | `:</strong> May 21, 2026</p><p><a class="btn-outline" href="/ZCMI_FCOI_Policy.pdf">Download the policy as a PDF</a></p></header><details clas` |
| PASS | U4 footer application order neural first, GI last | `col-apps"><h2 class="label">Applications</h2><ul role="list"><li><a href="/applications/neural-interfaces">Neural interfaces</a></li><li><a href="/applications/ ...` |
| PASS | U4 nav application menu order neural first, GI last | `apps-menu" data-sub-toggle>Applications<svg width="10" height="10" viewBox="0 0 10 10" fill="none" stroke="currentColor" stroke-width="1.6" aria-hidden="true">< ...` |
| PASS | U3 wordmark logo in nav and footer | `brand-logo" src="/logo.svg?v=2" alt="ZwiCoat" width="119" height="40" decoding="async"></a><button class="menu-toggle" type="button" aria-expanded="false" aria- ...` |
| PASS | Banned-term grep (ZwiGuard, benzophenone, monomer names, scientist/partner names, prestigious, hover or focus, UK spelling, not significant, p values outside sources, em-dash, coming next) | `no hits outside allowed contexts` |

### Charts, data and assets (built site)

| Status | Item | Proof (built HTML) |
|---|---|---|
| PASS | E1 W24 image labels the dissertation Horne 2024 | `figures/W24_publication_timeline.svg: ...584" transform="rotate(-45 584.56104 267.554584)">Horne 2024</text> </g> <g id="Path...` |
| PASS | E1 W24 image has no Horne 2023 dissertation label | `figures/W24_publication_timeline.svg: absent 'Horne 2023'` |
| PASS | E1 W24 json: Horne dissertation 2024 | `data/W24_publications.json: "year": 2024, "type": "dissertation", "first_author": "Horne"` |
| PASS | E1 interactive timeline bundle: Horne dissertation 2024 | `_astro/W24_publications.js: year:2024,type:'dissertation',first_author:'Horne'` |
| PASS | D6 W11 title | `figures/W11_sterilization.svg: ..."47.791562" transform="rotate(-0 21.6 47.791562)">Compatible with multiple sterilization methods</text> </g> </g> <g id...` |
| PASS | D6 W11 wet e-beam tile says failed | `figures/W11_sterilization.svg: ...al'" transform="translate(208.335753 229.950129)">failed</text> </g> <g id="text...` |
| PASS | D6 W11 'not recommended' gone | `figures/W11_sterilization.svg: absent 'not recommended'` |
| PASS | D6 W11 eight tiles (7 passed + 1 failed) | `figures/W11_sterilization.svg: 'passed' x 7` |
| PASS | M11/21 W25 keeps (not significant) on the four-week polarization pair | `figures/W25_sheep_impedance_components.svg: ...ial'" transform="translate(508.22282 267.573371)">(not significant)</text> </g> <g id="text...` |
| PASS | M11/20 W27 has no PEG bar | `figures/W27_capsule_thickness_mice.svg: no match PEG/non-zwitterionic` |
| PASS | M11/20 W27 panel A bracket | `figures/W27_capsule_thickness_mice.svg: ...969677" transform="rotate(-0 252.18 129.969677)">−67%, p = 0.010</text> </g> <g id="text...` |
| PASS | M4 W34 single short annotation | `figures/W34_peek_bond_strength.svg: 'gel tears before' x 1` |
| PASS | M4 W34 long annotation gone | `figures/W34_peek_bond_strength.svg: absent 'Every PEEK test'` |
| PASS | M4 W34 footnotes gone | `figures/W34_peek_bond_strength.svg: absent 'load-cell limit'` |
| PASS | M4 W34 short subtitle | `figures/W34_peek_bond_strength.svg: ..."56.603672" transform="rotate(-0 21.6 56.603672)">Lap-shear bond strength on PEEK, silicone and PVC; group means; ZwiCoat internal tests, 2025 to 2026</text> </g> </g> <defs> ...` |
| PASS | T8/D5 W31 axis | `figures/W31_bond_strength_vs_grafting_agent.svg: ...144969" transform="rotate(-0 318.276 387.144969)">Grafting agent concentration (mg/mL)</text> </g> </g> <g...` |
| PASS | T8 no benzophenone in W31 | `figures/W31_bond_strength_vs_grafting_agent.svg: no match (?i)benzophenone` |
| PASS | T9 W30 shows the SBMA series | `figures/W30_crosslinker_tradeoff.svg: ...813" transform="rotate(-0 267.033288 133.517813)">SBMA</text> </g> <g id="li...` |
| PASS | T9 W30 shows the CBMA series | `figures/W30_crosslinker_tradeoff.svg: ...125" transform="rotate(-0 267.033288 147.663125)">CBMA</text> </g> </g> </g...` |
| PASS | T7 W04 no not-significant (hollow) bar | `figures/W04_fibrosis_by_study.svg: absent 'not significant'` |
| PASS | E4 tile value 6 months (sheep) | `data/W12_numbers.json: "value": "6 months", "label": "functional human arrays in sheep"` |
| PASS | M7/5 'largest device markets' kept | `data/W12_numbers.json: ...nited States, Australia, China, Japan and Mexico: the largest device markets.", "source": "ZCMI patent s...` |
| PASS | N4 no provisional wording in tiles | `data/W12_numbers.json: no match (?i)provisional` |
| PASS | U3 logo is the ZwiCoat wordmark | `logo.svg: ... viewBox="-4.00 -104.00 667.49 224.21" role="img" aria-label="ZwiCoat"> <title>ZwiCoat</title> <...` |
| PASS | U1/U2 no ZwiGuard, benzophenone, CIVCO, Kyle Ruby or Reineke in any shipped html, js, json, svg or css file | `0 hits across dist` |

## Staging re-check (https://staging.zwicoat.com, after deploy)

Fetched with curl into a local mirror, then the same checker was run on it. Failures listed first (none).

#### Home (/) (staging): 33 PASS, 0 FAIL

| Status | Item | Proof (built HTML) |
|---|---|---|
| PASS | Logo uses the cache-busting query | `href="/" aria-label="ZwiCoat home"><img class="brand-logo" src="/logo.svg?v=2" alt="ZwiCoat" width="119" height="40" decoding="async"></a>` |
| PASS | Favicon uses the cache-busting query | `ef="https://zwicoat.com/"><link rel="icon" type="image/png" href="/favicon.png?v=2"><meta property="og:type" content="website"><meta property="` |
| PASS | No unversioned logo reference | `no match: src="/logo\.svg"` |
| PASS | Nav order Technology, Evidence, Durability, Applications, Partner, About | `>Technology</a></li><li><a href="/evidence">Evidence</a></li><li><a href="/durability">Durability</a></li><li class="has-sub" data-sub><button type="button" cla ...` |
| PASS | P1 hero subhead | `to the device, that keeps protein, cells and bacteria off. It means less scarring, lower impedance, easier insertion and fewer bacteria, from a single coating step. The evidence spans ten years of published work.</p><div class="he ...` |
| PASS | P1 old fragment subhead gone | `absent: One coating step. Ten years of evidence.` |
| PASS | P2 sources sentence kept | `ilm have no foothold.</span></li></ul><p class="tiles-note">Every number on this site comes from a published paper, dissertation or issued patent.</p><p class="tiles-note tiles-src label">Sources: the ten j` |
| PASS | P2 replacement sentence absent | `absent: Every number has its source listed under it.` |
| PASS | P3 archive line removed | `absent: 182 archived experiments` |
| PASS | P3 rewritten archive line removed | `absent: 182 documented experiments` |
| PASS | P4 It-stays-on title | `xt"><p class="label">It stays on</p><h2 class="claim-title">Friction was unchanged after three weeks in mice.</h2><div class="claim-body"><p>Coated silicone was implante` |
| PASS | W26 not on home | `absent: W26_sheep_histology` |
| PASS | Less scar row uses rebuilt W27 | `Less scar</p><h2 class="claim-title">A thinner scar capsule around coated implants.</h2><div class="claim-body"><p>In mice, the scar capsule was 67 percent thin ...` |
| PASS | W27 caption has no PEG control | `absent: non-zwitterionic` |
| PASS | Card order neural first, GI last | `<ul class="grid" role="list"><li><a class="card" href="/applications/neural-interfaces"><div class="media media-photo fit-contain"><img src="/images/lab/ci-arra ...` |
| PASS | P9 airway card | `bes</h3><p class="stat">~60%</p><p class="stat-label label">less force to intubate with coated endotracheal tubes in a cadaveric larynx (ZwiCoat internal study, 2026)</p></div></a></li><li><a class="card compact" href="/applic` |
| PASS | P10 indwelling card | `ers</h3><p class="stat">~90%</p><p class="stat-label label">lower friction on coated silicone, still in place after three weeks in mice (Peel 2024)</p></div></a></li><li><a class="card compact" href="/applic` |
| PASS | P11 PEEK card | `/h3><p class="stat">~635 kPa</p><p class="stat-label label">bond strength of the coating on PEEK, dry (ZwiCoat internal tests)</p></div></a></li><li><a class="card compact" href="/applic` |
| PASS | P12 expander card alt | `pct-01.jpg" alt="A tissue expander coated in blue hydrogel, inflated to 300 percent of its rated volume, with the blue coating covering the whole shell." loading="` |
| PASS | No 200 percent wording | `absent: 200 percent` |
| PASS | No regulatory wording on home | `no match: (?i)510\(k\)/\bPMA\b/Master File` |
| PASS | No monomer names on home | `no match: SBMA/CBMA/sulfobetaine/carboxybetaine` |
| PASS | CTA band kept on home | `<div class="band"><div class="band-text"><h2 id="cta-title">Bring us a device with a fouling, scar or friction problem.</h2><p>We coat it free, with no cap on quantity, and return` |
| PASS | U4 footer application order neural first, GI last | `col-apps"><h2 class="label">Applications</h2><ul role="list"><li><a href="/applications/neural-interfaces">Neural interfaces</a></li><li><a href="/applications/ ...` |
| PASS | U4 nav application menu order neural first, GI last | `apps-menu" data-sub-toggle>Applications<svg width="10" height="10" viewBox="0 0 10 10" fill="none" stroke="currentColor" stroke-width="1.6" aria-hidden="true">< ...` |
| PASS | U3 wordmark logo in nav and footer | `brand-logo" src="/logo.svg?v=2" alt="ZwiCoat" width="119" height="40" decoding="async"></a><button class="menu-toggle" type="button" aria-expanded="false" aria- ...` |
| PASS | N4 tile: further patent applications pending, no titles | `tent applications pending</span><span class="tile-takeaway">Further patent applications are pending.</span></li><li class="tile"><span class="tile-value">1 year` |
| PASS | N4 no provisional wording | `absent: provisional` |
| PASS | T2 first sentence of the hero has no monomer name | `<p class="lead">ZwiCoat is a zwitterionic hydrogel coating, covalently bonded to the device` |
| PASS | T10 no process-video element | `no match: process-video/<video[^>]*dipcoat` |
| PASS | E4 tile reads 6 months for sheep | `6 months</span><span class="tile-label label">functional human arrays in sheep` |
| PASS | A3 airway card stat is the ETT number (~60%) | `~60%</p><p class="stat-label label">less force to intubate with coated endotracheal tubes` |
| PASS | Banned-term grep (ZwiGuard, benzophenone, monomer names, scientist/partner names, prestigious, hover or focus, UK spelling, not significant, p values outside sources, em-dash, coming next) | `no hits outside allowed contexts; allowed: read from the in source/reference` |

#### Technology (staging): 28 PASS, 0 FAIL

| Status | Item | Proof (built HTML) |
|---|---|---|
| PASS | Logo uses the cache-busting query | `href="/" aria-label="ZwiCoat home"><img class="brand-logo" src="/logo.svg?v=2" alt="ZwiCoat" width="119" height="40" decoding="async"></a>` |
| PASS | Favicon uses the cache-busting query | `/zwicoat.com/technology/"><link rel="icon" type="image/png" href="/favicon.png?v=2"><meta property="og:type" content="website"><meta property="` |
| PASS | No unversioned logo reference | `no match: src="/logo\.svg"` |
| PASS | Nav order Technology, Evidence, Durability, Applications, Partner, About | `>Technology</a></li><li><a href="/evidence">Evidence</a></li><li><a href="/durability">Durability</a></li><li class="has-sub" data-sub><button type="button" cla ...` |
| PASS | P6 first sentence kept | `r that nothing can displace.</h2><div class="claim-body"><p>ZwiCoat is a zwitterionic hydrogel that dramatically lowers friction, infection, inflammation and biofouling.</p><p>Each repeat unit carries a strong dipole. The dipole` |
| PASS | P6 dipole sentences | `ers friction, infection, inflammation and biofouling.</p><p>Each repeat unit carries a strong dipole. The dipole binds tightly to water, creating a hydration barrier between the device and body.</p><p>Proteins, cells and bacteria  ...` |
| PASS | P6 new paragraph | `reating a hydration barrier between the device and body.</p><p>Proteins, cells and bacteria cannot displace that hydration barrier, so they do not stick. The barrier is far stronger than the hydrogen-bonded hydration of PEG, the u ...` |
| PASS | P6 old water-shell sentence removed | `absent: The dipole binds a tightly ordered shell of water.` |
| PASS | P6 old 'hold is stronger' sentence removed | `absent: The hold is stronger` |
| PASS | P6 UV sentences kept | `l., Nature Biotechnology).</p><p>One UV step does two jobs. It covalently bonds the coating to the device surface. The same light crosslinks the network.</p><p>The result is a crosslinked hydrogel anchored to the` |
| PASS | P7 tethered-brush sentence kept | `he result is a crosslinked hydrogel anchored to the device. It is not a thin tethered brush, an adsorbed layer that can wash off, or an additive blended into the polymer.</p></div></div><div class="claim-figure"><figure class="sch` |
| PASS | P8 sterilization paragraph | `by six weeks. The ZwiCoat film did not (Horne 2023).</p><p>The coating is compatible with steam, ethylene oxide, gamma, UV and dry e-beam sterilization, and bond strength held after sterilization and shipping. We validate on your  ...` |
| PASS | W11 chart on page | `, about 5 per group.</span></p><img class="figure-img" src="/figures/W11_sterilization.png" alt="Two panels. Left: the coating was unchanged after ste` |
| PASS | W27 rebuilt text | `of scar capsule thickness in mice, uncoated against coated. Panel A, six weeks on flat silicone sheets: 82 micrometers uncoated and 27 coated. Panel B, one year on human cochlear implant arrays: 47 micr` |
| PASS | No regulatory section | `no match: (?i)510\(k\)/Master File/>Regulatory<` |
| PASS | No visible process-video slot | `no match: (?i)process video: coming` |
| PASS | CTA band kept | `<div class="band"><div class="band-text"><h2 id="cta-title">Bring us a device with a fouling, scar or friction problem.</h2><p>We coat it free, with no cap on quantity, and return` |
| PASS | U4 footer application order neural first, GI last | `col-apps"><h2 class="label">Applications</h2><ul role="list"><li><a href="/applications/neural-interfaces">Neural interfaces</a></li><li><a href="/applications/ ...` |
| PASS | U4 nav application menu order neural first, GI last | `apps-menu" data-sub-toggle>Applications<svg width="10" height="10" viewBox="0 0 10 10" fill="none" stroke="currentColor" stroke-width="1.6" aria-hidden="true">< ...` |
| PASS | U3 wordmark logo in nav and footer | `brand-logo" src="/logo.svg?v=2" alt="ZwiCoat" width="119" height="40" decoding="async"></a><button class="menu-toggle" type="button" aria-expanded="false" aria- ...` |
| PASS | T5 'Silicone is published' block gone | `absent: Silicone is published` |
| PASS | T5 substrates block reads cleanly | `of.</h2></div><div class="block-body"><div class="prose"><p>ZwiCoat has been grafted to silicone, PVC, PEEK, parylene-C and polyurethane, and across platinum contacts. On silicone the bond is stronger than the gel itself: in pu` |
| PASS | T7 W04 hollow-bar sentence gone | `no match: (?i)hollow` |
| PASS | T9 W30 chart on page | `biomaterials.1c00852</span></p><img class="figure-img" src="/figures/W30_crosslinker_tradeoff.png" alt="Charts against crosslinker percentage for the coating` |
| PASS | T8 W31 chart on page | `acs.langmuir.8b00838</span></p><img class="figure-img" src="/figures/W31_bond_strength_vs_grafting_agent.png" alt="Shear bond strength of the zwitterionic film on silic` |
| PASS | T10 no process-video element | `no match: process-video/<video[^>]*dipcoat` |
| PASS | T11 'The partner files' section gone | `absent: The partner files` |
| PASS | Banned-term grep (ZwiGuard, benzophenone, monomer names, scientist/partner names, prestigious, hover or focus, UK spelling, not significant, p values outside sources, em-dash, coming next) | `no hits outside allowed contexts; allowed: SBMA in W30 figure; read from the in source/reference` |

#### Evidence (staging): 30 PASS, 0 FAIL

| Status | Item | Proof (built HTML) |
|---|---|---|
| PASS | Logo uses the cache-busting query | `href="/" aria-label="ZwiCoat home"><img class="brand-logo" src="/logo.svg?v=2" alt="ZwiCoat" width="119" height="40" decoding="async"></a>` |
| PASS | Favicon uses the cache-busting query | `://zwicoat.com/evidence/"><link rel="icon" type="image/png" href="/favicon.png?v=2"><meta property="og:type" content="website"><meta property="` |
| PASS | No unversioned logo reference | `no match: src="/logo\.svg"` |
| PASS | Nav order Technology, Evidence, Durability, Applications, Partner, About | `>Technology</a></li><li><a href="/evidence" aria-current="page">Evidence</a></li><li><a href="/durability">Durability</a></li><li class="has-sub" data-sub><butt ...` |
| PASS | Horne dissertation 2024 | `Ryan R. Horne, University of Iowa, 2024` |
| PASS | No Horne 2023 dissertation | `no match: Horne, University of Iowa, 2023` |
| PASS | W26 not on evidence | `absent: W26_sheep_histology` |
| PASS | W27 rebuilt on evidence | `j.actbio.2023.05.011</span></p><img class="figure-img" src="/figures/W27_capsule_thickness_mice.png" alt="Two bar charts of scar capsule thickness in mice, unc` |
| PASS | W27 no PEG control text | `absent: non-zwitterionic` |
| PASS | W25 on evidence | `j.heares.2026.109606</span></p><img class="figure-img" src="/figures/W25_sheep_impedance_components.png" alt="Three bar charts for sheep: total impedance, polariza` |
| PASS | P5 largest device markets tile | `akeaway">United States, Australia, China, Japan and Mexico: the largest device markets.</span></li><li class="tile"><span class="tile-value">More<` |
| PASS | P19 patent note | `/patent/US12116498">US 12,116,498</a><span class="pub-meta">Coated-device system, continuation of the 11,814,526 family: a medical device carrying a covalently grafted zwitterionic hydrogel film.</span></li></ul></div></div></sect ...` |
| PASS | Archive tiles removed | `absent: 182 archived` |
| PASS | CTA band kept | `<div class="band"><div class="band-text"><h2 id="cta-title">Bring us a device with a fouling, scar or friction problem.</h2><p>We coat it free, with no cap on quantity, and return` |
| PASS | U4 footer application order neural first, GI last | `col-apps"><h2 class="label">Applications</h2><ul role="list"><li><a href="/applications/neural-interfaces">Neural interfaces</a></li><li><a href="/applications/ ...` |
| PASS | U4 nav application menu order neural first, GI last | `apps-menu" data-sub-toggle>Applications<svg width="10" height="10" viewBox="0 0 10 10" fill="none" stroke="currentColor" stroke-width="1.6" aria-hidden="true">< ...` |
| PASS | U3 wordmark logo in nav and footer | `brand-logo" src="/logo.svg?v=2" alt="ZwiCoat" width="119" height="40" decoding="async"></a><button class="menu-toggle" type="button" aria-expanded="false" aria- ...` |
| PASS | E2 timeline not on evidence | `absent: W24_publication_timeline` |
| PASS | E3 section order: scar first, antifouling second | `id="scar" aria-labelledby="scar-h"><div class="ev-head"><p class="label ev-num">01</p><h2 id="scar-h">Scar tissue</h2><p class="ev-text">Capsules were thinner a ...` |
| PASS | E9 impedance below insertion and friction | `id="insertion-friction" aria-labelledby="insertion-friction-h"><div class="ev-head"><p class="label ev-num">03</p><h2 id="insertion-friction-h">Insertion force  ...` |
| PASS | E10 W08 rendered at 640 px | `W08_impedance_sheep.png" alt="Bar chart of total electrode impedance in sheep for coated and uncoated cochlear implant arrays, at implantation and at four weeks ...` |
| PASS | E4 tile reads 6 months for sheep | `6 months</span><span class="tile-label label">functional human arrays in sheep` |
| PASS | E5 archive tiles removed | `absent: 1,056` |
| PASS | E6 archive source line, plain wording, last line of the page body | `Archive counts: ZwiCoat Data archive.</p></div>` |
| PASS | E6 no E-report method-tag wording | `absent: E-report method tags` |
| PASS | E8 sheep histology photo on evidence | `frame fit-cover" style="aspect-ratio: 1750/1150;"><img src="/images/histology-sheep.png" alt="Four tissue sections of a sheep cochlea. The top row` |
| PASS | N4 no provisional wording | `absent: provisional` |
| PASS | T7 no hollow-bar wording | `no match: (?i)hollow` |
| PASS | E11 W37 not placed (held for review, see VERIFY) | `absent: W37_ci_insertion_synthetic` |
| PASS | Banned-term grep (ZwiGuard, benzophenone, monomer names, scientist/partner names, prestigious, hover or focus, UK spelling, not significant, p values outside sources, em-dash, coming next) | `no hits outside allowed contexts; allowed: SBMA in W30 figure; read from the in source/reference` |

#### 1. Neural interfaces (staging): 20 PASS, 0 FAIL

| Status | Item | Proof (built HTML) |
|---|---|---|
| PASS | Logo uses the cache-busting query | `href="/" aria-label="ZwiCoat home"><img class="brand-logo" src="/logo.svg?v=2" alt="ZwiCoat" width="119" height="40" decoding="async"></a>` |
| PASS | Favicon uses the cache-busting query | `tions/neural-interfaces/"><link rel="icon" type="image/png" href="/favicon.png?v=2"><meta property="og:type" content="website"><meta property="` |
| PASS | No unversioned logo reference | `no match: src="/logo\.svg"` |
| PASS | Nav order Technology, Evidence, Durability, Applications, Partner, About | `>Technology</a></li><li><a href="/evidence">Evidence</a></li><li><a href="/durability">Durability</a></li><li class="has-sub" data-sub><button type="button" cla ...` |
| PASS | P23 opener removed | `absent: What follows is our design rationale` |
| PASS | P23 rationale in plain voice | `0156.</p></figcaption></figure></div><div class="prose"> <p><strong>Why this matters for the next generation of electrodes.</strong> A zwitterionic hydrogel is wet, ion-rich and tightly bound to the metal. At the contact it raises ...` |
| PASS | W26 stays on neural | `j.heares.2026.109606</span></p><img class="figure-img" src="/figures/W26_sheep_histology.png" alt="Three small charts comparing uncoated and coated arra` |
| PASS | W25 on neural | `j.heares.2026.109606</span></p><img class="figure-img" src="/figures/W25_sheep_impedance_components.png" alt="Three small bar charts of electrode impedance in kilo` |
| PASS | Sheep histology photo (Coated label repainted) | `frame fit-cover" style="aspect-ratio: 1750/1150;"><img src="/images/histology-sheep.png" alt="Tissue sections from the base of a sheep cochlea at t` |
| PASS | W27 rebuilt text | `against coated. Panel A, six weeks on flat silicone sheets: 82 micrometers uncoated and 27 coated. Panel B, one year on human cochlear implant arrays: 47 mic` |
| PASS | U4 footer application order neural first, GI last | `col-apps"><h2 class="label">Applications</h2><ul role="list"><li><a href="/applications/neural-interfaces">Neural interfaces</a></li><li><a href="/applications/ ...` |
| PASS | U4 nav application menu order neural first, GI last | `apps-menu" data-sub-toggle>Applications<svg width="10" height="10" viewBox="0 0 10 10" fill="none" stroke="currentColor" stroke-width="1.6" aria-hidden="true">< ...` |
| PASS | U3 wordmark logo in nav and footer | `brand-logo" src="/logo.svg?v=2" alt="ZwiCoat" width="119" height="40" decoding="async"></a><button class="menu-toggle" type="button" aria-expanded="false" aria- ...` |
| PASS | NI1 leads with sheep histology | `class="lead-media"><div class="fig"><figure class="photo" style="--ratio: 1.5217;"><div class="photo-box"><p class="fig-tag" aria-hidden="true"><span class="fig ...` |
| PASS | NI2 conceals the platinum, texturing | `voltage and a smaller contact can deliver the same charge. Because the coating conceals the platinum from tissue, contact surfaces can be textured for even more surface area without inviting more scar.</p> <p>Lower impedance, smal ...` |
| PASS | NI2 capacitance and smaller contacts | `c hydrogel is wet, ion-rich and tightly bound to the metal. At the contact it raises the capacity to store charge at the electrode surface, so the same stimulus needs less voltage and a smaller contact can deliver the same charge. ...` |
| PASS | NI3 problem paragraph | `ph pending Kam --> <h2 id="the-problem">The problem</h2> <p>A neural electrode works or fails at one place: the interface between the device and tissue. Within seconds of implantation, proteins coat the array, an` |
| PASS | E11 W37 not placed (held for review, see VERIFY) | `absent: W37_ci_insertion_synthetic` |
| PASS | T12 regulatory: exactly one line, in the spec strip | `Regulatory path PMA supplement with our Master File behind your submission Evidence mice, one year; sheep, four weeks (six months in preparation); human cadaveric cochlea [spec-strip count=1; regulatory mentions in the article bod ...` |
| PASS | Banned-term grep (ZwiGuard, benzophenone, monomer names, scientist/partner names, prestigious, hover or focus, UK spelling, not significant, p values outside sources, em-dash, coming next) | `no hits outside allowed contexts; allowed: read from the in source/reference` |

#### 3. Airway tubes (staging): 17 PASS, 0 FAIL

| Status | Item | Proof (built HTML) |
|---|---|---|
| PASS | Logo uses the cache-busting query | `href="/" aria-label="ZwiCoat home"><img class="brand-logo" src="/logo.svg?v=2" alt="ZwiCoat" width="119" height="40" decoding="async"></a>` |
| PASS | Favicon uses the cache-busting query | `com/applications/airway/"><link rel="icon" type="image/png" href="/favicon.png?v=2"><meta property="og:type" content="website"><meta property="` |
| PASS | No unversioned logo reference | `no match: src="/logo\.svg"` |
| PASS | Nav order Technology, Evidence, Durability, Applications, Partner, About | `>Technology</a></li><li><a href="/evidence">Evidence</a></li><li><a href="/durability">Durability</a></li><li class="has-sub" data-sub><button type="button" cla ...` |
| PASS | P13 standfirst | `ay tubes / ZwiCoat</title><meta name="description" content="ZwiCoat is a drug-free coating that enhances mucus flow, resists bacteria and lowers friction, and it has been tested on endotracheal tubes."><link rel="canonical" href=" ...` |
| PASS | U4 footer application order neural first, GI last | `col-apps"><h2 class="label">Applications</h2><ul role="list"><li><a href="/applications/neural-interfaces">Neural interfaces</a></li><li><a href="/applications/ ...` |
| PASS | U4 nav application menu order neural first, GI last | `apps-menu" data-sub-toggle>Applications<svg width="10" height="10" viewBox="0 0 10 10" fill="none" stroke="currentColor" stroke-width="1.6" aria-hidden="true">< ...` |
| PASS | U3 wordmark logo in nav and footer | `brand-logo" src="/logo.svg?v=2" alt="ZwiCoat" width="119" height="40" decoding="async"></a><button class="menu-toggle" type="button" aria-expanded="false" aria- ...` |
| PASS | A1 leads with the cuff clip | `class="lead-media"><div class="fig pair"><div class="pair-item"><figure class="vl" style="--ratio: 0.5625;"><div class="vl-box"><p class="fig-tag" aria-hidden=" ...` |
| PASS | A3 W38 ETT insertion-force chart on the page | `0459478 (CC BY 4.0).</span></p><img class="figure-img" src="/figures/W38_ett_insertion_force.png" alt="Four panels of endotracheal tube insertion force in a` |
| PASS | A3 W38 caption | `surgeons intubated a cadaveric human larynx on a load cell. Coated endotracheal tubes needed 62 percent (Surgeon 1) and 61 percent (Surgeon 2) less integrated insertion force than the uncoated tube.</p><p class="figure-source labe ...` |
| PASS | A3 W38 internal source, minimal citation | `Source: ZwiCoat internal study, 2026 (1 uncoated and 3 coated tubes per surgeon` |
| PASS | A3 ETT result in the body copy | `ed a cadaveric human larynx with coated and uncoated tubes. Coated tubes needed about 60 percent less insertion force, for both surgeons (ZwiCoat internal study, 2026).</p> </div><div class="fig"><figure class="figure"><div clas` |
| PASS | A2 stenosis before pneumonia | `Stenosis comes first. A rigid tube scrapes the larynx on the way in, and the airway reacts to it for as long as the tube stays. In a review of nine studies, 83  ...` |
| PASS | A2 stenosis citations resolved in references | `<li>Brodsky MB, Levy MJ, Jedlanek E, et al. Laryngeal injury and upper airway symptoms after oral endotracheal intubation with mechanical ventilation during cri ...` |
| PASS | T12 regulatory: exactly one line, in the spec strip | `Regulatory path 510(k) path with our Master File behind your submission Evidence coated endotracheal tubes in a cadaveric larynx (ZwiCoat internal study, 2026); mucus-flo [spec-strip count=1; regulatory mentions in the article bod ...` |
| PASS | Banned-term grep (ZwiGuard, benzophenone, monomer names, scientist/partner names, prestigious, hover or focus, UK spelling, not significant, p values outside sources, em-dash, coming next) | `no hits outside allowed contexts; allowed: p < 0 in source line; read from the in source/reference` |

#### About (staging): 13 PASS, 0 FAIL

| Status | Item | Proof (built HTML) |
|---|---|---|
| PASS | Logo uses the cache-busting query | `href="/" aria-label="ZwiCoat home"><img class="brand-logo" src="/logo.svg?v=2" alt="ZwiCoat" width="119" height="40" decoding="async"></a>` |
| PASS | Favicon uses the cache-busting query | `tps://zwicoat.com/about/"><link rel="icon" type="image/png" href="/favicon.png?v=2"><meta property="og:type" content="website"><meta property="` |
| PASS | No unversioned logo reference | `no match: src="/logo\.svg"` |
| PASS | Nav order Technology, Evidence, Durability, Applications, Partner, About | `>Technology</a></li><li><a href="/evidence">Evidence</a></li><li><a href="/durability">Durability</a></li><li class="has-sub" data-sub><button type="button" cla ...` |
| PASS | P17 NSF fellowship wording | `ublications, the Cheves T. Walling Graduate Research Award, and a National Science Foundation Graduate Research Fellowship. His proposal for applying zwitterionic coatings to medical` |
| PASS | P17 GRFP wording gone | `absent: GRFP` |
| PASS | P24 founder owned | `am.</p><p>The company is based near Iowa City, Iowa, and is 100 percent founder owned.</p><p class="collab"><span class="label">Collaborators</sp` |
| PASS | Timeline alt has dissertations 2018, 2023 and 2024 | `m 2017 to 2026, three University of Iowa dissertations were completed in 2018, 2023 and 2024, and three US patents were issued in 2022, 2023 and 2024."` |
| PASS | Timeline source lists Horne 2024 dissertation | `aring Research; Barrera 2026 ACS Applied Polymer Materials; dissertations Leigh 2018, Peel 2023, Horne 2024 (University of Iowa); US patents 11,525,069 (2022), 11,814,` |
| PASS | U4 footer application order neural first, GI last | `col-apps"><h2 class="label">Applications</h2><ul role="list"><li><a href="/applications/neural-interfaces">Neural interfaces</a></li><li><a href="/applications/ ...` |
| PASS | U4 nav application menu order neural first, GI last | `apps-menu" data-sub-toggle>Applications<svg width="10" height="10" viewBox="0 0 10 10" fill="none" stroke="currentColor" stroke-width="1.6" aria-hidden="true">< ...` |
| PASS | U3 wordmark logo in nav and footer | `brand-logo" src="/logo.svg?v=2" alt="ZwiCoat" width="119" height="40" decoding="async"></a><button class="menu-toggle" type="button" aria-expanded="false" aria- ...` |
| PASS | Banned-term grep (ZwiGuard, benzophenone, monomer names, scientist/partner names, prestigious, hover or focus, UK spelling, not significant, p values outside sources, em-dash, coming next) | `no hits outside allowed contexts` |

#### Assets (staging)

| Status | Item | Proof (built HTML) |
|---|---|---|
| PASS | E1 W24 image labels the dissertation Horne 2024 | `figures/W24_publication_timeline.svg: ...584" transform="rotate(-45 584.56104 267.554584)">Horne 2024</text> </g> <g id="Path...` |
| PASS | E1 W24 image has no Horne 2023 dissertation label | `figures/W24_publication_timeline.svg: absent 'Horne 2023'` |
| PASS | E1 W24 json: Horne dissertation 2024 | `data/W24_publications.json: "year": 2024, "type": "dissertation", "first_author": "Horne"` |
| PASS | E1 interactive timeline bundle: Horne dissertation 2024 | `_astro/W24_publications.js: year:2024,type:'dissertation',first_author:'Horne'` |
| PASS | D6 W11 title | `figures/W11_sterilization.svg: ..."47.791562" transform="rotate(-0 21.6 47.791562)">Compatible with multiple sterilization methods</text> </g> </g> <g id...` |
| PASS | D6 W11 wet e-beam tile says failed | `figures/W11_sterilization.svg: ...al'" transform="translate(208.335753 229.950129)">failed</text> </g> <g id="text...` |
| PASS | D6 W11 'not recommended' gone | `figures/W11_sterilization.svg: absent 'not recommended'` |
| PASS | D6 W11 eight tiles (7 passed + 1 failed) | `figures/W11_sterilization.svg: 'passed' x 7` |
| PASS | M11/21 W25 keeps (not significant) on the four-week polarization pair | `figures/W25_sheep_impedance_components.svg: ...ial'" transform="translate(508.22282 267.573371)">(not significant)</text> </g> <g id="text...` |
| PASS | M11/20 W27 has no PEG bar | `figures/W27_capsule_thickness_mice.svg: no match PEG/non-zwitterionic` |
| PASS | M11/20 W27 panel A bracket | `figures/W27_capsule_thickness_mice.svg: ...969677" transform="rotate(-0 252.18 129.969677)">−67%, p = 0.010</text> </g> <g id="text...` |
| PASS | M4 W34 single short annotation | `figures/W34_peek_bond_strength.svg: 'gel tears before' x 1` |
| PASS | M4 W34 long annotation gone | `figures/W34_peek_bond_strength.svg: absent 'Every PEEK test'` |
| PASS | M4 W34 footnotes gone | `figures/W34_peek_bond_strength.svg: absent 'load-cell limit'` |
| PASS | M4 W34 short subtitle | `figures/W34_peek_bond_strength.svg: ..."56.603672" transform="rotate(-0 21.6 56.603672)">Lap-shear bond strength on PEEK, silicone and PVC; group means; ZwiCoat internal tests, 2025 to 2026</text> </g> </g> <defs> ...` |
| PASS | T8/D5 W31 axis | `figures/W31_bond_strength_vs_grafting_agent.svg: ...144969" transform="rotate(-0 318.276 387.144969)">Grafting agent concentration (mg/mL)</text> </g> </g> <g...` |
| PASS | T8 no benzophenone in W31 | `figures/W31_bond_strength_vs_grafting_agent.svg: no match (?i)benzophenone` |
| PASS | T9 W30 shows the SBMA series | `figures/W30_crosslinker_tradeoff.svg: ...813" transform="rotate(-0 267.033288 133.517813)">SBMA</text> </g> <g id="li...` |
| PASS | T9 W30 shows the CBMA series | `figures/W30_crosslinker_tradeoff.svg: ...125" transform="rotate(-0 267.033288 147.663125)">CBMA</text> </g> </g> </g...` |
| PASS | T7 W04 no not-significant (hollow) bar | `figures/W04_fibrosis_by_study.svg: absent 'not significant'` |
| PASS | E4 tile value 6 months (sheep) | `data/W12_numbers.json: "value": "6 months", "label": "functional human arrays in sheep"` |
| PASS | M7/5 'largest device markets' kept | `data/W12_numbers.json: ...nited States, Australia, China, Japan and Mexico: the largest device markets.", "source": "ZCMI patent s...` |
| PASS | N4 no provisional wording in tiles | `data/W12_numbers.json: no match (?i)provisional` |
| PASS | U3 logo is the ZwiCoat wordmark | `logo.svg: ... viewBox="-4.00 -104.00 667.49 224.21" role="img" aria-label="ZwiCoat"> <title>ZwiCoat</title> <...` |
| PASS | U1/U2 no ZwiGuard, benzophenone, CIVCO, Kyle Ruby or Reineke in any shipped html, js, json, svg or css file | `0 hits across dist` |

#### Raw grep counts on staging (entities decoded; case-insensitive)

The two SBMA hits on technology and evidence are the W30 chart source line ('SBMA series'), which the brief allows. 'Horne, University of Iowa, 2024' appears once on evidence (the dissertations list); about shows the dissertation through the timeline. Logo and favicon counts are 2 and 1 on every page (nav plus footer, head).

| page | ZwiGuard | benzophenone | SBMA | CBMA | Kyle | Ruby | Reineke | CIVCO | prestigious | hover or focus | micrometre | millimetre | not significant | p = 0 | p < 0 | W26_sheep_histology | logo.svg?v=2 | favicon.png?v=2 | Horne, University of Iowa, 2024 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| / | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 2 | 1 | 0 |
| /technology/ | 0 | 0 | 2 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 2 | 1 | 0 |
| /evidence/ | 0 | 0 | 2 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 2 | 1 | 1 |
| /about/ | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 2 | 1 | 0 |
| /applications/neural-interfaces/ | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 2 | 1 | 0 |
| /applications/airway/ | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 2 | 0 | 2 | 1 | 0 |

Also on staging: `/logo.svg?v=2` and `/favicon.png?v=2` return 200; `images/histology-sheep.png` md5 0c07a519b65b870e6d0d09858eba4b34 and `figures/W38_ett_insertion_force.png` md5 851f700286e900f4913f14ff12f36301 match the local build. The two 'p < 0' hits on airway are the W38 source line (classified as allowed by the checker).

## FEEDBACK-CHECKLIST.md mapping

| # | Status | Proof or reason |
|---|---|---|
| N1 | DONE | durability: W35 and W36 on page; banned-term grep clean (no customer names) |
| N2 | DONE | peek: W34 on page, rat sentence (answer 16), no cranioplasty paper figures (no cranio image src) |
| N3 | TODO | assigned to a later worker (market-research arguments on the nine application pages); not attempted |
| N4 | DONE | fixed this pass: W12 tile '5 provisional applications filed' replaced by 'More / patent applications pending / Further patent applications are pending.'; no 'provisional' on home or evidence |
| T1 | DONE | technology: first sentence present verbatim |
| T2 | DONE | monomer names only inside the W30 figure (caption source) and one published reference title on vascular access; none on home; hero first sentence has none |
| T3 | DONE | about: '100 percent founder owned' |
| T4 | DONE | technology: UV sentences present verbatim |
| T5 | DONE | technology: 'Silicone is published' absent; substrates paragraph quoted |
| T6 | DONE | technology: answer-6 wording verbatim, old two sentences absent |
| T7 | DONE | W04 svg has no 'not significant'; no 'hollow' on technology or evidence |
| T8 | DONE | W31 svg axis 'Grafting agent concentration (mg/mL)'; benzophenone 0 hits across all of dist |
| T9 | DONE | W30 svg contains both SBMA and CBMA series labels |
| T10 | DONE | no process-video element on home or technology (comment only) |
| T11 | DONE | 'The partner files' absent; no 510(k), PMA or Master File text on home or technology |
| T12 | DONE | each application page: one 'Regulatory path' line in the spec strip; no regulatory paragraph in the article body (indwelling mentions a Device Master File once in a process sentence) |
| E1 | DONE | fixed at the source this pass: build_figures.py DISSERTATIONS and source strings, W24 png/svg ('Horne 2024'), W24_publications.json, the inlined timeline JS bundle, publications.json; evidence and publications lists show 2024 |
| E2 | DONE | W24 timeline absent from evidence; on /about as the last section |
| E3 | DONE | evidence: id=scar before id=antifouling |
| E4 | DONE | fixed this pass (the lead's notes said done, but the tile still read '4 weeks'): W12 tile now '6 months / functional human arrays in sheep', source adds 'six-month sheep cohort, ZwiCoat internal study, 2026' |
| E5 | DONE | no archive tiles (no 1,056 / 182) on evidence or home |
| E6 | DONE | 'Archive counts: ZwiCoat Data archive.' is the last line of the evidence page body; no 'E-report method tags' |
| E7 | DONE | W26 absent from home, evidence and sensors; present on neural only |
| E8 | DONE | histology-sheep.png header re-rendered with Pillow (Arial Bold 54 px 'Coated', same cap height and baseline as 'Uncoated'); md5 0c07a519b65b870e6d0d09858eba4b34 identical in public, dist and staging |
| E9 | DONE | evidence: id=insertion-friction before id=impedance |
| E10 | DONE | evidence: W08 img width=640 |
| E11 | OPEN | W37 and its caption arrived (figures/MANIFEST-sbir.md), but the manifest carries a 'Build note, W37 (review before publishing)': the 66 percent work reduction integrates each trace over its own length, and coated traces stop earlier (14.9 to 17.8 mm against up to 23.2 mm). Over the depth every trace reaches (0 to 14 mm) the reduction is 38 percent, p = 0.14. All coated runs are repeat insertions of one array. Held off evidence and neural until Kam or the lead decides which number to publish; the PNG/SVG sit unreferenced in site/public/figures. Placement is a two-line change once decided. The W37 source line also names the insertion robot product and the sterilization vendor, which the editorial rules would strip |
| D1 | DONE | same as N1 |
| D2 | DONE | durability: no 'not shown yet' or 'come next' |
| D3 | DONE | durability: W28a img width=1000 |
| D4 | DONE | durability: pendulum-loop clip, caption 'close-up' (aspect 540/1080); clip content not re-inspected frame by frame |
| D5 | DONE | W31 on durability with the grafting-agent axis; benzophenone 0 hits |
| D6 | DONE | row header 'Compatible with multiple sterilization methods.'; W11 svg title the same, 8 tiles (7 'passed', 1 'failed'), 'not recommended' gone (build_figures.py fixed) |
| D7 | DONE | no 'intact' in the durability sterilization row; sterilization paragraph replaced with answer-8 text |
| D8 | DONE | durability uses W28a only; W28_durability_peel absent |
| U1 | DONE | Kyle, Ruby, Reineke, CIVCO: 0 hits in any html, js, json, svg or css in dist |
| U2 | DONE | ZwiGuard: 0 hits across dist (html, js, json, svg, css) |
| U3 | DONE | logo.svg?v=2 in nav and footer on every page, favicon.png?v=2 in head; logo.svg is the outlined 'ZwiCoat' wordmark with two swoosh paths (#0A68A6 and #4FA3D8). Note: build_logo.py draws both swooshes under the text; if Kam meant a swoosh above the letters, that is a logo redesign (OPEN for Kam) |
| U4 | DONE | order neural, expanders, airway, vascular, indwelling, PEEK, sensors, ENT, GI verified in nav menu and footer on all 19 pages, and in the home and index grids |
| U5 | DONE | 'overlap' 0 hits in body copy on every page |
| U6 | DONE | p values and 'read from the' only in source lines; 'not significant' 0 hits in html (it appears only inside the W25 chart image) |
| NI1 | DONE | neural: lead media is histology-sheep |
| NI2 | DONE | neural: capacitance, smaller contacts, conceals platinum, texturing sentences present; design-rationale opener removed (answer 23) |
| NI3 | DONE | neural 'The problem' first paragraph mixes a 13-word opener, a 40-word sentence and short ones (quoted in the neural section) |
| A1 | DONE | airway: lead media is the cuff-loop clip |
| A2 | DONE | airway: 'Stenosis comes first.' before 'Pneumonia comes second.'; Brodsky 2018 resolved in the reference list |
| A3 | DONE | W38 placed on airway (first result under 'What ZwiCoat does here') with the MANIFEST-sbir caption minus the p value, minimal internal source (no surgeon initials), alt text; body sentence 'Coated tubes needed about 60 percent less insertion force, for both surgeons'; card stat ~60% (62 and 61 percent per surgeon, pooled 60.8) on home and /applications; airway spec-strip evidence now lists the larynx study instead of 'no airway-tube study published' |
| A4 | DONE | airway standfirst verbatim |
| M1 | DONE | 'prestigious' 0 hits; about bio reads 'and a National Science Foundation Graduate Research Fellowship' |
| M2 | DONE | contact form: Silicone, PVC, Polyurethane, PEEK, Polyethylene, Polypropylene, Nylon, PTFE, FEP, Polycarbonate, Parylene, Titanium, Stainless steel, Nitinol, Other |
| M3 | DONE | peek: 'none published' absent; spec strip 'PEEK: rats, cranioplasty model' |
| M4 | TODO | W34 simplified (one annotation on the dry PEEK bar, no footnotes, short subtitle) is DONE; the hand-drawn grafting-pathway SVG is assigned to a later worker |
| M5 | DONE | PEEK is sixth in nav, footer and grids |
| M6 | DONE | expanders: 300 percent sentence present; '200 percent' 0 hits; card alt updated |
| M7 | DONE | home: answers 1 to 4 verified; 'the largest device markets' in W12_numbers.json and the evidence tile |
| M8 | DONE | technology: tethered-brush sentence and answer-8 sterilization paragraph; same paragraph on durability and partner |
| M9 | DONE | cards: airway ~60% ETT insertion force (answer 9, number now computed by W38), indwelling ~90%, PEEK ~635 kPa, on home and /applications |
| M10 | DONE | sensors, PEEK standfirsts; publications h1; US 12,116,498 note on publications and evidence |
| M11 | DONE | W27 svg has no PEG bar (uncoated 82, coated 27, '-67%, p = 0.010'); W25 svg shows '(not significant)' on the four-week polarization pair; founder owned kept |

## Open points for Kam

- Expander card photo: the file is `expander-inflated-200pct-01.jpg`, and the old alt said 200 percent of starting volume. Per answer 12 the alt now says 300 percent of rated volume. Confirm the photo shows the 300 percent inflation (or swap in a 300 percent still).
- US 12,116,498 note: `figures/published/patents.md` has only the schedule row (application 18/507,969, granted 2024-10-15), no claim summary, so 'continuation of the 11,814,526 family' could not be checked against the patent text. Nothing in the file contradicts it.
- Home sources sentence (answer 2) now sits above tiles that include the six-month sheep cohort (internal) and the 'patent applications pending' tile. The tile source line under Evidence says 'ZwiCoat internal study, 2026' for the six-month cohort.
- Logo: two swooshes sit under the wordmark (build_logo.py). If 'top swoosh' meant a swoosh above the letters, that is a redesign.
- W37 (E11): decide between the full-trace 66 percent and the common-depth 38 percent (p = 0.14) before it goes on evidence and neural; see the E11 row.
- W38 on airway uses data Kam held on 2026-10-30 ('ETT manuscript figures: hold until the paper is out'); answer 9 and checklist A3 ask for it now, and the raw data are public on Zenodo. Confirm.

## Final pass (2026-11-02): N3, M4, E11 and the trace viewer

Same method as above. Checker: `check_final.py` (the round-three checker with E11 inverted, the extra banned terms iotaSoft, Andersen, '[ref', six-fold, 'within seven years' and 'removed for complications', and the checks below). Run on `site/dist` after `npm run build` (20 pages, no errors or warnings), then on a curl mirror of the ten changed staging pages after `bash server/deploy-staging.sh --no-build`.

- Built site, every page and asset check (old and new): **386 PASS, 0 FAIL**.
- Staging, the ten changed pages plus the trace JSON and the W37/W38 PNGs: **210 PASS, 0 FAIL**.
- Live check in a browser on https://staging.zwicoat.com/evidence/: both viewers mounted (`traces-w37`: 11 lines, '11 insertions shown: 6 uncoated, 5 coated'; `traces-w38`: 29 lines for Surgeon 1, 60 with 'Both surgeons').
- Staging HTTP: evidence, neural-interfaces, airway, peek-and-orthopedic, tissue-expanders, vascular-access, indwelling-catheters, sensors, ent-tubes, gi-stents all 200; `/data/W37_traces.json` (61,464 bytes) and `/data/W38_traces.json` (239,867 bytes) 200 and byte-identical to `site/dist`; W37 and W38 PNGs 200.

### What changed (source files)

- `site/src/content/applications/*.md`: N3 problem statements and arguments (expanders, vascular, indwelling, sensors, ENT, GI, PEEK); airway stenosis and VAP sentences from the ready-to-paste block; neural Jones 2022 wording; PEEK Li 2017 wording; new references; W37 on neural; `{{diagram:peek-pathway}}` on PEEK; ENT devices line adds nasal splints and implants.
- `site/src/components/PeekPathway.astro` (new, M4), rendered by a new `{{diagram:name}}` token in `pages/applications/[slug].astro` and `components/MediaBlocks.astro`.
- `site/src/scripts/traces.ts` (new) and trace styles appended to `site/src/styles/charts.css`; `pages/evidence.astro` mounts two instances, fetching `/data/W37_traces.json` and `/data/W38_traces.json` (about 300 kB together, so fetched rather than inlined) and calling `showFallback` on any error.
- `site/src/data/figure-text.ts`: shared W37 and W38 alt, caption (no p values) and sanitized sources.
- `site/public/data/W37_traces.json`, `W38_traces.json`: rewritten from `figures/data` by `sanitize_traces.py` (scratchpad): file names, the source and method strings (file paths, analysis script names), p values, extubation values and the 0 to 14 mm sub-analysis removed; trial labels are now 'Coated insertion 1' and 'Surgeon 1, coated tube 2, intubation 3'. The internal originals in `figures/data` are unchanged.
- Fallback tested in dev by hiding `W37_traces.json`: the mount showed the static W37 PNG (`ichart-mount is-fallback`).

### Proof, built site (`site/dist`)

| Status | Page | Item | Proof (built HTML or file) |
|---|---|---|---|
| PASS | evidence | E11 order in the insertion section: W07, W37 viewer, W38 viewer, then W28 | `W07_insertion_force.png" alt="Three panels of insertion force for uncoated and coated cochlear implant arrays in human cadaveric cochleae, nine per group. Peak  ...` |
| PASS | evidence | E11 body sentence (W37) | `lower after three weeks in mice (Bennion 2021, Peel 2024). In a synthetic cochlea model, coated arrays inserted with about two thirds less peak force and work of insertion (NIH SBIR Phase I dataset, Zenodo). Coated endotracheal tubes needed about 60 percent less forc` |
| PASS | evidence | E11 body sentence (W38) | `e and work of insertion (NIH SBIR Phase I dataset, Zenodo). Coated endotracheal tubes needed about 60 percent less force to intubate a cadaveric human larynx, for both surgeons (ZwiCoat internal study, 2026). Every trace from both studies is drawn below.</p></div><div` |
| PASS | evidence | E11 W37 caption (MANIFEST-sbir, no p values) | `electrode array into a synthetic cochlea at constant speed. The sterilized coated array reached a 64 percent lower peak insertion force than the uncoated array (mean 17.5 versus 48.3 mN) and needed 66 percent less work of insertion (99 versus 291 mN·mm), measured on the same insertions. Each line is one insertion; select a line  ...` |
| PASS | evidence | E11 W37 sanitized source line | `its peak force and work.</p><p class="ichart-source label">Source: NIH SBIR Phase I dataset, ZwiCoat Materials Innovations, Zenodo, doi:10.5281/zenodo.10459478</p><p class="ichart-dl"><a href="/figures/W37_ci_insertion_synt` |
| PASS | evidence | E11 W38 caption | `surgeons intubated a cadaveric human larynx on a load cell. Coated endotracheal tubes needed 62 percent (Surgeon 1) and 61 percent (Surgeon 2) less integrated insertion force than the uncoated tube. Each line is one intubation, aligned to its start; choose a` |
| PASS | evidence | E11 W38 source line | `rce and integrated force.</p><p class="ichart-source label">Source: ZwiCoat internal study, 2026; raw data in the NIH SBIR Phase I dataset, Zenodo</p><p class="ichart-dl"><a href="/figures/W38_ett_insertion_for` |
| PASS | evidence | Traces: W37 noscript PNG fallback | `wer." data-fallback-width="1000" data-fallback-height="429"><noscript><img class="ch-fallback-img" src="/figures/W37_ci_insertion_synthetic.png" alt="Three panels for a cochlear implant electrode array in` |
| PASS | evidence | Traces: W38 noscript PNG fallback | `wer." data-fallback-width="1000" data-fallback-height="868"><noscript><img class="ch-fallback-img" src="/figures/W38_ett_insertion_force.png" alt="Four panels of endotracheal tube insertion force in a` |
| PASS | evidence | Traces: fallback data attributes for showFallback | `data-chart="traces-w37" data-fallback-src="/figures/W37_ci_insertion_synthetic.png"` |
| PASS | evidence | No robot or sterilization vendor names | `no match: (?i)iota\|Andersen` |
| PASS | neural-interfaces | E11 W37 after the insertion-force paragraph and W07 | `Force variation fell about 42 percent in the first study.</p> </div><div class="fig"><figure class="figure"><div class="fig-frame"><p class="fig-tag" aria-hidde ...` |
| PASS | neural-interfaces | E11 W37 sanitized source line | `class="fig-tag-id">FIG W37</span><span class="fig-tag-src">NIH SBIR Phase I dataset, ZwiCoat Materials Innovations, Zenodo, doi:10.5281/zenodo.10459478</span></p><img class="figure-img" src="/figures/W37_ci_inse` |
| PASS | neural-interfaces | Correction: spinal cord stimulator removals (Jones 2022) | `lates the contacts from the neurons they are meant to hear. In Australia, hospital records show about 4 spinal cord stimulator removals for every 10 implanted (Jones 2022).</p> <h2 id="what-zwicoat-does-here">What ZwiCoat does here<` |
| PASS | neural-interfaces | Correction: Jones 2022 full reference | `s="label">References (6)</summary><ol class="refs-list"><li>Jones CMP, Abdel Shaheed C, Ferreira G, et al. Spinal cord stimulators: an analysis of the adverse events reported to the Australian Therapeutic Goods Administration. J Patient Saf. 2022;18(5):507-511. doi:10.1097/PTS.0000000000000971</li><li>Ben-Shlomo N, Peel A, Etler ...` |
| PASS | neural-interfaces | Old 'removed for complications' wording gone | `absent: removed for complications` |
| PASS | tissue-expanders | N3 infection argument (Kraenzlin 2022) | `d fibrosis restricts filling. Infection is the bigger risk. Expander reconstruction has reported infection rates of up to 31 percent, against the 1 to 2 percent typical of surgical site infections (Kraenzlin 2022). In that series of 490 breasts, about 14 percent became infected before the second-stage operation. Infection is a l ...` |
| PASS | tissue-expanders | N3 company argument | `act downstream. None of them changes the silicone surface. That is where we start. A shell that proteins and bacteria cannot grip gives the capsule, and the bacteria, much less to build on.</p> <h2 id="what-zwicoat-does-here">What ZwiCoat does here<` |
| PASS | tissue-expanders | N3 Kraenzlin reference | `enter retrospective study. Plast Surg (Oakv). 2025.</li><li>Kraenzlin F, Habibi M, Aliu O, et al. Infections after mastectomy and tissue expander placement: a multivariate regression analysis. J Plast Reconstr Aesthet Surg. 2022;75(7):2190-2196. doi:10.1016/j.bjps.2022.01.050</li></ol></details></section></div></main><footer cla ...` |
| PASS | tissue-expanders | No 'removed after two weeks' claim | `no match: (?i)removed after (~\|about )?(2\|two) weeks` |
| PASS | airway | Correction (a): stenosis incidence (Dorris 2021; Schweiger 2013) | `ated ICU adults had laryngeal injury (Brodsky 2018).</p> <p>Reported rates of subglottic stenosis after intubation run from 0.3 percent to more than 11 percent, and in one prospective study of children under 5 in intensive care it was about 11 percent (Dorris 2021; Schweiger 2013). In a 2025 cohort of 441 intubated newborns in i ...` |
| PASS | airway | Correction (b): neonatal stenosis about 3 percent (Stoler 2025) | `care it was about 11 percent (Dorris 2021; Schweiger 2013). In a 2025 cohort of 441 intubated newborns in intensive care, about 3 percent developed subglottic stenosis (Stoler 2025). In children under 5, each extra five days of intubation rai` |
| PASS | airway | Correction (c): intubation-related stenosis cost (Yin 2019) | `intubation raised the risk about 50 percent (Manica 2013). In a four-year study of 34 patients, care for stenosis that followed intubation cost about $5,287 per patient per year, against about $2,874 for stenosis with no known cause (Yin 2019).</p> <p>Pneumonia comes second. Ventilator-associated pneumo` |
| PASS | airway | VAP 8 to 28 percent with Chastre 2002 | `h no known cause (Yin 2019).</p> <p>Pneumonia comes second. Ventilator-associated pneumonia affects 8 to 28 percent of patients on a ventilator (Chastre 2002), and each case costs about $40,000 (Zimlichman 2013). Biofilm was found on 95 percent of endotracheal tubes in on` |
| PASS | airway | Stenosis before pneumonia | `Stenosis comes first. A rigid tube scrapes the larynx on the way in, and the airway reacts to it for as long as the tube stays. In a review of nine studies, 83  ...` |
| PASS | airway | References: Dorris, Schweiger, Stoler, Yin, Chastre, Zimlichman DOI | `doi:10.1001/jamainternmed.2013.9763</li><li>Dorris ER, Russell J, Murphy M. Post-intubation subglottic stenosis: aetiology at the cellular and molecular level.  ...` |
| PASS | airway | No unsupported neonatal 1 to 11 percent | `absent: 1 to 11 percent` |
| PASS | airway | No 'lifelong' on the strength of Yin 2019 | `absent: lifelong` |
| PASS | vascular-access | N3 company argument | `polyurethane one on catheter failure (Ullman 2025).</p> <p>Occlusion, thrombus and infection look like three problems. They share one first step: protein on the catheter wall. Our argument is that the fix belongs at that step, in the surface itself. A wall that stays clean in the first seconds leaves the she` |
| PASS | vascular-access | No six-fold or HydroPICC claim | `no match: (?i)six-fold\|HydroPICC` |
| PASS | vascular-access | Zimlichman reference has its DOI | `ealth care system. JAMA Intern Med. 2013;173(22):2039-2046. doi:10.1001/jamainternmed.2013.9763</li><li>Chopra V, et al. Risk of venous thromboembolism ass` |
| PASS | indwelling-catheters | N3 AMR argument (Murray 2022) | `al.</p> <p>Antimicrobial catheters also carry a wider cost. Bacterial resistance to antimicrobials was directly responsible for an estimated 1.27 million deaths worldwide in 2019 (Murray 2022). We take a different route. ZwiCoat keeps bacteria and protein from attaching to the ca` |
| PASS | indwelling-catheters | N3 Murray reference | `trial (CATHETER). Lancet. 2012;380(9857):1927-1935.</li><li>Murray CJL, Ikuta KS, Sharara F, et al. Global burden of bacterial antimicrobial resistance in 2019: a systematic analysis. Lancet. 2022;399(10325):629-655. doi:10.1016/S0140-6736(21)02724-0</li><li>Leigh BL, Cheng E, Xu L, Derk A, Hansen MR, Guymon` |
| PASS | indwelling-catheters | No competitor catheter named | `no match: (?i)ClearTract` |
| PASS | peek-and-orthopedic | Correction: Li 2017 cranioplasty wording | `ranioplasties, 15 percent had complications (Punchak 2017). In a US claims database of 8,275 patients who had cranioplasty between 2007 and 2014, 36.6 percent had a complication, and this covers autograft and synthetic implants, not PEEK alone (Li 2017). Antibiotic-loaded bone cement made no measurable difference` |
| PASS | peek-and-orthopedic | Li 2017 full reference | `="label">References (15)</summary><ol class="refs-list"><li>Li A, Azad TD, Veeravagu A, et al. Cranioplasty complications and costs: a national population-level analysis using the MarketScan Longitudinal Database. World Neurosurg. 2017;102:209-220. doi:10.1016/j.wneu.2017.03.022</li><li>Shen N, Cheng E, Whitley JW, et al. Photog ...` |
| PASS | peek-and-orthopedic | No 'within seven years' | `absent: within seven years` |
| PASS | peek-and-orthopedic | N3 argument | `s coatings peeling, flaking and shedding (FDA 2019).</p> <p>Our argument is simple. PEEK’s weak points sit at its surface, and the surface is what we change. The coating bonds to PEEK itself, with no primer and no change to the bulk material.</p> <h2 id="what-zwicoat-does-here">What ZwiCoat does here<` |
| PASS | peek-and-orthopedic | M4 diagram in 'How it fits your process' after its lead-in | `How it fits your process</h2> <p>The diagram shows why no primer is needed: under UV light, the ketone groups in PEEK’s own backbone start the graft, and the hy ...` |
| PASS | peek-and-orthopedic | M4 label: PEEK backbone | `<text x="40" y="372" class="pp-label">PEEK backbone</text>` |
| PASS | peek-and-orthopedic | M4 label: UV light | `<text x="20" y="44" class="pp-label pp-uv-text">UV light</text>` |
| PASS | peek-and-orthopedic | M4 label: the ketone in the backbone starts the graft | `>the ketone in</text><text class="pp-label" x="150" y="150">the backbone</text><text class="pp-label" x="150" y="172">starts the graft</text>` |
| PASS | peek-and-orthopedic | M4 label: hydrogel bonded to the surface | `<text x="340" y="52" class="pp-label">hydrogel bonded to the surface</text>` |
| PASS | peek-and-orthopedic | M4 label: no primer | `<text x="470" y="266" text-anchor="middle" class="pp-tag-text">no primer</text>` |
| PASS | peek-and-orthopedic | M4 highlighted ketone C=O (double bond + O) and radical site | `class="pp-halo"></circle><line x1="106.5" y1="300" x2="106.5" y2="268" class="pp-bond pp-ket"></line><line x1="113.5" y1="300" x2="113.5" y2="268" class="pp-bon ...` |
| PASS | peek-and-orthopedic | M4 no monomer names or grafting-agent name on the page | `no match: (?i)benzophenone\|SBMA\|CBMA\|sulfobetaine\|carboxybetaine` |
| PASS | peek-and-orthopedic | M4 token replaced (no raw {{diagram}} left) | `absent: {{diagram` |
| PASS | sensors | N3 lag sentence (Zaharieva 2019) | `shows it.</p> <p>Lag matters most when glucose moves fast. During exercise, a current CGM trailed fingerstick glucose by about 12 minutes on average (Zaharieva 2019). Even a sensor built to tolerate encapsulation needed a two-` |
| PASS | sensors | N3 stabilization sentence (Gough 2010) | `ck glucose by about 12 minutes on average (Zaharieva 2019). Even a sensor built to tolerate encapsulation needed a two-week stabilization period after implantation in pigs (Gough 2010). The capsule also shows up as drift and lost sensitivity. On` |
| PASS | sensors | N3 company argument | `oid-eluting collar. That is a finite drug reservoir.</p> <p>Our argument is that the capsule starts at the surface, so the surface is where to stop it. A thin, wet hydrogel keeps proteins and cells off, and that` |
| PASS | sensors | N3 references Zaharieva and Gough | `Zaharieva DP, Turksoy K, McGaugh SM, et al. Lag time remains with newer real-time continuous glucose monitoring technology during aerobic exercise in adults liv ...` |
| PASS | sensors | No competitor sensor names | `no match: (?i)Senseonics\|Eversense\|GlySens\|Profusa\|Biolinq\|Nemaura` |
| PASS | ent-tubes | N3 nasal implant complications (Kim 2014) | `l implants and splints meet the same foreign body response. Complications of silicone nasal implants, including infection, calcification, contracture, extrusion and shift, have been reported in up to 36 percent of cases (Kim 2014). In one series of contracted nasal implants, biofilm was fou` |
| PASS | ent-tubes | N3 biofilm in contracture (Jirawatnotai 2019) | `ses (Kim 2014). In one series of contracted nasal implants, biofilm was found on 14 of the 19 with the two most severe grades (Jirawatnotai 2019).</p> <p>Today’s fixes are flushing and replacing the tube. N` |
| PASS | ent-tubes | N3 company argument | `flushing and replacing the tube. None changes the surface. Our argument is that a lumen and a shell that stay wet and slippery give mucus, bacteria and scar much less to hold on to.</p> <h2 id="what-zwicoat-does-here">What ZwiCoat does here<` |
| PASS | ent-tubes | N3 references Kim 2014 and Jirawatnotai 2019 | `Kim HS, Park SS, Kim MH, et al. Problems associated with alloplastic materials in rhinoplasty. Yonsei Med J. 2014;55(6):1617-1623. doi:10.3349/ymj.2014.55.6.161 ...` |
| PASS | gi-stents | N3 company argument | `enough to replace conventional ones (Donelli 2007).</p> <p>Almost every one of these failures begins with something settling on the stent: protein, bacteria, sludge or food. We take a different approach from slick plastics and antimicrobials. ZwiCoat holds a layer of water on the surface, so that first film has nothing to grip.< ...` |
| PASS | assets | M4 W34 single short annotation | `figures/W34_peek_bond_strength.svg: 'gel tears before' x 1` |
| PASS | assets | M4 W34 long annotation gone | `figures/W34_peek_bond_strength.svg: absent 'Every PEEK test'` |
| PASS | assets | M4 W34 footnotes gone | `figures/W34_peek_bond_strength.svg: absent 'load-cell limit'` |
| PASS | assets | M4 W34 short subtitle | `figures/W34_peek_bond_strength.svg: ..."56.603672" transform="rotate(-0 21.6 56.603672)">Lap-shear bond strength on PEEK, silicone and PVC; group means; ZwiCoat internal tests, 2025 to 2026</text> </g> </g> <defs> ...` |
| PASS | assets | E11 W37 PNG shipped | `figures/W37_ci_insertion_synthetic.png: 353,289 bytes` |
| PASS | assets | E11 W38 PNG shipped | `figures/W38_ett_insertion_force.png: 347,670 bytes` |
| PASS | assets | Traces: data/W37_traces.json holds only traces, trial and group labels and summary statistics | `11 trials; keys ['chart', 'depth', 'depth_mm', 'force', 'force_mN', 'group', 'label', 'n_coated', 'n_uncoated', 'peak_coated_mean', 'peak_mN', 'peak_reduction_pct', 'peak_uncoated_mean', 'summary', 'trials', 'units', 'work', 'work_coated_mean', 'work_mN_mm', 'work_reduction_pct', 'work_uncoated_mean']; leaks []; e.g. label 'Coat ...` |
| PASS | assets | Traces: data/W38_traces.json holds only traces, trial and group labels and summary statistics | `60 trials; keys ['Surgeon 1', 'Surgeon 2', 'chart', 'force', 'force_N', 'group', 'impulse', 'impulse_Ns', 'impulse_coated_mean', 'impulse_uncoated_mean', 'label', 'n_coated', 'n_uncoated', 'peak_N', 'per_surgeon', 'reduction_pct', 'summary', 'surgeon', 'time', 'time_s', 'trials', 'tube', 'units']; leaks []; e.g. label 'Surgeon 1 ...` |
| PASS | assets | No iotaSoft, iotaMotion, Andersen, [ref, six-fold, within seven years, removed for complications, HydroPICC or ClearTract in any shipped file | `0 hits across dist` |

### Banned-term grep on the ten changed pages (built)

| Status | Page | Item | Proof (built HTML or file) |
|---|---|---|---|
| PASS | evidence | Banned-term grep (ZwiGuard, benzophenone, monomer names, scientist/partner names, prestigious, hover or focus, UK spelling, not significant, p values outside sources, em-dash, coming next) | `no hits outside allowed contexts; allowed: SBMA in W30 figure; read from the in source/reference` |
| PASS | neural-interfaces | Banned-term grep (ZwiGuard, benzophenone, monomer names, scientist/partner names, prestigious, hover or focus, UK spelling, not significant, p values outside sources, em-dash, coming next) | `no hits outside allowed contexts; allowed: read from the in source/reference` |
| PASS | tissue-expanders | Banned-term grep (ZwiGuard, benzophenone, monomer names, scientist/partner names, prestigious, hover or focus, UK spelling, not significant, p values outside sources, em-dash, coming next) | `no hits outside allowed contexts; allowed: p < 0 in source line; p = 0 in source line; read from the in source/reference` |
| PASS | airway | Banned-term grep (ZwiGuard, benzophenone, monomer names, scientist/partner names, prestigious, hover or focus, UK spelling, not significant, p values outside sources, em-dash, coming next) | `no hits outside allowed contexts; allowed: p < 0 in source line; read from the in source/reference` |
| PASS | vascular-access | Banned-term grep (ZwiGuard, benzophenone, monomer names, scientist/partner names, prestigious, hover or focus, UK spelling, not significant, p values outside sources, em-dash, coming next) | `no hits outside allowed contexts; allowed: p < 0 in source line; read from the in source/reference; sulfobetaine in title of a published reference` |
| PASS | indwelling-catheters | Banned-term grep (ZwiGuard, benzophenone, monomer names, scientist/partner names, prestigious, hover or focus, UK spelling, not significant, p values outside sources, em-dash, coming next) | `no hits outside allowed contexts; allowed: read from the in source/reference` |
| PASS | peek-and-orthopedic | Banned-term grep (ZwiGuard, benzophenone, monomer names, scientist/partner names, prestigious, hover or focus, UK spelling, not significant, p values outside sources, em-dash, coming next) | `no hits outside allowed contexts; allowed: read from the in source/reference` |
| PASS | sensors | Banned-term grep (ZwiGuard, benzophenone, monomer names, scientist/partner names, prestigious, hover or focus, UK spelling, not significant, p values outside sources, em-dash, coming next) | `no hits outside allowed contexts; allowed: SBMA in W30 figure; read from the in source/reference` |
| PASS | ent-tubes | Banned-term grep (ZwiGuard, benzophenone, monomer names, scientist/partner names, prestigious, hover or focus, UK spelling, not significant, p values outside sources, em-dash, coming next) | `no hits outside allowed contexts; allowed: p < 0 in source line; read from the in source/reference` |
| PASS | gi-stents | Banned-term grep (ZwiGuard, benzophenone, monomer names, scientist/partner names, prestigious, hover or focus, UK spelling, not significant, p values outside sources, em-dash, coming next) | `no hits outside allowed contexts; allowed: read from the in source/reference` |

### Proof, staging mirror (https://staging.zwicoat.com)

| Status | Page | Item | Proof (built HTML or file) |
|---|---|---|---|
| PASS | evidence | E11 order in the insertion section: W07, W37 viewer, W38 viewer, then W28 | `W07_insertion_force.png" alt="Three panels of insertion force for uncoated and coated cochlear implant arrays in human cadaveric cochleae, nine per group. Peak  ...` |
| PASS | evidence | E11 body sentence (W37) | `lower after three weeks in mice (Bennion 2021, Peel 2024). In a synthetic cochlea model, coated arrays inserted with about two thirds less peak force and work of insertion (NIH SBIR Phase I dataset, Zenodo). Coated endotracheal tubes needed about 60 percent less forc` |
| PASS | evidence | E11 body sentence (W38) | `e and work of insertion (NIH SBIR Phase I dataset, Zenodo). Coated endotracheal tubes needed about 60 percent less force to intubate a cadaveric human larynx, for both surgeons (ZwiCoat internal study, 2026). Every trace from both studies is drawn below.</p></div><div` |
| PASS | evidence | E11 W37 caption (MANIFEST-sbir, no p values) | `electrode array into a synthetic cochlea at constant speed. The sterilized coated array reached a 64 percent lower peak insertion force than the uncoated array (mean 17.5 versus 48.3 mN) and needed 66 percent less work of insertion (99 versus 291 mN·mm), measured on the same insertions. Each line is one insertion; select a line  ...` |
| PASS | evidence | E11 W37 sanitized source line | `its peak force and work.</p><p class="ichart-source label">Source: NIH SBIR Phase I dataset, ZwiCoat Materials Innovations, Zenodo, doi:10.5281/zenodo.10459478</p><p class="ichart-dl"><a href="/figures/W37_ci_insertion_synt` |
| PASS | evidence | E11 W38 caption | `surgeons intubated a cadaveric human larynx on a load cell. Coated endotracheal tubes needed 62 percent (Surgeon 1) and 61 percent (Surgeon 2) less integrated insertion force than the uncoated tube. Each line is one intubation, aligned to its start; choose a` |
| PASS | evidence | E11 W38 source line | `rce and integrated force.</p><p class="ichart-source label">Source: ZwiCoat internal study, 2026; raw data in the NIH SBIR Phase I dataset, Zenodo</p><p class="ichart-dl"><a href="/figures/W38_ett_insertion_for` |
| PASS | evidence | Traces: W37 noscript PNG fallback | `wer." data-fallback-width="1000" data-fallback-height="429"><noscript><img class="ch-fallback-img" src="/figures/W37_ci_insertion_synthetic.png" alt="Three panels for a cochlear implant electrode array in` |
| PASS | evidence | Traces: W38 noscript PNG fallback | `wer." data-fallback-width="1000" data-fallback-height="868"><noscript><img class="ch-fallback-img" src="/figures/W38_ett_insertion_force.png" alt="Four panels of endotracheal tube insertion force in a` |
| PASS | evidence | Traces: fallback data attributes for showFallback | `data-chart="traces-w37" data-fallback-src="/figures/W37_ci_insertion_synthetic.png"` |
| PASS | evidence | No robot or sterilization vendor names | `no match: (?i)iota\|Andersen` |
| PASS | neural-interfaces | E11 W37 after the insertion-force paragraph and W07 | `Force variation fell about 42 percent in the first study.</p> </div><div class="fig"><figure class="figure"><div class="fig-frame"><p class="fig-tag" aria-hidde ...` |
| PASS | neural-interfaces | E11 W37 sanitized source line | `class="fig-tag-id">FIG W37</span><span class="fig-tag-src">NIH SBIR Phase I dataset, ZwiCoat Materials Innovations, Zenodo, doi:10.5281/zenodo.10459478</span></p><img class="figure-img" src="/figures/W37_ci_inse` |
| PASS | neural-interfaces | Correction: spinal cord stimulator removals (Jones 2022) | `lates the contacts from the neurons they are meant to hear. In Australia, hospital records show about 4 spinal cord stimulator removals for every 10 implanted (Jones 2022).</p> <h2 id="what-zwicoat-does-here">What ZwiCoat does here<` |
| PASS | neural-interfaces | Correction: Jones 2022 full reference | `s="label">References (6)</summary><ol class="refs-list"><li>Jones CMP, Abdel Shaheed C, Ferreira G, et al. Spinal cord stimulators: an analysis of the adverse events reported to the Australian Therapeutic Goods Administration. J Patient Saf. 2022;18(5):507-511. doi:10.1097/PTS.0000000000000971</li><li>Ben-Shlomo N, Peel A, Etler ...` |
| PASS | neural-interfaces | Old 'removed for complications' wording gone | `absent: removed for complications` |
| PASS | airway | Correction (a): stenosis incidence (Dorris 2021; Schweiger 2013) | `ated ICU adults had laryngeal injury (Brodsky 2018).</p> <p>Reported rates of subglottic stenosis after intubation run from 0.3 percent to more than 11 percent, and in one prospective study of children under 5 in intensive care it was about 11 percent (Dorris 2021; Schweiger 2013). In a 2025 cohort of 441 intubated newborns in i ...` |
| PASS | airway | Correction (b): neonatal stenosis about 3 percent (Stoler 2025) | `care it was about 11 percent (Dorris 2021; Schweiger 2013). In a 2025 cohort of 441 intubated newborns in intensive care, about 3 percent developed subglottic stenosis (Stoler 2025). In children under 5, each extra five days of intubation rai` |
| PASS | airway | Correction (c): intubation-related stenosis cost (Yin 2019) | `intubation raised the risk about 50 percent (Manica 2013). In a four-year study of 34 patients, care for stenosis that followed intubation cost about $5,287 per patient per year, against about $2,874 for stenosis with no known cause (Yin 2019).</p> <p>Pneumonia comes second. Ventilator-associated pneumo` |
| PASS | airway | VAP 8 to 28 percent with Chastre 2002 | `h no known cause (Yin 2019).</p> <p>Pneumonia comes second. Ventilator-associated pneumonia affects 8 to 28 percent of patients on a ventilator (Chastre 2002), and each case costs about $40,000 (Zimlichman 2013). Biofilm was found on 95 percent of endotracheal tubes in on` |
| PASS | airway | Stenosis before pneumonia | `Stenosis comes first. A rigid tube scrapes the larynx on the way in, and the airway reacts to it for as long as the tube stays. In a review of nine studies, 83  ...` |
| PASS | airway | References: Dorris, Schweiger, Stoler, Yin, Chastre, Zimlichman DOI | `doi:10.1001/jamainternmed.2013.9763</li><li>Dorris ER, Russell J, Murphy M. Post-intubation subglottic stenosis: aetiology at the cellular and molecular level.  ...` |
| PASS | airway | No unsupported neonatal 1 to 11 percent | `absent: 1 to 11 percent` |
| PASS | airway | No 'lifelong' on the strength of Yin 2019 | `absent: lifelong` |
| PASS | peek-and-orthopedic | Correction: Li 2017 cranioplasty wording | `ranioplasties, 15 percent had complications (Punchak 2017). In a US claims database of 8,275 patients who had cranioplasty between 2007 and 2014, 36.6 percent had a complication, and this covers autograft and synthetic implants, not PEEK alone (Li 2017). Antibiotic-loaded bone cement made no measurable difference` |
| PASS | peek-and-orthopedic | Li 2017 full reference | `="label">References (15)</summary><ol class="refs-list"><li>Li A, Azad TD, Veeravagu A, et al. Cranioplasty complications and costs: a national population-level analysis using the MarketScan Longitudinal Database. World Neurosurg. 2017;102:209-220. doi:10.1016/j.wneu.2017.03.022</li><li>Shen N, Cheng E, Whitley JW, et al. Photog ...` |
| PASS | peek-and-orthopedic | No 'within seven years' | `absent: within seven years` |
| PASS | peek-and-orthopedic | N3 argument | `s coatings peeling, flaking and shedding (FDA 2019).</p> <p>Our argument is simple. PEEK’s weak points sit at its surface, and the surface is what we change. The coating bonds to PEEK itself, with no primer and no change to the bulk material.</p> <h2 id="what-zwicoat-does-here">What ZwiCoat does here<` |
| PASS | peek-and-orthopedic | M4 diagram in 'How it fits your process' after its lead-in | `How it fits your process</h2> <p>The diagram shows why no primer is needed: under UV light, the ketone groups in PEEK’s own backbone start the graft, and the hy ...` |
| PASS | peek-and-orthopedic | M4 label: PEEK backbone | `<text x="40" y="372" class="pp-label">PEEK backbone</text>` |
| PASS | peek-and-orthopedic | M4 label: UV light | `<text x="20" y="44" class="pp-label pp-uv-text">UV light</text>` |
| PASS | peek-and-orthopedic | M4 label: the ketone in the backbone starts the graft | `>the ketone in</text><text class="pp-label" x="150" y="150">the backbone</text><text class="pp-label" x="150" y="172">starts the graft</text>` |
| PASS | peek-and-orthopedic | M4 label: hydrogel bonded to the surface | `<text x="340" y="52" class="pp-label">hydrogel bonded to the surface</text>` |
| PASS | peek-and-orthopedic | M4 label: no primer | `<text x="470" y="266" text-anchor="middle" class="pp-tag-text">no primer</text>` |
| PASS | peek-and-orthopedic | M4 highlighted ketone C=O (double bond + O) and radical site | `class="pp-halo"></circle><line x1="106.5" y1="300" x2="106.5" y2="268" class="pp-bond pp-ket"></line><line x1="113.5" y1="300" x2="113.5" y2="268" class="pp-bon ...` |
| PASS | peek-and-orthopedic | M4 no monomer names or grafting-agent name on the page | `no match: (?i)benzophenone\|SBMA\|CBMA\|sulfobetaine\|carboxybetaine` |
| PASS | peek-and-orthopedic | M4 token replaced (no raw {{diagram}} left) | `absent: {{diagram` |
| PASS | tissue-expanders | N3 infection argument (Kraenzlin 2022) | `d fibrosis restricts filling. Infection is the bigger risk. Expander reconstruction has reported infection rates of up to 31 percent, against the 1 to 2 percent typical of surgical site infections (Kraenzlin 2022). In that series of 490 breasts, about 14 percent became infected before the second-stage operation. Infection is a l ...` |
| PASS | tissue-expanders | N3 company argument | `act downstream. None of them changes the silicone surface. That is where we start. A shell that proteins and bacteria cannot grip gives the capsule, and the bacteria, much less to build on.</p> <h2 id="what-zwicoat-does-here">What ZwiCoat does here<` |
| PASS | tissue-expanders | N3 Kraenzlin reference | `enter retrospective study. Plast Surg (Oakv). 2025.</li><li>Kraenzlin F, Habibi M, Aliu O, et al. Infections after mastectomy and tissue expander placement: a multivariate regression analysis. J Plast Reconstr Aesthet Surg. 2022;75(7):2190-2196. doi:10.1016/j.bjps.2022.01.050</li></ol></details></section></div></main><footer cla ...` |
| PASS | tissue-expanders | No 'removed after two weeks' claim | `no match: (?i)removed after (~\|about )?(2\|two) weeks` |
| PASS | vascular-access | N3 company argument | `polyurethane one on catheter failure (Ullman 2025).</p> <p>Occlusion, thrombus and infection look like three problems. They share one first step: protein on the catheter wall. Our argument is that the fix belongs at that step, in the surface itself. A wall that stays clean in the first seconds leaves the she` |
| PASS | vascular-access | No six-fold or HydroPICC claim | `no match: (?i)six-fold\|HydroPICC` |
| PASS | vascular-access | Zimlichman reference has its DOI | `ealth care system. JAMA Intern Med. 2013;173(22):2039-2046. doi:10.1001/jamainternmed.2013.9763</li><li>Chopra V, et al. Risk of venous thromboembolism ass` |
| PASS | indwelling-catheters | N3 AMR argument (Murray 2022) | `al.</p> <p>Antimicrobial catheters also carry a wider cost. Bacterial resistance to antimicrobials was directly responsible for an estimated 1.27 million deaths worldwide in 2019 (Murray 2022). We take a different route. ZwiCoat keeps bacteria and protein from attaching to the ca` |
| PASS | indwelling-catheters | N3 Murray reference | `trial (CATHETER). Lancet. 2012;380(9857):1927-1935.</li><li>Murray CJL, Ikuta KS, Sharara F, et al. Global burden of bacterial antimicrobial resistance in 2019: a systematic analysis. Lancet. 2022;399(10325):629-655. doi:10.1016/S0140-6736(21)02724-0</li><li>Leigh BL, Cheng E, Xu L, Derk A, Hansen MR, Guymon` |
| PASS | indwelling-catheters | No competitor catheter named | `no match: (?i)ClearTract` |
| PASS | sensors | N3 lag sentence (Zaharieva 2019) | `shows it.</p> <p>Lag matters most when glucose moves fast. During exercise, a current CGM trailed fingerstick glucose by about 12 minutes on average (Zaharieva 2019). Even a sensor built to tolerate encapsulation needed a two-` |
| PASS | sensors | N3 stabilization sentence (Gough 2010) | `ck glucose by about 12 minutes on average (Zaharieva 2019). Even a sensor built to tolerate encapsulation needed a two-week stabilization period after implantation in pigs (Gough 2010). The capsule also shows up as drift and lost sensitivity. On` |
| PASS | sensors | N3 company argument | `oid-eluting collar. That is a finite drug reservoir.</p> <p>Our argument is that the capsule starts at the surface, so the surface is where to stop it. A thin, wet hydrogel keeps proteins and cells off, and that` |
| PASS | sensors | N3 references Zaharieva and Gough | `Zaharieva DP, Turksoy K, McGaugh SM, et al. Lag time remains with newer real-time continuous glucose monitoring technology during aerobic exercise in adults liv ...` |
| PASS | sensors | No competitor sensor names | `no match: (?i)Senseonics\|Eversense\|GlySens\|Profusa\|Biolinq\|Nemaura` |
| PASS | ent-tubes | N3 nasal implant complications (Kim 2014) | `l implants and splints meet the same foreign body response. Complications of silicone nasal implants, including infection, calcification, contracture, extrusion and shift, have been reported in up to 36 percent of cases (Kim 2014). In one series of contracted nasal implants, biofilm was fou` |
| PASS | ent-tubes | N3 biofilm in contracture (Jirawatnotai 2019) | `ses (Kim 2014). In one series of contracted nasal implants, biofilm was found on 14 of the 19 with the two most severe grades (Jirawatnotai 2019).</p> <p>Today’s fixes are flushing and replacing the tube. N` |
| PASS | ent-tubes | N3 company argument | `flushing and replacing the tube. None changes the surface. Our argument is that a lumen and a shell that stay wet and slippery give mucus, bacteria and scar much less to hold on to.</p> <h2 id="what-zwicoat-does-here">What ZwiCoat does here<` |
| PASS | ent-tubes | N3 references Kim 2014 and Jirawatnotai 2019 | `Kim HS, Park SS, Kim MH, et al. Problems associated with alloplastic materials in rhinoplasty. Yonsei Med J. 2014;55(6):1617-1623. doi:10.3349/ymj.2014.55.6.161 ...` |
| PASS | gi-stents | N3 company argument | `enough to replace conventional ones (Donelli 2007).</p> <p>Almost every one of these failures begins with something settling on the stent: protein, bacteria, sludge or food. We take a different approach from slick plastics and antimicrobials. ZwiCoat holds a layer of water on the surface, so that first film has nothing to grip.< ...` |
| PASS | assets | E11 W37 PNG shipped | `figures/W37_ci_insertion_synthetic.png: 353,289 bytes` |
| PASS | assets | E11 W38 PNG shipped | `figures/W38_ett_insertion_force.png: 347,670 bytes` |
| PASS | assets | Traces: data/W37_traces.json holds only traces, trial and group labels and summary statistics | `11 trials; keys ['chart', 'depth', 'depth_mm', 'force', 'force_mN', 'group', 'label', 'n_coated', 'n_uncoated', 'peak_coated_mean', 'peak_mN', 'peak_reduction_pct', 'peak_uncoated_mean', 'summary', 'trials', 'units', 'work', 'work_coated_mean', 'work_mN_mm', 'work_reduction_pct', 'work_uncoated_mean']; leaks []; e.g. label 'Coat ...` |
| PASS | assets | Traces: data/W38_traces.json holds only traces, trial and group labels and summary statistics | `60 trials; keys ['Surgeon 1', 'Surgeon 2', 'chart', 'force', 'force_N', 'group', 'impulse', 'impulse_Ns', 'impulse_coated_mean', 'impulse_uncoated_mean', 'label', 'n_coated', 'n_uncoated', 'peak_N', 'per_surgeon', 'reduction_pct', 'summary', 'surgeon', 'time', 'time_s', 'trials', 'tube', 'units']; leaks []; e.g. label 'Surgeon 1 ...` |
| PASS | assets | No iotaSoft, iotaMotion, Andersen, [ref, six-fold, within seven years, removed for complications, HydroPICC or ClearTract in any shipped file | `0 hits across dist` |

### Open points from this pass

- W37 build note still applies: over the depth every trace reaches (0 to 14 mm) the work difference is 38 percent (p = 0.14). The site uses the full-trace 66 percent as the lead instructed. Kam should confirm.
- The evidence page header still says 'The published evidence'; section 3 now also holds the Zenodo dataset (W37) and the internal ETT study (W38), each labeled in its source line.
- Sensors: the steroid-collar sentence was already on the page without a citation; it carries no number, so it was kept as is.

## Round five (2026-11-02 evening): FEEDBACK-ROUND5.md R1 to R21

Method as above: a script reads the BUILT pages (`site/dist`, after `npm run build`, 21 pages, no errors or warnings), decodes entities, strips the Astro `data-astro-cid` attributes and quotes the matching HTML. The same checks for home, evidence, durability, neural, tissue expanders and logo options were run again against https://staging.zwicoat.com after `bash server/deploy-staging.sh --no-build`. Interaction was checked in a preview server on port 4329 (`astro preview`, not 4321) at 1280 x 900 and 375 px: every interactive chart mounts (none falls back), no page scrolls sideways at 375 px, and the scripted checks below.

### Summary

- Built site: **79 PASS, 0 FAIL**. Staging: **54 PASS, 0 FAIL**.
- Interaction (preview, scripted): scar chart: 9 bars, count "9 of 9 measurements", species filter Rats gives "4 of 9", tooltip shows paper, year, journal, model, uncoated and coated values with unit, n and an "Open the paper" link (https://doi.org/10.1016/j.actbio.2023.05.011 for the one-year array bar); a click pins the tooltip (`pointer-events: auto`) so the link can be followed; ArrowDown moves focus to the next bar; Enter opens the DOI. Durability timeline: 7 markers (two stacked at 6 months), tooltip "6 weeks, rats / The scar capsule around coated silicone was about 75 percent thinner ... / Barrera et al. 2026, ACS Applied Polymer Materials"; ArrowRight then Enter opened https://doi.org/10.1021/acsabm.4c00156; a click on the 1-year marker opened the Horne 2023 DOI; the list under the chart links every paper. Trace viewers: two panels with titles "Uncoated (6 insertions)" at x = 58 and "Coated (5 insertions)" at x = 665; W38 with Surgeon 2 selected: "Uncoated (10 intubations)" and "Coated (21 intubations)", identical y tick labels in both panels (shared range), focus on a trace draws the highlight and peak dot and shows "Surgeon 2, uncoated tube, intubation 8, Peak force 1.59 N, Integrated force 0.95 N·s". In-vivo browser: count "50 of 50 comparisons shown"; legend Mice, Rats, Sheep, Human cadaveric cochlea, Human cadaveric larynx, Synthetic cochlea. Capsule panels: Coated on the silicone column sets `data-mode="coated"`, the uncoated image goes to opacity 0 and hidden, the coated image stays visible (0.25 s fade; none with reduced motion).
- Forbidden-term grep over every shipped HTML, JS and CSS file (figure files and `data/` excluded, see below): ZwiGuard, benzophenone, Kyle, Ruby, Reineke, CIVCO, iotaSoft, Andersen, prestigious, "hover or focus", micrometre, millimetre, "device families", "read from the", "plotted", "text states": **0 hits in HTML**. "approximate": one HTML hit, the FCOI policy's required wording ("Approximate dollar value of the SFI"), which is regulation text, not a chart disclaimer; kept. SBMA/CBMA and "p = 0"/"p < 0": **0 hits in HTML**; the evidence bundle still carries them inside the inlined data JSON (the record: `chemistry`, `device_or_substrate`, `note` and `p_text` fields). What the page shows from that data is now cleaned: the in-vivo tooltip and table strip monomer names from the device text (`deviceText()` in `studies.ts`), and the antifouling tooltip no longer shows build caveats ("ratio of plotted bars ... inventory caveat"). One displayed p string remains in an antifouling tooltip "p" row: "0.02 or less; new vs 6-month p = 0.73" (data, not body copy).
- Tiles: no "dissertations" in the tiles section (checked on the built home page; the evidence page has no tiles).

### What changed (source files, so a rebuild keeps it)

- New: `site/src/scripts/fibrosis.ts` (W04 interactive), `site/src/scripts/durability.ts` (W06 interactive), `site/src/components/FibrosisChart.astro`, `DurabilityChart.astro` (each mounts every instance on a page, PNG fallback through `InteractiveChart`), `CapsulePanels.astro` (R9), `ImpactBlock.astro` (pendulum clip with the before and after photos, R13 and R18), `site/src/data/source-short.ts` (the manifests' `source_short` column, one line per chart).
- `Figure.astro`, `InteractiveChart.astro`: new `sourceShort` prop; the displayed source is `sourceShort`, else the manifest short source for that chart name, else `source`. The full `source` stays in the code as the record and is not rendered. `Photo.astro`, `VideoLoop.astro`: `sourceShort` shown in place of `credit` when given; `Photo` also takes `maxWidth` (used for the small slide-2 photos and the elemental map). `Figure.astro` caps every chart at its design width (half the 2x PNG width, 45 percent for tall charts) unless `maxWidth` is given.
- `figure-text.ts`: `sourceShort` on every entry; W07 caption, alt and body for three studies; new W06, W08, W11, W24, W02 and W32 entries; W04 alt says 9 measurements (the chart has 9 bars).
- Application frontmatter: `sourceShort` added under every figure's `source` (schema: optional `sourceShort` and `width`); W07 caption, alt and full source updated on neural and airway; tissue expanders W17 `width: 640`.
- `[slug].astro` and `MediaBlocks.astro`: tokens `{{interactive:durability}}`, `{{panels:capsule}}`, `{{block:impact}}`, `{{photopair:name}}` (pairs `expander-fill` and `expander-300`), `{{video:pendulum}}`; ent-tubes, indwelling catheters and vascular access now use `{{interactive:durability}}` in place of the static W06.
- `studies.ts`: species keys `larynx` (Human cadaveric larynx, darker orange) and `synthetic` (Synthetic cochlea, gray); Insertion force group matches impulse and work; left band labeled "Ex vivo / bench"; "Approximate, read from the plot" badges reworded "Estimated from a published plot". Same rewording in `antifouling.ts`.
- `traces.ts`: two panels (uncoated left, coated right) on one shared x and y range, group label above each, no overlay; stacks below 520 px.
- `ClaimRow.astro`: `wide` prop (text on top, figure full width), used for every static-chart row on home, technology and durability (R19). Technology two-column blocks put their charts full width. Evidence impedance pair stacked.
- Images: `expander-inflation-100pct.jpg` and `-300pct.jpg` (Pillow, 1600 px wide, JPEG q85, 108 and 102 kB); JPEG copies of the four capsule panels, `histology-scar-01`, `expander-deflated` and `expander-inflated` (q88, native size). The PNG originals are left in place.
- Tiles (R12): `site/public/data/W12_numbers.json` and `figures/data/W12_numbers.json`; `figures/build_figures.py` NUMBERS (the W12 tile data, read only by `w12_numbers`) and the W12 caption and source strings in `w12_numbers`; the W12 row of `figures/MANIFEST.md` to match. The figures script was not re-run (W12 PNG is not used on the site).
- `logo-options.astro`: the favicon row wraps (it scrolled sideways by 10 px at 375 px).
- `.claude/launch.json`: a `site-preview` entry on port 4329 for the sizing screen.

### R19 figure sizing screen (1280 px, every `figure img` and every interactive fallback)

Rule: flag rendered width under 480 px when natural is over 1800 (text too small) and over 1000 px when natural is under 1200 (oversized); rule of thumb rendered at least 45 percent of natural for the 2x charts. Natural width from the decoded image. Before this pass every chart in a claim row rendered at 681 px (26 to 38 percent); they now take a full-width row. No image is flagged. W30 (43 percent) and W37 (42 percent) reach the 1200 px container and cannot grow further at this breakpoint.

| Page | Image | Rendered (px) | Natural (px) | Rendered / natural | Flag |
|---|---|---|---|---|---|
| / | W27_capsule_thickness_mice.png | 1198 | 2491 | 48% | ok |
| / | W25_sheep_impedance_components.png | 1198 | 2434 | 49% | ok |
| / | W07_insertion_force.png | 1198 | 2522 | 48% | ok |
| / | W29_bacteria_rats.png | 1198 | 2577 | 46% | ok |
| / | W28_durability_peel.png | 1198 | 2611 | 46% | ok |
| / | W04_fibrosis_by_study.png (interactive; PNG only without JS) | 663 | 2496 | 27% | ok (HTML chart; fallback only) |
| / | W24_publication_timeline.png (interactive; PNG only without JS) | 1200 | 2316 | 52% | ok |
| /technology | W05_antifouling_and_friction.png | 1051 | 2340 | 45% | ok (tall chart, capped at 45%) |
| /technology | W04_fibrosis_by_study.png | 1198 | 2496 | 48% | ok |
| /technology | W27_capsule_thickness_mice.png | 1198 | 2491 | 48% | ok |
| /technology | W07_insertion_force.png | 1198 | 2522 | 48% | ok |
| /technology | W08_impedance_sheep.png | 709 | 1421 | 50% | ok |
| /technology | histology-sheep.png | 1066 | 1750 | 61% | ok |
| /technology | W28_durability_peel.png | 1198 | 2611 | 46% | ok |
| /technology | W11_sterilization.png | 982 | 1967 | 50% | ok |
| /technology | ci-array-elemental-map.png | 842 | 844 | 100% | ok (capped at native) |
| /technology | W10_substrate_evidence_matrix.png | 1057 | 2117 | 50% | ok |
| /technology | W31_bond_strength_vs_grafting_agent.png | 788 | 1579 | 50% | ok |
| /technology | W30_crosslinker_tradeoff.png | 1198 | 2807 | 43% | at the 1200 px container limit |
| /technology | W06_durability_timeline.png (interactive; PNG only without JS) | 1200 | 2057 | 58% | ok |
| /evidence | histology-scar-01.jpg | 734 | 965 | 76% | ok |
| /evidence | W27_capsule_thickness_mice.png | 1198 | 2491 | 48% | ok |
| /evidence | W29_bacteria_rats.png | 1198 | 2577 | 46% | ok |
| /evidence | W28_durability_peel.png | 1198 | 2611 | 46% | ok |
| /evidence | W07_insertion_force.png | 1198 | 2522 | 48% | ok |
| /evidence | W08_impedance_sheep.png | 709 | 1421 | 50% | ok |
| /evidence | W25_sheep_impedance_components.png | 1198 | 2434 | 49% | ok (was 578, 24%, in a pair) |
| /evidence | histology-sheep.png | 734 | 1750 | 42% | ok (photo) |
| /evidence | W31_bond_strength_vs_grafting_agent.png | 788 | 1579 | 50% | ok (was 1198, 76%, oversized) |
| /evidence | W30_crosslinker_tradeoff.png | 1198 | 2807 | 43% | at the 1200 px container limit |
| /evidence | W04_fibrosis_by_study.png (interactive) | 1200 | 2496 | 48% | ok |
| /evidence | W05_antifouling_and_friction.png (interactive) | 1200 | 2340 | 51% | ok |
| /evidence | W37_ci_insertion_synthetic.png (interactive) | 1200 | 2879 | 42% | ok (HTML chart; fallback only) |
| /evidence | W38_ett_insertion_force.png (interactive) | 1200 | 2256 | 53% | ok |
| /evidence | W06_durability_timeline.png (interactive) | 1200 | 2057 | 58% | ok |
| /evidence | W02_lapshear_database.png (interactive) | 1200 | 2090 | 57% | ok |
| /evidence | W04_fibrosis_by_study.png (interactive, in-vivo browser) | 1200 | 2496 | 48% | ok |
| /durability | W28a_friction_after_explant.png | 887 | 1777 | 50% | ok (was 681, 38%) |
| /durability | W35_wear_2500_passes.png | 887 | 1778 | 50% | ok (was 681, 38%) |
| /durability | W36_dry_and_rewet.png | 1082 | 2167 | 50% | ok (was 681, 31%) |
| /durability | expander-impact-before.jpg | 579 | 2000 | 29% | ok (photo) |
| /durability | expander-impact-after.jpg | 579 | 2000 | 29% | ok (photo) |
| /durability | W31_bond_strength_vs_grafting_agent.png | 788 | 1579 | 50% | ok |
| /durability | W11_sterilization.png | 982 | 1967 | 50% | ok (was 681, 35%) |
| /durability | W06_durability_timeline.png (interactive) | 683 | 2057 | 33% | ok (HTML chart; fallback only) |
| /durability | pendulum-loop.webm (video) | 385 | 540 | 71% | ok |
| /applications/neural-interfaces | capsule-pdms-uncoated.jpg | 423 | 1178 | 36% | ok (micrograph; labels about 14 px) |
| /applications/neural-interfaces | capsule-pdms-coated.jpg | 423 | 1163 | 36% | ok |
| /applications/neural-interfaces | capsule-pt-uncoated.jpg | 423 | 1169 | 36% | ok |
| /applications/neural-interfaces | capsule-pt-coated.jpg | 423 | 1179 | 36% | ok |
| /applications/neural-interfaces | W27_capsule_thickness_mice.png | 1198 | 2491 | 48% | ok (was 990, 40%) |
| /applications/neural-interfaces | W25_sheep_impedance_components.png | 1198 | 2434 | 49% | ok |
| /applications/neural-interfaces | W26_sheep_histology.png | 1198 | 2434 | 49% | ok |
| /applications/neural-interfaces | histology-sheep.png | 990 | 1750 | 57% | ok |
| /applications/neural-interfaces | W07_insertion_force.png | 1198 | 2522 | 48% | ok |
| /applications/neural-interfaces | W37_ci_insertion_synthetic.png | 1198 | 2879 | 42% | at the 1200 px container limit |
| /applications/neural-interfaces | ci-array-elemental-map.png | 842 | 844 | 100% | ok (was 990, upscaled) |
| /applications/neural-interfaces | ci-array-coated-dyed.png | 990 | 1594 | 62% | ok |
| /applications/neural-interfaces | ci-proxy-section-blue-ring.jpg | 934 | 2816 | 33% | ok (photo) |
| /applications/airway | ett-cuff-coated.jpg | 306 | 1080 | 28% | ok (portrait photo) |
| /applications/airway | W19_silver_ett_forest.png | 1187 | 2378 | 50% | ok |
| /applications/airway | W38_ett_insertion_force.png | 1126 | 2256 | 50% | ok |
| /applications/airway | W21_mucus_flow.png | 1039 | 2082 | 50% | ok |
| /applications/airway | W07_insertion_force.png | 1198 | 2522 | 48% | ok |
| /applications/airway | cuff-loop.webm (video) | 306 | 540 | 57% | ok |
| /applications/ent-tubes | W21_mucus_flow.png | 1039 | 2082 | 50% | ok |
| /applications/ent-tubes | W05_antifouling_and_friction.png | 1051 | 2340 | 45% | ok (tall chart, capped at 45%) |
| /applications/ent-tubes | W06_durability_timeline.png (interactive) | 1200 | 2057 | 58% | ok |
| /applications/gi-stents | W29_bacteria_rats.png | 1198 | 2577 | 46% | ok |
| /applications/gi-stents | W21_mucus_flow.png | 1039 | 2082 | 50% | ok |
| /applications/gi-stents | W11_sterilization.png | 982 | 1967 | 50% | ok |
| /applications/gi-stents | W10_substrate_evidence_matrix.png | 1057 | 2117 | 50% | ok |
| /applications/indwelling-catheters | W18_silver_foley_cauti.png | 647 | 1298 | 50% | ok (was 990, 76%, oversized) |
| /applications/indwelling-catheters | W29_bacteria_rats.png | 1198 | 2577 | 46% | ok |
| /applications/indwelling-catheters | W28_durability_peel.png | 1198 | 2611 | 46% | ok |
| /applications/indwelling-catheters | W06_durability_timeline.png (interactive) | 1200 | 2057 | 58% | ok |
| /applications/peek-and-orthopedic | W34_peek_bond_strength.png | 1082 | 2167 | 50% | ok |
| /applications/peek-and-orthopedic | W10_substrate_evidence_matrix.png | 1057 | 2117 | 50% | ok |
| /applications/peek-and-orthopedic | W05_antifouling_and_friction.png | 1051 | 2340 | 45% | ok (tall chart, capped at 45%) |
| /applications/peek-and-orthopedic | W04_fibrosis_by_study.png | 1198 | 2496 | 48% | ok |
| /applications/sensors | W20_cgm_delay.png | 512 | 1143 | 45% | ok (tall chart; was 702, 61%) |
| /applications/sensors | W27_capsule_thickness_mice.png | 1198 | 2491 | 48% | ok |
| /applications/sensors | W30_crosslinker_tradeoff.png | 1198 | 2807 | 43% | at the 1200 px container limit |
| /applications/tissue-expanders | W27_capsule_thickness_mice.png | 1198 | 2491 | 48% | ok |
| /applications/tissue-expanders | W17_textured_implants.png | 638 | 1236 | 52% | ok (width 640, R16) |
| /applications/tissue-expanders | W04_fibrosis_by_study.png | 1198 | 2496 | 48% | ok |
| /applications/tissue-expanders | expander-deflated.jpg | 342 | 364 | 94% | ok (cap 546 = 1.5x) |
| /applications/tissue-expanders | expander-inflated.jpg | 342 | 447 | 77% | ok (cap 670 = 1.5x) |
| /applications/tissue-expanders | expander-inflation-100pct.jpg | 486 | 1600 | 30% | ok (photo) |
| /applications/tissue-expanders | expander-inflation-300pct.jpg | 486 | 1600 | 30% | ok (photo) |
| /applications/tissue-expanders | W11_sterilization.png | 982 | 1967 | 50% | ok |
| /applications/tissue-expanders | expander-impact-before.jpg | 579 | 2000 | 29% | ok (photo) |
| /applications/tissue-expanders | expander-impact-after.jpg | 579 | 2000 | 29% | ok (photo) |
| /applications/tissue-expanders | pendulum-loop.webm (video) | 385 | 540 | 71% | ok |
| /applications/vascular-access | W05_antifouling_and_friction.png | 1051 | 2340 | 45% | ok (tall chart, capped at 45%) |
| /applications/vascular-access | W28_durability_peel.png | 1198 | 2611 | 46% | ok |
| /applications/vascular-access | W31_bond_strength_vs_grafting_agent.png | 788 | 1579 | 50% | ok |
| /applications/vascular-access | W06_durability_timeline.png (interactive) | 1200 | 2057 | 58% | ok |
| /about | W24_publication_timeline.png (interactive) | 1200 | 2316 | 52% | ok |

### Built site checks (site/dist)

| Status | R | Page | Item | Proof |
|---|---|---|---|---|
| PASS | R1 | evidence | Section 1 order: interactive W04, histology photo, W27 | positions data-chart="fibrosis"@13767, histology-scar-01\.jpg@15792, /figures/W27_capsule_thickness_mice\.png@16847 |
| PASS | R1 | evidence | Interactive W04 frame with PNG fallback | <div class="ev-body"><figure class="ichart"><div class="ichart-mount" data-chart="fibrosis" data-fallback-src="/figures/W04_fibrosis_by_study.png" data-fallback-alt="Horizontal bar chart of 9 measurements of scar cap |
| PASS | R1 | evidence | Histology caption | c"></div></div><figcaption class="photo-cap"><p class="photo-caption">Tissue section after one year in a mouse: a thick capsule on uncoated silicone, a thin quiet interface on coated silicone. Adapted from Horne et al., Acta Biomaterialia 2023.</p><p class="photo-credit label">Adapted from Horne et al., Acta Biom |
| PASS | R10 | home | Hero holds the interactive W04 (compact) | class="btn-outline" href="/partner#form">Send us parts</a></div></div><div class="hero-figure"><figure class="ichart compact"><div class="ichart-mount" data-chart="fibrosis" data-fallback-src="/figures/W04_fibrosis_by_study.png" data-fallback- |
| PASS | R10 | home | Hero noscript PNG fallback | ut 85 percent." data-fallback-width="1000" data-fallback-height="572"><noscript><img class="ch-fallback-img" src="/figures/W04_fibrosis_by_study.png" alt="Horizontal bar chart of 9 measurements of scar capsule or fibros |
| PASS | R10 | home | Two-column hero layout kept | er(`change`,()=>s(!1))}</script><main id="main"><section class="hero"><div class="container hero-grid"><div class="hero-text"><p class="label">Zwitterionic hydrogel coating for medical devices</p> |
| PASS | R2/R20 | home | 12 displayed source lines, none with a disclaimer | 12 lines checked |
| PASS | R2/R20 | evidence | 25 displayed source lines, none with a disclaimer | 25 lines checked |
| PASS | R2/R20 | durability | 16 displayed source lines, none with a disclaimer | 16 lines checked |
| PASS | R2/R20 | neural | 15 displayed source lines, none with a disclaimer | 15 lines checked |
| PASS | R2/R20 | tissue-expanders | 12 displayed source lines, none with a disclaimer | 12 lines checked |
| PASS | R2/R20 | logo-options | 0 displayed source lines, none with a disclaimer | 0 lines checked |
| PASS | R2/R20 | technology | 24 displayed source lines, none with a disclaimer | 24 lines checked |
| PASS | R2/R20 | applications | 0 displayed source lines, none with a disclaimer | 0 lines checked |
| PASS | R2/R20 | ent-tubes | 5 displayed source lines, none with a disclaimer | 5 lines checked |
| PASS | R2/R20 | indwelling-catheters | 7 displayed source lines, none with a disclaimer | 7 lines checked |
| PASS | R2/R20 | vascular-access | 7 displayed source lines, none with a disclaimer | 7 lines checked |
| PASS | R2/R20 | airway | 10 displayed source lines, none with a disclaimer | 10 lines checked |
| PASS | R2/R20 | peek | 9 displayed source lines, none with a disclaimer | 9 lines checked |
| PASS | R2/R20 | sensors | 6 displayed source lines, none with a disclaimer | 6 lines checked |
| PASS | R2/R20 | gi-stents | 8 displayed source lines, none with a disclaimer | 8 lines checked |
| PASS | R2/R20 | about | 1 displayed source lines, none with a disclaimer | 1 lines checked |
| PASS | R2 | evidence | W05 short source (citation plus figures) | hen select a bar to see its values.</p><p class="ichart-source label">Source: Leigh et al. 2017, Biomacromolecules, Figs 4, 6E, 7E and 8E; Leigh et al. 2019, Langmuir, Figs 7D and 10D; Jensen et al. 2021, ACS |
| PASS | R2 | neural | W25 short source on an application page |  at implantation and at four weeks.</p><p class="figure-source label">Source: Ben-Shlomo et al. 2026, Hearing Research, Figs 3B to 3D</p></figcaption></figure></div><div class="prose"> <p><strong>Less inflam |
| PASS | R3 | evidence | Section 3 order: W28, cochlear viewer, ETT viewer, W07 | positions /figures/W28_durability_peel\.png@22560, data-chart="traces-w37"@23401, data-chart="traces-w38"@25562, /figures/W07_insertion_force\.png@27858 |
| PASS | R4 | evidence | Viewer captions say uncoated left, coated right |  of insertion (99 versus 291 mN·mm), measured on the same insertions. Uncoated insertions are on the left and coated on the right, on the same scales. Each line is one insertion; select a line to see its peak force and w |
| PASS | R5 | evidence | W07 caption names three studies |  arrays needed about half the peak insertion force of uncoated arrays in three studies: 42 percent less in human cadaveric cochleae (Bennion 2021), about 50 percent less in human cadaveric cochleae (Peel 2024) and 64 percent less in a synthetic cochlea (NIH SBIR Phase I dataset).</p><p class="figure-source label">Source: |
| PASS | R5 | neural | Neural page keeps W37 static | H SBIR Phase I dataset, Zenodo, doi:10.5281/zenodo.10459478</span></p><img class="figure-img" src="/figures/W37_ci_insertion_synthetic.png" alt="Three panels for a cochlear implant electrode array inserted by  |
| PASS | R6 | evidence | Interactive W06 with PNG fallback | <div class="ev-body"><figure class="ichart"><div class="ichart-mount" data-chart="durability" data-fallback-src="/figures/W06_durability_timeline.png" data-fallback-alt="Timeline of in-vivo checkpoints from two weeks to  |
| PASS | R6 | evidence | No static W06 image | absent: <img class="figure-img" src="/figures/W06_durability_timeline |
| PASS | R6 | durability | Interactive W06 with PNG fallback | ="claim-figure"><div><figure class="ichart"><div class="ichart-mount" data-chart="durability" data-fallback-src="/figures/W06_durability_timeline.png" data-fallback-alt="Timeline of in-vivo checkpoints from two weeks to  |
| PASS | R6 | durability | No static W06 image | absent: <img class="figure-img" src="/figures/W06_durability_timeline |
| PASS | R6 | technology | Interactive W06 with PNG fallback | "><div class="stack"><figure class="ichart"><div class="ichart-mount" data-chart="durability" data-fallback-src="/figures/W06_durability_timeline.png" data-fallback-alt="Timeline of in-vivo checkpoints from two weeks to  |
| PASS | R6 | technology | No static W06 image | absent: <img class="figure-img" src="/figures/W06_durability_timeline |
| PASS | R6 | ent-tubes | Interactive W06 with PNG fallback | div><div class="fig"><figure class="ichart"><div class="ichart-mount" data-chart="durability" data-fallback-src="/figures/W06_durability_timeline.png" data-fallback-alt="Timeline of in-vivo checkpoints from two weeks to  |
| PASS | R6 | ent-tubes | No static W06 image | absent: <img class="figure-img" src="/figures/W06_durability_timeline |
| PASS | R6 | indwelling-catheters | Interactive W06 with PNG fallback | div><div class="fig"><figure class="ichart"><div class="ichart-mount" data-chart="durability" data-fallback-src="/figures/W06_durability_timeline.png" data-fallback-alt="Timeline of in-vivo checkpoints from two weeks to  |
| PASS | R6 | indwelling-catheters | No static W06 image | absent: <img class="figure-img" src="/figures/W06_durability_timeline |
| PASS | R6 | vascular-access | Interactive W06 with PNG fallback | div><div class="fig"><figure class="ichart"><div class="ichart-mount" data-chart="durability" data-fallback-src="/figures/W06_durability_timeline.png" data-fallback-alt="Timeline of in-vivo checkpoints from two weeks to  |
| PASS | R6 | vascular-access | No static W06 image | absent: <img class="figure-img" src="/figures/W06_durability_timeline |
| PASS | R8 | evidence | No stat tiles on the evidence page | absent: class="tiles|tile-value |
| PASS | R9 | neural | Capsule panels are the page lead (before the spec strip) |  working implants, and a surface the tissue leaves alone.</p></header><div class="lead-media"><div class="fig"><figure class="cp" data-capsule-panels><div class="cp-box"><p class="fig-tag" aria-hidden="true"><span class |
| PASS | R9 | neural | Columns Silicone and Platinum | ia-labelledby="cp-silicone"><div class="cp-head"><h3 class="cp-title" id="cp-silicone">Silicone</h3><div class="cp-toggle" role="group" aria-label="Silicone: show uncoated, coated or both" hidden><button type="button" data-mode-btn="uncoated" aria-pressed="false">Uncoated</button><button type="button" data-mode-btn="coated" aria ... |
| PASS | R9 | neural | Toggle buttons Uncoated / Coated / Compare (aria-pressed) | e="group" aria-label="Silicone: show uncoated, coated or both" hidden><button type="button" data-mode-btn="uncoated" aria-pressed="false">Uncoated</button><button type="button" data-mode-btn="coated" aria-pressed="false">Coated</button><button type="button" data-mode-btn="compare" aria-pressed="true">Compare</button></div></div> ... |
| PASS | R9 | neural | All four images in the markup (compare state without JS) | lass="cp-stack"><div class="cp-img cp-uncoated"><img src="/images/lab/capsule-pdms-uncoated.jpg" alt="Tissue section next to uncoated silicone (PDMS) on an implanted array, explanted from a mouse. A thick blue-stained band of fibrous capsule runs along the silicone surface, marked by red lines across its width." width="1178" hei ... |
| PASS | R9 | neural | Caption with 47 to 18 micrometers | , but a thin, quiet interface on coated silicone and coated platinum. Mean capsule thickness on the device fell about 60 percent, 47 to 18 micrometers, with coating.</p><p class="cp-credit label">Adapted from Horne et al., Acta Biomate |
| PASS | R9 | neural | Credit | nt, 47 to 18 micrometers, with coating.</p><p class="cp-credit label">Adapted from Horne et al., Acta Biomaterialia 2023</p></figcaption></figure><script type="module">document.querySelectorAll( |
| PASS | R9 | neural | Sheep histology moved lower (after W26) | search, Figs 6E to 6G</span></p><img class="figure-img" src="/figures/W26_sheep_histology.png" alt="Three small charts comparing uncoated and coated arrays at the round window of the sheep cochlea: cell nuclei density, macrophage density and fibrosis. The pooled coated bar is lower in all three. A line joins each of the three sh ... |
| PASS | R11 | home | Applications heading | class="section-head"><p class="label">Applications</p><h2 id="apps-h">Nine places to start. ZwiCoat bonds to the elastomers and plastics most devices are made of.</h2><p class="apps-intro">Each page starts with the clinical problem, |
| PASS | R11 | home | Intro sentence | mers and plastics most devices are made of.</h2><p class="apps-intro">Each page starts with the clinical problem, then shows what coated devices achieved in published studies.</p></div><ul class="grid" role="list"><li><a class="card" href="/appl |
| PASS | R11 | home | No "device families" | absent: device families |
| PASS | R11 | applications | Applications heading | ction"><header class="page-head"><p class="label">Applications</p><h1>Nine places to start. ZwiCoat bonds to the elastomers and plastics most devices are made of.</h1><p class="lead">Each page starts with the clinical problem, then  |
| PASS | R11 | applications | Intro sentence | elastomers and plastics most devices are made of.</h1><p class="lead">Each page starts with the clinical problem, then shows what coated devices achieved in published studies.</p></header><ul class="grid" role="list"><li><a class="card" href="/a |
| PASS | R11 | applications | No "device families" | absent: device families |
| PASS | R12 | home | Tiles below the "Ten years of published work" section | positions id="timeline-h"@24496, id="numbers-h"@26133 |
| PASS | R12 | home | ~60% tile | ro and in four animal and cadaver models.</span></li><li class="tile"><span class="tile-value">~60%</span><span class="tile-label label">thinner fibrotic capsule around coated implants</span><span class="tile-takeaway">One year in mice, on human cochlear implant arrays, over platinum and silicone alike (Horne 2023).</span></li>< ... |
| PASS | R12 | home | ~50% tile | n and Mexico: the largest device markets.</span></li><li class="tile"><span class="tile-value">~50%</span><span class="tile-label label">less insertion force with coated cochlear implants</span><span class="tile-takeaway">Three studies: human cadaver cochleae twice and a synthetic cochlea (Bennion 2021, Peel 2024, SBIR dataset). ... |
| PASS | R12 | home | No dissertations tile | absent: tile-label label">PhD dissertations |
| PASS | R12 | home | No patents-pending tile | absent: patent applications pending |
| PASS | R12 | home | No "dissertations" anywhere in the tiles section | absent: dissertation |
| PASS | R13 | durability | Impact block: clip left, photos right | </p></div></div><div class="claim-figure"><div><figure class="impact"><div class="impact-grid"><div class="impact-video"><figure class="vl" style="--ratio: 0.6667;"><div class="vl-box"><p class="fig-tag" aria-hidden="true"><span class="fig-tag-id">VIDEO</span><span class="fig-tag-src">ZwiCoat, 2026</span></p><div class="vl-frame ... |
| PASS | R13 | durability | Photo captions | c"></div></div><figcaption class="photo-cap"><p class="photo-caption">Before impact</p><p class="photo-credit label">ZwiCoat, 2026</p></figcaption></figure><figure class="photo" style="--ratio: 2.0000;"><div class="photo-box"><p class="fig-tag" aria-hidden="true"><span class="fig-tag-id">PHOTO</span><span class="fig-tag-src">Zwi ... |
| PASS | R13 | durability | Lead-in and 45 J caption | h2 class="claim-title">It takes a hit.</h2><div class="claim-body"><p>A 45 J pendulum strike on a coated tissue expander.</p><p>The photographs show the expander before and after the strike.  |
| PASS | R13 | durability | Source line | strike on a coated tissue expander.</p><p class="impact-source label">Source: ZwiCoat internal test, 2026</p></figcaption></figure></div></div></section><section class="claim reve |
| PASS | R14 | durability | Clip aspect 540/810 and poster | <div class="impact-grid"><div class="impact-video"><figure class="vl" style="--ratio: 0.6667;"><div class="vl-box"><p class="fig-tag" aria-hidden="true"><span class="fig-tag-id">VIDEO</span><span class="fig-tag-src">ZwiCoat, 2026</span></p><div class="vl-frame" style="aspect-ratio: 540/810;"><video data-loop autoplay muted loop  ... |
| PASS | R15 | durability | Side panel title | t (Leigh 2019).</p><aside class="bond-panel" aria-labelledby="bond-h"><h3 id="bond-h" class="bond-title">Bond strength on silicone today</h3><ul class="bond-list" role="list"><li><span class="bond-val">~105 kPa< |
| PASS | R15 | durability | Panel values | oday</h3><ul class="bond-list" role="list"><li><span class="bond-val">~105 kPa</span> <span class="bond-lab">median as prepared (36 groups, 123 tests, 2025 to 2026)</span></li><li><span class="bond-val">~94 kPa</span> <span class="bond-lab">median after soaking in PBS (26 groups, 2025)</span></li><li><span class="bond-val bond-t ... |
| PASS | R15 | durability | Panel sentence and source | 2019 published film (Leigh 2019)</span></li></ul><p class="bond-text">The bond is measured by pulling the film off silicone; today's groups sit above the 2019 published values, and the gel still tears first.</p><p class="bond-src label">Source: ZwiCoat lap-shear database, 2025 to 2026; Leigh 2019, Fig 6</p></aside></div></div><d ... |
| PASS | R16 | tissue-expanders | W17 capped at 640 px | ants and expanders, and textured use fell.</p> </div><div class="fig"><figure class="figure" style="max-width: min(100%, 640px);" data-design-width="618"><div class="fig-frame"><p class="fig-tag" aria-hidden="true"><span class="fig-tag-id">FIG W17</span><span class="fig-tag-src">Matros et al. 2021, Plastic and Reconstructi |
| PASS | R17 | tissue-expanders | Slide 2 pair after the 300 percent sentence, slide 3 pair beneath | positions inflated to 300 percent of its rated volume kept the coating@17100, expander-deflated\.jpg@17500, expander-inflated\.jpg@17944, expander-inflation-100pct\.jpg@18656, expander-inflation-300pct\.jpg@19166 |
| PASS | R17 | tissue-expanders | Slide 3 caption | re></div></div><figcaption class="ppair-cap"><p class="ppair-caption">A coated 100 cc expander inflated to 300 cc: no tearing. ZwiCoat internal test, 2026.</p><p class="ppair-credit label">ZwiCoat, 2026</p></figcaption></figu |
| PASS | R17 | tissue-expanders | Small originals capped at 1.5x (546 and 670 px) | ><div class="pair-item"><figure class="photo" style="--ratio: 0.9529; --max-w: 546px;"><div class="photo-box"><div class="photo-frame fit-contain" style="aspect-ratio: 364/382;"><img src="/images/lab/expander-deflated.jpg" alt="A deflated coated tissue expander lying folded in a glass bowl of blue liquid." loading="lazy" decodin ... |
| PASS | R18 | tissue-expanders | "Takes a hit" block before "How to start" | positions id="takes-a-hit">Takes a hit</h2>@21297, pendulum-loop@22094, expander-impact-after\.jpg@23911, id="how-to-start"@24536 |
| PASS | R18 | tissue-expanders | 45 J cited | ="prose"> <h2 id="takes-a-hit">Takes a hit</h2> <p>Expanders get hit. A 45 J pendulum strike on a coated expander left no visible damage to the coating (ZwiCoat internal test, 2026). <a href="/durability">See the durability record.</a></p> </div><div  |
| PASS | R7 | evidence | W32 data: 50 rows, 2 larynx, 2 synthetic cochlea | 50 rows; larynx ['Intubation impulse (integrated insertion force)', 'Intubation impulse (integrated insertion force)']; synthetic ['Peak insertion force', 'Work of insertion'] |
| PASS | R7 | evidence bundle | Legend entry: Human cadaveric larynx | uman cadaveric cochlea`,cls:`sp-human`},larynx:{label:`Human cadaveric larynx`,cls:`sp-larynx`},synthetic:{label:`Synthetic cochlea`,cl |
| PASS | R7 | evidence bundle | Legend entry: Synthetic cochlea | uman cadaveric larynx`,cls:`sp-larynx`},synthetic:{label:`Synthetic cochlea`,cls:`sp-synthetic`},invitro:{label:`In vitro`,cls:`sp-invit |
| PASS | R7 | evidence bundle | Insertion force group includes impulse and work | nsertion`,label:`Insertion force`,test:/insertion\|force variation\|impulse\|work of/i,shape:`cross`},{key:`other`,label:`Ot |
| PASS | R21 | logo-options | Current plus five proposals | ption="Now"><div class="opt-head"><span class="letter">Now</span><div><h2>Current</h2><p>The logo on the site today: an Arial Black wordmark with a long dark wave and a short light swoosh.</p></div></div><div class="mock-nav" aria-hidden="true"><img class="logo-40" src="/logo.svg?v=2" alt=""><span class="mock-links"><span>Techno ... |

PASS 79, FAIL 0

### Staging checks (https://staging.zwicoat.com)

| Status | R | Page | Item | Proof |
|---|---|---|---|---|
| PASS | R1 | evidence | Section 1 order: interactive W04, histology photo, W27 | positions data-chart="fibrosis"@13767, histology-scar-01\.jpg@15792, /figures/W27_capsule_thickness_mice\.png@16847 |
| PASS | R1 | evidence | Interactive W04 frame with PNG fallback | <div class="ev-body"><figure class="ichart"><div class="ichart-mount" data-chart="fibrosis" data-fallback-src="/figures/W04_fibrosis_by_study.png" data-fallback-alt="Horizontal bar chart of 9 measurements of scar cap |
| PASS | R1 | evidence | Histology caption | c"></div></div><figcaption class="photo-cap"><p class="photo-caption">Tissue section after one year in a mouse: a thick capsule on uncoated silicone, a thin quiet interface on coated silicone. Adapted from Horne et al., Acta Biomaterialia 2023.</p><p class="photo-credit label">Adapted from Horne et al., Acta Biom |
| PASS | R10 | home | Hero holds the interactive W04 (compact) | class="btn-outline" href="/partner#form">Send us parts</a></div></div><div class="hero-figure"><figure class="ichart compact"><div class="ichart-mount" data-chart="fibrosis" data-fallback-src="/figures/W04_fibrosis_by_study.png" data-fallback- |
| PASS | R10 | home | Hero noscript PNG fallback | ut 85 percent." data-fallback-width="1000" data-fallback-height="572"><noscript><img class="ch-fallback-img" src="/figures/W04_fibrosis_by_study.png" alt="Horizontal bar chart of 9 measurements of scar capsule or fibros |
| PASS | R10 | home | Two-column hero layout kept | er(`change`,()=>s(!1))}</script><main id="main"><section class="hero"><div class="container hero-grid"><div class="hero-text"><p class="label">Zwitterionic hydrogel coating for medical devices</p> |
| PASS | R2/R20 | home | 12 displayed source lines, none with a disclaimer | 12 lines checked |
| PASS | R2/R20 | evidence | 25 displayed source lines, none with a disclaimer | 25 lines checked |
| PASS | R2/R20 | durability | 16 displayed source lines, none with a disclaimer | 16 lines checked |
| PASS | R2/R20 | neural | 15 displayed source lines, none with a disclaimer | 15 lines checked |
| PASS | R2/R20 | tissue-expanders | 12 displayed source lines, none with a disclaimer | 12 lines checked |
| PASS | R2/R20 | logo-options | 0 displayed source lines, none with a disclaimer | 0 lines checked |
| PASS | R2 | evidence | W05 short source (citation plus figures) | hen select a bar to see its values.</p><p class="ichart-source label">Source: Leigh et al. 2017, Biomacromolecules, Figs 4, 6E, 7E and 8E; Leigh et al. 2019, Langmuir, Figs 7D and 10D; Jensen et al. 2021, ACS |
| PASS | R2 | neural | W25 short source on an application page |  at implantation and at four weeks.</p><p class="figure-source label">Source: Ben-Shlomo et al. 2026, Hearing Research, Figs 3B to 3D</p></figcaption></figure></div><div class="prose"> <p><strong>Less inflam |
| PASS | R3 | evidence | Section 3 order: W28, cochlear viewer, ETT viewer, W07 | positions /figures/W28_durability_peel\.png@22560, data-chart="traces-w37"@23401, data-chart="traces-w38"@25562, /figures/W07_insertion_force\.png@27858 |
| PASS | R4 | evidence | Viewer captions say uncoated left, coated right |  of insertion (99 versus 291 mN·mm), measured on the same insertions. Uncoated insertions are on the left and coated on the right, on the same scales. Each line is one insertion; select a line to see its peak force and w |
| PASS | R5 | evidence | W07 caption names three studies |  arrays needed about half the peak insertion force of uncoated arrays in three studies: 42 percent less in human cadaveric cochleae (Bennion 2021), about 50 percent less in human cadaveric cochleae (Peel 2024) and 64 percent less in a synthetic cochlea (NIH SBIR Phase I dataset).</p><p class="figure-source label">Source: |
| PASS | R5 | neural | Neural page keeps W37 static | H SBIR Phase I dataset, Zenodo, doi:10.5281/zenodo.10459478</span></p><img class="figure-img" src="/figures/W37_ci_insertion_synthetic.png" alt="Three panels for a cochlear implant electrode array inserted by  |
| PASS | R6 | evidence | Interactive W06 with PNG fallback | <div class="ev-body"><figure class="ichart"><div class="ichart-mount" data-chart="durability" data-fallback-src="/figures/W06_durability_timeline.png" data-fallback-alt="Timeline of in-vivo checkpoints from two weeks to  |
| PASS | R6 | evidence | No static W06 image | absent: <img class="figure-img" src="/figures/W06_durability_timeline |
| PASS | R6 | durability | Interactive W06 with PNG fallback | ="claim-figure"><div><figure class="ichart"><div class="ichart-mount" data-chart="durability" data-fallback-src="/figures/W06_durability_timeline.png" data-fallback-alt="Timeline of in-vivo checkpoints from two weeks to  |
| PASS | R6 | durability | No static W06 image | absent: <img class="figure-img" src="/figures/W06_durability_timeline |
| PASS | R8 | evidence | No stat tiles on the evidence page | absent: class="tiles|tile-value |
| PASS | R9 | neural | Capsule panels are the page lead (before the spec strip) |  working implants, and a surface the tissue leaves alone.</p></header><div class="lead-media"><div class="fig"><figure class="cp" data-capsule-panels><div class="cp-box"><p class="fig-tag" aria-hidden="true"><span class |
| PASS | R9 | neural | Columns Silicone and Platinum | ia-labelledby="cp-silicone"><div class="cp-head"><h3 class="cp-title" id="cp-silicone">Silicone</h3><div class="cp-toggle" role="group" aria-label="Silicone: show uncoated, coated or both" hidden><button type="button" data-mode-btn="uncoated" aria-pressed="false">Uncoated</button><button type="button" data-mode-btn="coated" aria ... |
| PASS | R9 | neural | Toggle buttons Uncoated / Coated / Compare (aria-pressed) | e="group" aria-label="Silicone: show uncoated, coated or both" hidden><button type="button" data-mode-btn="uncoated" aria-pressed="false">Uncoated</button><button type="button" data-mode-btn="coated" aria-pressed="false">Coated</button><button type="button" data-mode-btn="compare" aria-pressed="true">Compare</button></div></div> ... |
| PASS | R9 | neural | All four images in the markup (compare state without JS) | lass="cp-stack"><div class="cp-img cp-uncoated"><img src="/images/lab/capsule-pdms-uncoated.jpg" alt="Tissue section next to uncoated silicone (PDMS) on an implanted array, explanted from a mouse. A thick blue-stained band of fibrous capsule runs along the silicone surface, marked by red lines across its width." width="1178" hei ... |
| PASS | R9 | neural | Caption with 47 to 18 micrometers | , but a thin, quiet interface on coated silicone and coated platinum. Mean capsule thickness on the device fell about 60 percent, 47 to 18 micrometers, with coating.</p><p class="cp-credit label">Adapted from Horne et al., Acta Biomate |
| PASS | R9 | neural | Credit | nt, 47 to 18 micrometers, with coating.</p><p class="cp-credit label">Adapted from Horne et al., Acta Biomaterialia 2023</p></figcaption></figure><script type="module">document.querySelectorAll( |
| PASS | R9 | neural | Sheep histology moved lower (after W26) | search, Figs 6E to 6G</span></p><img class="figure-img" src="/figures/W26_sheep_histology.png" alt="Three small charts comparing uncoated and coated arrays at the round window of the sheep cochlea: cell nuclei density, macrophage density and fibrosis. The pooled coated bar is lower in all three. A line joins each of the three sh ... |
| PASS | R11 | home | Applications heading | class="section-head"><p class="label">Applications</p><h2 id="apps-h">Nine places to start. ZwiCoat bonds to the elastomers and plastics most devices are made of.</h2><p class="apps-intro">Each page starts with the clinical problem, |
| PASS | R11 | home | Intro sentence | mers and plastics most devices are made of.</h2><p class="apps-intro">Each page starts with the clinical problem, then shows what coated devices achieved in published studies.</p></div><ul class="grid" role="list"><li><a class="card" href="/appl |
| PASS | R11 | home | No "device families" | absent: device families |
| PASS | R12 | home | Tiles below the "Ten years of published work" section | positions id="timeline-h"@24496, id="numbers-h"@26133 |
| PASS | R12 | home | ~60% tile | ro and in four animal and cadaver models.</span></li><li class="tile"><span class="tile-value">~60%</span><span class="tile-label label">thinner fibrotic capsule around coated implants</span><span class="tile-takeaway">One year in mice, on human cochlear implant arrays, over platinum and silicone alike (Horne 2023).</span></li>< ... |
| PASS | R12 | home | ~50% tile | n and Mexico: the largest device markets.</span></li><li class="tile"><span class="tile-value">~50%</span><span class="tile-label label">less insertion force with coated cochlear implants</span><span class="tile-takeaway">Three studies: human cadaver cochleae twice and a synthetic cochlea (Bennion 2021, Peel 2024, SBIR dataset). ... |
| PASS | R12 | home | No dissertations tile | absent: tile-label label">PhD dissertations |
| PASS | R12 | home | No patents-pending tile | absent: patent applications pending |
| PASS | R12 | home | No "dissertations" anywhere in the tiles section | absent: dissertation |
| PASS | R13 | durability | Impact block: clip left, photos right | </p></div></div><div class="claim-figure"><div><figure class="impact"><div class="impact-grid"><div class="impact-video"><figure class="vl" style="--ratio: 0.6667;"><div class="vl-box"><p class="fig-tag" aria-hidden="true"><span class="fig-tag-id">VIDEO</span><span class="fig-tag-src">ZwiCoat, 2026</span></p><div class="vl-frame ... |
| PASS | R13 | durability | Photo captions | c"></div></div><figcaption class="photo-cap"><p class="photo-caption">Before impact</p><p class="photo-credit label">ZwiCoat, 2026</p></figcaption></figure><figure class="photo" style="--ratio: 2.0000;"><div class="photo-box"><p class="fig-tag" aria-hidden="true"><span class="fig-tag-id">PHOTO</span><span class="fig-tag-src">Zwi ... |
| PASS | R13 | durability | Lead-in and 45 J caption | h2 class="claim-title">It takes a hit.</h2><div class="claim-body"><p>A 45 J pendulum strike on a coated tissue expander.</p><p>The photographs show the expander before and after the strike.  |
| PASS | R13 | durability | Source line | strike on a coated tissue expander.</p><p class="impact-source label">Source: ZwiCoat internal test, 2026</p></figcaption></figure></div></div></section><section class="claim reve |
| PASS | R14 | durability | Clip aspect 540/810 and poster | <div class="impact-grid"><div class="impact-video"><figure class="vl" style="--ratio: 0.6667;"><div class="vl-box"><p class="fig-tag" aria-hidden="true"><span class="fig-tag-id">VIDEO</span><span class="fig-tag-src">ZwiCoat, 2026</span></p><div class="vl-frame" style="aspect-ratio: 540/810;"><video data-loop autoplay muted loop  ... |
| PASS | R15 | durability | Side panel title | t (Leigh 2019).</p><aside class="bond-panel" aria-labelledby="bond-h"><h3 id="bond-h" class="bond-title">Bond strength on silicone today</h3><ul class="bond-list" role="list"><li><span class="bond-val">~105 kPa< |
| PASS | R15 | durability | Panel values | oday</h3><ul class="bond-list" role="list"><li><span class="bond-val">~105 kPa</span> <span class="bond-lab">median as prepared (36 groups, 123 tests, 2025 to 2026)</span></li><li><span class="bond-val">~94 kPa</span> <span class="bond-lab">median after soaking in PBS (26 groups, 2025)</span></li><li><span class="bond-val bond-t ... |
| PASS | R15 | durability | Panel sentence and source | 2019 published film (Leigh 2019)</span></li></ul><p class="bond-text">The bond is measured by pulling the film off silicone; today's groups sit above the 2019 published values, and the gel still tears first.</p><p class="bond-src label">Source: ZwiCoat lap-shear database, 2025 to 2026; Leigh 2019, Fig 6</p></aside></div></div><d ... |
| PASS | R16 | tissue-expanders | W17 capped at 640 px | ants and expanders, and textured use fell.</p> </div><div class="fig"><figure class="figure" style="max-width: min(100%, 640px);" data-design-width="618"><div class="fig-frame"><p class="fig-tag" aria-hidden="true"><span class="fig-tag-id">FIG W17</span><span class="fig-tag-src">Matros et al. 2021, Plastic and Reconstructi |
| PASS | R17 | tissue-expanders | Slide 2 pair after the 300 percent sentence, slide 3 pair beneath | positions inflated to 300 percent of its rated volume kept the coating@17100, expander-deflated\.jpg@17500, expander-inflated\.jpg@17944, expander-inflation-100pct\.jpg@18656, expander-inflation-300pct\.jpg@19166 |
| PASS | R17 | tissue-expanders | Slide 3 caption | re></div></div><figcaption class="ppair-cap"><p class="ppair-caption">A coated 100 cc expander inflated to 300 cc: no tearing. ZwiCoat internal test, 2026.</p><p class="ppair-credit label">ZwiCoat, 2026</p></figcaption></figu |
| PASS | R17 | tissue-expanders | Small originals capped at 1.5x (546 and 670 px) | ><div class="pair-item"><figure class="photo" style="--ratio: 0.9529; --max-w: 546px;"><div class="photo-box"><div class="photo-frame fit-contain" style="aspect-ratio: 364/382;"><img src="/images/lab/expander-deflated.jpg" alt="A deflated coated tissue expander lying folded in a glass bowl of blue liquid." loading="lazy" decodin ... |
| PASS | R18 | tissue-expanders | "Takes a hit" block before "How to start" | positions id="takes-a-hit">Takes a hit</h2>@21297, pendulum-loop@22094, expander-impact-after\.jpg@23911, id="how-to-start"@24536 |
| PASS | R18 | tissue-expanders | 45 J cited | ="prose"> <h2 id="takes-a-hit">Takes a hit</h2> <p>Expanders get hit. A 45 J pendulum strike on a coated expander left no visible damage to the coating (ZwiCoat internal test, 2026). <a href="/durability">See the durability record.</a></p> </div><div  |
| PASS | R21 | logo-options | Current plus five proposals | ption="Now"><div class="opt-head"><span class="letter">Now</span><div><h2>Current</h2><p>The logo on the site today: an Arial Black wordmark with a long dark wave and a short light swoosh.</p></div></div><div class="mock-nav" aria-hidden="true"><img class="logo-40" src="/logo.svg?v=2" alt=""><span class="mock-links"><span>Techno ... |

PASS 54, FAIL 0

### Open points from round five

- Chart images still carry their own subtitle notes, for example W07 "~ = approximate, read from the published figure", W04 and W31. They are PNG text, rebuilt by `figures/build_figures.py`; the HTML source lines are clean. If Kam wants them gone from the images too, the figures worker should drop those subtitles and rebuild.
- The home hero chart is about 900 px tall at 1280 px (nine bars with filters, legend and caption). The two-column layout is kept; the text column is centered beside it.
- R14: the clip and poster are the 540 x 810 files placed by the lead; the crop itself was not part of this pass.
- The capsule panel alt text says "explanted from a mouse" on an implanted array; the panel caption is Kam's wording. The deck slide does not say whether Fig 4 is the one-year cohort, so the alt text does not.
- The 1.5 MB PNG originals of the slide-3 photos are still in `public/images/lab` (unused); delete them if shipping weight matters.

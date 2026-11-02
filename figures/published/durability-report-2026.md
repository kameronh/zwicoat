# Durability report to an implant maker, 30 October 2026: what can go on the public Durability page

Extraction worker output, 2026-11-02. Read-only on every source. Nothing here is site copy until Kam approves it. The implant maker is not named anywhere in this file (it is "the customer" or "the implant maker").

## 1. Header

- **What the report is.** A 15-page plan titled "Coating durability: action plan and where ZwiCoat stands today", prepared by ZwiCoat Materials Innovations for a cochlear implant manufacturer after a durability workshop. It records who runs which test (section 1), the handling tests ZwiCoat will run first (section 2), a benchtop plan to judge patient risk if the coating is torn (section 3), what FDA is likely to expect (section 4), a Pass/Good scorecard in eight categories with a red/amber/green/grey status for where ZwiCoat stands (section 5, 5.1 to 5.8), and an appendix explaining how each threshold was set plus 43 references. Most of its ten figures are re-plots or photos from ZwiCoat's 2025 Phase II grant application, the 2023 Peel dissertation (published as Peel 2024), the Bennion 2021 paper, the Kyle Ruby 2025 sterilization study and the 2026 pendulum tests.
- **Date.** 30 October 2026, marked "Draft for discussion" (PDF created 29 October 2026).
- **Audience.** One customer's materials, regulatory and surgical teams. It is a working document with customer requirements, proposed owners, a target date and open failures in it.
- **One-sentence takeaway.** The coating bends, stretches, takes ten insertions, survives ethylene oxide and takes a 44 to 54 J padded pendulum hit without visible damage, its bond to silicone is about 80 kPa with the gel tearing before the bond lets go, and the open risks are sharp-tool contact, drying while bent, aging and shelf life, none of which has been measured to a standard yet.
- **Sources read.** The 15-page PDF (all pages and all ten embedded images), both pptx files (every slide and note), `Durability_criteria_research_notes.md`, the 4-page EA22 coating summary PDF, the customer requirements docx, `_build/BUILD_REPORT.md`, `_build/research/zwicoat_data_digest.md` (the best map of where each number came from), the three `replot_*.py` scripts, the Kyle Ruby sterilization summary csv and the Adreann Peel extracted-data csvs, plus `figures/data/W02_lapshear_public.json` and the published-paper notes in this folder.

## 2. Every quantitative result in the report

"Raw numbers" = where the underlying values live. `ZD` = `C:\Users\Kameron\Zwicoat Dropbox\ZwiCoat Data`. `MD` = the October 2026 workshop's `material durability\_build` folder under `G:\My Drive\9 Zwitterion\Claude Code projects and misc files\misc claude code (Zwitterion)\26.10.26 (workshop folder)` (name abbreviated). Call = sensitivity screen in section 3.

| ID | Test | Conditions | Metric | Result | n | Figure or slide | Raw numbers | Call |
|---|---|---|---|---|---|---|---|---|
| R1 | Impedance after conditioning (customer item 1.1) | Four molded implants, coated vs uncoated, saline, EA22 summary Jan 2026 | Impedance, kOhm | Report text: coated "0% to 30% lower". The slide-4 plots show coated mostly 2 to 5 (one array to about 7) vs uncoated about 4 to 12, which is nearer 40 to 60% lower. One coated array is above the customer's 5 kOhm limit | 4 implants, 2 reads each | Report table 1.2; EA22 pdf slide 4 | EA22 pdf (plots only; no csv found) | PRIVATE |
| R2 | Electrochemical stability, platinum dissolution (items 1.2, 1.3) | n/a | n/a | Not tested | 0 | Table 1.2 | n/a | PRIVATE (customer requirement) |
| R3 | Insertion force, human cadaver cochleae | 6 fresh-frozen temporal bones, 3 insertions each, 2 lateral-wall array types, coated vs uncoated, 0.5 mm/s | Peak insertion force | About 37 vs 64 mN, about 40% less (exact in Bennion 2021: 37.0 +/- 11.3 vs 64.2 +/- 17.9 mN, p = 0.001) | 9 vs 9 insertions | Section 5.4, Fig 5; table 1.2 item 2.2 | `figures/published/2021-bennion-otolneurotol.md`; MD `assets\replot_fig4_insertion_metrics.png` | PUBLIC (published; already W07) |
| R4 | Insertion work, synthetic cochlea | Robotic insertion, EtO-sterilized dip-coated arrays | Work of insertion | 68% less (68.4%, p < 0.001) | 5 trials per group | 5.4; table 1.2 | Phase II grant 2025 Fig 6 only (not found as csv); digest sec 4 | BORDERLINE |
| R5 | Insertion work, cadaver | Same as R3 | Work of insertion | About 285 vs 216 microjoule (24% less; p = 0.05 in paper, 0.19 in re-analysis); the report leaves it out | 9 vs 9 | Digest only | Bennion 2021 | PRIVATE (weak, borderline stat) |
| R6 | Repeated insertion | Arrays, 10 insertions, dye coverage | Coverage | Full coverage, qualitative | not stated | 5.4; Fig 2a | Grant Fig 5a; `MD\assets\grant_fig5_embedded.png` (483 x 807 px) | BORDERLINE |
| R7 | Friction vs steel, ceramic, tissue | Coated vs bare silicone discs, 1 N | Friction | Over 90% lower (Bennion 2021: about 0.06 relative) | 4 | 5.4 text | `2021-bennion-otolneurotol.md` Fig 1 | PUBLIC |
| R8 | Sliding wear, 2,500 passes | Flat silicone discs, 1 N sapphire probe, PBS, about 17 h | Friction relative to bare silicone, first 100 vs last 100 passes | Equal for every crosslinked coating, about 0.07 at 2 to 13% crosslinker; 0.10 at 31%; uncrosslinked film not protective (0.97 then 0.70) | at least 4 | 5.4, Fig 6 | `ZD\Adreann Peel\22.01_Long_Term_Wear_2500_Cycles\extracted-data\Fig6.9_COF_first_vs_last_100cycles_wide.csv` (pixel readings of the printed figure); replot script `MD\replot_wear.py` | PUBLIC (Peel 2024 Fig 9) |
| R9 | Tool contact (forceps, tweezers) | One photo set, informal, undated | Visible damage | None seen. Caption says silicone strip, adjacent text says PEEK strip. No grip force, tool, wet or dry, or n recorded | 1 photo set | 5.1, Fig 1 (A1 to A3) | `MD\fig_crops\tweezers.png`; digest sec 1 | PRIVATE (not a test) |
| R10 | Wet bending around rods | Hydrated coating on 35 x 75 x 1 mm strips, rods 32 down to 2 mm | Cracking | None at every crosslinker level except 100% | at least 3 | 5.2 | Peel 2024 text; `ZD\Adreann Peel\21.11_Mandrel_Bend_Flexural_Durability\extracted-data\Fig6.7_mandrel_bend_time_to_failure.csv` | PUBLIC |
| R11 | Array curling | Arrays curled to a full circle 50 times, then 10 insertions | Dye coverage | 100% coverage, qualitative | not stated | 5.2, Fig 2a | Grant Fig 5a | BORDERLINE |
| R12 | Tissue expander inflation | One 100 cc smooth expander, 50% steps, previously cycled twice | Coating condition | Report: "3.5 times nominal fill with the coating still attached". Source deck: no cracking recorded to 200 cc, fine crack-like lines visible at 350 cc, defects circled at 100 cc, second side stopped at 300 cc | 1 device, 1 run | 5.2; scorecard row 2 | `MD\sources\Coating_inflation_limit_test.pdf`; digest sec 2 | BORDERLINE (use only "200 percent", which is already on the site) |
| R13 | Stretch to failure, thick gels | 1 mm gel on flat silicone, strips | Strain at failure | 22 to 49%; softer and thinner did best (about 42% vs 24%; 49% vs 22 to 23%) | 6 per group | 5.2 | Kyle Ruby 26.06.22 and 26.07.03 workups (`ZD\Kyle Ruby\26.07.03_Kyle_XL_Concentration_Stretch\workup\xl_vs_stretch.png`) | PRIVATE (crosslinker and recipe dependent) |
| R14 | Drying while bent, flat coatings | Bent every 5 min on a 5 mm rod while drying | Minutes to first crack | About 75 (type CBMA, 5% crosslinker), 47.5 to 50 (type SBMA, 5%), 7 (SBMA 67%), 0 at 100%. Values by crosslinker in Peel 2024 Fig 7 | at least 3 | 5.3, Fig 4A | `Fig6.7_mandrel_bend_time_to_failure.csv`, `2024-peel-acsabm.md` | PUBLIC |
| R15 | Drying while bent, breathing tubes | Coated tubes bent every 10 min in air (water or PBS soaked) | Minutes to first crack | 190, 140, 120, 130, 190, 120 min (mean about 148); none cracked at 30 min. Process predates current dip coating | 6 tubes | 5.3, Fig 3e | Grant Fig 7d,e; `MD\assets\grant_fig7_d_e.png` (read the bar labels) | BORDERLINE |
| R16 | Dry-out and re-wet, slipperiness | Discs dried 24 h, re-wet 24 h in saline | Friction vs never-dried | Same as pristine at 25% crosslinker or below (about 0.03); flaked at 50% or more (0.18 to 0.23, uncoated 0.179) | at least 4 | 5.3, Fig 4B | `ZD\Adreann Peel\21.12_Desiccation_Rehydration_COF\extracted-data\Fig6.8_COF_swollen_vs_rehydrated_wide.csv` | PUBLIC (Peel 2024 Fig 8); the "today's recipe is in the recovering range" sentence is PRIVATE |
| R17 | Bond after dry-out and re-wet | Lap shear, two datasets, formulation not recorded | Bond strength | About 91 vs 96 to 106 kPa (no loss); about 85 vs 55 to 60 kPa (about 30% loss) | 3 each | 5.3 text | Digest sec 3 (Emma Tebben 25.04.16) | PRIVATE (a loss, unresolved) |
| R18 | Dry, bag one month, re-wet | Arrays, tubes, silicone | Dye coverage | 100%, qualitative | not stated | 5.3; Fig 2d | Grant Fig 5d | BORDERLINE |
| R19 | Packaged-drop and 1 m drop | None run | n/a | Not tested | 0 | 5.5 | n/a | PRIVATE |
| R20 | Pendulum impact, 125 cc expander | Steel slug, silicone-padded, rigid backboard | Visible damage | About 44 to 54 J, none, front or back | 1 device | 5.5, Fig 7 | `MD\assets\pendulum_before_after_impact.png`; lab-media in `assets-staging` | PUBLIC (already on the site as the pendulum video) |
| R21 | Pendulum impact, 200 cc expander | Padded; backboard moved so some energy lost | Visible damage | About 59 to 70 J, one small scrape, rest intact | 1 device | 5.5 | digest sec 5 | BORDERLINE (shows damage; site already carries it as a caption note per `CANDIDATES.md`) |
| R22 | Glancing hits | Two off-center hits on the 125 cc, excluded | Damage | One scraped the coating | 2 | 5.5 | digest sec 5 | PRIVATE |
| R23 | Dropped implant energy | Estimate, masses not recorded | Energy | "Well under 1 J" | none | 5.5 | not in any data | PRIVATE (an estimate, Kam to confirm) |
| R24 | Lap-shear bond strength on implant silicone | Wet coating between silicone and functionalized glass, standard recipe, PBS-soaked | Group mean | Median about 79 to 80 kPa, middle half 45 to 91, 14 groups; gel tore first "in every group where failure was recorded" (digest: 11 of 11) | usually 3 to 5 per group | 5.6, Fig 8; scorecard row 6 | `MD\assets\L1_substrate_standard_recipe.png`; `figures/data/W02_lapshear_public.json` | PUBLIC (W02 class); see flag 1 |
| R25 | Lap-shear by other materials | Same | Median of group means | PVC about 237 (24 groups), Sylgard about 97 (16), Bentec about 84 (12), sanded Sylgard about 84 (42), implant silicone about 79 (14) | per figure | Fig 8 | W02 json | PUBLIC (W02 class) |
| R26 | Early coating bond vs one-year mouse study | Iowa bench lap shear, 2020, soaked in PBS; same coating family as the one-year mouse implant (Horne 2023) | Bond and film state | Bench bond about 25 to 35 kPa; film intact and spanning platinum contacts at one year; "today's bond is two to three times stronger" | not stated | 5.6 text; scorecard row 6 | Peel 2023 dissertation chapter 4; W02 json (2020 silicone film on glass: 98 groups, median 31 kPa) | BORDERLINE |
| R27 | Bond strength after 60 days soak | Lap shear, flat | Bond | Flat 1 h to 1 month (about 65 to 95 kPa), about 47 kPa at 2 months, water controls fell too, cause unexplained | not stated | digest sec 6; scorecard "unexplained drop" | FINDINGS in data project | PRIVATE (a drop) |
| R28 | Ethylene oxide, visual | Coated implant silicone, probe cover, breathing tube; arrays 16 h at 50 C | Visible coating loss | None in 38 before and after image pairs; arrays full dye coverage | 38 pairs | 5.7 text | Kyle Ruby 25.04 E-report; grant Fig 5c | PUBLIC to BORDERLINE (qualitative; dry EtO already on the site in W11) |
| R29 | Ethylene oxide, bond | Lap shear, after EtO | Bond strength | About 55 kPa (33 to 78), vs about 155 for a dried-and-re-wet set made by another person; not like-for-like | 3 | 5.7 text | digest sec 7 | PRIVATE (confounded; formulation recorded as W12 C0.025) |
| R30 | Gamma and e-beam plus shipping, implant silicone, dry | Shipped to a steriliser and back (about 14 days), 14 days in saline | Lap shear, kPa | Shipped-only 93.6 +/- 5.8; gamma control 85.6 +/- 18.6; gamma 73.6 +/- 72.2; e-beam control 84.1 +/- 5.3; e-beam 90.7 +/- 8.4 | 2 to 3 per group | 5.7, Fig 9 | `ZD\Kyle Ruby\25.09.01_Kyle_Sterilization_LapShear\workup\sterilization_lapshear_summary.csv`; `MD\replot_sterilization.py` | BORDERLINE (n of 2 to 3 and an SD of 72 are too thin to chart) |
| R31 | Wet packaging | Same, wet | Lap shear | Roughly halved on every material (implant silicone 30 to 45 vs 85 to 94 dry) | 1 to 2 | 5.7, Fig 9 | same csv | PRIVATE (a failure) |
| R32 | Gamma and e-beam, shipped, sanded silicone, dry | Same | Lap shear, kPa | Shipped-only 61.0 +/- 8.6; gamma 49.8 +/- 13.3; e-beam 60.5 +/- 16.1. The batch controls (gamma 71.3 +/- 10.6, n = 4; e-beam 60.1 +/- 13.3, n = 5) are not in the report figure | 5 each | 5.7, 5.8, Fig 10 | same csv; `MD\replot_shipping.py` | PUBLIC (this is the right panel of W11) |
| R33 | Wet gamma and wet e-beam on probe covers | Polyester covers, 336 h | Bond, coating | Wet gamma about 0.5 kPa (n = 1); wet e-beam left no testable samples | 0 to 1 | digest sec 7 | same csv | PRIVATE (the failed cycle) |
| R34 | Courier shipping, dry | Round trip to a steriliser, about 2 weeks | Bond | No loss, with or without irradiation | 5 | 5.8, Fig 10 | same csv | PUBLIC (same as R32) |
| R35 | Heat, cold, shelf life | Not run | n/a | Not tested. The accelerated-aging figure (82 C, mass loss about 17%, 1.3% per equivalent year) was pulled from the report by Kam | 0 | 5.8 | `ZD\Aryaman Verma\24.12_...\workup\aa82_mass_vs_weeks.png` | PRIVATE (rule 3: aging mass-loss rates) |
| R36 | Peel 2024 data in the report (Figs 4, 6) | Published | See R14, R16, R8 | See above | | Figs 4 and 6 | `2024-peel-acsabm.md` | PUBLIC |
| R37 | Handling-test plan | Three planned tests, target 30 November 2026 | n/a | Plan only | 0 | Section 2 | n/a | PRIVATE (timeline, customer) |
| R38 | Benchtop risk tests | Shed-and-count (10, 25, 50 micrometre bins), tear growth over 2 weeks, 4-week flake soak | n/a | Plan only | 0 | Section 3 | n/a | PRIVATE |
| R39 | Regulatory comparison | 10-row table of two cleared competitor products and the FDA guidewire guidance | Test headings | Public regulatory facts; competitor products named | n/a | Section 4 | `MD\_build\research\regulatory_precedents.md` | PRIVATE (names competitors, includes regulatory strategy and a PMA-supplement judgement) |
| R40 | Pass and Good thresholds | Proposals, set by a language model per the report's own note | Values, for example 30% strain, 20 grips, 129 days at 55 C | Proposals, not results | n/a | Section 5, Appendix A | n/a | PRIVATE (customer-specific and unvalidated) |
| R41 | Literature numbers in Appendix A | Insertion forces 0.05 to 0.10 N, tip force about 3 mN, surface strain 6 to 28%, label temperatures | Context | Not ZwiCoat results | n/a | Appendix A | cited papers | PRIVATE (not ours; do not restate) |

## 3. Sensitivity screen

Rule applied (CLAUDE.md rule 3, strictly): published first; internal data only if the company already broadcasts it in the MedTech decks or it is on the allowed list (sterilization compatibility W11, substrate evidence matrix W10, lap-shear database by substrate without formulation fields, archive counts with a takeaway, lab photographs and videos). Never: formulation ratios, W/C/I values, crosslinker or initiator doses of ZwiCoat recipes, accelerated-aging mass-loss rates, process yields and scores, anything from manuscripts in preparation.

| Call | Results | Reason |
|---|---|---|
| PUBLIC | R3, R7, R8, R10, R14, R16 (the figure, not the recipe sentence), R20, R24, R25, R32, R34, R36 | Published in a paper (R3, R7, R8, R10, R14, R16; Peel 2024 is CC-BY 4.0) or already in the allowed internal classes (lap-shear database, sterilization W11, pendulum). None names a recipe, customer or failure. |
| BORDERLINE (needs Kam) | R4, R6, R11, R12, R15, R18, R21, R26, R28, R30 | Come from the 2025 Phase II grant (not public), have no recorded n, or are n = 1 to 3, or show a single scrape or crack. R12 only works as "200 percent". R26 pairs a Horne 2023 result with an Iowa bench value that Horne does not report; the link is ZwiCoat's inference. R30 has an SD larger than the mean. |
| PRIVATE | R1, R2, R5, R9, R13, R17, R19, R22, R23, R27, R29, R31, R33, R35, R37 to R41 | Customer requirements and owners, impedance on the customer's product, timelines, proposed test plans, regulatory strategy and competitor names, unresolved failures (bond loss after drying, wet packaging halving bond, wet e-beam, 2-month bond drop), crosslinker-dependent stretch results, aging mass loss, and unvalidated thresholds. |

### Flags for Kam (things in or around the report that do not match the data)

1. **"The gel tore in every group" is not what the site database says.** The report (5.6) and the digest say 11 of 11 groups with a recorded failure on implant silicone. `W02_lapshear_public.json` has 22 implant-silicone groups, 14 with a recorded mode: 12 gel-first, 2 bond-first (median 34 kPa for those two). On silicone (PDMS) it is 75 of 90 (83%). Use the W02 numbers on the site, not "every".
2. **The 3.5 times tissue expander line overstates.** Source deck: fine crack-like lines at 350 cc, a written no-cracking verdict only to 200 cc, one device. The site already says 200 percent. Do not add 3.5.
3. **"Hundreds of kPa" is true for PVC only.** Silicone is gel-limited near 80 kPa (report A.6 says the lap-shear value is "capped by the gel's own strength rather than by the bond"). See highlight 3 for the honest then-versus-now.
4. **The current Durability page and technology page claim steam and UV pass.** The digest says no E-report or data file supports the steam or UV ticks, and "wet e-beam failed" was seen only on polyester probe covers (CI silicone n = 1 to 2 looked fine). Also the card title "Seven of eight cycles" is a tally and breaks the editorial rule. Check before launch.
5. **Gamma on sanded silicone looks 30% lower than its own batch control** (49.8 vs 71.3 kPa; both n = 4 to 5). The report compares to the shipped-only group (61.0) instead. That sits at the lab's own noise floor (about 30% at n = 5), so "within scatter" is defensible but should not be called "no change".
6. **Impedance sentence vs slide.** Report table says coated impedance is 0 to 30% lower. The EA22 plots show a larger gap (coated about 2 to 5 kOhm vs uncoated about 4 to 12), and one coated array is above 5 kOhm. Private anyway.
7. **Kam's pendulum slide says "around 75 J we saw ripping or flaking".** The Impact Testing deck tops out at 59 to 70 J with one small scrape. Not on the site.
8. **Tweezer photo (Fig 1).** Caption says silicone strip, text says PEEK strip, undated, no force or tool recorded. Do not publish as a test result.

## 4. Proposed site highlights

Voice: company, positive, plain, no em-dashes. Chart text is Arial, rebuilt by `figures/build_figures.py`. No monomer names or "benzophenone" in headlines or chart labels; where a published figure splits by chemistry use "Coating A" and "Coating B". All numbers marked "approximate" are read from printed figures or csv pixel extractions.

### Highlight 1. Friction stays low after 17 hours of rubbing (PUBLIC)

- **Headline.** "Still slippery after 2,500 passes."
- **Chart.** Grouped bars, one pair per coating stiffness. Y: friction relative to bare silicone (bare silicone = 1.0, dashed line). Series: "First 100 passes" (light) and "Last 100 of 2,500 passes" (dark). Recommended bars (approximate, pixel readings of Peel 2024 Fig 9, n at least 4, SEM, no significant difference first vs last):

  | Crosslinker in coating (percent) | First 100 | Last 100 |
  |---|---|---|
  | 2 to 5 | 0.068 | 0.068 |
  | 13 | 0.068 | 0.068 |
  | 31 | 0.103 | 0.103 |
  | 50 | 0.23 | 0.19 |
  | 67 | 0.255 | 0.255 |

  The 0 percent bar (0.97 then 0.70, "did not lubricate") and the 100 percent bar (0.254 then 0.335) are not ZwiCoat coatings. Leave them out, or Kam adds them for honesty. The axis label "Crosslinker in the coating (percent)" is the published one and gives no ZwiCoat recipe.
- **Caption.** "Coated silicone, rubbed under a 1 N load in saline for about 17 hours. Friction in the last 100 passes matched the first 100 and stayed at about 7 percent of bare silicone." The 7 percent is for the 2 to 13 percent bars.
- **Source.** Peel et al., ACS Appl Bio Mater 2024;7:3124-3135 (Fig 9).
- **Note.** Flat discs and older photografted films, not the current dip coating. The report says so; the caption need not, since the source is the paper.

### Highlight 2. It dries out and comes back (PUBLIC; one BORDERLINE add-on)

- **Headline.** "After a full dry-out and re-wet, it is as slippery as new."
- **Chart.** Two panels, shared style.
  - Panel A, "Time before the first crack while drying and bending (minutes)". Dots with SD, X = crosslinker percent, series Coating A and Coating B and a grey non-zwitterionic control. Approximate values (Peel 2024 Fig 7 / csv `Fig6.7`): Coating A 75 (SD 7.2) at 5 percent, 58 at 20, 25 at 67; Coating B 47.5 (SD 3.8) at 5, 37 at 20, 7 at 67; control 24, 12, 3.4. Text-exact: Coating A 75 min and B 50 min at 5 percent, bent every 5 minutes on a 5 mm rod. n at least 3.
  - Panel B, "Friction after drying 24 hours and re-wetting 24 hours". Series: never dried (open) vs dried and re-wet (filled), X = crosslinker percent 2 to 5, 13, 20, 31. Approximate values: never dried 0.026, 0.031, 0.033, 0.034; re-wet 0.026, 0.031, 0.033, 0.058. Reference line: bare silicone 0.179 (exact, from the caption). n at least 4. Keep the x range to 31 percent; the 50 and above points (0.18, 0.23) are the flaking stiff coatings, which Kam may choose to omit as "not our coating".
- **Caption.** "Coated silicone dried for 24 hours and re-wet for 24 hours returned to its original friction. Coatings dried while being bent every 5 minutes lasted 50 to 75 minutes before the first crack."
- **Source.** Peel et al., ACS Appl Bio Mater 2024 (Figs 7 and 8).
- **Optional add-on (BORDERLINE).** "Arrays dried, bagged for a month and re-wet kept 100 percent dye coverage." Qualitative, n not recorded, 2025 grant photo (R18). Needs n and a fresh photo before use. A second add-on, six coated breathing tubes bent every 10 minutes while drying in air first cracked at 120 to 190 minutes (190, 140, 120, 130, 190, 120; mean about 148), is the only array-adjacent time number in the report; the source is the non-public grant and the process predates the current dip coating, so I recommend leaving it off unless Kam approves the specific figure.

### Highlight 3. The gel tears before the bond lets go (PUBLIC from the W02 database; replaces or extends W31)

- **Headline.** "On silicone, the gel gives way before the bond does."
- **Chart.** Strip plot, one column per material, one dot per lap-shear group (group mean, kPa), a bar at the median, and under each column the count and the share of groups where the gel tore first. Data are in `figures/data/W02_lapshear_public.json` (no formulation fields; recompute in `build_figures.py`). Values:

  | Material | Groups | Median kPa | Middle half kPa | Highest | Gel tore first (of groups with a recorded mode) |
  |---|---|---|---|---|---|
  | Implant silicone | 22 | 74 | 41 to 90 | 353 (a 15 minute soak group) | 12 of 14 |
  | Silicone (PDMS) | 139 | 83 | 55 to 113 | 261 | 75 of 90 |
  | Polyurethane (probe cover) | 46 | 33 | 12 to 57 | 113 | 24 of 37 |
  | PVC | 64 | 249 | 82 to 369 | 710 | 26 of 36 |

  Leave out PEEK (3 groups), Parylene-C (8 groups, 1 recorded mode) and silicone film on glass (early tests designed to fail at the interface). Kam decides whether polyurethane and PVC stay; the take-away works on silicone alone.
- **Caption.** "Bond strength of the coating by lap shear, one dot per test group. On silicone, the gel tore before the bond let go in most groups. Medians are about 80 kPa on silicone and over 200 kPa on PVC."
- **Source.** ZwiCoat internal study, 2026 (lap-shear database, 2017 to 2026).
- **Then versus now (requested; the numbers do not support a big claim).**
  - Published then: Leigh 2019 Fig 6, silicone, as prepared, at the highest grafting-agent levels: about 71 kPa (Coating B) and about 100 kPa (Coating A); about 35 and 62 kPa after 48 h swollen (approximate, converted from N/m2 x 10^4; already plotted as W31). The 2017 groups in the lap-shear database behind that paper: 36 groups, median 40 kPa, 14 gel-first groups at median 59 kPa (range 34 to 102).
  - Now: 2024 silicone-film-on-glass groups, 14 of 14 gel-first, median 97, range 63 to 138; silicone (PDMS) 2025 to 2026, 86 groups, median 91 to 99, middle half 57 to 129, highest 237 to 261; implant silicone median 74 (2025) and 98 (2026, n = 3 groups).
  - Honest summary: typical bond on silicone is about 1.5 times the published plateau (97 vs 59 kPa like-for-like) and about 2.4 times the early all-group median (97 vs 40), not ten times. It is gel-limited, which is why "the gel tears first" is the claim to make, not "stronger". Only PVC reaches hundreds of kPa. Within-group scatter is about 25 percent, so differences under about 30 percent are not real.
  - I recommend not building a "hundreds of kPa vs tens of kPa" chart for silicone.
- **Variant 3b (BORDERLINE): "A bond about a third as strong lasted a year in the body."** Two bars: early coating, bench bond about 25 to 35 kPa (2020), film intact at one year in mice (Horne 2023, already on the page as W06); current coating on implant silicone about 80 kPa (median 74, middle half 41 to 90). Caption: "An early coating with a bond about a third as strong as today's stayed intact and bridged platinum contacts for a year implanted in mice." Flags: Horne 2023 reports no lap-shear value, the 25 to 35 kPa is from Iowa bench data (dissertation chapter 4), and the report's "10 percent crosslinker" must stay out. Show as a range, no formulation.

### Highlight 4. Survives sterilization and shipping (PUBLIC; upgrade of W11)

- **Headline.** "Compatible with multiple sterilization methods" (the editorial rule's own example; drop the "Seven of eight cycles" tally).
- **Chart.** Keep the W11 right panel and make its labels explicit. Bars, mean kPa with one SD whisker, n = 5 each, sanded silicone coupons, dry packaged, shipped to a steriliser and back, then soaked 14 days: "Shipped only" 61.0 (SD 8.6), "Shipped plus gamma" 49.8 (SD 13.3), "Shipped plus e-beam" 60.5 (SD 16.1). Do not add batch controls without Kam (gamma control 71.3). Do not chart the implant-silicone set (n = 2 to 3, SD 72) or any wet packaged group.
- **New sentence the report supports.** "Ethylene oxide left no visible coating loss in 38 of 38 before-and-after image pairs, on implant silicone, a probe cover and a breathing tube." Source: ZwiCoat internal study, 2025 (R28). Qualitative, so PUBLIC to BORDERLINE; the 16 h at 50 C array result adds full dye coverage on three device types.
- **Source.** ZwiCoat internal study, 2025.
- **Before launch.** Resolve flag 4 (steam, UV).

### Highlight 5. Bends, curls and re-inserts without losing coverage (BORDERLINE, mostly photographic)

- **Headline.** "Curled 50 times and inserted 10 times, still fully coated."
- **Chart.** No chart. A two-photo figure (arrays after "50 full-circle bends plus 10 insertions" and after "dry, bag a month, re-wet", dye-stained, on grid paper), with a one-line table under it: Stress, Result (100 percent dye coverage, 100 percent dye coverage). Add, as a plain bar pair if Kam approves R4: "Insertion work in a synthetic cochlea, uncoated = 100, coated = 32 (68 percent less; 5 trials per group, p < 0.001)". Absolute values are not in my sources; the grant Fig 6 is needed. The published cadaver result (about 40 percent less peak force, 37 vs 64 mN, 9 insertions per group) is already W07 on the evidence page and can be cited in the same caption.
- **Caption.** "Coated electrode arrays kept full dye coverage after 50 full-circle bends and 10 insertions, and after drying, a month in a bag and re-wetting."
- **Source.** ZwiCoat internal study, 2025.
- **Why BORDERLINE.** n is not recorded, the arrays carry the 2025 formulation, and the report itself rates curl and drying as "green" and "amber" respectively. The photo in the report is 493 x 432 px with a device-named legend; a new photo from the lab archive is better (see section 5). Wet rod bending down to 2 mm (R10) is a published sentence that can ride along: "Hydrated coatings bent around rods from 32 mm down to 2 mm without cracking (Peel 2024)".

### Not proposed, with reasons

Tool contact, drop tests, shelf life, heat, cold, residual gas: not measured. Impedance, the target date, the benchtop risk plan, regulatory table, thresholds: private. The 3.5 times expander line: overstated, see flag 2. The pendulum result is already on the page as video; keep it at "about 50 J, no visible damage, one device".

## 5. Images

| File | Slide or page | What it shows | Rating (1 to 5, public site) | Note |
|---|---|---|---|---|
| `MD\assets\pendulum_before_after_impact.png` (same as report Fig 7; 1948 x 1048, 2.2 MB) | Report p. 10; Kam's slides 2 | 125 cc coated expander front and back, before and after a padded 44 to 54 J pendulum hit, no visible damage | 4 | Clean and honest. The site already has sharper, separate jpgs in `assets-staging/lab-media/` (`expander-mentor125-before-front.jpg` and others, rated 4 to 5). Use those with fresh crops and the site's labels, not this composite (its labels are not in Arial). Kam's slide 2 shows "75 J" text: do not use. |
| Report Fig 2 a and d (`imgs\i-007-001.png`; original `MD\assets\grant_fig5_embedded.png`, 483 x 807) | Report p. 7 | Stained arrays and breathing tubes after 50 bends and 10 insertions (a) and dry, bag, re-wet (d) | 3 | Low resolution, legend text names the device type, mixes arrays and tubes. Find the full-size originals in the grant files or shoot new ones. |
| Report Fig 1, A1 to A3 (`imgs\i-006-000.png`; `MD\fig_crops\tweezers.png`) | Report p. 6 | Blue-coated strip held by tweezers, grid paper | 2 | Informal, undated, strip substrate unclear (silicone or PEEK), no instrument or grip recorded. Reshoot after the handling tests (target 30 November 2026). |
| Report Fig 3 d (`imgs\i-008-002.png`) | Report p. 8 | Coated breathing tube at 30 and 140 minutes of drying, cracks marked with red arrows | 2 | Shows failure, gloved hands. Not for a public page. |
| EA22 summary slides 2 and 3 (`26.01.13_EA22_coating summary.pdf` pages 2 and 3, rendered to jpg) | Pages 2, 3 | Eight blue-dye coated electrode arrays, hand-numbered T300 to T307, on stone with yellow foam, ZCMI banner on top | 3 | Real device photos, uniform stain. The numbers and slide banner must be cropped off, and they are the customer's shape (EA22). The lab-media array photos (`ci-array-coated-rehydrated-curl-01.jpg` and `ci-array-coated-electrodes-01.jpg`) are better. |
| EA22 summary slide 4 | Page 4 | Impedance plots, four implants | 1 | PRIVATE. |
| Report Fig 5, Fig 6, Fig 8, Fig 9, Fig 10 (`imgs\i-009-004.png`, `i-009-005.png`, `i-011-008.png`, `i-011-009.png`, `i-010-007.png`) | Pages 9, 11 | Charts, re-plotted in matplotlib (Fig 5, 8 in DejaVu Sans, Fig 6, 9, 10 in Arial) | 1 as images, 5 as sources | Never publish these PNGs. Rebuild from the csv or json named in section 2. |
| `MD\assets\L1_substrate_standard_recipe.png` through `L6_*.png`, `eo_vs_dried_rehydrated_lapshear.png`, `aa82_mass_vs_weeks.png` | `_build\assets` | Lap-shear scatter plots with recipe codes and researcher first names in the legends; accelerated-aging mass loss | 1 | Recipe codes (W, C) and aging rates are barred by rule 3. Not published; rebuild only the allowed W02 view. |
| `MD\assets\medel_*` images | `_build\assets` | Other implant makers' devices | 1 | Not ours; skip. |
| `ks_s2_Picture20.png` (Kam's slides 2) | Slide 2 | Same pendulum composite as above | 3 | See first row. |
| Kam's slides 3 picture (Picture 13, 1822 x 1006) | Slide 3 | 100 cc expander being inflated, "3.5x" slide title | 2 | Do not use with 3.5x; the site already holds `expander-inflated-200pct-01.jpg`. |

## 6. Where each highlight's numbers will be rebuilt from

- H1: `ZD\Adreann Peel\22.01_Long_Term_Wear_2500_Cycles\extracted-data\Fig6.9_COF_first_vs_last_100cycles_wide.csv` (copy to `figures/data/`).
- H2: `...\21.11_Mandrel_Bend_Flexural_Durability\extracted-data\Fig6.7_mandrel_bend_time_to_failure.csv` and `...\21.12_Desiccation_Rehydration_COF\extracted-data\Fig6.8_COF_swollen_vs_rehydrated_wide.csv`.
- H3: `figures/data/W02_lapshear_public.json` (already in the repo).
- H4: `ZD\Kyle Ruby\25.09.01_Kyle_Sterilization_LapShear\workup\sterilization_lapshear_summary.csv`, rows "Sylgard 60grit" (shipped-only, gamma, e-beam). W11 already uses these.
- H5: needs the grant Fig 5 originals and Fig 6 (68 percent) absolute values, not located in the sources I was given.

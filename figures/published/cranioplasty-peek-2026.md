# Cranioplasty and PEEK, 2026 (manuscript in preparation, grant draft, archive lap-shear)

Extracted 2026-11-02 for the PEEK and orthopedic page. Everything below is
read-only extraction; nothing here is approved for the site until Kam says so
(see section 5). Figures from the manuscript are NOT to be posted.

Sources read in full:

- Manuscript: `G:\My Drive\9 Zwitterion\Claude Code projects and misc files\misc transfer files\For website\cranioplasty\Zwitterion and Cranioplasty paper 8-28 CLAUDE ANNOTATED 9-22.docx` (tracked changes and 16 comments read; the text is mostly tracked insertions, so a plain docx read misses it).
- Grant: same folder, `Research Strategy 9-18 ty (1) CLAUDE EDITS 9-21.docx` (tracked changes and 8 comments read).
- Archive: `Lap-shear Master.xlsx` (all year sheets, 430+ groups), Kyle Ruby E-reports `25.07.10_Kyle_PEEK_KLSMartin_Tensile` and `26.04.27_Kyle_PEEK_TissueExpander_DipCoating_LapShear`, plus two files you did not list but that decide the n and the sample sizes: Benjamin Brower `26.04.24_Ben_PEEK_LapShear_Irgacure_Comparison` and Terry Yin `26.04.22_Rodent_Cranioplasty_Behavioral_Data\raw data\Terrys data.xlsx` (per-animal values).

## 0. Read this first: what the manuscript does and does not contain

- The manuscript draft stops after the Methods, Results and Discussion of a SMALL study. Its only in-vivo result is rat beam-walk motor recovery after early cranioplasty. There is NO fibrous capsule thickness, NO bacterial count, NO infection rate, NO bone contact and NO histology in the manuscript or in the grant's preliminary data for PEEK.
- Capsule, histology (H&E, trichrome, Iba1, CD68, GFAP, NeuN) and in-vivo bacterial burden (S. aureus or P. aeruginosa, imaging, CFU, SEM) are PROPOSED aims in the grant (Aims 2.2 and 2.3), not results. The sentence in the brief, "coated PEEK implants showed less fibrous capsule and fewer bacteria", is therefore not supported for PEEK and must not go on the site.
- The 50 percent capsule and 95 percent protein numbers in the grant (its Fig 4) are from silicone (PDMS) in mice, from already published work (Horne 2023, Acta Biomaterialia, which is already in `figures/published/`). They are not PEEK data.
- One in-vitro bacterial number exists for PEEK (grant Fig 8, about 35 percent of uncoated). It is thin; see 3 and 5.

## 1. Header

Manuscript (as drafted):

- Title: "Feasibility and Utility of Zwitterion-Coated Alloplastic Cranioplasty Following Decompressive Craniectomy" (title completed by the annotator; the original was truncated after "Alloplastic").
- Authors (as listed): Terry C. Yin PhD; Kameron Hansen; Steffen G. Osborn BS BBA; Danny C. Bartlett BS (the grant cites a Bartelt DC, so the surname is probably misspelled here); George Barrera; C. Allan Guymon PhD; Marlan R. Hansen MD; Brian T. Andrews MD MA (corresponding). Affiliations: Departments of Otolaryngology and of Neurosurgery, University of Iowa Carver College of Medicine.
- Disclosures printed: CAG and MRH co-founders of ZwiCoat Materials Innovations with equity; KRH president and CTO with equity.
- Intended journal: NOT stated anywhere in the file.
- Status: manuscript in preparation. Open placeholders in the text: implant dimensions ("~XX x XX mm"), sanding tool "XX", ethics number given (IACUC 2062484), Methods stop before imaging or histology, citations incomplete (comment c13 lists mismatches in refs 13 to 16).
- One-sentence finding: Photografted zwitterionic hydrogel on PEEK (overmolded or dip-coated) bonds so strongly that the gel fails before the interface does, and rats given coated PEEK after brain injury crossed a balance beam in 53 percent of baseline time against 90 percent for uncoated PEEK (p = 0.0454).

Grant:

- Title: none on the Research Strategy pages ("RESEARCH STRATEGY", R01 per the text "this R01 proposal"; Aim 1 freestanding zwitterionic hydrogel at the decompressive craniectomy site, Aim 2 zwitterionic-coated PEEK cranial implants). PI named in comments: Brian T. Andrews. Funder is not named beyond "R01" and "NIH R01 renewal" in Future Investigations.
- Status: unfunded draft, dated 9-18 with edits 9-21 (a 5-year plan, Aim 1 done by year 3). A letter of support from a PEEK cranial implant manufacturer is referenced; do not name the partner on the site (CLAUDE.md editorial rule).
- A public abstract: none in the files. I could not check NIH RePORTER from here. Treat the grant as not public until Kam confirms an award and a public abstract.

## 2. In-vivo results

Study as the manuscript describes it: early cranioplasty study, 56 rats purchased in total (28 male, 28 female Long Evans, 10 weeks, 350 +/- 20 g; this is the whole cohort, the PEEK groups are a subset). Closed-skull "hit and run" cortical impact (5 mm probe, 4 mm depth, 6.0 m/s, 0.1 s), immediate hemi-craniectomy, then cranioplasty with an uncoated or a dip-coated PEEK piece cut and bevelled to fit, glued with cyanoacrylate. Dip-coated pieces were checked for full coverage before implantation. Statistics: GraphPad Prism; the methods say two-way ANOVA with Dunnett, but the two PEEK results use an unpaired two-tailed Welch t-test (a mismatch to fix in the draft). Error bars SEM.

Per-animal n is NOT in the manuscript text. It is in Terry Yin's workbook (archive): 10 ZI-PEEK rats and 7 PEEK rats for each of the two behavior measures. I re-ran the Welch test on those values: means and p reproduce exactly (see notes).

| Species / strain | Implant (coated vs uncoated) | Timepoint, duration | Metric | Uncoated PEEK | Coated PEEK | Change | n (uncoated / coated) | p | Exact or approximate | Figure |
|---|---|---|---|---|---|---|---|---|---|---|
| Rat, Long Evans, male and female | Dip-coated zwitterionic hydrogel on PEEK vs bare PEEK, early cranioplasty after cortical impact and hemi-craniectomy | Post-cranioplasty day not stated (planned early window in the grant: 24 to 48 h after injury; follow-up 12 weeks planned) | Beam-walk crossing time, normalized to baseline | 0.896 +/- 0.156 SEM (0.896 +/- 0.145 recomputed) | 0.529 +/- 0.040 SEM (0.529 +/- 0.041 recomputed) | -41 percent (grant text says 41 percent) | 7 / 10 (from per-animal sheet) | 0.0454; diff of means 0.367, 95% CI 0.010 to 0.725 | Exact (text); n is exact from the sheet | Manuscript Fig 4A; grant Fig 9 |
| same | same | same | Hindlimb slips, normalized to baseline | 1.798 +/- 0.576 (1.798 +/- 0.551 recomputed) | 1.380 +/- 0.319 (1.380 +/- 0.360 recomputed) | -23 percent | 7 / 10 | 0.5388, not significant | Exact (text) | Manuscript Fig 4B |
| same | same | same | Grip strength (archive only; never reported in manuscript or grant; units not in file) | 4.18 (10 values under the "PEEK" header) | 4.19 (11 values under "PEEK/ZI") | +0.3 percent | 10 / 11 | 0.99 (my Welch test) | Computed by me; not in any document | none |

Notes on the table:

- Which column is coated for grip: the sheet lists columns "PEEK" and "PEEK/ZI" with 10 and 11 values; I have assigned them by header. No unit and no timepoint are recorded.
- The manuscript's SEMs for PEEK (0.156) and for slips differ a little from my recomputation. Means and p values match to four decimals, so this is probably a transcription edit in the draft. Flag for the authors, not for the site.
- Sham and TBI-only grip values (n = 3 and 4) also sit in the sheet; unreported.
- Cohort within-study contrasts the grant mentions but the manuscript does not report: early vs late cranioplasty with polydioxanone plates (Osborn 2025/2026, already published, see below).

Already-published, related in-vivo context that appears in the grant (not PEEK, with the publication that carries it):

| Item | Value as stated in the grant | Publication (grant ref) | Status |
|---|---|---|---|
| Unrepaired craniectomy raises foot slips in rats (sham vs TBI-DC day 4) | p < .0001; days 11 and 18 p = .0305 and .0426 | Osborn SG et al. Cleft Palate Craniofac J 2026;63(7):1968-1973, DOI 10.1177/10556656251357992 (ref 9) | Published (the manuscript cites it as accepted in press June 2025) |
| Freestanding zwitterionic hydrogel at the craniectomy site, beam-walk crossing time (fraction of baseline), sham / TBI-craniectomy / hydrogel | Day 7: about 1.10 / 1.74 / 0.79; day 14: about 0.82 / 1.68 / 0.66 (values read by eye from the grant's Fig 6; verify in the paper) | Bartelt DC et al. Face 2026, DOI 10.1177/27325016261483163 (ref 19) | Published per the grant; I did not open the paper |
| Serum TBI biomarkers (GFAP, NfL, UCH-L1) lower with hydrogel | GFAP F(3,20) = 8.996 p = 0.0006; NfL p = 0.0306; UCH-L1 p = 0.0187 (group means not given) | same (ref 19) | Published per the grant |
| Soft-tissue fibrosis lower with hydrogel at the craniectomy site | qualitative (Masson trichrome) | same (ref 19) | Published per the grant |
| Capsule about 50 percent thinner at one year; protein adsorption about 95 percent lower; fibroblast adhesion more than 80 percent lower after six months explanted | on silicone, mice | Horne 2023 Acta Biomater 166:212-223 (ref 12); Leigh 2019 Langmuir (ref 18) | Already in `figures/published/` |

## 3. In-vitro results

| Test | Result | n | Statistics | Source | Exact or approximate |
|---|---|---|---|---|---|
| Coating coverage on flat PEEK (methylene blue staining) | Overmolding gave continuous full-surface coverage. Dip-coating gave acceptable coverage but not full coverage on every piece (a typical piece is bare near the lower edge); fully coated dip-coated pieces were also obtained. Inverting the piece mid-cure gave more even coverage than not inverting. Exposures 5 to 10 s | not given | none | Manuscript Results, Fig 1 and Fig S1 | Qualitative |
| Lap-shear, PEEK, as-prepared (dry) | 635 kPa, cohesive failure inside the gel | about 5 (from chart; matches the archive group, n = 5) | mean, error bars about 145 (this is the SD of the archive group, the caption says SE) | Manuscript Fig 2C; archive 26.04.28 | Exact (text) |
| Lap-shear, PEEK, "swollen" | 163 kPa, cohesive failure | about 5 | mean, error about 33 (SD) | Manuscript Fig 2C | Exact (text); the soak condition conflicts with the archive, see 4 |
| Lap-shear, silicone (PDMS) control grafted with a surface grafting agent | all failed adhesively near 130 kPa (chart about 120 swollen, about 140 as-prepared) | about 4 to 6 per bar | none | Manuscript Fig 2C | Approximate (chart) |
| Bacterial adhesion on PEEK | coated PEEK about 35 percent of uncoated (uncoated set to 100; error bars SD about 106 on uncoated, about 17 on coated) | not stated | none stated | Grant Fig 8; text says "60 percent reduction" while the figure shows about 65 percent (annotator's comment c5 asks Kam to reconcile). The figure axis says "% Adhesion" and does not name species or method; the text says bacterial | Approximate, read from chart |
| Protein adhesion on PEEK | none; fibrinogen on PEEK is listed as an Aim 2.1 plan | - | - | Grant | Not done |
| Cells on PEEK (fibroblasts, macrophages) | none; Aim 2.1 plan | - | - | Grant | Not done |
| Accelerated aging, in-vivo bacterial burden, capsule, histology on PEEK | none; Aims 2.2 and 2.3 plan | - | - | Grant | Not done |
| Mechanism | Self-initiated photografting: under 365 nm light the ketone group in every PEEK repeat unit is excited, takes a hydrogen from a nearby molecule (water, monomer or crosslinker), and the resulting surface radical bonds to a monomer. Chains then grow from the surface while bulk polymerization runs in parallel | - | - | Manuscript Results and Fig 3 caption; grant Innovation and Preliminary data; supporting literature cited there: Kyomoto and Ishihara 2009 (ACS Appl Mater Interfaces 1(3):537-542, DOI 10.1021/am800260t) and Kyomoto 2013 (Biomaterials 34(32):7829-7839, DOI 10.1016/j.biomaterials.2013.07.023) | Qualitative |

Process details (PRIVATE, not for the site): formulation (water-to-monomer 12, crosslinker 0.05), initiator 0.087 wt percent of monomer, cure 5 min at 365 nm about 60 mW/cm2 for overmolding, dip 5 to 10 s at about 780 mW/cm2 total then more than 1000 mW/cm2, dosing volume 0.03 uL per mm2.

## 4. PEEK lap-shear from the archive

Source: `Lap-shear Master.xlsx`, 2026 sheet, plus the E-reports and per-sample CSVs. All four archive PEEK groups were cured to the same silanized-glass sandwich geometry. All failed cohesively (inside the gel). PEEK is KLS Martin cranioplasty stock in the two Kyle groups.

| Group | Date | Condition (as recorded) | Avg (kPa) | SD (kPa) | n | Year | Failure mode | Notes |
|---|---|---|---|---|---|---|---|---|
| Kyle, PEEK, dry | 2026-04-28 | No soak (dry), W12 C0.05 | 635.2 | 143.6 | 5 | 2026 | cohesive (C) | 2 of 5 pulls reached the 100 N load cell limit, so the true mean is higher: it is a lower bound. Per-sample 518, 843 (maxed out), 498, 604 (maxed out), 713 kPa |
| Kyle, PEEK, soaked, all samples | 2026-04-28 | 10 min soak in water, W12 C0.05 | 129.0 | 66.0 | 7 | 2026 | cohesive (C) | 2 of 7 flagged "potentially stripped loading" (18 and 71 kPa) |
| Kyle, PEEK, soaked, without the 2 stripped pulls | 2026-04-28 | same | 162.7 | 34.7 | 5 | 2026 | cohesive (C) | Matches the manuscript's "163 kPa"; per-sample 177, 194, 187, 110, 146 kPa |
| Ben, PEEK, with Irgacure | 2026-04-24 | recipe not recorded | 7.7 | 4.6 | 3 | 2026 | cohesive (C) | Per-sample 3.1 (popped off early), 12.3, 7.7 kPa |
| Ben, PEEK, no Irgacure | 2026-04-25 | recipe not recorded | 13.7 | 11.0 | 3 | 2026 | cohesive (C) | Per-sample 26.2, 9.4, 5.4 kPa; one may have slipped |
| "Cranioplasty material" (row in the 2025 sheet under the roughness campaign) | 2025-08-20 | W10 C0.03, PBS soak (time blank) | 680.5 | 62.0 | not recorded | 2025 | not recorded | Scientist Kyle. Likely PEEK from the same KLS Martin stock but the substrate is only named "Cranioplasty material"; treat as unconfirmed |
| Kyle, July 2025 tensile pulls | 2025-07-10 | W12 C0.05 on KLS Martin PEEK | peak loads about 27, 48, 61 N | - | 3 | 2025 | not stated | Dimensions are template defaults; load only, no stress. Not a lap-shear. Do not use |

Where the manuscript and the archive disagree (needs a decision before anything is quoted):

- The manuscript says the 163 kPa "swollen" samples were equilibrated 24 h in PBS. The archive records 10 min in water. The archive is the primary record. If the 24 h PBS test also exists, I did not find it. Safe wording for the site: "after a short water soak" until Kam checks the notebook.
- The manuscript's 635 kPa has no flag for the load-cell limit. In the archive two of the five dry pulls hit the 100 N limit, so 635 kPa is a lower bound. On the site say "over 600 kPa".
- The manuscript's "163 kPa" drops two pulls flagged as possibly stripped on loading. The all-samples mean is 129 kPa (n = 7). State both or round to "about 130 to 160 kPa".
- The 2026 W02 public data (`figures/data/W02_lapshear_public.json`) carries PEEK as 129.0 (n 7), 7.7 and 13.7 (n 3 each) and does NOT include the 635 kPa dry group (probably dropped by the "untrustworthy" flag). Its PEEK median of 13.7 kPa would badly understate PEEK. Recommend rebuilding the PEEK entries: dry 635 (lower bound), soaked 129 (n 7) and 163 (n 5), and leaving Ben's n = 3 groups out.

Mechanism sentence and its source:

- "The ketone group built into the PEEK backbone absorbs the same light that cures the gel, so the coating grafts straight onto the surface with no primer or pretreatment step."
- Sources: manuscript Results (Fig 3 text) and grant Innovation; the E-reports do not contain a mechanism statement (the Kyle E-report says only how strong the bond is). Published support: Kyomoto and Ishihara 2009 (PEEK, a phosphorylcholine monomer, no added initiator).
- Careful wording: the gel itself still contains a light-activated initiator in solution (Marlan Hansen's margin question "No photoinitiator?" was answered by the annotator: only the SURFACE initiator step is removed). Do not write "no photoinitiator". The existing page sentence "its backbone ketone acts as the photoinitiator" should be changed to "its backbone ketone does the grafting, so no primer is needed". Ben's no-Irgacure group (13.7 kPa, n 3) shows nothing about it; do not cite it.

## 5. Sensitivity screen

Rule applied (CLAUDE.md rule 3 and the editorial rules): published or already-shown-in-decks data are public; results from a manuscript in preparation stay off the site unless Kam approves the specific figure; formulation, process settings, partner names, scientist names and unpublished study designs are never posted. The owner's note for this session (2026-11-02) is read as: the PEEK lap-shear result may go online; the chart of PEEK grafting strength and the chemical pathway may be reworked and posted; the rat outcome may be discussed in general terms without the paper's figures; the animal studies may join the holistic figures. The paper's own figures (its Fig 1 to 4 and S1) are not posted; they must be rebuilt or replaced by archive originals.

| Item | Call | Reason |
|---|---|---|
| PEEK lap-shear: bond stronger than the gel, over 600 kPa dry, about 130 to 160 kPa after a short soak, all cohesive | PUBLIC (owner-approved) | Lap-shear database by substrate is already allowed; sources are archive groups. Do not print W, C or initiator dose. Say "lower bound" for the dry value. Source line "ZwiCoat internal tests, 2025 to 2026" (PEEK groups are 2026; the silicone and PVC comparison rows are 2025 to 2026; see section 6) |
| PEEK lap-shear chart reworked from archive data | PUBLIC (owner-approved) | Rebuild in `figures/build_figures.py` from archive numbers, not from the manuscript Fig 2 |
| Chemical pathway (ketone excited, hydrogen taken, surface radical, chain growth) | PUBLIC (owner-approved) | Redraw our own scheme (not the manuscript's Fig 3). Label the monomer "zwitterionic monomer"; do not draw or name SBMA; do not say "benzophenone" (the manuscript's caption does); say "diaryl ketone" or "ketone group". Mechanism is in Kyomoto 2009 |
| PEEK mechanism sentence ("no primer, backbone ketone grafts") | PUBLIC | Published precedent; fix the "photoinitiator" wording as noted in 4 |
| Rat early-cranioplasty motor benefit, general terms only | BORDERLINE: general wording only if Kam approves | Manuscript in preparation; 10 vs 7 rats, one significant metric (p = 0.0454), the other measure not significant, no timepoint stated. Allowed (per the owner): "rats with coated PEEK implants recovered balance-beam performance faster than rats with uncoated PEEK". No numbers, no p value, no figure, no n, until Kam approves the exact figure |
| Exact values 0.529 vs 0.896, p = 0.0454, n | PRIVATE until Kam approves | Rule 3 |
| Hindlimb slips (p = 0.54) and grip strength (no difference) | PRIVATE | Not significant and not reported; the site drops non-significant results |
| In-vivo capsule, bacterial count, infection, histology on PEEK | DOES NOT EXIST | Aims 2.2 and 2.3 only. No sentence on the site may imply results |
| PEEK in-vitro bacterial adhesion about 35 percent of uncoated (grant Fig 8) | PRIVATE (and do not use as is) | Unpublished; error bar on the uncoated bar exceeds the bar; no n, no test, no species or method; text and figure disagree (60 vs 65 percent) |
| Published antifouling and capsule numbers on silicone and arrays (Horne 2023, Shen 2021, Leigh 2019) | PUBLIC | Already in `figures/published/`; they are not PEEK, so the page already labels them as silicone and arrays |
| Grant problem-framing numbers (cranioplasty complication rate, cost, infection) | PUBLIC (published refs) with checks | Cited to papers. Verify refs before use (see section 6 flags). Market-size numbers: skip (commercial report) |
| Grant (aims, power analysis, design, budget-like content, unpublished preliminary figures) | PRIVATE | Unfunded draft |
| Grant's public abstract | NONE FOUND | Check NIH RePORTER if an award exists |
| Formulation, doses, cure lamp settings, dip-coating process settings, surfactant, sanding | PRIVATE | Rule 3 |
| Dip-coating partial coverage on some pieces | PRIVATE | Process yield |
| Ben's PEEK Irgacure vs no-Irgacure groups (8 and 14 kPa, n = 3) | PRIVATE | Recipe not recorded, loading artifacts, n = 3; says nothing about the bond |
| Ambiguous "Cranioplasty material" 680 kPa row | BORDERLINE | Substrate and n not confirmed; do not use |
| Photos in the manuscript (Fig 1, Fig S1, dyed coated PEEK) | Not for the site | They are the paper's figures. If Kam wants a PEEK photo, use an archive original with a fresh crop, or one of the OV white-paper PEEK photos already in the deck pool |
| Partner and scientist names (KLS Martin, Yin, Andrews, Kyle, Ben) | PRIVATE | Editorial rule: minimum citation "ZwiCoat internal study, 2026" |

## 6. Proposed site text for the PEEK and orthopedic page

Style per editorial rules: no monomer names, no "benzophenone", no em-dashes, plain language, varied sentences. Product name is ZwiCoat.

Problem framing (for the "The problem" block, in addition to what the page has; claims and sources):

> Cranial reconstruction has a high failure rate: in a US claims database of 8,275 people who had cranial implants, 36.6 percent had a complication within seven years (Li et al., World Neurosurgery 2017). PEEK is the material surgeons reach for most often, and it is hydrophobic, so proteins and bacteria stick to it. When that goes wrong, the usual outcome is wound breakdown and removal of the implant (Henry et al., Neurosurgery 2021).

Checks before use:

- The 36.6 percent figure is for all cranial reconstruction in that database (autologous and synthetic), not for PEEK alone. The wording above says so.
- "PEEK is the material surgeons reach for most often" is the grant's claim ("the most utilized cranioplasty biomaterial") and the manuscript's ("dominant biomaterial") without a citation. Cite a source or soften to "PEEK is widely used".
- The explant sentence is the grant's own wording with Henry 2021 (Neurosurgery 89(3):383-394, DOI 10.1093/neuros/nyab180). I did not open that paper.
- The grant's 3.4 percent (autologous) vs 5.3 percent (alloplastic) "readmission" rates cite Do 2023, J Neurosurg 138:514-521, whose title is about operative intervention for infection; the grant's wording and the title do not match. Do not use until read.
- The grant's HCUP numbers (12,700 craniectomies in 2001; 20,616 repair procedures; 949 million dollars) cite a 2002 HCUP overview paper that is unlikely to carry them. Skip.
- The existing page line "15 percent of 183 PEEK cranioplasties had complications" is not in these documents; its source is elsewhere.

General-terms results paragraph. Option A is the default and needs no approval. Option B is only for use if Kam approves.

- Option A: "A rat study of coated and uncoated PEEK cranial implants is under way with a university surgical team."
- Option B (needs Kam's approval, no figures): "In a rat model of brain injury and early cranioplasty, animals that received a coated PEEK implant recovered balance-beam performance faster than animals that received an uncoated one. The study measured motor recovery; infection and tissue response are the next questions." This is the one sentence the data support. Do NOT write "less fibrous capsule" or "fewer bacteria" about PEEK. If Kam wants a tissue or bacterial sentence for PEEK it has to wait for Aims 2.2 and 2.3.

Mechanism (spec strip and a small redrawn scheme):

> PEEK needs no primer. The ketone group built into its backbone absorbs the curing light and starts the graft, so the coating bonds to the surface in the same step that forms the gel.

Lap-shear chart spec (rebuild with `figures/build_figures.py`, Arial):

- Title (positive, plain): "The coating bonds to PEEK more strongly than the gel itself".
- Panel layout: two groups of bars on one y axis, "Bond strength (kPa)". Group 1 "As prepared (dry)", group 2 "After a short water soak". Within each group: PEEK, silicone, PVC. A strip of the archive groups' values over each bar, n shown under each label ("n = 5 samples", "n = 7 groups, 37 samples").
- PEEK, dry: 635 kPa mean, n = 5, drawn with an arrow or "over" mark and the footnote "two of five tests reached the load cell limit, so the true value is higher". PEEK, soaked (10 min in water): 129 kPa (n = 7) and 163 kPa (n = 5, two flagged pulls excluded); show the 129 as the bar and mention 163 in the caption.
- Silicone (Sylgard, Bentec and other medical silicones, 2025 to 2026), short soak (up to 15 min): median 84 kPa, range 78 to 138, 7 groups, 37 tests, 6 cohesive and 1 split. Dry (no soak recorded): median 131 kPa, range 90 to 237, 11 groups, only 8 samples with a recorded n (the rest do not record n); drop this bar if n is not defensible.
- PVC (medical PVC and ETT PVC), short soak (15 min, 2025): 419 kPa, 5 samples, one group, cohesive. Dry: median 349, range 184 to 491, 7 groups, 36 tests. After long soaks (24 h or more) PVC groups are much weaker (median 44 kPa, range 0 to 171, 11 groups, 37 tests), so the PVC bars must carry their soak label; omit PVC from the swollen panel if the comparison cannot be matched.
- The label the owner asked for: "coated film fails inside the gel, not at the PEEK surface". Supported: all 4 PEEK archive groups plus the manuscript failed cohesively. Caution: silicone also fails cohesively in most long-soak groups (47 of 56 W10-12 PBS groups), so the statement distinguishes PEEK from the BARE-silicone case only without a grafting agent. Put it as a PEEK annotation, not as a contrast with silicone.
- Matching caveat to put in the notes, not the headline: PEEK soak was 10 minutes, whereas most silicone groups in the database were soaked 24 h to 14 days; the matched short-soak silicone subset above is the fair comparison.
- Source line: "ZwiCoat internal tests, 2025 to 2026" (PEEK is 2026; silicone and PVC comparison rows are 2025 to 2026). Do not print the formulation. Do not name KLS Martin; write "PEEK cranial implant stock".
- Static PNG fallback required. Keep the chart static (rule 5).

## 7. Rows for the in-vivo study browser (W32 format)

For Kam's decision. All rows are from a manuscript in preparation and are NOT to be added until approved. Columns follow `figures/data/W32_invivo_studies.json`: paper, year, journal, species, duration, device_or_substrate, metric, uncoated, coated, unit, pct_change, n, p, p_text, exact, figure, setting, note. The editorial rule drops non-significant bars, so the second row is listed for completeness and should probably be left out.

```json
[
  {
    "paper": "Yin et al.",
    "year": 2026,
    "journal": "manuscript in preparation",
    "species": "rats (Long Evans)",
    "duration": "not stated (post-cranioplasty day not given)",
    "device_or_substrate": "PEEK cranial implant, dip-coated",
    "metric": "Beam-walk crossing time, normalized to baseline",
    "uncoated": 0.896,
    "coated": 0.529,
    "unit": "fraction of baseline time",
    "pct_change": -41,
    "n": "7 vs 10",
    "p": 0.0454,
    "p_text": "0.0454",
    "exact": true,
    "figure": "manuscript Fig 4A (not for posting)",
    "setting": "in vivo",
    "note": "manuscript in preparation; early cranioplasty after brain injury; Welch t-test; means and p from the draft, n from the per-animal sheet; needs Kam approval"
  },
  {
    "paper": "Yin et al.",
    "year": 2026,
    "journal": "manuscript in preparation",
    "species": "rats (Long Evans)",
    "duration": "not stated",
    "device_or_substrate": "PEEK cranial implant, dip-coated",
    "metric": "Hindlimb slips, normalized to baseline",
    "uncoated": 1.798,
    "coated": 1.380,
    "unit": "fraction of baseline",
    "pct_change": -23,
    "n": "7 vs 10",
    "p": 0.5388,
    "p_text": "0.5388 (ns)",
    "exact": true,
    "figure": "manuscript Fig 4B (not for posting)",
    "setting": "in vivo",
    "note": "manuscript in preparation; not significant; leave out under the site rule on non-significant results"
  }
]
```

Notes for the decision:

- W32 currently holds only published papers, and the "paper" and "journal" fields drive citations on the page. If these rows go in, the page needs a visible "manuscript in preparation" tag, or the browser should leave them out and let the general-terms sentence carry the result.
- No capsule, bacteria, infection, bone-contact or histology rows can be written for PEEK because the data do not exist yet.
- Candidates from the grant that could be W32 rows once the underlying paper is opened (they are published; I have only the grant's figure): freestanding hydrogel at the craniectomy site, beam-walk crossing time, Bartelt et al., Face 2026 (day 7 about 0.79 vs 1.74; day 14 about 0.66 vs 1.68 of baseline; uncoated = TBI-craniectomy without hydrogel). Verify values and n from the paper itself before adding.

## 8. Items to ask Kam

1. Approve or withhold the exact beam-walk values (0.529 vs 0.896, p = 0.0454, n 10 vs 7), or keep to the general sentence.
2. The manuscript says 24 h PBS soak for the "163 kPa" group and the archive says 10 min in water. Which is the truth? The site must use the archive wording until this is settled.
3. Should the W02 public PEEK entries be rebuilt (dry 635 lower bound, 129 n 7, 163 n 5; drop Ben's groups)?
4. The brief mentions capsule and bacteria on coated PEEK in rats. These results do not exist in either document. Is there a separate dataset (Aim 2.2 or 2.3 pilot)? If so, it would need its own extraction.
5. Open questions in the drafts that touch the page: intended journal, the bacterial adhesion method behind grant Fig 8, "Cranioplasty material" row identity.

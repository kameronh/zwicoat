# Figure and image approval sheet

Kam's rule (2026-10-29): nothing goes on the site unless it comes from
published data, or Kam approves it here. Phase 0 built figures from the
internal archive; this sheet sorts them. Kam marks the "Decision" column.

Classes:

- **P**: every number is from a published paper or public document. Safe.
- **P-**: published except one series; rebuild without that series. Safe
  after rebuild.
- **A**: aggregate counts of the archive (how many tests, how many animals);
  no result values. Reveals scale, not results. Kam's call.
- **I**: internal results or process data (formulations, thickness recipes,
  yields, unpublished studies). Hold unless Kam approves.
- **M**: manuscript in preparation. Hold until published.

## Charts (figures/png)

| id | what it shows | class | note | Decision |
|---|---|---|---|---|
| W01 | experiments per year by category | A | counts only, but the category split hints at the program; scientists' names are not shown | |
| W02 | 430 lap-shear group means by substrate | I | bond strengths per substrate are internal process data | |
| W03 | CI dip-coating database and learning curve | I | process yield and jig generations | |
| W04 | fibrosis reduction by study | P- | drop the "dual-network manuscript" rat bar; keep Horne 2023 (3 bars), Peel 2024, Ben-Shlomo 2026 | |
| W05 | fibroblasts, S. aureus, S. epidermidis, friction | P- | drop the "ZwiCoat 2025 probe cover" bar; keep Horne 2023, Shen 2021, Bennion 2021 | |
| W06 | durability checkpoints 2 weeks to 1 year | P | Shen 2021, Peel 2024, Ben-Shlomo 2026, Horne 2023 | |
| W07 | insertion force on three devices | P- | keep Bennion 2021 only, or hold until the ETT paper is out; a one-bar chart is weak, so prefer Bennion's force traces instead (new figure from the paper) | |
| W08 | sheep impedance at implantation and 4 weeks | P | Ben-Shlomo 2026 Fig 3B | |
| W09 | accelerated aging mass loss | I | | |
| W10 | substrate by test-type matrix | I/A | mostly "yes/no" plus group counts; reveals which substrates have been worked on | |
| W11 | sterilization compatibility | I | | |
| W12 | nine stat tiles | A | counts only (191 experiments, 1,156 tests, 468 samples, 136 animals, 9 papers, 10 years, 706 photos, 2,812 files, 20 people) | |
| W13 | claims by evidence tier | I | built from the internal evidence map | |
| W14 | 15-formulation sweep on PVC | I | formulation ratios; the most sensitive chart in the set | |
| W15 | thickness vs cure time on ET tubes | M | ETT manuscript | |
| W16 | every ETT intubation by surgeon | M | ETT manuscript | |
| W17 | textured implants 2016 vs 2019 | P | literature, cited in the expander white paper | |
| W18 | silver Foley CAUTI trial | P | Pickard 2012 | |
| W19 | silver ETT risk ratios | P | literature meta-analyses | |
| W20 | CGM signal delay | P | McClatchey 2019 | |
| W21 | mucus flow and plug clearance | P | Horne 2025 | |
| W22 | six-month sheep cohort | M | not built | hold |
| W23 | rat trachea submucosa | M | not built | hold |

## Interactive charts

| id | class | note | Decision |
|---|---|---|---|
| lap-shear explorer | I | exposes substrate, year, formulation W and C, failure mode and scientist per group; the richest process disclosure on the site | |
| timeline (W01 interactive) | A | per-year counts plus scientist names on hover | |

## Photographs and micrographs (assets-staging/deck-images)

| file | what | class | note | Decision |
|---|---|---|---|---|
| s26 | coated cochlear implant array, blue dye | I | a photo of a coated commercial array; reveals partner device? | |
| s30 | tissue expander before and after impact | I | internal 2026 test | |
| expanders_s12_9 | coated expander | I | | |
| expanders_s12_8, s39 | coated ET tube, cross sections, thickness chart | M | ETT manuscript | |
| s05 | histology, coated and uncoated PDMS on one sheet | P | Horne 2023 Fig 5; Elsevier, co-author reuse right to confirm | |
| s12 | histology, array capsule E to H | P | Horne 2023 Fig 7; same reuse question | |
| airway_s23_6 | sheep cochlea H&E and immunofluorescence | P | Ben-Shlomo 2026; believed CC BY (extraction worker confirming) | |
| s40_1 | rat tracheal histology | M | | hold |
| s04_2, s04_3 | protein and cell adhesion stripe micrographs | P | Leigh 2019 (confirm which figure) | |
| s19, s32, s33, s35, s37, s41, s43, s44, s01, s03 | drawn illustrations | n/a | excluded under the no-cartoons rule unless Kam wants them | |
| s09 | CAD of the jig | n/a | excluded by rule | |
| s13, s18, s29, s34, s36, s38, s45, s06, s10, s11, s24, s22, s07, s08 | deck charts | n/a | never placed as images; rebuilt in Arial where the data are published | |

## What replaces the held material

The site's "depth" story moves from internal counts to the published record:
nine papers, three dissertations, two issued patents, four species models,
ten years. The extraction workers are inventorying every quantitative result
in the papers (figures/published/*.md); the lead will propose a published-only
figure set (W24 onward) from that inventory, and the stat tiles become
"9 papers, 3 dissertations, 3 US patents, 4 animal models, 10 years, 20
authors" or similar public facts.

If Kam approves the class A items, the home page keeps the archive counts as
a second tile row labeled "and in the archive".

## Published-only set (built 2026-10-29 after the inventories)

| id | source | class |
|---|---|---|
| W04, W05, W07 | rebuilt with published series only (Horne 2023, Peel 2024, Ben-Shlomo 2026, Shen 2021, Bennion 2021) | P |
| W12 | public facts: papers, dissertations, patents, models, durations | P |
| W24 | publication timeline 2017 to 2026 | P |
| W25, W26 | Ben-Shlomo 2026 impedance components; round-window histology counts | P (values read from the figure, p exact) |
| W27 | Horne 2023 capsule thickness, six weeks and one year | P (exact) |
| W28 | Peel 2024 friction after explant; friction on six tissues | P (read from figure) |
| W29 | Shen 2021 bacteria on rat explants | P (read from figure, p exact) |
| W30 | Jensen 2021 crosslinker trade-off | P (read from figure) |
| W31 | Leigh 2019 bond strength vs benzophenone | P (read from figure, thresholds exact) |
| interactive 1 | publication timeline (W24 data) | P |
| interactive 2 | in-vivo study browser (W32 data) | P |

The lap-shear explorer is retired from the site plan unless Kam approves class I.
Image licenses: Ben-Shlomo 2026 CC BY 4.0 (free with credit); Peel 2024 CC BY 4.0
(its Fig 11 coated-array photograph can replace the internal array photo);
Jensen 2021 likely CC BY (confirm on the ACS page); Horne 2025 CC BY-NC-ND (numbers
re-plotted, images need the authors' consent; the authors are the founders);
Horne 2023, Bennion 2021, Leigh 2017, Leigh 2019, Shen 2021 are publisher
copyright (figures need permission; numbers may be re-plotted).

## Kam's decisions (2026-10-29, evening)

- Aggregate counts (class A): allowed when each number carries a takeaway.
- Internal photographs: allowed if the pictures are good. Lab media survey in
  `assets-staging/lab-media/`.
- Published micrographs: do not copy the journal panels; remake from the lab's
  original images with new crops and labels.
- Internal data in general: fine when broadcast-worthy and not sensitive.
  Reinstated: W10 (substrate matrix, with polyurethane), W11 (sterilization),
  the lap-shear database by substrate without formulation fields (interactive
  explorer returns in a sanitized form). Still held: W14 (formulation sweep),
  W09 (aging), W03 (process scores), W13; W15 and W16 (ETT manuscript) await
  a specific yes.
- Polyurethane is tested (CIVCO probe covers). The "Polyester" class in the
  lap-shear figures is relabeled "Polyurethane (probe cover)".
- Horne dissertation: 2023. Contact form: mail to info@zwicoat.com.

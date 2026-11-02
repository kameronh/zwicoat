/*
  Alt text, captions and sources for the charts that several pages share.
  Caption and source follow figures/MANIFEST.md. Update here, then match the
  copies in content/applications/*.md frontmatter (markdown cannot import this).
*/

export const W05 = {
  /** Short source line for the home and technology pages; the full one is under `source`. */
  sourceShort:
    '38 comparisons from 8 papers, 2017 to 2026: Leigh 2017 Biomacromolecules; Leigh 2019 Langmuir; Jensen 2021 ACS Biomaterials Science and Engineering; Shen 2021 ACS Applied Bio Materials; Bennion 2021 Otology and Neurotology; Horne 2023 Acta Biomaterialia; Peel 2024 ACS Applied Bio Materials; Barrera 2026 ACS Applied Polymer Materials. Bar values approximate where marked, read from the published plots.',
  name: 'W05_antifouling_and_friction',
  alt: 'Horizontal bar chart of 38 comparisons of coated versus uncoated surfaces from eight papers, grouped into four bands, as percent reduction. Protein: six bars, 91 to 98 percent. Cells: 16 bars, 53 to 99 percent. Bacteria: seven bars, 84 to 97 percent. Friction: nine bars, 84 to 96 percent. The median reduction is 94 percent.',
  caption:
    'Protein, cells, bacteria and friction: every published bench comparison of coated versus uncoated surfaces (38 bars from 8 papers), as percent reduction.',
  source:
    'Leigh BL, et al. Biomacromolecules 2017;18(8):2389-2401 (Fig 4 fibrinogen; Figs 6E, 7E, 8E cells on glass; fibrinogen and fibroblast values read from the published plots, astrocyte and Schwann cell values from the stated fold changes); Leigh BL, et al. Langmuir 2019;35(4):1100-1110 (Fig 7D fibrinogen; Fig 10D fibroblasts after 14 days in medium, plotted ratios used because the plotted absolute values conflict with the text); Jensen MJ, et al. ACS Biomaterials Science and Engineering 2021;7(9):4494-4502 (Figs 1G, 2G, 3G at 5 percent cross-linker; Fig 5A friction at 4 percent; values read from the published plots); Shen N, et al. ACS Applied Bio Materials 2021;4(2):1283-1293 (Fig 3 in vitro, Figs 7C, 7D rat explants at day 21, Fig 8 after 2 weeks in rats; values read from the published plots); Horne R, et al. Acta Biomaterialia 2023;166:212-223 (Fig 3F, mean of four cross-linker levels, new and after 6 months in mice; read from the published plot); Bennion DM, et al. Otology and Neurotology 2021;42(10):1476-1483 (Fig 1B, steel, ceramic and guinea pig dermis; text states more than 90 percent lower); Peel A, et al. ACS Applied Bio Materials 2024;7:3124-3135 (Fig 4 pristine and after 3 weeks in mice; Fig 5A six probes, bar shows the mean, range in the label; read from the published plots); Barrera G, et al. ACS Applied Polymer Materials 2026;8(18):16328-16338, doi:10.1021/acsapm.6c02510 (Fig 6 fibroblasts, text states more than 99 percent for low and about 90 percent for high cross-linker; Fig 4B friction, best group 2.5/2.5 percent).',
};

export const W04 = {
  /** Short source line for the home hero and the technology page; the full one is under `source`. */
  sourceShort:
    '10 measurements in mice, rats and sheep. Horne 2023, Acta Biomaterialia; Peel 2024, ACS Applied Bio Materials; Barrera 2026, ACS Applied Polymer Materials; Ben-Shlomo 2026, Hearing Research. Values read from the published figures.',
  name: 'W04_fibrosis_by_study',
  alt: 'Horizontal bar chart of 10 measurements of scar capsule or fibrosis around coated surfaces compared with uncoated, in mice, rats and sheep, four weeks to one year, from four papers (Horne 2023, Peel 2024, Barrera 2026, Ben-Shlomo 2026). Reductions run from about 45 to about 85 percent.',
  caption:
    'Less scar tissue around coated surfaces in mice, rats and sheep: percent reduction in fibrotic capsule or fibrosis, measurement by measurement.',
  source:
    'Horne R, et al. Acta Biomaterialia 2023;166:212-223 (Figs 5, 6G, 7I; flat-sheet and one-year values from the text, cylinder value approximate, read from the published figure); Peel A, et al. ACS Applied Bio Materials 2024;7:3124-3135 (Fig 3, values approximate, read from the published figure; text states over 60 percent); Barrera G, et al. ACS Applied Polymer Materials 2026;8(18):16328-16338, doi:10.1021/acsapm.6c02510 (Fig 7F, four coated groups, rats, 6 weeks, means read from the published plot); Ben-Shlomo N, et al. Hearing Research 2026;474:109606 (Fig 6G round window; pooled values approximate, read from the published figure).',
};

/* Charts say "uncoated versus coated" with no chemistry in the image or the caption. Chemistry may appear in a source line. */

export const W07 = {
  name: 'W07_insertion_force',
  title: 'Insertion force fell by about half.',
  body:
    'In two studies on human cadaver cochleae, coated arrays needed about 42 and about 50 percent less force to insert.',
  alt: 'Three panels of insertion force for uncoated and coated cochlear implant arrays in human cadaveric cochleae, nine per group. Peak insertion force in Bennion 2021 was 64.2 millinewtons uncoated and 37.0 coated, about 42 percent lower. Force variation in the same study was 89.9 millinewtons per second uncoated and 52.1 coated, about 42 percent lower. Peak insertion force in Peel 2024 was about 68 millinewtons uncoated and about 35 coated, about 50 percent lower.',
  caption:
    'Coated cochlear implant arrays needed about half the peak insertion force of uncoated arrays in two human cadaveric studies: about 42 percent less (Bennion 2021) and about 50 percent less (Peel 2024).',
  source:
    'Bennion DM, Horne R, Peel A, et al. Otology and Neurotology 2021;42(10):1476-1483, Fig 4A and 4B (means and SD from the text), doi:10.1097/MAO.0000000000003288; Peel A, Bennion D, Horne R, Hansen MR, Guymon CA. ACS Applied Bio Materials 2024;7:3124-3135, Fig 13A (values approximate, read from the published figure), doi:10.1021/acsabm.4c00156.',
};

export const W25 = {
  name: 'W25_sheep_impedance_components',
  alt: 'Three bar charts for sheep: total impedance, polarization impedance and access resistance of uncoated and coated arrays, at implantation and at four weeks. Coated arrays read lower in total impedance and access resistance at both times.',
  caption:
    'Total impedance, polarization impedance and access resistance of coated and uncoated human cochlear implant arrays in sheep, at implantation and at four weeks.',
  source:
    'Ben-Shlomo N, et al. Hearing Research 2026;474:109606, Fig 3B to 3D (bar heights approximate, read from the published figure; p values as printed). doi:10.1016/j.heares.2026.109606',
};

export const W26 = {
  name: 'W26_sheep_histology',
  alt: 'Three panels for sheep at four weeks: cell nuclei density, macrophage density and fibrosis at the round window, uncoated versus coated, with one line per sheep joining its uncoated and coated values. Pooled across three sheep, coated arrays had fewer nuclei, fewer macrophages and less fibrosis.',
  caption:
    'At the round window of the sheep cochlea, coated arrays had fewer cell nuclei, fewer macrophages and less fibrosis than uncoated arrays when the three sheep were pooled.',
  source:
    'Ben-Shlomo N, et al. Hearing Research 2026;474:109606, Fig 6E to 6G (bar and per-sheep values approximate, read from the published figure; pooled p values as printed). doi:10.1016/j.heares.2026.109606',
};

export const W28 = {
  name: 'W28_durability_peel',
  alt: 'Friction of coated and uncoated silicone. Panel A: uncoated vs coated, before and after three weeks in mice; coated silicone kept about 90 percent lower friction. Panel B: against steel and five animal tissues, coated silicone had at least 90 percent lower friction.',
  caption:
    'Friction of uncoated vs coated silicone, before and after three weeks in mice (panel A). Coated silicone kept about 90 percent lower friction after three weeks in mice, and at least 90 percent lower against steel and five animal tissues.',
  source:
    'Peel A, Bennion D, Horne R, Hansen MR, Guymon CA. ACS Applied Bio Materials 2024;7:3124-3135, Figs 4 and 5A (values approximate, read from the published figure; the at-least-90-percent statement is from the text). doi:10.1021/acsabm.4c00156',
};

export const W29 = {
  name: 'W29_bacteria_rats',
  alt: 'Charts of S. aureus on silicone implants in rats. At day 21, coated implants carried far fewer adherent bacteria and live colonies than uncoated implants. A coating kept in a rat for two weeks still resisted a fresh S. aureus challenge.',
  caption:
    'In rats challenged with S. aureus, coated silicone implants carried far fewer bacteria and live colonies at day 21, and a coating kept in a rat for two weeks still resisted a fresh S. aureus challenge.',
  source:
    'Shen N, Cheng E, Whitley JW, Horne RR, Leigh B, Xu L, Jones BD, Guymon CA, Hansen MR. ACS Applied Bio Materials 2021;4(2):1283-1293, Figs 7C, 7D and 8 (values approximate, read from the published figure; p values as printed). doi:10.1021/acsabm.0c01147',
};

export const W30 = {
  name: 'W30_crosslinker_tradeoff',
  alt: 'Charts against crosslinker percentage for the coating. More crosslinker makes the gel stiffer and less swollen. Protein, cell and friction benefits are strongest at about 5 to 15 percent crosslinker.',
  caption:
    'More crosslinker makes the gel stiffer and less swollen. Protein, cell and friction benefits are strongest at about 5 to 15 percent crosslinker.',
  source:
    'Jensen MJ, Peel A, Horne R, Chamberlain J, Xu L, Hansen MR, Guymon CA. ACS Biomaterials Science and Engineering 2021;7(9):4494-4502, Figs 3G, 4A, 4B, 5B (SBMA series; values approximate, read from the published figures; stiffness shown relative to the lowest cross-linker, baseline implied by the text, 50-fold rise; the 5 to 15 percent window is stated in the text). doi:10.1021/acsbiomaterials.1c00852',
};

export const W31 = {
  name: 'W31_bond_strength_vs_grafting_agent',
  alt: 'Shear bond strength of the zwitterionic film on silicone against grafting agent concentration. Strength rises until failure moves from the silicone interface into the gel, at 2.5 mg per mL.',
  caption:
    'Shear bond strength of the zwitterionic film on silicone rises with grafting agent concentration until failure moves from the silicone interface into the gel itself, at 2.5 mg/mL.',
  source:
    'Leigh BL, Cheng E, Xu L, Derk A, Hansen MR, Guymon CA. Langmuir 2019;35(4):1100-1110, Fig 6 (values approximate, read from the published figure and converted from N/m2 x 10^4 to kPa; failure thresholds from the text). doi:10.1021/acs.langmuir.8b00838',
};

export const W28a = {
  name: 'W28a_friction_after_explant',
  alt: 'Bar chart of the friction coefficient of uncoated and coated silicone, before and after three weeks implanted in mice. Coated silicone kept about 90 percent lower friction than uncoated silicone at both times.',
  caption:
    'Coated silicone kept about 90 percent lower friction than uncoated silicone after three weeks in mice, the same as before implantation.',
  source:
    'Peel A, Bennion D, Horne R, Hansen MR, Guymon CA. ACS Applied Bio Materials 2024;7:3124-3135, Figs 4 and 5A (values approximate, read from the published figure; the at-least-90-percent statement is from the text). doi:10.1021/acsabm.4c00156',
};

export const W34 = {
  name: 'W34_peek_bond_strength',
  alt: 'Two bar charts of lap-shear bond strength of the coating on PEEK, silicone and PVC. Panel A, as prepared (dry): PEEK at least 635 kilopascals, silicone about 131 and PVC about 349; a note on the PEEK bar says the gel tears before the bond lets go. Panel B, after a short water soak: PEEK about 129, silicone about 84 and PVC about 419.',
  caption:
    'Bond strength of the coating on PEEK is among the highest we measure. PEEK takes part in the grafting step, so no primer is needed, and the gel tears before the bond lets go.',
  source: 'ZwiCoat internal tests, 2025 to 2026',
};

/* W27 (rebuilt 2026-11-02): uncoated against coated only; the PEG-type control bar is gone from the chart. */
export const W27 = {
  name: 'W27_capsule_thickness_mice',
  alt: 'Two bar charts of scar capsule thickness in mice, uncoated against coated. Panel A, six weeks on flat silicone sheets: 82 micrometers uncoated and 27 coated. Panel B, one year on human cochlear implant arrays: 47 micrometers uncoated and 18 coated.',
  caption:
    'In mice, scar capsules were 67 percent thinner around coated silicone at six weeks and 62 percent thinner around coated human cochlear implant arrays at one year.',
  source:
    'Horne R, Ben-Shlomo N, Jensen M, et al. Acta Biomaterialia 2023;166:212-223, Figs 5D and 7I (means and p values from the text; SEM whiskers approximate, read from the published figure). doi:10.1016/j.actbio.2023.05.011',
};

export const W35 = {
  name: 'W35_wear_2500_passes',
  alt: 'Bar chart of friction relative to bare silicone, first and last 100 passes of a 2,500-pass wear test, by crosslinker percentage in the coating. At 2 to 5 and 13 percent the first and last values are both about 0.068, and at 31 percent both are about 0.10. At 50 and 67 percent they are between 0.19 and 0.26. Bare silicone is 1.0.',
  caption:
    'Coated silicone, rubbed under a 1 N load in saline for about 17 hours. Friction in the last 100 passes matched the first 100 and stayed at about 7 percent of bare silicone for the 2 to 13 percent crosslinker coatings.',
  source:
    'Peel A, et al. ACS Applied Bio Materials 2024;7:3124-3135, Fig 9 (values approximate, read from the published figure; n at least 4). doi:10.1021/acsabm.4c00156',
};

export const W36 = {
  name: 'W36_dry_and_rewet',
  alt: 'Two charts. Panel A: minutes to the first crack when a coating is dried while being bent every 5 minutes, 75 for Coating A and 47.5 for Coating B, both at 5 percent crosslinker. Panel B: friction coefficient of bare silicone (0.179) and of coatings at 2 to 5, 13, 20 and 31 percent crosslinker, never dried or dried 24 hours and re-wet 24 hours. Friction was unchanged after drying and re-wetting up to 20 percent crosslinker, and well below bare silicone at all four.',
  caption:
    'Coated silicone dried for 24 hours and re-wet for 24 hours returned to its original friction. Coatings dried while being bent every 5 minutes lasted 47 to 75 minutes before the first crack.',
  source:
    'Peel A, et al. ACS Applied Bio Materials 2024;7:3124-3135, Figs 7, 8 and 9 (values approximate, read from the published figures; Fig 7 n at least 3, Fig 8 n at least 4). doi:10.1021/acsabm.4c00156',
};

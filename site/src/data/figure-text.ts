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
    'Leigh BL, et al. Biomacromolecules 2017;18(8):2389-2401 (Fig 4 fibrinogen; Figs 6E, 7E, 8E cells on glass; fibrinogen and fibroblast values read from the published plots, astrocyte and Schwann cell values from the stated fold changes); Leigh BL, et al. Langmuir 2019;35(4):1100-1110 (Fig 7D fibrinogen; Fig 10D fibroblasts after 14 days in medium, plotted ratios used because the plotted absolute values conflict with the text); Jensen MJ, et al. ACS Biomaterials Science and Engineering 2021;7(9):4494-4502 (Figs 1G, 2G, 3G at 5 percent cross-linker; Fig 5A friction at 4 percent; values read from the published plots); Shen N, et al. ACS Applied Bio Materials 2021;4(2):1283-1293 (Fig 3 in vitro, Figs 7C, 7D rat explants at day 21, Fig 8 after 2 weeks in rats; values read from the published plots); Horne R, et al. Acta Biomaterialia 2023;166:212-223 (Fig 3F, mean of four cross-linker levels, new and after 6 months in mice; read from the published plot); Bennion DM, et al. Otology and Neurotology 2021;42(10):1476-1483 (Fig 1B, steel, ceramic and guinea pig dermis; text states more than 90 percent lower, p < 0.0001); Peel A, et al. ACS Applied Bio Materials 2024;7:3124-3135 (Fig 4 pristine and after 3 weeks in mice; Fig 5A six probes, bar shows the mean, range in the label; read from the published plots); Barrera G, et al. ACS Applied Polymer Materials 2026;8(18):16328-16338, doi:10.1021/acsapm.6c02510 (Fig 6 fibroblasts, text states more than 99 percent for low and about 90 percent for high cross-linker; Fig 4B friction, best group 2.5/2.5 percent).',
};

export const W04 = {
  /** Short source line for the home hero and the technology page; the full one is under `source`. */
  sourceShort:
    '10 measurements in mice, rats and sheep. Horne 2023, Acta Biomaterialia; Peel 2024, ACS Applied Bio Materials; Barrera 2026, ACS Applied Polymer Materials; Ben-Shlomo 2026, Hearing Research. Values read from the published figures; the basal-turn bar is not significant.',
  name: 'W04_fibrosis_by_study',
  alt: 'Horizontal bar chart of 10 measurements of scar capsule or fibrosis around coated surfaces compared with uncoated, in mice, rats and sheep, four weeks to one year, from four papers (Horne 2023, Peel 2024, Barrera 2026, Ben-Shlomo 2026). Reductions run from about 45 to about 85 percent. The sheep basal-turn bar, about 78 percent, is drawn hollow because it is not significant.',
  caption:
    'Less scar tissue around coated surfaces in mice, rats and sheep: percent reduction in fibrotic capsule or fibrosis, measurement by measurement. The hollow bar is not statistically significant.',
  source:
    'Horne R, et al. Acta Biomaterialia 2023;166:212-223 (Figs 5, 6G, 7I; flat-sheet and one-year values from the text, cylinder value approximate, read from the published figure); Peel A, et al. ACS Applied Bio Materials 2024;7:3124-3135 (Fig 3, values approximate, read from the published figure; text states over 60 percent); Barrera G, et al. ACS Applied Polymer Materials 2026;8(18):16328-16338, doi:10.1021/acsapm.6c02510 (Fig 7F, four coated groups, rats, 6 weeks, means read from the published plot; p < 0.0001 each versus uncoated); Ben-Shlomo N, et al. Hearing Research 2026;474:109606 (Fig 6G round window, p = 0.0101; Fig 5G basal turn, not significant; pooled values approximate, read from the published figure).',
};

/* Charts say "uncoated versus coated" with no chemistry in the image or the caption. Chemistry may appear in a source line. */

export const W07 = {
  name: 'W07_insertion_force',
  title: 'Insertion force fell by about half.',
  body:
    'Two cadaveric studies of coated cochlear implant arrays: peak insertion force fell about 42 percent (Bennion 2021, 64.2 to 37.0 mN, n = 9, p = 0.001) and about 50 percent (Peel 2024, about 68 to 35 mN, read from the figure).',
  alt: 'Three panels of insertion force for uncoated and coated cochlear implant arrays in human cadaveric cochleae, nine per group. Peak insertion force in Bennion 2021 was 64.2 millinewtons uncoated and 37.0 coated, about 42 percent lower (p = 0.001). Force variation in the same study was 89.9 millinewtons per second uncoated and 52.1 coated, about 42 percent lower (p = 0.03). Peak insertion force in Peel 2024 was about 68 millinewtons uncoated and about 35 coated, about 50 percent lower.',
  caption:
    'Coated cochlear implant arrays needed about half the peak insertion force of uncoated arrays in two human cadaveric studies: about 42 percent less (Bennion 2021) and about 50 percent less (Peel 2024).',
  source:
    'Bennion DM, Horne R, Peel A, Reineke P, Henslee A, Kaufmann C, Guymon CA, Hansen MR. Otology and Neurotology 2021;42(10):1476-1483, Fig 4A and 4B (means and SD from the text), doi:10.1097/MAO.0000000000003288; Peel A, Bennion D, Horne R, Hansen MR, Guymon CA. ACS Applied Bio Materials 2024;7:3124-3135, Fig 13A (values approximate, read from the published figure), doi:10.1021/acsabm.4c00156.',
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
  alt: 'Three panels for sheep at four weeks: cell nuclei density, macrophage density and fibrosis at the round window, uncoated versus coated, with one line per sheep joining its uncoated and coated values. Pooled across three sheep, coated arrays had fewer nuclei, fewer macrophages and less fibrosis. One sheep showed no difference in cells or macrophages.',
  caption:
    'At the round window of the sheep cochlea, coated arrays had fewer cell nuclei, fewer macrophages and less fibrosis than uncoated arrays when the three sheep were pooled. One sheep showed no difference in cells or macrophages.',
  source:
    'Ben-Shlomo N, et al. Hearing Research 2026;474:109606, Fig 6E to 6G (bar and per-sheep values approximate, read from the published figure; pooled p values as printed). doi:10.1016/j.heares.2026.109606',
};

export const W28 = {
  name: 'W28_durability_peel',
  alt: 'Friction of coated and uncoated silicone. Panel A: uncoated vs coated, before and after three weeks in mice; coated silicone kept about 90 percent lower friction. Panel B: against five guinea pig tissues and steel, coated silicone had at least 90 percent lower friction.',
  caption:
    'Friction of uncoated vs coated silicone, before and after three weeks in mice (panel A). Coated silicone kept about 90 percent lower friction, and had at least 90 percent lower friction against five guinea pig tissues and steel.',
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
  alt: 'Charts against cross-linker percentage for the coating. More cross-linker makes the gel stiffer and less swollen, while protein, cell and friction benefits are strongest at about 5 to 15 percent cross-linker.',
  caption:
    'For the coating, more cross-linker makes the gel stiffer and less swollen, while protein, cell and friction benefits are strongest at about 5 to 15 percent cross-linker.',
  source:
    'Jensen MJ, Peel A, Horne R, Chamberlain J, Xu L, Hansen MR, Guymon CA. ACS Biomaterials Science and Engineering 2021;7(9):4494-4502, Figs 3G, 4A, 4B, 5B (SBMA series; values approximate, read from the published figures; stiffness shown relative to the lowest cross-linker, baseline implied by the text, 50-fold rise; the 5 to 15 percent window is stated in the text). doi:10.1021/acsbiomaterials.1c00852',
};

export const W31 = {
  name: 'W31_bond_strength_vs_benzophenone',
  alt: 'Shear bond strength of the zwitterionic film on silicone against benzophenone grafting agent concentration. Strength rises until failure moves from the silicone interface into the gel, at 2.5 mg per mL.',
  caption:
    'Shear bond strength of the zwitterionic film on silicone rises with benzophenone grafting agent until failure moves from the silicone interface into the gel itself, at 2.5 mg/mL.',
  source:
    'Leigh BL, Cheng E, Xu L, Derk A, Hansen MR, Guymon CA. Langmuir 2019;35(4):1100-1110, Fig 6 (values approximate, read from the published figure and converted from N/m2 x 10^4 to kPa; failure thresholds from the text, 2.5 mg/mL for SBMA and 5 mg/mL for CBMA). doi:10.1021/acs.langmuir.8b00838',
};

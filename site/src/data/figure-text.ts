/*
  Alt text, captions and sources for the two charts that several pages share.
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

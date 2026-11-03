/*
  Short source lines, one per chart: citation plus figure numbers only.
  Copied from the source_short column of figures/MANIFEST.md and figures/MANIFEST-sbir.md
  (regenerate when the manifests change). Figure, InteractiveChart and the application
  pages display these; the full source strings stay in figure-text.ts and the frontmatter as the record.
*/
export const SOURCE_SHORT: Record<string, string> = {
  W01_experiment_timeline: "ZwiCoat Data archive",
  W02_lapshear_database: "ZwiCoat lap-shear database, 2017 to 2026",
  W03_ci_database_and_learning_curve: "ZwiCoat cochlear implant dip-coating database",
  W04_fibrosis_by_study: "Horne et al. 2023, Acta Biomaterialia, Figs 5, 6G and 7I; Peel et al. 2024, ACS Applied Bio Materials, Fig 3; Barrera et al. 2026, ACS Applied Polymer Materials, Fig 7F; Ben-Shlomo et al. 2026, Hearing Research, Fig 6G",
  W05_antifouling_and_friction: "Leigh et al. 2017, Biomacromolecules, Figs 4, 6E, 7E and 8E; Leigh et al. 2019, Langmuir, Figs 7D and 10D; Jensen et al. 2021, ACS Biomaterials Science and Engineering, Figs 1G, 2G, 3G and 5A; Shen et al. 2021, ACS Applied Bio Materials, Figs 3, 7C, 7D and 8; Horne et al. 2023, Acta Biomaterialia, Fig 3F; Bennion et al. 2021, Otology and Neurotology, Fig 1B; Peel et al. 2024, ACS Applied Bio Materials, Figs 4 and 5A; Barrera et al. 2026, ACS Applied Polymer Materials, Figs 4B and 6",
  W06_durability_timeline: "Shen et al. 2021, ACS Applied Bio Materials, Fig 8; Peel et al. 2024, ACS Applied Bio Materials, Figs 2 and 4; Ben-Shlomo et al. 2026, Hearing Research; Barrera et al. 2026, ACS Applied Polymer Materials, Fig 7; Horne et al. 2023, Acta Biomaterialia, Figs 2, 3F and 7",
  W07_insertion_force: "Bennion et al. 2021, Otology and Neurotology, Fig 4A; Peel et al. 2024, ACS Applied Bio Materials, Fig 13A; NIH SBIR Phase I dataset, Zenodo, doi:10.5281/zenodo.10459478",
  W08_impedance_sheep: "Ben-Shlomo et al. 2026, Hearing Research, Fig 3B",
  W09_accelerated_aging: "ZwiCoat internal study, accelerated aging",
  W10_substrate_evidence_matrix: "ZwiCoat Data archive; published studies",
  W11_sterilization: "ZwiCoat internal study, 2025",
  W12_numbers: "Ten peer-reviewed papers and three US patents (see W24); ZwiCoat patent schedule, 2025; Horne et al. 2023, Acta Biomaterialia, Figs 7 and 7I; Bennion et al. 2021, Otology and Neurotology, Fig 4A; Peel et al. 2024, ACS Applied Bio Materials, Fig 13A; NIH SBIR Phase I dataset, Zenodo; Ben-Shlomo et al. 2026, Hearing Research; bench studies in W05",
  W33_archive_numbers: "ZwiCoat Data archive counts, 2026",
  W13_claims_by_evidence_tier: "ZwiCoat evidence map, 2026",
  W14_formulation_sweep: "ZwiCoat internal study, 2026",
  W15_thickness_vs_cure: "ZwiCoat internal study, 2026",
  W16_ett_insertion_trials: "ZwiCoat internal study, 2026",
  W17_textured_implants: "Matros et al. 2021, Plastic and Reconstructive Surgery Global Open",
  W18_silver_foley_cauti: "Pickard et al. 2012, The Lancet (CATHETER trial)",
  W19_silver_ett_forest: "Tokmaji et al. 2015, Cochrane Database of Systematic Reviews; Yang et al. 2024, Critical Care",
  W20_cgm_delay: "McClatchey et al. 2019, Diabetes",
  W21_mucus_flow: "Horne et al. 2025, Laryngoscope Investigative Otolaryngology",
  W24_publication_timeline: "Ten peer-reviewed papers, 2017 to 2026; three University of Iowa dissertations; US patents 11,525,069, 11,814,526 and 12,116,498",
  W25_sheep_impedance_components: "Ben-Shlomo et al. 2026, Hearing Research, Figs 3B to 3D",
  W26_sheep_histology: "Ben-Shlomo et al. 2026, Hearing Research, Figs 6E to 6G",
  W27_capsule_thickness_mice: "Horne et al. 2023, Acta Biomaterialia, Figs 5D and 7I",
  W28_durability_peel: "Peel et al. 2024, ACS Applied Bio Materials, Figs 4 and 5A",
  W28a_friction_after_explant: "Peel et al. 2024, ACS Applied Bio Materials, Fig 4",
  W29_bacteria_rats: "Shen et al. 2021, ACS Applied Bio Materials, Figs 7C, 7D and 8",
  W30_crosslinker_tradeoff: "Jensen et al. 2021, ACS Biomaterials Science and Engineering, Figs 3G, 4A, 4B and 5B",
  W31_bond_strength_vs_grafting_agent: "Leigh et al. 2019, Langmuir, Fig 6",
  W34_peek_bond_strength: "ZwiCoat internal tests, 2025 to 2026",
  W35_wear_2500_passes: "Peel et al. 2024, ACS Applied Bio Materials, Fig 9",
  W36_dry_and_rewet: "Peel et al. 2024, ACS Applied Bio Materials, Figs 7, 8 and 9",
  W37_ci_insertion_synthetic: "NIH SBIR Phase I dataset, Zenodo, doi:10.5281/zenodo.10459478",
  W38_ett_insertion_force: "ZwiCoat internal study, 2026; raw data in the NIH SBIR Phase I dataset, Zenodo, doi:10.5281/zenodo.10459478",
};

/** The short source for a chart name (e.g. "W07_insertion_force"), if the manifests list one. */
export const shortSourceFor = (name: string): string | undefined => SOURCE_SHORT[name];

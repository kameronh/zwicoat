# ZwiCoat website v2: planning and assets

Start here. Built 2026-10-29 as Phase 0 of the zwicoat.com redesign.

```
CLAUDE.md            rules for any agent working here (Arial, no cartoons, sources, video slot)
PLAN.md              site map, phases, gates, decisions for Kam
DESIGN-BRIEF.md      reference-site notes and the three design directions (pick one at Gate 0)
content/             every page's copy: home, technology, evidence, partner, publications-and-about,
                     claims-rules.md, applications/ (nine summarized white papers)
figures/
  build_figures.py   builds every chart (Arial, validated palette); re-run after data changes
  png/  svg/         the 16 charts (W01 to W16), 2x PNG and SVG
  data/              JSON behind the charts and the interactive versions
  interactive/       lapshear-explorer.html (prototype, static fallback built in)
  MANIFEST.md        caption and source for every chart
data/                experiments_by_year_tag.csv (archive index behind W01)
assets-staging/
  deck-images/       46 unique images pulled from the six 2026 MedTech decks, MANIFEST.csv
```

To preview the interactive prototype: open `figures/interactive/lapshear-explorer.html`
through a local server (for example `python -m http.server` in `figures/`) because it
fetches `data/W02_lapshear_groups.json`.

Decisions needed from Kam are listed at the end of PLAN.md.

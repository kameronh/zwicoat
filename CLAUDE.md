# ZwiCoat website v2 (zwicoat.com redesign)

Owner: Kam (CTO). This folder is the planning and asset home for the
redesign of zwicoat.com. The current site lives in
`C:\Users\Kameron\PycharmProjects\ZwiCoat website` (React 18 + Vite,
styled-components, deployed as static files on the shared EC2 box); its
CLAUDE.md has the deploy details. v2 replaces it.

Read, in order: `PLAN.md` (phases and gates), `DESIGN-BRIEF.md` (Phase 0,
the three proposed directions), `content/` (every page's copy),
`figures/MANIFEST.md` (every chart, with sources).

## Hard rules (Kam, 2026-10-29)

1. **Arial for every plot.** Charts are rebuilt by
   `figures/build_figures.py`; never hand-edit a PNG. The page font may
   differ (see the brief) but chart text is Arial.
2. **No AI-generated cartoons** or stock-looking illustrations. Imagery is
   real: photographs of coated devices, micrographs, histology, and
   charts. The deck images in `assets-staging/deck-images/` are the
   candidate pool only (see FIGURE-APPROVAL.md); anything new must come from the lab. Do NOT use the
   CAD render of the dip-coating jig (deck image GENERAL_s09); Kam wants
   a real video of the process there. The video does not exist yet:
   build a `ProcessVideo` slot with a poster still and drop the clip in
   when it arrives (see DESIGN-BRIEF.md, image requests).
3. **Published first; internal data only when broadcast-worthy (Kam,
   2026-10-29, revised the same evening).** Every chart and number comes
   from a published paper, dissertation, patent or public document, OR from
   internal data that the company already shows in its MedTech decks and
   that is not sensitive. Never on the site: formulation ratios and recipes
   (W and C values, crosslinker and photoinitiator doses), accelerated-aging
   mass-loss rates, process yields and scores, and results from manuscripts
   in preparation unless Kam approves the specific figure. Allowed internal
   items so far: sterilization compatibility (W11), the substrate evidence
   matrix (W10), the lap-shear database by substrate without formulation
   fields, archive counts when each carries a takeaway, lab photographs and
   videos from the archive when they are good. Polyurethane IS a tested
   substrate (the CIVCO probe covers are polyurethane). Published figure
   panels (micrographs) are not copied from the papers: use the lab's own
   original images from the archive with a fresh crop and labels, so no
   publisher permission is needed. `FIGURE-APPROVAL.md` is the ledger.
4. **Every number on the site has a source.** Numbers come from
   `figures/data/` or `content/` with a citation; the evidence map in the
   data project (`ZwiCoat Data Project\ZwiCoat - insights\holistic\evidence-map`)
   is the ledger. No clinical claims: performance claims only (see
   `content/claims-rules.md`).
5. **Mostly static.** Interactive charts are allowed where they earn it
   (Kam, 2026-10-29: "feel free to do a few more"; the original cap was
   two). Each one has a static PNG fallback that renders if JavaScript is
   off. Everything else is a static image.
6. **Different from both the current site and a default AI-looking site.**
   See the brief: no purple gradients, no glassmorphism cards in a grid of
   three, no hero with a centered headline over a blurred blob.
7. Plain language, no em-dashes in copy. One idea per sentence.

## Where things come from

- White papers (the source of each application page):
  `G:\My Drive\9 Zwitterion\Claude Code projects and misc files\misc claude code (Zwitterion)\26.10 MedTech 2026\white papers\final\`
  (GEN, GI, IC, OV, VA) and `C:\Users\Kameron\Zwicoat Dropbox\ZwiCoat White Papers\`
  (tissue expanders, neurostimulators/BCI).
- Decks: `C:\Users\Kameron\Zwicoat Dropbox\ZwiCoat Slide Decks\2026\` (the six
  MedTech decks; images extracted to `assets-staging/deck-images/`).
- Data: the Dropbox archive `C:\Users\Kameron\Zwicoat Dropbox\ZwiCoat Data\`
  (read-only here) and the data project's evidence map and goal reports.

## Phases (detail in PLAN.md)

0. Inspiration and three design directions (this folder, done first; Kam picks one).
1. Content lock: every page's copy and figure list approved.
2. Build: new repo from a clean Vite + React (or Astro) scaffold, the
   chosen direction's design system, static figures, two interactive charts.
3. Review on a staging URL; accessibility and mobile pass.
4. Launch: swap the build on the EC2 box; redirects from old routes.

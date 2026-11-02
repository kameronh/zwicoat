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

## Editorial rules (Kam, 2026-11-02; apply to every page)

- **Product name is ZwiCoat.** "ZwiGuard" is retired. The company is ZwiCoat
  Materials Innovations; the coating is ZwiCoat; prefer "coated" and
  "uncoated" in comparisons.
- **No monomer names in prominent copy.** Do not write SBMA, CBMA,
  sulfobetaine or carboxybetaine in headlines, first sentences or chart
  labels. Rare exceptions where the chemistry is the point (W30 keeps both
  series), never on the home page.
- **Do not use the word "benzophenone"** on the site. Say "grafting agent".
  Axis: "Grafting agent concentration (mg/mL)".
- **Internal, unpublished sources get the minimum citation**: "ZwiCoat
  internal study, 2025". No scientist names, no partner or customer names.
- **Company website, not a lab report.** Remove non-significant bars and
  the sentences that explain them, caveats about sample overlap, p values in
  headlines, and anything that only a reviewer would want. Headers make a
  positive, plain statement ("Compatible with multiple sterilization
  methods"), not a tally ("Seven of eight cycles ...").
- **Hide what does not exist yet.** No "coming next", "not shown yet" or
  empty video slots. The process-video slot stays hidden until the clip
  exists.
- **Regulatory**: one brief, optimistic sentence on each application page
  only; nothing on the home page or technology page.
- **Every sentence must make sense on its own and connect to its
  neighbour**; delete or rewrite any that does not ("Silicone is published.
  Your material is the feasibility round." fails).
- **Vary sentence length and tone**; no long runs of identical short
  sentences; keep paragraphs short.
- **Application order**: neural interfaces, tissue expanders and breast
  implants, airway tubes, vascular access, indwelling catheters, PEEK and
  orthopedic, sensors, ENT and feeding tubes, GI stents.
- Horne dissertation year is 2024. The sheep work runs to six months.

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

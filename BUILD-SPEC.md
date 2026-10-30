# Build spec: zwicoat.com v2 (Phase 2)

Written 2026-10-29 by the lead session. Workers build from this file; the
lead reviews every deliverable in the browser before the next step starts.
Read CLAUDE.md first. Its six hard rules apply to every line of code here.

## Status note (2026-10-29, later the same day)

Kam ruled that only published data may appear on the site. The figure and
image assignments below are the Phase 0 set and are NOT approved; see
FIGURE-APPROVAL.md. Workers keep the page structure and component contract
exactly as written; the lead swaps figure names and images at review once
the published-only set (W24 onward) exists.

## Decisions taken (Kam can overturn any of these at review)

| Decision | Choice | Why |
|---|---|---|
| Direction | C "Evidence first" for home and evidence; B "Blueprint" spec strip on application pages | The brief's recommendation. Tokens are isolated in one file so a reskin to A is a one-file change. |
| Framework | Astro (static output, no React) | Pages are static; the two interactive charts are plain TypeScript modules, not framework islands. Output is a `dist/` folder of HTML, served by the same Apache config as today. |
| Application pages | All nine | Content exists for all nine. |
| Lap-shear explorer | Full (430 groups, four filters) | It is the proof of depth. |
| Deck illustrations (s19, s32, s33, s35, s37, s41, s43, s44, s01, s03) | Excluded | They are drawn illustrations, which rule 2 forbids. Kam decides at review whether any come back. |
| Deck charts (s06, s10, s11, s13, s18, s29, s34, s36, s38, s40_2, s45) | Rebuilt in Arial by build_figures.py (W17 to W22) | Rule 1. The deck PNGs are never placed on the site. |
| Contact form | Static form posting to a form endpoint set by env var; mailto fallback when unset | The current site is a mailto link only. Kam picks the endpoint (Formspree or similar) before launch. |
| Fonts | Public Sans (body and headings, self-hosted via @fontsource), JetBrains Mono (labels, sources, spec values) | Not Inter, not system-ui, so it does not read as a default AI site. Charts stay Arial. |

## Deployment (same as the current site)

Astro is a static site generator. `npm run build` writes a `dist/` folder of
plain HTML, CSS and JS. On the EC2 box the steps are unchanged from the
current site's CLAUDE.md: `git pull`, `npm run build`, Apache serves `dist/`.
Astro writes `/route/index.html` for every page, so Apache serves the routes
natively and `FallbackResource /index.html` is no longer needed (harmless if
left). Old routes (/about, /technology, /contact, /fcoi) keep their paths.
No database and no S3 are required; the form endpoint is an env var so it
can point at a third-party form service now and at a small endpoint on the
box later.

## Folder layout

```
ZwiCoat website v2/
  site/                      the Astro project (this spec builds it)
    public/figures/          copied from ../figures/png and ../figures/svg (never edited here)
    public/images/           real photographs and micrographs from assets-staging (renamed, see below)
    public/data/             JSON for the two interactive charts (copied from ../figures/data)
    src/styles/tokens.css    every color, font, size, radius, shadow: the only place they are defined
    src/styles/global.css    reset, type scale, prose, utilities
    src/layouts/Base.astro   head, nav, footer, skip link, meta
    src/components/          the component set below
    src/content/applications/*.md   nine pages, frontmatter + body
    src/data/publications.json, team.json, applications-index.json
    src/pages/               index, technology, evidence, applications/[slug], applications/index,
                             partner, publications, about, contact, fcoi
    src/scripts/lapshear.ts, timeline.ts   the two interactive charts
```

## Design tokens (src/styles/tokens.css)

```
--paper: #FCFCFB        page background (never pure white)
--paper-2: #F3F5F7      panel background
--ink: #141A1F          headings, body
--ink-2: #4A5058        secondary text
--muted: #7A8089        captions, source lines
--line: #E6E8EA         hairlines
--blue: #0E7FC4         brand, "coated", links, the one accent
--blue-deep: #0A5F94    hover, large flat panels
--blue-tint: #E7F2FA    tinted backgrounds behind figures
--orange: #C9711A       second series only when a chart needs it (never decorative)
--plum: #7B4FA6         third series only
--font-sans: "Public Sans", system-ui, sans-serif
--font-mono: "JetBrains Mono", ui-monospace, monospace
--measure: 68ch         max prose width
--container: 1200px
--radius: 4px           small; no pill buttons, no 16px card radii
--shadow: none          flat design; depth comes from hairlines and tint, not shadows
```

Type scale (rem): 0.75 (label), 0.875 (caption, source), 1 (body), 1.25 (lead),
1.75 (h3), 2.5 (h2), 3.5 to 5 fluid (h1, display numerals). Headings weight
700, letter-spacing -0.02em. Labels in mono, uppercase, 0.75rem, letter-spacing
0.08em, color --muted.

Forbidden (rule 5): gradients, glassmorphism, blurred blobs, drop-shadowed
card grids of three, centered hero headline over an image, rounded pill
buttons, emoji icons, icon libraries. Allowed: hairlines, flat blue panels,
large numerals, real photographs with hairline frames, mono labels.

## Components (src/components)

Each is an .astro file with the props listed. Workers B, C and D use these and
do not modify them; if one needs a change, the worker reports it to the lead.

- `Nav.astro`: logo (text wordmark "ZwiCoat" in sans 700 plus the drop mark
  from the current site's `public/edited-logo.png`, recolored to --blue if
  needed), links Technology, Evidence, Applications (dropdown listing the nine
  pages, opens on hover and on click, closes on Escape, fully keyboard
  reachable), Partner with us, About. Right side: "Send us parts" button
  (links /partner#form). Mobile: a disclosure menu, no hamburger icon font;
  use an inline SVG. Sticky at top with a hairline bottom border.
- `Footer.astro`: four columns (Company, Applications, Evidence, Contact),
  address, "ZwiGuard is a trademark of ZwiCoat Materials Innovations, LLC",
  FCOI link, University of Iowa and NIH SBIR text lines (no logos until
  rights are confirmed).
- `Hero.astro` (home only): two-column at desktop. Left: eyebrow label
  (mono), h1, lead paragraph, two buttons. Right: `<Figure>` of
  W04_fibrosis_by_study with its caption. On mobile the figure follows the
  text. No background image.
- `Figure.astro` props: `name` (e.g. "W04_fibrosis_by_study"), `alt`,
  `caption`, `source`, `width` (px of the 1x render, default 1000),
  `format` ("png" default or "svg"). Renders `<figure>` with `<img>`
  loading="lazy" decoding="async" width/height set, the caption in body
  size and the source line in mono --muted prefixed "Source:". Static PNGs
  are the 2x files in public/figures.
- `Photo.astro` props: `src`, `alt`, `caption`, `credit`, `aspect`
  (e.g. "16/9"). Hairline frame, object-fit cover.
- `StatTiles.astro` props: `items` [{value, label}], `columns` (3 or 6).
  Flat tiles on --paper-2, display numerals in --blue, label in --ink-2.
  No borders between tiles except a hairline grid.
- `ClaimRow.astro` props: `label` (mono eyebrow), `title`, `body` (slot),
  `reverse` (boolean). Two columns: text 5/12, figure 7/12 (slot). Stacks on
  mobile. This is the Direction C building block.
- `SpecStrip.astro` props: `items` [{label, value}]. A hairline-ruled row
  (wraps to 2 columns on mobile) with mono labels above sans values. Used at
  the top of every application page.
- `ApplicationCard.astro` props: `slug`, `title`, `stat`, `statLabel`,
  `image`, `alt`. Photo on top (aspect 4/3), title, the one number large,
  its label in mono. Hairline frame, no shadow.
- `CTABand.astro` props: `title`, `body`, `button` {text, href}. Flat
  --blue panel, white text, one button (white outline). Appears on every page
  above the footer.
- `ProcessVideo.astro` props: `poster`, `src` (optional), `caption`. A
  16:9 slot. If `src` is set: `<video autoplay muted loop playsinline
  poster>`; else the poster `<img>` with the caption. The layout must not
  change when `src` is added later.
- `Steps.astro` props: `steps` [{n, title, body}]. Numbered, mono numerals,
  hairline between.
- `Callout.astro` props: `label`, `title`, `href`. The published-paper
  callout (Silq's idea): mono label "Published", title, journal, link.
- `References.astro`: `<details>` with a mono summary "References (n)" and
  an ordered list slot.
- `Prose.astro`: wrapper applying the prose styles to rendered markdown.
- `ContactForm.astro`: fields name, organization, email, device type
  (select: the nine families + other), material (select: silicone, PVC,
  polyurethane, PEEK, other), message. `action` from
  `import.meta.env.PUBLIC_FORM_ENDPOINT`; if unset, render a mailto link
  with the same fields in the body and hide the form. Honeypot field. No
  file upload.

## Pages

### / (home)

1. Hero: eyebrow "Zwitterionic hydrogel coating for medical devices";
   h1 "The surface the body ignores."; lead = home.md subhead; buttons
   "See the evidence" (/evidence) and "Send us parts" (/partner#form);
   figure W04.
2. StatTiles, six: 191, 1,156, 468, 136, 9 + 3, 10 (labels from
   figures/data/W12_numbers.json). Line under: "Every number on this site
   traces to a study or a dataset in our archive."
3. Four ClaimRows (alternate `reverse`): Less scar (W04 is already in the
   hero, so use the Horne 2023 histology photo `histology-pdms-capsule.jpg`
   here), Lower impedance (W08), Easier insertion (W07), Fewer bacteria and
   less friction (W05). Copy from content/home.md, one claim per row with
   its study named.
4. "It stays on": ClaimRow with W06.
5. ProcessVideo slot: poster `coated-array.jpg`, caption "Automated dip
   coating: one step, about a minute per part. Video coming."
6. Applications: a 3-column grid of nine ApplicationCards (order from
   home.md). Stats per card are in src/data/applications-index.json.
7. Steps: the three steps from home.md "How we work together".
8. Credibility strip: text only. "University of Iowa spin-off. NIH SBIR
   Phase I and Phase II. US patents 11,525,069; 11,814,526; 12,116,498.
   Nine peer-reviewed papers."
9. CTABand.

### /technology

Content from content/technology.md, in this order: opening; how it works
(one inline SVG line diagram drawn in the site's style: device surface,
covalent bond ticks, hydrogel layer with +/- pairs, bound water dots, three
arrows bouncing off; no cells drawn as cartoons, use labeled dots); what it
does (four Figures W05, W04, W07, W08 in ClaimRows); it stays on (W06, W11,
W09); substrates (W10, W02 static); process (ProcessVideo, W15, W03);
compared with other coatings (an HTML table from the GEN white paper
summary in technology.md); regulatory paragraph; CTABand.

### /evidence

Sections from content/evidence.md. Section 1 holds the interactive
timeline (W01), section 7 the interactive explorer (W02). Every other
figure is a static `<Figure>`. Each section has a mono section number and
a sticky h2 on desktop. The publications list at the bottom reuses the
publications component. The footer note from evidence.md is rendered
verbatim.

### /applications and /applications/[slug]

Index: short intro plus the nine ApplicationCards. Each page renders from
`src/content/applications/<slug>.md`:

Frontmatter: `title`, `slug`, `order`, `devices`, `substrates`, `thickness`,
`sterilization`, `regulatory`, `evidence`, `heroFigure` (the one chart that
matters for that device), `cardImage`, `cardStat`, `cardStatLabel`,
`figures` (list of {name|src, caption, source}), `sources` (list of strings).

Template order: h1 and one-sentence standfirst; SpecStrip from frontmatter;
hero Figure; "The problem" (prose); "What ZwiGuard does here" (prose with
the figures interleaved, one real image where one exists); "Why it drops in";
"How to start" with CTABand text pointing to /partner#form; References.
Body copy comes from content/applications/*.md, lightly edited to flow;
every number keeps its citation. Hero figure per page: neural W08,
expanders W04, vascular W05, indwelling W05, GI W05, PEEK W02, airway W16,
sensors W04, ENT W21 (new, see figures).

### /partner, /publications, /about, /contact, /fcoi

From content/partner.md and content/publications-and-about.md. Contact page
is the ContactForm plus address and email. FCOI: copy the current site's
FCOI page text verbatim (src/pages/FCOI.jsx of the current site) and link
the PDF (copy `public/ZCMI_FCOI_Policy.pdf` over). Publications: list from
src/data/publications.json (nine papers with DOI links; take the six links
from the current site's data.js and add the three missing DOIs from
content/publications-and-about.md), theses, manuscripts in preparation,
patents. About: four bios shortened to about 80 words each with a
`<details>` "Read more" holding the full text from the current site's
data.js; team photos copied from the current site.

## Images (public/images)

Copy and rename from assets-staging/deck-images. Only these; nothing else
from the pool goes on the site.

| new name | source file | use |
|---|---|---|
| coated-array.jpg | GENERAL_combined_s26_0 | hero poster, neural card, process video poster |
| expander-impact.jpg | GENERAL_combined_s30_2 | expanders page |
| expander-coated.jpg | expanders_s12_9 | expanders card |
| ett-coated.png | expanders_s12_8 (the coated ET tube cutout) | airway card and page |
| ett-panel.png | GENERAL_combined_s39_0 | airway page (crop to panels A and C if simple; otherwise whole) |
| histology-pdms-capsule.jpg | GENERAL_combined_s05_1 | home, expanders, sensors (Horne 2023 Fig 5; credit line required) |
| histology-array-1yr.jpg | GENERAL_combined_s12_3 | neural, PEEK (Horne 2023 Fig 7; credit line required) |
| histology-sheep.jpg | airway_s23_6 (the Ben-Shlomo cochlea panels) | neural, evidence (open access, CC BY; credit line) |
| histology-trachea.jpg | GENERAL_combined_s40_1 | airway (manuscript in preparation; credit "ZwiCoat, unpublished") |
| stripes-protein.png, stripes-cells.png | GENERAL_combined_s04_2, s04_3 | technology, vascular, catheters (Leigh 2019 pattern micrographs) |

Cards without a real device photo (vascular, indwelling, GI, sensors, ENT)
use a tinted panel with the device family name in large type and the one
number, not a placeholder image and not an icon.

## The two interactive charts

Both are vanilla TypeScript modules in src/scripts, imported by the evidence
page with `<script>`. Both render into an SVG next to a `<noscript>` image
and also swap in the static PNG if the JSON import fails. Data is imported
at build time (Astro inlines it), not fetched.

1. Lap-shear explorer: port figures/interactive/lapshear-explorer.html as
   is (filters substrate, year, W, failure mode; tooltip; table view), in
   the site tokens. Static fallback W02.
2. Timeline: W01 bars from figures/data/W01_timeline.json; hovering a bar
   segment shows a tooltip with year, category, count and the scientists
   active that year (from data/experiments_by_year_tag.csv, aggregated at
   build time into public/data/W01_people.json by a small script in
   figures/). Clicking a year highlights the publications from that year in
   the list below. Static fallback W01.

## New figures (worker E, figures/build_figures.py)

Add these, same style as W01 to W16, data typed into the script with the
source in a comment and in the manifest. Values come from the deck charts
and the white papers (paths in CLAUDE.md).

- W17_textured_implants: textured share of US cases 2016 vs 2019, cosmetic
  18 to 2 percent, reconstructive 41 to 8 percent. Source: expanders white
  paper / deck slide 29 citation.
- W18_silver_foley_cauti: CATHETER trial, symptomatic CAUTI by 6 weeks:
  standard PTFE 12.6, silver alloy 12.5, nitrofural 10.6 percent, n = 7,102.
  Source: Pickard 2012 Lancet (cite as in IC white paper).
- W19_silver_ett_forest: risk ratios with 95 percent CI: silver ETT VAP 0.64
  (0.43 to 0.96), mortality 1.09 (0.93 to 1.29); metal-coated ETTs VAP 0.71
  (0.54 to 0.95), mortality 1.05 (0.86 to 1.27). Source as in the airway deck.
- W20_cgm_delay: time to peak signal, blood 2 min (1 to 3), implanted CGM
  24 min (17 to 31). Source: McClatchey 2019 as cited in the sensors deck.
- W21_mucus_flow: Horne 2025: tilt to start flow on sheets (saline and 5
  percent mucus about 0 vs 40 to 45 degrees; 10 percent mucus under 10 vs
  30) and in 2.64 mm tubes (31 vs 48 degrees); plug clearance median 22.5
  vs 30 min. Two panels.
- W22_sheep_6month: the six-month cohort summary, normalized impedance
  reductions 61.9 (saline), 58.5 (implanted), 53.7 (6 months) percent,
  p < 0.001, labeled "manuscript in preparation". Bars, not the boxplot,
  since raw points are not in the archive.
- W23_trachea_submucosa: rat tracheal study, submucosal thickness no tube
  about 130, uncoated ETT about 255, coated ETT about 85 micrometers, with
  the p values from deck slide 40 (p = 0.011 coated vs uncoated).
  "Manuscript in preparation".

Also write figures/build_people.py that aggregates
data/experiments_by_year_tag.csv into figures/data/W01_people.json:
`{year: {scientists: [...], total: n, by_category: {...}}}` using the same
category mapping as W01 in build_figures.py.

## Worker split and order

- A (first, alone): scaffold site/, tokens, global styles, Base layout, Nav,
  Footer, every component above, the home page, copy figures and images,
  `npm run build` clean, `npm run dev` for the lead to review.
- E (parallel with A, touches only figures/): W17 to W23 and build_people.py.
- After the lead approves A: B (technology, partner, publications, about,
  contact, fcoi), C (applications collection, index and nine pages), D
  (evidence page and the two interactive charts). B, C and D add files only;
  they do not edit tokens.css, global.css or existing components.
- Lead: browser review of every page at 1280 and 390 px, claims check
  against content/claims-rules.md, Lighthouse.

## Definition of done for every worker

- `npm run build` passes with no warnings about missing images.
- No console errors on the pages touched.
- Every figure has alt, caption and a source line.
- No em-dashes in copy (grep for the character).
- No text in images other than the chart PNGs and the histology panels.
- Report back: files added, anything in the spec that could not be done
  and why, and any shared-component change requested.

## Published-only figure map (added later on 2026-10-29; supersedes the figure names in the page recipes above)

Allowed charts: W04, W05, W06, W07, W08 (rebuilt, published series only), W12
(public-fact tiles), W17 to W21 (literature), W24 to W31 (from the nine
papers). Held until Kam approves: W01, W02, W03, W09, W10, W11, W13, W14,
W15, W16, the lap-shear explorer, and every deck photograph. Allowed images:
`histology-sheep.png` (CC BY, credit Ben-Shlomo et al. 2026, Hearing
Research); the two Horne 2023 panels and the Leigh 2019 stripes only after
reuse is confirmed (leave the slot with a PENDING APPROVAL comment).

| page | figures in order |
|---|---|
| / | hero W04; tiles W12; claim rows W27, W08, W07, W05; stays on W06; process slot (neutral poster); applications grid (tinted panels, no photos); steps; credibility; CTA |
| /technology | SVG diagram; W05, W27, W07, W08; W06, W28; W31 (bond strength on silicone), W30 (tunable window); process slot; comparison table; regulatory |
| /evidence | 1 the record: interactive W24 timeline + W12; 2 scar: W04, W27, W26, histology-sheep; 3 impedance: W08, W25; 4 insertion and friction: W07, W28; 5 bacteria: W05, W29; 6 durability: W06, W28 (panel reference only, not repeated; link up); 7 adhesion and tuning: W31, W30; 8 every in-vivo result: interactive study browser (W32 data, fallback W04); publications; footer note |
| /applications/neural-interfaces | hero W25; then W27 (B panel), W07, W26, histology-sheep |
| /applications/tissue-expanders | hero W27; then W17, W04, W06, W29 |
| /applications/vascular-access | hero W05; then W29, W06, W31 |
| /applications/indwelling-catheters | hero W18; then W05, W29, W21 |
| /applications/gi-stents | hero W21; then W05, W29, W06 |
| /applications/peek-and-orthopedic | hero W29; then W05, W27, W31 (no PEEK data are published; the page says PEEK bonding is measured in the feasibility round) |
| /applications/airway | hero W19; then W21, W07, W05, W29 (ETT insertion-force and tracheal results are manuscripts in preparation and are not stated) |
| /applications/sensors | hero W20; then W27, W04, W06 |
| /applications/ent-tubes | hero W21; then W05, W29 |

Interactive charts (two, evidence page only):

1. **Publication timeline** (data `figures/data/W24_publications.json`):
   W24 rendered as SVG; hover a marker for title, journal, one-line finding
   and open-access flag; click a marker to open the DOI. Static fallback W24.
2. **In-vivo study browser** (data `figures/data/W32_invivo_studies.json`):
   each published in-vivo comparison as a dot, x = duration (log, days),
   y = percent change coated vs uncoated, color = species, shape or filter =
   metric (capsule, fibrosis, cells, bacteria, impedance, friction); hover
   for the paper, device, n and p; filters for species and metric. Static
   fallback W04.

The lap-shear explorer prototype stays in `figures/interactive/` and is not
wired into the site.

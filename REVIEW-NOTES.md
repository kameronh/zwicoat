# Lead review notes (running log)

Browser review at 1280 and 375 px on the local dev server. Items here feed
the polish worker once all page workers have finished.

## Home (worker A) 2026-10-29

- Passes the design gate: evidence-led editorial layout, no template look,
  phone layout holds.
- CTABand uses --blue-deep for contrast (accepted).
- Figures and photos on this page are the Phase 0 set; swap to the
  published map in BUILD-SPEC.md once W24 to W31 exist: hero W04 (rebuilt),
  claim rows W27, W08, W07 (rebuilt), W05 (rebuilt); application cards all
  tinted panels (no internal photos); process poster neutral panel; tiles
  from the new W12_numbers.json.
- Node: Astro 7 needs Node 22.23.4 or newer on the EC2 box (local is 24).

## Technology, partner, publications, about, contact, fcoi (worker B)

- Page header h1 sits in a narrow column with nothing beside it on
  /partner, /publications and /contact, so it wraps one word per line at
  1280 px. Fix in the shared page-header styling: full container width
  with max-width about 18ch for display headings when no figure is beside.
- ProcessVideo with no `src` renders a large flat pale panel that reads as
  a broken image. Add a mono label inside the panel ("Process video:
  coming") and an `alt` prop; the layout must still not change when a clip
  is added.
- /technology places `histology-array-1yr` (Horne 2023, Elsevier): keep
  behind a PENDING APPROVAL comment until reuse is confirmed; use
  `histology-sheep` (CC BY) or W27 in that slot meanwhile.
- /technology W04 and W05 captions assume the pre-rebuild series; re-read
  after worker F.
- /technology "Less friction, easier insertion" row has no figure; place
  the rebuilt W07 there.
- /technology: once W28, W30, W31 exist, place them per the figure map.
- Publications: Horne 2025 is CC BY-NC-ND; the "open access" badge is
  accurate but add "(no derivatives)" nowhere on the site; fine as is.
  Horne dissertation year shows 2024 from the title page; confirm with Kam.
- Stripe micrographs credit (Leigh 2019 vs Leigh 2017) unconfirmed; they
  are not placed on any page yet. Keep it that way until confirmed.

## Open questions for Kam (collected)

1. Class A aggregate counts (W01, old W12 tiles): keep or hold.
2. Internal photographs (coated array, expander, ET tube): hold or allow.
3. Hero headline choice.
4. Form endpoint (Formspree or an endpoint on the box).
5. Horne 2023 figure reuse (Elsevier) and Horne 2025 image reuse (NC-ND).
6. Horne dissertation year (2023 in content, 2024 on the title page).
7. Patent 12,116,498: confirm issued; it is not in the patents folder.
8. Footer address and phone are copied from the current site; confirm.
9. Deck illustrations: any to bring back.

## Exact polish items found by grep (home, technology, Hero)

- `components/Hero.astro` lines 7 to 9: alt says "six studies in mice, rats and sheep" and source names the dual-network manuscript; rewrite to the rebuilt W04 (five measurements, mice and sheep; sources Horne 2023, Peel 2024, Ben-Shlomo 2026).
- `pages/index.astro` line 33 and `pages/technology.astro` line 89: "45 to 84 percent" is now "45 to 85 percent" (W04 rebuilt); reword to "about 45 to 85 percent".
- `pages/index.astro` lines 47 and 48: delete the ETT and probe-cover sentences; W07 is now Bennion only (peak force 64.2 to 37.0 mN, force variation 89.9 to 52.1 mN/s, n = 9, p = 0.001 and 0.03); rewrite the alt.
- `pages/index.astro` line 51: "83 to 97 percent" is now "88 to 97 percent".
- `pages/index.astro` line 36: the Horne 2023 histology photo (Elsevier) stays behind a PENDING APPROVAL comment; replace the slot with Figure W27.
- `pages/index.astro` line 65: process poster `coated-array.png` is an internal photo; use `/images/process-poster.png` and the in-panel label.
- `pages/index.astro`: stat tiles now read from the new W12_numbers.json (six public facts); check the labels render and drop the "Every number on this site traces to ... our archive" line in favor of "Every number on this site comes from a published paper, dissertation or issued patent."
- `pages/technology.astro` line 95: `histology-array-1yr.png` (Elsevier) behind a PENDING APPROVAL comment; use `histology-sheep.png` or nothing.
- `pages/technology.astro` lines 139 and 153: the PENDING comments can now be filled with W31 (bond strength on silicone) and W30 (tunable window) per the figure map; the insertion row gets W07; "It stays on" gets W28 beside W06.
- Application cards on the home page: all `image: null` once worker C updates applications-index.json; check the grid still looks balanced with nine tinted panels (consider a 3 x 3 grid with the number large).

## Applications (worker C) 2026-10-29

- Content passes: published values with p and n, species and duration named, caveats stated, "not a ZwiGuard result" labels on precedent devices.
- `ApplicationCard` with `image: null` reserves the full 4:3 photo area as an empty tinted block, so every card on /applications and the home grid is mostly blank. Make the null variant compact: tinted panel holding the title, the number and the label only, equal heights across the row, no empty area.
- Dev server note: content collections need a server restart after `content.config.ts` is added; port 4321 served 404s for the new routes until restarted.
- Follow-ups for Kam: ten deck-level citations on airway and ENT are incomplete ("as cited in the ZwiCoat deck"); regulatory strip text on ENT, sensors and PEEK is placeholder wording; airway card stat is a cochlear-implant result and says so.

## End of build day 2026-10-29 (lead)

Done and reviewed: all 18 pages build clean (`site/`, `npm run build`, 18 MB dist);
home, technology, evidence (three interactive charts: publication timeline,
in-vivo study browser, antifouling browser), nine application pages, partner,
publications, about, contact, FCOI. Published-only rule applied throughout;
figures W04 to W08, W12, W17 to W21, W24 to W31 in use; W01, W02, W03, W09,
W10, W11, W13 to W16 and the lap-shear explorer held. Kam's feedback of the day
applied: ten papers, expanded antifouling and animal charts, patent tiles with
takeaways, leadership order, ZCMI logo, W26 title.

Small follow-ups (next session):
- W32_invivo_studies.json: some `note` fields start with "text:"; strip in
  build_figures.py.
- Horne dissertation year: content says 2023, title page says 2024 (Kam).
- Ten deck-level citations on airway and ENT pages are incomplete.
- Regulatory strip wording on ENT, sensors and PEEK pages is placeholder.
- Jensen 2021 and Barrera 2026 licenses unconfirmed (badges off for Barrera).
- Lighthouse pass and a real-phone check not yet run.
- Node 22.23.4 or newer needed on the EC2 box for Astro 7.
- The v2 folder is not a git repository yet; `site/` has no commits.

## State at usage cutoff, 2026-10-29 late evening

Done since Kam's evening answers: rule 3 revised (internal data allowed when
broadcast-worthy); polyurethane relabeled across W02/W10 and the site copy;
W10, W11, W01 and the archive tiles (W33, 182/1,056/468/136/2,812/20, each
with a takeaway) placed on the site; sanitized lap-shear explorer (no
formulation fields) as a fourth interactive chart; Directions A and B as
switchable themes (`?themes=1` shows the switcher; `/design-compare` explains
them); sterilization sentence and "email info@zwicoat.com" lines back; ten
deck citations completed on airway and ENT (Goldberg 2010 and Mondorf 2023
matched by topic only, confirm); lab media surveyed into
`assets-staging/lab-media/` with CANDIDATES.md (18 stills, 17 clips).

NOT yet done (next session, in this order):
1. Visual review of themes A and B at 1280 px (the pane kept resizing; not
   checked) and of the new explorer.
2. Media placement worker: pendulum loop (`pendulum-sidebyside-v2.mp4`, 5.5 s,
   loop with a hold; caption "no visible damage"; energy text in HTML) on the
   expanders page and home "It stays on"; expander photo strip (Mentor 125
   before/after front and back, 200 percent inflated); cuff-inflate loop and
   coated-cuff still on airway; coated-array and cross-section micrograph on
   neural; `dipcoat-ett-raw-01.mp4` trimmed to about 15 s and muted as the
   stopgap process video (ffmpeg is at C:\ffmpeg\bin). Rule: lab clutter in
   the wide pendulum shot needs Kam's OK.
3. `npm run build` after the above; Lighthouse; phone check; git init.
4. Kam to answer: ETT manuscript figures (W15, W16) yes or no; Formspree vs
   EC2 endpoint for the form; feeding-tube clogging reference (Anziliero 2023)
   if wanted back on the ENT page.

## Kam's decisions, 2026-10-30

- ETT manuscript figures (W15, W16, ETT insertion bar): hold until the paper is out.
- Contact form: no third-party account; build an endpoint on the EC2 box.
- Design: Blueprint (Direction B) is the choice. Kam saw blown-up or zoomed
  images in Blueprint; diagnose and fix.
- More variation in the figures across the nine application pages.
- Fewer "send us parts" and "partner with us" blocks: do not end every
  application article with the same paragraph; keep the nav button and the
  bands on home, technology and evidence.

## 2026-10-30: Blueprint default, media placed, endpoint built (lead review)

- Blueprint is the default theme; A and C remain behind the `?themes=1`
  switcher. The blown-up-image glitch was the theme-B figure title block: its
  long citation set the figure's min-content width, so figures grew to the
  citation length (evidence page was 5,009 px wide). Fixed with
  `contain: inline-size` on the title block and max-width rules on frames.
- CTABand now only on home, technology and evidence. Application pages end
  with a one- or two-sentence varied "Start a feasibility round" link.
- Figure map per application page rewritten (every hero distinct; no figure
  on more than three pages). Lab media placed: pendulum loop (expanders,
  home), expander photo strip, cuff loop and coated-cuff photo (airway),
  array cross-section (neural), trimmed dip-coating clip as the stopgap
  process video. Media in site/public/media (6 MB) and images/lab.
- Contact endpoint built in server/contact (Flask behind Apache at
  /api/contact; README with deploy steps and the two ProxyPass lines).
  Needs SMTP credentials from Kam at deploy time. Honeypot field is named
  "website"; if real visitors get rejected by browser autofill, rename it.
- Build clean, 19 pages. Reviewed home (Blueprint) and tissue-expanders in
  the browser; no console errors.
- Pending Kam: lab clutter in the wide pendulum shot is visible on the site
  (needs OK); SMTP choice; the ETT figures stay held.

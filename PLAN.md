# zwicoat.com v2: the plan

Written 2026-10-29. Kam owns the decisions; this file is the running plan.
Each phase ends with a gate where Kam reviews before the next starts.

## What the new site has to do

1. Make a device company's R&D lead, in under a minute, believe three
   things: the coating works (fibrosis, infection, friction, impedance),
   it stays on (durability), and it drops into their line (process,
   sterilization, regulatory path).
2. Show the depth of the evidence: ten years, 191 experiments, 1,156
   adhesion tests, 468 coated implants, 136 animals, 9 papers. The
   current site shows six publication covers and two renders.
3. Route each visitor to their application in two clicks, with a page
   that reads like a summarized white paper and ends in "send us parts".
4. Look like a serious materials company, not a template.

## Site map (v2)

```
/                       Home: one claim, one real image, the numbers, the four properties,
                        applications grid, how we work together, contact
/technology             The coating: chemistry, grafting, process, thickness, substrates,
                        sterilization, manufacturing (the platform white paper, summarized)
/evidence               The data: every figure, grouped by claim, with sources; the
                        interactive lap-shear explorer and the study timeline live here
/applications           Index: one card per application
/applications/neural-interfaces      (cochlear implants, neurostimulators, BCI)
/applications/tissue-expanders       (and breast implants)
/applications/vascular-access        (PICC, CVC, dialysis, ports)
/applications/indwelling-catheters   (urinary, drainage)
/applications/gi-stents
/applications/peek-and-orthopedic    (PEEK implants, spinal and cranial)
/applications/airway                 (endotracheal and tracheostomy tubes)
/applications/sensors                (CGM and implanted sensors)
/applications/ent-tubes              (tympanostomy and feeding tubes)
/partner                How we work: free feasibility round, joint development, Master File,
                        regulatory pathway, sterilization and shipping
/publications           Nine papers, three theses, patents
/about                  Team, University of Iowa origin, funding (NIH SBIR), patents
/contact
/fcoi                   (kept, plain document page)
```

Navigation: Technology, Evidence, Applications (dropdown with the nine
pages), Partner with us, About. "Send us parts" is the one call to action
and appears on every page.

## Phases and gates

### Phase 0: inspiration and direction (this delivery)

- Reviewed iotamotion.com, silq.tech, haystackmedical.com and the
  current zwicoat.com (notes in DESIGN-BRIEF.md).
- Three design directions proposed, each with a name, a palette, a type
  pairing, a layout idea for the home page and the application page, and
  what it borrows from the reference sites. Kam picks one or mixes.
- Figure set v1 built (figures/), content drafted (content/).
- Gate 0: Kam picks a direction and marks up the content.

### Phase 1: content lock

- Rewrite every page in the chosen voice; final figure list per page.
- Collect the real images the pages need (list in content/image-requests.md):
  the jig on the bench, a coated array under the microscope, a dyed
  coated tube, the histology panels, the sheep OR photo if shareable.
- Build the two interactive charts as standalone HTML prototypes
  (figures/interactive/) and approve their static fallbacks.
- Gate 1: Kam signs off page by page.

### Status 2026-10-29 (end of day)

Phase 2 build exists in `site/` (Astro). Every page is built and reviewed on
localhost. Published-only rule (CLAUDE.md rule 3) governs all figures and
copy; FIGURE-APPROVAL.md is the ledger and REVIEW-NOTES.md the review log.
Remaining before Phase 3: Kam's answers to the open questions in
REVIEW-NOTES.md, a git repository for `site/`, Lighthouse, a real-phone pass.

### Phase 2: build

- New repo (ZwiCoat website v2/site), Vite + React Router like the
  current site so the deploy path is unchanged, or Astro if we want
  mostly-static pages with islands for the two charts (recommendation:
  Astro; decision at Gate 0).
- Design tokens from the chosen direction; one component set (hero,
  claim block, figure with caption and source, stat tiles, application
  card, CTA band, footer).
- Figures imported from figures/png (2x) and figures/svg; alt text from
  the manifest captions.
- Interactive charts as islands; `<noscript>` and failed-load fallback to
  the static PNG.
- Gate 2: internal walkthrough on localhost.

### Phase 3: review

- Staging deploy on the EC2 box under a subpath or staging subdomain.
- Lighthouse pass (performance, accessibility above 90), mobile check
  on a phone, print check of an application page.
- Copy and claims review against content/claims-rules.md.
- Gate 3: Kam approves launch.

### Phase 4: launch

- Replace the dist on the EC2 box; keep /fcoi and /technology routes;
  redirect /about and /contact to their v2 pages.
- Update the FCOI PDF link; verify the MedTech QR codes still resolve.

## Decisions for Kam at Gate 0

1. Direction A, B or C (DESIGN-BRIEF.md), or a mix.
2. Astro (recommended) or stay on Vite + React.
3. Which application pages ship at launch: all nine, or the five with
   white papers plus neural and expanders (seven), with sensors and ENT
   tubes following.
4. Whether the evidence page shows the full lap-shear explorer (463
   groups, substrate filters) or a simplified version.
5. Image permissions: the sheep histology and XRM panels are open access
   (CC BY, Ben-Shlomo 2026); the Horne 2023 histology is Elsevier and
   needs the company's co-author reuse right confirmed.

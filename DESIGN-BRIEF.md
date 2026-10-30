# Design brief, Phase 0: inspiration and three directions

Written 2026-10-29 from a review of iotamotion.com, silq.tech,
haystackmedical.com and the current zwicoat.com, plus the six MedTech
decks and seven white papers. Kam picks one direction (or a mix) at Gate 0.

## What the reference sites do well, and what to take

**iotaMotion (iotamotion.com).** One bold claim in the hero
("Advancing CI surgery beyond human capability"), a strong single brand
color (mustard) used as large flat panels rather than gradients, real
photographs of people and the device, a "Ways we help" section that
splits the audience (surgeons, hospitals, patients), and a resources row
with downloadable PDFs. Take: the audience split (device makers,
clinicians, investors), the flat color panel, the downloadable white
papers as a visible row. Leave: the stock lifestyle photos; ZwiCoat's
images should be lab and device images.

**Silq (silq.tech).** A direct competitor in zwitterionic surfaces. Dark
hero with a product render, four benefit tiles with one-line claims,
a published-paper callout ("Published in Advanced Materials"), a quote,
a B2B "Surface Treatment Services" block, and a news strip (prize, GPO
contracts). Take: the published-paper callout as a first-class element,
the B2B partnership block, the news strip format. Leave: the dark render
hero (reads generic). Note for copy: Silq leads with "FDA Cleared,
Antibiotic-free"; ZwiCoat's counter is "covalently bonded, crosslinked
hydrogel, intact after a year in vivo, on silicone, PVC and PEEK", and the
evidence depth. Say it with data, not adjectives.

**Haystack Medical (haystackmedical.com).** Minimal. One sentence
("Ultra-sharp needles unlock inner ear therapies"), a device image, two
proof blocks (minimally invasive access; "Extensive publication record,
20+ publications"), team with photos and one-line bios, university and
NIH logos. Take: the publication record as a proof block, the restraint,
the one-sentence hero, the institutional logos. Leave: the thinness (it
has almost no data).

**Current zwicoat.com.** Weak hero (pastel gradient wordmark over a faded
elemental map), long body copy, one green fluorescence image, a page-flip
publications widget, no applications section, no data. The team bios are
good and reusable. Everything else is replaced.

## Positioning line (for all three directions)

ZwiGuard: a covalently bonded zwitterionic hydrogel that keeps protein,
cells and bacteria off medical devices. One coating step. Ten years of
evidence. Headline options for the hero:

- "The surface the body ignores."
- "Nothing sticks. Nothing elutes. Nothing peels."
- "A coating that stays on, so the body leaves the device alone."

## Shared design rules (all directions)

- Real images only: coated arrays, dyed coated tubes, micrographs,
  histology, the dip-coating jig, the tissue expander, the lab.
  No AI cartoons. Schematics are allowed only as simple line diagrams
  drawn by hand in SVG (the protein-film-versus-hydration-barrier
  diagram) and kept to two or three.
- Charts: Arial, light panel, brand blue for "coated", gray for
  "uncoated", generous padding, source line under every chart. Palette
  validated for color-vision deficiency (blue #0E7FC4, orange #C9711A,
  plum #7B4FA6; de-emphasis gray #8A929B).
- Mostly static. Two interactive charts at most (evidence page), each
  with a static fallback.
- Mobile first: the application pages must read well on a phone at a
  conference.
- No em-dashes, no exclamation marks, no "revolutionary".

## Direction A: "Lab notebook"

The site reads like a well-kept research record. White paper stock,
near-black ink, one accent (brand blue), ruled lines and small-caps
labels like a figure legend. Type: a humanist sans for body (Source Sans
3 or IBM Plex Sans) and the same face bold for headings; charts in Arial
so they sit naturally. Layout: generous left margin with a running
section label, figures full-width with the caption and source set in a
narrow right column, numbers as large inline figures rather than tiles.
Home page: a single sentence, then the W01 timeline full-width as the
first thing a visitor sees ("ten years of experiments, year by year"),
then the four properties each with one chart, then applications as a
plain indexed list. Application page: title, one-paragraph problem, "what
we have shown" with two charts and one micrograph, a comparison table
(from the white paper), "where to start", references in a collapsible
footnote block. Borrows: Haystack's restraint and publication-record
block, iotaMotion's downloadable PDFs. Risk: can look academic; mitigated
by large numbers and real device photos.

## Direction B: "Blueprint"

Engineering document aesthetic. Pale blue-gray background panels like a
drawing sheet, thin hairline rules, dimension-style callouts on the
device images (coating thickness 10 to 100 micrometers, bond strength,
cure time), monospace for data labels (JetBrains Mono) and a geometric
sans for headings (Inter Tight or Manrope). Brand blue plus a single warm
accent (the validated orange) for "uncoated" contrasts. Layout: a fixed
left rail with the section index on desktop, wide content area, charts in
"drawing frames" with a title block (figure number, source, date) in the
corner. Home page: hero is a large photograph of a coated electrode array
with three dimension callouts (thickness, bond strength, impedance drop),
then the numbers tile row (W12), then an "evidence by claim" matrix
(W13) that links into the evidence page, then applications as a card
grid with a device photo per card. Application page: a "spec sheet"
header (substrates, thickness range, sterilization compatible, regulatory
path) above the narrative. Borrows: Silq's benefit tiles and B2B block,
iotaMotion's audience split. Risk: can feel cold; mitigated by histology
and photographs in warm-toned frames.

## Direction C: "Evidence first"

A data-journalism layout. The hero is the data: the lap-shear explorer
(W02 interactive) or the fibrosis forest (W04) rendered large with a
one-line headline over it, before any marketing copy. Type: a strong
editorial sans (Söhne-like; practical choice Inter or Public Sans) with
very large numerals; black, white, brand blue, one accent. Layout:
scroll-driven sections, each a claim in large type on the left and the
chart on the right, with the source as a footnote; sticky section
headings; the applications section as a horizontal strip of real device
photos. Application page: opens with the one chart that matters for that
device (impedance for neural, insertion force for airway and catheters,
fibrosis for expanders), then the problem, then the data, then the
partner path. Borrows: Silq's published-paper callout, everything else is
the data itself. Risk: heaviest build (two interactive charts carry the
home page); mitigated by static fallbacks and by keeping the interactive
pieces on the evidence page if Gate 0 asks.

## Recommendation

Direction C for the home page and evidence page, with Direction B's
spec-sheet header on the application pages. That combination makes the
evidence the brand and gives each application page the one-glance
"does it fit my device" summary a device engineer wants. Direction A is
the fallback if Kam wants the lowest-risk build.

## Interactive charts (two, with static fallbacks)

1. **Lap-shear explorer** (evidence page). 463 group means as dots by
   substrate; hover shows formulation (W, C), n, year, scientist and
   failure mode; a filter row for substrate, year and formulation.
   Static fallback: W02. Data: figures/data/W02_lapshear_groups.json.
2. **Ten-year study timeline** (home or evidence page). The W01 bars with
   hover listing the experiments in that year and category; clicking a
   year filters the publications list. Static fallback: W01. Data:
   figures/data/W01_timeline.json plus a per-experiment list to add.

## Image requests for the lab (Phase 1)

- **Dip-coating process video (placeholder).** Kam does not want the CAD
  render of the jig on the site. The technology page and the "how it
  drops in" section of each application page reserve a 16:9 slot for a
  short, silent, looping clip of a real dip-and-cure cycle (10 to 20 s,
  no audio, autoplay muted, poster frame = a still of the coated part).
  Until the video exists the slot shows the poster still (a photo of a
  coated array or tube) with the caption "Automated dip coating: one
  step, about a minute per part". Build the component so the clip can be
  dropped in later without a layout change.
- The automated dip-coating jig on the bench, lit, no clutter (a still,
  used as the poster frame until the video exists).
- A coated cochlear implant array under the stereo microscope with the
  blue dye (the deck photo exists at 1594 x 526; a taller crop is needed).
- A dyed coated endotracheal tube, cuff inflated (deck slide 39 panel A
  exists; a cleaner studio shot would help).
- The tissue expander before and after the impact test (deck slide 30
  exists and is usable).
- Overmolded PEEK coupon (white paper OV Fig 4).
- Histology: Horne 2023 Fig 7 E to H (co-author reuse to confirm),
  Ben-Shlomo 2026 Fig 5 and 6 (open access).
- Team portraits: the four existing photos are fine; add Parker and any
  current staff Kam wants listed.

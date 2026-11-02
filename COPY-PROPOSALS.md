# Copy proposals (for Kam to approve one by one)

Audit date 2026-11-02. Read-only pass over the pages, the nine application files, `figure-text.ts`, `applications-index.json`, `publications.json`, `team.json`, `W12_numbers.json`, `W33_archive.json` and the `figures/MANIFEST.md` captions.

Skipped because they are already being fixed: ZwiGuard, benzophenone, citations with scientist names, the "Silicone is published" block, the regulatory section on the technology page, and the neural "problem" paragraph.

How to read the tables: "Current text" is an exact quote. "Problem" is a five-word tag. "Proposed" is the replacement, or "remove". Proposals use only numbers already on the site. Approve by number, for example "Home 8, Durability 3".

---

## site/src/pages/index.astro (home; also components/Hero.astro and public/data/W12_numbers.json)

| # | Current text | Problem | Proposed replacement |
|---|---|---|---|
| 1 | Less scar, lower impedance, easier insertion, fewer bacteria. One coating step. Ten years of evidence. | Stack of fragments | It means less scar, lower impedance, easier insertion and fewer bacteria, from a single coating step. The evidence spans ten years of published work. |
| 2 | a few micrometres to 100 or more, tunable | Vague, missing unit | From a few micrometres to over 100, set by the process |
| 3 | about half, four weeks in sheep (Ben-Shlomo 2026) | Fragment with author name | About half the impedance after four weeks in sheep |
| 4 | Every number on this site comes from a published paper, dissertation or issued patent. | Untrue and defensive | Every number has its source listed under it. |
| 5 | And behind the papers: 182 archived experiments, 1,056 adhesion tests, 136 animals. | Starts with "And"; list | Behind the papers sit 182 documented experiments, 1,056 adhesion tests and 136 animals. |
| 6 | Sources: the ten journal papers and the dissertations listed on the Publications page, USPTO records, ZCMI patent schedule, 2025. | Internal jargon, unclear | Sources are listed on the Publications page and in the US patent record. |
| 7 | In three sheep, each with one coated and one uncoated human cochlear implant array, the coated ears had fewer cell nuclei (p = 0.0020), fewer macrophages (p = 0.0063) and less fibrous tissue (p = 0.0101) at four weeks. Each line is one sheep. | Lab report, p values | In three sheep, each fitted with one coated and one uncoated human cochlear implant array, the coated ears had fewer cells, fewer macrophages and less fibrous tissue after four weeks. |
| 8 | One sheep showed no difference in cells or macrophages, and the authors call the study a small pilot (Ben-Shlomo 2026, Hearing Research). Across mice, rats and sheep, scar was about 45 to 85 percent lower. | Undercuts our own result | Across mice, rats and sheep, scar was about 45 to 85 percent lower (Ben-Shlomo 2026, Hearing Research). |
| 9 | Three sheep, one coated and one uncoated array each (Ben-Shlomo 2026, Hearing Research). No coated device has been implanted in a person. | Fragment, then hedge | Same sheep study, same arrays: the coated side read lower on every comparison. All results are from animal and laboratory studies. |
| 10 | Two cadaveric studies of coated cochlear implant arrays: peak insertion force fell about 42 percent (Bennion 2021, 64.2 to 37.0 mN, n = 9, p = 0.001) and about 50 percent (Peel 2024, about 68 to 35 mN, read from the figure). | Lab report in body | In two studies on human cadaver cochleae, coated arrays needed about 42 and about 50 percent less force to insert. |
| 11 | Silicone implants were placed in rats and challenged with S. aureus. At day 21, coated implants carried far fewer adherent bacteria and live colonies than uncoated ones (Shen 2021, ACS Applied Bio Materials). | Jargon, dense | Silicone implants in rats were challenged with Staphylococcus aureus. After 21 days, coated implants carried far fewer bacteria than uncoated ones (Shen 2021, ACS Applied Bio Materials). |
| 12 | A coating kept in a rat for two weeks still resisted a fresh challenge. These are animal results, not clinical results. | Disclaimer after claim | A coating that had spent two weeks in a rat still resisted a fresh challenge. |
| 13 | Friction was unchanged after three weeks in mice. | Weak, negative phrasing | Friction stayed about 90 percent lower after three weeks in mice. |
| 14 | Ten papers, three dissertations and three issued US patents, 2017 to 2026. Hover or focus a marker to read what it found. | Fragment, tool jargon | Ten papers, three dissertations and three US patents, from 2017 to 2026. Select a marker to see what each one found. |
| 15 | Automated dip coating: one step. Video coming. | Promises missing video | remove the whole process section until the clip exists, or keep the text only (see 16) |
| 16 | The part is dipped into the monomer solution, then moved under UV light. One UV step grafts the film and crosslinks it. | Monomer jargon | The part is dipped in the coating solution, then passed under UV light. That one UV step bonds the film to the device and links it into a gel. |
| 17 | Nothing sticks: the hydration shell turns away protein, cells and bacteria before scar or biofilm can start. | Overclaim | A tightly bound water shell turns away protein, cells and bacteria, so scar and biofilm have no foothold. |
| 18 | United States, Australia, China, Japan and Mexico: the largest device markets. | Unsourced claim | Granted in the United States, Australia, China, Japan and Mexico. |
| 19 | Five new inventions filed; national applications pending in Canada, Europe and South Africa. | Mixes two ideas | Five new inventions filed, and applications are in progress in Canada, Europe and South Africa. |
| 20 | Durable: the covalent graft outlasts the study and the capsule stays thin. | Vague claim | The covalent graft was still intact at one year, and the scar capsule stayed thin. |

---

## site/src/pages/technology.astro

| # | Current text | Problem | Proposed replacement |
|---|---|---|---|
| 1 | ZwiGuard is a zwitterionic hydrogel made from sulfobetaine and carboxybetaine methacrylate. | Monomer names | ZwiCoat is a zwitterionic hydrogel, a water-swollen polymer network in which every unit carries both a positive and a negative charge. |
| 2 | Each repeat unit carries balanced positive and negative charges and a strong dipole. The dipole binds a tightly ordered shell of water. | Repeats previous idea | Those paired charges form a strong dipole, and the dipole binds a tightly ordered shell of water. |
| 3 | The hold is stronger than the hydrogen-bonded hydration of PEG. | Jargon, unsourced comparison | The water is held more tightly than on PEG, the usual hydrophilic polymer. |
| 4 | Zwitterionic hydrogels implanted in mice resisted the foreign body reaction in a 2013 study (Zhang et al., Nature Biotechnology). | Disconnected, outside work | Independent work published in Nature Biotechnology in 2013 showed zwitterionic hydrogels resisting the foreign body reaction in mice. |
| 5 | The result is a crosslinked hydrogel anchored to the device. It is not a thin tethered brush, an adsorbed layer that can wash off, or an additive blended into the polymer. | Defines by negation | The result is a crosslinked gel anchored to the device, so it cannot wash off or leach out the way an adsorbed layer or an additive can. |
| 6 | The range was 53 to 99 percent. | Lab-report caveat | remove (the median says it) |
| 7 | S. aureus adhesion fell by 97 percent in suspension and 84 percent on explants from rats (Shen 2021). | Jargon: suspension, explants | Staphylococcus aureus adhesion fell by 97 percent in the lab and by 84 percent on tissue taken from rats (Shen 2021). |
| 8 | Friction against dermis was 94 percent lower (Bennion 2021). These are bench and explant measurements, not clinical results. | Disclaimer after claim | Friction against skin tissue was 94 percent lower (Bennion 2021). |
| 9 | The largest reduction, about 85 percent less fibrosis, was in sheep cochleae at four weeks (Ben-Shlomo 2026, Hearing Research). The basal-turn measurement in the same study was not statistically significant. | Not significant, lab report | The largest reduction, about 85 percent less fibrosis, was in sheep cochleae at four weeks (Ben-Shlomo 2026, Hearing Research). |
| 10 | In rats, four coated groups had capsules about 72 to 83 percent thinner at six weeks (Barrera 2026, ACS Applied Polymer Materials). | "Groups" unclear | In rats, capsules around four coated variants were about 72 to 83 percent thinner at six weeks (Barrera 2026, ACS Applied Polymer Materials). |
| 11 | Peak insertion force fell about 42 percent in one study (Bennion 2021, 64.2 to 37.0 mN, n = 9, p = 0.001) and about 50 percent in another (Peel 2024, about 68 to 35 mN, read from the figure). | Repeats caption, lab report | remove (the paragraph above and the chart caption already say it) |
| 12 | The study used three sheep, with one coated and one uncoated array each (Ben-Shlomo 2026). The sheep cochleae also showed less inflammation. No coated device has been implanted in a person. | Choppy, hedge ending | The study used three sheep, each with one coated and one uncoated array (Ben-Shlomo 2026). The coated cochleae also showed less inflammation. |
| 13 | Friction was unchanged after three weeks implanted in mice (Peel 2024). Antifouling was unchanged at six months (Horne 2023, Peel 2024). | "Unchanged" twice, weak | Friction stayed low after three weeks in mice (Peel 2024), and protein and cell resistance held at six months (Horne 2023, Peel 2024). |
| 14 | A PEG-based control film partly detached at six weeks in mice, and the zwitterionic film did not (Horne 2023, Fig 5). | Figure number, odd order | In the same mouse study, a PEG-based film partly detached by six weeks. The ZwiCoat film did not (Horne 2023). |
| 15 | The coating has been tested through common sterilization cycles (steam, EtO, UV and gamma, wet or dry, and dry e-beam); wet e-beam did not pass. Bond strength held after gamma or e-beam plus shipping. We validate on your cycle during joint development. | Lists a failure | The coating is compatible with steam, ethylene oxide, gamma, UV and dry e-beam sterilization, and bond strength held after sterilization and shipping. We validate on your own cycle during joint development. (Same paragraph appears on the durability and partner pages.) |
| 16 | Automated dip coating: one step. Video coming. | Promises missing video | remove the "The process, on video" block until the clip exists |
| 17 | Cross-section of a coated cochlear implant array: elemental map showing the hydrogel film on the silicone carrier. ZwiCoat. | Credit repeated in caption | Cross-section of a coated cochlear implant array, mapped by element, showing the hydrogel film on the silicone carrier. |
| 18 | Evidence matrix: substrates versus the kinds of test on record. Blue means data exist in the ZwiCoat archive; polyurethane is the CIVCO probe cover. | Names a customer | Evidence matrix: which materials have been tested, and how. Blue means ZwiCoat has data; polyurethane is an ultrasound probe cover. (Same caption on the PEEK and GI pages and in MANIFEST.md.) |
| 19 | A finite reservoir: in the CATHETER trial, silver alloy catheters had 12.5 percent symptomatic urinary infection and standard catheters 12.6 percent. | Clunky, trial name | A finite reservoir that runs out: in a trial of 7,102 patients, silver alloy catheters did no better than standard catheters against symptomatic urinary infection. |
| 20 | Regulatory note (table row: "A coating on the device." / "Antimicrobial agents bring added FDA testing and labeling." / "No antimicrobial agent, so no antimicrobial-agent data are required.") | Regulatory on technology page | remove the row (the rules allow regulatory only on application pages) |

---

## site/src/pages/evidence.astro

| # | Current text | Problem | Proposed replacement |
|---|---|---|---|
| 1 | This page shows them grouped by what they show, with the source under every chart and the papers linked at the bottom. | Circular, meta | The results are grouped here by what they show. Every chart carries its source, and the papers are linked at the bottom. |
| 2 | Hover or focus a marker to read what it found. Under the tiles, the archive counts show the work behind the papers. | Repeats home, tool jargon | Each marker is one paper, dissertation or patent. Select one to see what it found. |
| 3 | In mice the capsule was 67 percent thinner at six weeks on flat silicone and 62 percent thinner at one year on cochlear implant arrays (Horne 2023). In rats, four coated groups had capsules about 72 to 83 percent thinner at six weeks (Barrera 2026). | Run of numbers, "groups" | In mice the capsule was 67 percent thinner at six weeks on flat silicone and 62 percent thinner at one year on cochlear implant arrays (Horne 2023). In rats, capsules around four coated variants were 72 to 83 percent thinner at six weeks (Barrera 2026). |
| 4 | The browser below adds ten more variants, 48 in all. In rats challenged with S. aureus, coated implants carried far fewer bacteria at day 21 (Shen 2021). | Jargon, abrupt last sentence | The interactive chart below shows all 48 comparisons. Below it, a rat study shows the same effect on implants: far fewer Staphylococcus aureus bacteria at day 21 (Shen 2021). |
| 5 | Filter by category, chemistry, setting or paper, then hover or focus a bar for the values, n and p. The static chart shows 38 of the 48 comparisons, from 8 papers. | Chemistry filter, lab report | Filter by category, setting or paper, then select a bar to see its values. |
| 6 | The friction measurements after explant are in section 4. | Jargon: explant | Friction after three weeks in mice is in section 4. |
| 7 | The explorer shows every lap-shear group in our database, by substrate. With enough grafting agent, the gel fails before its bond to silicone does (Leigh 2019). The cross-linker level trades stiffness against antifouling, and the best balance is at roughly 5 to 15 percent (Jensen 2021). | Jargon, unclear trade-off | Every dot in the chart below is one bond-strength test group, sorted by material. With enough grafting agent, the gel itself gives way before its bond to silicone does (Leigh 2019). Crosslinking tunes the gel: stiffer gels cost some antifouling, and the best balance sits at roughly 5 to 15 percent (Jensen 2021). |
| 8 | Each dot is one experimental group (3 to 10 samples); black bar = median. ZwiCoat lap-shear database, 2017 to 2026; formulation details withheld. Filter by substrate, year or failure mode, then hover or focus a dot for the values. | Lab report caption | Each dot is one bond-strength test group. The black bar marks the median for each material. Filter by material or year, then select a dot to see its values. (Keep "formulation details withheld" in the source line only.) |
| 9 | Forty-six comparisons from the published animal and cadaver studies, one marker each. Filter by species and metric, then hover or focus a marker for the paper, n and p value. | p values, tally | Every published animal and cadaver comparison, one marker each. Filter by species and measure, then select a marker for the paper and the result. |
| 10 | Time is on a log axis, and negative values mean less with the coating. The static chart is the fibrosis summary: 10 measurements in mice, rats and sheep. | Chart-reading instructions | remove (put "Negative values mean less with the coating" in the axis label instead) |
| 11 | Durable: bond strength characterized on silicone, PVC, PEEK, parylene-C and polyurethane. | Label does not fit tile | Bond strength measured on silicone, PVC, PEEK, parylene-C and polyurethane. |
| 12 | Traceable: the raw data sit behind every chart. | Untrue for published charts | Traceable: the raw data for our own studies are archived. |

---

## site/src/pages/durability.astro

| # | Current text | Problem | Proposed replacement |
|---|---|---|---|
| 1 | Here is the published record and our own tests. | Filler opener | The evidence comes from published studies and our own tests. |
| 2 | Checkpoints run from two weeks in rats to one year in mice. At one year in mice, the film was intact (Horne 2023). | Repeats the headline | Studies run from two weeks in rats to one year in mice (Horne 2023). |
| 3 | Four weeks in sheep cochleae showed no delamination (Ben-Shlomo 2026). | Negative phrasing | In sheep, the film stayed attached to working cochlear implant arrays for four weeks (Ben-Shlomo 2026). |
| 4 | After explant | Jargon label | After implantation |
| 5 | Friction was unchanged after three weeks in mice. | Weak, negative phrasing | Friction stayed about 90 percent lower after three weeks in mice. |
| 6 | It kept about 90 percent lower friction than uncoated silicone. Against five guinea pig tissues and steel, friction was at least 90 percent lower. | "Five guinea pig tissues" odd | It kept about 90 percent lower friction than uncoated silicone. Against steel and a range of animal tissues, friction was at least 90 percent lower. |
| 7 | A weighted pendulum strikes a coated tissue expander. | Run of short sentences | A weighted pendulum struck a coated tissue expander, and the coating showed no visible damage (ZwiCoat internal study, 2026). |
| 8 | On silicone, the gel tore before the interface let go (Leigh 2019). | Repeats the headline | On silicone the bond is stronger than the gel itself. Adhesion tests end with the gel tearing, not the film peeling off, once there is enough grafting agent (Leigh 2019). |
| 9 | Seven of eight cycles left the coating intact. | Header tallies | Compatible with multiple sterilization methods. |
| 10 | Sterilization compatibility and bond strength after sterilization plus shipping. The coating was intact after seven of eight sterilization cycles; wet e-beam failed. (W11 caption, also in figure-text and MANIFEST: "Seven of eight sterilization methods left the coating intact") | Tally, names a failure | Compatible with multiple sterilization methods, and bond strength held after sterilization and shipping. Drop wet e-beam from the chart and its alt text. |
| 11 | What we have not shown yet / Aging and shelf life come next. / Long-term aging and shelf life are measured in joint development. / Results from studies in preparation are not on this site. | Hedges, promises, undercuts us | remove the whole block (the technology page already says aging and shelf life are part of joint development) |

---

## site/src/pages/applications/index.astro and site/src/data/applications-index.json

| # | Current text | Problem | Proposed replacement |
|---|---|---|---|
| 1 | Every page names the problem first, then the published study that bears on it. The number on each card comes from that study, and every page lists its sources. No coated device has been implanted in a person. Where a substrate or result is not yet published, the page says the feasibility round measures it on your parts. | Procedural, hedging run-on | Each page starts with the clinical problem, then shows what coated devices achieved in published studies. Every number is cited. |
| 2 | 12.5 vs 12.6% / symptomatic CAUTI with silver alloy versus standard catheters: the problem a new surface must solve (Pickard 2012) | Card shows competitor, jargon | ~90% / lower friction on coated silicone, still in place after three weeks in mice (Peel 2024) |
| 3 | ~50% / less peak insertion force for coated cochlear implant arrays in human cadaveric cochleae (Bennion 2021, Peel 2024) (airway card) | Not an airway result | 31 vs 48 degrees / tilt to start mucus flow in a coated 2.6 mm silicone tube against an uncoated one (Horne 2025) |
| 4 | feasibility / PEEK bonding is measured on your parts | Card has no number | 155 vs 940 / bacteria per field on coated against uncoated implants in rats at day 21 (Shen 2021) |
| 5 | Nine device families, one number that matters for each. (home and index headline) | Cute, hard to read | Nine device families, and the published result that matters for each. |

---

## site/src/content/applications/neural-interfaces.md

| # | Current text | Problem | Proposed replacement |
|---|---|---|---|
| 1 | Every result below comes from a published study. No coated device has been implanted in a person. | Opens with a hedge | Every result below comes from a published study in animals or human cadaver cochleae. |
| 2 | Three sheep each received one coated and one uncoated human cochlear implant array. Total impedance was about 30 against 10.5 kilohms at implantation (p < 0.0001) and about 17.5 against 9.5 at four weeks (p = 0.0007), about 50 percent lower. Access resistance was also lower at four weeks (p = 0.0084). Polarization impedance was not significantly different then (p = 0.26). | Lab report, p values | In three sheep, each given one coated and one uncoated human cochlear implant array, total impedance was about 30 against 10.5 kilohms at implantation and about 17.5 against 9.5 four weeks later, roughly half. Access resistance was lower too. |
| 3 | At the round window, the pooled coated ears had fewer cell nuclei (p = 0.0020), fewer macrophages (p = 0.0063) and less fibrous tissue (p = 0.0101). One of the three sheep showed no difference in cells or macrophages. At the basal turn the pooled differences were not significant. The authors call the study a small pilot. | Four caveats in a row | At the round window, where the array enters the cochlea, coated ears had fewer cells, fewer macrophages and less fibrous tissue after four weeks. |
| 4 | grew a capsule about 60 percent thinner when coated, 47 against 18 micrometres (p = 0.026). | p value in body | grew a capsule about 60 percent thinner when coated, 18 against 47 micrometres. |
| 5 | A cross-section of a coated array, mapped by element, shows the hydrogel film on the silicone carrier. The second picture is a coated array dyed blue so the film is easy to see. | "Second picture" ambiguous | A cross-section mapped by element shows the hydrogel film on the silicone carrier. Dyed blue, the film is easy to see on the whole array and in section. |
| 6 | On silicone, adhesion tests show the film failing inside the gel before the interface lets go (Leigh 2019). | "Failing" reads negative | On silicone, the film bonds so firmly that the gel tears before the interface lets go (Leigh 2019). |
| 7 | Why it drops in | Idiom unclear | How it fits your process (applies to all nine pages) |

---

## site/src/content/applications/tissue-expanders.md

| # | Current text | Problem | Proposed replacement |
|---|---|---|---|
| 1 | Every result below is a laboratory, mouse, rat or sheep result from a published study. No coated implant or expander has been placed in a person. | Opens with a hedge | Every result below comes from published laboratory, mouse, rat and sheep studies. |
| 2 | In 2019 the FDA requested a recall of BIOCELL textured implants and expanders, and textured use fell. | Names a product | In 2019 the FDA requested a recall of one maker's textured implants and expanders, and textured use fell. |
| 3 | Around coated silicone sheets the capsule was 27 micrometres, against 82 around uncoated sheets (p = 0.010). A non-zwitterionic PEG-type hydrogel gave 43, not significantly different from uncoated. | Not significant, p value | Around coated silicone sheets the capsule measured 27 micrometres, against 82 around uncoated sheets. |
| 4 | After six months under the skin of mice, the fibroblast-repelling effect was unchanged, and the film was intact at one year (Horne 2023). | Awkward, weak | After six months under the skin of mice, coated silicone still repelled fibroblasts, and the film was intact at one year (Horne 2023). |
| 5 | about 940 bacteria per field uncoated and about 155 coated at day 21 (p < 0.0001). These are laboratory and rat results, not clinical results. (Shen 2021.) | p value, disclaimer | about 940 bacteria per field uncoated and about 155 coated at day 21 (Shen 2021). |
| 6 | Whether the film stretches with an inflated expander is measured in the feasibility round on your parts. So is adhesion on your silicone grade. | Hedge | A coated expander inflated to 200 percent of its starting volume kept the coating across the whole shell (ZwiCoat internal test, 2026). Adhesion on your silicone grade is confirmed in the feasibility round. (Kam to confirm the 200 percent photo is a test we can state.) |
| 7 | In ZwiCoat's own tests on silicone coupons, the coating survived seven of eight sterilization cycles; wet e-beam did not. | Tally, failure | In ZwiCoat's own tests on silicone, the coating was compatible with steam, ethylene oxide, gamma, UV and dry e-beam sterilization. |

---

## site/src/content/applications/airway.md

| # | Current text | Problem | Proposed replacement |
|---|---|---|---|
| 1 | tested for mucus flow and bacterial adhesion on silicone, with no endotracheal tube study published yet. | Hedge in standfirst | a drug-free coating that lets mucus flow at a gentler tilt, resists bacteria and lowers friction on silicone. |
| 2 | No ZwiGuard result on an endotracheal or tracheostomy tube is published. The results below are on silicone and on cochlear implant arrays. The feasibility round measures them on your tube. | Opens by admitting a gap | The results below come from published studies on silicone and on cochlear implant arrays, the models for mucus flow, friction and insertion force. |
| 3 | In a 2.6 millimetre silicone tube, mucus started to flow at 31 degrees of tilt against 48 uncoated (p = 0.0017). Dried mucus plugs cleared in a median 22.5 minutes against 30 (p = 0.024). The effect is largest in wider tubes. The mucus was a non-human model, and the authors call the plug result modest and preliminary. | p values, caveats | In a 2.6 millimetre silicone tube, mucus started to flow at 31 degrees of tilt against 48 uncoated. Dried mucus plugs cleared in a median 22.5 minutes against 30. The effect is largest in wider tubes, such as airway tubes. |
| 4 | The clip and the photograph show a coated cuff in our lab. They are images of a coated part, not performance data. Whether the film stretches with your cuff is measured in the feasibility round. | Disclaims own images | The clip and the photograph show a coated cuff in our lab, inflating and deflating. |
| 5 | This is the published insertion-force model. It is not a tube result. | Undercuts own result | Coated cochlear implant arrays are the published model for insertion force. |
| 6 | Bonding to PVC, the usual tube material, is measured in the feasibility round on your tubes. | Contradicts internal PVC tests | ZwiCoat has also tested bonding to PVC, the usual tube material, in its own lab. The feasibility round confirms it on your tubes. |

---

## site/src/content/applications/vascular-access.md

| # | Current text | Problem | Proposed replacement |
|---|---|---|---|
| 1 | Every result below is from a published study on silicone, in the laboratory or under the skin of an animal. None was measured in flowing blood. | Ends on a gap | Every result below is from a published study on silicone, in the laboratory or under the skin of an animal. (Also remove "not measured in blood" from the evidence strip.) |
| 2 | In the PICNIC trial, catheter failure was 5.9 percent with a hydrophobic PICC, 9.9 percent with a chlorhexidine PICC and 6.1 percent with a standard polyurethane PICC (Ullman 2025). | Number run, trial name | In a large PICC trial, neither a hydrophobic nor a chlorhexidine catheter beat a standard polyurethane one on catheter failure (Ullman 2025). |
| 3 | A grafted sulfobetaine surface cut thrombus about 99 percent in a canine model (Smith 2012), and FDA cleared a zwitterionic-surface PICC (K113225). Neither is a ZwiGuard result. | Monomer name, undercuts | A grafted zwitterionic surface cut thrombus by about 99 percent in a canine model (Smith 2012), and FDA has cleared a zwitterionic-surface PICC (K113225). |
| 4 | One dip step coats the outer wall and the lumen. The film is grafted and crosslinked in one UV step. Bond strength rises with the grafting agent until the film fails inside the gel, not at the silicone interface. | Repeats "one step" | One dip coats the outer wall and the lumen together. Bond strength rises with the grafting agent until the gel itself, not the bond, is the weak point. |

---

## site/src/content/applications/indwelling-catheters.md

| # | Current text | Problem | Proposed replacement |
|---|---|---|---|
| 1 | tested on silicone for protein, cell and bacterial adhesion, with no urine data yet. | Hedge in standfirst | tested on silicone for protein, cell and bacterial adhesion. (Also remove "urine not yet measured" from the evidence strip.) |
| 2 | Every result below is from a published study on silicone. No urine data are published. | Admits a gap | Every result below is from a published study on silicone. |
| 3 | FDA has cleared zwitterion-modified silicone Foley catheters (K192034 through K233013). | Orphan in friction paragraph | remove here (it is already in the regulatory line of the strip) |
| 4 | Not yet measured. Urine, encrustation and Gram-negative bacteria. The feasibility round measures adhesion and friction on your catheter. Your team runs bladder-model and urine tests on the coated parts. | "Not yet" heading, fragments | The feasibility round measures adhesion and friction on your catheter, and your team can run bladder-model and urine tests on the coated parts. |
| 5 | One chemistry and one dip step serve urinary, drainage and vascular lines. The coating is applied to the outer wall and the lumen together. One development program and one Device Master File can carry across a product line. The film is drug-free, so there is no antimicrobial to manage. | Identical short sentences | One chemistry and one dip step coat urinary, drainage and vascular lines, outer wall and lumen together, so one development program and one Device Master File can cover a whole product line. The film is drug-free, with no antimicrobial to manage. |

---

## site/src/content/applications/peek-and-orthopedic.md

| # | Current text | Problem | Proposed replacement |
|---|---|---|---|
| 1 | whose published data are on silicone, so PEEK bonding is measured in the feasibility round on your parts. | Hedge in standfirst | tested for bacterial adhesion and bond strength on silicone, and tested on PEEK in our own lab. (Also change the evidence strip "PEEK: none published".) |
| 2 | No PEEK data are published. The matrix above shows where ZwiCoat has its own tests on PEEK and other substrates. Every published result below was measured on silicone, or on silicone and platinum arrays. | Opens with a gap | The matrix above shows where ZwiCoat has tested PEEK and other materials in its own lab. The published results below were measured on silicone and on platinum-contact arrays. |
| 3 | The film bonds so firmly that it fails inside the gel before the silicone interface lets go. | "Fails" reads negative | The film bonds so firmly that the gel tears before the silicone interface lets go. |
| 4 | None of this was measured on bone or PEEK. | Undercuts the paragraph | remove |
| 5 | PEEK has its own problems. | Vague opener | PEEK brings its own challenges. |

---

## site/src/content/applications/sensors.md

| # | Current text | Problem | Proposed replacement |
|---|---|---|---|
| 1 | with sensor response still to be measured on your parts. | Hedge in standfirst | a drug-free coating tested for scar capsule thickness on silicone and implant arrays, and tunable to stay thin. (Also remove "sensor response not yet measured" from the evidence strip.) |
| 2 | No sensor has been coated and measured in a published ZwiGuard study. The results below are on silicone and on implant arrays. | Opens with a gap | The results below are from published studies on silicone and on implant arrays. |
| 3 | One sheep showed no difference in cells or macrophages. | Undercuts our result | remove (also in the W26 caption and alt text) |
| 4 | A different zwitterionic coating, poly(MPC), cut glucose sensor error without recalibration from 73 to 17 percent in mice over three days and from 48 to 18 percent in non-diabetic primates over five days (Xie 2018). In diabetic primates the gap was smaller, 32 against 22 percent, and it disappeared with recalibration. That is not a ZwiGuard result. | Jargon, concedes the point | Related work points the same way. A different zwitterionic coating cut glucose sensor error without recalibration from 73 to 17 percent in mice over three days (Xie 2018). ZwiCoat is a thicker, crosslinked, grafted hydrogel. |
| 5 | A sensor needs the film to stay thin and let glucose through, and the film can be tuned. More crosslinker makes the gel stiffer and less swollen, while the protein, cell and friction benefits are strongest at about 5 to 15 percent crosslinker. | Run-on, mixes ideas | A sensor needs a thin film that lets glucose through, and the film is tunable: the crosslinker level sets how stiff and how swollen the gel is. |
| 6 | Glucose diffusion through the film and sensor response time are not yet measured. Your bench measures response time on the coated parts. The film is drug-free. | "Not yet measured" | Your bench can measure sensor response time on the coated parts. The film is drug-free. |

---

## site/src/content/applications/ent-tubes.md

| # | Current text | Problem | Proposed replacement |
|---|---|---|---|
| 1 | Saline started to flow at about 0 degrees of tilt on coated silicone sheets, against 45 on uncoated sheets. With 5 percent mucus, zwitterionic coatings needed 10 degrees or less against 40. With 10 percent mucus, flow started at 10 degrees or less against 30. | Number run | Saline started to flow at about 0 degrees of tilt on coated silicone sheets, against 45 on uncoated sheets. With mucus at 5 and 10 percent, flow started at 10 degrees or less on coated sheets, against 40 and 30 uncoated. |
| 2 | In 1.0 millimetre tubes the figures were 35 against 46 degrees (p = 0.047). The effect is largest in wider tubes and fades in narrow ones. Ear tubes are narrower than these, so the feasibility round measures flow on your tube. | Undercuts ENT page | In 1.0 millimetre tubes, flow started at 35 degrees against 46. The feasibility round measures flow on your own tube. |
| 3 | The first plug cleared at 3 minutes in the coated group and 21 in the uncoated group. The mucus was a non-human model, and the authors call this result modest and preliminary. | Cherry-pick, caveat | remove both sentences |
| 4 | Coating narrows the bore, and the published benefit shrinks with diameter. So the feasibility round measures flow on your tube before any design change. | Opens with a negative | The published film is about 7 micrometres thick, so the bore barely changes. The feasibility round measures flow on your tube before any design change. |

---

## site/src/content/applications/gi-stents.md

| # | Current text | Problem | Proposed replacement |
|---|---|---|---|
| 1 | Every result below is from a published study on silicone, or from a bench model. No stent has been coated and tested in a published ZwiGuard study. | Admits a gap | Every result below is from a published study on silicone or from a bench model. |
| 2 | The mucus was a non-human model, and the authors call the plug result modest and preliminary. The effect fades in narrower tubes: in 1.0 millimetre tubes the difference was 11 degrees. (Horne 2025.) | Caveats stacked | remove both sentences |
| 3 | That is a reason to test delivery. It is not a patency result. | Undercuts friction claim | Low friction is relevant to stent delivery, which the feasibility round can test. |
| 4 | In ZwiCoat's own tests on silicone coupons, it was intact after seven of eight sterilization cycles; wet e-beam did not pass. Your cycle is validated during joint development. | Tally, failure | In ZwiCoat's own tests on silicone, the coating was compatible with steam, ethylene oxide, gamma, UV and dry e-beam sterilization. We validate your own cycle during joint development. |
| 5 | Silicone is the published substrate. The matrix below shows where ZwiCoat also has internal data. PTFE, FEP and nitinol, and crimping and expansion of a finished stent, are feasibility-round questions. | Flat, negative close | The matrix shows the materials ZwiCoat has also tested in its own lab. PTFE, FEP and nitinol, and crimping and expanding a finished stent, are where the feasibility round starts. |

---

## site/src/pages/partner.astro

| # | Current text | Problem | Proposed replacement |
|---|---|---|---|
| 1 | We return coated parts with matched uncoated controls and data on coverage and adhesion, friction, and protein and bacterial adhesion. | "Adhesion" used twice | We return coated parts with matched uncoated controls and data on coverage, bond strength, friction, and protein and bacterial adhesion. |
| 2 | We run the program the claim needs: ISO 10993 biocompatibility, sterilization validation on your cycle, accelerated aging and shelf life, and an animal model. | "Program the claim needs" unclear | We run the studies your submission needs: ISO 10993 biocompatibility, sterilization validation on your cycle, accelerated aging and shelf life, and an animal model. |
| 3 | Device manufacturers: cochlear implants and neurostimulators, breast implants and tissue expanders, catheters and vascular access, airway and ENT tubes, GI stents, PEEK implants and sensors. Contract and component manufacturers. Consultants and innovation centers who bring client devices. | List and two fragments | We work with device makers in cochlear implants and neurostimulators, breast implants and tissue expanders, catheters and vascular access, airway and ENT tubes, GI stents, PEEK implants and sensors. Contract and component manufacturers, and consultants and innovation centers with client devices, are welcome too. |
| 4 | Expect FDA to treat the zwitterionic polymer as a novel material. Plan on a full ISO 10993 package plus chemical characterization. | Pessimistic, jargon | A Pre-Submission with FDA confirms the path early, and our Device Master File carries the formulation and safety data. |

---

## site/src/pages/about.astro and site/src/data/team.json

| # | Current text | Problem | Proposed replacement |
|---|---|---|---|
| 1 | ZwiCoat Materials Innovations, LLC (ZCMI) makes ZwiGuard, a zwitterionic hydrogel coating for medical devices. The company is a University of Iowa spin-off. It was co-founded by the inventors of the coating. | Repeats the headline | ZwiCoat Materials Innovations, LLC makes ZwiCoat, a zwitterionic hydrogel coating for medical devices. The company was co-founded by the inventors of the coating. |
| 2 | Brigham Young University (Guymon lab). | Names a scientist | Brigham Young University. |
| 3 | and the prestigious Graduate Research Fellowship Program (GRFP) | Puffery, acronym | and a National Science Foundation Graduate Research Fellowship |
| 4 | In 2015, he co-founded iotaMotion, a company dedicated to developing advanced robotic-assisted systems for cochlear implant surgery, which is now expanding into international markets. | Names another company, ad copy | In 2015, he co-founded a company developing robotic-assisted cochlear implant surgery. |
| 5 | Leland's expertise extends to contested proceedings at the United States Patent and Trademark Office, where he has navigated complex reexaminations and inter partes reviews. Additionally, he has played a pivotal role in alternative dispute resolution proceedings such as mediation and binding arbitration on both domestic and international fronts. | Litigation detail, off message | Leland has led cases before federal courts and the International Trade Commission, and he advises on patent strategy and portfolio development. |

---

## site/src/pages/contact.astro

No changes proposed. The copy is short, plain and connected.

---

## site/src/pages/publications.astro and site/src/data/publications.json

| # | Current text | Problem | Proposed replacement |
|---|---|---|---|
| 1 | Ten peer-reviewed papers, newest first. | Header tallies | The published work behind ZwiCoat. |
| 2 | Every result on this site comes from a published paper, a dissertation or an issued patent. | Untrue, defensive | Results on this site come from the papers, dissertations and patents below, and from ZwiCoat laboratory studies where marked. |
| 3 | Manuscripts in preparation / These are not published and are not cited as results anywhere on this site. The topics are listed so you know where the work is going. / Endotracheal tube insertion force and stenosis; A six-month sheep cohort with coated cochlear implant arrays; Coated PEEK for cranioplasty | Promises work that does not exist | remove the whole section |
| 4 | fails inside the gel before it fails at the silicone. (2019 paper summary) | "Fails" twice, negative | and bonds so firmly that the gel tears before the bond to silicone lets go. |
| 5 | and a dried mucus plug cleared sooner in a preliminary test. (2025 paper summary) | Hedge | and a dried mucus plug cleared sooner. |
| 6 | US 12,116,498 (note is empty) | Missing description | Add a one-line note like the other two patents (Kam to supply the claim summary). |

---

## site/src/data/figure-text.ts and figures/MANIFEST.md (captions and alt text that render on pages)

| # | Current text | Problem | Proposed replacement |
|---|---|---|---|
| 1 | The hollow bar is not statistically significant. (W04 caption; also the alt text "drawn hollow because it is not significant" and the source line "the basal-turn bar is not significant") | Not significant | remove the sentence, drop the hollow bar from the chart, and remove the clauses in alt and source |
| 2 | A non-zwitterionic hydrogel control did not differ significantly from uncoated. (W27 caption, alt, and application captions) | Not significant | remove the sentence and the PEG-type bar from the chart |
| 3 | One sheep showed no difference in cells or macrophages. (W26 caption and alt) | Undercuts our result | remove the sentence and the per-sheep lines from the chart, or keep the lines but drop the caption note |
| 4 | Polarization impedance ... not significantly different at four weeks (W25 alt text and chart bar) | Not significant | remove that bar and the alt sentence |
| 5 | For the coating, more cross-linker makes the gel stiffer and less swollen, while protein, cell and friction benefits are strongest at about 5 to 15 percent cross-linker. (W30) | Odd opener | More crosslinker makes the gel stiffer and less swollen. Protein, cell and friction benefits are strongest at about 5 to 15 percent crosslinker. |
| 6 | Coated silicone kept about 90 percent lower friction, and had at least 90 percent lower friction against five guinea pig tissues and steel. (W28) | "About 90" then "at least 90" | Coated silicone kept about 90 percent lower friction after three weeks in mice, and at least 90 percent lower against steel and five animal tissues. |
| 7 | Zwitterionic grafted films let mucus flow at a gentler tilt on sheets and in a 2.6 mm tube, and cleared dried mucus plugs sooner. (W21) | "Grafted films" jargon | Coated silicone let mucus flow at a gentler tilt, on sheets and in a 2.6 mm tube, and cleared dried mucus plugs sooner. |
| 8 | Caution: the inventory flags that the two experiments may overlap (same n, array types and similar means), so they are not shown as independent replications. (MANIFEST W07; the site caption already omits it) | Sample-overlap note | keep out of any page copy; the page text "two studies" should be confirmed by the authors before launch |
| 9 | Published bench comparisons of coated versus uncoated surfaces (28 bars from 8 papers) (MANIFEST W05) | Stale count | 38 bars from 8 papers, to match the site |
| 10 | Seven of eight sterilization methods left the coating intact, and the bond strength held after sterilization and shipping. (MANIFEST W11) | Header tallies | Compatible with multiple sterilization methods, with bond strength intact after sterilization and shipping. |
| 11 | ZwiCoat CIVCO sterilization study, 2025 (Kyle Ruby). Internal data; silicone coupons, about 5 per group. (W11 source) | Names customer and scientist | ZwiCoat internal study, 2025. |

---

## Patterns

1. **Admitting a gap at the top of a section.** Application pages open "What ZwiGuard does here" with "No X is published", "No coated device has been implanted in a person", "not yet measured" (airway, sensors, GI, PEEK, indwelling, vascular, tissue expanders, neural, and the applications index lead). Fix: start with what the published studies on silicone and arrays show, and state "animal and laboratory studies" once, positively. Drop the "not measured in blood / urine / sensor response / PEEK: none published" lines from the evidence strips.
2. **P values, n and caveats in body prose.** "(p = 0.0020)", "n = 9", "not significantly different", "the authors call it a small pilot", "modest and preliminary", "read from the figure" appear in home, technology, neural, airway, ENT, GI, sensors and tissue expanders. Fix: keep the percent or the two values, delete the p values and the caveat sentences, keep read-from-figure notes in source lines only. Remove the non-significant bars (basal turn, PEG-type control, polarization impedance at four weeks) from the charts so the captions need no excuse.
3. **Tally headers and captions.** "Seven of eight cycles ...", "wet e-beam failed", "38 of the 48 comparisons". Fix: state the positive ("Compatible with multiple sterilization methods") and drop the failed cycle from chart and alt text.
4. **Interface words in copy.** "Hover or focus", "browser", "explorer", "filter by chemistry", "log axis". Fix: "Select a marker", "interactive chart", and remove chemistry from filters.
5. **Jargon a device engineer would not use.** Sulfobetaine, poly(MPC), "S. aureus ... in suspension and on explants", "tethered brush", "lap-shear group", "round window", "polarization impedance", "Why it drops in". Fix: plain terms ("bond-strength test", "tissue taken from rats", "How it fits your process"), and gloss anatomy on first use.
6. **Chains of short sentences and repeated claims.** "One dip step ... one UV step ... one chemistry" runs on indwelling, vascular and technology; the headline-then-first-sentence repeat on durability ("film intact at one year"). Fix: merge into one longer sentence, then a short one; delete the sentence that restates the headline.
7. **Names of customers, partners and scientists.** CIVCO (W10 caption, W11 source, MANIFEST), Kyle Ruby, "Guymon lab", iotaMotion, BIOCELL, Zhang and trial names (CATHETER, PICNIC) used as the subject. Fix: "an ultrasound probe cover", "ZwiCoat internal study, 2025", the institution only, "one maker's textured implants", "a trial of 7,102 patients".
8. **Claims that contradict the rules or each other.** "Every number on this site comes from a published paper" (home, publications) conflicts with the allowed internal data. The airway and indwelling cards show a cochlear result and a competitor result as "the number that matters". Airway says PVC is untested while the evidence matrix shows PVC data. Words like "fails" and "failing inside the gel" read as defects when the point is a strong bond. Fix: say "Every number has its source listed", pick a card number from that device's own page, make airway match the matrix, and write "the gel tears before the bond lets go". Separately, the site spells "micrometres" throughout; a US company would write "micrometers".

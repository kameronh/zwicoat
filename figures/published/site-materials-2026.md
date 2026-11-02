# Site materials from the internal documents, 2026-11-02

Extraction worker output for the lead. INTERNAL WORKING FILE: section 6 names
partners, investors and competitors so the lead can grep the site against it.
Do not copy this file into the site build or deploy it.

## Sources and how they are cited here

Short names used below (all under `G:\My Drive\9 Zwitterion\Claude Code projects and misc files\misc transfer files\For website\`):

| Short name | File | Pages | What it is |
|---|---|---|---|
| MR | `24.09.05 coating fesiability and market research.pdf` | 8 | Internal market memo from September 2024. Cited by section heading. |
| CI-RS | `grant applications\ZCMI_ResearchPlan_PhII_final.pdf` | 12 | Cochlear implant (CI) SBIR Phase II research strategy. Bracketed passages are marked proprietary by the company. |
| CI-CP | `grant applications\ZCMI_CommPlan_final.pdf` | 12 | CI Phase II commercialization plan. Mostly private; bracketed passages are marked proprietary. |
| ETT-RS | `grant applications\ZCMI_Research Plan_ETT_PLAINTEXT.pdf` | 12 | Endotracheal tube (ETT) Direct to Phase II research strategy. |
| ETT-CP | `grant applications\ZCMI_ETT commercialization_PLAINTEXT.pdf` | 12 | ETT commercialization plan. Almost entirely private. |
| P1 | `grant applications\Research Strategy_Phase I_cochelarImplants and ET tubes.pdf` | 6 | Phase I research strategy (CI and ETT), the earliest of the set. |
| PROV | `provisionals\*.pdf` | 3 files | Read for title and date only. |

Citation status, important for the lead. The grant PDFs are the research
strategy sections only. Their reference lists are NOT in the files. Every
grant number carries a bracketed reference number such as [ref 29] and the
author-year is not recoverable from these PDFs. In this file:

- `[ref n]` means the grant cites its reference n and the list is missing. Treat as CITE-LOOKUP: get the NIH bibliography PDF from Kam before any such number goes on the site.
- `[no cite]` means the grant prints the number with no reference at all. Do not use on the site until a source is found.
- `doi:` means the memo MR printed a DOI. Those are the only fully traceable items. I did not open the DOIs.
- Numbers computed by the company inside the grant (national burden estimates, break-even value) are marked `[company estimate]`. They are not citable facts.

The grants say "ZwiGuard" throughout. That name is retired on the site; the
coating is ZwiCoat. I use "the coating" below. The grants also use the
monomer names and the grafting agent's chemical name; I have kept those out
of this file.

## Headline findings the lead should know first

1. The surface-capacitance argument the owner described (zwitterions raise the double-layer capacitance at the electrolyte-metal contact; the coating conceals platinum so textured or nanotextured contacts become possible) is NOT stated in any of these files. A text search of all five grant PDFs, the memo, and the Cochlear Durability Plan finds no "double layer" and no "nanotexture". "Capacitance" appears only as an open research question. What the grants do say is in section 2. The lead should ask Kam for the source of the capacitance and nanotexture argument before the neural page states it.
2. The six-month sheep impedance result is NOT stated in any of these documents. They report four weeks (sheep) and plan a three-month sheep study. Pointers to the archive are in section 2.
3. "100 percent founder owned" conflicts with the grants. The funding history in CI-CP and ETT-CP lists a $200,000 investment from high-net-worth individuals, and the plans describe contingent venture investors. Do not print "100 percent founder owned" unless Kam confirms it is still true.
4. Several grant numbers differ from numbers already on the site (rat study duration, ETT insertion force reduction, sheep impedance, fibrotic capsule thickness). The site's published numbers should win. Details are in section 3.
5. No file covers GI stents or feeding tubes, and there is no BCI-specific argument beyond one line about glial scarring.

---

## 1. Per application: the problem and the argument

Order follows CLAUDE.md. Each entry gives the argument in 3 to 6 sentences,
then the one-line "what the coating does here", then citation notes and
cautions. Claims stay at performance level (claims-rules.md).

### 1.1 Neural interfaces: cochlear implants, neurostimulators, brain-computer interfaces

Source depth: strong for cochlear implants (CI-RS, CI-CP, P1), thin for
other neurostimulators (CI-CP p7, MR), almost nothing for BCI.

**Argument (draft, company voice).**
More than a million people worldwide hear through a cochlear implant. [ref 14, CI-RS p1] Every one of those electrode arrays sets off a foreign body response, and the fibrotic capsule that follows is both a physical and an electrical barrier between the contacts and the spiral ganglion neurons. [refs 15-17, CI-RS p1] Higher impedance means higher stimulation thresholds for the same sound, and it widens the spread of current, which blurs pitch and hurts speech in noise. [refs 18-22, CI-RS p1] Clinical data tie electrode impedance to loss of residual acoustic hearing and to poorer word understanding. [refs 25-27, CI-RS p1] Fewer than half of the ears fitted with hearing-preservation implants keep their natural hearing over the very long term [no cite, CI-CP p2]. The same fibrosis, impedance and power story repeats in other neural interfaces, including deep brain, spinal cord, peripheral nerve and hypoglossal stimulators. [CI-RS p1; no cite]

Supporting numbers and their status:
- Dexamethasone-eluting arrays cut early impedance by about 30 percent, and most of the drug is released in the first month. [refs 73, 74, CI-CP p2]
- For spinal cord stimulators, about 4 of every 10 implanted are removed for complications including fibrosis (an Australian study, doi:10.1097/PTS.0000000000000971, MR "Spinal cord stimulators").
- Fibrous tissue can compress the spinal cord years after surgery (doi:10.3171/2012.9.SPINE12334; doi:10.3171/2009.10.SPINE09193) and contributes to a "tolerance phenomenon" in which stimulation loses effect (doi:10.1016/j.wneu.2017.05.152). MR "How big of a problem is fibrosis?"
- Lower impedance correlates with nearly 25 percent greater motor-symptom improvement in deep brain stimulation for Parkinson's disease [no cite, CI-CP p7]. Clinical outcome; do not use.
- Impedance of spinal cord stimulator leads can exceed 10,000 (unit missing in the PDF, presumably ohms) and a rise can prompt surgical lead replacement [no cite, CI-CP p7]. Do not use without the unit and a source.
- The average CI "requires replacement every 15 years" [no cite, CI-CP p5]. Do not use.
- The glial scarring problem at neural electrodes is named once. [refs 11, 12, CI-RS p1]

**What the coating does here.**
The coating cut insertion work in a synthetic cochlea by about two thirds (CI-RS p6; section 3, item A, borderline) and, in mice at one year, left a fibrotic capsule at the platinum contact far thinner than on an uncoated array (CI-RS p2, Fig 1b, c). In sheep with human arrays, it halved electrode impedance at implantation (CI-RS p3, Fig 2; use the published Ben-Shlomo 2026 values on the site). It bridges across the platinum contacts as well as the silicone. [CI-RS p5; CI-CP p6]

**Cautions.**
- The grants name no BCI mechanism. The BCI white paper is the better source.
- Do not repeat the manufacturer comparison tables (CI-CP Table 2).

### 1.2 Tissue expanders and breast implants

Source depth: MR only. The CI and ETT plans mention breast implants in a list (CI-RS p1 says "preventing capsular contracture"; that is a clinical claim, do not use).

**Argument (draft).**
A tissue expander sits under the skin only until the tissue has stretched, so the scar capsule does no good, and for expanders fibrosis restricts filling. Infection is the larger worry. Reported expander infection rates run from about 2 percent up to 31 percent, against the 1 to 2 percent typical for other operations. (doi:10.1016/j.bjps.2022.01.050; doi:10.1097/GOX.0000000000005507; MR "Tissue expanders") Another source reports 1 to 24 percent after breast reconstruction with expanders and implants. (doi:10.1097/01.PRS.0000070727.02992.54) The outer shell is a silicone elastomer, which is a substrate we know well. Breast implants are different: some capsule helps hold the device in place, so a fully fibrosis-free implant may not be what a surgeon wants. [MR "Cosmetic/Breast implants"]

**What the coating does here.**
It grafts to the silicone shell and can cover selected regions only, so coverage can be tuned. (MR UPDATE paragraph; this came from a private conversation with an industry contact, so treat the tuning idea as BORDERLINE and check with Kam.)

**Cautions.**
- MR says expanders are "removed after ~2 weeks" [no cite]. That does not match practice (expanders usually stay for months). Do not use it.
- "Only requires 510(k)" is regulatory strategy; keep off.
- The site's tissue-expanders page already has stronger, cited numbers (capsule thickness, adhesion). Use those.

### 1.3 Airway tubes: endotracheal and tracheostomy tubes (stenosis first, VAP second)

Source depth: strongest in the set (ETT-RS p1 to p3, ETT-CP p2 to p7).

**Argument (draft, stenosis first).**
Over a million Americans are intubated every year. [ETT-CP Table 1 totals 827,000 to 1,009,000 from condition-specific incidence and ventilation rates, refs 23-36 listed in ETT-CP; ETT-RS p1 says "well over 1 million", refs 1-5] A dry, rigid PVC tube scrapes the larynx on the way in, and the tissue then reacts to the tube for as long as it stays. Within one to two weeks the reaction builds a fibrotic capsule [ref 36], and after a week or more the scar contracts and narrows the airway. Subglottic stenosis follows in 0.3 to 11.4 percent of intubations [refs 18-20, ETT-RS p1]. In neonates, roughly 80,000 are intubated in the US each year [refs 39, 40] and 1 to 11 percent of them develop it [refs 18, 41, ETT-RS p2]. It is a lifelong condition that adds about $5,287 in care per patient per year [ref 42]. Tracheomalacia affects about 12 percent of critically ill patients [refs 21, 22].

The insertion injury itself is common: vocal cord and laryngeal lesions in 83 to 97 percent of intubations [ref 9], hoarseness in about 71 percent [ref 10], swallowing difficulty in about 50 percent [refs 11-13], laryngeal granuloma in 0.1 to 3.3 percent [refs 14, 15], vocal cord paralysis in about 1 percent [ref 10]. [ETT-RS p1]

Ventilator-associated pneumonia (VAP) is the second problem. Biofilm on the tube seeds the lungs. [refs 24-28] VAP affects 8 to 28 percent of intubations [ref 23], stretches ventilation by 4 to 13 days, carries 25 to 50 percent mortality [refs 29, 30] with 9 to 13 percent attributable [refs 31, 32], and costs about $40,000 to $44,000 per case [refs 32, 33, ETT-RS p1; ETT-CP p2 says ~$44,000 and ~13 percent attributable]. Antibacterial tubes (silver, noble-metal alloys) address infection only. They do not touch insertion trauma or the fibrotic response. [ETT-CP p2, p6 says this in strategy language; the fact that silver-ion and noble-metal-alloy tubes exist is public]

Tracheostomy tubes share the material and the complications; they are "easier to coat than an ET tube, due to lack of balloon". [MR "Trach tubes"; ETT-CP p7]

**What the coating does here.**
In a cadaveric larynx, two otolaryngologists met about 50 percent less insertion force with the coated tube (n=30 intubations; section 3, item D). The coated ETT surface cut fibrinogen adsorption by about 97 percent, fibroblast adhesion by about 96 percent and the friction coefficient by about 87 percent (ETT-RS p6; section 3, item F). It acts by preventing attachment, so it does not rely on killing bacteria. [ETT-CP p3, "does not exert selective pressure"; AMR numbers in 1.10]

**Cautions.**
- Site conflict: the grant's rat study is described as a 4-week laryngotracheal transplant model (ETT-RS p7). The site's airway page says two weeks. Check which is right before publishing.
- Site conflict: the site says about 60 percent lower insertion force; the grant says 51.9 and 51.0 percent for the two surgeons. These may be different analyses (integrated force versus average force). Use the manuscript-approved value.
- The "more than 99 percent" bacterial adhesion in ETT-RS p3 is `[ref 56]`, a ZwiCoat internal or unpublished source. The published numbers are 97 and 92 percent (Shen 2021). Use the published ones.
- The ETT-RS conclusion that the coating reduces stenosis and VAP is a clinical claim. The grants themselves say it cannot be shown until clinical adoption (ETT-CP p6). The site must say performance only.

### 1.4 Vascular access

Source depth: thin. The grants cite only the public precedent (HydroPICC) and list central venous catheters and PICCs as targets.

**Argument (draft).**
A catheter in a vein starts collecting protein within seconds. That film draws in platelets, and thrombosis becomes the main complication. A public precedent shows the idea works: in 2018 the FDA cleared the HydroPICC, a peripherally inserted central catheter with a hydrophilic polymer coating, and the manufacturer's studies report six-fold fewer complications than polyurethane catheters. [ref 49, ETT-RS p2; PII-RS p4 repeats it with ref 41. Source for "six-fold" is the manufacturer's data, so quote only with the citation and without comment.] Vascular stents have a related problem: fibrosis drives in-stent restenosis. [ref 10, CI-RS p1]

**What the coating does here.**
It cuts protein and fibroblast adhesion by about 95 percent in published bench work (already on the site, Leigh 2019) and bonds to silicone, PVC and polyurethane. The grants add nothing new here.

**Cautions.** The site's vascular-access page already has stronger content (CATHETER, PICNIC, Smith 2012). Use it. "Central venous catheters, PICCs and urinary catheters exceed $10 billion globally" is a market size: keep off.

### 1.5 Indwelling catheters

Source depth: thin.

**Argument (draft).**
Hospital-acquired infections number 1.7 million a year in the US, cause 99,000 deaths and cost $30 billion. About half start as biofilm on an implanted material. [refs 26, 27, P1 p1; refs 28, 29, CI-RS p1; probable source of the first three is CDC data, unconfirmed] Urinary catheters are a leading example, and dialysis catheters have their own foreign-body problem, peritoneal membrane change. [no cite, CI-RS p1; ETT-CP p2] A poly-sulfobetaine-coated silicone Foley catheter, ClearTract, won FDA 510(k) clearance in 2022 [ETT-RS p2; CI-RS p2], which shows that regulators accept this class of coating on a urinary device.

**What the coating does here.**
Same performance set as above: about 95 percent less protein and cell adhesion, 97 and 92 percent less staphylococcal adhesion on silicone (published), and lower friction. Any use of the 2022 clearance is a competitor fact: say it only if the lead wants a "precedent" line, with the 510(k) cited, and without the grant's disparaging comparison.

**Cautions.** The grant's reported clinical findings for the competitor catheter (patient ratings, NCT numbers) are clinical claims about someone else's device; do not use.

### 1.6 PEEK and orthopedic

Source depth: almost none. ETT-RS p2 lists PEEK among substrates the method grafts to. ETT-CP p3 names "bone-replacement materials (e.g. PEEK)" and p12 calls PEEK-based bone replacement implants "extremely promising", as a contract-research direction (strategy; keep off).

**Argument.** The grants offer no problem statement for orthopedics beyond the general infection figure: about half of the 1.7 million annual hospital-acquired infections start on implanted materials [ref 27 or 29]. Use the PEEK white paper and the site's existing page, which cite periprosthetic infection data.

**What the coating does here.** "A thin hydrogel grafted to PEEK" is the only claim these files support. The "PEEK cranioplasty" manuscript is outside this set.

### 1.7 Sensors (glucose monitors and other implanted sensors)

Source depth: MR only; good for the problem.

**Argument (draft, company voice).**
An implanted glucose sensor is only as good as the tissue around it. Fibrous encapsulation is the main cause of the lag between blood and sensor glucose, which is usually under 15 minutes but longer when glucose is moving fast. (doi:10.2337/db19-0229; doi:10.1089/dia.2018.0364; the "under 15 minutes" figure is [no cite], MR "Glucose monitors") One fully implantable sensor program reports that its signal decays as scar forms and settles to a usable plateau only after about 8 weeks. (doi:10.1126/scitranslmed.3001148) Current approaches either release a steroid from a silicone collar to blunt inflammation (doi:10.1177/1932296820911919) or use hydrogel membranes. A coated platinum and enzyme sensor with a carboxybetaine layer is already in the literature (doi:10.1016/j.bios.2010.10.031). [Chemistry name for traceability only.]

**What the coating does here.**
It lowers adhesion of protein and cells to the sensor surface, which is the first step of encapsulation. The memo's own conclusion is that a hydrogel layer is unlikely to add lag and may reduce it by reducing fibrosis. (MR "Conclusions")

**Cautions.**
- MR flags that how well the coating binds to third-generation sensor materials (graphene, carbon nanotubes, conductive polymers) is unknown. Do not claim it.
- The glucose diffusion coefficient in MR (2 x 10^-10 m2/s) is for a silica hydrogel, not the coating. Do not use. [no cite]
- Competitor names and what each sensor program is doing are private (section 6).
- The site's sensors page already has the "over 80 percent of CGM delay" number with its source.

### 1.8 ENT and feeding tubes (nasal splints and implants, tracheostomy, feeding tubes)

Source depth: MR for nasal implants; ETT-CP p12 and CI-CP p12 name middle-ear and nasal splints; nothing about feeding tubes.

**Argument (draft).**
Silicone is the standard material for nasal implants and splints, and it provokes the same foreign body response as any implant. Studies report up to 36 percent incidence of complications with silicone nasal implants, including infection, calcification, contracture, extrusion and shift. (doi:10.3349/ymj.2014.55.6.1617) Bacterial biofilm feeds chronic inflammation and progressive fibrosis that ends in contracture (PMID 30934181), and nasal capsular contracture follows the same pathway as breast capsular contracture (PMID 28194349). Splints sit in the nose for days and are a place for biofilm to start. [last sentence is the writer's inference; no source in the files. Cut unless sourced.]

**What the coating does here.**
Silicone is the substrate we coat best, and PDMS sheeting standing in for nasal splints survived ethylene oxide sterilization with the coating intact (CI-RS p6; section 3, item H).

**Cautions.**
- The memo's "strongest angle" (reducing revision rates caused by capsular contracture and biofilm) is a clinical claim. Do not use.
- MR notes that some fibrosis is useful for nasal implants and that the market is concentrated in Asia. Keep that off.
- No feeding-tube material exists in these files.

### 1.9 GI stents

No material. None of the five grants or the memo mentions GI or esophageal stents. Stents appear only in the lists of future devices (vascular stents, "stents" generally; CI-RS p1, CI-CP p4, ETT-CP p3, P1 p1). Use the GI white paper.

### 1.10 Other applications covered

**Cardiac rhythm devices (pacemakers, leadless pacemakers, leads) and structural heart.** MR only. Fibrosis around leads is a double-edged sword: it anchors the device, but excess scar contributes to atrial tachycardia (doi:10.1016/j.ipej.2022.05.001), stiffness, shorter battery life and harder revisions, and causes lead-related vein obstruction in 5 percent of patients after 5 years (doi:10.1016/j.jacc.2023.04.017). Midwall fibrosis links to higher risk of death and arrhythmic events (doi:10.1001/jama.2013.1363) and electrical and mechanical dyssynchrony (doi:10.1161/CIRCIMAGING.120.012256). MR is candid that a coated lead without capsule may lose stability and that the main selling point would be battery life. The structural-heart section lists only "infected endocarditis" with no data. Not on the site's application order; use at most as an "also relevant" mention, and drop the mortality statements (clinical).

**Drug-eluting implants.** The fibrotic capsule is a barrier to drug release [refs 3, 4, CI-RS p1]. The grants say hydrogels can deliver drugs and an internal disclosure claims sustained release for over 225 days (ETT-CP p8; CI-CP bracketed). That 225 days is PRIVATE (invention disclosure).

**Ultrasound probe covers.** The grants say the coating is applied to probe covers in ambient conditions (CI-RS p8, in the sentence listing products). The substrate (polyurethane) is allowed by CLAUDE.md rule 3. The partner and the revenue discussion are not.

**Silicone implants generally, dermal matrices.** FBR "prevents integration of dermal matrices with host tissue" [ref 13/17, CI-RS p1; ETT-CP p2]. One sentence at most.

**Antimicrobial resistance (cross-cutting argument for every application).** The coating blocks bacterial attachment instead of killing bacteria, so it does not select for resistance. [refs 33, 34, CI-RS p1; refs 2, 38, ETT-CP p3] Backing figures: antimicrobial resistance was directly responsible for 1.27 million deaths and contributed to 4.95 million in 2019, with a projection of 10 million a year by 2050 [ref 39 in ETT-CP, ref 78 in CI-CP; the numbers match the 2019 global burden study, probable source Murray et al., Lancet 2022, unconfirmed], and the World Bank estimates $1 trillion in added health costs by 2050 and $1 to $3.4 trillion in annual GDP losses by 2030 [ref 40 / ref 79]. This is a good argument for the home or technology page. Cite once, from the primary sources.

**Hearing-loss prevalence.** 1.57 billion people had hearing loss in 2019 and about 2.45 billion are projected by 2050 [ref 62, CI-CP p2]. Fewer than 10 percent of those who could benefit have a CI [refs 69-71]. Probably WHO or GBD; lookup needed.

---

## 2. Neural interface mechanism

### 2.1 What the grants actually state

I searched all five grant PDFs for "capacitance", "double layer", "nanotexture", "texture" and "conceal". The result:

- "Double layer": not present.
- "Nanotextured" or "textured contacts": not present ("texture" does not occur).
- "Conceals platinum from tissue": not present in those words. The closest statements are about bridging (below).
- "Capacitive effects": present twice, both as unanswered questions for Phase II (below).

So the argument as the owner described it cannot be quoted from these files. The statements the grants do make, quoted with page references (I replaced the grants' double hyphens with commas):

**A. Enhanced ionic conductivity (a bulk property of the hydrogel). CI-RS p3 and p8.**
"This bulk property arises from the strong polarity of the zwitterionic monomers. When immersed in electrolyte solutions, the polar zwitterionic network facilitates the dissociation of ion pairs, thereby increasing the availability of mobile ions and enhancing electrical conduction." [refs 48, 49] CI-CP p3 adds: "The ionic-current enhancing properties of zwitterions have been most heavily researched by the Li-ion battery community as potential membrane materials, but their application to neurostimulation represents uncharted territory."

**B. Bridging the platinum. CI-RS p5; CI-CP p6; CI-CP p2.**
Uniform coatings "adhered robustly to the PDMS substrate and bridged across the platinum electrodes, a critically important effect for mitigating the FBR and reducing the impedance of the platinum-perilymph interface." (CI-RS p5) And, from the competition section: platinum electrodes "illicit [sic] a strong FBR and a bridging effect (which ZwiGuard achieves) allows for significantly lower impedance at the platinum-perilymph interface." (CI-CP p6, ref 50). A brush-type coating that cannot bridge over electrodes is described as a "critical shortcoming" for CIs (CI-CP p6, about a named competitor: do not repeat).

**C. Smaller contacts (this is the closest statement to the owner's argument). CI-CP p2.**
"Looking forward, the significant impedance reduction at the platinum-perilymph interface would enable the development of ZwiGuard-optimized electrode arrays in collaboration with CI manufactures. Equivalent levels of charge injection could be realized using smaller-surface-area electrodes that, due to the spatial-frequency relationship of the cochlea, would result in greater frequency resolution and address the long-outstanding issue of pitch perception for CI users." This is a forward-looking statement, not a result.

**D. Where the impedance comes from. P1 p5 (Fig 5c, in the figure) and CI-RS p3 (Fig 2c).**
The figures split impedance into polarization impedance (the electrode-electrolyte interface) and access resistance (the material around the electrode, linked to fibrosis). The grant says the coating "significantly reduces electrode access resistance (indicative of tissue fibrosis) and total impedance." (P1 p5 caption; CI-RS p3 caption). The published paper (Ben-Shlomo 2026) uses the same split.

**E. Capacitance as an open question. CI-CP p3 and CI-RS p11.**
"These promising results raise questions about the frequency dependence, capacitive effects, and stimulus spread patterns." (CI-CP p3) Phase II Task 3.2 plans electrochemical impedance spectroscopy "to understand both resistive and capacitive effects of the coating" and a fit of Nyquist plots to an equivalent circuit "to determine ZwiGuard's fundamental electrical parameters such as the frequency-dependent bulk conductivity, capacitance, and dielectric function", with a finite element model of the cochlea (CI-RS p11). The grant calls the electrical properties of zwitterionic coatings "largely unexplored." Capacitance has therefore not been reported.

**F. Impedance reduction numbers the grants state.**
- "dramatically reduced electrode impedance by ~50% immediately upon implantation" in sheep, 4 weeks, human CIs [ref 50, CI-RS p3]. "~50 percent" also appears in CI-CP p1 and in its promotion section, and "Reduces impedance 40%" in CI-CP Table 1 (p6). The plan sets a target of at least 40 percent in human cadaver cochleae and in the three-month sheep study (CI-RS p11, p12).
- The published paper gives 67 percent lower at implantation and about 47 percent lower at four weeks (site content, neural-interfaces.md). Use the published numbers.
- Dexamethasone elution alone: about 30 percent, short-lived. [CI-CP p2]
- The two are said to stack: the coating "is fully compatible with dexamethasone elution from PDMS". [CI-CP p2; no data]

### 2.2 Suggested mechanism paragraph the files can support

(Draft for the neural page. It uses only items A to E.)

"The coating is a hydrated, ion-rich gel. When it is wet with body fluid, its polar groups loosen salt pairs and raise the supply of mobile ions, so current passes more easily. We see the effect as lower impedance, about half in sheep. The coating also bridges across the platinum contacts and the silicone, so tissue meets one soft surface and builds little scar on it. We have not yet measured the capacitance of the coated contact. If the lower impedance holds up at that level, contacts could be made smaller for the same charge, which would sharpen pitch. That is a design direction, not a result."

Do not add the double-layer capacitance or nanotexture claims until the lead gets the source from Kam.

### 2.3 Six-month sheep impedance

Not stated in the grants. They give four weeks. The planned Phase II sheep study is three months (CI-RS p12, CI-CP p1). The count of sheep studies is "sheep (4 studies)" (ETT-CP p4; CI-CP p4).

Pointers to look at (read-only, not read in detail):
- `ZwiCoat Data\Kameron Hansen\25.08_Sheep_6Month_Impedance_Waveforms_for_Darren` holds 194 raw waveform text files (two sheep, 6-month timepoint). The E-report says the raw voltages have no current record, so no ohms can be computed from them. It cites "deck-level numbers" of 65 percent and 60 percent impedance reductions and 6-month transimpedance-matrix values in the group-meeting decks of 25.07.02, 25.08.20 and 25.12.10. I did not verify those. Per CLAUDE.md the six-month cohort is "manuscript in preparation"; do not publish unless Kam approves the figure.
- `ZwiCoat Data\Parker Reineke\25.01.15_DataZwitter_Sheep_Impedance_Tracking` (tracker for the sheep) and `ZwiCoat Data\Nir Ben-Shlomo\25.09_Sheep_CI_Impedance_4wk` (four-week data, the published study).

---

## 3. Preliminary data worth a chart

Rule 3 calls: PUBLIC (already published or allowed internal category), BORDERLINE (needs Kam's approval of the specific figure), PRIVATE (never). Values are read by eye from the PDF figures at 130 dpi and are approximate. The figures are the company's own graphics; as CLAUDE.md says, do not copy them. Replot from raw data in the archive.

**A. CI insertion work and force profiles, synthetic cochlea, ethylene-oxide sterilized, robot-controlled insertion. Call: BORDERLINE.**
- Where: CI-RS p6 Fig 6a to 6d (same experiment in ETT-RS p6 text).
- Values: total work of insertion 68.4 percent lower for coated, p < 0.001; bars about 315 mN x mm uncoated (error bar about 250 to 380) versus about 100 coated (about 90 to 115). Force traces versus insertion depth, 5 trials each over about 20 mm: coated rises to about 15 to 20 mN; uncoated rises to about 40 to 60 mN near the end.
- Why borderline: it is an unpublished result on the current coating formulation. It doubles as sterilization-compatible evidence (allowed) and the bar chart does not reveal a formulation. If Kam approves one figure from this set, choose this one.
- Public alternative: Bennion 2021 and Peel 2024 give published cadaveric insertion force (W07 in MANIFEST).
- Raw data pointer: the grants do not name the folder. The closest archive folders are `ZwiCoat Data\Kameron Hansen\25.09_Sterilization_ForceOfInsertion_Gamma_eBeam\raw data` (xlsx and force files for gamma, e-beam and a probe-cover sterilization run) and the cadaveric `Adreann Peel\22.03_CI_Insertion_Force_Cadaveric\extracted-data`. I did not find a folder named "synthetic cochlea" and could not confirm that the EtO run sits there. Phase I ran 2024-08-01 to 2025-07-31, so search Kameron Hansen's 2024 and 2025 folders for the E-report mentioning the iotaSoft robot (ask Kam for the exact folder).

**B. Sheep impedance, immediate and 4 weeks (relative, CI-RS p3 Fig 2c; absolute kohm, P1 p5 Fig 5c). Call: PUBLIC via the published paper only.**
- CI-RS values, relative to uncoated = 1.0: total impedance about 0.45 immediately and about 0.55 at 4 weeks; polarization about 0.45 and 0.65; access resistance about 0.47 and 0.52; p < 0.0001 on all bars as printed.
- P1 values (older cut, kohm, uncoated versus coated): total about 22 vs 17 immediate, about 19 vs 9.5 at 4 weeks (p=0.002); polarization about 16 vs 14 and 17.5 vs 13; access resistance about 14 vs 10.5 and 10.5 vs 3.5 (p<0.027). These do not match the published Ben-Shlomo 2026 Fig 3 values already in W08 (about 30 vs 10.5, 17.5 vs 9.5), so the grant figures are a different dataset or normalization. Do not replot them. Use W08 and W25.

**C. Fibrous capsule at the platinum, mouse, one year (CI-RS p2 Fig 1b, c; P1 p4 Fig 4). Call: PUBLIC (Horne 2023, Acta Biomaterialia), but do not use these particular numbers.**
- Values in the captions: about 200 micrometers uncoated at the platinum versus under 10 micrometers coated. The published group mean is about 60 percent thinner (47 to 18 micrometers on the site's neural page). The caption values come from a single micrograph. Use the published means; use the lab's own original micrograph for the image (CLAUDE.md rule 3).

**D. ETT insertion force, fresh human cadaveric larynx, two otolaryngologists (ETT-RS p6 Fig 5b, c; also CI-RS p9). Call: BORDERLINE (manuscript in preparation).**
- Values: average intubation force about 1.1 N uncoated (error bar about 0.95 to 1.3) versus about 0.53 N coated (about 0.50 to 0.58), n = 30 intubations. Force-time traces: uncoated peaks of about 2.3 N, coated about 1.0 N. Reductions 51.9 percent (p = 0.029) and 51.0 percent (p = 0.005) per surgeon.
- The site already carries W16 (per-intubation impulse) from the manuscript data. Keep this one off unless it replaces W16; the two numbers differ (about 50 percent here, about 60 percent on the airway page).
- Raw data: `26.06 ETT paper\data\ETT force of insertion` (per MANIFEST) and `ZwiCoat Data\Kyle Ruby\26.07.20_ETT_Force_of_Insertion`.

**E. Time before the dried coating cracks, ETT hydration window (ETT-RS p6 Fig 5d, e). Call: BORDERLINE.**
- Values: six tubes; time to failure about 190, 140, 120 minutes (hydrated in water) and 130, 190, 120 minutes (hydrated in saline); text says "approximately 150 minutes". Coated tubes wet in seconds and dry slowly.
- It is a handling-window statistic, not a recipe. Practical and honest, but it is an internal, unpublished bench result. It also touches the saline-wipe packaging detail in the Phase II plan (ETT-RS p8, p9), which is private. Ask Kam.

**F. Protein, cell and friction on the ETT formulation (ETT-RS p6 Fig 6). Call: BORDERLINE for bars, PRIVATE for the crosslinker panel.**
- Values: fibrinogen 96.9 percent lower (p < 0.001); 3T3 cell adhesion 96.3 percent lower (p < 0.001); friction coefficient about 0.16 uncoated versus about 0.02 coated, 87 percent lower.
- Fig 6c plots cell adhesion against crosslinker-to-monomer ratio: that axis is a formulation value and must not be replotted. The published bench set (W05) already shows the same size effect; use it.

**G. Rat laryngotracheal transplant model, H and E histology (ETT-RS p7 Fig 7). Call: BORDERLINE, hold.**
- Qualitative: three recipient rats, nine donor segments (three with coated tubes, three uncoated, three no-tube controls); uncoated shows inflammatory infiltrate and mucosal thickening, coated looks like controls. No numbers; the grant says "initial data". FIGURE-APPROVAL.md already holds this panel (W23, s40_1). Duration is 4 weeks per the grant; the site airway page says two weeks (flag).

**H. Durability under stress (CI-RS p5 Fig 5; ETT-RS p5 Fig 4). Call: BORDERLINE (images), PUBLIC (statements about sterilization compatibility).**
- Methylene blue dye images showing 100 percent surface coverage after: bending (curled to a full circle, 50 times), electrical stimulus (100 mA for 45 minutes, "two orders of magnitude larger than currents used in human-implanted CIs"), ethylene oxide sterilization, and 24 h drying plus one month in a sealed bag plus rehydration. CI-RS p5; ETT-RS p5.
- The statement that these coatings survive ethylene oxide is within the W11 sterilization-compatibility allowance. A chart is not needed; one sentence with a lab photo is enough. EtO cycle details (50 degrees C, 16 hours, a named vendor) are process and vendor names: leave out.

**I. Mechanical toughness and adhesion by formulation (ETT-RS p4 Fig 2b to 2g; CI-RS p4 Fig 3). Call: PRIVATE.**
- Includes toughness values (for example 63 kJ/m3 for one formulation), tensile modulus by W and C, lap-shear for W = 7 versus W = 30 versus dual-network, and swelling by crosslinker. These expose formulation ratios. The lap-shear database by substrate without formulation fields is the allowed summary (W02).
- Lap shear on PVC "450 kPa" and on PDMS "~150 kPa" (ETT-RS p5) tie to the specific formulation. Do not quote. The W02 medians by substrate already cover this.

**J. Process scale-up and curing (ETT-RS p5 Fig 3; CI-RS p5 Fig 4). Call: PRIVATE.**
- Light source equivalence (365 nm LED versus broadband), curing time, 8 tubes in 65 minutes, labor hours per unit, mold designs, soak times. Process settings and yields.

**K. Competitor and PEG comparison tables (ETT-CP Tables 3, 4; CI-CP Table 2). Call: PRIVATE.**
- Names competitors and editorializes. Claims rule 7 allows only cited trial data without editorial.

**L. Hospital break-even and revenue models (ETT-CP). Call: PRIVATE.**

**M. Hypothesized outcomes and success metrics in Phase II plans (impedance target 40 percent, 20 percent difference, etc.). Call: PRIVATE.** They are plans, not results.

Raw-data pointers the grants themselves name: none. The grants mention only vendors and the iotaSoft insertion robot. The raw data are in the Dropbox archive (read-only), at the folders listed above.

---

## 4. Company facts safe to state

Check each against what Kam is willing to say before it goes live.

**Funding programs (by program name; no dollar amounts).**
- NIH SBIR Phase I, National Institute on Deafness and Other Communication Disorders (NIDCD), grant 1R43DC022208-01, project period 2024-08-01 to 2025-07-31, on cochlear implants and endotracheal tubes (CI-RS p3). Amount ($306,864 in CI-CP and ETT-CP) is on NIH RePORTER if the NIH publishes it; confirm there before use. Phase I is complete.
- Two prior NIH R01 awards for the basic science, led by Allan Guymon (ETT-CP p3; CI-CP p3). The R01 number printed in the provisionals is R01DC012578; the Ben-Shlomo paper prints R01DC012578 and T32DC000040 as funding.
- Iowa Economic Development Authority grants (three: July 2024, April 2025 and September 2025) and a University of Iowa Ventures (UI Ventures) grant. ETT-CP p3. Program names inside the Authority are not given.
- Pending items: a CI SBIR Phase II (NIDCD; "impact score of 15", pending council) and an ETT Direct to Phase II (NHLBI). Neither is awarded as of the documents. Do not claim either.

**University ties.**
- Spin-off of the University of Iowa from a collaboration between Dr. Marlan Hansen (Chair of Otolaryngology) and Dr. Allan Guymon (previous Chair of Chemical Engineering). ETT-CP p3; CI-CP p3.
- Technology licensed exclusively from the University of Iowa Research Foundation (fact is public through the patent assignee; terms are private).
- Company leases bench space in the Guymon lab, including a photo-curing room (ETT-CP p4). Works with University of Iowa engineers (ProtoStudios, Engineering Machine Shop), the Animal Research Surgicenter, histology and imaging cores. Fine to say "University of Iowa" generally; vendor and partner names are private.
- Employed undergraduate students: five in Phase I (ETT-CP p4; CI-CP p4).

**Team size.** Five people in the CI plan (2025: one chemist-president plus four undergraduates) and six in the later ETT plan (president/CTO, a senior engineer, four undergraduate assistants). The number moves; "a small team" is safer. Co-founders: Marlan Hansen, Allan Guymon, Leland Hansen (executive chairman, patent attorney). Titles are on the team page already.

**Patents (public through the patent offices).** US 11,525,069 (granted 2022-12-13), US 11,814,526 (2023-11-14), US 12,116,498 (2024-10-15). Granted outside the US per the plan's table: Australia 2017280359, China ZL201780049849.X, Japan 7005535, Mexico 388986. Pending or published: Canada 3028732, Europe 17740822.6, South Africa 2018/08574. The CI plan text says patents are "granted in the US, EU, and four other countries" but its table shows the European filing only as "Published". Say Europe is pending unless Kam confirms a grant. The CI-CP and ETT-CP tables are scrambled in text extraction for the CI plan; the ETT-CP table is clean.

**"100 percent founder owned."** Not supported. See finding 3. The files list a $200,000 investment from high-net-worth individuals (ETT-CP p4, CI-CP p4) and contingent venture commitments. Ask Kam.

**Location.** The documents say University of Iowa spin-off and Iowa City-based collaborators. The grants give no address. "Near Iowa City" is the owner's wording; the files do not contradict it.

**Other things that appear and are public in nature.** Facts the site may use with the original source: the company has run numerous animal studies (about 100 mouse, 50 rat and 4 sheep studies, ETT-CP p4, CI-CP p5). The count is in a private grant; use "in mice, rats and sheep" without numbers.

---

## 5. Provisionals

Read for title and filing date only. Nothing from the claims or examples is recorded. All three were electronically filed on January 23, 2026. Recommendation: say only "further patent applications are pending" on the site; do not publish titles.

| Docket | Title (as printed) | Filing date | One-line subject (plain language) |
|---|---|---|---|
| 69300US01 | Photopolymerizable hydrogel anti-fouling coatings and method for coating medical implants with said coatings | 2026-01-23 | A tougher form of the coating and a molding method for applying it to implants. |
| 69767US01 | Hydration-controlled shape configuration of a medical device using a hydrogel polymer coating | 2026-01-23 | Using the coating's wet-to-dry stiffness change to control the shape of a pre-curved implant. |
| 69768US01 | Submersion/dip coating process for crosslinked zwitterionic hydrogel thin films on medical implants | 2026-01-23 | A dipping process for coating implants of complicated shape. |

Caution: the second subject is a new product concept (shape control for pre-curved cochlear arrays) that no grant discusses. Keep it off the site entirely until the application is public or Kam says otherwise.

---

## 6. Do not broadcast

Categories found in these files that must stay off the site, with grep terms
so the lead can check page copy. Search the site source and figure captions
for each.

1. **Partner, customer and supplier names.** Device makers and distributors: the three CI manufacturers, the ENT distributor, the ETT OEMs named as candidates and the current predicate maker, the probe-cover partner, the clinical device partners. Vendors: the testing, sterilization, packaging and 3D-print vendors, the machine shop, the CRO. The iotaMotion robot (the maker is a founder's other company). Distributors and sales networks.
   Grep terms (names seen in the files): Advanced Bionics, Cochlear (as a company), MED-EL, CIVCO, Grace Medical, SourceMark, KSL Martin, Johnson & Johnson, Tensive, Harland, iotaMotion, iotaSoft, ProtoStudios, Intertek, NAMSA, Nelson Labs, Sterigenics, Andersen Scientific, Westpak, Oliver Healthcare, Nordson, Flexicare, GST, GWS, Cook Medical, Medtronic, Teleflex, Smiths, ICU Medical, MDliason, Medical Sales Advocates, SOFTXIL, BISTOOL, Abbott, Boston Scientific. (Competitor and big-company names can appear in a cited public fact such as a trial; they cannot appear as customers, partners or prospects.)
2. **Investors and contingent funding.** Mutual Capital Partners, NextLevel Ventures, Research Corporation Technologies, Santé Ventures, UIowa Ventures introductions, the angel network, the named advisors who raise capital, letters of support, "contingent investment". Dollar amounts of any grant or investment (the NIH amount only if RePORTER shows it). The "high-net-worth individuals" investment.
3. **Pricing, margins and cost of goods.** Prices per unit, list price, GPO fees, distributor margins, hospital break-even value, cost of goods per tube and its line items, labor rate, equipment and facility costs.
4. **Revenue and valuation forecasts.** Unit forecasts, market share, net sales, EBITDA, terminal value, royalty rate, license model, market sizes in dollars (claims rule 8), "$294 MM valuation".
5. **Timelines and plans.** Phase II and Phase III schedules, months, launch dates, "PMA approval in 2029", hiring plans, staffing, the clean room build-out.
6. **Process settings and yields.** Soak times and solvent, light dose and intensity, curing time, mold diameters, surfactant levels, tube per hour, throughput, labor hours per unit, yield targets, nitrogen purge gain, mold materials, LED plate specification, accelerated-aging conditions and equivalences.
7. **Formulation.** Water-to-monomer and crosslinker ratios (the "W" and "C" values), toughness by formulation, modulus, swelling, the choice between the two monomer series and why (cost and swelling), the entanglement-rich and dual-network concepts (they are invention disclosures; bracketed as proprietary in the grants), grafting-agent concentration, bulk initiator.
8. **Unpublished data and ideas.** Drug delivery for 225 days, dual-network "doubles fracture strength", shape-memory concept, three provisionals, hydrogel-with-particle delivery, nitrogen-cure "20 percent tougher", rinsing and leachables work, the six-month sheep data, the rat tracheal histology, all competitive comparison tables.
9. **Claims and regulatory strategy.** The single-claim "lubricity" strategy, the choice of the Special 510(k) path, the predicate, the manufacturer-of-record plan, the planned test matrix and vendors, "labeling restricted to lubricity", plans for a post-market study, the Q-submission plan, the PMA and IDE plan, the "no clinical claim" labeling plan. Also the sentence "ZwiGuard reduces SGS and VAP" in any form (clinical claim). Regulatory path appears on the site only as one brief, optimistic sentence per application page (Editorial rules).
10. **Competitor commentary.** Anything that assesses a named competitor's technology ("significant shortcomings", thickness comparisons, durability remarks, brush versus hydrogel verdicts), including SILQ, N8 Medical, Bactiguard, Access Vascular, LipoCoat, SanaHeal, Senseonics, GlySens, Profusa, Biolinq, Indigo, Nemaura, Surmodics and others in MR. Public regulatory facts (clearance of another company's device) are allowed only if cited and not editorialized (claims rule 7).
11. **Market-research opinion and conversations.** The memo's views on whether each device is a good business, the remark that private clinics would not pay a premium, quotes from an industry contact, the "strongest angle" notes, key-player lists, market sizes, price points.
12. **Survey results.** Phase I surveys of specialists, audiologists and patients (small n, internal). Do not quote percentages or "most said".
13. **Intellectual-property terms.** License terms from the university, attorney names, IP budget, freedom-to-operate plans.
14. **Staffing and people not on the team page.** Names of advisors, consultants, collaborators who gave letters of support, regulatory consultant and quality consultant names.
15. **Anything marked proprietary by brackets in CI-RS or CI-CP.** Those passages (formulation, surfactant, cross-linker choice, partners, financing, royalty) were flagged by the company as not for release.
16. **Retired and discouraged wording.** "ZwiGuard", monomer names in prominent copy, the grafting agent's chemical name (say "grafting agent"), "biological Teflon", and per CLAUDE.md the sentence structures that explain statistics to a reviewer.
17. **Claims that are clinical or not substantiated by the published record.** Reduces stenosis, reduces VAP, prevents capsular contracture, improves hearing or pitch perception, lowers revision rate, "nearly 25 percent greater clinical improvement" for DBS, "extends battery life" (the grants say it "will"; no measurement).

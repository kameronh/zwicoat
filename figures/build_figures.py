"""Website v2 figure set. Every figure: Arial, light surface, brand palette
validated with the dataviz palette checker (blue #0E7FC4 / orange #C9711A /
plum #7B4FA6; uncoated and context in de-emphasis gray). Outputs PNG (2x)
and SVG into figures/png and figures/svg, plus JSON data for the interactive
versions into figures/data. Re-run after any data change:
    python figures/build_figures.py
Sources (read-only): the Dropbox archive (lap-shear and CI masters, aging
package), the project evidence map, data/experiments_by_year_tag.csv.
"""
import csv
import json
import os
import re
import collections

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch
import openpyxl

HERE = os.path.dirname(os.path.abspath(__file__))
V2 = os.path.dirname(HERE)
PNG = os.path.join(HERE, "png"); SVG = os.path.join(HERE, "svg"); DATA = os.path.join(HERE, "data")
for d in (PNG, SVG, DATA):
    os.makedirs(d, exist_ok=True)
DBX = r"C:\Users\Kameron\Zwicoat Dropbox\ZwiCoat Data"
PROJ = r"C:\Users\Kameron\ZwiCoat Data Project"

BLUE, ORANGE, PLUM = "#0E7FC4", "#C9711A", "#7B4FA6"
GRAY, GRAY_LIGHT, INK, INK2, MUTED, SURFACE, GRID = "#8A929B", "#C9CED4", "#1B1F24", "#4A5058", "#7A8089", "#FCFCFB", "#E6E8EA"
BLUE_RAMP = ["#D6EAF7", "#A9D2EE", "#6FB3E0", "#0E7FC4", "#0A5F94", "#073F63"]

plt.rcParams.update({
    # Type scale raised about 15 percent (owner, 2026-11-02): charts keep their on-page size but read larger.
    "font.family": "Arial", "font.size": 12.5, "axes.titlesize": 15, "axes.labelsize": 12.5,
    "xtick.labelsize": 12, "ytick.labelsize": 12,
    "axes.edgecolor": GRID, "axes.linewidth": 1, "axes.spines.top": False, "axes.spines.right": False,
    "axes.grid": True, "grid.color": GRID, "grid.linewidth": 1, "grid.alpha": 1, "axes.axisbelow": True,
    "xtick.color": INK2, "ytick.color": INK2, "text.color": INK, "axes.labelcolor": INK2,
    "figure.facecolor": SURFACE, "axes.facecolor": SURFACE, "savefig.facecolor": SURFACE,
    "legend.frameon": False, "legend.fontsize": 11.5, "figure.dpi": 100, "savefig.dpi": 200,
    "svg.fonttype": "none",
})
MANIFEST = []


def save(fig, name, caption, sources, source_short=None):
    """Write PNG and SVG and record the manifest row. `sources` is the full trace (method notes, approximations);
    `source_short` is the citation line for the site: citations with figure numbers only."""
    fig.savefig(os.path.join(PNG, name + ".png"), bbox_inches="tight", pad_inches=0.3)
    fig.savefig(os.path.join(SVG, name + ".svg"), bbox_inches="tight", pad_inches=0.3)
    plt.close(fig)
    MANIFEST.append({"file": name, "caption": caption, "sources": sources, "source_short": source_short or sources})
    print("saved", name)


def manifest_rows(rows):
    """Markdown table rows for the manifest files (shared with build_sbir.py)."""
    return (["| file | caption | source_short | sources |", "|---|---|---|---|"]
            + [f"| {m['file']} | {m['caption']} | {m['source_short']} | {m['sources']} |" for m in rows])


def title(ax, text, sub=None):
    ax.set_title(text, loc="left", fontsize=16, fontweight="bold", color=INK, pad=(18 + 15 * (sub.count("\n") + 1)) if sub else 14)
    if sub:
        ax.text(0, 1.025, sub, transform=ax.transAxes, fontsize=12, color=MUTED, va="bottom", linespacing=1.3)


def ftitle(fig, text, sub=None, nsub=1):
    """Figure-level title for multi-panel charts: bold left title, muted subtitle (same look as title())."""
    h = fig.get_figheight()
    fig.text(0.01, 1 - 0.12 / h, text, fontsize=16, fontweight="bold", color=INK, va="top", ha="left")
    if sub:
        fig.text(0.01, 1 - 0.54 / h, sub, fontsize=12, color=MUTED, va="top", ha="left", linespacing=1.4)
    fig.subplots_adjust(top=1 - (1.04 + 0.233 * nsub) / h)


def ptitle(ax, text):
    ax.set_title(text, loc="left", fontsize=13, fontweight="bold", color=INK, pad=8)


def bracket(ax, x1, x2, y, text, h, color=INK2, fs=10.5):
    ax.plot([x1, x1, x2, x2], [y - h, y, y, y - h], color=color, lw=1.2, clip_on=False)
    ax.text((x1 + x2) / 2, y + h * 0.3, text, ha="center", va="bottom", fontsize=fs, color=INK)


def num(v):
    try:
        f = float(v)
        return f if f == f else None
    except (TypeError, ValueError):
        return None


def median(v):
    v = sorted(v); n = len(v)
    return v[n // 2] if n % 2 else (v[n // 2 - 1] + v[n // 2]) / 2


# ---------------------------------------------------------------- data loaders
def load_experiments():
    rows = list(csv.DictReader(open(os.path.join(V2, "data", "experiments_by_year_tag.csv"), encoding="utf-8")))
    return [r for r in rows if r["scientist"] != "_databases"]


def load_lapshear():
    wb = openpyxl.load_workbook(os.path.join(DBX, "_databases", "Lap-shear Database", "Lap-shear Master.xlsx"), read_only=True)
    rows = []
    for name in ["2017", "2020", "2024", "2025", "2026", "Undated"]:
        ws = wb[name]; it = ws.iter_rows(values_only=True); hdr = next(it)
        for r in it:
            if not any(v is not None for v in r):
                continue
            d = dict(zip(hdr, r)); d["sheet"] = name
            d["avg"] = num(d.get("Avg (kPa)")); d["n_s"] = num(d.get("n")); d["W"] = num(d.get("W")); d["C"] = num(d.get("C"))
            d["sub"] = substrate_class(str(d.get("Substrate") or "")); d["company"] = not str(d.get("campaign") or "").startswith("DISSERTATION")
            d["untrust"] = str(d.get("Untrustworthy?") or "").strip() not in ("", "None")
            rows.append(d)
    return rows


POLYURETHANE = "Polyurethane"


def substrate_class(s):
    t = s.lower()
    if "pdms-glass" in t or "grafted film" in t: return "Silicone film on glass"
    if "sylgard" in t or "bentec" in t or "pdms" in t: return "Silicone (PDMS)"
    if "cochlear" in t or "med-el" in t or "medel" in t: return "Implant silicone"
    # The database strings say "polyester" for some CIVCO rows, but Kam (CTO) identified the probe-cover
    # material as polyurethane on 2026-10-29, so all of them are one class.
    if "civco" in t or "probe cover" in t or "polyester" in t or "polyurethane" in t: return POLYURETHANE
    if "parylene" in t: return "Parylene-C"
    if "peek" in t: return "PEEK"
    if "pvc" in t: return "PVC"
    return "Not recorded"


def load_ci():
    wb = openpyxl.load_workbook(os.path.join(DBX, "_databases", "CI Dip Coating Database", "CI master database.xlsx"), read_only=True)
    ws = wb["CI master"]; it = ws.iter_rows(values_only=True); hdr = list(next(it))
    return [dict(zip(hdr, r)) for r in it if any(v is not None for v in r)]


def load_aging():
    p = os.path.join(DBX, "_databases", "Accelerated aging Database", "Accelerated_Aging_Updated_Plots_and_MATLAB", "timepoint_summary.csv")
    return list(csv.DictReader(open(p, encoding="utf-8-sig")))


def load_evidence():
    return list(csv.DictReader(open(os.path.join(PROJ, "ZwiCoat - insights", "holistic", "evidence-map", "EVIDENCE-MAP.csv"), encoding="utf-8")))


# ---------------------------------------------------------------- W01 timeline
CATS = [("Adhesion and mechanics", ["lap shear", "tensile/compression", "mass swelling"], BLUE),
        ("Coating process", ["dip-coating", "overmolding"], ORANGE),
        ("Biology (cells, bacteria, animals)", ["antifouling assay", "animal study"], PLUM),
        ("Device function (friction, insertion, impedance)", ["tribometry", "insertion forces", "electrical/impedance"], "#0A5F94"),
        ("Durability (aging, sterilization, leachables)", ["accelerated aging", "sterilization/packaging", "leachables"], GRAY)]


OTHER_CAT = "Other / reference"


def exp_year(r):
    """Year of an experiment row, or None when it is before 2016 or undated (W01 rule)."""
    return int(r["year"]) if r["year"].isdigit() and int(r["year"]) >= 2016 else None


def exp_category(r):
    """First matching CATS category for an experiment row, else OTHER_CAT (shared by W01 and build_people.py)."""
    tags = r["method_tags"].split("|") if r["method_tags"] else []
    for name, tl, _ in CATS:
        if any(t in tags for t in tl):
            return name
    return OTHER_CAT


def w01_timeline(exps):
    years = list(range(2016, 2027))
    counts = {c[0]: collections.Counter() for c in CATS}; other = collections.Counter()
    for r in exps:
        y = exp_year(r)
        if not y: continue
        cat = exp_category(r)
        if cat == OTHER_CAT: other[y] += 1
        else: counts[cat][y] += 1
    fig, ax = plt.subplots(figsize=(12, 5.2))
    bottom = [0] * len(years)
    for name, _, col in CATS:
        vals = [counts[name][y] for y in years]
        ax.bar(years, vals, bottom=bottom, width=0.62, color=col, label=name, edgecolor=SURFACE, linewidth=2)
        bottom = [b + v for b, v in zip(bottom, vals)]
    vals = [other[y] for y in years]
    ax.bar(years, vals, bottom=bottom, width=0.62, color=GRAY_LIGHT, label="Other / reference", edgecolor=SURFACE, linewidth=2)
    tot = [b + v for b, v in zip(bottom, vals)]
    for y, t in zip(years, tot):
        if t: ax.text(y, t + 0.8, str(t), ha="center", fontsize=10, color=INK2)
    ax.axvspan(2015.5, 2023.5, color=BLUE, alpha=0.04, lw=0); ax.axvspan(2023.5, 2026.5, color=ORANGE, alpha=0.04, lw=0)
    ax.text(2016, max(tot) * 1.08, "University of Iowa, Guymon and Hansen labs", fontsize=10, color=MUTED)
    ax.text(2024, max(tot) * 1.08, "ZwiCoat", fontsize=10, color=MUTED, fontweight="bold")
    ax.set_xticks(years); ax.set_ylabel("Experiments archived per year"); ax.set_ylim(0, max(tot) * 1.18)
    ax.legend(loc="upper left", ncol=2, bbox_to_anchor=(0, -0.1))
    title(ax, "Ten years of experiments, year by year", f"{sum(tot)} archived experiments with a written report, grouped by what they measured")
    save(fig, "W01_experiment_timeline", "Every experiment in the ZwiCoat archive by year and by what it measured.", "ZwiCoat Data archive",
         source_short="ZwiCoat Data archive")
    json.dump({"years": years, "series": {n: [counts[n][y] for y in years] for n, _, _ in CATS} | {"Other": vals}}, open(os.path.join(DATA, "W01_timeline.json"), "w"), indent=1)


# ---------------------------------------------------------------- W02 lap-shear universe
def w02_lapshear(ls):
    good = [r for r in ls if r["avg"] is not None and not r["untrust"] and r["sub"] != "Not recorded"]
    order = ["PVC", "Silicone (PDMS)", "Silicone film on glass", "Implant silicone", "PEEK", "Parylene-C", POLYURETHANE]
    by = {s: [r for r in good if r["sub"] == s] for s in order}
    samples = {s: int(sum(r["n_s"] or 0 for r in by[s])) for s in order}
    fig, ax = plt.subplots(figsize=(12, 6))
    import random; random.seed(3)
    for i, s in enumerate(order):
        v = [r["avg"] for r in by[s]]
        xs = [i + random.uniform(-0.28, 0.28) for _ in v]
        ax.scatter(xs, v, s=22, color=BLUE, alpha=0.55, edgecolor=SURFACE, linewidth=0.8)
        ax.hlines(median(v), i - 0.36, i + 0.36, color=INK, lw=2.5)
        ax.text(i, -0.1, f"{len(v)} groups\n{samples[s] or '-'} tests", transform=ax.get_xaxis_transform(), ha="center", va="top", fontsize=9.5, color=MUTED)
    ax.set_xticks(range(len(order))); ax.set_xticklabels([o.replace(" (probe", "\n(probe") for o in order], fontsize=10.5)
    ax.set_ylabel("Lap-shear bond strength, group mean (kPa)"); ax.set_ylim(0, 700)
    ax.text(0.99, 0.97, "Black bar = median of the groups\nEach dot = one experimental group (3 to 10 samples)", transform=ax.transAxes, ha="right", va="top", fontsize=10, color=INK2)
    title(ax, f"{sum(samples.values()):,} adhesion tests across seven substrates", f"{len(good)} experimental groups with a recorded substrate, lap-shear database 2017 to 2026")
    save(fig, "W02_lapshear_database", "Every lap-shear group with a recorded substrate, by substrate. Polyurethane is the ultrasound probe cover material.", f"Lap-shear Master.xlsx (ZwiCoat Data/_databases); totals: {len(good)} groups, {sum(samples.values()):,} tests, {len(order)} substrates, groups dated 2017 to 2026 ({sum(1 for r in good if r['sheet'] == 'Undated')} undated); interactive data in figures/data/W02_lapshear_public.json",
         source_short="ZwiCoat lap-shear database, 2017 to 2026")
    out = [{"substrate": r["sub"], "kPa": round(r["avg"], 1), "n": r["n_s"], "year": r["sheet"], "W": r["W"], "C": r["C"], "scientist": str(r.get("Scientist") or ""), "campaign": str(r.get("campaign") or "")[:60], "fail": str(r.get("Fail mode") or "")[:12]} for r in good]
    json.dump(out, open(os.path.join(DATA, "W02_lapshear_groups.json"), "w"), indent=0)
    # Sanitized list for the public explorer: no formulation (W, C), no scientist, no campaign, no sheet name.
    def fail_class(v):
        t = str(v or "").strip().lower()
        if t.startswith("mixed"): return "mixed"
        if t == "c" or t.startswith("c ") or t.startswith("cohesive"): return "cohesive"
        if t == "a" or t.startswith("adhesive") or t.startswith("predominantly adhesive"): return "adhesive"
        return "not stated"
    pub = [{"substrate": r["sub"], "kPa": round(r["avg"], 1), "n": int(r["n_s"]) if r["n_s"] else None,
            "year": int(r["sheet"]) if r["sheet"].isdigit() else None, "fail": fail_class(r.get("Fail mode"))} for r in good]
    json.dump(pub, open(os.path.join(DATA, "W02_lapshear_public.json"), "w"), indent=1)
    yrs = [p["year"] for p in pub if p["year"]]
    print("W02 public rows:", len(pub), "tests:", sum(p["n"] or 0 for p in pub), "substrates:", len({p["substrate"] for p in pub}), "years:", min(yrs), max(yrs), "undated:", sum(1 for p in pub if not p["year"]))
    print("W02 polyurethane rows:", len(by[POLYURETHANE]), "fail:", dict(collections.Counter(p["fail"] for p in pub)))


# ---------------------------------------------------------------- W03 CI database
def w03_ci(ci):
    mon = collections.Counter(str(r.get("date"))[:7] for r in ci if r.get("date"))
    months = sorted(m for m in mon if m[:2] == "20")
    fig, (ax, ax2) = plt.subplots(1, 2, figsize=(12, 4.8), gridspec_kw={"width_ratios": [1.6, 1]})
    ax.bar(range(len(months)), [mon[m] for m in months], color=BLUE, width=0.7, edgecolor=SURFACE, linewidth=2)
    ax.set_xticks(range(len(months))); ax.set_xticklabels([m[2:4] + "/" + m[5:] for m in months], rotation=0, fontsize=9)
    ax.set_ylabel("Coated cochlear-implant samples logged")
    ax.set_xlabel("Month (YY/MM)")
    cum = 0
    for i, m in enumerate(months): cum += mon[m]
    title(ax, f"{cum} coated implant samples in the process database", "Each sample: formulation, process settings, photographs and a scored coating")
    eras = [("Jig v1\n2025", 54.9, 38), ("Jig v2\n2025-26", 74.0, 181), ("Jig v3\npre-mixing", 69.5, 58), ("Jig v3\nwell-mixed", 78.5, 93)]
    cols = [GRAY_LIGHT, GRAY, GRAY, BLUE]
    ax2.bar(range(4), [e[1] for e in eras], color=cols, width=0.62, edgecolor=SURFACE, linewidth=2)
    for i, e in enumerate(eras):
        ax2.text(i, e[1] + 1.5, f"{e[1]:.0f}", ha="center", fontsize=10.5, color=INK, fontweight="bold" if i == 3 else "normal")
        ax2.text(i, 3, f"n = {e[2]}", ha="center", fontsize=9, color=SURFACE if i == 3 else INK2)
    ax2.set_xticks(range(4)); ax2.set_xticklabels([e[0] for e in eras], fontsize=9.5); ax2.set_ylim(0, 100)
    ax2.set_ylabel("Median coating score (0 to 100)")
    title(ax2, "Process control raised the median score", "Same recipe, three jig generations; mixing the solution was the key step")
    save(fig, "W03_ci_database_and_learning_curve", "The cochlear-implant dip-coating database and the process learning curve.", "CI master database.xlsx; CI Dip Coating Database/insights findings A01, A13",
         source_short="ZwiCoat cochlear implant dip-coating database")


# ---------------------------------------------------------------- W04 fibrosis
SHEEP_BLUE = "#0A5F94"


# Paper metadata for the interactive data files (DOIs as in site/src/data/publications.json).
PAPER_META = {
    "horne2023": ("Horne et al.", 2023, "Acta Biomaterialia", "10.1016/j.actbio.2023.05.011"),
    "peel2024": ("Peel et al.", 2024, "ACS Applied Bio Materials", "10.1021/acsabm.4c00156"),
    "barrera2026": ("Barrera et al.", 2026, "ACS Applied Polymer Materials", "10.1021/acsapm.6c02510"),
    "benshlomo2026": ("Ben-Shlomo et al.", 2026, "Hearing Research", "10.1016/j.heares.2026.109606"),
    "shen2021": ("Shen et al.", 2021, "ACS Applied Bio Materials", "10.1021/acsabm.0c01147"),
    "bennion2021": ("Bennion et al.", 2021, "Otology and Neurotology", "10.1097/MAO.0000000000003288"),
}


def paper_fields(key):
    a, y, j, d = PAPER_META[key]
    return {"paper": a, "year": y, "journal": j, "doi": "https://doi.org/" + d}


def w04_fibrosis():
    # Published values only (figures/published inventories). pct = reduction in capsule thickness or fibrosis vs uncoated.
    #   Horne 2023 Acta Biomater, Fig 5 (text means): flat sheets, 6 wk, 82 -> 27 um = 67 % (exact text means).
    #   Horne 2023 Fig 6G: 1.2 mm cylinders, 6 wk, 10 % cross-linker, about 25.5 -> about 14 um = 45 % (read from figure).
    #   Horne 2023 Fig 7 (text means): one-year human CI arrays, 47 -> 18 um = 62 % (text says "60% less").
    #   Peel 2024 Fig 3: flat PDMS, 6 wk, about 45 -> about 17 um = 62 % (text "over 60% less", p = 0.033).
    #   Barrera 2026 Fig 7F (means read from the plot): rats, 6 wk, flat PDMS, uncoated about 210 um; single 2.5 % about 57,
    #     dual 2.5/2.5 about 38, single 20 % about 36, dual 20/20 about 58 um (the text says about 75 % for the lower cross-linker groups).
    #   Ben-Shlomo 2026 Fig 6G: round window fibrosis, pooled, about 16.5 -> about 2.5 % volume = 85 % (read from figure; p = 0.0101).
    def pct(u, c):
        return int(100 * (1 - c / u) + 0.5)
    UM, FV = "um (capsule thickness)", "% of scala tympani volume (fibrosis)"
    # (chart label, species, duration, substrate, paper key, uncoated, coated, unit, n, exact)
    rows = [("Mouse, flat silicone sheets, 6 weeks\nHorne 2023, n = 3 to 5", "mouse", "6 weeks", "Silicone (PDMS) flat sheet", "horne2023", 82, 27, UM, "3 to 5", True),
            ("Mouse, silicone cylinders, 6 weeks\nHorne 2023, n = 3", "mouse", "6 weeks", "Silicone (PDMS) cylinder, 1.2 mm", "horne2023", 25.5, 14, UM, "3", False),
            ("Mouse, human cochlear implant arrays, 1 year\nHorne 2023, n = 3 to 4", "mouse", "1 year", "Human cochlear implant array", "horne2023", 47, 18, UM, "3 to 4", True),
            ("Mouse, flat silicone, 6 weeks\nPeel 2024, n = 3 to 5", "mouse", "6 weeks", "Silicone (PDMS) flat sheet", "peel2024", 45, 17, UM, "3 to 5", False),
            ("Rat, flat silicone, 6 weeks, single network 2.5%\nBarrera 2026, n = 6", "rat", "6 weeks", "Silicone (PDMS) flat disk, single network 2.5%", "barrera2026", 210, 57, UM, "6", False),
            ("Rat, flat silicone, 6 weeks, dual network 2.5/2.5%\nBarrera 2026, n = 6", "rat", "6 weeks", "Silicone (PDMS) flat disk, dual network 2.5/2.5%", "barrera2026", 210, 38, UM, "6", False),
            ("Rat, flat silicone, 6 weeks, single network 20%\nBarrera 2026, n = 6", "rat", "6 weeks", "Silicone (PDMS) flat disk, single network 20%", "barrera2026", 210, 36, UM, "6", False),
            ("Rat, flat silicone, 6 weeks, dual network 20/20%\nBarrera 2026, n = 6", "rat", "6 weeks", "Silicone (PDMS) flat disk, dual network 20/20%", "barrera2026", 210, 58, UM, "6", False),
            ("Sheep, human cochlear implant arrays, 4 weeks\nBen-Shlomo 2026, 3 sheep, round window", "sheep", "4 weeks", "Human cochlear implant array, round window", "benshlomo2026", 16.5, 2.5, FV, "3 sheep, pooled", False)]
    items = [(r[0], pct(r[5], r[6]), r[1], not r[9], False) for r in rows]
    json.dump([dict(label=r[0].split("\n")[0], species=r[1], duration=r[2], substrate=r[3], **paper_fields(r[4]), pct_reduction=pct(r[5], r[6]),
                    uncoated=r[5], coated=r[6], unit=r[7], n=r[8], exact=r[9]) for r in rows],
              open(os.path.join(DATA, "W04_fibrosis.json"), "w"), indent=1)
    colmap = {"mouse": BLUE, "rat": PLUM, "sheep": SHEEP_BLUE}
    fig, ax = plt.subplots(figsize=(11.5, 7.2))
    y = list(range(len(items)))[::-1]
    for yi, it in zip(y, items):
        hollow = it[4]
        ax.barh(yi, it[1], color="none" if hollow else colmap[it[2]], height=0.6, edgecolor=colmap[it[2]] if hollow else SURFACE, linewidth=2.2 if hollow else 2)
        lab = ("~" if it[3] else "") + f"{it[1]}%" + ("  not significant" if hollow else "")
        ax.text(it[1] + 1.2, yi, lab, va="center", fontsize=11, color=INK, fontweight="bold")
    ax.set_yticks(y); ax.set_yticklabels([i[0] for i in items], fontsize=9.5)
    ax.set_xlim(0, 112); ax.set_xticks(range(0, 101, 20))
    ax.set_xlabel("Reduction in fibrotic capsule or fibrosis vs uncoated (%)")
    ax.grid(axis="y", visible=False)
    for lab, c in (("mouse", BLUE), ("rat", PLUM), ("sheep", SHEEP_BLUE)):
        ax.scatter([], [], color=c, s=60, label=lab)
    ax.legend(loc="upper right")
    title(ax, "Less scar tissue around coated surfaces in mice, rats and sheep",
          f"{len(items)} measurements in 4 papers; mice, rats and sheep, four weeks to one year, on silicone and on human cochlear implant arrays")
    save(fig, "W04_fibrosis_by_study", "Percent reduction in fibrotic capsule or fibrosis around coated surfaces in mice, rats and sheep, measurement by measurement.",
         "Horne R, et al. Acta Biomaterialia 2023;166:212-223 (Figs 5, 6G, 7I; flat-sheet and one-year values from the text, cylinder value approximate, read from the published figure); "
         "Peel A, et al. ACS Applied Bio Materials 2024;7:3124-3135 (Fig 3, text states over 60 percent); "
         "Barrera G, et al. ACS Applied Polymer Materials 2026;8(18):16328-16338, doi:10.1021/acsapm.6c02510 (Fig 7F, four coated groups, rats, 6 weeks, means read from the published plot: uncoated about 210 um, "
         "single network 2.5 percent about 57, dual 2.5/2.5 about 38, single 20 percent about 36, dual 20/20 about 58; p < 0.0001 each versus uncoated; the text states about 75 percent for the lower cross-linker groups and a capsule under one third of uncoated); "
         "Ben-Shlomo N, et al. Hearing Research 2026;474:109606 (Fig 6G round window, p = 0.0101; pooled values approximate, read from the published figure)",
         source_short="Horne et al. 2023, Acta Biomaterialia, Figs 5, 6G and 7I; Peel et al. 2024, ACS Applied Bio Materials, Fig 3; Barrera et al. 2026, ACS Applied Polymer Materials, Fig 7F; Ben-Shlomo et al. 2026, Hearing Research, Fig 6G")


# ---------------------------------------------------------------- W05 antifouling & friction: every published bench comparison
def w05_rows():
    """One dict per published bench comparison (coated vs uncoated). chart=False rows go to the JSON only."""
    rows = []

    def add(cat, assay, surface, paper, year, journal, setting, unit, u, c, n, p, exact, fig, cassay, cstudy, pct=None, chart=True, note=None, chem=None):
        v = pct if pct is not None else 100 * (1 - c / u)
        rows.append(dict(category=cat, assay=assay, surface=surface, paper=paper, year=year, journal=journal, species_or_setting=setting, uncoated=u, coated=c, unit=unit,
                         pct_reduction=int(v + 0.5), n=n, p_text=p, exact=exact, figure=fig, in_static_chart=chart, note=note, chemistry=chem, _assay=cassay, _study=cstudy))
    L17, L19, JN, SH, H23, BN, PL, BA = ("Leigh et al.", 2017, "Biomacromolecules"), ("Leigh et al.", 2019, "Langmuir"), ("Jensen et al.", 2021, "ACS Biomaterials Science and Engineering"), \
        ("Shen et al.", 2021, "ACS Applied Bio Materials"), ("Horne et al.", 2023, "Acta Biomaterialia"), ("Bennion et al.", 2021, "Otology and Neurotology"), \
        ("Peel et al.", 2024, "ACS Applied Bio Materials"), ("Barrera et al.", 2026, "ACS Applied Polymer Materials")
    g = "in vitro, glass"
    s = "in vitro, silicone (PDMS)"
    # ---- Protein  (rule, Kam 2026-10-30: the site says "uncoated" vs "coated"; where a paper tested SBMA and CBMA only the SBMA result is kept.
    #      The original chemistry is stored in the `chemistry` field of the JSON for traceability, never in the image.)
    uf = "relative fluorescence (uncoated = 1)"
    add("Protein", "Fibrinogen adsorption", "Glass, coated, 2.5 wt% monomer", *L17, g, uf, 1.0, 0.09, "3 samples, 5 images each", "not stated (text: below 10% of control)", False, "Fig 4A", "Fibrinogen on glass", "Leigh 2017, n = 3", chem="SBMA")
    add("Protein", "Fibrinogen adsorption", "Silicone (PDMS), coated", *L19, s, uf, 1.0, 0.02, "3 samples, 5 images each", "< 0.001 (text: greater than 90% reduction)", False, "Fig 7D", "Fibrinogen on silicone", "Leigh 2019, n = 3", chem="SBMA")
    add("Protein", "Fibrinogen adsorption", "Reinforced silicone, coated, 5% cross-linker", *JN, s, uf, 1.0, 0.09, "3 samples, 9 images each", "not stated (ANOVA with Tukey in Methods)", False, "Fig 1G", "Fibrinogen on reinforced silicone", "Jensen 2021, 5% cross-linker, n = 3", chem="SBMA")
    # ---- Cells
    cu = "cells per um2 x 10^-4"
    add("Cells", "Fibroblast adhesion, 48 h", "Glass, coated", *L17, g, cu, 9.0, 4.2, "at least 3 samples, at least 10 fields", "< 0.001", False, "Fig 6E", "Fibroblasts on glass", "Leigh 2017, n ≥ 3", note="text: less than half of glass", chem="SBMA")
    add("Cells", "Astrocyte adhesion, 48 h", "Glass, coated", *L17, g, cu, 6.1, 0.45, "at least 3 samples, at least 10 fields", "< 0.001", True, "Fig 7E", "Astrocytes on glass", "Leigh 2017, n ≥ 3", pct=100 * (1 - 1 / 13), note="text: 13-fold reduction", chem="SBMA")
    add("Cells", "Schwann cell adhesion, 48 h", "Glass, coated", *L17, g, cu, 14.0, 0.3, "at least 3 samples, at least 10 fields", "< 0.001", False, "Fig 8E", "Schwann cells on glass", "Leigh 2017, n ≥ 3", pct=100 * (1 - 1 / 40), note="text: more than 40-fold decrease (lower bound)", chem="SBMA")
    add("Cells", "Fibroblast adhesion after 14 days soaking in culture medium", "Silicone (PDMS), coated", *L19, s, cu, 30, 2.8, "at least 3 substrates, at least 10 images", "< 0.001", False, "Fig 10D", "Fibroblasts on silicone, 14 d soak", "Leigh 2019, n ≥ 3", note="ratio of plotted bars; plotted absolute values conflict with the text (inventory caveat)", chem="SBMA")
    add("Cells", "Fibroblast adhesion, 48 h, no serum pre-soak", "Silicone (PDMS), coated", *L19, s, cu, 7.8, 0.4, "at least 3 substrates, at least 10 images", "< 0.001", False, "Fig 8D", "Fibroblasts on silicone", "Leigh 2019, n ≥ 3", chart=False, note="text: less than 5% of control", chem="SBMA")
    add("Cells", "Fibroblast adhesion, 48 h", "Reinforced silicone, coated, 5% cross-linker", *JN, s, cu, 11.6, 1.75, "3 samples, 10 images each", "not stated (ANOVA with Tukey in Methods)", False, "Fig 3G", "Fibroblasts on silicone", "Jensen 2021, 5% cross-linker, n = 3", chem="SBMA")
    add("Cells", "Macrophage adhesion, 7 days", "Reinforced silicone, coated, 5% cross-linker", *JN, s, cu, 7.6, 0.45, "3 samples, 10 images each", "not stated (ANOVA with Tukey in Methods)", False, "Fig 2G", "Macrophages on silicone", "Jensen 2021, 5% cross-linker, n = 3", chem="SBMA")
    # Horne 2023 Fig 3F, newly made coatings at 1.6/5/13/31 % cross-linker ~0.18/0.12/0.03/0.14; after 6 months in mice ~0.20/0.14/0.11/0.16 (uncoated = 1)
    add("Cells", "Fibroblast adhesion, 48 h, newly made coating (mean of 4 cross-linker levels)", "Silicone (PDMS), coated", *H23, s, "relative to uncoated (uncoated = 1)", 1.0, round((0.18 + 0.12 + 0.03 + 0.14) / 4, 4), "3 per condition", "0.02 or less (Tukey, all coated groups)", False, "Fig 3F", "Fibroblasts on silicone, new", "Horne 2023, 1.6 to 31% cross-linker, n = 3", note="text: an order of magnitude less", chem="CBMA")
    add("Cells", "Fibroblast adhesion, 48 h, coating explanted after 6 months in mice (mean of 4 levels)", "Silicone (PDMS), coated", *H23, "in vitro assay on coatings explanted after 6 months in mice", "relative to uncoated (uncoated = 1)", 1.0, round((0.20 + 0.14 + 0.11 + 0.16) / 4, 4), "3 per condition", "0.02 or less; new vs 6-month p = 0.73", False, "Fig 3F", "Fibroblasts, coating kept 6 months in mice", "Horne 2023, 1.6 to 31% cross-linker, n = 3", chem="CBMA")
    add("Cells", "Fibroblast adhesion, 48 h (3T3), low cross-linker", "Silicone (PDMS), coated, 2.5% primary cross-linker", *BA, s, "relative to uncoated (uncoated = 1; PDMS 32 cells/mm2)", 1.0, 0.01, "at least 4", "not stated ('significantly')", False, "Fig 6", "Fibroblasts on silicone", "Barrera 2026, 2.5% cross-linker, n ≥ 4", note="text: more than 99% reduction (low cross-link groups)", chem="SBMA (dual network)")
    add("Cells", "Fibroblast adhesion, 48 h (3T3), high cross-linker", "Silicone (PDMS), coated, 20% primary and 5% secondary cross-linker", *BA, s, "relative to uncoated (uncoated = 1; PDMS 32 cells/mm2)", 1.0, 0.10, "at least 4", "not stated ('significantly')", False, "Figs 5D, 6", "Fibroblasts on silicone", "Barrera 2026, 20%/5% cross-linker, n ≥ 4", note="text: about 90% reduction for the high cross-link coating", chem="SBMA (dual network)")
    # ---- Bacteria (Shen 2021, counts per high-power field; the coating there is the carboxybetaine polymer, pCBMA)
    hp = "counts per high-power field"
    add("Bacteria", "S. aureus adhesion, 1 h in suspension", "Silicone (PDMS), coated", *SH, s, hp, 1560, 40, "10 fields per condition", "< 0.0001 (ANOVA with Tukey)", False, "Fig 3", "S. aureus, 1 h in suspension", "Shen 2021, n = 10 fields", chem="pCBMA")
    add("Bacteria", "S. epidermidis adhesion, 1 h in suspension", "Silicone (PDMS), coated", *SH, s, hp, 890, 60, "10 fields per condition", "< 0.0001 (ANOVA with Tukey)", False, "Fig 3", "S. epidermidis, 1 h in suspension", "Shen 2021, n = 10 fields", chem="pCBMA")
    add("Bacteria", "S. aureus adhesion, 1 h droplet (spray) exposure", "Silicone (PDMS), coated", *SH, s, hp, 510, 80, "10 fields per condition", "< 0.0001 (ANOVA with Tukey)", False, "Fig 3", "S. aureus, 1 h droplet", "Shen 2021, n = 10 fields", chem="pCBMA")
    add("Bacteria", "S. epidermidis adhesion, 1 h droplet (spray) exposure", "Silicone (PDMS), coated", *SH, s, hp, 240, 30, "10 fields per condition", "< 0.0001 (ANOVA with Tukey)", False, "Fig 3", "S. epidermidis, 1 h droplet", "Shen 2021, n = 10 fields", chem="pCBMA")
    add("Bacteria", "Adherent S. aureus on explant, day 21", "Silicone (PDMS) implant under the skin, coated, S. aureus inoculated", *SH, "in vivo, rats, 21 days", hp, 940, 155, "about 71 fields (t test df = 69)", "< 0.0001", False, "Fig 7C", "S. aureus on explant, rats, day 21", "Shen 2021, n ≈ 71 fields", note="text: more than 500 counts per field fewer", chem="pCBMA")
    add("Bacteria", "Viable colonies recovered from explant, day 21", "Silicone (PDMS) implant under the skin, coated, S. aureus inoculated", *SH, "in vivo, rats, 21 days", "colonies (as plotted)", 690, 35, "6 implants", "0.0006", False, "Fig 7D", "Live colonies on explant, rats, day 21", "Shen 2021, n = 6 implants", chem="pCBMA")
    add("Bacteria", "Adherent S. aureus in a 24 h challenge after 2 weeks in rats", "Silicone (PDMS) implant, coated", *SH, "in vivo for 2 weeks, then challenged in a dish", hp, 2520, 210, "6 rats per group (30 fields)", "< 0.0001", False, "Fig 8", "S. aureus after 2 weeks in rats", "Shen 2021, n = 6 rats", note="text: more than 1000 counts per field fewer", chem="pCBMA")
    # ---- Friction
    fu = "relative coefficient of friction (uncoated = 1)"
    add("Friction", "Friction vs sapphire ball in PBS", "Reinforced silicone, coated, 4% cross-linker", *JN, s, fu, 1.0, 0.062, "4", "not stated ('significantly decreased')", False, "Fig 5A", "Friction vs sapphire", "Jensen 2021, 4% cross-linker, n = 4", chem="SBMA")
    add("Friction", "Friction vs steel ball in PBS", "Silicone (PDMS), coated", *BN, "bench, PBS, 1 N", fu, 1.0, 0.06, "not stated", "< 0.0001 (text: greater than 90% reduction)", False, "Fig 1B", "Friction vs steel", "Bennion 2021", chem="SBMA")
    add("Friction", "Friction vs ceramic ball in PBS", "Silicone (PDMS), coated", *BN, "bench, PBS, 1 N", fu, 1.0, 0.06, "not stated", "< 0.0001 (text: greater than 90% reduction)", False, "Fig 1B", "Friction vs ceramic", "Bennion 2021", chem="SBMA")
    add("Friction", "Friction vs guinea pig dermis in PBS", "Silicone (PDMS), coated", *BN, "bench, ex vivo guinea pig dermis, PBS, 1 N", fu, 1.0, 0.06, "4 guinea pigs", "< 0.0001 (text: greater than 90% reduction)", False, "Fig 1B", "Friction vs guinea pig dermis", "Bennion 2021, n = 4", chem="SBMA")
    add("Friction", "Friction vs sapphire probe in PBS, pristine coating", "Silicone (PDMS), coated", *PL, s, "coefficient of friction (absolute)", 0.25, 0.027, "4 or more", "not stated", False, "Fig 4", "Friction vs sapphire, pristine", "Peel 2024, n ≥ 4", chem="SBMA")
    add("Friction", "Friction vs sapphire probe in PBS, after 3 weeks in mice", "Silicone (PDMS) disk, coated", *PL, "in vivo for 3 weeks (mice), then bench", "coefficient of friction (absolute)", 0.27, 0.03, "4 or more", "not stated (no change from pristine)", False, "Fig 4", "Friction, after 3 weeks in mice", "Peel 2024, n ≥ 4", chem="SBMA")
    tis = [("aorta", 0.03), ("bladder", 0.03), ("dermis", 0.06), ("fat", 0.02), ("trachea", 0.05), ("steel", 0.05)]
    for nm, v in tis:
        add("Friction", f"Friction vs guinea pig {nm}" if nm != "steel" else "Friction vs steel probe", "Silicone (PDMS), coated, 5% cross-linker", *PL, "bench, ex vivo guinea pig tissue-covered probe, PBS" if nm != "steel" else "bench, PBS", fu, 1.0, v, "3 or more", "not stated (text: at least 90% reduction for all tissues)", False, "Fig 5A", "", "", chart=False, chem="SBMA")
    mean_pct = sum(100 * (1 - v) for _, v in tis) / len(tis)
    lo, hi = min(100 * (1 - v) for _, v in tis), max(100 * (1 - v) for _, v in tis)
    rows.append(dict(category="Friction", assay="Friction vs five guinea pig tissues and steel (mean of six probes)", surface="Silicone (PDMS), coated, 5% cross-linker", paper="Peel et al.", year=2024, journal="ACS Applied Bio Materials",
                     species_or_setting="bench, ex vivo guinea pig tissue-covered probes, PBS", uncoated=1.0, coated=round(1 - mean_pct / 100, 3), unit=fu, pct_reduction=int(mean_pct + 0.5), n="3 or more", p_text="not stated (text: at least 90% reduction for all tissues)",
                     exact=False, figure="Fig 5A", in_static_chart=True, note=f"mean of six probe reductions (range about {int(lo + 0.5)} to {int(hi + 0.5)}); the six single-probe rows are listed separately", chemistry="SBMA",
                     _assay="Friction vs five tissues and steel", _study=f"Peel 2024, range ~{int(lo + 0.5)} to {int(hi + 0.5)}, n ≥ 3"))
    add("Friction", "Friction vs sapphire ball, 1 N, best group", "Silicone (PDMS), coated, 2.5% primary and 2.5% secondary cross-linker", *BA, s, fu, 1.0, 0.16, "3 measurements per point", "not stated", False, "Fig 4B", "Friction vs sapphire", "Barrera 2026, 2.5%/2.5% cross-linker, n = 3", note="text: over 80% reduction for some coatings; other coatings reduce by about 58 to 74%", chem="SBMA (dual network)")
    # order: protein, cells, bacteria, friction (insertion order within each already by paper)
    order = {"Protein": 0, "Cells": 1, "Bacteria": 2, "Friction": 3}
    rows.sort(key=lambda r: order[r["category"]])
    return rows


def w05_antifouling():
    rows = w05_rows()
    chart = [r for r in rows if r["in_static_chart"]]
    papers = {(r["paper"], r["year"]) for r in chart}
    bands = [("Protein", "Protein: fibrinogen adsorption"), ("Cells", "Cells: attachment in culture"), ("Bacteria", "Bacteria: Staphylococcus adhesion"), ("Friction", "Friction: coated versus uncoated silicone")]
    H = 13.4
    fig = plt.figure(figsize=(11, H))
    axl, axw = 5.5 / 11, 5.1 / 11
    ax = fig.add_axes([axl, 0.07, axw, 0.865])
    tr = ax.get_yaxis_transform()
    ax_w_in = 5.1
    x_study = -(5.5 - 0.3) / ax_w_in
    x_assay = -0.02
    # row layout
    pos = []; y = 0
    for cat, _ in bands:
        pos.append(("head", cat, y)); y += 1
        for r in [r for r in chart if r["category"] == cat]:
            pos.append(("row", r, y)); y += 1
        y += 0.35
    ymax = y
    n_rows = sum(1 for p in pos if p[0] == "row")
    for kind, obj, yy in pos:
        if kind == "head":
            cnt = sum(1 for r in chart if r["category"] == obj)
            from matplotlib.patches import Rectangle
            ax.add_patch(Rectangle((x_study - 0.03, yy - 0.5), 1.03 - x_study + 0.12, 1.0, transform=tr, facecolor="#E9F2F9", edgecolor="none", clip_on=False, zorder=0))
            ax.text(x_study, yy, dict(bands)[obj] + f"  ({cnt})", transform=tr, ha="left", va="center", fontsize=10.5, fontweight="bold", color=INK)
        else:
            r = obj
            ax.barh(yy, 100, height=0.62, color="#EEF0F2", edgecolor="none", zorder=1)
            ax.barh(yy, r["pct_reduction"], height=0.62, color=BLUE, edgecolor="none", zorder=2)
            lab = ("" if r["exact"] else "~") + f"{r['pct_reduction']}%"
            ax.text(r["pct_reduction"] + 1.3, yy, lab, va="center", ha="left", fontsize=9.5, fontweight="bold", color=INK, zorder=3)
            ax.text(x_assay, yy, r["_assay"], transform=tr, ha="right", va="center", fontsize=9.5, color=INK)
            ax.text(x_study, yy, r["_study"], transform=tr, ha="left", va="center", fontsize=8.5, color=MUTED)
    ax.set_ylim(ymax - 0.6, -0.8); ax.set_xlim(0, 112)
    ax.set_yticks([]); ax.set_xticks(range(0, 101, 20)); ax.set_xticklabels([f"{t}%" for t in range(0, 101, 20)])
    ax.grid(axis="y", visible=False); ax.spines["left"].set_visible(False)
    ax.set_xlabel("Reduction versus the uncoated surface. Blue bar = coated surface; gray track = uncoated (100%).", fontsize=9.5)
    ftitle(fig, "Protein, cells, bacteria and friction: published comparisons, coated versus uncoated",
           f"{n_rows} comparisons from {len(papers)} papers, 2017 to 2026; in vitro on glass or silicone unless the label says rats or mice")
    fig.text(0.01, 0.008, "~ = value read from a published plot", fontsize=8.5, color=MUTED)
    srcs = ("Leigh BL, et al. Biomacromolecules 2017;18(8):2389-2401 (Fig 4 fibrinogen; Figs 6E, 7E, 8E cells on glass; fibrinogen and fibroblast values read from the published plots, astrocyte and Schwann cell values from the stated fold changes); "
            "Leigh BL, et al. Langmuir 2019;35(4):1100-1110 (Fig 7D fibrinogen; Fig 10D fibroblasts after 14 days in medium, plotted ratios used because the plotted absolute values conflict with the text); "
            "Jensen MJ, et al. ACS Biomaterials Science and Engineering 2021;7(9):4494-4502 (Figs 1G, 2G, 3G at 5 percent cross-linker; Fig 5A friction at 4 percent; values read from the published plots); "
            "Shen N, et al. ACS Applied Bio Materials 2021;4(2):1283-1293 (Fig 3 in vitro, Figs 7C, 7D rat explants at day 21, Fig 8 after 2 weeks in rats; values read from the published plots); "
            "Horne R, et al. Acta Biomaterialia 2023;166:212-223 (Fig 3F, mean of four cross-linker levels, new and after 6 months in mice; read from the published plot); "
            "Bennion DM, et al. Otology and Neurotology 2021;42(10):1476-1483 (Fig 1B, steel, ceramic and guinea pig dermis; text states more than 90 percent lower, p < 0.0001); "
            "Peel A, et al. ACS Applied Bio Materials 2024;7:3124-3135 (Fig 4 pristine and after 3 weeks in mice; Fig 5A six probes, bar shows the mean, range in the label; read from the published plots); "
            "Barrera G, et al. ACS Applied Polymer Materials 2026;8(18):16328-16338, doi:10.1021/acsapm.6c02510 (Fig 6 fibroblasts, text states more than 99 percent for low and about 90 percent for high cross-linker; Fig 4B friction, best group 2.5/2.5 percent). "
            "Chemistry, for traceability only (not shown in the image): where a paper tested both an SBMA and a CBMA coating, the SBMA result is plotted; Shen 2021 and Horne 2023 are CBMA coatings; Barrera 2026 is an SBMA dual-network coating. "
            "Per-comparison values, n and p, and the chemistry of each row, are in figures/data/W05_antifouling_all.json")
    save(fig, "W05_antifouling_and_friction", f"Published bench comparisons of coated versus uncoated surfaces ({n_rows} bars from {len(papers)} papers): protein adsorption, cell attachment, bacterial adhesion and friction, as percent reduction.", srcs,
         source_short="Leigh et al. 2017, Biomacromolecules, Figs 4, 6E, 7E and 8E; Leigh et al. 2019, Langmuir, Figs 7D and 10D; Jensen et al. 2021, ACS Biomaterials Science and Engineering, Figs 1G, 2G, 3G and 5A; Shen et al. 2021, ACS Applied Bio Materials, Figs 3, 7C, 7D and 8; Horne et al. 2023, Acta Biomaterialia, Fig 3F; Bennion et al. 2021, Otology and Neurotology, Fig 1B; Peel et al. 2024, ACS Applied Bio Materials, Figs 4 and 5A; Barrera et al. 2026, ACS Applied Polymer Materials, Figs 4B and 6")
    out = [{k: v for k, v in r.items() if not k.startswith("_")} for r in rows]
    json.dump(out, open(os.path.join(DATA, "W05_antifouling_all.json"), "w"), indent=1, ensure_ascii=False)
    print("W05 bars:", n_rows, "papers:", len(papers), "json rows:", len(out))
    for r in chart:
        print(("   %s | %s | %s | %s%d" % (r["category"], r["_assay"], r["_study"], "" if r["exact"] else "~", r["pct_reduction"])).encode("ascii", "replace").decode())
    import statistics
    print("W05 median pct:", statistics.median(r["pct_reduction"] for r in chart))
    return rows


# ---------------------------------------------------------------- W06 durability timeline
# Every checkpoint, one record per paper (the static chart merges the two six-month papers into one label).
#   Shen 2021 Fig 8 (2 weeks, rats); Peel 2024 Fig 4 (3 weeks, mice, friction) and Fig 2 (6 months, SEM, films intact);
#   Ben-Shlomo 2026 text p. 4 (4 weeks, sheep, no delamination); Barrera 2026 Fig 7 and text p. 16335 (6 weeks, rats, "75% reduction");
#   Horne 2023 Figs 2 and 3F (6 months, mice) and Fig 7 (1 year, mice, capsule 60 percent thinner).
W06_CHECKPOINTS = [
    (14, "2 weeks", "rats", "A coating kept under the skin of rats for two weeks still repelled S. aureus in a fresh challenge.", "shen2021"),
    (21, "3 weeks", "mice", "Coated silicone kept its low friction after three weeks in mice.", "peel2024"),
    (28, "4 weeks", "sheep", "Coated human cochlear implant arrays showed no delamination after four weeks in a sheep cochlea, and every array kept working.", "benshlomo2026"),
    (42, "6 weeks", "rats", "The scar capsule around coated silicone was about 75 percent thinner than around uncoated silicone after six weeks in rats.", "barrera2026"),
    (182, "6 months", "mice", "Coated silicone still turned away fibroblasts after six months in mice, and the film was still in place.", "horne2023"),
    (182, "6 months", "mice", "Coated silicone films were intact, with little to no delamination, after six months in mice.", "peel2024"),
    (365, "1 year", "mice", "On human cochlear implant arrays kept for one year in mice, the film was intact and the scar capsule was about 60 percent thinner.", "horne2023"),
]


def w06_durability():
    json.dump([dict(days=d, label=lab, species=sp, what_was_shown=w, **paper_fields(k)) for d, lab, sp, w, k in sorted(W06_CHECKPOINTS, key=lambda r: r[0])],
              open(os.path.join(DATA, "W06_durability.json"), "w"), indent=1)
    # (days, label x, label y, text); x in years
    events = [(14, 0.0, 0.55, "2 weeks in rats\nstill repels S. aureus\nShen 2021"),
              (21, 0.075, -0.5, "3 weeks in mice\nfriction unchanged\nPeel 2024"),
              (28, 0.255, 0.55, "4 weeks in a sheep cochlea\nno delamination, all arrays working\nBen-Shlomo 2026"),
              (42, 0.30, -0.5, "6 weeks in rats\ncapsule about 75% thinner\nBarrera 2026"),
              (182, 0.55, 0.55, "6 months in mice\nantifouling unchanged, films intact\nHorne 2023, Peel 2024"),
              (365, 0.93, -0.5, "1 year in mice on human implant arrays\nfilm intact, capsule 60% thinner\nHorne 2023")]
    fig, ax = plt.subplots(figsize=(12.5, 4.2))
    ax.hlines(0, 0, 1.08, color=GRAY_LIGHT, lw=3)
    for d, xt, yt, txt in events:
        t = d / 365
        ax.scatter([t], [0], s=140, color=BLUE, zorder=3, edgecolor=SURFACE, linewidth=2)
        ax.annotate(txt, (t, 0), xytext=(xt, yt), ha="center", va="bottom" if yt > 0 else "top", fontsize=9.5, color=INK, linespacing=1.35,
                    arrowprops=dict(arrowstyle="-", color=GRAY, lw=1, shrinkA=2, shrinkB=6))
    ax.set_xlim(-0.1, 1.1); ax.set_ylim(-1.15, 1.15); ax.set_yticks([]); ax.grid(False)
    ax.set_xticks([0, 0.25, 0.5, 0.75, 1.0]); ax.set_xticklabels(["Day 0", "3 months", "6 months", "9 months", "1 year"])
    for s in ("left", "top", "right"): ax.spines[s].set_visible(False)
    title(ax, "The coating stays on: checkpoints from two weeks to one year in vivo", "Covalently grafted, so the film is part of the surface rather than a layer on it")
    save(fig, "W06_durability_timeline", "In-vivo durability checkpoints from two weeks to one year, in rats, mice and sheep.",
         "Shen N, et al. ACS Applied Bio Materials 2021;4(2):1283-1293 (Fig 8, 2 weeks in rats); Peel A, et al. ACS Applied Bio Materials 2024;7:3124-3135 (Fig 4, 3 weeks; Fig 2, 6 months); "
         "Ben-Shlomo N, et al. Hearing Research 2026;474:109606 (text p. 4, no delamination after 4 weeks); Barrera G, et al. ACS Applied Polymer Materials 2026;8(18):16328-16338 "
         "(Fig 7 and text p. 16335, about 75 percent thinner capsule at 6 weeks in rats); Horne R, et al. Acta Biomaterialia 2023;166:212-223 (Figs 2 and 3F, 6 months; Fig 7, 1 year). "
         "Checkpoint data with DOIs: figures/data/W06_durability.json",
         source_short="Shen et al. 2021, ACS Applied Bio Materials, Fig 8; Peel et al. 2024, ACS Applied Bio Materials, Figs 2 and 4; Ben-Shlomo et al. 2026, Hearing Research; "
                      "Barrera et al. 2026, ACS Applied Polymer Materials, Fig 7; Horne et al. 2023, Acta Biomaterialia, Figs 2, 3F and 7")


# ---------------------------------------------------------------- W07 insertion force, W08 impedance
def w37_summary():
    """Peak-force summary of the synthetic-cochlea insertions, written by build_sbir.py (computed there from the raw Zenodo files)."""
    return json.load(open(os.path.join(DATA, "W37_traces.json"), encoding="utf-8"))["summary"]


def w07_insertion():
    # A. Bennion DM, et al. Otol Neurotol 2021;42(10):1476-1483, Fig 4A and text (exact): human cadaveric cochleae, n = 9 per group, mean +/- SD,
    #    maximum force uncoated 64.2 +/- 17.9 mN, coated 37.0 +/- 11.3 mN, p = 0.001.
    # B. Peel A, et al. ACS Appl Bio Mater 2024;7:3124-3135, Fig 13A (approximate, read from the figure; the paper prints no group means): uncoated about 68 mN,
    #    coated about 35 mN, n = 9 per group, p < 0.003. The inventory flags that this may be the same experiment as Bennion 2021 re-analysed.
    # C. NIH SBIR Phase I dataset (Zenodo), synthetic cochlea, robotic insertion: peak force per trial, computed by build_sbir.py from the raw files.
    s = w37_summary()
    pu, pc = (s["peak_uncoated_mean"], s["peak_uncoated_sd"]), (s["peak_coated_mean"], s["peak_coated_sd"])
    panels = [("A. Human cadaveric cochleae", "Bennion et al. 2021", (64.2, 17.9), (37.0, 11.3), (9, 9), False),
              ("B. Human cadaveric cochleae", "Peel et al. 2024", (68, None), (35, None), (9, 9), True),
              ("C. Synthetic cochlea", "NIH SBIR Phase I dataset", pu, pc, (s["n_uncoated"], s["n_coated"]), False)]
    ymax = 120
    fig, axes = plt.subplots(1, 3, figsize=(13.5, 5.6), sharey=True)
    for ax, (pt, who, u, c, (nu, nc), approx) in zip(axes, panels):
        for i, ((m, sd), col) in enumerate(((u, GRAY), (c, BLUE))):
            ax.bar(i, m, width=0.55, color=col, edgecolor=SURFACE, linewidth=2)
            if sd is not None:
                ax.errorbar(i, m, yerr=sd, color=INK, capsize=6, lw=1.6, capthick=1.6)
                if m - sd < ymax * 0.2:  # short bar: the label would collide with the whisker, so it sits above the bar
                    ax.text(i, m + sd + ymax * 0.02, f"{m:.1f}\n± {sd:.1f}", ha="center", va="bottom", fontsize=11, color=INK, fontweight="bold")
                else:
                    ax.text(i, ymax * 0.03, f"{m:.1f}\n± {sd:.1f}", ha="center", va="bottom", fontsize=11, color="white", fontweight="bold")
            else:
                ax.text(i, ymax * 0.03, f"~{m:g}", ha="center", va="bottom", fontsize=11, color="white", fontweight="bold")
        red = 100 * (1 - c[0] / u[0])
        top = u[0] + (u[1] or 0)
        lab = f"about −{round(red / 5) * 5:.0f}%" if approx else f"−{red:.0f}%"
        bracket(ax, 0, 1, top + ymax * 0.07, lab, ymax * 0.03, fs=12)
        ax.set_xticks([0, 1]); ax.set_xticklabels([f"Uncoated\n(n = {nu})", f"Coated\n(n = {nc})"], fontsize=10.5)
        ax.set_xlim(-0.6, 1.6); ax.set_ylim(0, ymax); ax.grid(axis="x", visible=False)
        ax.tick_params(axis="y", labelleft=True)
        ax.set_title(pt, loc="left", fontsize=11.5, fontweight="bold", color=INK, pad=24)
        ax.text(0, 1.015, who, transform=ax.transAxes, fontsize=10, color=MUTED, va="bottom")
    axes[0].set_ylabel("Peak insertion force (mN)")
    fig.subplots_adjust(wspace=0.22)
    ftitle(fig, "Coated cochlear implants insert with about half the force, in three studies",
           "Peak insertion force of cochlear implant electrode arrays in human cadaveric cochleae (Bennion 2021, Peel 2024) and in a synthetic cochlea\n"
           "(NIH SBIR Phase I dataset); mean ± SD where published", nsub=2)
    save(fig, "W07_insertion_force",
         f"Coated cochlear implant electrode arrays needed about half the peak insertion force of uncoated arrays in three studies: 42 percent less in human cadaveric cochleae "
         f"(Bennion 2021), about 50 percent less in human cadaveric cochleae (Peel 2024) and {100 * (1 - pc[0] / pu[0]):.0f} percent less in a synthetic cochlea (NIH SBIR Phase I dataset).",
         "Bennion DM, Horne R, Peel A, Reineke P, Henslee A, Kaufmann C, Guymon CA, Hansen MR. Zwitterionic photografted coatings of cochlear implant biomaterials reduce friction and insertion forces. "
         "Otology and Neurotology 2021;42(10):1476-1483. doi:10.1097/MAO.0000000000003288 (Fig 4A; means, SD and p = 0.001 from the text, exact; n = 9 per group; coating is SBMA); "
         "Peel A, Bennion D, Horne R, Hansen MR, Guymon CA. Photografted zwitterionic hydrogel coating durability for reduced foreign body response to cochlear implants. ACS Applied Bio Materials "
         "2024;7:3124-3135. doi:10.1021/acsabm.4c00156, Fig 13A (means about 68 and about 35 mN read from the published figure, approximate; n = 9 per group, p < 0.003 from the caption; SBMA coating; "
         "the paper prints no group means or SD for this figure); "
         f"ZwiCoat Materials Innovations, NIH SBIR Phase I dataset, Zenodo, doi:10.5281/zenodo.10459478, folder 'CI force of insertion' (peak force per trial computed by build_sbir.py: "
         f"uncoated {pu[0]:.1f} ± {pu[1]:.1f} mN, n = {s['n_uncoated']}; coated {pc[0]:.1f} ± {pc[1]:.1f} mN, n = {s['n_coated']}; Welch p = {s['p_peak_welch']:.1e}; see W37). "
         "Build note: the Peel Fig 13 caption, n, array types and means resemble Bennion Fig 4, so panels A and B may be the same cadaver experiment re-analysed.",
         source_short="Bennion et al. 2021, Otology and Neurotology, Fig 4A; Peel et al. 2024, ACS Applied Bio Materials, Fig 13A; NIH SBIR Phase I dataset, Zenodo, doi:10.5281/zenodo.10459478")


def w08_impedance():
    imp = [("At implantation", 30, 10), ("4 weeks later", 17, 9)]
    fig, ax = plt.subplots(figsize=(7, 5))
    ax.bar([i - 0.19 for i in range(2)], [u for _, u, c in imp], width=0.36, color=GRAY_LIGHT, label="Uncoated ear", edgecolor=SURFACE, linewidth=2)
    ax.bar([i + 0.19 for i in range(2)], [c for _, u, c in imp], width=0.36, color=BLUE, label="Coated ear", edgecolor=SURFACE, linewidth=2)
    for i, (_, u, c) in enumerate(imp): ax.text(i + 0.19, c + 0.7, f"\u2212{100 * (1 - c / u):.0f}%", ha="center", fontsize=12, color=INK, fontweight="bold")
    ax.set_xticks(range(2)); ax.set_xticklabels([t for t, *_ in imp]); ax.set_ylabel("Total electrode impedance (kOhm)"); ax.legend(loc="upper right")
    title(ax, "Lower electrode impedance on working human implants in sheep", "Three sheep, one coated and one uncoated array each; Ben-Shlomo 2026")
    save(fig, "W08_impedance_sheep", "Electrode impedance of coated vs uncoated cochlear implant arrays in sheep.", "Ben-Shlomo et al. 2026, Hearing Research 474:109606, Fig 3B (values read from the figure)",
         source_short="Ben-Shlomo et al. 2026, Hearing Research, Fig 3B")


# ---------------------------------------------------------------- W09 aging mass loss
def w09_aging(ag):
    # Owner rule (2026-10-30): no chemistry names in the image. "Standard" is the SBMA recipe; the CBMA series (composition "CBMA" in the data) is not plotted.
    series = {"Standard recipe": (BLUE, 2.6), "Low crosslinker": (GRAY, 1.8), "Low monomer": (GRAY_LIGHT, 1.8)}
    key = {"Standard": "Standard recipe", "Low XL": "Low crosslinker", "Low monomer": "Low monomer"}
    fig, ax = plt.subplots(figsize=(10, 5.2))
    for comp, lab in key.items():
        pts = sorted((float(r["equivalent_years_at_37c"]), float(r["percent_change_from_baseline"])) for r in ag if r["batch"] == "Aryaman" and r["composition"] == comp and r["percent_change_from_baseline"] not in ("", None) and r["n"] not in ("", None))
        col, lw = series[lab]
        ax.plot([p[0] for p in pts], [p[1] for p in pts], "-o", color=col, lw=lw, ms=7, label=lab, markeredgecolor=SURFACE, markeredgewidth=1.5)
        ax.text(pts[-1][0] + 0.3, pts[-1][1], lab, fontsize=9.5, color=INK2, va="center")
    ax.axhline(0, color=GRAY, lw=1)
    ax.set_xlabel("Equivalent time at body temperature (years; 82 C oven, Q10 = 2)"); ax.set_ylabel("Change in dry mass (%)"); ax.set_xlim(0, 27); ax.legend(loc="lower left")
    title(ax, "Accelerated aging: the standard recipe loses about 1 to 2 percent per equivalent year", "Free-standing gels at 82 C for 27 weeks, 4 to 25 gels per point")
    save(fig, "W09_accelerated_aging", "Dry-mass change of free-standing gels under accelerated aging.", "Accelerated aging Database, ambient-corrected package (timepoint_summary.csv); the standard recipe is the SBMA gel, the CBMA series is not plotted",
         source_short="ZwiCoat internal study, accelerated aging")


# ---------------------------------------------------------------- W10 substrate x evidence matrix
def w10_substrate_matrix(ls):
    subs = ["Silicone (PDMS)", "Implant silicone", "PVC", "PEEK", "Parylene-C", POLYURETHANE, "Platinum contacts"]
    cols = ["Adhesion tests\n(lap-shear groups)", "Dip or mold\ncoated", "Sterilization\ntested", "Insertion force\nmeasured", "Implanted\nin vivo"]
    good = [r for r in ls if r["avg"] is not None and not r["untrust"]]
    lsc = collections.Counter(r["sub"] for r in good if r["company"])
    lsc["Silicone (PDMS)"] += sum(1 for r in good if not r["company"])
    M = {
        "Silicone (PDMS)": [lsc["Silicone (PDMS)"], "yes", "yes", "", "mouse, rat, sheep"],
        "Implant silicone": [lsc["Implant silicone"], "yes", "yes", "yes", "sheep (CI arrays)"],
        "PVC": [lsc["PVC"], "yes", "yes", "yes (ET tube)", "rat (ET tube)"],
        "PEEK": [lsc["PEEK"], "yes", "", "", "rat (cranioplasty, ongoing)"],
        "Parylene-C": [lsc["Parylene-C"], "", "", "", ""],
        POLYURETHANE: [lsc[POLYURETHANE], "yes", "yes", "yes (probe cover)", ""],
        "Platinum contacts": ["bridged by film", "yes", "yes", "yes", "mouse (1 yr), sheep"],
    }
    fig, ax = plt.subplots(figsize=(11, 5.6))
    ax.set_xlim(0, len(cols)); ax.set_ylim(0, len(subs)); ax.invert_yaxis(); ax.axis("off")
    for j, c in enumerate(cols): ax.text(j + 0.5, -0.35, c, ha="center", va="bottom", fontsize=10, color=INK2, fontweight="bold")
    for i, s in enumerate(subs):
        ax.text(-0.15, i + 0.5, s, ha="right", va="center", fontsize=11, color=INK)
        for j, v in enumerate(M[s]):
            filled = v not in ("", 0, None)
            ax.add_patch(FancyBboxPatch((j + 0.07, i + 0.1), 0.86, 0.8, boxstyle="round,pad=0,rounding_size=0.08", fc=BLUE if filled else "#F1F2F3", ec=SURFACE, lw=2))
            if filled:
                txt = (f"{v} groups" if isinstance(v, int) else v)
                ax.text(j + 0.5, i + 0.5, txt, ha="center", va="center", fontsize=9.5 if len(str(txt)) < 16 else 8.3, color="white")
    ax.text(0, len(subs) + 0.25, "Blue = data exist in the ZwiCoat archive. Polyurethane rows are the probe-cover studies.", fontsize=9.5, color=MUTED, va="top")
    ax.set_title("What has been tested on which material", loc="left", fontsize=14, fontweight="bold", pad=64)
    save(fig, "W10_substrate_evidence_matrix", "What has been tested on which material: lap-shear groups, coating, sterilization, insertion force and implantation, by substrate.", "ZwiCoat Data archive; published studies",
         source_short="ZwiCoat Data archive; published studies")


# ---------------------------------------------------------------- W11 sterilization
def w11_sterilization():
    conds = [("Steam (wet)", 1), ("EtO (dry)", 1), ("UV (wet)", 1), ("UV (dry)", 1), ("Gamma (wet)", 1), ("Gamma (dry)", 1), ("E-beam (wet)", 0), ("E-beam (dry)", 1)]
    fig, (ax, ax2) = plt.subplots(1, 2, figsize=(11, 4.6), gridspec_kw={"width_ratios": [1, 1.1]})
    ax.set_xlim(0, 2); ax.set_ylim(0, 4); ax.invert_yaxis(); ax.axis("off")
    for k, (c, ok) in enumerate(conds):
        i, j = k % 4, k // 4
        ax.add_patch(FancyBboxPatch((j + 0.05, i + 0.08), 0.9, 0.84, boxstyle="round,pad=0,rounding_size=0.08", fc=BLUE if ok else "#F1F2F3", ec=SURFACE, lw=2))
        ax.text(j + 0.5, i + 0.5, c + ("\npassed" if ok else "\nfailed"), ha="center", va="center", fontsize=10.5, color="white" if ok else INK2, linespacing=1.3)
    ax.set_title("Compatible with multiple sterilization methods", loc="left", fontsize=14, fontweight="bold", pad=14)
    vals = [("Control", 61, GRAY_LIGHT), ("Gamma +\nshipped", 50, BLUE), ("E-beam +\nshipped", 61, BLUE)]
    ax2.bar(range(3), [v[1] for v in vals], color=[v[2] for v in vals], width=0.58, edgecolor=SURFACE, linewidth=2)
    for i, v in enumerate(vals): ax2.text(i, v[1] + 1.5, f"~{v[1]}", ha="center", fontsize=11, color=INK)
    ax2.set_xticks(range(3)); ax2.set_xticklabels([v[0] for v in vals]); ax2.set_ylim(0, 80); ax2.set_ylabel("Lap-shear bond strength (kPa)")
    title(ax2, "Bond strength holds after sterilization and shipping", "Silicone coupons, about 5 per group")
    save(fig, "W11_sterilization", "The coating is compatible with multiple sterilization methods, and the bond strength held after sterilization and shipping.", "ZwiCoat internal study, 2025",
         source_short="ZwiCoat internal study, 2025")


# ---------------------------------------------------------------- W12 numbers (static tile sheet; public facts only)
# Patents: US 11,525,069 B2 (method, issued Dec 13, 2022) and US 11,814,526 B2 (system, issued Nov 14, 2023) are in figures/published/patents.md;
# US 12,116,498 B2 (issued Oct 15, 2024) was confirmed as an issued B2 on Google Patents (same title, same assignee) on 2026-10-29.
PATENT_SCHED = ("ZCMI patent schedule, 2025 (US 11,525,069; 11,814,526; 12,116,498; AU 2017280359; CN ZL201780049849.X; JP 7005535; MX 388986); Kam Hansen, 2026-10-29")
NUMBERS = [("10", "peer-reviewed papers,\n2017 to 2026", "Protein, cells, bacteria and scar all measured, in vitro and in four animal and cadaver models.",
            "Ten papers listed in figures/data/W24_publications.json (DOIs given there)"),
           ("~60%", "thinner fibrotic capsule\naround coated implants", "One year in mice, on human cochlear implant arrays, over platinum and silicone alike (Horne 2023).",
            "Horne R, et al. Acta Biomaterialia 2023;166:212-223 (Fig 7I: 47 versus 18 micrometers, about 62 percent thinner, one year in mice)"),
           ("3", "issued US patents", "The photografting method and the coated-device system are protected.",
            "US 11,525,069 B2 (Dec 13, 2022); US 11,814,526 B2 (Nov 14, 2023); US 12,116,498 B2 (Oct 15, 2024)"),
           ("7", "patents granted in\nfive countries", "United States, Australia, China, Japan and Mexico: the largest device markets.", PATENT_SCHED),
           ("~50%", "less insertion force with\ncoated cochlear implants", "Three studies: human cadaver cochleae twice and a synthetic cochlea (Bennion 2021, Peel 2024, SBIR dataset).",
            "Bennion DM, et al. Otology and Neurotology 2021 (Fig 4A, 42 percent less); Peel A, et al. ACS Applied Bio Materials 2024 (Fig 13A, about 50 percent less); NIH SBIR Phase I dataset, Zenodo, doi:10.5281/zenodo.10459478 (64 percent less); see W07"),
           ("1 year", "film intact after\nimplantation, mice", "The covalent graft was still intact at one year, and the scar capsule stayed thin.",
            "Horne R, et al. Acta Biomaterialia 2023;166:212-223 (Fig 7)"),
           ("6 months", "functional human arrays\nin sheep", "Works on the real device: lower impedance and less inflammation on a working implant.",
            "Ben-Shlomo N, et al. Hearing Research 2026;474:109606 (four weeks); six-month sheep cohort, ZwiCoat internal study, 2026"),
           ("~90%", "less protein, cell and bacterial\nadhesion and friction,\npublished bench studies", "A tightly bound water shell turns away protein, cells and bacteria, so scar and biofilm have no foothold.",
            "Leigh 2017, Leigh 2019, Jensen 2021, Shen 2021, Horne 2023, Bennion 2021, Peel 2024, Barrera 2026 (see W05; median of the plotted bars is about 94 percent, range about 53 to 99)")]


def w12_numbers():
    import textwrap
    fig, ax = plt.subplots(figsize=(13, 6.6)); ax.set_xlim(0, 4); ax.set_ylim(0, 2); ax.invert_yaxis(); ax.axis("off")
    for k, (big, small, take, _) in enumerate(NUMBERS):
        i, j = k // 4, k % 4
        ax.add_patch(FancyBboxPatch((j + 0.04, i + 0.04), 0.92, 0.92, boxstyle="round,pad=0,rounding_size=0.05", fc="#F1F6FA", ec=SURFACE, lw=2))
        ax.text(j + 0.5, i + 0.22, big, ha="center", va="center", fontsize=32, color=BLUE, fontweight="bold")
        ax.text(j + 0.5, i + 0.43, small, ha="center", va="center", fontsize=10.5, color=INK, linespacing=1.25)
        ax.text(j + 0.5, i + 0.73, "\n".join(textwrap.wrap(take, 36)), ha="center", va="center", fontsize=9, color=INK2, linespacing=1.3)
    ax.set_title("The public record in numbers", loc="left", fontsize=14, fontweight="bold", pad=10)
    save(fig, "W12_numbers", "Stat tiles for the public record: ten papers, about 60 percent thinner fibrotic capsule (one year in mice), three issued US patents, seven patents granted in five countries, about 50 percent less cochlear implant insertion force (three studies), one year in mice, six months in sheep, and about 90 percent less adhesion and friction in the published bench studies.",
         "Peer-reviewed publications (see W24); US patents 11,525,069, 11,814,526 and 12,116,498; " + PATENT_SCHED + "; Horne 2023 Acta Biomaterialia (Figs 7, 7I); Bennion 2021 Otology and Neurotology (Fig 4A); Peel 2024 ACS Applied Bio Materials (Fig 13A); NIH SBIR Phase I dataset, Zenodo, doi:10.5281/zenodo.10459478; Ben-Shlomo 2026 Hearing Research; "
         "bench studies Leigh 2017, Leigh 2019, Jensen 2021, Shen 2021, Horne 2023, Bennion 2021, Peel 2024, Barrera 2026 (W05)",
         source_short="Ten peer-reviewed papers and three US patents (see W24); ZwiCoat patent schedule, 2025; Horne et al. 2023, Acta Biomaterialia, Figs 7 and 7I; Bennion et al. 2021, Otology and Neurotology, Fig 4A; Peel et al. 2024, ACS Applied Bio Materials, Fig 13A; NIH SBIR Phase I dataset, Zenodo; Ben-Shlomo et al. 2026, Hearing Research; bench studies in W05")
    json.dump([{"value": b_, "label": s_.replace("\n", " "), "takeaway": t_, "source": src} for b_, s_, t_, src in NUMBERS], open(os.path.join(DATA, "W12_numbers.json"), "w"), indent=1, ensure_ascii=False)


# ---------------------------------------------------------------- W33 archive numbers (tile sheet, same style as W12)
ARCHIVE_SRC = "ZwiCoat Data archive counts, 2026-10-29"


def w33_archive_numbers(ls, ci, exps=None):
    import textwrap
    # Experiments: the same count W01 uses (archive index rows with a year 2016 or later), so the tile and the timeline agree.
    n_exp = sum(1 for r in (exps or []) if exp_year(r) is not None) if exps else 182
    # Same filter as W02: groups with an average, not untrustworthy, substrate recorded (1,056 tests in 430 groups).
    n_tests = int(sum(r["n_s"] or 0 for r in ls if r["avg"] is not None and not r["untrust"] and r["sub"] != "Not recorded"))
    n_ci = len(ci)                                   # CI master database rows
    # 191 experiments, 136 animals, 2,812 raw files and 20 scientists are archive counts taken from content/evidence.md and the
    # evidence map (not recomputable from files read here: experiments_by_year_tag.csv is a later partial extract of 188 rows).
    tiles = [(f"{n_exp:,}", "experiments with a written report", "Every result traces to a dated report in our archive."),
             (f"{n_tests:,}", "adhesion tests on seven substrates", "Durable: bond strength characterized on silicone, PVC, PEEK, parylene-C and polyurethane."),
             (f"{n_ci:,}", "coated cochlear implant samples scored", "Repeatable: a scored process record behind every coated array."),
             ("136", "animals with recorded outcomes (mice, rats, sheep)", "Four models, from bench to a working implant."),
             ("2,812", "raw data files archived", "Traceable: the raw data sit behind every chart."),
             ("20", "scientists and students since 2016", "Ten years of work across two university labs and the company.")]
    fig, ax = plt.subplots(figsize=(10.5, 6.6)); ax.set_xlim(0, 3); ax.set_ylim(0, 2); ax.invert_yaxis(); ax.axis("off")
    for k, (big, small, take) in enumerate(tiles):
        i, j = k // 3, k % 3
        ax.add_patch(FancyBboxPatch((j + 0.04, i + 0.04), 0.92, 0.92, boxstyle="round,pad=0,rounding_size=0.05", fc="#F1F6FA", ec=SURFACE, lw=2))
        ax.text(j + 0.5, i + 0.22, big, ha="center", va="center", fontsize=32, color=BLUE, fontweight="bold")
        ax.text(j + 0.5, i + 0.43, "\n".join(textwrap.wrap(small, 30)), ha="center", va="center", fontsize=10.5, color=INK, linespacing=1.25)
        ax.text(j + 0.5, i + 0.73, "\n".join(textwrap.wrap(take, 34)), ha="center", va="center", fontsize=9, color=INK2, linespacing=1.3)
    ax.set_title("And in the archive", loc="left", fontsize=14, fontweight="bold", pad=10)
    save(fig, "W33_archive_numbers", f"Six counts from the ZwiCoat data archive: {n_exp} experiments with a written report, {n_tests:,} adhesion tests, 468 scored coated cochlear implant samples, 136 animals with recorded outcomes, 2,812 raw data files and 20 scientists and students since 2016.", ARCHIVE_SRC,
         source_short="ZwiCoat Data archive counts, 2026")
    json.dump([{"value": b_, "label": s_, "takeaway": t_, "source": ARCHIVE_SRC} for b_, s_, t_ in tiles], open(os.path.join(DATA, "W33_archive.json"), "w"), indent=1, ensure_ascii=False)
    print("W33 values:", [t[0] for t in tiles])


# ---------------------------------------------------------------- W13 claims x evidence tier
def w13_claims(ev):
    tiers = ["In vitro", "Benchtop device", "Human cadaver tissue", "Small animal", "Large animal"]
    def tier(m):
        m = m.lower()
        if "sheep" in m: return "Large animal"
        if "mouse" in m or "rat" in m: return "Small animal"
        if "cadaver" in m: return "Human cadaver tissue"
        if "in vitro" in m or "pbs" in m: return "In vitro"
        return "Benchtop device"
    claims = ["Fibrosis", "Impedance", "Insertion force", "Infection", "Durability", "Lubricity", "Antifouling in vitro", "Mucus flow"]
    M = {c: collections.Counter() for c in claims}
    for r in ev:
        if r["group"] in M: M[r["group"]][tier(r["model"])] += 1
    fig, ax = plt.subplots(figsize=(11, 6)); ax.set_xlim(0, len(tiers)); ax.set_ylim(0, len(claims)); ax.invert_yaxis(); ax.axis("off")
    mx = max(max(c.values()) for c in M.values())
    for j, t in enumerate(tiers): ax.text(j + 0.5, -0.3, t, ha="center", va="bottom", fontsize=10.5, color=INK2, fontweight="bold")
    for i, c in enumerate(claims):
        ax.text(-0.15, i + 0.5, c, ha="right", va="center", fontsize=11, color=INK)
        for j, t in enumerate(tiers):
            v = M[c][t]
            shade = BLUE_RAMP[min(5, 1 + round(4 * v / mx))] if v else "#F1F2F3"
            ax.add_patch(FancyBboxPatch((j + 0.07, i + 0.1), 0.86, 0.8, boxstyle="round,pad=0,rounding_size=0.08", fc=shade, ec=SURFACE, lw=2))
            if v: ax.text(j + 0.5, i + 0.5, str(v), ha="center", va="center", fontsize=12, color="white" if v / mx > 0.35 else INK, fontweight="bold")
    ax.text(0, len(claims) + 0.25, "Number of independent studies or measurements in the evidence map; darker = more.", fontsize=9.5, color=MUTED, va="top")
    ax.set_title("How much evidence sits behind each claim, and at what level", loc="left", fontsize=14, fontweight="bold", pad=52)
    save(fig, "W13_claims_by_evidence_tier", "Claims versus evidence tier, counted from the evidence map.", "ZwiCoat evidence map (EVIDENCE-MAP.csv, 2026-10-13)",
         source_short="ZwiCoat evidence map, 2026")


# ---------------------------------------------------------------- W14 formulation sweep, W15 thickness
def w14_w_sweep(ls):
    kate = [r for r in ls if str(r.get("campaign") or "").startswith("PHASE C RAW DATA: Kate")]
    fig, ax = plt.subplots(figsize=(9, 5))
    for k, (c, col) in enumerate(zip(sorted(set(r["C"] for r in kate)), [BLUE_RAMP[2], BLUE, BLUE_RAMP[5]])):
        pts = sorted((r["W"], r["avg"], num(r.get("Std (kPa)")) or 0) for r in kate if r["C"] == c)
        ax.errorbar([p[0] for p in pts], [p[1] for p in pts], yerr=[p[2] for p in pts], fmt="-o", color=col, lw=2, ms=7, capsize=3, label=f"crosslinker ratio {c:g}", markeredgecolor=SURFACE, markeredgewidth=1.5)
    ax.set_xlabel("Water ratio of the recipe (more water to the right)"); ax.set_ylabel("Lap-shear bond strength on PVC (kPa)"); ax.set_ylim(0, 650); ax.legend(loc="upper right")
    title(ax, "Adhesion is tunable: less water, stronger bond", "15 formulations on flexible PVC, 6 samples each (ZwiCoat internal study, 2026)")
    save(fig, "W14_formulation_sweep", "Bond strength across a 15-formulation sweep on PVC.", "ZwiCoat internal study, 2026",
         source_short="ZwiCoat internal study, 2026")


ETT = r"G:\My Drive\9 Zwitterion\IA Data n Workups\26.06 ETT paper\data"


def w15_thickness():
    import random
    rows = list(csv.reader(open(os.path.join(ETT, "dip coating thickness", "ETT_dip_coat_I_cure_V_thickness_Sheet1_.csv"), encoding="utf-8-sig")))
    data = [(int(r[0]), [float(v) for v in r[1:] if v]) for r in rows[1:] if r and r[0]]
    random.seed(1)
    fig, ax = plt.subplots(figsize=(7.5, 5))
    for i, (c, vals) in enumerate(data):
        m = sum(vals) / len(vals)
        ax.bar(i, m, color=BLUE_RAMP[1], width=0.55, edgecolor=SURFACE, linewidth=2)
        ax.scatter([i + random.uniform(-0.16, 0.16) for _ in vals], vals, s=26, color=BLUE, edgecolor=SURFACE, linewidth=1, zorder=3)
        ax.text(i, max(vals) + 14, f"{m:.0f} \u00b5m", ha="center", fontsize=11, color=INK, fontweight="bold")
    ax.set_xticks(range(len(data))); ax.set_xticklabels([f"{c} s cure" for c, _ in data]); ax.set_ylabel("Coating thickness (\u00b5m)"); ax.set_ylim(0, 470)
    title(ax, "Thickness is set by cure time", f"Dip-coated endotracheal tubes, {len(data[0][1])} measurements per cure time (ZwiCoat 2026)")
    save(fig, "W15_thickness_vs_cure", "Coating thickness versus initial cure time on ET tubes, every measurement shown.", "26.06 ETT paper/data/dip coating thickness (ZwiCoat, manuscript in preparation)",
         source_short="ZwiCoat internal study, 2026")


def w16_ett_trials():
    import random
    trials = json.load(open(os.path.join(DATA, "ETT_insertion_trials.json")))
    random.seed(2)
    fig, axes = plt.subplots(1, 2, figsize=(11, 5), sharey=False)
    for ax, (s, lab) in zip(axes, [("MH", "Surgeon 1"), ("MB", "Surgeon 2")]):
        for i, cond in enumerate(["uncoated", "coated"]):
            v = [t["impulse_Ns"] for t in trials if t["surgeon"] == s and t["condition"] == cond]
            col = GRAY if cond == "uncoated" else BLUE
            ax.scatter([i + random.uniform(-0.22, 0.22) for _ in v], v, s=34, color=col, edgecolor=SURFACE, linewidth=1, zorder=3)
            ax.hlines(median(v), i - 0.32, i + 0.32, color=INK, lw=2.5, zorder=4)
            ax.text(i, -0.08, f"n = {len(v)}", transform=ax.get_xaxis_transform(), ha="center", va="top", fontsize=9.5, color=MUTED)
        # the manuscript's statistic: tube = experimental unit; coated = mean of the three batch (tube) means
        unc_v = [t["impulse_Ns"] for t in trials if t["surgeon"] == s and t["condition"] == "uncoated"]
        unc = sum(unc_v) / len(unc_v)
        batches = sorted(set(t["batch"] for t in trials if t["surgeon"] == s and t["condition"] == "coated"))
        bm = [sum(v) / len(v) for v in ([t["impulse_Ns"] for t in trials if t["surgeon"] == s and t["batch"] == b] for b in batches)]
        coa = sum(bm) / len(bm)
        ax.set_xticks([0, 1]); ax.set_xticklabels(["Uncoated tube", "Coated tubes (3 batches)"]); ax.set_xlim(-0.6, 1.6); ax.set_ylim(bottom=0)
        ax.set_title(f"{lab}: \u2212{100 * (1 - coa / unc):.0f}% (tube means)", loc="left", fontsize=12, fontweight="bold", pad=10)
    axes[0].set_ylabel("Integrated insertion force per intubation (N\u00b7s)")
    fig.suptitle("Every intubation, two surgeons: coated tubes need about 60 percent less force", x=0.01, ha="left", fontsize=14, fontweight="bold", y=1.02)
    fig.text(0.01, 0.955, "Cadaveric larynx on a load cell; one dot per intubation; coated tubes from three coating batches; black bar = median", fontsize=10.5, color=MUTED)
    save(fig, "W16_ett_insertion_trials", "Per-intubation insertion impulse for coated and uncoated endotracheal tubes, by surgeon.", "26.06 ETT paper/data/ETT force of insertion (ZwiCoat, manuscript in preparation)",
         source_short="ZwiCoat internal study, 2026")


# ---------------------------------------------------------------- W17 to W21: rebuilt deck charts (published literature only)
def w17_textured():
    # Matros E, et al. Plast Reconstr Surg Glob Open 2021;9(3):e3499 (TOPS registry, abstract values, confirmed 2026-10-29):
    # textured share of US cases, 2016 peak vs 2019. Cosmetic 17.83 -> 2.15 %, reconstructive 40.88 -> 7.58 %.
    groups = ["Cosmetic\n(augmentation)", "Reconstructive"]
    v2016, v2019 = [17.83, 40.88], [2.15, 7.58]
    fig, ax = plt.subplots(figsize=(6.6, 5))
    x = range(2)
    ax.bar([i - 0.19 for i in x], v2016, width=0.36, color=GRAY_LIGHT, label="2016", edgecolor=SURFACE, linewidth=2)
    ax.bar([i + 0.19 for i in x], v2019, width=0.36, color=BLUE, label="2019", edgecolor=SURFACE, linewidth=2)
    for i in x:
        ax.text(i - 0.19, v2016[i] + 0.9, f"{v2016[i]:.0f}%", ha="center", fontsize=11.5, color=INK, fontweight="bold")
        ax.text(i + 0.19, v2019[i] + 0.9, f"{v2019[i]:.0f}%", ha="center", fontsize=11.5, color=INK, fontweight="bold")
    ax.set_xticks(list(x)); ax.set_xticklabels(groups, fontsize=10.5); ax.set_ylim(0, 50); ax.set_xlim(-0.6, 1.6)
    ax.set_ylabel("Textured implants (% of US cases)"); ax.legend(loc="upper left", ncol=2)
    ax.grid(axis="x", visible=False)
    title(ax, "Textured breast implants all but disappeared", "Share of US cases using a textured device, 2016 versus 2019 (TOPS registry)")
    save(fig, "W17_textured_implants", "Textured breast implant use fell from 18 to 2 percent of cosmetic cases and from 41 to 8 percent of reconstructive cases between 2016 and 2019.",
         "Matros E, Shamsunder MG, Rubenstein RN, et al. Textured and smooth implant use reported in the TOPS database: epidemiologic implications for BIA-ALCL. Plast Reconstr Surg Glob Open 2021;9(3):e3499. doi:10.1097/GOX.0000000000003499",
         source_short="Matros et al. 2021, Plastic and Reconstructive Surgery Global Open")


def w18_catheter():
    # Pickard R, et al. Lancet 2012;380(9857):1927-1935 (CATHETER trial), abstract values:
    # symptomatic CAUTI treated with antibiotics by 6 weeks: PTFE control 271/2144 = 12.6 %, silver alloy 263/2097 = 12.5 %,
    # nitrofural 228/2153 = 10.6 % (nitrofural difference -2.1 points, 95% CI -4.2 to 0.1). 7,102 patients randomized.
    arms = [("Standard\n(PTFE-coated)", 12.6, GRAY_LIGHT), ("Silver alloy", 12.5, GRAY), ("Nitrofural", 10.6, GRAY_LIGHT)]
    fig, ax = plt.subplots(figsize=(7, 5))
    ax.bar(range(3), [a[1] for a in arms], color=[a[2] for a in arms], width=0.58, edgecolor=SURFACE, linewidth=2)
    for i, a in enumerate(arms): ax.text(i, a[1] + 0.3, f"{a[1]}%", ha="center", fontsize=12, color=INK, fontweight="bold")
    ax.set_xticks(range(3)); ax.set_xticklabels([a[0] for a in arms], fontsize=10.5); ax.set_ylim(0, 16)
    ax.set_ylabel("Symptomatic CAUTI by 6 weeks (%)")
    ax.grid(axis="x", visible=False)
    title(ax, "Silver catheters did not reduce urinary infections", "CATHETER trial, 7,102 randomized patients; infections treated with antibiotics")
    save(fig, "W18_silver_foley_cauti", "In the CATHETER trial, silver alloy urinary catheters did not lower symptomatic catheter-associated urinary tract infection (12.5 percent) compared with standard catheters (12.6 percent).",
         "Pickard R, Lam T, MacLennan G, et al. Antimicrobial catheters for reduction of symptomatic urinary tract infection in adults requiring short-term catheterisation in hospital: a multicentre randomised controlled trial (CATHETER). Lancet 2012;380(9857):1927-1935. doi:10.1016/S0140-6736(12)61380-4",
         source_short="Pickard et al. 2012, The Lancet (CATHETER trial)")


def w19_ett_forest():
    # Risk ratios (95% CI) versus uncoated tube. Silver ETT: Tokmaji G, et al. Cochrane Database Syst Rev 2015;(8):CD009201
    # (1 RCT, 1,509 participants): VAP 0.64 (0.43-0.96), hospital mortality 1.09 (0.93-1.29).
    # Metal-coated ETT: Yang Y, et al. Crit Care 2024;28(1):309 (5 RCTs, 2,157 patients): VAP 0.71 (0.54-0.95), mortality 1.05 (0.86-1.27).
    rows = [("Silver ETT: VAP", 0.64, 0.43, 0.96), ("Silver ETT: mortality", 1.09, 0.93, 1.29),
            ("Metal-coated ETTs: VAP", 0.71, 0.54, 0.95), ("Metal-coated ETTs: mortality", 1.05, 0.86, 1.27)]
    fig, ax = plt.subplots(figsize=(10, 4.6))
    ys = list(range(len(rows)))[::-1]
    ax.set_xscale("log"); ax.set_xlim(0.35, 1.6); ax.set_ylim(-0.7, 3.7)
    ax.axvline(1.0, color=GRAY, lw=1.3, ls=(0, (4, 3)), zorder=1)
    for y, (lab, rr, lo, hi) in zip(ys, rows):
        col = BLUE if hi < 1.0 else GRAY
        ax.hlines(y, lo, hi, color=col, lw=2.4, zorder=2)
        ax.plot([rr], [y], marker="s", ms=11, color=col, zorder=3, markeredgecolor=SURFACE, markeredgewidth=1.2)
        ax.text(1.04, y, f"{rr:.2f} ({lo:.2f} to {hi:.2f})", transform=ax.get_yaxis_transform(), ha="left", va="center", fontsize=11, color=INK)
    ax.set_yticks(ys); ax.set_yticklabels([r[0] for r in rows], fontsize=11)
    ax.set_xticks([0.4, 0.5, 0.7, 1.0, 1.4]); ax.set_xticklabels(["0.4", "0.5", "0.7", "1.0", "1.4"]); ax.minorticks_off()
    ax.grid(False); ax.grid(axis="x", visible=True)
    ax.tick_params(axis="y", length=0)
    ax.text(0.97, 3.62, "favors coated tube", ha="right", va="center", fontsize=10, color=MUTED)
    ax.text(1.03, 3.62, "favors uncoated tube", ha="left", va="center", fontsize=10, color=MUTED)
    ax.text(1.04, 3.62, "Risk ratio (95% CI)", transform=ax.get_yaxis_transform(), ha="left", va="center", fontsize=10, color=MUTED, fontweight="bold")
    ax.set_xlabel("Risk ratio versus uncoated tube (log scale)")
    title(ax, "Silver endotracheal tubes: fewer pneumonias, no survival benefit", "VAP = ventilator-associated pneumonia. Blue = interval excludes 1.0")
    save(fig, "W19_silver_ett_forest", "Silver and metal-coated endotracheal tubes lowered ventilator-associated pneumonia but did not change hospital mortality.",
         "Tokmaji G, Vermeulen H, Muller MC, Kwakman PH, Schultz MJ, Zaat SA. Silver-coated endotracheal tubes for prevention of ventilator-associated pneumonia in critically ill patients. Cochrane Database Syst Rev 2015;(8):CD009201 (silver ETT, 1 RCT, 1,509 participants); Yang Y, Xiong X, Wang X, Dong Q, Pan L. Prevention of ventilator-associated pneumonia by metal-coated endotracheal tubes: a meta-analysis. Crit Care 2024;28(1):309 (5 RCTs, 2,157 patients)",
         source_short="Tokmaji et al. 2015, Cochrane Database of Systematic Reviews; Yang et al. 2024, Critical Care")


def w20_cgm_delay():
    # McClatchey PM, et al. Diabetes 2019;68(10):1892-1901 (abstract): in mice, time to maximum signal after an IV glucose
    # challenge: blood glucose 2 +/- 1 min, implanted CGM 24 +/- 7 min (P = 0.0017). Whiskers = mean +/- SD (2: 1 to 3; 24: 17 to 31).
    fig, ax = plt.subplots(figsize=(6, 5))
    vals = [("Blood glucose", 2, 1, GRAY_LIGHT), ("Implanted CGM", 24, 7, GRAY)]
    for i, (lab, m, sd, col) in enumerate(vals):
        ax.bar(i, m, width=0.56, color=col, edgecolor=SURFACE, linewidth=2)
        ax.errorbar(i, m, yerr=sd, color=INK, capsize=6, lw=1.6, capthick=1.6)
        ax.text(i + 0.34, m, f"{m} min", ha="left", va="center", fontsize=12, color=INK, fontweight="bold")
    ax.set_xticks(range(2)); ax.set_xticklabels([v[0] for v in vals], fontsize=10.5); ax.set_xlim(-0.6, 1.85)
    ax.set_ylim(0, 38); ax.set_ylabel("Time to peak signal (min)")
    ax.grid(axis="x", visible=False)
    title(ax, "The capsule delays the signal", "Mice, after a glucose challenge; mean ± SD")
    save(fig, "W20_cgm_delay", "In mice, an implanted continuous glucose monitor took 24 minutes to reach its peak signal, compared with 2 minutes for blood glucose.",
         "McClatchey PM, McClain ES, Williams IM, et al. Fibrotic encapsulation is the dominant source of continuous glucose monitor delays. Diabetes 2019;68(10):1892-1901. doi:10.2337/db19-0229",
         source_short="McClatchey et al. 2019, Diabetes")


def w21_mucus_flow():
    # Horne R, Escudero C, Ellerman M, Guymon CA, Hansen M. Laryngoscope Investig Otolaryngol 2025;10(2):e70118 (open access, PMC11886986).
    # Coated = zwitterionic pSBMA hydrogel film on PDMS silicone. Tilt (degrees) for mucus to start flowing:
    #   flat sheets: saline ~45 vs 0 (flows when flat); 10% mucus 30 vs <=10 (all hydrogels, plotted at 10); 20% mucus 35 vs 20.
    #   2.6 mm tube, 5% mucus: 48 vs 31 (p = 0.0017, t-test; functional bore of coated tube about 1.6 mm).
    # Dried-plug test: median time to unplug in saline 30 vs 22.5 min (log-rank p = 0.024; 6 tubes per group).
    # Not used: the spec's 5% mucus on sheets, because the paper text gives no pSBMA value for it (only uncoated 40, pPEGMA 5).
    cases = [("Sheet\nsaline", 45, 0, "0"), ("Sheet\n10% mucus", 30, 10, "≤10"), ("Sheet\n20% mucus", 35, 20, "20"), ("2.6 mm tube\n5% mucus", 48, 31, "31")]
    fig, (ax, ax2) = plt.subplots(1, 2, figsize=(12, 5), gridspec_kw={"width_ratios": [1.9, 1]})
    for i, (lab, u, c, ctxt) in enumerate(cases):
        ax.bar(i - 0.19, u, width=0.36, color=GRAY_LIGHT, label="Uncoated" if i == 0 else None, edgecolor=SURFACE, linewidth=2)
        ax.bar(i + 0.19, c, width=0.36, color=BLUE, label="Zwitterionic coating" if i == 0 else None, edgecolor=SURFACE, linewidth=2)
        ax.text(i - 0.19, u + 1, f"{u}", ha="center", fontsize=11, color=INK, fontweight="bold")
        ax.text(i + 0.19, c + 1, ctxt, ha="center", fontsize=11, color=INK, fontweight="bold")
    ax.set_xticks(range(4)); ax.set_xticklabels([c[0] for c in cases], fontsize=10); ax.set_ylim(0, 66)
    ax.set_ylabel("Tilt needed for mucus to start flowing (degrees)"); ax.legend(loc="upper left", ncol=2)
    ax.grid(axis="x", visible=False)
    title(ax, "Mucus flows at a gentler tilt", "Silicone sheets and a 2.6 mm tube, coated versus uncoated")
    ax2.bar([0], [30], width=0.56, color=GRAY_LIGHT, edgecolor=SURFACE, linewidth=2); ax2.bar([1], [22.5], width=0.56, color=BLUE, edgecolor=SURFACE, linewidth=2)
    ax2.text(0, 31.2, "30 min", ha="center", fontsize=11, color=INK, fontweight="bold"); ax2.text(1, 23.7, "22.5 min", ha="center", fontsize=11, color=INK, fontweight="bold")
    ax2.set_xticks([0, 1]); ax2.set_xticklabels(["Uncoated", "Zwitterionic\ncoating"], fontsize=10); ax2.set_ylim(0, 40); ax2.set_xlim(-0.6, 1.6)
    ax2.set_ylabel("Median time to clear a dried plug (min)")
    ax2.grid(axis="x", visible=False)
    title(ax2, "Dried mucus plugs clear sooner", "Six tubes per group, p = 0.024")
    save(fig, "W21_mucus_flow", "Coated silicone let mucus flow at a gentler tilt, on sheets and in a 2.6 mm tube, and cleared dried mucus plugs sooner.",
         "Horne R, Escudero C, Ellerman M, Guymon CA, Hansen M. Enhancing mucus flow and clearance by grafting zwitterionic hydrogel films to luminal surfaces. Laryngoscope Investig Otolaryngol 2025;10(2):e70118. doi:10.1002/lio2.70118",
         source_short="Horne et al. 2025, Laryngoscope Investigative Otolaryngology")


# ---------------------------------------------------------------- W24 to W32: figures built only from the published-paper inventories (figures/published/*.md)
DARKBLUE = "#0A5F94"
CITE = {
    "leigh2017": "Leigh BL, et al. Biomacromolecules 2017;18(8):2389-2401",
    "leigh2019": "Leigh BL, et al. Langmuir 2019;35(4):1100-1110",
    "jensen": "Jensen MJ, et al. ACS Biomaterials Science and Engineering 2021;7(9):4494-4502",
    "shen": "Shen N, et al. ACS Applied Bio Materials 2021;4(2):1283-1293",
    "bennion": "Bennion DM, et al. Otology and Neurotology 2021;42(10):1476-1483",
    "horne2023": "Horne R, et al. Acta Biomaterialia 2023;166:212-223",
    "peel": "Peel A, et al. ACS Applied Bio Materials 2024;7:3124-3135",
    "horne2025": "Horne R, et al. Laryngoscope Investigative Otolaryngology 2025;10(2):e70118",
    "benshlomo": "Ben-Shlomo N, et al. Hearing Research 2026;474:109606",
    "barrera": "Barrera G, et al. ACS Applied Polymer Materials 2026;8(18):16328-16338",
}

PAPERS = [
    dict(year=2017, type="paper", first_author="Leigh", short="neural patterns", title="Photopolymerizable zwitterionic polymer patterns control cell adhesion and guide neural growth",
         journal="Biomacromolecules", doi="10.1021/acs.biomac.7b00579", open_access=False,
         finding="A one-step UV process grafts thin zwitterionic coatings onto glass that cut fibrinogen adsorption to under 10 percent of bare glass, nearly eliminate fibroblast, astrocyte and Schwann cell attachment, and make nerve fibers grow in straight lines along 100 micrometer stripes (in vitro)."),
    dict(year=2019, type="paper", first_author="Leigh", short="PDMS antifouling", title="Antifouling photograftable zwitterionic coatings on PDMS substrates",
         journal="Langmuir", doi="10.1021/acs.langmuir.8b00838", open_access=False,
         finding="A one-step UV process grafts a cross-linked zwitterionic hydrogel about 7 micrometers thick onto silicone so firmly that the gel tears before the silicone interface lets go, cuts fibrinogen adsorption by more than 90 percent and fibroblast attachment 20-fold or more (in vitro)."),
    dict(year=2021, type="paper", first_author="Jensen", short="crosslink density", title="Antifouling and mechanical properties of photografted zwitterionic hydrogel thin-film coatings depend on the cross-link density",
         journal="ACS Biomaterials Science and Engineering", doi="10.1021/acsbiomaterials.1c00852", open_access=True,
         finding="Cross-linked zwitterionic coatings on silicone cut protein, macrophage and fibroblast attachment and friction, with the best balance at roughly 5 to 15 percent cross-linker; more cross-linker makes the gel stiffer and less swollen but less antifouling (in vitro)."),
    dict(year=2021, type="paper", first_author="Shen", short="bacteria in rats", title="Photograftable zwitterionic coatings prevent Staphylococcus aureus and Staphylococcus epidermidis adhesion to PDMS surfaces",
         journal="ACS Applied Bio Materials", doi="10.1021/acsabm.0c01147", open_access=False,
         finding="A zwitterionic coating on silicone cut adhesion of two common device-infection bacteria roughly 10-fold or more in the lab, and in rats left far fewer bacteria on the implant at day 21 and still resisted S. aureus after two weeks in the animal."),
    dict(year=2021, type="paper", first_author="Bennion", short="insertion force", title="Zwitterionic photografted coatings of cochlear implant biomaterials reduce friction and insertion forces",
         journal="Otology and Neurotology", doi="10.1097/MAO.0000000000003288", open_access=False,
         finding="A thin zwitterionic coating cut friction on silicone by more than 90 percent and cut the peak force needed to push a cochlear implant electrode into human cadaveric cochleae by about 40 percent."),
    dict(year=2023, type="paper", first_author="Horne", short="foreign body response", title="Reducing the foreign body response on human cochlear implants and their materials in vivo with photografted zwitterionic hydrogel coatings",
         journal="Acta Biomaterialia", doi="10.1016/j.actbio.2023.05.011", open_access=False,
         finding="Coated silicone and cochlear implant arrays grew a scar capsule about 40 to 70 percent thinner than uncoated ones in mice, from six weeks out to one year, and the coating stayed intact."),
    dict(year=2024, type="paper", first_author="Peel", short="durability in vivo", title="Photografted zwitterionic hydrogel coating durability for reduced foreign body response to cochlear implants",
         journal="ACS Applied Bio Materials", doi="10.1021/acsabm.4c00156", open_access=True,
         finding="The coatings stay on and keep their very low friction after weeks in mice, drying and rewetting, bending, long wear and high loads."),
    dict(year=2025, type="paper", first_author="Horne", short="mucus flow", title="Enhancing mucus flow and clearance by grafting zwitterionic hydrogel films to luminal surfaces",
         journal="Laryngoscope Investigative Otolaryngology", doi="10.1002/lio2.70118", open_access=True,
         finding="Hydrogel films grafted onto silicone sheets and tubes lowered the tilt angle needed to start mucus flow, with the largest benefit on flat sheets and larger tubes, and a dried mucus plug cleared sooner."),
    dict(year=2026, type="paper", first_author="Ben-Shlomo", short="sheep implants", title="Development of zwitterionic hydrogel thin film coatings of cochlear implant electrode arrays that reduce intracochlear inflammation and electrode impedance",
         journal="Hearing Research", doi="10.1016/j.heares.2026.109606", open_access=True,
         finding="In a three-sheep study, coated human cochlear implant arrays had about half the electrode impedance of uncoated arrays at implantation, and at the round window level had fewer cells, fewer macrophages and less fibrous tissue."),
    dict(year=2026, type="paper", first_author="Barrera", short="dual network", title="Photografted dual-network zwitterionic hydrogel coatings for biomaterials",
         journal="ACS Applied Polymer Materials", doi="10.1021/acsapm.6c02510", open_access="unknown",
         finding="Adding a second zwitterionic network on top of the grafted one cut swelling by up to about threefold and nearly doubled adhesion strength, kept friction low, cut fibroblast adhesion by about 90 to 99 percent in vitro and thinned the scar capsule by about 75 percent in rats at six weeks."),
]
DISSERTATIONS = [
    dict(year=2018, type="dissertation", first_author="Leigh", title="PhD dissertation, University of Iowa", journal="University of Iowa", doi=None, finding=None, open_access="unknown"),
    dict(year=2023, type="dissertation", first_author="Peel", title="PhD dissertation, University of Iowa", journal="University of Iowa", doi=None, finding=None, open_access="unknown"),
    dict(year=2024, type="dissertation", first_author="Horne", title="PhD dissertation, University of Iowa", journal="University of Iowa", doi=None, finding=None, open_access="unknown"),
]
PATENTS = [
    dict(year=2022, type="patent", first_author="Cheng", number="US 11,525,069 B2", short="method", title="Durable photopolymerizable cross-linked anti-fouling coatings (method)",
         journal="US 11,525,069 B2, issued Dec 13, 2022", doi=None, open_access=True,
         finding="A method for making a cross-linked anti-fouling coating on a medical-system component: treat the surface with an adhesion-promoting substance, apply a zwitterionic monomer liquid, then polymerize with light in the presence of a cross-linker."),
    dict(year=2023, type="patent", first_author="Cheng", number="US 11,814,526 B2", short="system", title="Durable photopolymerizable cross-linked anti-fouling coatings (system)",
         journal="US 11,814,526 B2, issued Nov 14, 2023", doi=None, open_access=True,
         finding="A system made of a substrate and a cross-linked zwitterionic hydrogel coating that is covalently bonded to the substrate surface and resists adhesion by biomolecules, cells, tissue or bacteria."),
    dict(year=2024, type="patent", first_author="Cheng", number="US 12,116,498 B2", short="coatings", title="Durable photopolymerizable cross-linked anti-fouling coatings",
         journal="US 12,116,498 B2, issued Oct 15, 2024", doi=None, open_access=True,
         finding="Third US patent in the family on durable, photografted, cross-linked anti-fouling coatings (issue date and title confirmed on Google Patents, 2026-10-29)."),
]


def w24_timeline():
    fig, ax = plt.subplots(figsize=(13, 6.4))
    rows = {"patent": 0.0, "dissertation": 3.2, "paper": 6.0}
    colors = {"patent": GRAY, "dissertation": DARKBLUE, "paper": BLUE}
    ax.set_xlim(2016.6, 2027.4); ax.set_ylim(-0.7, 9.4)
    ax.grid(False); ax.grid(axis="x", visible=True)
    for t, y in rows.items():
        ax.hlines(y, 2016.7, 2026.7, color=GRID, lw=3, zorder=1)
    ax.set_yticks(list(rows.values())); ax.set_yticklabels(["Issued US\npatents", "PhD\ndissertations", "Papers"], fontsize=11)
    ax.tick_params(axis="y", length=0); ax.set_xticks(range(2017, 2027))
    ang = 45

    def place(x, y, text, dx=0.0, dy=0.35, fs=9.5, bold_first=True):
        ax.scatter([x + dx], [y], s=130, color=colors[kind], zorder=3, edgecolor=SURFACE, linewidth=2)
        ax.text(x + dx + 0.03, y + dy, text, rotation=ang, rotation_mode="anchor", ha="left", va="bottom", fontsize=fs, color=INK)

    seen = {}
    for p in PAPERS:
        kind = "paper"
        n = sum(1 for q in PAPERS if q["year"] == p["year"])
        k = seen.get(p["year"], 0); seen[p["year"]] = k + 1
        dx = 0.0 if n == 1 else ((-0.3, 0.3) if n == 2 else (-0.42, 0.0, 0.42))[k]
        place(p["year"], rows["paper"], f"{p['first_author']}, {p['short']}", dx=dx)
    seen = {}
    for p in DISSERTATIONS:
        kind = "dissertation"
        n = sum(1 for q in DISSERTATIONS if q["year"] == p["year"])
        k = seen.get(p["year"], 0); seen[p["year"]] = k + 1
        dx = 0.0 if n == 1 else (-0.25, 0.25)[k]
        place(p["year"], rows["dissertation"], f"{p['first_author']} {p['year']}", dx=dx, dy=0.3)
    for p in PATENTS:
        kind = "patent"
        place(p["year"], rows["patent"], f"{p['number'].replace(' B2', '')}, {p['short']}" if p["short"] != "coatings" else p["number"].replace(" B2", ""), dy=0.3)
    ax.spines["left"].set_visible(False)
    title(ax, "A ten-year public record: ten papers, three dissertations, three patents",
          "Peer-reviewed papers by year of the journal issue, University of Iowa dissertations, and issued US patents, 2017 to 2026")
    save(fig, "W24_publication_timeline", "Timeline of the public record, 2017 to 2026: ten peer-reviewed papers, three PhD dissertations and three issued US patents.",
         "Leigh 2017 Biomacromolecules; Leigh 2019 Langmuir; Jensen 2021 ACS Biomaterials Science and Engineering; Shen 2021 ACS Applied Bio Materials; Bennion 2021 Otology and Neurotology; Horne 2023 Acta Biomaterialia; "
         "Peel 2024 ACS Applied Bio Materials; Horne 2025 Laryngoscope Investigative Otolaryngology; Ben-Shlomo 2026 Hearing Research; Barrera 2026 ACS Applied Polymer Materials; dissertations Leigh 2018, Peel 2023, Horne 2024 (University of Iowa); "
         "US patents 11,525,069 (2022), 11,814,526 (2023), 12,116,498 (2024); DOIs in figures/data/W24_publications.json",
         source_short="Ten peer-reviewed papers, 2017 to 2026; three University of Iowa dissertations; US patents 11,525,069, 11,814,526 and 12,116,498")
    out = [{k: p[k] for k in ("year", "type", "first_author", "title", "journal", "doi", "finding", "open_access")} for p in PAPERS + DISSERTATIONS + PATENTS]
    json.dump(out, open(os.path.join(DATA, "W24_publications.json"), "w"), indent=1)


# ---------------------------------------------------------------- W25 sheep impedance components
def w25_sheep_impedance():
    # Ben-Shlomo N, et al. Hearing Research 2026;474:109606, Fig 3B to 3D. Bar heights read from the figure (kOhm, approximate);
    # p values printed on the figure (2-way ANOVA, Sidak) are exact. Uncoated, coated, p.
    panels = [("Total impedance", [(30, 10.5, "p < 0.0001"), (17.5, 9.5, "p = 0.0007")]),
              ("Polarization impedance\n(electrode surface)", [(20, 6, "p < 0.0001"), (9.5, 6, "p = 0.2586, not significant")]),
              ("Access resistance\n(material around the electrode)", [(12.5, 6, "p = 0.0019"), (11, 5, "p = 0.0084")])]
    fig, axes = plt.subplots(1, 3, figsize=(13, 5.4), sharey=True)
    for k, (ax, (pt, vals)) in enumerate(zip(axes, panels)):
        for i, (u, c, ptxt) in enumerate(vals):
            ax.bar(i - 0.19, u, width=0.34, color=GRAY_LIGHT, label="Uncoated" if (k == 0 and i == 0) else None, edgecolor=SURFACE, linewidth=2)
            ax.bar(i + 0.19, c, width=0.34, color=BLUE, label="Coated" if (k == 0 and i == 0) else None, edgecolor=SURFACE, linewidth=2)
            ax.text(i - 0.19, u + 0.6, f"~{u:g}", ha="center", fontsize=10, color=INK2)
            ax.text(i + 0.19, c + 0.6, f"~{c:g}", ha="center", fontsize=10, color=INK2)
            if ptxt:
                bracket(ax, i - 0.19, i + 0.19, max(u, c) + 4.2, ptxt.replace(", not significant", "\n(not significant)"), 0.9, fs=9.5)
        ax.set_xticks([0, 1]); ax.set_xticklabels(["At implantation", "4 weeks"], fontsize=10.5); ax.set_xlim(-0.6, 1.6); ax.set_ylim(0, 40)
        ax.grid(axis="x", visible=False); ptitle(ax, pt)
    axes[0].set_ylabel("Impedance (kOhm)"); axes[0].legend(loc="upper right")
    ftitle(fig, "Lower electrode impedance with the coating; total impedance and access resistance stay lower at four weeks",
           "Three sheep, one coated and one uncoated human array each")
    save(fig, "W25_sheep_impedance_components", "Total impedance, polarization impedance and access resistance of coated and uncoated human cochlear implant arrays in sheep, at implantation and at four weeks.",
         "Ben-Shlomo N, et al. Development of zwitterionic hydrogel thin film coatings of cochlear implant electrode arrays that reduce intracochlear inflammation and electrode impedance. Hearing Research 2026;474:109606, Fig 3B to 3D (bar heights approximate, read from the published figure; p values as printed). doi:10.1016/j.heares.2026.109606",
         source_short="Ben-Shlomo et al. 2026, Hearing Research, Figs 3B to 3D")


# ---------------------------------------------------------------- W26 sheep histology
def w26_sheep_histology():
    # Ben-Shlomo 2026, Fig 6E to 6G, round window level. Pooled bars and per-sheep points read from the figure (approximate); pooled p exact.
    # Each: (panel, unit, pooled U, pooled C, p, [sheep1 (U, C), sheep2, sheep3])
    panels = [("Cell nuclei density", "per 10⁵ µm³", 19, 4.5, "p = 0.0020", [(24.5, 4.5), (8.5, 8.5), (24, 2)], 32),
              ("Macrophage density", "per 10⁵ µm³", 9.8, 2.6, "p = 0.0063", [(13.3, 1.2), (4.5, 5.5), (11.8, 0.9)], 18),
              ("Fibrosis", "% of scala tympani volume", 16.5, 2.5, "p = 0.0101", [(29, 3.5), (5, 2.5), (15, 1)], 38)]
    fig, axes = plt.subplots(1, 3, figsize=(13, 5.6))
    for ax, (pt, unit, pu, pc, ptxt, sheep, ymax) in zip(axes, panels):
        ax.bar(0, pu, width=0.55, color=GRAY_LIGHT, edgecolor=SURFACE, linewidth=2)
        ax.bar(1, pc, width=0.55, color=BLUE, edgecolor=SURFACE, linewidth=2)
        ly = {}
        for s_i in sorted(range(3), key=lambda q: sheep[q][0]):
            ly[s_i] = sheep[s_i][0] if not ly or sheep[s_i][0] - max(ly.values()) >= ymax * 0.055 else max(ly.values()) + ymax * 0.055
        for s, (u, c) in enumerate(sheep):
            ax.plot([0, 1], [u, c], color=INK2, lw=1, alpha=0.55, zorder=3)
            ax.scatter([0, 1], [u, c], s=46, color=INK, zorder=4, edgecolor=SURFACE, linewidth=1)
            ax.text(-0.12, ly[s], f"sheep {s + 1}", ha="right", va="center", fontsize=8.5, color=INK2)
        bracket(ax, 0, 1, ymax * 0.93, f"pooled {ptxt}", ymax * 0.025, fs=10)
        ax.set_xticks([0, 1]); ax.set_xticklabels(["Uncoated", "Coated"], fontsize=10.5); ax.set_xlim(-0.95, 1.6); ax.set_ylim(0, ymax)
        ax.set_ylabel(unit); ax.grid(axis="x", visible=False); ptitle(ax, pt)
    ftitle(fig, "Less inflammation and scar at the round window of the sheep cochlea",
           "Three sheep, 4 weeks, one coated and one uncoated human array each; bars = pooled mean, dots and lines = each sheep;\n"
           "pooled p values as printed (2-way ANOVA, Sidak)", nsub=2)
    save(fig, "W26_sheep_histology", "At the round window of the sheep cochlea, coated arrays had fewer cell nuclei, fewer macrophages and less fibrosis than uncoated arrays when the three sheep were pooled.",
         "Ben-Shlomo N, et al. Development of zwitterionic hydrogel thin film coatings of cochlear implant electrode arrays that reduce intracochlear inflammation and electrode impedance. Hearing Research 2026;474:109606, Fig 6E to 6G (bar and per-sheep pooled p values as printed). doi:10.1016/j.heares.2026.109606",
         source_short="Ben-Shlomo et al. 2026, Hearing Research, Figs 6E to 6G")


# ---------------------------------------------------------------- W27 capsule thickness in mice (Horne 2023)
def w27_capsule_mice():
    # Horne 2023 Acta Biomaterialia, Fig 5D (flat sheets, 6 wk): text means 82 / 43 / 27 um; Tukey vs uncoated p = 0.061 (pPEGDMA), 0.010 (zwitterionic);
    # SEM read from the figure (about 27, 17, 11; approximate). Fig 7I (human CI arrays, 1 yr): 47 vs 18 um (text), p = 0.026, n = 3 to 4.
    fig, (axA, axB) = plt.subplots(1, 2, figsize=(11, 5.6), gridspec_kw={"width_ratios": [1, 1]})
    vals = [(82, 27, GRAY, "Uncoated"), (27, 11, BLUE, "Coated")]
    for i, (m, sem, col, lab) in enumerate(vals):
        axA.bar(i, m, width=0.55, color=col, edgecolor=SURFACE, linewidth=2)
        axA.errorbar(i, m, yerr=sem, color=INK, capsize=5, lw=1.4, capthick=1.4)
        axA.text(i, 3, f"{m}", ha="center", va="bottom", fontsize=12, color="white", fontweight="bold")
    bracket(axA, 0, 1, 124, "−67%, p = 0.010", 3, fs=10)
    axA.set_xticks(range(2)); axA.set_xticklabels([v[3] for v in vals], fontsize=10); axA.set_ylim(0, 140); axA.set_xlim(-0.6, 1.6)
    axA.set_ylabel("Capsule thickness (µm)"); axA.grid(axis="x", visible=False)
    ptitle(axA, "A. Six weeks, flat silicone sheets, n = 3 to 5")
    for i, (m, col, lab) in enumerate([(47, GRAY, "Uncoated"), (18, BLUE, "Coated")]):
        axB.bar(i, m, width=0.55, color=col, edgecolor=SURFACE, linewidth=2)
        axB.text(i, 1.5, f"{m}", ha="center", va="bottom", fontsize=12, color="white", fontweight="bold")
    bracket(axB, 0, 1, 56, "−62%, p = 0.026", 1.5, fs=10)
    axB.set_xticks([0, 1]); axB.set_xticklabels(["Uncoated", "Coated"], fontsize=10); axB.set_ylim(0, 70); axB.set_xlim(-0.6, 1.6)
    axB.set_ylabel("Capsule thickness (µm)"); axB.grid(axis="x", visible=False)
    ptitle(axB, "B. One year, human cochlear implant arrays, n = 3 to 4")
    ftitle(fig, "A thinner scar capsule around coated implants in mice",
           "Mice, subcutaneous implants. Means from the text; whiskers in A are SEM, approximate, read from the published figure\n"
           "Axes differ because the implant shapes differ; Horne et al. 2023", nsub=2)
    save(fig, "W27_capsule_thickness_mice", "In mice, scar capsules were 67 percent thinner around coated silicone at six weeks and 62 percent thinner around coated human cochlear implant arrays at one year.",
         "Horne R, Ben-Shlomo N, Jensen M, et al. Reducing the foreign body response on human cochlear implants and their materials in vivo with photografted zwitterionic hydrogel coatings. Acta Biomaterialia 2023;166:212-223, Figs 5D and 7I (means and p values from the text; SEM whiskers approximate, read from the published figure). doi:10.1016/j.actbio.2023.05.011",
         source_short="Horne et al. 2023, Acta Biomaterialia, Figs 5D and 7I")


# ---------------------------------------------------------------- W28 durability (Peel 2024)
def _w28_panel_a(axA):
    groups = [("Uncoated", (0.25, 0.27), (GRAY_LIGHT, GRAY)), ("Coated", (0.027, 0.03), ("#A9D2EE", BLUE))]
    for g, (lab, (pr, ex), (c1, c2)) in enumerate(groups):
        axA.bar(g * 3, pr, width=0.9, color=c1, edgecolor=SURFACE, linewidth=2)
        axA.bar(g * 3 + 1, ex, width=0.9, color=c2, edgecolor=SURFACE, linewidth=2)
        axA.text(g * 3, pr + 0.006, f"~{pr:g}", ha="center", fontsize=9, color=INK2)
        axA.text(g * 3 + 1, ex + 0.006, f"~{ex:g}", ha="center", fontsize=9, color=INK2)
        axA.text(g * 3 + 0.5, -0.115, lab, transform=axA.get_xaxis_transform(), ha="center", va="top", fontsize=10.5, color=INK, fontweight="bold")
    axA.set_xticks([x for g in range(2) for x in (g * 3, g * 3 + 1)]); axA.set_xticklabels(["pristine", "explanted"] * 2, fontsize=9)
    axA.set_ylim(0, 0.34); axA.set_xlim(-0.8, 5.0); axA.set_ylabel("Coefficient of friction (sapphire probe, in PBS)"); axA.grid(axis="x", visible=False)


W28_SOURCE = ("Peel A, Bennion D, Horne R, Hansen MR, Guymon CA. Photografted zwitterionic hydrogel coating durability for reduced foreign body response to cochlear implants. ACS Applied Bio Materials 2024;7:3124-3135, Figs 4 and 5A "
              "(the at-least-90-percent statement is from the text; the coated series is the SBMA coating, the CBMA coating is not plotted). doi:10.1021/acsabm.4c00156")


def w28_durability_peel():
    # Peel A, et al. ACS Appl Bio Mater 2024;7:3124-3135. Fig 4 (read from figure, approximate): absolute coefficient of friction, sapphire probe in PBS.
    #   uncoated 0.25 pristine / 0.27 explanted; CBMA 0.035 / 0.035 (dropped from the chart, owner rule 2026-10-30); SBMA 0.027 / 0.03 (shown as "Coated"). Explanted = 3 weeks in mice.
    # Fig 5A (read from figure, approximate): SBMA-coated PDMS relative to uncoated = 1.0:
    #   aorta 0.03, bladder 0.03, dermis 0.06, fat 0.02, trachea 0.05, steel 0.05. Text (exact): at least 90 percent lower for every surface.
    fig, (axA, axB) = plt.subplots(1, 2, figsize=(14, 6), gridspec_kw={"width_ratios": [1.3, 1.4]})
    _w28_panel_a(axA)
    ptitle(axA, "A. Friction before and after 3 weeks in mice")
    tiss = [("Aorta", 0.03), ("Bladder", 0.03), ("Dermis", 0.06), ("Fat", 0.02), ("Trachea", 0.05), ("Steel", 0.05)]
    for i, (lab, c) in enumerate(tiss):
        axB.bar(i - 0.19, 1, width=0.34, color=GRAY_LIGHT, label="Uncoated" if i == 0 else None, edgecolor=SURFACE, linewidth=2)
        axB.bar(i + 0.19, c, width=0.34, color=BLUE, label="Coated" if i == 0 else None, edgecolor=SURFACE, linewidth=2)
        axB.text(i + 0.19, c + 0.025, f"~{c:g}", ha="center", fontsize=9.5, color=INK2)
    axB.set_xticks(range(6)); axB.set_xticklabels([t[0] for t in tiss], fontsize=10.5); axB.set_ylim(0, 1.15)
    axB.set_ylabel("Friction relative to uncoated silicone"); axB.legend(loc="upper right"); axB.grid(axis="x", visible=False)
    ptitle(axB, "B. Friction against five guinea pig tissues and steel")
    ftitle(fig, "The coating keeps its low friction after weeks in mice",
           "Mice, 3 weeks, n of 4 or more (A); at least 90 percent lower friction against every surface tested (B, stated in the text); bar Peel et al. 2024", nsub=1)
    save(fig, "W28_durability_peel", "Coated silicone kept about 90 percent lower friction after three weeks in mice, and at least 90 percent lower against steel and five animal tissues.", W28_SOURCE,
         source_short="Peel et al. 2024, ACS Applied Bio Materials, Figs 4 and 5A")
    # Panel A alone, for the durability page
    fig, ax = plt.subplots(figsize=(8, 6))
    _w28_panel_a(ax); ax.set_xlim(-0.7, 4.7)
    title(ax, "Friction stays low after 3 weeks in mice", "Coated vs uncoated silicone, pristine vs explanted; Peel et al. 2024")
    save(fig, "W28a_friction_after_explant", "Coated silicone kept about 90 percent lower friction than uncoated silicone after three weeks in mice, the same as before implantation.", W28_SOURCE,
         source_short="Peel et al. 2024, ACS Applied Bio Materials, Fig 4")


# ---------------------------------------------------------------- W29 bacteria in rats (Shen 2021)
def w29_bacteria_rats():
    # Shen N, et al. ACS Appl Bio Mater 2021;4:1283-1293. Fig 7C: day-21 explants, S. aureus counts/hpf, uncoated ~940 vs pCBMA ~155 (t = 7.011, df = 69, p < 0.0001).
    # Fig 7D: viable colonies, ~690 vs ~35 (n = 6 implants, p = 0.0006). Fig 8: implants after 2 weeks in vivo then 24 h S. aureus challenge, ~2520 vs ~210
    # counts/hpf (30 fields per group from 6 rats, p < 0.0001). All values approximate, read from the figure; p values exact.
    fig, axes = plt.subplots(1, 3, figsize=(13, 5.6))
    spec = [("A1. Bacteria on implants at day 21", "Adherent S. aureus (counts per field)", 940, 155, "p < 0.0001", 1250, "n about 71 fields"),
            ("A2. Live colonies recovered at day 21", "Viable colonies (as plotted)", 690, 35, "p = 0.0006", 920, "n = 6 implants"),
            ("B. Coating after 2 weeks in rats, then challenged", "Adherent S. aureus (counts per field)", 2520, 210, "p < 0.0001", 3300, "n = 30 fields, 6 rats")]
    for ax, (pt, yl, u, c, ptxt, ymax, nn) in zip(axes, spec):
        ax.bar(0, u, width=0.55, color=GRAY, edgecolor=SURFACE, linewidth=2)
        ax.bar(1, c, width=0.55, color=BLUE, edgecolor=SURFACE, linewidth=2)
        ax.text(0, u + ymax * 0.015, f"~{u:,}", ha="center", va="bottom", fontsize=11, color=INK, fontweight="bold")
        ax.text(1, c + ymax * 0.015, f"~{c:,}", ha="center", va="bottom", fontsize=11, color=INK, fontweight="bold")
        bracket(ax, 0, 1, ymax * 0.88, f"{ptxt}", ymax * 0.025, fs=10.5)
        ax.set_xticks([0, 1]); ax.set_xticklabels([f"Uncoated", f"Coated"], fontsize=10.5); ax.set_xlim(-0.6, 1.6); ax.set_ylim(0, ymax)
        ax.set_ylabel(yl, fontsize=10); ax.grid(axis="x", visible=False); ptitle(ax, pt)
        ax.text(0.5, -0.17, nn, transform=ax.transAxes, ha="center", fontsize=9.5, color=MUTED)
    ftitle(fig, "Coated implants carry far fewer bacteria in rats",
           "Rats, six per group, 21 days; S. aureus challenge; p values as printed; Shen et al. 2021")
    save(fig, "W29_bacteria_rats", "In rats challenged with S. aureus, coated silicone implants carried far fewer bacteria and live colonies at day 21, and a coating kept in a rat for two weeks still resisted a fresh S. aureus challenge.",
         "Shen N, Cheng E, Whitley JW, Horne RR, Leigh B, Xu L, Jones BD, Guymon CA, Hansen MR. Photograftable zwitterionic coatings prevent Staphylococcus aureus and Staphylococcus epidermidis adhesion to PDMS surfaces. ACS Applied Bio Materials 2021;4(2):1283-1293, Figs 7C, 7D and 8 (p values as printed). doi:10.1021/acsabm.0c01147",
         source_short="Shen et al. 2021, ACS Applied Bio Materials, Figs 7C, 7D and 8")


# ---------------------------------------------------------------- W30 cross-linker tradeoff (Jensen 2021)
def w30_crosslinker():
    # Jensen MJ, et al. ACS Biomater Sci Eng 2021;7(9):4494-4502. Values read from the figures (approximate); x = cross-linker percent of monomer.
    # Swelling (Fig 4A, PBS, percent of dry mass) at 1.6/4.8/13/31.3 %. Compressive modulus (Fig 4B, MPa) shown relative to the lowest cross-linker (1.6 %):
    #   SBMA 1 / 1.1 / 6 / 18.8 (plotted); CBMA 4.8 / 17.5 / 34.7 against a 1.6 % value of about 0.7 MPa implied by the text's 50-fold rise (not plotted).
    # Friction (Fig 5B) and fibroblast density (Fig 3G) relative to bare silicone (PDMS = 1); fibroblast uncoated = 11.6 x 10^-4 cells/um2.
    xs4 = [1.6, 4.8, 13, 31.3]
    # Kam (2026-11-02): W30 shows BOTH series again (the one chart where the chemistry is the point).
    # CBMA values (Jensen Figs 3G, 4A, 4B, 5B): swelling PBS 980/520/310/225; stiffness 4.8/17.5/34.7 MPa over an implied 0.7 MPa at 1.6 % (50-fold rise in the text);
    # friction 0.053/0.060/0.10/0.145; fibroblast 3.2/0.4/0.15/0.05/0.6/0.2/0.45 (x 10^-4 cells/um2, uncoated 11.6).
    swell = {"SBMA": [750, 400, 260, 215], "CBMA": [980, 520, 310, 225]}
    mod = {"SBMA": [1, 1.1, 6, 18.8], "CBMA": [1, 4.8 / 0.7, 17.5 / 0.7, 34.7 / 0.7]}
    fric = {"SBMA": [0.055, 0.063, 0.075, 0.10], "CBMA": [0.053, 0.060, 0.10, 0.145]}
    xsf = [0, 1.6, 4.8, 13, 31.3, 50, 66.7]
    fib = {"SBMA": [v / 11.6 for v in (6.8, 1.5, 1.75, 1.55, 2.3, 3.1, 4.4)],
           "CBMA": [v / 11.6 for v in (3.2, 0.4, 0.15, 0.05, 0.6, 0.2, 0.45)]}
    # Kam (2026-11-02): no orange on W30. SBMA = solid blue circles; CBMA = white circles outlined in blue (dashed line), same convention as W31.
    sty = {"SBMA": dict(color=BLUE, marker="o", ls="-", mfc=BLUE), "CBMA": dict(color=BLUE, marker="o", ls=(0, (5, 3)), mfc="white")}
    fig, axes = plt.subplots(1, 4, figsize=(15, 4.9), sharex=True)
    panels = [(axes[0], xs4, swell, "Swelling in saline (% of dry mass)", "Swelling", False, None),
              (axes[1], xs4, mod, "Stiffness, relative to the 1.6% sample", "Stiffness", False, None),
              (axes[2], xs4, fric, "Friction relative to bare silicone", "Friction", True, 1.0),
              (axes[3], xsf, fib, "Fibroblast density relative to bare silicone", "Fibroblast attachment", True, 1.0)]
    for ax, xs, d, yl, pt, log, ref in panels:
        ax.axvspan(5, 15, color=BLUE, alpha=0.08, lw=0)
        for name, ys in d.items():
            ax.plot(xs, ys, label=name, lw=2, ms=7, markeredgewidth=1.8, markeredgecolor=sty[name]["color"], **sty[name])
        if log:
            ax.set_yscale("log"); ax.axhline(ref, color=GRAY, lw=1.2, ls=(0, (4, 3))); ax.text(68, ref * 1.12, "bare silicone = 1", ha="right", fontsize=9, color=MUTED)
            ax.set_ylim(0.003 if pt != "Friction" else 0.03, 2)
        else:
            ax.set_ylim(bottom=0)
        ax.set_xlim(-2, 70); ax.set_xticks([0, 10, 20, 30, 40, 50, 60, 70]); ax.set_ylabel(yl); ax.set_xlabel("Cross-linker (% of monomer)")
        ptitle(ax, pt)
    axes[0].legend(loc="upper right")
    fig.subplots_adjust(wspace=0.42)
    ftitle(fig, "One chemistry, a tunable window",
           "Shaded band = the window the paper reports as best for antifouling, about 5 to 15 percent cross-linker (workable from 1 to 50 percent)\n"
           "More cross-linker gives a stiffer, less swollen gel. In vitro, free-standing gels for swelling and stiffness; Jensen et al. 2021", nsub=2)
    save(fig, "W30_crosslinker_tradeoff", "More crosslinker makes the gel stiffer and less swollen. Protein, cell and friction benefits are strongest at about 5 to 15 percent crosslinker. Two zwitterionic chemistries, SBMA and CBMA, follow the same pattern.",
         "Jensen MJ, Peel A, Horne R, Chamberlain J, Xu L, Hansen MR, Guymon CA. Antifouling and mechanical properties of photografted zwitterionic hydrogel thin-film coatings depend on the cross-link density. ACS Biomaterials Science and Engineering 2021;7(9):4494-4502, Figs 3G, 4A, 4B, 5B (stiffness shown relative to the lowest cross-linker, with the CBMA 1.6 percent value implied by the text; both the SBMA and the CBMA coatings are plotted; the 5 to 15 percent window is stated in the text). doi:10.1021/acsbiomaterials.1c00852",
         source_short="Jensen et al. 2021, ACS Biomaterials Science and Engineering, Figs 3G, 4A, 4B and 5B")


# ---------------------------------------------------------------- W31 bond strength vs benzophenone (Leigh 2019)
def w31_bond_strength():
    # Leigh BL, et al. Langmuir 2019;35(4):1100-1110, Fig 6 (read from figure, N/m2 x 10^4; shown here in kPa, 10^4 N/m2 = 10 kPa). Approximate.
    # Thresholds from the text (exact): adhesive failure below 2.5 mg/mL (SBMA) and below 5 mg/mL (CBMA); cohesive failure (gel tears first) at or above.
    # Owner rule (2026-10-30): the image shows the SBMA coating only, as a single panel with no chemistry name; the CBMA panel (pCBMA) is not plotted.
    bp = [0, 0.25, 0.5, 0.75, 1, 2.5, 5, 10, 50]
    asp, swl, thr = [0.9, 3.9, 4.3, 5.4, 5.0, 5.2, 6.1, 7.4, 7.1], [0, 1.0, 1.5, 1.5, 0.5, 3.4, 3.9, 3.7, 3.5], 5
    fig, ax = plt.subplots(figsize=(8.2, 5.4))
    xs = list(range(len(bp)))
    ax.axvspan(thr - 0.5, len(bp) - 0.5, color=BLUE, alpha=0.09, lw=0)
    # Same marker convention as W30: as prepared = solid blue circles; after swelling = white circles outlined in blue.
    ax.plot(xs, [v * 10 for v in asp], color=BLUE, marker="o", lw=2, ms=7, markeredgecolor=BLUE, label="As prepared")
    ax.plot(xs, [v * 10 for v in swl], color=BLUE, marker="o", lw=2, ls="--", ms=7, mfc="white", markeredgecolor=BLUE, markeredgewidth=1.8, label="After 48 h swelling in water")
    ax.axvline(thr - 0.5, color=BLUE, lw=1.2)
    ax.text(thr - 0.4, 108, f"gel tears before the\ninterface lets go,\nfrom {bp[thr]:g} mg/mL", fontsize=10.5, color=DARKBLUE, va="top", ha="left")
    ax.text(thr - 0.6, 108, "interface fails first", fontsize=10.5, color=INK2, va="top", ha="right")
    ax.set_xticks(xs); ax.set_xticklabels([f"{b:g}" for b in bp]); ax.set_ylim(0, 112); ax.set_xlim(-0.4, len(bp) - 0.6)
    ax.set_xlabel("Grafting agent concentration (mg/mL)"); ax.grid(axis="x", visible=False)
    ax.set_ylabel("Shear strength at break (kPa)"); ax.legend(loc="upper left", bbox_to_anchor=(0.01, 0.80))
    ftitle(fig, "The bond gets stronger until the gel tears before the interface lets go",
           "Grafted hydrogel films on silicone, pull test, in vitro;\nfailure threshold from the text; Leigh et al. 2019", nsub=2)
    save(fig, "W31_bond_strength_vs_grafting_agent", "Shear bond strength of a zwitterionic film on silicone rises with grafting agent concentration until failure moves from the silicone interface into the gel itself, at 2.5 mg/mL.",
         "Leigh BL, Cheng E, Xu L, Derk A, Hansen MR, Guymon CA. Antifouling photograftable zwitterionic coatings on PDMS substrates. Langmuir 2019;35(4):1100-1110, Fig 6 (values approximate, read from the published figure and converted from N/m2 x 10^4 to kPa; failure threshold from the text; the plotted series is the SBMA coating, the CBMA panel is not shown, its threshold is 5 mg/mL). doi:10.1021/acs.langmuir.8b00838",
         source_short="Leigh et al. 2019, Langmuir, Fig 6")


# ---------------------------------------------------------------- W32 every published in-vivo comparison (data only)
def w32_invivo_studies():
    ref = {"horne2023": ("Horne et al.", 2023, "Acta Biomaterialia"), "peel": ("Peel et al.", 2024, "ACS Applied Bio Materials"),
           "shen": ("Shen et al.", 2021, "ACS Applied Bio Materials"), "benshlomo": ("Ben-Shlomo et al.", 2026, "Hearing Research"),
           "bennion": ("Bennion et al.", 2021, "Otology and Neurotology"),
           "barrera": ("Barrera et al.", 2026, "ACS Applied Polymer Materials"),
           "zwicoat_ett": ("ZwiCoat internal study", 2026, "unpublished; raw data on Zenodo"),
           "sbir": ("NIH SBIR Phase I dataset", 2024, "Zenodo, doi:10.5281/zenodo.10459478")}
    rows = []

    def add(r, species, dur, dev, metric, u, c, unit, n, p, exact, fig, ptxt=None, setting="in vivo", note=None):
        a, y, j = ref[r]
        pct = round(100 * (c - u) / u) if (u not in (None, 0) and c is not None) else None
        rows.append(dict(paper=a, year=y, journal=j, species=species, duration=dur, device_or_substrate=dev, metric=metric, uncoated=u, coated=c, unit=unit,
                         pct_change=pct, n=n, p=p, p_text=ptxt if ptxt is not None else (None if p is None else str(p)), exact=exact, figure=fig, setting=setting, note=note))
    H = "mice (CBA/J)"
    add("horne2023", H, "6 weeks", "PDMS flat sheet, pCBMA 10% cross-linker", "Capsule thickness", 82, 27, "um", "3 to 5", 0.010, True, "Fig 5D", ptxt="0.010", note="means from the text; Tukey vs uncoated")
    add("horne2023", H, "6 weeks", "PDMS flat sheet, pPEGDMA (non-zwitterionic control)", "Capsule thickness", 82, 43, "um", "3 to 5", 0.061, True, "Fig 5D", ptxt="0.061 (ns)", note="means from the text; not significant")
    for xl, v, p, ptxt in ((0, 28, 0.3322, "0.3322 (ns)"), (5, 14.7, 0.0039, None), (10, 14, 0.0031, None), (25, 17.4, 0.0031, None), (50, 18.3, 0.0265, None)):
        add("horne2023", H, "6 weeks", f"PDMS cylinder 1.2 mm OD, pCBMA {xl}% cross-linker", "Capsule thickness", 25.5, v, "um", "3", p, False, "Fig 6G", ptxt=ptxt, note="means read from figure; Dunnett vs uncoated")
    add("horne2023", H, "1 year", "Human cochlear implant array (mid-scala), pCBMA 10% cross-linker", "Capsule thickness, all surfaces", 47, 18, "um", "3 to 4", 0.026, True, "Fig 7I", note="means from the text; two-way ANOVA, coated vs uncoated")
    add("horne2023", H, "1 year", "Human cochlear implant array, PDMS housing", "Capsule thickness", 37, 19, "um", "3 to 4", None, False, "Fig 7I", note="read from figure; no separate p")
    add("horne2023", H, "1 year", "Human cochlear implant array, platinum electrode", "Capsule thickness", 57, 17, "um", "3 to 4", None, False, "Fig 7I", note="read from figure; no separate p")
    add("peel", "mice (BL/6)", "6 weeks", "PDMS flat sheet, CBMA 5% cross-linker", "Capsule thickness", 45, 17, "um", "5 uncoated, 3 coated (from plotted points)", 0.033, False, "Fig 3C", note="bars read from figure; text says over 60% less")
    add("peel", "mice (CBA/J)", "3 weeks", "PDMS disk, CBMA coating, explanted then tested", "Coefficient of friction after implantation", 0.27, 0.035, "dimensionless (sapphire probe, PBS)", "4 or more", None, False, "Fig 4", ptxt="not stated", note="read from figure; text: about 90% lower, no significant change from pristine")
    add("peel", "mice (CBA/J)", "3 weeks", "PDMS disk, SBMA coating, explanted then tested", "Coefficient of friction after implantation", 0.27, 0.03, "dimensionless (sapphire probe, PBS)", "4 or more", None, False, "Fig 4", ptxt="not stated", note="read from figure; text: about 90% lower, no significant change from pristine")
    ic = "Human cochlear implant arrays, two types pooled"
    add("bennion", "human cadaveric cochlea", "acute (insertion)", ic + ", SBMA coating", "Peak insertion force", 64.2, 37.0, "mN", "9 per group", 0.001, True, "Fig 4A", setting="ex vivo (human cadaver)", note="mean from the text; caption says p < 0.002, abstract p < 0.001")
    add("bennion", "human cadaveric cochlea", "acute (insertion)", ic + ", SBMA coating", "Force variation", 89.9, 52.1, "mN/s", "9 per group", 0.03, True, "Fig 4B", setting="ex vivo (human cadaver)", note="means from the text")
    add("bennion", "human cadaveric cochlea", "acute (insertion)", ic + ", SBMA coating", "Work of insertion", 285.0, 216.3, "microjoules", "9 per group", 0.05, True, "Fig 4C", setting="ex vivo (human cadaver)", note="means from the text; borderline")
    add("peel", "human cadaveric cochlea", "acute (insertion)", ic + ", SBMA coating", "Peak insertion force", 68, 35, "mN", "9 per group", 0.003, False, "Fig 13A", ptxt="< 0.003", setting="ex vivo (human cadaver)", note="read from figure; possible data overlap with Bennion 2021, do not count as an independent replication")
    add("peel", "human cadaveric cochlea", "acute (insertion)", ic + ", SBMA coating", "Work of insertion", 335, 235, "microjoules", "9 per group", 0.19, False, "Fig 13B", setting="ex vivo (human cadaver)", note="read from figure; not significant; possible data overlap with Bennion 2021")
    for day, su, sc, tu, tc, ps, pt_ in ((3, 1.75, 0.95, 1.6, 0.95, "< 0.05", "< 0.05"), (7, 1.62, 1.08, 1.4, 0.95, "< 0.05", "< 0.05"),
                                         (14, 1.35, 0.95, 1.5, 0.6, "> 0.05 (ns)", "< 0.05"), (21, 1.0, 0.68, 1.0, 0.5, "> 0.05 (ns)", "< 0.05")):
        add("shen", "rats", f"{day} days", "PDMS implant under the skin, pCBMA, S. aureus inoculated", "Bacterial load, relative radiant efficiency", su, sc, "unitless", "6 per group", None, False, "Fig 6K", ptxt=ps, note="read from figure")
        add("shen", "rats", f"{day} days", "PDMS implant through the skin, pCBMA, S. aureus inoculated", "Bacterial load, relative radiant efficiency", tu, tc, "unitless", "6 per group", None, False, "Fig 6K", ptxt=pt_, note="read from figure")
    add("shen", "rats", "21 days", "PDMS implant under the skin, pCBMA, S. aureus inoculated", "Adherent bacteria on explant", 940, 155, "counts per high-power field", "about 71 fields (t test df = 69)", None, False, "Fig 7C", ptxt="< 0.0001", note="read from figure; text: more than 500 counts per field fewer")
    add("shen", "rats", "21 days", "PDMS implant under the skin, pCBMA, S. aureus inoculated", "Viable colonies recovered from explant", 690, 35, "colonies (as plotted)", "6 implants", 0.0006, False, "Fig 7D", note="read from figure")
    add("shen", "rats", "2 weeks in vivo, then 24 h challenge in a dish", "PDMS implant under the skin, pCBMA", "Adherent S. aureus after challenge", 2520, 210, "counts per high-power field", "6 rats per group (30 fields)", None, False, "Fig 8", ptxt="< 0.0001", note="read from figure; text: more than 1000 counts per field fewer")
    sh = "sheep (Suffolk-Dorsett)"
    dev = "Advanced Bionics HiFocus SlimJ human array, CBMA coating"
    for mname, tm, (u, c), pp, pt_ in (("Total impedance", "at implantation", (30, 10.5), 0.0001, "< 0.0001"), ("Total impedance", "4 weeks", (17.5, 9.5), 0.0007, "0.0007"),
                                       ("Polarization impedance", "at implantation", (20, 6), 0.0001, "< 0.0001"), ("Polarization impedance", "4 weeks", (9.5, 6), 0.2586, "0.2586 (ns)"),
                                       ("Access resistance", "at implantation", (12.5, 6), 0.0019, "0.0019"), ("Access resistance", "4 weeks", (11, 5), 0.0084, "0.0084")):
        add("benshlomo", sh, tm, dev, mname, u, c, "kOhm", "3 sheep, 3 arrays per group (per-electrode n not stated)", pp if "<" not in pt_ else None, False, "Fig 3B to 3D", ptxt=pt_, note="read from figure; p as printed (2-way ANOVA, Sidak)")
    for mname, (u, c), pp, unit in (("Cell nuclei density, round window", (19, 4.5), 0.0020, "per 10^5 um3"), ("Macrophage density, round window", (9.8, 2.6), 0.0063, "per 10^5 um3"),
                                    ("Fibrosis, round window", (16.5, 2.5), 0.0101, "% of scala tympani volume")):
        add("benshlomo", sh, "4 weeks", dev, mname, u, c, unit, "3 sheep, pooled", pp, False, "Fig 6E to 6G", note="pooled bars read from figure; sheep 2 showed no benefit for nuclei and macrophages")
    for mname, (u, c), unit in (("Cell nuclei density, basal turn", (29, 19), "per 10^5 um3"), ("Macrophage density, basal turn", (17.5, 11), "per 10^5 um3"),
                                ("Fibrosis, basal turn", (27, 6), "% of scala tympani volume")):
        add("benshlomo", sh, "4 weeks", dev, mname, u, c, unit, "3 sheep, pooled", None, False, "Fig 5E to 5G", ptxt="not significant", note="pooled bars read from figure; significant only in sheep 1")
    add("benshlomo", sh, "4 weeks", dev, "New bone (neoossification) volume", 12.24e-3, 0.795e-3, "mm3", "3 sheep per group (inferred)", None, True, "Section 3.3 (text)", ptxt="not significant", note="means from the text; underpowered pilot")
    for dev_, c_ in (("single network, 2.5% cross-linker", 57), ("dual network, 2.5% primary and 2.5% secondary cross-linker", 38), ("single network, 20% cross-linker", 36), ("dual network, 20% primary and 20% secondary cross-linker", 58)):
        add("barrera", "rats (Sprague-Dawley)", "6 weeks", f"PDMS flat disk under the skin, SBMA {dev_}", "Capsule thickness", 210, c_, "um", "6 per condition", None, False, "Fig 7F", ptxt="< 0.0001",
            note="means read from the plot (uncoated about 210 um); one-way ANOVA, coated vs uncoated; text states about 75 percent reduction for the lower cross-link groups and a capsule under one third of uncoated; no significant difference between single and dual networks")
    # Human cadaveric ETT intubation (ZwiCoat internal study, 2026) and the synthetic cochlea (NIH SBIR Phase I), both computed by build_sbir.py from the raw files.
    ett = json.load(open(os.path.join(DATA, "W38_traces.json"), encoding="utf-8"))["summary"]
    for surg in ("Surgeon 1", "Surgeon 2"):
        q = ett["per_surgeon"][surg]
        add("zwicoat_ett", "human cadaveric larynx", "acute (intubation)", f"Endotracheal tube (PVC), coated versus uncoated, {surg}", "Intubation impulse (integrated insertion force)",
            round(q["uncoated_mean_Ns"], 2), round(q["coated_mean_of_tube_means_Ns"], 2), "N·s", f"{q['n_uncoated']} uncoated, {q['n_coated']} coated intubations (1 uncoated and {q['n_coated_tubes']} coated tubes)",
            None, True, "W38", ptxt="< 0.001 (both surgeons pooled, tube-level mixed model)", setting="ex vivo (human cadaver)",
            note=f"coated value is the mean of the {q['n_coated_tubes']} tube means; {q['reduction_pct']:.0f} percent lower")
    ci = w37_summary()
    sb = "Cochlear implant electrode array, EtO-sterilized coated array versus uncoated array, robotic insertion at constant speed"
    nn = f"{ci['n_uncoated']} uncoated, {ci['n_coated']} coated insertions"
    add("sbir", "synthetic cochlea", "acute (insertion)", sb, "Peak insertion force", round(ci["peak_uncoated_mean"], 1), round(ci["peak_coated_mean"], 1), "mN", nn,
        round(ci["p_peak_welch"], 6), True, "W37B", ptxt="< 0.001 (Welch t-test)", setting="bench (synthetic cochlea)", note="repeated insertions of one coated and one uncoated array")
    add("sbir", "synthetic cochlea", "acute (insertion)", sb, "Work of insertion", round(ci["work_uncoated_mean"], 1), round(ci["work_coated_mean"], 1), "mN·mm", nn,
        round(ci["p_welch"], 6), True, "W37C", ptxt="< 0.001 (Welch t-test)", setting="bench (synthetic cochlea)", note="work integrated over each full trace; repeated insertions of one coated and one uncoated array")
    for r in rows:
        if isinstance(r.get("note"), str):
            r["note"] = re.sub(r"^\s*text:\s*", "", r["note"])
    json.dump(rows, open(os.path.join(DATA, "W32_invivo_studies.json"), "w"), indent=1)
    print("wrote W32_invivo_studies.json,", len(rows), "rows")


# ---------------------------------------------------------------- W34 PEEK bond strength
def w34_peek_bond(ls):
    # PEEK: archive groups from Lap-shear Master.xlsx (2026 sheet), read via load_lapshear(). The dry group (635 kPa, n = 5) is flagged
    # "Untrustworthy?" in the master (2 of 5 pulls reached the 100 N load cell limit, so the mean is a lower bound) and is therefore not in W02;
    # it is used here deliberately and labelled "at least". Excluded: the two low-bond groups with no recorded recipe, and the "Cranioplasty material" row.
    peek = [r for r in ls if r["sub"] == "PEEK" and r["avg"] is not None and r["n_s"] and "KLS" in str(r.get("Substrate"))]
    dry = [r for r in peek if "dry" in str(r.get("Name")).lower()][0]
    soak = [r for r in peek if "soak" in str(r.get("Name")).lower()][0]
    assert abs(dry["avg"] - 635.2) < 1 and abs(soak["avg"] - 129.0) < 1
    # Short-soak silicone and PVC (soak of 15 min or less, 2025 to 2026, company groups with a recorded n): computed from the archive.
    def short(sub):
        return [r for r in ls if r["sub"] == sub and r["company"] and not r["untrust"] and r["avg"] is not None and r["n_s"]
                and r["sheet"] in ("2025", "2026") and num(r.get("Soak time (h)")) is not None and num(r.get("Soak time (h)")) <= 0.25]
    sil_soak, pvc_soak = short("Silicone (PDMS)"), short("PVC")
    sil_soak_med = median([r["avg"] for r in sil_soak]); pvc_soak_med = median([r["avg"] for r in pvc_soak])
    # Dry comparators: the archive does not label dry reliably (most rows carry no soak field and mix pretreatment screens and formulation sweeps),
    # so the medians from the project inventory (cranioplasty-peek-2026.md, section 6) are used: PVC 349 (7 groups, 36 tests), silicone 131 (11 groups).
    SIL_DRY, PVC_DRY = 131, 349
    print("W34 PEEK dry", round(dry["avg"], 1), "n", dry["n_s"], "| soaked", round(soak["avg"], 1), "n", soak["n_s"],
          "| silicone short soak median", round(sil_soak_med, 1), len(sil_soak), "groups", int(sum(r["n_s"] for r in sil_soak)), "tests",
          "| PVC short soak", round(pvc_soak_med, 1), len(pvc_soak), "group(s)", int(sum(r["n_s"] for r in pvc_soak)), "tests")
    fig, (axA, axB) = plt.subplots(1, 2, figsize=(11.5, 5.8))

    def panel(ax, vals, sub, head):
        ymax = 900
        for i, (lab, v, col, lbl) in enumerate(vals):
            ax.bar(i, v, width=0.6, color=col, edgecolor=SURFACE, linewidth=2)
            ax.text(i, v + ymax * 0.015, lbl, ha="center", va="bottom", fontsize=11.5, color=INK, fontweight="bold" if col == BLUE else "normal")
        ax.set_xticks(range(len(vals))); ax.set_xticklabels([v[0] for v in vals], fontsize=10.5)
        ax.set_ylim(0, ymax); ax.set_xlim(-0.6, len(vals) - 0.4); ax.grid(axis="x", visible=False)
        ax.set_ylabel("Lap-shear bond strength (kPa)"); ptitle(ax, head)
        if sub:
            ax.text(0.5, -0.12, sub, transform=ax.transAxes, ha="center", va="top", fontsize=9.3, color=MUTED, linespacing=1.4)
    panel(axA, [("PEEK", dry["avg"], BLUE, "at least ~635"), ("Silicone", SIL_DRY, GRAY_LIGHT, f"~{SIL_DRY}"), ("PVC", PVC_DRY, GRAY_LIGHT, f"~{PVC_DRY}")],
          None, "A. As prepared (dry)")
    panel(axB, [("PEEK", soak["avg"], BLUE, "~129"), ("Silicone", sil_soak_med, GRAY_LIGHT, f"~{sil_soak_med:.0f}"), ("PVC", pvc_soak_med, GRAY_LIGHT, f"~{pvc_soak_med:.0f}")],
          None, "B. After a short water soak")
    # One short annotation, on the dry PEEK bar only (Kam, 2026-11-02).
    axA.annotate("gel tears before\nthe bond lets go", xy=(0.31, dry["avg"] * 0.85), xytext=(1.1, 720), fontsize=10, color=BLUE, ha="center", va="center",
                 linespacing=1.35, arrowprops=dict(arrowstyle="-", color=BLUE, lw=1.2, shrinkA=2, shrinkB=2))
    ftitle(fig, "The coating grafts directly to PEEK, with no primer",
           "Lap-shear bond strength on PEEK, silicone and PVC; group means; ZwiCoat internal tests, 2025 to 2026")
    fig.subplots_adjust(wspace=0.28)
    save(fig, "W34_peek_bond_strength", "Bond strength of the coating on PEEK is among the highest we measure. PEEK takes part in the grafting step, so no primer is needed, and the gel tears before the bond lets go.",
         "ZwiCoat internal tests, 2025 to 2026",
         source_short="ZwiCoat internal tests, 2025 to 2026")


# ---------------------------------------------------------------- W35 wear (Peel 2024 Fig 9)
def w35_wear():
    # Peel 2024 Fig 9, approximate pixel readings: friction relative to bare silicone, first 100 vs last 100 of 2,500 passes. n at least 4.
    groups = [("2 to 5%", 0.068, 0.068), ("13%", 0.068, 0.068), ("31%", 0.103, 0.103), ("50%", 0.23, 0.19), ("67%", 0.255, 0.255)]
    fig, ax = plt.subplots(figsize=(10, 5.6))
    for i, (lab, f, l) in enumerate(groups):
        ax.bar(i - 0.2, f, width=0.36, color=BLUE, edgecolor=SURFACE, linewidth=2, label="First 100 passes" if i == 0 else None)
        ax.bar(i + 0.2, l, width=0.36, color=BLUE_RAMP[4], edgecolor=SURFACE, linewidth=2, label="Last 100 of 2,500 passes" if i == 0 else None)
        ax.text(i - 0.2, f + 0.015, f"{f:.3g}".lstrip("0"), ha="center", fontsize=9.5, color=INK2)
        ax.text(i + 0.2, l + 0.015, f"{l:.3g}".lstrip("0"), ha="center", fontsize=9.5, color=INK2)
    ax.axhline(1.0, color=INK2, lw=1.2, ls=(0, (5, 4)))
    ax.text(4.55, 1.025, "Bare silicone = 1.0", ha="right", va="bottom", fontsize=10, color=INK2)
    ax.set_xticks(range(len(groups))); ax.set_xticklabels([g[0] for g in groups], fontsize=10.5)
    ax.set_xlabel("Crosslinker in the coating (percent)"); ax.set_ylabel("Friction relative to bare silicone")
    ax.set_ylim(0, 1.12); ax.set_xlim(-0.6, 4.6); ax.grid(axis="x", visible=False); ax.legend(loc="center right", bbox_to_anchor=(1.0, 0.7))
    title(ax, "Still slippery after 2,500 passes", "Friction relative to bare silicone, first and last 100 passes of a 2,500-pass wear test; Peel et al. 2024")
    save(fig, "W35_wear_2500_passes", "Coated silicone, rubbed under a 1 N load in saline for about 17 hours. Friction in the last 100 passes matched the first 100 and stayed at about 7 percent of bare silicone for the 2 to 13 percent crosslinker coatings.",
         "Peel A, et al. ACS Applied Bio Materials 2024;7:3124-3135, Fig 9 (n at least 4)",
         source_short="Peel et al. 2024, ACS Applied Bio Materials, Fig 9")


# ---------------------------------------------------------------- W36 dry-out and re-wet (Peel 2024)
def w36_dry_rewet():
    # Peel 2024 Fig 7 (minutes to first crack, bent every 5 min on a 5 mm rod while drying, 5% crosslinker; A 75, B 47.5; n at least 3) and
    # Fig 8 (friction never dried vs dried 24 h and re-wet 24 h; bare silicone 0.179 from the caption; n at least 4). Values approximate.
    fig, (axA, axB) = plt.subplots(1, 2, figsize=(11.5, 5.6), gridspec_kw={"width_ratios": [0.8, 1.6]})
    for i, (lab, v, col) in enumerate([("Coating A", 75, BLUE), ("Coating B", 47.5, BLUE_RAMP[4])]):
        axA.bar(i, v, width=0.55, color=col, edgecolor=SURFACE, linewidth=2)
        axA.text(i, v + 1.5, f"{v:g}", ha="center", fontsize=12, color=INK, fontweight="bold")
    axA.set_xticks([0, 1]); axA.set_xticklabels(["Coating A", "Coating B"], fontsize=10.5); axA.set_xlim(-0.6, 1.6); axA.set_ylim(0, 95)
    axA.set_ylabel("Minutes to first crack"); axA.grid(axis="x", visible=False)
    ptitle(axA, "A. Drying while bent")
    axA.set_xlabel("5% crosslinker, bent every 5 minutes")
    levels = ["2 to 5%", "13%", "20%", "31%"]; never = [0.026, 0.031, 0.033, 0.034]; rewet = [0.026, 0.031, 0.033, 0.058]
    axB.bar(0, 0.179, width=0.55, color=GRAY, edgecolor=SURFACE, linewidth=2)
    axB.text(0, 0.179 + 0.004, ".179", ha="center", fontsize=10, color=INK2)
    for i, (n_, r_) in enumerate(zip(never, rewet)):
        x = i + 1.6
        axB.bar(x - 0.19, n_, width=0.34, color="#A9D2EE", edgecolor=SURFACE, linewidth=2, label="Never dried" if i == 0 else None)
        axB.bar(x + 0.19, r_, width=0.34, color=BLUE, edgecolor=SURFACE, linewidth=2, label="Dried 24 h, re-wet 24 h" if i == 0 else None)
        axB.text(x - 0.19, n_ + 0.004, f"{n_:.3f}".lstrip("0"), ha="center", fontsize=9, color=INK2)
        axB.text(x + 0.19, r_ + 0.004, f"{r_:.3f}".lstrip("0"), ha="center", fontsize=9, color=INK2)
    axB.set_xticks([0] + [i + 1.6 for i in range(4)]); axB.set_xticklabels(["Bare\nsilicone"] + levels, fontsize=10.5)
    axB.set_xlim(-0.6, 5.3); axB.set_ylim(0, 0.22); axB.set_ylabel("Friction coefficient"); axB.grid(axis="x", visible=False)
    axB.set_xlabel("Crosslinker in the coating (percent)"); axB.legend(loc="upper right", bbox_to_anchor=(1.0, 0.92))
    ptitle(axB, "B. Friction after drying and re-wetting")
    ftitle(fig, "Dry it out, re-wet it, and it is as slippery as new", "Peel et al. 2024")
    save(fig, "W36_dry_and_rewet", "Coated silicone dried for 24 hours and re-wet for 24 hours returned to its original friction. Coatings dried while being bent every 5 minutes lasted 47 to 75 minutes before the first crack.",
         "Peel A, et al. ACS Applied Bio Materials 2024;7:3124-3135, Figs 7, 8 and 9 (Fig 7 n at least 3, Fig 8 n at least 4)",
         source_short="Peel et al. 2024, ACS Applied Bio Materials, Figs 7, 8 and 9")


# ---------------------------------------------------------------- W39 bond on silicone, then and now (gate check only)
W39_NOTE = []


def _quartiles(v):
    v = sorted(v); n = len(v)

    def q(p):
        k = (n - 1) * p; f = int(k); c = min(f + 1, n - 1)
        return v[f] + (v[c] - v[f]) * (k - f)
    return q(0.25), q(0.5), q(0.75)


def w39_bond_check(ls):
    """Owner request (2026-11-02): chart 2025 to 2026 'as prepared' and 'swelled in PBS' silicone groups against Leigh 2019 (about 71 to 100 kPa),
    but only if both center near 200 kPa. The archive has no as-prepared or swelled label for 2025 to 2026 (those words occur only on the
    2017 dissertation rows), so the soak fields define the groups. No formulation fields are read or written."""
    sil = [r for r in ls if r["sub"] in ("Silicone (PDMS)", "Implant silicone") and r["sheet"] in ("2025", "2026") and r["avg"] is not None
           and not r["untrust"] and r["n_s"] != 0]

    def cond(r):
        txt = " ".join(str(r.get(k) or "") for k in ("Name", "campaign", "condition", "Notes")).lower()
        name = str(r.get("Name") or "").lower()
        h = num(r.get("Soak time (h)")); solv = str(r.get("soaking solvent") or "")
        # left out: the ionogel liquid-phase series, dried-and-rehydrated groups, and the packaged sterilization and shipping arms (Gamma, E-beam, EO, shipping)
        if "ionogel" in txt or "rehydrated" in name or re.search(r"gamma|e ?beam|shipping|eo steril", name):
            return None
        if h is None or h <= 0.25 or "never dried" in txt:
            return "As prepared (no soak, or 15 min or less)"
        if "PBS" in solv and h >= 24:
            return "Swelled in PBS (24 h or more)"
        return None
    groups = collections.defaultdict(list)
    for r in sil:
        c = cond(r)
        if c:
            groups[(c, r["sheet"])].append(r); groups[(c, "2025 to 2026")].append(r)
    out = {}
    for k in sorted(groups):
        v = [r["avg"] for r in groups[k]]
        q1, md, q3 = _quartiles(v)
        out[k] = dict(median=md, q1=q1, q3=q3, groups=len(v), tests=int(sum(r["n_s"] or 0 for r in groups[k])))
        print("W39 check:", k, {a: (round(b, 1) if isinstance(b, float) else b) for a, b in out[k].items()})
    near = all(150 <= out[(c, "2025 to 2026")]["median"] <= 250 for c in ("As prepared (no soak, or 15 min or less)", "Swelled in PBS (24 h or more)"))
    a, s = out[("As prepared (no soak, or 15 min or less)", "2025 to 2026")], out[("Swelled in PBS (24 h or more)", "2025 to 2026")]
    W39_NOTE.append(
        f"Build note, W39 (bond on silicone, then and now): {'built' if near else 'NOT built'}. Silicone groups (Silicone (PDMS) and Implant silicone, 2025 and 2026 sheets, "
        f"untrustworthy rows excluded; sterilization, dry-rehydrate and ionogel series left out): as prepared (no soak recorded, or 15 min or less) median {a['median']:.0f} kPa, "
        f"IQR {a['q1']:.0f} to {a['q3']:.0f}, {a['groups']} groups, {a['tests']} tests with a recorded n; swelled in PBS for 24 h or more median {s['median']:.0f} kPa, "
        f"IQR {s['q1']:.0f} to {s['q3']:.0f}, {s['groups']} groups, {s['tests']} tests. Leigh 2019 Fig 6 plateau (5 to 50 mg/mL grafting agent): as prepared about 61 to 74 kPa (SBMA) and 71 to 100 kPa (CBMA), "
        "swollen about 35 to 62. " + ("Both conditions center near 200 kPa; the chart still needs to be drawn." if near else
                                       "Neither 2025 to 2026 condition centers near 200 kPa, so the chart is not drawn."))
    W39_NOTE.append(bentec_note(ls))
    return near


def bentec_note(ls):
    """Owner belief (2026-11-02): 'we routinely get about 200 kPa on Bentec' (Bentec = the silicone in Leigh 2019 Fig 6). Check against the
    lap-shear master: every trusted row whose Substrate string names Bentec ('Bentec', 'Bentec (no BP)', and 'not recorded (Sylgard/Bentec era)'),
    grouped by sheet year. No formulation fields are read or written. Site wording this supports: 'Bentec silicone: median about 100 kPa,
    best groups 150 to 195 kPa (2024 to 2026)'."""
    ben = [r for r in ls if "bentec" in str(r.get("Substrate") or "").lower() and r["avg"] is not None and not r["untrust"]]

    def st(rows):
        v = [r["avg"] for r in rows]; q1, md, q3 = _quartiles(v)
        return f"median {md:.0f} kPa (IQR {q1:.0f} to {q3:.0f}, max {max(v):.0f}, {len(v)} groups, {sum(1 for x in v if x >= 150)} at or above 150)"
    years = [y for y in ("2024", "2025", "2026", "Undated") if any(r["sheet"] == y for r in ben)]
    per = "; ".join(f"{y}: {st([r for r in ben if r['sheet'] == y])}" for y in years)
    amb = [r for r in ben if not str(r.get("Substrate") or "").lower().startswith("bentec")]
    strict = [r for r in ben if str(r.get("Substrate") or "").lower().startswith("bentec")]
    top = sorted(ben, key=lambda r: -r["avg"])[0]
    note = (f"Build note, Bentec bond strength (no chart): all trusted Bentec groups in the lap-shear master, {st(ben)}. By sheet: {per}. "
            f"The Undated sheet rows are one soak-time campaign with no date recorded. {len(amb)} rows are labelled 'not recorded (Sylgard/Bentec era)'; "
            f"Bentec-only rows give {st(strict)}. The top group ({top['avg']:.0f} kPa, {top['sheet']}) is a surface-roughness group (60 grit). "
            "So about 200 kPa is the best case, not the routine result; site wording: 'Bentec silicone: median about 100 kPa, best groups 150 to 195 kPa (2024 to 2026)'. "
            "Leigh 2019 Fig 6 plateau for comparison: about 61 to 74 kPa as prepared (SBMA).")
    print(note)
    return note


def main():
    exps = load_experiments(); ls = load_lapshear(); ci = load_ci(); ag = load_aging(); ev = load_evidence()
    w01_timeline(exps); w02_lapshear(ls); w03_ci(ci); w04_fibrosis(); w05_antifouling(); w06_durability(); w07_insertion(); w08_impedance()
    w09_aging(ag); w10_substrate_matrix(ls); w11_sterilization(); w12_numbers(); w33_archive_numbers(ls, ci, exps); w13_claims(ev); w14_w_sweep(ls); w15_thickness(); w16_ett_trials()
    w17_textured(); w18_catheter(); w19_ett_forest(); w20_cgm_delay(); w21_mucus_flow()
    w24_timeline(); w25_sheep_impedance(); w26_sheep_histology(); w27_capsule_mice(); w28_durability_peel(); w29_bacteria_rats()
    w30_crosslinker(); w31_bond_strength(); w32_invivo_studies(); w34_peek_bond(ls); w35_wear(); w36_dry_rewet()
    w39_bond_check(ls)
    md = ["# Figure manifest (built by figures/build_figures.py)", ""] + manifest_rows(MANIFEST)
    md += ["", "Build note, W34: PEEK bars are archive groups (Lap-shear Master.xlsx, 2026 sheet: dry 635 kPa, n = 5, a lower bound because 2 pulls reached the load-cell limit; 10 min water soak 129 kPa, n = 7; all cohesive failures). "
           "The dry group is flagged untrustworthy in the master and is deliberately absent from W02. Short-soak silicone (84 kPa, median of 7 groups, 37 tests, soak 15 min or less) and PVC (419 kPa, 1 group, n = 5, 15 min) are computed from the archive. "
           "The archive does not label dry reliably, so the dry silicone (131) and PVC (349) medians come from the project inventory (figures/published/cranioplasty-peek-2026.md, section 6)."]
    md += [""] + W39_NOTE
    md += ["", "PNG at 2x in png/, SVG in svg/, data for interactive versions in data/. Font: Arial everywhere."]
    open(os.path.join(HERE, "MANIFEST.md"), "w", encoding="utf-8").write("\n".join(md) + "\n")


if __name__ == "__main__":
    main()

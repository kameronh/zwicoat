"""SBIR Phase I charts (W37, W38) for the v2 site, built from raw data.

Uses the style block of build_figures.py (Arial, palette, title helpers, save()).
Outputs PNG (2x) and SVG into figures/png and figures/svg, trace JSON for the
interactive versions into figures/data, and figures/MANIFEST-sbir.md.
    python figures/build_sbir.py

Sources (read-only):
  ZEN : the public Zenodo record of the NIH SBIR Phase I dataset
        (ZwiCoat Materials Innovations, SBIR Phase 1 Dataset,
        doi:10.5281/zenodo.10459478; grant 1R43DC022208-01), local copy.
  ETTW: the 2026 ETT force-of-insertion workup. Its 60 raw CSVs are
        byte-identical to the ones in the Zenodo record; the workup adds the
        revised, unsmoothed intubation-detection script ported below.
Every number is computed here from the raw files.
"""
import glob
import json
import os
import sys

import numpy as np
import pandas as pd
from scipy import optimize, stats

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import build_figures as bf  # noqa: E402  (style block only; main() is guarded)
from build_figures import (BLUE, GRAY, GRAY_LIGHT, INK, INK2, MUTED, SURFACE, DATA,  # noqa: E402
                           title, ftitle, ptitle, bracket, save, plt)

ZEN = r"G:\My Drive\9 Zwitterion\SBIR Phase 1 Dataset\26.04 Zenodo repo"
ETTW = r"G:\My Drive\9 Zwitterion\IA Data n Workups\26.06 ETT paper\data\ETT force of insertion"
ZENODO = "ZwiCoat Materials Innovations, SBIR Phase 1 Dataset, Zenodo, doi:10.5281/zenodo.10459478 (NIH SBIR grant 1R43DC022208-01, CC BY 4.0)"
BLUE_LIGHT = "#A9D2EE"


def mround(x):
    """MATLAB round (half away from zero)."""
    return int(np.floor(abs(x) + 0.5) * np.sign(x))


def fwd_window(x, w, fn):
    """MATLAB mov*(x, [0 w]): window x(i:i+w), truncated at the end. fn is 'mean' or 'std' (ddof 1)."""
    n = len(x)
    out = np.empty(n)
    m = max(0, n - w)
    if m:
        win = np.lib.stride_tricks.sliding_window_view(x, w + 1)
        out[:m] = win.mean(1) if fn == "mean" else win.std(1, ddof=1)
    for i in range(m, n):
        v = x[i:]
        out[i] = v.mean() if fn == "mean" else (v.std(ddof=1) if len(v) > 1 else 0.0)
    return out


def fwd_sum(x, w):
    c = np.concatenate([[0.0], np.cumsum(x, dtype=float)])
    idx = np.arange(len(x))
    return c[np.minimum(len(x), idx + w + 1)] - c[idx]


def mad_sd(v):
    return 1.4826 * np.median(np.abs(v - np.median(v)))


# ================================================================ CI insertion (Zenodo: CI force of insertion)
CI_DIR = os.path.join(ZEN, "CI force of insertion")
MM_PER_SAMPLE = 0.2 / 50   # plot_data.m: "depth (mm) = counts x 0.2 / 50"; column 1 is the sample index (50 samples/s)


def load_ci():
    """Replicates plot_data.m exactly: alphabetical file order, the two manual trims
    (files 7 and 8 = UNCoated SS t2 and t3), depth = column 1 x 0.2/50, work = trapz."""
    files = sorted(glob.glob(os.path.join(CI_DIR, "*.xlsx")), key=lambda p: os.path.basename(p))
    trials = []
    for idx, f in enumerate(files, 1):
        d = pd.read_excel(f, sheet_name=0)
        x = d.iloc[:, 0].to_numpy(float); y = d.iloc[:, 1].to_numpy(float)   # Sample Number, Tracking Value (mN)
        if idx == 7:
            x = x[999:-500]; y = y[999:-500]; x = x - x[0]
        if idx == 8:
            x = x[:-300]; y = y[:-300]; x = x - x[0]
        z = x * MM_PER_SAMPLE
        name = os.path.basename(f)
        coated = name.lower().startswith("coated")
        trials.append(dict(file=name, group="coated" if coated else "uncoated", depth=z, force=y,
                           work=float(np.trapz(y, z)), peak=float(y.max()), end_depth=float(z[-1])))
    return trials


def ci_stats(trials):
    c = np.array([t["work"] for t in trials if t["group"] == "coated"])
    u = np.array([t["work"] for t in trials if t["group"] == "uncoated"])
    pc = np.array([t["peak"] for t in trials if t["group"] == "coated"])
    pu = np.array([t["peak"] for t in trials if t["group"] == "uncoated"])
    # sensitivity: work over the depth every trace reaches (0 to 14 mm)
    w14 = {g: np.array([np.trapz(t["force"][t["depth"] <= 14.0], t["depth"][t["depth"] <= 14.0]) for t in trials if t["group"] == g])
           for g in ("coated", "uncoated")}
    s = dict(n_coated=len(c), n_uncoated=len(u),
             work_coated_mean=c.mean(), work_coated_sd=c.std(ddof=1), work_uncoated_mean=u.mean(), work_uncoated_sd=u.std(ddof=1),
             work_reduction_pct=100 * (1 - c.mean() / u.mean()),
             p_welch=stats.ttest_ind(c, u, equal_var=False).pvalue, p_student=stats.ttest_ind(c, u).pvalue,
             p_mannwhitney=stats.mannwhitneyu(c, u).pvalue,
             peak_coated_mean=pc.mean(), peak_coated_sd=pc.std(ddof=1), peak_uncoated_mean=pu.mean(), peak_uncoated_sd=pu.std(ddof=1),
             p_peak_mannwhitney=stats.mannwhitneyu(pc, pu).pvalue, p_peak_student=stats.ttest_ind(pc, pu).pvalue, peak_reduction_pct=100 * (1 - pc.mean() / pu.mean()),
             p_peak_welch=stats.ttest_ind(pc, pu, equal_var=False).pvalue,
             end_depth_coated=[round(t["end_depth"], 2) for t in trials if t["group"] == "coated"],
             end_depth_uncoated=[round(t["end_depth"], 2) for t in trials if t["group"] == "uncoated"],
             work_0_14mm_coated_mean=w14["coated"].mean(), work_0_14mm_uncoated_mean=w14["uncoated"].mean(),
             work_0_14mm_reduction_pct=100 * (1 - w14["coated"].mean() / w14["uncoated"].mean()),
             p_0_14mm_welch=stats.ttest_ind(w14["coated"], w14["uncoated"], equal_var=False).pvalue)
    p14 = {g: np.array([t["force"][t["depth"] <= 14.0].max() for t in trials if t["group"] == g]) for g in ("coated", "uncoated")}
    s.update(peak_0_14mm_coated_mean=p14["coated"].mean(), peak_0_14mm_uncoated_mean=p14["uncoated"].mean(),
             peak_0_14mm_reduction_pct=100 * (1 - p14["coated"].mean() / p14["uncoated"].mean()),
             p_peak_0_14mm_welch=stats.ttest_ind(p14["coated"], p14["uncoated"], equal_var=False).pvalue)
    return s


def binned(z, y, k=10):
    """Display only: mean of every k samples (k = 10 -> 0.04 mm bins)."""
    m = len(y) // k
    return z[:m * k].reshape(m, k).mean(1), y[:m * k].reshape(m, k).mean(1)


def _w37_bars(ax, trials, key, red, p, ylabel, ymax, fmt, pad):
    rng = np.random.default_rng(3)
    for i, g in enumerate(("uncoated", "coated")):
        v = np.array([t[key] for t in trials if t["group"] == g])
        col, light = (GRAY, GRAY_LIGHT) if g == "uncoated" else (BLUE, BLUE_LIGHT)
        ax.bar(i, v.mean(), width=0.58, color=light, edgecolor=SURFACE, linewidth=2, zorder=1)
        ax.scatter(i + rng.uniform(-0.14, 0.14, len(v)), v, s=40, color=col, edgecolor=SURFACE, linewidth=1, zorder=3)
        ax.text(i, v.mean() / 2, fmt.format(v.mean()), ha="center", va="center", fontsize=12, color=INK, fontweight="bold", zorder=4)
    top = max(t[key] for t in trials)
    bracket(ax, 0, 1, top + pad, f"−{red:.0f}%, {'p < 0.001' if p < 0.001 else f'p = {p:.3f}'}", pad / 3)
    n_u = sum(t["group"] == "uncoated" for t in trials); n_c = sum(t["group"] == "coated" for t in trials)
    ax.set_xticks([0, 1]); ax.set_xticklabels([f"Uncoated\n(n = {n_u})", f"Coated\n(n = {n_c})"])
    ax.set_xlim(-0.6, 1.6); ax.set_ylim(0, ymax); ax.grid(axis="x", visible=False)
    ax.set_ylabel(ylabel)


def w37_ci(trials, s):
    fig, (axA, axB, axC) = plt.subplots(1, 3, figsize=(15.5, 5.9), gridspec_kw={"width_ratios": [1.75, 1, 1]})
    for t in sorted(trials, key=lambda t: t["group"] == "coated"):
        zb, yb = binned(t["depth"], t["force"])
        col = BLUE if t["group"] == "coated" else GRAY
        axA.plot(zb, yb, color=col, lw=1.3, alpha=0.9, zorder=3 if t["group"] == "coated" else 2)
    axA.plot([], [], color=GRAY, lw=2.2, label=f"Uncoated ({s['n_uncoated']} insertions)")
    axA.plot([], [], color=BLUE, lw=2.2, label=f"Coated ({s['n_coated']} insertions)")
    axA.legend(loc="upper left")
    axA.set_xlim(0, 24); axA.set_ylim(-2, 66)
    axA.set_xlabel("Insertion depth (mm)"); axA.set_ylabel("Insertion force (mN)")
    ptitle(axA, "A. Force along the insertion, every trial")
    _w37_bars(axB, trials, "peak", s["peak_reduction_pct"], s["p_peak_welch"], "Peak insertion force (mN)", 78, "{:.0f}", 6)
    ptitle(axB, "B. Peak insertion force")
    _w37_bars(axC, trials, "work", s["work_reduction_pct"], s["p_welch"], "Work of insertion (mN·mm)", 430, "{:.0f}", 30)
    ptitle(axC, "C. Work of insertion")
    fig.subplots_adjust(wspace=0.34)
    ftitle(fig, "Coated cochlear implants slide into a synthetic cochlea with about two thirds less force",
           f"Robotic insertion into a synthetic cochlea model, n = {s['n_coated']} coated and {s['n_uncoated']} uncoated insertions; "
           "EtO-sterilized coated array\nPeak force and work from the same insertions; bars = mean, dots = single insertions; NIH SBIR Phase I dataset (Zenodo)", nsub=2)
    save(fig, "W37_ci_insertion_synthetic",
         f"A robot inserted a cochlear implant electrode array into a synthetic cochlea at constant speed. The EtO-sterilized coated array reached a "
         f"{s['peak_reduction_pct']:.0f} percent lower peak insertion force than the uncoated array (mean {s['peak_coated_mean']:.1f} versus "
         f"{s['peak_uncoated_mean']:.1f} mN, p < 0.001) and needed {s['work_reduction_pct']:.0f} percent less work of insertion "
         f"({s['work_coated_mean']:.0f} versus {s['work_uncoated_mean']:.0f} mN·mm, p < 0.001), measured on the same insertions.",
         f"{ZENODO}, folder 'CI force of insertion': the 11 trial files 'Coated SS#4 3.xlsx', 'Coated SS#4 t2/t4/t5/t6.xlsx' (coated, n = 5) and "
         "'UNCoated SS t1 to t6.xlsx' (uncoated, n = 6), first sheet, columns Sample Number and Tracking Value (mN, 50 samples/s); analysis replicates "
         "the record's plot_data.m (depth = column 1 x 0.2/50 mm, manual trims of t2 and t3, work = trapezoidal area under force versus depth). "
         f"Peak force = maximum raw force per trial: coated {s['peak_coated_mean']:.1f} ± {s['peak_coated_sd']:.1f}, uncoated {s['peak_uncoated_mean']:.1f} ± "
         f"{s['peak_uncoated_sd']:.1f} mN, Welch t-test p = {s['p_peak_welch']:.1e} (Mann-Whitney p = {s['p_peak_mannwhitney']:.4f}). "
         f"Work: coated {s['work_coated_mean']:.1f} ± {s['work_coated_sd']:.1f}, uncoated {s['work_uncoated_mean']:.1f} ± {s['work_uncoated_sd']:.1f} mN·mm "
         f"(mean ± SD); Welch t-test p = {s['p_welch']:.1e} (Student p = {s['p_student']:.1e}, Mann-Whitney p = {s['p_mannwhitney']:.4f}). "
         "EtO sterilization (Andersen Scientific, 50 C, 16 h) and the iotaSoft insertion robot are stated in the SBIR Phase I close-out and the Phase II research "
         "plans, not in the Zenodo README. The coated trials are repeated insertions of one coated array (SS#4), the uncoated trials of one uncoated array. "
         "Traces in panel A are 0.04 mm bin means for display; all numbers use the raw samples. Trace data: figures/data/W37_traces.json",
         source_short="NIH SBIR Phase I dataset, Zenodo, doi:10.5281/zenodo.10459478")


def w37_json(trials, s):
    out = {"chart": "W37_ci_insertion_synthetic", "units": {"depth": "mm", "force": "mN", "work": "mN*mm"},
           "source": ZENODO + ", folder 'CI force of insertion'",
           "method": "plot_data.m replicated: depth = sample index x 0.2/50 mm (50 samples/s at 0.2 mm/s), trims on UNCoated SS t2 and t3, work = trapz(force, depth) on raw samples; traces here are 0.04 mm bin means",
           "summary": {k: (round(v, 6) if isinstance(v, float) else v) for k, v in s.items()},
           "trials": []}
    for t in trials:
        zb, yb = binned(t["depth"], t["force"])
        out["trials"].append({"file": t["file"], "group": t["group"], "work_mN_mm": round(t["work"], 2), "peak_mN": round(t["peak"], 2),
                              "depth_mm": [round(float(v), 3) for v in zb], "force_mN": [round(float(v), 2) for v in yb]})
    json.dump(out, open(os.path.join(DATA, "W37_traces.json"), "w"), separators=(",", ":"))


# ================================================================ ETT intubation (workup; raw CSVs identical to Zenodo)
# one subfolder = one tube; MH is shown as Surgeon 1 and MB as Surgeon 2 (same mapping as W16)
TUBES = [("otolaryngologist MH/uncoated", "MH", "uncoated", "uncoated"),
         ("otolaryngologist MH/coated 1", "MH", "coated", "tube 1"),
         ("otolaryngologist MH/coated 2", "MH", "coated", "tube 2"),
         ("otolaryngologist MH/coated 3", "MH", "coated", "tube 3"),
         ("otolaryngologist MB/uncoated", "MB", "uncoated", "uncoated"),
         ("otolaryngologist MB/1", "MB", "coated", "tube 1"),
         ("otolaryngologist MB/2", "MB", "coated", "tube 2"),
         ("otolaryngologist MB/3", "MB", "coated", "tube 3")]
SURGEON = {"MH": "Surgeon 1", "MB": "Surgeon 2"}


def ett_regions(time, force):
    """Python port of ett_force_analysis.m (2026 workup version; raw signal, no smoothing).
    Returns 0-based (start_A, end_A, start_B, end_B, plateau)."""
    n = len(force)
    dt = float(np.median(np.diff(time)))
    susN = max(1, mround(0.05 / dt))
    below = (force < -0.05).astype(float)
    hits = np.nonzero(fwd_sum(below, susN) > susN)[0]
    if not len(hits):
        raise ValueError("no intubation dip")
    sA = int(hits[0])
    while sA > 0 and force[sA - 1] < -0.01:
        sA -= 1
    base = force[:sA] if sA > 19 else force[:min(n, mround(1 / dt))]
    noise0 = max(mad_sd(base), 1e-4)
    idx_max = int(np.argmax(force))
    ext = idx_max
    while ext > 0 and force[ext - 1] > 0.05:
        ext -= 1
    if ext <= sA + susN:
        ext = n - 1
    seg = force[sA:ext + 1]
    deep = 0.5 * seg.min()
    d1 = int(np.nonzero(seg < deep)[0][0]); d2 = d1
    while d2 < len(seg) - 1 and seg[d2 + 1] < deep:
        d2 += 1
    imin = sA + d1 + int(np.argmin(seg[d1:d2 + 1]))
    W = max(2, mround(0.4 / dt))
    mv_mean = fwd_window(force, W, "mean")
    mv_std = fwd_window(force, W, "std")
    flat_thr = max(0.025, 4 * noise0)
    kk = np.arange(imin, min(ext, n - 1 - W) + 1)
    cand = mv_mean[kk][mv_std[kk] < flat_thr]
    cand = cand[np.abs(cand) <= 0.25]
    if len(cand) >= mround(0.3 / dt):
        edges = -0.25 + 0.02 * np.arange(26)
        cnt, _ = np.histogram(cand, edges)
        bi = int(np.argmax(cnt))
        c0 = (edges[bi] + edges[bi + 1]) / 2
        plateau = float(np.median(cand[np.abs(cand - c0) <= 0.03]))
    else:
        plateau = 0.0
    gap = force[imin:ext + 1]
    resid = gap[np.abs(gap - plateau) < 0.05]
    noise = mad_sd(resid) if len(resid) > 10 else noise0
    noise = max(noise, noise0)
    tol = min(max(4 * noise, 0.03), 0.15)
    eA = None
    for k in range(imin, min(ext, n - 1 - W) + 1):
        if mv_std[k] < flat_thr and abs(mv_mean[k] - plateau) < tol:
            eA = k
            break
    if eA is None:
        r = np.nonzero(force[imin:ext + 1] >= plateau - tol)[0]
        eA = imin + int(r[0]) if len(r) else ext - 1
    eA = min(eA, ext - 1)
    sig_thr = plateau - max(0.08, 6 * noise0)
    susE = max(1, mround(0.05 / dt)); gapN = mround(0.5 / dt)
    sigSus = fwd_sum((force < sig_thr).astype(float), susE) > susE
    while True:
        k2 = min(eA + gapN, ext - susE - 1)
        if k2 <= eA:
            break
        nx = np.nonzero(sigSus[eA:k2 + 1])[0]
        if not len(nx):
            break
        ks = eA + int(nx[0])
        rec = np.nonzero(force[ks:ext] >= plateau - 0.03)[0]
        if not len(rec):
            eA = ext - 1
            break
        ne = ks + int(rec[0])
        if ne <= eA:
            break
        eA = ne
    eA = max(eA, sA + 1)
    # Region B (extubation), as in the script
    thrB = max(plateau + 5 * noise, 0.05)
    aboveB = (force > thrB).astype(float)
    hb = np.nonzero(fwd_sum(aboveB[eA:], susN) > susN)[0]
    sB = idx_max if not len(hb) else eA + int(hb[0])
    while sB > eA + 1 and force[sB - 1] > plateau + noise:
        sB -= 1
    eB = n - 1
    for k in range(idx_max, n - W):
        if np.all(np.abs(force[k:k + W + 1]) < 0.05):
            eB = k
            break
    return sA, eA, sB, eB, plateau


def load_ett():
    trials = []
    for sub, op, cond, tube in TUBES:
        for f in sorted(glob.glob(os.path.join(ETTW, sub, "*.csv"))):
            d = pd.read_csv(f)
            t = d.iloc[:, 0].to_numpy(float); y = d.iloc[:, 1].to_numpy(float)
            ok = ~(np.isnan(t) | np.isnan(y)); t, y = t[ok], y[ok]
            sA, eA, sB, eB, plateau = ett_regions(t, y)
            imp = -np.trapz(y[sA:eA + 1], t[sA:eA + 1])
            trials.append(dict(op=op, surgeon=SURGEON[op], condition=cond, tube=f"{op}-{tube}", file=f"{sub}/{os.path.basename(f)}",
                               time=t, force=y, sA=sA, eA=eA, impulse=float(imp), peak=float(-y[sA:eA + 1].min()),
                               ext_impulse=float(np.trapz(y[sB:eB + 1], t[sB:eB + 1])), ext_peak=float(y[sB:eB + 1].max())))
    return trials


def verify_ett(trials):
    """Check the port against the workup's MATLAB output (analysis_results.mat, integral_A)."""
    import scipy.io as sio
    worst = 0.0
    for sub, *_ in TUBES:
        m = sio.loadmat(os.path.join(ETTW, sub, "analysis_results.mat"))
        names = [str(x[0]) for x in m["trial_names"].ravel()]
        for nm, ia in zip(names, np.abs(m["integral_A"].ravel())):
            mine = next(t["impulse"] for t in trials if t["file"] == f"{sub}/{nm}")
            worst = max(worst, abs(mine - ia) / ia)
    print(f"ETT port vs MATLAB analysis_results.mat: worst relative difference in impulse = {worst:.2e}")
    return worst


def reml_random_intercept(y, X, groups):
    """Linear mixed model y = Xb + u_group + e, REML (what statsmodels mixedlm fits). Returns b, cov(b)."""
    g = pd.factorize(groups)[0]
    Z = np.eye(g.max() + 1)[g]
    n, p = X.shape

    def parts(th):
        V = np.exp(th[0]) * Z @ Z.T + np.exp(th[1]) * np.eye(n)
        Vi = np.linalg.inv(V)
        XtViX = X.T @ Vi @ X
        b = np.linalg.solve(XtViX, X.T @ Vi @ y)
        r = y - X @ b
        nll = np.linalg.slogdet(V)[1] + np.linalg.slogdet(XtViX)[1] + r @ Vi @ r
        return nll, b, XtViX

    best = min((optimize.minimize(lambda th: parts(th)[0], x0, method="Nelder-Mead", options={"xatol": 1e-10, "fatol": 1e-12, "maxiter": 20000})
                for x0 in ([-2.0, -2.0], [-4.0, -1.0], [0.0, -3.0])), key=lambda r: r.fun)
    _, b, XtViX = parts(best.x)
    return b, np.linalg.inv(XtViX), np.exp(best.x)


def ett_stats(trials):
    df = pd.DataFrame([{k: t[k] for k in ("op", "condition", "tube", "impulse", "ext_impulse", "peak")} for t in trials])
    s = {"per_surgeon": {}}
    for op in ("MH", "MB"):
        g = df[df.op == op]
        u = g[g.condition == "uncoated"]
        tm = g[g.condition == "coated"].groupby("tube").impulse.mean()
        unc, coa = u.impulse.mean(), tm.mean()
        s["per_surgeon"][SURGEON[op]] = dict(
            n_uncoated=int(len(u)), n_coated=int((g.condition == "coated").sum()), n_coated_tubes=int(len(tm)),
            uncoated_mean_Ns=unc, coated_mean_of_tube_means_Ns=coa, coated_tube_means_Ns=[round(v, 4) for v in tm.values],
            coated_insertion_mean_Ns=g[g.condition == "coated"].impulse.mean(),
            reduction_pct=100 * (1 - coa / unc),
            reduction_pct_insertion_means=100 * (1 - g[g.condition == "coated"].impulse.mean() / unc),
            peak_uncoated_mean_N=u.peak.mean(), peak_coated_mean_N=g[g.condition == "coated"].peak.mean(),
            ext_uncoated_mean_Ns=u.ext_impulse.mean(), ext_coated_mean_of_tube_means_Ns=g[g.condition == "coated"].groupby("tube").ext_impulse.mean().mean())
    # primary test (as in the workup's foi_pooled_stats.py): log(impulse) ~ surgeon + coating, random intercept per tube, REML
    X = np.column_stack([np.ones(len(df)), (df.op == "MH").astype(float), (df.condition == "uncoated").astype(float)])
    b, cov, var = reml_random_intercept(np.log(df.impulse.to_numpy()), X, df.tube.to_numpy())
    se = np.sqrt(cov[2, 2]); z = b[2] / se
    s["mixed_model"] = dict(model="log(impulse) ~ surgeon + coating, random intercept for tube (8 tubes), REML; Wald z test",
                            ratio_coated_to_uncoated=float(np.exp(-b[2])), reduction_pct=float(100 * (1 - np.exp(-b[2]))),
                            ci95_reduction_pct=[float(100 * (1 - np.exp(-(b[2] - 1.96 * se)))), float(100 * (1 - np.exp(-(b[2] + 1.96 * se))))],
                            p=float(2 * stats.norm.sf(abs(z))), tube_sd_log=float(np.sqrt(var[0])))
    # supporting: tube means on the log scale, surgeon as block (n = 8 tubes)
    bm = df.assign(ly=np.log(df.impulse)).groupby(["op", "condition", "tube"], as_index=False).ly.mean()
    Xb = np.column_stack([np.ones(len(bm)), (bm.op == "MH").astype(float), (bm.condition == "uncoated").astype(float)])
    beta, res, *_ = np.linalg.lstsq(Xb, bm.ly.to_numpy(), rcond=None)
    dof = len(bm) - 3; s2 = float(res[0]) / dof
    seb = np.sqrt(s2 * np.linalg.inv(Xb.T @ Xb)[2, 2])
    s["tube_level_ols"] = dict(n_tubes=len(bm), reduction_pct=float(100 * (1 - np.exp(-beta[2]))), p=float(2 * stats.t.sf(abs(beta[2] / seb), dof)))
    s["n_uncoated"] = int((df.condition == "uncoated").sum()); s["n_coated"] = int((df.condition == "coated").sum())
    return s


def representative(trials, op, cond):
    g = [t for t in trials if t["op"] == op and t["condition"] == cond]
    med = np.median([t["impulse"] for t in g])
    return min(g, key=lambda t: abs(t["impulse"] - med))


def w38_ett(trials, s):
    fig, axes = plt.subplots(2, 2, figsize=(12, 10), gridspec_kw={"height_ratios": [1, 1.05]})
    rng = np.random.default_rng(5)
    for col, op in enumerate(("MH", "MB")):
        lab = SURGEON[op]; ps = s["per_surgeon"][lab]
        axA = axes[0, col]
        for cond, c, light in (("uncoated", GRAY, GRAY_LIGHT), ("coated", BLUE, BLUE_LIGHT)):
            t = representative(trials, op, cond)
            t0 = t["time"][t["sA"]]
            sl = slice(max(0, t["sA"] - 100), min(len(t["time"]), t["eA"] + 150))
            tt = t["time"][sl] - t0; ff = -t["force"][sl]
            axA.plot(tt, ff, color=c, lw=1.6, zorder=3, label=f"{cond.capitalize()} ({t['impulse']:.2f} N\u00b7s)")
            ra = slice(t["sA"], t["eA"] + 1)
            axA.fill_between(t["time"][ra] - t0, 0, -t["force"][ra], color=light, alpha=0.55, lw=0, zorder=2)
        axA.axhline(0, color=INK2, lw=0.8, zorder=1)
        axA.set_xlabel("Time from start of intubation (s)")
        axA.legend(loc="upper left" if op == "MH" else "upper right", title="Shaded area = impulse", title_fontsize=9.5)
        axA.set_xlim(left=-1); lo, hi = axA.get_ylim(); axA.set_ylim(lo, hi + 0.12 * (hi - lo))
        ptitle(axA, f"A{col + 1}. {lab}: one typical intubation each")
        axB = axes[1, col]
        for i, cond in enumerate(("uncoated", "coated")):
            v = np.array([t["impulse"] for t in trials if t["op"] == op and t["condition"] == cond])
            c = GRAY if cond == "uncoated" else BLUE
            axB.scatter(i + rng.uniform(-0.2, 0.2, len(v)), v, s=36, color=c, edgecolor=SURFACE, linewidth=1, zorder=3)
            m = ps["uncoated_mean_Ns"] if cond == "uncoated" else ps["coated_mean_of_tube_means_Ns"]
            axB.hlines(m, i - 0.32, i + 0.32, color=INK, lw=2.5, zorder=4)
            axB.text(i + 0.36, m, f"{m:.2f}", va="center", ha="left", fontsize=10.5, color=INK, fontweight="bold")
        ymax = max(t["impulse"] for t in trials if t["op"] == op) * 1.22
        bracket(axB, 0, 1, ymax * 0.9, f"\u2212{ps['reduction_pct']:.0f}%", ymax * 0.025)
        axB.set_ylim(0, ymax); axB.set_xlim(-0.6, 1.75); axB.grid(axis="x", visible=False)
        axB.set_xticks([0, 1]); axB.set_xticklabels([f"Uncoated\n(n = {ps['n_uncoated']})", f"Coated\n(n = {ps['n_coated']}, {ps['n_coated_tubes']} tubes)"])
        ptitle(axB, f"B{col + 1}. {lab}: every intubation")
    axes[0, 0].set_ylabel("Insertion force (N)"); axes[1, 0].set_ylabel("Integrated insertion force, impulse (N\u00b7s)")
    fig.subplots_adjust(hspace=0.42, wspace=0.22)
    mm = s["mixed_model"]
    ftitle(fig, "Coated endotracheal tubes intubate with about 60 percent less force",
           f"Cadaveric human larynx model, Surgeon 1 and Surgeon 2; n = {s['n_uncoated']} uncoated and {s['n_coated']} coated intubations "
           f"(1 uncoated and 3 coated tubes per surgeon)\nLine = group mean; p < 0.001 for both surgeons together, tube-level model; ZwiCoat internal study, 2026", nsub=2)
    p1, p2 = s["per_surgeon"]["Surgeon 1"], s["per_surgeon"]["Surgeon 2"]
    save(fig, "W38_ett_insertion_force",
         f"Two surgeons intubated a cadaveric human larynx on a load cell. Coated endotracheal tubes needed {p1['reduction_pct']:.0f} percent (Surgeon 1) "
         f"and {p2['reduction_pct']:.0f} percent (Surgeon 2) less integrated insertion force than the uncoated tube (p < 0.001).",
         "ZwiCoat internal study, 2026: 26.06 ETT paper workup, folder 'ETT force of insertion' (otolaryngologist MH = Surgeon 1, MB = Surgeon 2; subfolders "
         "uncoated, coated 1 to 3 and uncoated, 1 to 3; 60 raw CSVs, column 1 time (s), column 2 load (N), 100 samples/s). The same 60 CSVs are public, byte-identical, "
         f"in {ZENODO}, folder 'ETT force of insertion'. Intubation impulse = trapezoidal integral of the raw force over the intubation region detected by the "
         "workup's ett_force_analysis.m (2026, no smoothing), ported to Python here and checked against its analysis_results.mat. Each subfolder is one tube: "
         f"coated mean = mean of the three tube means. Surgeon 1: uncoated {p1['uncoated_mean_Ns']:.2f} N\u00b7s (n = {p1['n_uncoated']}), coated "
         f"{p1['coated_mean_of_tube_means_Ns']:.2f} N\u00b7s (n = {p1['n_coated']}), \u2212{p1['reduction_pct']:.1f}%. Surgeon 2: uncoated {p2['uncoated_mean_Ns']:.2f} "
         f"(n = {p2['n_uncoated']}), coated {p2['coated_mean_of_tube_means_Ns']:.2f} (n = {p2['n_coated']}), \u2212{p2['reduction_pct']:.1f}%. "
         f"Test: log(impulse) ~ surgeon + coating with a random intercept per tube (REML), pooled reduction {mm['reduction_pct']:.1f}% "
         f"(95% CI {mm['ci95_reduction_pct'][0]:.1f} to {mm['ci95_reduction_pct'][1]:.1f}%), p = {mm['p']:.4f}; with one uncoated tube per surgeon a per-surgeon "
         "p at the tube level is not estimable, so one pooled p is shown. Representative traces = the intubation closest to its group median. "
         "Trace data: figures/data/W38_traces.json",
         source_short="ZwiCoat internal study, 2026; raw data in the NIH SBIR Phase I dataset, Zenodo, doi:10.5281/zenodo.10459478")


def w38_json(trials, s):
    out = {"chart": "W38_ett_insertion_force", "units": {"time": "s", "force": "N (intubation push shown positive)", "impulse": "N*s"},
           "source": "ZwiCoat internal study, 2026 (raw CSVs also public in " + ZENODO + ")",
           "method": "time is relative to the detected start of intubation; window = 1 s before to 1.5 s after the intubation region, every 2nd sample (50 per s); impulse uses all raw samples",
           "summary": json.loads(json.dumps(s, default=float)), "trials": []}
    for t in trials:
        t0 = t["time"][t["sA"]]
        sl = slice(max(0, t["sA"] - 100), min(len(t["time"]), t["eA"] + 150), 2)
        out["trials"].append({"surgeon": t["surgeon"], "group": t["condition"], "tube": t["tube"].split("-", 1)[1],
                              "impulse_Ns": round(t["impulse"], 4), "peak_N": round(t["peak"], 4),
                              "intubation_s": [0.0, round(float(t["time"][t["eA"]] - t0), 3)],
                              "time_s": [round(float(v), 3) for v in t["time"][sl] - t0],
                              "force_N": [round(float(v), 4) for v in -t["force"][sl]]})
    json.dump(out, open(os.path.join(DATA, "W38_traces.json"), "w"), separators=(",", ":"))


def main():
    ci = load_ci(); cs = ci_stats(ci)
    print("CI:", json.dumps({k: (round(v, 4) if isinstance(v, float) else v) for k, v in cs.items()}, indent=1))
    w37_ci(ci, cs); w37_json(ci, cs)
    et = load_ett(); verify_ett(et); es = ett_stats(et)
    print("ETT:", json.dumps(es, indent=1, default=float))
    w38_ett(et, es); w38_json(et, es)
    md = ["# Figure manifest, SBIR Phase I charts (built by figures/build_sbir.py)", ""] + bf.manifest_rows(bf.MANIFEST)
    md += ["", f"Build note, W37 (review before publishing): the recorded insertion lengths differ by group (coated traces end at "
           f"{min(cs['end_depth_coated']):.1f} to {max(cs['end_depth_coated']):.1f} mm, uncoated at {min(cs['end_depth_uncoated']):.1f} to {max(cs['end_depth_uncoated']):.1f} mm, "
           "depth taken from the sample index as in plot_data.m), and work is integrated over each full trace. Over the depth every trace reaches (0 to 14 mm) "
           f"the work is {cs['work_0_14mm_coated_mean']:.0f} versus {cs['work_0_14mm_uncoated_mean']:.0f} mN·mm, {cs['work_0_14mm_reduction_pct']:.0f} percent lower, "
           f"Welch p = {cs['p_0_14mm_welch']:.2f}. Peak force is also reached late in the insertion: the peak within 0 to 14 mm is "
           f"{cs['peak_0_14mm_coated_mean']:.1f} versus {cs['peak_0_14mm_uncoated_mean']:.1f} mN, {cs['peak_0_14mm_reduction_pct']:.0f} percent lower, Welch p = {cs['p_peak_0_14mm_welch']:.2f}. The grant's 68.4 percent matches the record's untrimmed analysis (integral_comparison.png); the record's current "
           "plot_data.m with its two trims gives the 66 percent shown. The README calls column 1 encoder counts; in the files it is the logger's Sample Number at 50 samples/s."]
    md += ["", "W39 not built: the other public datasets in the record are ETT bending (six hard-coded time-to-crack values, no uncoated control) and ETT extubation "
           "force, which is not consistently lower for coated tubes (Surgeon 1 higher, Surgeon 2 lower)."]
    md += ["", "Source folders: ZEN = G:\\My Drive\\9 Zwitterion\\SBIR Phase 1 Dataset\\26.04 Zenodo repo (local copy of doi:10.5281/zenodo.10459478); "
           "ETTW = G:\\My Drive\\9 Zwitterion\\IA Data n Workups\\26.06 ETT paper\\data\\ETT force of insertion. PNG at 2x in png/, SVG in svg/, trace JSON in data/. Font: Arial."]
    open(os.path.join(HERE, "MANIFEST-sbir.md"), "w", encoding="utf-8").write("\n".join(md) + "\n")


if __name__ == "__main__":
    main()

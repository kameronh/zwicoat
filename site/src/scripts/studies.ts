/*
  In-vivo study browser (static fallback: W04_fibrosis_by_study.png).
  Data: W32_invivo_studies.json, inlined at build time by the evidence page.
  One marker per published comparison of coated versus uncoated.
  x = time in days on a log axis (rows with no duration sit in two left bands),
  y = percent change, coated versus uncoated (negative is better),
  color = species, shape = metric group, hollow = not significant.
*/
import { s, h, uid, guard, watchWidth, Tooltip } from './chart-utils';

export interface StudyRow {
  paper: string;
  year: number;
  journal: string;
  species: string;
  duration: string;
  device_or_substrate: string;
  metric: string;
  uncoated: number;
  coated: number;
  unit: string;
  pct_change: number;
  n: string;
  p: number | string | null;
  p_text: string | null;
  exact: boolean;
  figure?: string;
  setting: string;
  note?: string | null;
}

/* ---------- classification ---------- */

type SpeciesKey = 'mice' | 'rats' | 'sheep' | 'human' | 'invitro' | 'other';
type Band = 'ex' | 'day0' | null;
type Sig = 'sig' | 'ns' | 'unknown';

const SPECIES: Record<SpeciesKey, { label: string; cls: string }> = {
  mice: { label: 'Mice', cls: 'sp-mice' },
  rats: { label: 'Rats', cls: 'sp-rats' },
  sheep: { label: 'Sheep', cls: 'sp-sheep' },
  human: { label: 'Human cadaveric cochlea', cls: 'sp-human' },
  invitro: { label: 'In vitro', cls: 'sp-invitro' },
  other: { label: 'Other', cls: 'sp-other' },
};
const SPECIES_ORDER: SpeciesKey[] = ['mice', 'rats', 'sheep', 'human', 'invitro', 'other'];

/** Metric groups, matched on the metric string, in legend order. Each has a marker shape. */
const METRICS: { key: string; label: string; test: RegExp; shape: string }[] = [
  { key: 'capsule', label: 'Capsule thickness', test: /^capsule thickness/i, shape: 'circle' },
  { key: 'fibrosis', label: 'Fibrosis', test: /^fibrosis/i, shape: 'square' },
  { key: 'cells', label: 'Cells', test: /^cell nuclei/i, shape: 'diamond' },
  { key: 'macrophages', label: 'Macrophages', test: /^macrophage/i, shape: 'triangle' },
  { key: 'bacteria', label: 'Bacteria', test: /bacteri|colonies|s\. aureus/i, shape: 'triangleDown' },
  { key: 'impedance', label: 'Impedance', test: /impedance|access resistance/i, shape: 'hexagon' },
  { key: 'friction', label: 'Friction', test: /friction/i, shape: 'plus' },
  { key: 'insertion', label: 'Insertion force', test: /insertion|force variation/i, shape: 'cross' },
  { key: 'other', label: 'Other', test: /.*/, shape: 'pentagon' },
];

function metricGroup(metric: string) {
  return METRICS.find((m) => m.test.test(metric)) ?? METRICS[METRICS.length - 1];
}

function speciesKey(r: StudyRow): SpeciesKey {
  if (/in vitro/i.test(r.setting)) return 'invitro';
  const sp = r.species.toLowerCase();
  if (/mice|mouse/.test(sp)) return 'mice';
  if (/\brats?\b/.test(sp)) return 'rats';
  if (/sheep/.test(sp)) return 'sheep';
  if (/human|cadaver/.test(sp)) return 'human';
  return 'other';
}

/** Parse "6 weeks", "1 year", "21 days" and similar into days. Null when there is none. */
export function parseDays(duration: string): number | null {
  const m = duration.match(/(\d+(?:\.\d+)?)\s*(hour|h\b|day|week|month|year)/i);
  if (!m) return null;
  const n = parseFloat(m[1]);
  const u = m[2].toLowerCase();
  if (u.startsWith('h')) return n / 24;
  if (u.startsWith('day')) return n;
  if (u.startsWith('week')) return n * 7;
  if (u.startsWith('month')) return n * 30.4;
  return n * 365;
}

function bandFor(r: StudyRow, days: number | null): Band {
  if (days !== null) return null;
  if (/ex vivo|in vitro/i.test(r.setting)) return 'ex';
  if (/implantation|day 0/i.test(r.duration)) return 'day0';
  return 'ex';
}

/** Significance as printed: filled when p is at or below 0.05, hollow when not significant. */
function significance(pText: string | null): Sig {
  if (!pText) return 'unknown';
  const t = pText.toLowerCase();
  if (/not significant|\bns\b/.test(t)) return 'ns';
  if (/not stated/.test(t)) return 'unknown';
  const m = t.match(/([<>])?\s*(\d*\.?\d+)/);
  if (!m) return 'unknown';
  const v = parseFloat(m[2]);
  if (m[1] === '>') return 'ns';
  return v <= 0.05 ? 'sig' : 'ns';
}

function formatUnit(u: string): string {
  return u
    .replace(/10\^5/g, '10⁵')
    .replace(/\bum3\b/g, 'µm³')
    .replace(/\bmm3\b/g, 'mm³')
    .replace(/\bum\b/g, 'µm');
}

function formatNum(v: number): string {
  if (Math.abs(v) >= 100) return String(Math.round(v));
  return String(Number(v.toPrecision(3)));
}

/* ---------- marker shapes (centered on 0,0) ---------- */

function shapePath(kind: string, r: number): string {
  const f = (n: number) => Math.round(n * 100) / 100;
  switch (kind) {
    case 'square': {
      const a = r * 0.9;
      return `M${-a} ${-a}H${a}V${a}H${-a}Z`;
    }
    case 'diamond': {
      const a = r * 1.25;
      return `M0 ${-a}L${a} 0L0 ${a}L${-a} 0Z`;
    }
    case 'triangle': {
      const a = r * 1.2;
      return `M0 ${f(-a)}L${f(a)} ${f(a * 0.8)}L${f(-a)} ${f(a * 0.8)}Z`;
    }
    case 'triangleDown': {
      const a = r * 1.2;
      return `M0 ${f(a)}L${f(a)} ${f(-a * 0.8)}L${f(-a)} ${f(-a * 0.8)}Z`;
    }
    case 'hexagon': {
      const pts = [0, 1, 2, 3, 4, 5].map((i) => {
        const t = (Math.PI / 3) * i;
        return `${f(Math.cos(t) * r * 1.1)} ${f(Math.sin(t) * r * 1.1)}`;
      });
      return `M${pts.join('L')}Z`;
    }
    case 'pentagon': {
      const pts = [0, 1, 2, 3, 4].map((i) => {
        const t = -Math.PI / 2 + ((2 * Math.PI) / 5) * i;
        return `${f(Math.cos(t) * r * 1.15)} ${f(Math.sin(t) * r * 1.15)}`;
      });
      return `M${pts.join('L')}Z`;
    }
    case 'plus': {
      const a = r * 1.3;
      const b = r * 0.45;
      return `M${-b} ${-a}H${b}V${-b}H${a}V${b}H${b}V${a}H${-b}V${b}H${-a}V${-b}H${-b}Z`;
    }
    case 'cross': {
      const a = r * 1.3;
      const b = r * 0.45;
      const pts = [
        [-b, -a], [b, -a], [b, -b], [a, -b], [a, b], [b, b], [b, a], [-b, a], [-b, b], [-a, b], [-a, -b], [-b, -b],
      ].map(([x, y]) => {
        const c = Math.SQRT1_2;
        return `${f((x - y) * c)} ${f((x + y) * c)}`;
      });
      return `M${pts.join('L')}Z`;
    }
    default:
      return `M${-r} 0A${r} ${r} 0 1 0 ${r} 0A${r} ${r} 0 1 0 ${-r} 0Z`;
  }
}

/* ---------- derived rows ---------- */

interface Row extends StudyRow {
  id: string;
  sp: SpeciesKey;
  group: (typeof METRICS)[number];
  days: number | null;
  band: Band;
  sig: Sig;
  // Layout (computed per width, from all rows so filtering never moves a marker).
  px: number;
  py: number;
}

const DAY_MIN = 2;
const DAY_MAX = 500;
const Y_MAX = 20;
const Y_MIN = -100;
const TICKS_WIDE: [number, string][] = [[3, '3 d'], [7, '1 wk'], [14, '2 wk'], [28, '4 wk'], [42, '6 wk'], [91, '3 mo'], [182, '6 mo'], [365, '1 yr']];
const TICKS_NARROW: [number, string][] = [[7, '1 wk'], [28, '4 wk'], [91, '3 mo'], [365, '1 yr']];

export function mount(root: HTMLElement, data: StudyRow[]): void {
  if (!data.length) throw new Error('Study browser: no data');

  const rows: Row[] = data.map((r, i) => {
    const days = parseDays(r.duration);
    return {
      ...r,
      id: `st-${i}`,
      sp: speciesKey(r),
      group: metricGroup(r.metric),
      days,
      band: bandFor(r, days),
      sig: significance(r.p_text),
      px: 0,
      py: 0,
    };
  });
  const total = rows.length;
  const speciesPresent = SPECIES_ORDER.filter((k) => rows.some((r) => r.sp === k));
  const metricsPresent = METRICS.filter((m) => rows.some((r) => r.group.key === m.key));

  const state = { species: 'all', metric: 'all', exactOnly: false };

  const titleId = uid('sb-title');
  const descId = uid('sb-desc');
  const tipId = uid('sb-tip');
  const countId = uid('sb-count');

  /* ----- controls ----- */
  const speciesSel = h('select', { id: uid('sb-species') }, h('option', { value: 'all' }, 'All species'));
  speciesPresent.forEach((k) => speciesSel.append(h('option', { value: k }, SPECIES[k].label)));
  const metricSel = h('select', { id: uid('sb-metric') }, h('option', { value: 'all' }, 'All metrics'));
  metricsPresent.forEach((m) => metricSel.append(h('option', { value: m.key }, m.label)));
  const exactBox = h('input', { type: 'checkbox', id: uid('sb-exact') });
  const countEl = h('p', { class: 'sb-count', id: countId, 'aria-live': 'polite' });

  const controls = h(
    'div',
    { class: 'sb-controls' },
    h('label', { class: 'sb-field', for: speciesSel.id }, h('span', { class: 'label' }, 'Species'), speciesSel),
    h('label', { class: 'sb-field', for: metricSel.id }, h('span', { class: 'label' }, 'Metric'), metricSel),
    h('label', { class: 'sb-check', for: exactBox.id }, exactBox, h('span', {}, 'Exact values only')),
    countEl,
  );

  /* ----- legend ----- */
  const legend = h('div', { class: 'sb-legend' });
  const spList = h('ul', { class: 'sb-leg-list', role: 'list', 'aria-label': 'Color: species' });
  speciesPresent.forEach((k) => {
    spList.append(
      h(
        'li',
        {},
        s('svg', { class: 'sb-swatch', width: 14, height: 14, viewBox: '-7 -7 14 14', 'aria-hidden': 'true' }, s('circle', { class: `pt ${SPECIES[k].cls}`, r: 5.5 })),
        SPECIES[k].label,
      ),
    );
  });
  const shList = h('ul', { class: 'sb-leg-list', role: 'list', 'aria-label': 'Shape: metric' });
  metricsPresent.forEach((m) => {
    shList.append(
      h(
        'li',
        {},
        s('svg', { class: 'sb-swatch', width: 16, height: 16, viewBox: '-8 -8 16 16', 'aria-hidden': 'true' }, s('path', { class: 'pt sp-neutral', d: shapePath(m.shape, 5.5) })),
        m.label,
      ),
    );
  });
  const fillList = h(
    'ul',
    { class: 'sb-leg-list', role: 'list', 'aria-label': 'Fill: significance as printed' },
    h('li', {}, s('svg', { class: 'sb-swatch', width: 14, height: 14, viewBox: '-7 -7 14 14', 'aria-hidden': 'true' }, s('circle', { class: 'pt sp-neutral', r: 5 })), 'Filled: p at or below 0.05 as printed'),
    h('li', {}, s('svg', { class: 'sb-swatch', width: 14, height: 14, viewBox: '-7 -7 14 14', 'aria-hidden': 'true' }, s('circle', { class: 'pt sp-neutral ns', r: 5 })), 'Hollow: not significant'),
    h('li', {}, s('svg', { class: 'sb-swatch', width: 14, height: 14, viewBox: '-7 -7 14 14', 'aria-hidden': 'true' }, s('circle', { class: 'pt sp-neutral unknown', r: 5 })), 'Faded: p not reported'),
  );
  legend.append(spList, shList, fillList);

  /* ----- chart area ----- */
  const wrap = h('div', { class: 'ch-wrap' });
  const svgHost = h('div', { class: 'ch-svg-host' });
  wrap.append(svgHost);
  const tip = new Tooltip(wrap, tipId);

  /* ----- table view ----- */
  const tableHost = h('div', { class: 'sb-table-wrap' });
  const details = h(
    'details',
    { class: 'sb-details' },
    h('summary', {}, 'View the filtered comparisons as a table'),
    tableHost,
  );

  root.replaceChildren(controls, wrap, legend, details);
  root.classList.add('is-mounted');

  /* ----- helpers ----- */
  function visible(): Row[] {
    return rows.filter(
      (r) =>
        (state.species === 'all' || r.sp === state.species) &&
        (state.metric === 'all' || r.group.key === state.metric) &&
        (!state.exactOnly || r.exact),
    );
  }

  function describe(r: Row): string {
    return `${r.paper} (${r.year}), ${r.metric}, ${r.species}, ${r.duration}: ${formatNum(r.uncoated)} uncoated, ${formatNum(r.coated)} coated ${formatUnit(r.unit)}, ${r.pct_change} percent. p ${r.p_text ?? 'not stated'}.${r.exact ? '' : ' Approximate, read from the plot.'}`;
  }

  function dl(pairs: [string, string][]): HTMLElement {
    const el = h('dl', { class: 'ch-tip-dl' });
    pairs.forEach(([k, v]) => el.append(h('dt', {}, k), h('dd', {}, v)));
    return el;
  }

  function tipContent(r: Row): Node {
    return h(
      'div',
      { class: 'ch-tip-body' },
      h('p', { class: 'ch-tip-kicker label' }, `${r.paper} (${r.year}), ${r.journal}`),
      h('p', { class: 'ch-tip-title' }, r.metric),
      dl([
        ['Species', r.species],
        ['Duration', r.duration],
        ['Device', r.device_or_substrate],
        ['Uncoated', `${formatNum(r.uncoated)} ${formatUnit(r.unit)}`],
        ['Coated', `${formatNum(r.coated)} ${formatUnit(r.unit)}`],
        ['Change', `${r.pct_change > 0 ? '+' : ''}${r.pct_change} percent`],
        ['n', r.n],
        ['p', r.p_text ?? 'not stated'],
      ]),
      r.exact ? null : h('p', { class: 'ch-tip-badge ch-tip-approx' }, 'Approximate, read from the plot'),
    );
  }

  function renderTable(list: Row[]) {
    const head = ['Paper', 'Species', 'Duration', 'Device or substrate', 'Metric', 'Uncoated', 'Coated', 'Change (%)', 'n', 'p', 'Value'];
    const table = h(
      'table',
      { class: 'sb-table' },
      h('caption', { class: 'visually-hidden' }, 'Published comparisons of coated versus uncoated surfaces, matching the current filters'),
      h('thead', {}, h('tr', {}, ...head.map((t) => h('th', { scope: 'col' }, t)))),
      h(
        'tbody',
        {},
        ...list.map((r) =>
          h(
            'tr',
            {},
            h('th', { scope: 'row' }, `${r.paper} ${r.year}`),
            h('td', {}, r.species),
            h('td', {}, r.duration),
            h('td', {}, r.device_or_substrate),
            h('td', {}, r.metric),
            h('td', { class: 'num' }, `${formatNum(r.uncoated)} ${formatUnit(r.unit)}`),
            h('td', { class: 'num' }, `${formatNum(r.coated)} ${formatUnit(r.unit)}`),
            h('td', { class: 'num' }, `${r.pct_change > 0 ? '+' : ''}${r.pct_change}`),
            h('td', {}, r.n),
            h('td', {}, r.p_text ?? 'not stated'),
            h('td', {}, r.exact ? 'Exact' : 'Approximate'),
          ),
        ),
      ),
    );
    tableHost.replaceChildren(list.length ? table : h('p', {}, 'No comparisons match these filters.'));
  }

  /* ----- layout (positions for all rows, so filtering never moves a marker) ----- */
  function layout(W: number, H: number) {
    const narrow = W < 560;
    const m = { l: narrow ? 44 : 58, r: 14, t: 14, b: 62 };
    const bw = narrow ? 50 : 66;
    const bandsW = bw * 2;
    const xL = m.l + bandsW + 16;
    const xR = W - m.r;
    const ih = H - m.t - m.b;
    const lnMin = Math.log(DAY_MIN);
    const lnMax = Math.log(DAY_MAX);
    const xDay = (d: number) => xL + ((Math.log(d) - lnMin) / (lnMax - lnMin)) * (xR - xL);
    const yPct = (p: number) => m.t + ((Y_MAX - p) / (Y_MAX - Y_MIN)) * ih;
    const bandX = (b: 'ex' | 'day0') => m.l + (b === 'ex' ? bw / 2 : bw + bw / 2);

    const R = 6;
    const minDist = R * 2 + 1.5;
    const step = R * 1.7;
    const placed: { x: number; y: number }[] = [];
    const order = [...rows].sort((a, b) => {
      const ax = a.days !== null ? xDay(a.days) : bandX(a.band ?? 'ex');
      const bx = b.days !== null ? xDay(b.days) : bandX(b.band ?? 'ex');
      return ax - bx || a.pct_change - b.pct_change;
    });
    for (const r of order) {
      const x0 = r.days !== null ? xDay(r.days) : bandX(r.band ?? 'ex');
      const y = yPct(r.pct_change);
      let chosen = x0;
      for (let k = 0; k < 14; k++) {
        const off = (k % 2 === 0 ? 1 : -1) * Math.ceil(k / 2) * step;
        const x = x0 + off;
        if (placed.every((p) => Math.hypot(p.x - x, p.y - y) >= minDist)) {
          chosen = x;
          break;
        }
        if (k === 13) chosen = x0;
      }
      r.px = chosen;
      r.py = y;
      placed.push({ x: chosen, y });
    }
    return { narrow, m, bw, xL, xR, ih, xDay, yPct, R };
  }

  /* ----- drawing ----- */
  let current: string | null = null;
  let touchWasActive = false;
  let touchGesture = false;
  let lastWidth = 0;

  function setActive(id: string | null, showTip: boolean) {
    current = id;
    svgHost.querySelectorAll('.sb-mark').forEach((g) => g.classList.toggle('is-active', g.getAttribute('data-id') === id));
    if (!id) {
      tip.hide();
      return;
    }
    if (showTip) {
      const g = svgHost.querySelector(`[data-id="${id}"]`);
      const r = rows.find((x) => x.id === id);
      if (g && r) tip.show(tipContent(r), g.querySelector('.pt') ?? g);
    }
  }

  function draw(width: number) {
    lastWidth = width;
    const W = Math.max(280, width);
    const H = W < 560 ? 380 : 460;
    const L = layout(W, H);
    const { m, bw, xL, xR, ih, xDay, yPct, R } = L;
    const list = visible();

    countEl.textContent = `${list.length} of ${total} comparisons shown`;
    renderTable(list);

    const svg = s('svg', {
      class: 'ch-svg sb-svg',
      role: 'group',
      'aria-labelledby': `${titleId} ${descId}`,
      viewBox: `0 0 ${W} ${H}`,
      width: W,
      height: H,
    });
    svg.append(
      s('title', { id: titleId }, 'Every published in-vivo comparison of coated versus uncoated surfaces'),
      s(
        'desc',
        { id: descId },
        `Scatter chart. Horizontal axis: time in days on a log scale, with two bands at the left for ex vivo tests and for measurements at implantation. Vertical axis: percent change with the coating compared with uncoated; negative is better. ${list.length} of ${total} comparisons are shown. Use the arrow keys to move between markers. A table of the same data is below the chart.`,
      ),
    );

    // Bands for rows with no time axis position.
    svg.append(s('rect', { class: 'sb-band', x: m.l, y: m.t, width: bw * 2, height: ih }));
    svg.append(s('line', { class: 'ch-grid', x1: m.l + bw, x2: m.l + bw, y1: m.t, y2: m.t + ih }));

    // Horizontal gridlines and y labels.
    for (let v = Y_MIN; v <= Y_MAX; v += 20) {
      const y = yPct(v);
      svg.append(s('line', { class: v === 0 ? 'ch-zero' : 'ch-grid', x1: m.l, x2: xR, y1: y, y2: y }));
      svg.append(s('text', { class: 'ch-tick', x: m.l - 8, y: y + 4, 'text-anchor': 'end' }, String(v)));
    }
    const yTitle = s('text', { class: 'ch-axis-title', x: 0, y: 0, 'text-anchor': 'middle', transform: `translate(12 ${m.t + ih / 2}) rotate(-90)` }, 'Change, coated vs uncoated (%)');
    svg.append(yTitle);
    svg.append(s('text', { class: 'ch-note', x: xR - 4, y: yPct(0) - 6, 'text-anchor': 'end' }, 'Higher with coating'));
    svg.append(s('text', { class: 'ch-note', x: xR - 4, y: yPct(0) + 15, 'text-anchor': 'end' }, 'Lower with coating (better)'));

    // X ticks on the log axis.
    const ticks = L.narrow ? TICKS_NARROW : TICKS_WIDE;
    const yBase = m.t + ih;
    svg.append(s('line', { class: 'ch-axis', x1: m.l, x2: xR, y1: yBase, y2: yBase }));
    ticks.forEach(([d, label]) => {
      const x = xDay(d);
      svg.append(s('line', { class: 'ch-grid', x1: x, x2: x, y1: m.t, y2: yBase }));
      svg.append(s('line', { class: 'ch-axis', x1: x, x2: x, y1: yBase, y2: yBase + 4 }));
      svg.append(s('text', { class: 'ch-tick', x, y: yBase + 18, 'text-anchor': 'middle' }, label));
    });
    svg.append(s('text', { class: 'ch-axis-title', x: (xL + xR) / 2, y: yBase + 40, 'text-anchor': 'middle' }, 'Time after implantation (log scale)'));

    // Band labels.
    const bandLabel = (cx: number, lines: string[]) => {
      lines.forEach((t, i) => svg.append(s('text', { class: 'ch-tick ch-band-label', x: cx, y: yBase + 16 + i * 13, 'text-anchor': 'middle' }, t)));
    };
    bandLabel(m.l + bw / 2, L.narrow ? ['Ex vivo /', 'in vitro'] : ['Ex vivo /', 'in vitro']);
    bandLabel(m.l + bw + bw / 2, ['At', 'implant.']);

    if (list.length === 0) {
      svg.append(s('text', { class: 'ch-note ch-empty', x: (xL + xR) / 2, y: m.t + ih / 2, 'text-anchor': 'middle' }, 'No comparisons match these filters.'));
    }

    // Markers, ordered left to right so the arrow keys follow the picture.
    const ordered = [...list].sort((a, b) => a.px - b.px || a.py - b.py);
    const marks: SVGElement[] = [];
    ordered.forEach((r, idx) => {
      const g = s(
        'g',
        {
          class: `sb-mark ${r.sig}`,
          tabindex: idx === 0 ? 0 : -1,
          role: 'img',
          'aria-label': describe(r),
          'data-id': r.id,
          transform: `translate(${Math.round(r.px * 10) / 10} ${Math.round(r.py * 10) / 10})`,
        },
        s('circle', { class: 'hit', r: 9 }),
        s('path', { class: `pt ${SPECIES[r.sp].cls} ${r.sig === 'ns' ? 'ns' : ''} ${r.sig === 'unknown' ? 'unknown' : ''}`, d: shapePath(r.group.shape, R) }),
      );
      g.addEventListener('pointerenter', () => setActive(r.id, true));
      g.addEventListener('pointerleave', () => {
        if (document.activeElement !== g) setActive(null, false);
      });
      g.addEventListener('focus', () => {
        marks.forEach((x) => x.setAttribute('tabindex', x === g ? '0' : '-1'));
        setActive(r.id, true);
      });
      g.addEventListener('blur', () => setActive(null, false));
      g.addEventListener('pointerdown', (e) => {
        touchGesture = (e as PointerEvent).pointerType === 'touch';
        touchWasActive = current === r.id;
      });
      g.addEventListener('click', () => {
        if (touchGesture && !touchWasActive) setActive(r.id, true);
      });
      g.addEventListener('keydown', (e) => {
        const ke = e as KeyboardEvent;
        let next = -1;
        if (ke.key === 'ArrowRight' || ke.key === 'ArrowDown') next = Math.min(marks.length - 1, idx + 1);
        else if (ke.key === 'ArrowLeft' || ke.key === 'ArrowUp') next = Math.max(0, idx - 1);
        else if (ke.key === 'Home') next = 0;
        else if (ke.key === 'End') next = marks.length - 1;
        else if (ke.key === 'Escape') {
          setActive(null, false);
          return;
        }
        if (next >= 0) {
          ke.preventDefault();
          (marks[next] as unknown as HTMLElement).focus();
        }
      });
      marks.push(g);
      svg.append(g);
    });

    svgHost.replaceChildren(svg);
    current = null;
    tip.hide();
  }

  function redraw() {
    guard(root, () => draw(lastWidth || wrap.getBoundingClientRect().width));
  }

  speciesSel.addEventListener('change', () => {
    state.species = speciesSel.value;
    redraw();
  });
  metricSel.addEventListener('change', () => {
    state.metric = metricSel.value;
    redraw();
  });
  exactBox.addEventListener('change', () => {
    state.exactOnly = exactBox.checked;
    redraw();
  });
  document.addEventListener('pointerdown', (e) => {
    if (!(e.target instanceof Element) || !wrap.contains(e.target)) setActive(null, false);
  });

  watchWidth(wrap, (w) => guard(root, () => draw(w)));
}

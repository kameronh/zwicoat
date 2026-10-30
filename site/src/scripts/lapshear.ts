/*
  Lap-shear explorer (static fallback: W02_lapshear_database.png).
  Data: W02_lapshear_public.json, inlined at build time by the evidence page.
  One dot per experimental group (the group mean, 3 to 10 samples), grouped by
  substrate, with a bar at the median of the groups shown. Filters: substrate,
  year, failure mode. Formulation fields are not in the data and never shown.
  Vanilla TypeScript, colors only through the tokens applied in charts.css.
*/
import { s, h, uid, guard, watchWidth, Tooltip } from './chart-utils';

export interface LapShearRow {
  substrate: string;
  kPa: number;
  n: number | null;
  year: number | null;
  fail: string | null;
}

type FailKey = 'cohesive' | 'adhesive' | 'mixed' | 'not stated';

const FAIL_ORDER: FailKey[] = ['cohesive', 'adhesive', 'mixed', 'not stated'];
const FAIL_LABEL: Record<FailKey, string> = {
  cohesive: 'Cohesive (inside the gel)',
  adhesive: 'Adhesive (at the interface)',
  mixed: 'Mixed',
  'not stated': 'Not stated',
};
/** Column order, left to right. Any substrate not listed is appended in data order. */
const SUBSTRATE_ORDER = [
  'Silicone (PDMS)',
  'Silicone film on glass',
  'Implant silicone',
  'PVC',
  'PEEK',
  'Parylene-C',
  'Polyurethane (probe cover)',
];
/** Short names for the rotated labels on narrow screens. */
const SHORT: Record<string, string> = {
  'Silicone (PDMS)': 'PDMS',
  'Silicone film on glass': 'Film on glass',
  'Implant silicone': 'Implant silicone',
  'Polyurethane (probe cover)': 'Polyurethane',
};
const UNDATED = 'undated';

function failKey(f: string | null): FailKey {
  const t = (f ?? '').trim().toLowerCase();
  if (t.startsWith('coh')) return 'cohesive';
  if (t.startsWith('adh')) return 'adhesive';
  if (t.startsWith('mix')) return 'mixed';
  return 'not stated';
}

function median(values: number[]): number {
  const a = [...values].sort((x, y) => x - y);
  const n = a.length;
  if (!n) return 0;
  return n % 2 ? a[(n - 1) / 2] : (a[n / 2 - 1] + a[n / 2]) / 2;
}

/** Stable pseudo-random value in [0, 1) from an integer, so a dot never moves when filters change. */
function seeded(i: number): number {
  const x = Math.sin(i * 9301 + 49297) * 233280;
  return x - Math.floor(x);
}

const fmt = (v: number) => (v >= 100 ? String(Math.round(v)) : String(Number(v.toFixed(1))));

/** Break a label into lines of at most `max` characters. */
function wrap(text: string, max: number): string[] {
  const out: string[] = [];
  let line = '';
  for (const w of text.split(' ')) {
    if (line && (line + ' ' + w).length > max) {
      out.push(line);
      line = w;
    } else {
      line = line ? `${line} ${w}` : w;
    }
  }
  if (line) out.push(line);
  return out;
}

interface Row extends LapShearRow {
  id: string;
  idx: number;
  fk: FailKey;
  yearKey: string;
}

export function mount(root: HTMLElement, data: LapShearRow[]): void {
  if (!data.length) throw new Error('Lap-shear explorer: no data');

  const rows: Row[] = data.map((r, i) => ({
    ...r,
    id: `ls-${i}`,
    idx: i,
    fk: failKey(r.fail),
    yearKey: r.year === null || r.year === undefined ? UNDATED : String(r.year),
  }));
  const total = rows.length;

  const present = [...new Set(rows.map((r) => r.substrate))];
  const substrates = [...SUBSTRATE_ORDER.filter((x) => present.includes(x)), ...present.filter((x) => !SUBSTRATE_ORDER.includes(x))];
  const years = [...new Set(rows.map((r) => r.yearKey))].sort((a, b) => (a === UNDATED ? 1 : b === UNDATED ? -1 : a.localeCompare(b)));
  const fails = FAIL_ORDER.filter((k) => rows.some((r) => r.fk === k));

  const state = { substrate: 'all', year: 'all', fail: 'all' };

  const titleId = uid('ls-title');
  const descId = uid('ls-desc');
  const tipId = uid('ls-tip');
  const countId = uid('ls-count');

  /* ----- controls ----- */
  const select = (label: string, allText: string, opts: [string, string][]) => {
    const sel = h('select', { id: uid('ls-sel') }, h('option', { value: 'all' }, allText));
    opts.forEach(([v, t]) => sel.append(h('option', { value: v }, t)));
    const field = h('label', { class: 'sb-field', for: sel.id }, h('span', { class: 'label' }, label), sel);
    return { sel, field };
  };
  const subCtl = select('Substrate', 'All substrates', substrates.map((x) => [x, x]));
  const yearCtl = select('Year', 'All years', years.map((y) => [y, y === UNDATED ? 'Undated' : y]));
  const failCtl = select('Failure mode', 'All failure modes', fails.map((k) => [k, FAIL_LABEL[k]]));
  const countEl = h('p', { class: 'sb-count', id: countId, 'aria-live': 'polite' });
  const controls = h('div', { class: 'sb-controls' }, subCtl.field, yearCtl.field, failCtl.field, countEl);

  /* ----- chart area ----- */
  const wrapEl = h('div', { class: 'ch-wrap' });
  const svgHost = h('div', { class: 'ch-svg-host' });
  wrapEl.append(svgHost);
  const tip = new Tooltip(wrapEl, tipId);

  const note = h(
    'p',
    { class: 'ls-note' },
    'Each dot is one experimental group; the bar is the median of the groups shown. Strength is the group mean, so the values are not single tests. A group with no recorded sample count adds no tests to the count.',
  );

  /* ----- table view ----- */
  const tableHost = h('div', { class: 'sb-table-wrap' });
  const details = h('details', { class: 'sb-details' }, h('summary', {}, 'View the filtered groups as a table'), tableHost);

  root.replaceChildren(controls, wrapEl, note, details);
  root.classList.add('is-mounted');

  /* ----- helpers ----- */
  function visible(): Row[] {
    return rows.filter(
      (r) =>
        (state.substrate === 'all' || r.substrate === state.substrate) &&
        (state.year === 'all' || r.yearKey === state.year) &&
        (state.fail === 'all' || r.fk === state.fail),
    );
  }

  const nText = (r: Row) => (r.n === null || r.n === undefined ? 'n not recorded' : `n = ${r.n}`);
  const yearText = (r: Row) => (r.yearKey === UNDATED ? 'undated' : r.yearKey);

  function describe(r: Row): string {
    return `${r.substrate}, ${fmt(r.kPa)} kilopascals, ${nText(r)}, ${yearText(r)}, failure mode ${r.fk}.`;
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
      h('p', { class: 'ch-tip-title' }, r.substrate),
      dl([
        ['Strength', `${fmt(r.kPa)} kPa (group mean)`],
        ['Samples', r.n === null || r.n === undefined ? 'n not recorded' : String(r.n)],
        ['Year', r.yearKey === UNDATED ? 'Undated' : r.yearKey],
        ['Failure', FAIL_LABEL[r.fk]],
      ]),
    );
  }

  function renderTable(list: Row[]) {
    const head = ['Substrate', 'Strength (kPa)', 'n', 'Year', 'Failure mode'];
    const table = h(
      'table',
      { class: 'sb-table ls-table' },
      h('caption', { class: 'visually-hidden' }, 'Lap-shear groups matching the current filters'),
      h('thead', {}, h('tr', {}, ...head.map((t) => h('th', { scope: 'col' }, t)))),
      h(
        'tbody',
        {},
        ...list.map((r) =>
          h(
            'tr',
            {},
            h('th', { scope: 'row' }, r.substrate),
            h('td', { class: 'num' }, fmt(r.kPa)),
            h('td', { class: 'num' }, r.n === null || r.n === undefined ? 'not recorded' : String(r.n)),
            h('td', {}, r.yearKey === UNDATED ? 'Undated' : r.yearKey),
            h('td', {}, r.fk),
          ),
        ),
      ),
    );
    tableHost.replaceChildren(list.length ? table : h('p', {}, 'No groups match these filters.'));
  }

  /* ----- drawing ----- */
  const Y_STEP = 100;
  const yMax = Math.ceil(Math.max(...rows.map((r) => r.kPa)) / Y_STEP) * Y_STEP;
  let current: string | null = null;
  let touchWasActive = false;
  let touchGesture = false;
  let lastWidth = 0;

  function setActive(id: string | null, showTip: boolean) {
    current = id;
    svgHost.querySelectorAll('.ls-mark').forEach((g) => g.classList.toggle('is-active', g.getAttribute('data-id') === id));
    if (!id) {
      tip.hide();
      return;
    }
    if (showTip) {
      const g = svgHost.querySelector(`[data-id="${id}"]`);
      const r = rows.find((x) => x.id === id);
      if (g && r) tip.show(tipContent(r), g.querySelector('.ls-dot') ?? g);
    }
  }

  function draw(width: number) {
    lastWidth = width;
    const W = Math.max(280, width);
    const narrow = W < 560;
    const H = narrow ? 440 : 500;
    const m = { l: narrow ? 44 : 62, r: 12, t: 14, b: narrow ? 96 : 84 };
    const iw = W - m.l - m.r;
    const ih = H - m.t - m.b;
    const list = visible();
    const cols = state.substrate === 'all' ? substrates : [state.substrate];
    const colW = iw / cols.length;
    const xCol = (i: number) => m.l + (i + 0.5) * colW;
    const yVal = (v: number) => m.t + ih - (Math.min(v, yMax) / yMax) * ih;
    const half = Math.min(0.38 * colW, 70);

    const tests = list.reduce((a, r) => a + (r.n ?? 0), 0);
    const unrecorded = list.filter((r) => r.n === null || r.n === undefined).length;
    countEl.textContent = `${list.length} groups, ${tests.toLocaleString('en-US')} tests shown${unrecorded ? ` (${unrecorded} without a recorded n)` : ''}`;
    renderTable(list);

    const svg = s('svg', {
      class: 'ch-svg ls-svg',
      role: 'group',
      'aria-labelledby': `${titleId} ${descId}`,
      viewBox: `0 0 ${W} ${H}`,
      width: W,
      height: H,
    });
    svg.append(
      s('title', { id: titleId }, 'Lap-shear bond strength by substrate'),
      s(
        'desc',
        { id: descId },
        `Dot plot. One dot per experimental group, in one column per substrate. Vertical axis: lap-shear bond strength, group mean, in kilopascals. A bar marks the median of the groups in each column. ${list.length} of ${total} groups are shown. Use the arrow keys to move between dots. A table of the same data is below the chart.`,
      ),
    );

    for (let v = 0; v <= yMax; v += Y_STEP) {
      const y = yVal(v);
      svg.append(s('line', { class: v === 0 ? 'ch-axis' : 'ch-grid', x1: m.l, x2: W - m.r, y1: y, y2: y }));
      svg.append(s('text', { class: 'ch-tick', x: m.l - 8, y: y + 4, 'text-anchor': 'end' }, String(v)));
    }
    svg.append(
      s('text', { class: 'ch-axis-title', x: 0, y: 0, 'text-anchor': 'middle', transform: `translate(12 ${m.t + ih / 2}) rotate(-90)` }, narrow ? 'Bond strength, group mean (kPa)' : 'Lap-shear bond strength, group mean (kPa)'),
    );

    const marks: SVGElement[] = [];
    const ordered: { r: Row; x: number; y: number }[] = [];
    cols.forEach((sub, ci) => {
      const cx = xCol(ci);
      const pts = list.filter((r) => r.substrate === sub);
      const baseY = m.t + ih;

      // Column label (rotated on narrow screens) and its count.
      if (narrow) {
        svg.append(s('text', { class: 'ch-tick ls-col', x: cx, y: baseY + 14, 'text-anchor': 'end', transform: `rotate(-40 ${cx} ${baseY + 14})` }, `${SHORT[sub] ?? sub} (${pts.length})`));
      } else {
        const lines = wrap(sub, Math.max(10, Math.floor(colW / 7.5)));
        lines.forEach((t, k) => svg.append(s('text', { class: 'ch-rowlabel ls-col', x: cx, y: baseY + 20 + k * 16, 'text-anchor': 'middle' }, t)));
        svg.append(s('text', { class: 'ch-note', x: cx, y: baseY + 24 + lines.length * 16, 'text-anchor': 'middle' }, `${pts.length} groups`));
      }

      pts.forEach((r) => {
        const jx = (seeded(r.idx + 1) - 0.5) * 2 * half;
        ordered.push({ r, x: cx + jx, y: yVal(r.kPa) });
      });

      if (pts.length) {
        const med = median(pts.map((r) => r.kPa));
        const y = yVal(med);
        svg.append(
          s(
            'g',
            { class: 'ls-median' },
            s('title', {}, `${sub}: median ${fmt(med)} kPa across ${pts.length} groups`),
            s('line', { class: 'ls-bar', x1: cx - half - 8, x2: cx + half + 8, y1: y, y2: y }),
          ),
        );
        if (!narrow) svg.append(s('text', { class: 'ch-note ls-med', x: cx + half + 12, y: y + 4 }, fmt(med)));
      }
    });

    if (!list.length) {
      svg.append(s('text', { class: 'ch-note ch-empty', x: W / 2, y: m.t + ih / 2, 'text-anchor': 'middle' }, 'No groups match these filters.'));
    }

    // Dots in left-to-right order so the arrow keys follow the picture.
    ordered.sort((a, b) => a.x - b.x || a.y - b.y);
    ordered.forEach(({ r, x, y }, idx) => {
      const g = s(
        'g',
        {
          class: 'ls-mark',
          tabindex: idx === 0 ? 0 : -1,
          role: 'img',
          'aria-label': describe(r),
          'data-id': r.id,
          transform: `translate(${Math.round(x * 10) / 10} ${Math.round(y * 10) / 10})`,
        },
        s('circle', { class: 'hit', r: 9 }),
        s('circle', { class: 'ls-dot', r: 4.5 }),
      );
      g.addEventListener('pointerenter', () => setActive(r.id, true));
      g.addEventListener('pointerleave', () => {
        if (document.activeElement !== g) setActive(null, false);
      });
      g.addEventListener('focus', () => {
        marks.forEach((k) => k.setAttribute('tabindex', k === g ? '0' : '-1'));
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
    guard(root, () => draw(lastWidth || wrapEl.getBoundingClientRect().width));
  }

  subCtl.sel.addEventListener('change', () => {
    state.substrate = subCtl.sel.value;
    redraw();
  });
  yearCtl.sel.addEventListener('change', () => {
    state.year = yearCtl.sel.value;
    redraw();
  });
  failCtl.sel.addEventListener('change', () => {
    state.fail = failCtl.sel.value;
    redraw();
  });
  document.addEventListener('pointerdown', (e) => {
    if (!(e.target instanceof Element) || !wrapEl.contains(e.target)) setActive(null, false);
  });

  watchWidth(wrapEl, (w) => guard(root, () => draw(w)));
}

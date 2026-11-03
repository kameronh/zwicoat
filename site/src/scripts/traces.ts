/*
  Trace viewer (static fallbacks: W37_ci_insertion_synthetic.png, W38_ett_insertion_force.png).
  Data: W37_traces.json (synthetic cochlea, force against insertion depth, 11 insertions) and
  W38_traces.json (cadaveric larynx, force against time from the start of intubation, 60
  intubations). The public copies hold only the traces, trial and group labels and summary
  statistics. Two panels on one shared x and y range: uncoated traces on the left (gray),
  coated on the right (blue), no overlay. Hovering or focusing a trace draws it bold on top
  and shows its label, peak force and work or impulse.
  Vanilla TypeScript, colors only through the tokens applied in charts.css.
*/
import { s, h, uid, guard, watchWidth, Tooltip } from './chart-utils';

type Group = 'coated' | 'uncoated';

interface CochleaTrial {
  label: string;
  group: Group;
  peak_mN: number;
  work_mN_mm: number;
  depth_mm: number[];
  force_mN: number[];
}
interface LarynxTrial {
  label: string;
  surgeon: string;
  group: Group;
  tube: string;
  impulse_Ns: number;
  peak_N: number;
  time_s: number[];
  force_N: number[];
}
export interface CochleaData {
  chart: 'W37_ci_insertion_synthetic';
  trials: CochleaTrial[];
}
export interface LarynxData {
  chart: 'W38_ett_insertion_force';
  trials: LarynxTrial[];
}
export type TraceData = CochleaData | LarynxData;

/** One trace in a common shape, whichever dataset it came from. */
interface Trace {
  id: string;
  label: string;
  group: Group;
  set: string; // surgeon for W38, '' for W37
  xs: number[];
  ys: number[];
  peak: number;
  total: number; // work (mN·mm) or impulse (N·s)
}

interface Spec {
  title: string;
  xTitle: string;
  yTitle: string;
  yUnit: string;
  totalName: string;
  totalUnit: string;
  noun: string; // "insertion" or "intubation"
  sets: string[];
  traces: Trace[];
}

const GROUP_TEXT: Record<Group, string> = { uncoated: 'Uncoated', coated: 'Coated' };

const fmt = (v: number, digits: number) => {
  const t = v.toFixed(digits);
  return t.includes('.') ? t.replace(/\.?0+$/, '') : t;
};
const mean = (a: number[]) => (a.length ? a.reduce((x, y) => x + y, 0) / a.length : 0);

function niceStep(range: number, target: number): number {
  const raw = range / Math.max(1, target);
  const mag = 10 ** Math.floor(Math.log10(raw));
  const f = raw / mag;
  return (f <= 1 ? 1 : f <= 2 ? 2 : f <= 2.5 ? 2.5 : f <= 5 ? 5 : 10) * mag;
}
function ticks(lo: number, hi: number, target: number): number[] {
  const step = niceStep(hi - lo, target);
  const out: number[] = [];
  for (let v = Math.ceil(lo / step) * step; v <= hi + step * 1e-6; v += step) out.push(Math.round(v * 1e6) / 1e6);
  return out;
}

function toSpec(data: TraceData): Spec {
  if (data.chart === 'W37_ci_insertion_synthetic') {
    return {
      title: 'Insertion force along the depth of a synthetic cochlea, every insertion',
      xTitle: 'Insertion depth (mm)',
      yTitle: 'Insertion force (mN)',
      yUnit: 'mN',
      totalName: 'Work of insertion',
      totalUnit: 'mN·mm',
      noun: 'insertion',
      sets: [],
      traces: data.trials.map((t, i) => ({
        id: `tr37-${i}`,
        label: t.label,
        group: t.group,
        set: '',
        xs: t.depth_mm,
        ys: t.force_mN,
        peak: t.peak_mN,
        total: t.work_mN_mm,
      })),
    };
  }
  if (data.chart === 'W38_ett_insertion_force') {
    return {
      title: 'Endotracheal tube insertion force over time, every intubation',
      xTitle: 'Time from the start of intubation (s)',
      yTitle: 'Insertion force (N)',
      yUnit: 'N',
      totalName: 'Integrated force',
      totalUnit: 'N·s',
      noun: 'intubation',
      sets: [...new Set(data.trials.map((t) => t.surgeon))],
      traces: data.trials.map((t, i) => ({
        id: `tr38-${i}`,
        label: t.label,
        group: t.group,
        set: t.surgeon,
        xs: t.time_s,
        ys: t.force_N,
        peak: t.peak_N,
        total: t.impulse_Ns,
      })),
    };
  }
  throw new Error('Trace viewer: unknown dataset');
}

export function mount(root: HTMLElement, data: TraceData): void {
  const spec = toSpec(data);
  if (!spec.traces.length) throw new Error('Trace viewer: no traces');
  for (const t of spec.traces) {
    if (!t.xs.length || t.xs.length !== t.ys.length) throw new Error(`Trace viewer: bad trace ${t.label}`);
  }
  const big = spec.yUnit === 'N';
  const yDigits = big ? 2 : 1;
  const totDigits = big ? 2 : 0;

  const state = { set: spec.sets[0] ?? 'all' };

  const titleId = uid('tr-title');
  const descId = uid('tr-desc');
  const tipId = uid('tr-tip');

  /* ----- controls ----- */
  const controls = h('div', { class: 'sb-controls' });
  let setSel: HTMLSelectElement | null = null;
  if (spec.sets.length > 1) {
    setSel = h('select', { id: uid('tr-sel') });
    spec.sets.forEach((v) => setSel!.append(h('option', { value: v }, v)));
    setSel.append(h('option', { value: 'all' }, 'Both surgeons'));
    controls.append(h('label', { class: 'sb-field', for: setSel.id }, h('span', { class: 'label' }, 'Surgeon'), setSel));
  }
  const countEl = h('p', { class: 'sb-count', 'aria-live': 'polite' });
  controls.append(countEl);

  /* ----- chart ----- */
  const wrapEl = h('div', { class: 'ch-wrap' });
  const svgHost = h('div', { class: 'ch-svg-host' });
  wrapEl.append(svgHost);
  const tip = new Tooltip(wrapEl, tipId);

  /* ----- legend and group means ----- */
  const swatch = (g: Group) =>
    s('svg', { class: 'sb-swatch', width: 22, height: 10, viewBox: '0 0 22 10', 'aria-hidden': 'true' }, s('line', { class: `tr-swatch tr-${g}`, x1: 1, x2: 21, y1: 5, y2: 5 }));
  const legItems: Record<Group, HTMLElement> = {
    uncoated: h('li', {}),
    coated: h('li', {}),
  };
  const legend = h(
    'div',
    { class: 'sb-legend' },
    h('ul', { class: 'sb-leg-list', role: 'list', 'aria-label': 'Line color: group' }, legItems.uncoated, legItems.coated),
    h('p', { class: 'tr-hint' }, `Select a line, or tab to the chart and use the arrow keys, to see one ${spec.noun}.`),
  );

  /* ----- table ----- */
  const tableHost = h('div', { class: 'sb-table-wrap' });
  const details = h('details', { class: 'sb-details' }, h('summary', {}, `View every ${spec.noun} as a table`), tableHost);

  root.replaceChildren(controls, wrapEl, legend, details);
  root.classList.add('is-mounted');

  const visible = () => spec.traces.filter((t) => state.set === 'all' || t.set === state.set);
  const totalText = (t: Trace) => `${fmt(t.total, totDigits)} ${spec.totalUnit}`;
  const describe = (t: Trace) =>
    `${t.label}. ${GROUP_TEXT[t.group]}. Peak force ${fmt(t.peak, yDigits)} ${spec.yUnit}. ${spec.totalName} ${totalText(t)}.`;

  function tipContent(t: Trace): Node {
    const dl = h('dl', { class: 'ch-tip-dl' });
    const rows: [string, string][] = [
      ['Group', GROUP_TEXT[t.group]],
      ['Peak force', `${fmt(t.peak, yDigits)} ${spec.yUnit}`],
      [spec.totalName, totalText(t)],
    ];
    rows.forEach(([k, v]) => dl.append(h('dt', {}, k), h('dd', {}, v)));
    return h('div', { class: 'ch-tip-body' }, h('p', { class: 'ch-tip-title' }, t.label), dl);
  }

  function renderSide(list: Trace[]) {
    (['uncoated', 'coated'] as Group[]).forEach((g) => {
      const sub = list.filter((t) => t.group === g);
      legItems[g].replaceChildren(
        swatch(g),
        `${GROUP_TEXT[g]}, ${sub.length} ${spec.noun}s: mean peak ${fmt(mean(sub.map((t) => t.peak)), yDigits)} ${spec.yUnit}, mean ${spec.totalName.toLowerCase()} ${fmt(mean(sub.map((t) => t.total)), totDigits)} ${spec.totalUnit}`,
      );
    });
    const head = ['Trace', 'Group', `Peak force (${spec.yUnit})`, `${spec.totalName} (${spec.totalUnit})`];
    tableHost.replaceChildren(
      h(
        'table',
        { class: 'sb-table tr-table' },
        h('caption', { class: 'visually-hidden' }, `Every ${spec.noun} shown in the chart`),
        h('thead', {}, h('tr', {}, ...head.map((x) => h('th', { scope: 'col' }, x)))),
        h(
          'tbody',
          {},
          ...list.map((t) =>
            h(
              'tr',
              {},
              h('th', { scope: 'row' }, t.label),
              h('td', {}, GROUP_TEXT[t.group]),
              h('td', { class: 'num' }, fmt(t.peak, yDigits)),
              h('td', { class: 'num' }, fmt(t.total, totDigits)),
            ),
          ),
        ),
      ),
    );
    const nU = list.filter((t) => t.group === 'uncoated').length;
    countEl.textContent = `${list.length} ${spec.noun}s shown: ${nU} uncoated, ${list.length - nU} coated`;
  }

  /* ----- drawing ----- */
  let current: string | null = null;
  let lastWidth = 0;
  let touchGesture = false;
  let touchWasActive = false;
  let overlay: SVGElement | null = null;
  let svgEl: SVGElement | null = null;
  const paths = new Map<string, { d: string; px: number; py: number }>();

  function setActive(id: string | null, showTip: boolean) {
    current = id;
    svgHost.querySelectorAll('.tr-trace').forEach((g) => g.classList.toggle('is-active', g.getAttribute('data-id') === id));
    svgEl?.classList.toggle('has-active', !!id);
    if (!overlay) return;
    overlay.replaceChildren();
    if (!id) {
      tip.hide();
      return;
    }
    const t = spec.traces.find((x) => x.id === id);
    const p = paths.get(id);
    if (!t || !p) return;
    const dot = s('circle', { class: `tr-peak tr-${t.group}`, cx: p.px, cy: p.py, r: 4.5 });
    overlay.append(s('path', { class: `tr-hl tr-${t.group}`, d: p.d }), dot);
    if (showTip) tip.show(tipContent(t), dot);
  }

  function draw(width: number) {
    lastWidth = width;
    const W = Math.max(280, width);
    const narrow = W < 560;
    // Two panels, uncoated left and coated right, on one shared x and y range. Below 520 px they stack.
    const stacked = W < 520;
    const panelH = stacked ? 260 : narrow ? 320 : 380;
    const m = { l: narrow ? 46 : 58, r: 14, t: 30, b: 50 };
    const gap = stacked ? 0 : narrow ? 16 : 28;
    const pw = stacked ? W - m.l - m.r : (W - m.l - m.r - gap - m.l) / 2;
    const ih = panelH - m.t - m.b;
    const H = stacked ? panelH * 2 : panelH;
    const list = visible();
    renderSide(list);

    const xs = list.flatMap((t) => [t.xs[0], t.xs[t.xs.length - 1]]);
    const xLo = Math.min(0, ...xs);
    const xHi = Math.max(...xs);
    const yLoRaw = Math.min(0, ...list.map((t) => Math.min(...t.ys)));
    const yHiRaw = Math.max(...list.map((t) => Math.max(...t.ys)));
    const yStep = niceStep(yHiRaw - yLoRaw, narrow ? 4 : 6);
    const yHi = Math.ceil(yHiRaw / yStep) * yStep;
    const yLo = yLoRaw;
    const yT = ticks(yLo, yHi, narrow ? 4 : 6);
    const xT = ticks(xLo, xHi, narrow || !stacked ? 4 : 8);
    const groups: Group[] = ['uncoated', 'coated'];
    // Panel origin: left edge of the plot area and top of the panel.
    const origin = (g: Group) => {
      const i = groups.indexOf(g);
      return stacked ? { x: m.l, y: i * panelH } : { x: m.l + i * (pw + gap + m.l), y: 0 };
    };
    const Xg = (g: Group) => {
      const o = origin(g);
      return (v: number) => o.x + ((v - xLo) / (xHi - xLo || 1)) * pw;
    };
    const Yg = (g: Group) => {
      const o = origin(g);
      return (v: number) => o.y + m.t + ih - ((v - yLo) / (yHi - yLo || 1)) * ih;
    };

    const svg = s('svg', {
      class: 'ch-svg tr-svg',
      role: 'group',
      'aria-labelledby': `${titleId} ${descId}`,
      viewBox: `0 0 ${W} ${H}`,
      width: W,
      height: H,
    });
    svgEl = svg;
    svg.append(
      s('title', { id: titleId }, spec.title),
      s(
        'desc',
        { id: descId },
        `Two line charts side by side on the same scales, uncoated on the left and coated on the right, one line per ${spec.noun}: ${spec.xTitle.toLowerCase()} across, ${spec.yTitle.toLowerCase()} up. ${list.length} ${spec.noun}s are shown. Use the arrow keys to move from line to line; each line reports its peak force and ${spec.totalName.toLowerCase()}. A table of the same values is below the chart.`,
      ),
    );

    groups.forEach((g) => {
      const o = origin(g);
      const X = Xg(g);
      const Y = Yg(g);
      const n = list.filter((t) => t.group === g).length;
      svg.append(s('text', { class: `tr-panel-title tr-${g}-title`, x: o.x, y: o.y + 16 }, `${GROUP_TEXT[g]} (${n} ${spec.noun}s)`));
      yT.forEach((v) => {
        const y = Y(v);
        svg.append(s('line', { class: v === 0 ? 'ch-axis' : 'ch-grid', x1: o.x, x2: o.x + pw, y1: y, y2: y }));
        svg.append(s('text', { class: 'ch-tick', x: o.x - 8, y: y + 4, 'text-anchor': 'end' }, fmt(v, 2)));
      });
      xT.forEach((v) => {
        const x = X(v);
        svg.append(s('line', { class: 'ch-grid tr-vgrid', x1: x, x2: x, y1: o.y + m.t, y2: o.y + m.t + ih }));
        svg.append(s('text', { class: 'ch-tick', x, y: o.y + m.t + ih + 18, 'text-anchor': 'middle' }, fmt(v, 2)));
      });
      svg.append(
        s('text', { class: 'ch-axis-title', x: o.x + pw / 2, y: o.y + panelH - 8, 'text-anchor': 'middle' }, spec.xTitle),
        s('text', { class: 'ch-axis-title', x: 0, y: 0, 'text-anchor': 'middle', transform: `translate(${o.x - m.l + 13} ${o.y + m.t + ih / 2}) rotate(-90)` }, spec.yTitle),
      );
    });

    // Uncoated first, coated on top; within a group, smallest peak first. The arrow keys follow this order.
    const ordered = [...list].sort((a, b) => (a.group === b.group ? a.peak - b.peak : a.group === 'uncoated' ? -1 : 1));
    const marks: SVGElement[] = [];
    const lines = s('g', { class: 'tr-lines' });
    paths.clear();
    ordered.forEach((t, idx) => {
      const X = Xg(t.group);
      const Y = Yg(t.group);
      let d = '';
      let px = X(t.xs[0]);
      let py = Y(t.ys[0]);
      let best = -Infinity;
      for (let i = 0; i < t.xs.length; i++) {
        const x = Math.round(X(t.xs[i]) * 10) / 10;
        const y = Math.round(Y(t.ys[i]) * 10) / 10;
        d += `${i ? 'L' : 'M'}${x} ${y}`;
        if (t.ys[i] > best) {
          best = t.ys[i];
          px = x;
          py = y;
        }
      }
      paths.set(t.id, { d, px, py });
      const g = s(
        'g',
        {
          class: `tr-trace tr-${t.group}`,
          tabindex: idx === 0 ? 0 : -1,
          role: 'img',
          'aria-label': describe(t),
          'data-id': t.id,
        },
        s('path', { class: 'tr-hit', d }),
        s('path', { class: 'tr-line', d }),
      );
      g.addEventListener('pointerenter', () => setActive(t.id, true));
      g.addEventListener('pointerleave', () => {
        if (document.activeElement !== g) setActive(null, false);
      });
      g.addEventListener('focus', () => {
        marks.forEach((k) => k.setAttribute('tabindex', k === g ? '0' : '-1'));
        setActive(t.id, true);
      });
      g.addEventListener('blur', () => setActive(null, false));
      g.addEventListener('pointerdown', (e) => {
        touchGesture = (e as PointerEvent).pointerType === 'touch';
        touchWasActive = current === t.id;
      });
      g.addEventListener('click', () => {
        if (touchGesture && !touchWasActive) setActive(t.id, true);
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
      lines.append(g);
    });
    overlay = s('g', { class: 'tr-overlay', 'aria-hidden': 'true' });
    svg.append(lines, overlay);

    svgHost.replaceChildren(svg);
    current = null;
    tip.hide();
  }

  function redraw() {
    guard(root, () => draw(lastWidth || wrapEl.getBoundingClientRect().width));
  }

  setSel?.addEventListener('change', () => {
    state.set = setSel!.value;
    redraw();
  });
  document.addEventListener('pointerdown', (e) => {
    if (!(e.target instanceof Element) || !wrapEl.contains(e.target)) setActive(null, false);
  });

  watchWidth(wrapEl, (w) => guard(root, () => draw(w)));
}

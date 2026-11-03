/*
  Durability timeline (static fallback: W06_durability_timeline.png).
  Data: W06_durability.json, inlined at build time by DurabilityChart.astro.
  One marker per in-vivo checkpoint on a log days axis from about one week to
  one year; color = species. Hover or focus a marker for the species, what was
  shown and the paper; click, or press Enter, to open the paper (DOI). A list of
  the same checkpoints, with links, sits under the chart.
  Vanilla TypeScript, colors only through tokens in charts.css.
*/
import { s, h, uid, guard, watchWidth, Tooltip } from './chart-utils';

export interface DurabilityRow {
  days: number;
  label: string;
  species: string;
  what_was_shown: string;
  paper: string;
  year: number;
  journal: string;
  doi: string;
}

type SpeciesKey = 'mice' | 'rats' | 'sheep' | 'other';
const SPECIES: Record<SpeciesKey, { label: string; cls: string }> = {
  mice: { label: 'Mice', cls: 'fb-mouse' },
  rats: { label: 'Rats', cls: 'fb-rat' },
  sheep: { label: 'Sheep', cls: 'fb-sheep' },
  other: { label: 'Other', cls: 'fb-other' },
};
function speciesKey(sp: string): SpeciesKey {
  const t = sp.toLowerCase();
  if (/mouse|mice/.test(t)) return 'mice';
  if (/\brats?\b/.test(t)) return 'rats';
  if (/sheep/.test(t)) return 'sheep';
  return 'other';
}

const DAY_MIN = 10;
const DAY_MAX = 450;
const TICKS: [number, string][] = [[14, '2 wk'], [28, '4 wk'], [42, '6 wk'], [91, '3 mo'], [182, '6 mo'], [365, '1 yr']];
const TICKS_NARROW: [number, string][] = [[14, '2 wk'], [42, '6 wk'], [182, '6 mo'], [365, '1 yr']];

interface Item extends DurabilityRow {
  id: string;
  sp: SpeciesKey;
  stack: number; // 0 for the first checkpoint on a day, 1 for the second, ...
}

export function mount(root: HTMLElement, data: DurabilityRow[]): void {
  if (!data.length) throw new Error('Durability timeline: no data');
  const seen = new Map<number, number>();
  const items: Item[] = [...data]
    .sort((a, b) => a.days - b.days || a.year - b.year)
    .map((r, i) => {
      const k = seen.get(r.days) ?? 0;
      seen.set(r.days, k + 1);
      return { ...r, id: `du-${uid('c')}-${i}`, sp: speciesKey(r.species), stack: k };
    });
  const maxStack = Math.max(...items.map((r) => r.stack));

  const titleId = uid('du-title');
  const descId = uid('du-desc');
  const tipId = uid('du-tip');

  const wrap = h('div', { class: 'ch-wrap du-wrap' });
  const svgHost = h('div', { class: 'ch-svg-host' });
  wrap.append(svgHost);
  const tip = new Tooltip(wrap, tipId);

  const spPresent = (Object.keys(SPECIES) as SpeciesKey[]).filter((k) => items.some((r) => r.sp === k));
  const legend = h('ul', { class: 'sb-leg-list fb-legend', role: 'list', 'aria-label': 'Marker color: species' });
  spPresent.forEach((k) => legend.append(h('li', {}, h('span', { class: `fb-swatch fb-dot ${SPECIES[k].cls}`, 'aria-hidden': 'true' }), SPECIES[k].label)));
  const hint = h('p', { class: 'tr-hint' }, 'Select a marker for the finding; click it, or press Enter, to open the paper.');

  const list = h('ol', { class: 'tl-list du-list', 'aria-label': 'Durability checkpoints' });
  const listItems = new Map<string, HTMLElement>();
  items.forEach((r) => {
    const li = h(
      'li',
      { class: 'tl-item' },
      h('span', { class: 'tl-year' }, r.label),
      h('span', { class: 'tl-type' }, SPECIES[r.sp].label),
      h('span', { class: 'tl-text' }, `${r.what_was_shown} `, h('a', { href: r.doi, target: '_blank', rel: 'noopener' }, `${r.paper} ${r.year}, ${r.journal}`)),
    );
    listItems.set(r.id, li);
    list.append(li);
  });

  root.replaceChildren(wrap, h('div', { class: 'sb-legend' }, legend, hint), list);
  root.classList.add('is-mounted');

  const describe = (r: Item) => `${r.label} in ${r.species}: ${r.what_was_shown} ${r.paper} ${r.year}, ${r.journal}. Press Enter to open the paper.`;
  function tipContent(r: Item): Node {
    return h(
      'div',
      { class: 'ch-tip-body' },
      h('p', { class: 'ch-tip-kicker label' }, `${r.label}, ${SPECIES[r.sp].label.toLowerCase()}`),
      h('p', { class: 'ch-tip-title' }, r.what_was_shown),
      h('p', { class: 'ch-tip-meta' }, `${r.paper} ${r.year}, ${r.journal}`),
      h('p', { class: 'ch-tip-hint' }, 'Click to open the paper.'),
    );
  }

  let current: string | null = null;
  let touchGesture = false;
  let touchWasActive = false;

  function setActive(id: string | null, showTip: boolean) {
    current = id;
    svgHost.querySelectorAll('.du-mark').forEach((g) => g.classList.toggle('is-active', g.getAttribute('data-id') === id));
    listItems.forEach((li, k) => li.classList.toggle('is-active', k === id));
    if (!id) {
      tip.hide();
      return;
    }
    const g = svgHost.querySelector(`[data-id="${id}"]`);
    const r = items.find((x) => x.id === id);
    if (showTip && g && r) tip.show(tipContent(r), g.querySelector('.du-dot') ?? g);
  }

  function draw(width: number) {
    const W = Math.max(280, width);
    const narrow = W < 560;
    const R = narrow ? 7 : 8;
    const m = { l: 18, r: 18, t: 22, b: 44 };
    const rowGap = R * 2 + 8;
    const H = m.t + (maxStack + 1) * rowGap + 30 + m.b;
    const ln = (d: number) => Math.log(d);
    const X = (d: number) => m.l + ((ln(d) - ln(DAY_MIN)) / (ln(DAY_MAX) - ln(DAY_MIN))) * (W - m.l - m.r);
    const axisY = H - m.b;
    const svg = s('svg', {
      class: 'ch-svg du-svg',
      role: 'group',
      'aria-labelledby': `${titleId} ${descId}`,
      viewBox: `0 0 ${W} ${H}`,
      width: W,
      height: H,
    });
    svg.append(
      s('title', { id: titleId }, 'In-vivo durability checkpoints, two weeks to one year'),
      s(
        'desc',
        { id: descId },
        `Timeline on a log scale of days after implantation, with ${items.length} checkpoints colored by species. Use the arrow keys to move between checkpoints and Enter to open the paper. A list of the same checkpoints is below the chart.`,
      ),
    );
    svg.append(s('line', { class: 'du-axis', x1: m.l, x2: W - m.r, y1: axisY, y2: axisY }));
    (narrow ? TICKS_NARROW : TICKS).forEach(([d, t]) => {
      const x = X(d);
      svg.append(s('line', { class: 'ch-grid', x1: x, x2: x, y1: m.t - 6, y2: axisY }));
      svg.append(s('line', { class: 'ch-axis', x1: x, x2: x, y1: axisY, y2: axisY + 5 }));
      svg.append(s('text', { class: 'ch-tick', x, y: axisY + 20, 'text-anchor': 'middle' }, t));
    });
    svg.append(s('text', { class: 'ch-axis-title', x: (m.l + W - m.r) / 2, y: H - 6, 'text-anchor': 'middle' }, 'Time after implantation (log scale)'));

    // Markers sit above the axis; checkpoints on the same day stack upward. Nearby days are nudged so they never overlap.
    const marks: SVGElement[] = [];
    const placed: { x: number; y: number }[] = [];
    items.forEach((r, idx) => {
      let x = X(r.days);
      const y = axisY - 22 - r.stack * rowGap;
      for (const p of placed) if (Math.abs(p.y - y) < 1 && x - p.x < R * 2 + 3) x = p.x + R * 2 + 3;
      placed.push({ x, y });
      const g = s(
        'g',
        {
          class: `du-mark ${SPECIES[r.sp].cls}`,
          tabindex: idx === 0 ? 0 : -1,
          role: 'link',
          'aria-label': describe(r),
          'data-id': r.id,
          transform: `translate(${Math.round(x * 10) / 10} ${Math.round(y * 10) / 10})`,
        },
        s('line', { class: 'du-stem', x1: 0, x2: 0, y1: R, y2: axisY - y }),
        s('circle', { class: 'hit', r: R + 5 }),
        s('circle', { class: 'du-dot', r: R }),
      );
      const open = () => window.open(r.doi, '_blank', 'noopener');
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
        // On touch, the first tap shows the finding and the second opens the paper.
        if (touchGesture && !touchWasActive) setActive(r.id, true);
        else open();
      });
      g.addEventListener('keydown', (e) => {
        const ke = e as KeyboardEvent;
        let next = -1;
        if (ke.key === 'ArrowRight' || ke.key === 'ArrowDown') next = Math.min(marks.length - 1, idx + 1);
        else if (ke.key === 'ArrowLeft' || ke.key === 'ArrowUp') next = Math.max(0, idx - 1);
        else if (ke.key === 'Home') next = 0;
        else if (ke.key === 'End') next = marks.length - 1;
        else if (ke.key === 'Enter' || ke.key === ' ') {
          ke.preventDefault();
          open();
          return;
        } else if (ke.key === 'Escape') {
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

  document.addEventListener('pointerdown', (e) => {
    if (!(e.target instanceof Element) || !wrap.contains(e.target)) setActive(null, false);
  });
  watchWidth(wrap, (w) => guard(root, () => draw(w)));
}

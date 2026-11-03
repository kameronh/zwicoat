/*
  Scar-tissue interactive chart (static fallback: W04_fibrosis_by_study.png).
  Data: W04_fibrosis.json, inlined at build time by the page that mounts it.
  One horizontal bar per published measurement: bar length = percent reduction
  in fibrotic capsule or fibrosis around the coated surface versus uncoated.
  Color = species (mouse blue, rat plum, sheep blue-deep). Filters by species
  and paper. Hover or focus a bar for its values; click pins the tooltip so its
  "Open the paper" link can be followed; Enter opens the paper (DOI).
  Built like antifouling.ts. Vanilla TypeScript, colors only through tokens in charts.css.
*/
import { h, uid, guard, Tooltip } from './chart-utils';

export interface FibrosisRow {
  label: string;
  species: string;
  duration: string;
  substrate: string;
  paper: string;
  year: number;
  journal: string;
  doi: string;
  pct_reduction: number;
  uncoated: number;
  coated: number;
  unit: string;
  n: string;
  exact: boolean;
}

type SpeciesKey = 'mouse' | 'rat' | 'sheep' | 'other';

const SPECIES: Record<SpeciesKey, { label: string; cls: string }> = {
  mouse: { label: 'Mice', cls: 'fb-mouse' },
  rat: { label: 'Rats', cls: 'fb-rat' },
  sheep: { label: 'Sheep', cls: 'fb-sheep' },
  other: { label: 'Other', cls: 'fb-other' },
};
const SPECIES_ORDER: SpeciesKey[] = ['mouse', 'rat', 'sheep', 'other'];

function speciesKey(s: string): SpeciesKey {
  const t = s.toLowerCase();
  if (/mouse|mice/.test(t)) return 'mouse';
  if (/\brats?\b/.test(t)) return 'rat';
  if (/sheep/.test(t)) return 'sheep';
  return 'other';
}

const shortPaper = (r: FibrosisRow) => `${r.paper.replace(/\s+et al\.?/i, '')} ${r.year}`;

/** "um (capsule thickness)" -> value unit "µm", measure "capsule thickness". */
function splitUnit(u: string): { unit: string; measure: string } {
  const m = u.match(/^(.*?)\s*\((.*)\)\s*$/);
  const unit = (m ? m[1] : u).replace(/\bum\b/g, 'µm');
  return { unit, measure: m ? m[2] : '' };
}

const fmt = (v: number) => (Math.abs(v) >= 100 ? String(Math.round(v)) : String(Number(v.toPrecision(3))));
const withUnit = (v: number, unit: string) => (unit.startsWith('%') ? `${fmt(v)}${unit}` : `${fmt(v)} ${unit}`);

interface Row extends FibrosisRow {
  id: string;
  sp: SpeciesKey;
  paperKey: string;
  order: number;
}

export function mount(root: HTMLElement, data: FibrosisRow[]): void {
  if (!data.length) throw new Error('Fibrosis chart: no data');
  const rows: Row[] = data.map((r, i) => ({ ...r, id: `fb-${uid('r')}-${i}`, sp: speciesKey(r.species), paperKey: shortPaper(r), order: i }));
  const total = rows.length;
  const speciesPresent = SPECIES_ORDER.filter((k) => rows.some((r) => r.sp === k));
  const papers = [...new Map(rows.map((r) => [r.paperKey, r.year])).entries()]
    .sort((a, b) => a[1] - b[1] || a[0].localeCompare(b[0]))
    .map(([k]) => k);

  const state = { species: 'all', paper: 'all' };
  const titleId = uid('fb-title');
  const tipId = uid('fb-tip');

  /* ----- controls ----- */
  const select = (label: string, allText: string, opts: [string, string][]) => {
    const sel = h('select', { id: uid('fb-sel') }, h('option', { value: 'all' }, allText));
    opts.forEach(([v, t]) => sel.append(h('option', { value: v }, t)));
    const field = h('label', { class: 'sb-field', for: sel.id }, h('span', { class: 'label' }, label), sel);
    return { sel, field };
  };
  const spCtl = select('Species', 'All species', speciesPresent.map((k) => [k, SPECIES[k].label]));
  const paperCtl = select('Paper', 'All papers', papers.map((p) => [p, p]));
  const countEl = h('p', { class: 'sb-count', 'aria-live': 'polite' });
  const controls = h('div', { class: 'sb-controls' }, spCtl.field, paperCtl.field, countEl);

  /* ----- chart ----- */
  const wrap = h('div', { class: 'ch-wrap fb-wrap' });
  const list = h('div', { class: 'fb-chart', role: 'group', 'aria-labelledby': titleId });
  const titleEl = h(
    'p',
    { class: 'visually-hidden', id: titleId },
    'Reduction in scar capsule or fibrosis around coated surfaces compared with uncoated, one bar per published measurement, colored by species. Use the up and down arrow keys to move between bars; press Enter to open the paper. A table of the same data is below the chart.',
  );
  const axis = h('div', { class: 'fb-axis', 'aria-hidden': 'true' });
  const axTicks = h('span', { class: 'af-axis-ticks' });
  [0, 20, 40, 60, 80, 100].forEach((v) => axTicks.append(h('span', { style: `left:${v}%` }, `${v}%`)));
  axis.append(h('span', { class: 'af-axis-spacer' }), axTicks, h('span', { class: 'af-axis-spacer' }));
  const legend = h('ul', { class: 'sb-leg-list fb-legend', role: 'list', 'aria-label': 'Bar color: species' });
  speciesPresent.forEach((k) =>
    legend.append(h('li', {}, h('span', { class: `fb-swatch ${SPECIES[k].cls}`, 'aria-hidden': 'true' }), SPECIES[k].label)),
  );
  const note = h('p', { class: 'af-axis-note' }, 'Reduction in capsule thickness or fibrosis versus the uncoated surface. ~ marks a value estimated from a published plot.');
  wrap.append(titleEl, list, axis, legend, note);
  const tip = new Tooltip(wrap, tipId);

  /* ----- table ----- */
  const tableHost = h('div', { class: 'sb-table-wrap' });
  const details = h('details', { class: 'sb-details' }, h('summary', {}, 'View the measurements as a table'), tableHost);

  root.replaceChildren(controls, wrap, details);
  root.classList.add('is-mounted');

  const visible = () =>
    rows.filter((r) => (state.species === 'all' || r.sp === state.species) && (state.paper === 'all' || r.paperKey === state.paper));
  const valueText = (r: Row) => `${r.exact ? '' : '~'}${r.pct_reduction}%`;

  function describe(r: Row): string {
    const u = splitUnit(r.unit);
    return `${r.label}. ${r.paperKey}, ${r.journal}. ${u.measure ? `${u.measure}: ` : ''}${withUnit(r.uncoated, u.unit)} uncoated, ${withUnit(r.coated, u.unit)} coated, ${r.exact ? '' : 'about '}${r.pct_reduction} percent less. n ${r.n}. Press Enter to open the paper.`;
  }

  function tipContent(r: Row): Node {
    const u = splitUnit(r.unit);
    const dl = h('dl', { class: 'ch-tip-dl' });
    const pairs: [string, string][] = [
      ['Model', `${SPECIES[r.sp].label}, ${r.duration}`],
      ['Surface', r.substrate],
      ['Measure', u.measure || 'fibrosis'],
      ['Uncoated', withUnit(r.uncoated, u.unit)],
      ['Coated', withUnit(r.coated, u.unit)],
      ['Reduction', `${r.exact ? '' : 'about '}${r.pct_reduction} percent`],
      ['n', r.n],
    ];
    pairs.forEach(([k, v]) => dl.append(h('dt', {}, k), h('dd', {}, v)));
    return h(
      'div',
      { class: 'ch-tip-body' },
      h('p', { class: 'ch-tip-kicker label' }, `${r.paper} ${r.year}, ${r.journal}`),
      h('p', { class: 'ch-tip-title' }, r.label),
      dl,
      h('p', { class: 'ch-tip-link' }, h('a', { href: r.doi, target: '_blank', rel: 'noopener' }, 'Open the paper')),
    );
  }

  function renderTable(items: Row[]) {
    const head = ['Paper', 'Species', 'Duration', 'Surface', 'Uncoated', 'Coated', 'Reduction (%)', 'n', 'Link'];
    const table = h(
      'table',
      { class: 'sb-table fb-table' },
      h('caption', { class: 'visually-hidden' }, 'Published scar and fibrosis measurements, matching the current filters'),
      h('thead', {}, h('tr', {}, ...head.map((t) => h('th', { scope: 'col' }, t)))),
      h(
        'tbody',
        {},
        ...items.map((r) => {
          const u = splitUnit(r.unit);
          return h(
            'tr',
            {},
            h('th', { scope: 'row' }, `${r.paperKey}, ${r.journal}`),
            h('td', {}, SPECIES[r.sp].label),
            h('td', {}, r.duration),
            h('td', {}, r.substrate),
            h('td', { class: 'num' }, withUnit(r.uncoated, u.unit)),
            h('td', { class: 'num' }, withUnit(r.coated, u.unit)),
            h('td', { class: 'num' }, valueText(r).replace('%', '')),
            h('td', {}, r.n),
            h('td', {}, h('a', { href: r.doi, target: '_blank', rel: 'noopener' }, 'Paper')),
          );
        }),
      ),
    );
    tableHost.replaceChildren(items.length ? table : h('p', {}, 'No measurements match these filters.'));
  }

  /* ----- interaction ----- */
  let current: string | null = null;
  let pinned = false;
  let marks: HTMLElement[] = [];

  function setActive(id: string | null, showTip: boolean, pin = false) {
    current = id;
    pinned = !!id && pin;
    tip.el.classList.toggle('is-pinned', pinned);
    marks.forEach((m) => m.classList.toggle('is-active', m.dataset.id === id));
    if (!id) {
      tip.hide();
      return;
    }
    if (showTip) {
      const el = marks.find((m) => m.dataset.id === id);
      const r = rows.find((x) => x.id === id);
      if (el && r) tip.show(tipContent(r), el.querySelector('.fb-track') ?? el);
    }
  }

  function bindRow(el: HTMLElement, r: Row, idx: number) {
    el.addEventListener('pointerenter', () => {
      if (!pinned) setActive(r.id, true);
    });
    el.addEventListener('pointerleave', () => {
      if (!pinned && document.activeElement !== el) setActive(null, false);
    });
    el.addEventListener('focus', () => {
      marks.forEach((x) => x.setAttribute('tabindex', x === el ? '0' : '-1'));
      setActive(r.id, true);
    });
    el.addEventListener('click', () => {
      // A click pins the tooltip, so its link can be reached; a second click releases it.
      if (pinned && current === r.id) setActive(null, false);
      else setActive(r.id, true, true);
    });
    el.addEventListener('keydown', (e) => {
      let next = -1;
      if (e.key === 'ArrowDown' || e.key === 'ArrowRight') next = Math.min(marks.length - 1, idx + 1);
      else if (e.key === 'ArrowUp' || e.key === 'ArrowLeft') next = Math.max(0, idx - 1);
      else if (e.key === 'Home') next = 0;
      else if (e.key === 'End') next = marks.length - 1;
      else if (e.key === 'Enter' || e.key === ' ') {
        e.preventDefault();
        window.open(r.doi, '_blank', 'noopener');
        return;
      } else if (e.key === 'Escape') {
        setActive(null, false);
        return;
      }
      if (next >= 0) {
        e.preventDefault();
        marks[next].focus();
      }
    });
  }

  function draw() {
    const shown = visible();
    countEl.textContent = `${shown.length} of ${total} measurements`;
    renderTable(shown);
    marks = [];
    const children: HTMLElement[] = [];
    shown.forEach((r) => {
      const idx = marks.length;
      const el = h(
        'div',
        { class: `fb-row ${SPECIES[r.sp].cls}`, tabindex: idx === 0 ? 0 : -1, role: 'img', 'aria-label': describe(r), 'data-id': r.id },
        h('span', { class: 'af-label' }, h('span', { class: 'af-assay' }, r.label), h('span', { class: 'af-meta' }, r.paperKey, h('span', { class: 'fb-journal' }, `, ${r.journal}`))),
        h('span', { class: 'fb-track' }, h('span', { class: 'fb-bar', style: `width:${Math.max(0, Math.min(100, r.pct_reduction))}%` })),
        h('span', { class: 'af-val' }, valueText(r)),
      );
      bindRow(el, r, idx);
      marks.push(el);
      children.push(el);
    });
    if (!children.length) children.push(h('p', { class: 'af-empty' }, 'No measurements match these filters.'));
    list.replaceChildren(...children);
    axis.hidden = !marks.length;
    setActive(null, false);
  }
  const redraw = () => guard(root, draw);

  spCtl.sel.addEventListener('change', () => {
    state.species = spCtl.sel.value;
    redraw();
  });
  paperCtl.sel.addEventListener('change', () => {
    state.paper = paperCtl.sel.value;
    redraw();
  });
  document.addEventListener('pointerdown', (e) => {
    if (!(e.target instanceof Element) || !wrap.contains(e.target)) setActive(null, false);
  });
  wrap.addEventListener('focusout', (e) => {
    const to = (e as FocusEvent).relatedTarget;
    if (!(to instanceof Element) || !wrap.contains(to)) {
      if (!pinned) setActive(null, false);
    }
  });

  draw();
}

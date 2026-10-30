/*
  Antifouling browser (static fallback: W05_antifouling_and_friction.png).
  Data: W05_antifouling_all.json, inlined at build time by the evidence page.
  One bar per published comparison of a coated surface with an uncoated one:
  bar length = percent reduction versus uncoated, grouped into four bands
  (protein, cells, bacteria, friction). The page shows 48 comparisons; the
  static chart shows the 38 that have a single clean value.
  Vanilla TypeScript, colors only through the tokens applied in charts.css.
*/
import { h, uid, guard, Tooltip } from './chart-utils';

export interface AntifoulingRow {
  category: string;
  assay: string;
  surface: string;
  paper: string;
  year: number;
  journal: string;
  species_or_setting: string;
  uncoated: number;
  coated: number;
  unit: string;
  pct_reduction: number;
  n: string;
  p_text: string | null;
  exact: boolean;
  figure?: string | null;
  in_static_chart: boolean;
  note?: string | null;
}

/* ---------- classification ---------- */

type CategoryKey = 'Protein' | 'Cells' | 'Bacteria' | 'Friction';
type ChemKey = 'sbma' | 'cbma' | 'dual' | 'other';
type SettingKey = 'invitro' | 'invivo';
type SortKey = 'year' | 'reduction';

const BANDS: { key: CategoryKey; title: string }[] = [
  { key: 'Protein', title: 'Protein: fibrinogen adsorption' },
  { key: 'Cells', title: 'Cells: attachment in culture' },
  { key: 'Bacteria', title: 'Bacteria: Staphylococcus adhesion' },
  { key: 'Friction', title: 'Friction: coated versus uncoated silicone' },
];

const CHEMS: Record<ChemKey, string> = {
  sbma: 'SBMA',
  cbma: 'CBMA',
  dual: 'Dual network',
  other: 'Other',
};
const CHEM_ORDER: ChemKey[] = ['sbma', 'cbma', 'dual', 'other'];

const SETTINGS: Record<SettingKey, string> = {
  invitro: 'In vitro or bench',
  invivo: 'In vivo or explant',
};
const SETTING_ORDER: SettingKey[] = ['invitro', 'invivo'];

/**
 * Chemistry comes from the surface string. A dual network is checked first,
 * because the dual-network rows also name their SBMA monomer. pCBMA counts as CBMA.
 */
export function chemistryKey(surface: string): ChemKey {
  if (/dual[\s-]*network/i.test(surface)) return 'dual';
  if (/SBMA|sulfobetaine/i.test(surface)) return 'sbma';
  if (/CBMA|carboxybetaine/i.test(surface)) return 'cbma';
  return 'other';
}

/** In vivo or explant when the animal, the explant or an in-vivo exposure is part of the test. */
export function settingKey(setting: string): SettingKey {
  return /in vivo|explant/i.test(setting) ? 'invivo' : 'invitro';
}

function shortPaper(r: AntifoulingRow): string {
  return `${r.paper.replace(/\s+et al\.?/i, '')} ${r.year}`;
}

function formatUnit(u: string): string {
  return u
    .replace(/10\^-4/g, '10⁻⁴')
    .replace(/\bum2\b/g, 'µm²')
    .replace(/\bum\b/g, 'µm');
}

function formatNum(v: number): string {
  if (Math.abs(v) >= 100) return String(Math.round(v));
  return String(Number(v.toPrecision(3)));
}

/* ---------- derived rows ---------- */

interface Row extends AntifoulingRow {
  id: string;
  cat: CategoryKey;
  chem: ChemKey;
  setting: SettingKey;
  paperKey: string;
  order: number;
}

export function mount(root: HTMLElement, data: AntifoulingRow[]): void {
  if (!data.length) throw new Error('Antifouling browser: no data');

  const rows: Row[] = data.map((r, i) => {
    const cat = BANDS.find((b) => b.key === r.category)?.key;
    if (!cat) throw new Error(`Antifouling browser: unknown category "${r.category}"`);
    return {
      ...r,
      id: `af-${i}`,
      cat,
      chem: chemistryKey(r.surface),
      setting: settingKey(r.species_or_setting),
      paperKey: shortPaper(r),
      order: i,
    };
  });
  const total = rows.length;

  const papers = [...new Map(rows.map((r) => [r.paperKey, r.year])).entries()]
    .sort((a, b) => a[1] - b[1] || a[0].localeCompare(b[0]))
    .map(([k]) => k);
  const chemsPresent = CHEM_ORDER.filter((k) => rows.some((r) => r.chem === k));
  const settingsPresent = SETTING_ORDER.filter((k) => rows.some((r) => r.setting === k));
  const catsPresent = BANDS.filter((b) => rows.some((r) => r.cat === b.key));

  const state = { category: 'all', chem: 'all', setting: 'all', paper: 'all', sort: 'year' as SortKey };

  const titleId = uid('af-title');
  const tipId = uid('af-tip');
  const countId = uid('af-count');

  /* ----- controls ----- */
  const select = (label: string, allText: string, opts: [string, string][]) => {
    const sel = h('select', { id: uid('af-sel') }, h('option', { value: 'all' }, allText));
    opts.forEach(([v, t]) => sel.append(h('option', { value: v }, t)));
    const field = h('label', { class: 'sb-field', for: sel.id }, h('span', { class: 'label' }, label), sel);
    return { sel, field };
  };
  const catCtl = select('Category', 'All categories', catsPresent.map((b) => [b.key, b.key]));
  const chemCtl = select('Chemistry', 'All chemistries', chemsPresent.map((k) => [k, CHEMS[k]]));
  const setCtl = select('Setting', 'All settings', settingsPresent.map((k) => [k, SETTINGS[k]]));
  const paperCtl = select('Paper', 'All papers', papers.map((p) => [p, p]));

  const sortBtns: Record<SortKey, HTMLButtonElement> = {
    year: h('button', { type: 'button', class: 'af-sort-btn', 'aria-pressed': 'true' }, 'Paper year'),
    reduction: h('button', { type: 'button', class: 'af-sort-btn', 'aria-pressed': 'false' }, 'Reduction'),
  };
  const sortField = h(
    'div',
    { class: 'sb-field', role: 'group', 'aria-label': 'Sort within each band' },
    h('span', { class: 'label' }, 'Sort by'),
    h('div', { class: 'af-sort' }, sortBtns.year, sortBtns.reduction),
  );

  const countEl = h('p', { class: 'sb-count', id: countId, 'aria-live': 'polite' });
  const controls = h('div', { class: 'sb-controls' }, catCtl.field, chemCtl.field, setCtl.field, paperCtl.field, sortField, countEl);

  /* ----- chart area ----- */
  const wrap = h('div', { class: 'ch-wrap af-wrap' });
  const list = h('div', { class: 'af-chart', role: 'group', 'aria-labelledby': titleId });
  const titleEl = h(
    'p',
    { class: 'visually-hidden', id: titleId },
    'Reduction on coated surfaces compared with uncoated, one bar per published comparison, grouped into protein, cells, bacteria and friction. Use the up and down arrow keys to move between bars. A table of the same data is below the chart.',
  );
  const makeAxis = () => {
    const el = h('div', { class: 'af-axis', 'aria-hidden': 'true' });
    const ticks = h('span', { class: 'af-axis-ticks' });
    [0, 20, 40, 60, 80, 100].forEach((v) => ticks.append(h('span', { style: `left:${v}%` }, `${v}%`)));
    el.append(h('span', { class: 'af-axis-spacer' }), ticks, h('span', { class: 'af-axis-spacer' }));
    return el;
  };
  const axisTop = makeAxis();
  const axis = makeAxis();
  const axisNote = h('p', { class: 'af-axis-note' }, 'Reduction versus the uncoated surface. The bar is the reduction; the gray track is the uncoated value (100%). ~ means the value is approximate.');
  wrap.append(titleEl, axisTop, list, axis, axisNote);
  const tip = new Tooltip(wrap, tipId);

  /* ----- table view ----- */
  const tableHost = h('div', { class: 'sb-table-wrap' });
  const details = h('details', { class: 'sb-details' }, h('summary', {}, 'View the filtered comparisons as a table'), tableHost);

  root.replaceChildren(controls, wrap, details);
  root.classList.add('is-mounted');

  /* ----- helpers ----- */
  function visible(): Row[] {
    return rows.filter(
      (r) =>
        (state.category === 'all' || r.cat === state.category) &&
        (state.chem === 'all' || r.chem === state.chem) &&
        (state.setting === 'all' || r.setting === state.setting) &&
        (state.paper === 'all' || r.paperKey === state.paper),
    );
  }

  function sorted(items: Row[]): Row[] {
    const out = [...items];
    if (state.sort === 'reduction') out.sort((a, b) => b.pct_reduction - a.pct_reduction || a.order - b.order);
    else out.sort((a, b) => a.year - b.year || a.order - b.order);
    return out;
  }

  const valueText = (r: Row) => `${r.exact ? '' : '~'}${r.pct_reduction}%`;

  function describe(r: Row): string {
    return `${r.assay}, ${r.surface}. ${r.paperKey}, ${r.species_or_setting}. ${formatNum(r.uncoated)} uncoated, ${formatNum(r.coated)} coated ${formatUnit(r.unit)}: ${r.exact ? '' : 'about '}${r.pct_reduction} percent reduction. n ${r.n}. p ${r.p_text ?? 'not stated'}.${r.exact ? '' : ' Approximate.'}`;
  }

  function dl(pairs: [string, string][]): HTMLElement {
    const el = h('dl', { class: 'ch-tip-dl' });
    pairs.forEach(([k, v]) => el.append(h('dt', {}, k), h('dd', {}, v)));
    return el;
  }

  function tipContent(r: Row): Node {
    const pairs: [string, string][] = [
      ['Surface', r.surface],
      ['Setting', r.species_or_setting],
      ['Uncoated', `${formatNum(r.uncoated)} ${formatUnit(r.unit)}`],
      ['Coated', `${formatNum(r.coated)} ${formatUnit(r.unit)}`],
      ['Reduction', `${r.exact ? '' : 'about '}${r.pct_reduction} percent`],
      ['n', r.n],
      ['p', r.p_text ?? 'not stated'],
    ];
    if (r.figure) pairs.push(['Figure', r.figure]);
    return h(
      'div',
      { class: 'ch-tip-body' },
      h('p', { class: 'ch-tip-kicker label' }, `${r.paperKey}, ${r.journal}`),
      h('p', { class: 'ch-tip-title' }, r.assay),
      dl(pairs),
      r.note ? h('p', { class: 'ch-tip-meta' }, r.note) : null,
      r.exact ? null : h('p', { class: 'ch-tip-badge ch-tip-approx' }, 'Approximate'),
      r.in_static_chart ? null : h('p', { class: 'ch-tip-meta' }, 'Not drawn in the static chart.'),
    );
  }

  function renderTable(items: Row[]) {
    const head = ['Paper', 'Category', 'Assay', 'Surface', 'Setting', 'Uncoated', 'Coated', 'Reduction (%)', 'n', 'p', 'Value'];
    const table = h(
      'table',
      { class: 'sb-table' },
      h('caption', { class: 'visually-hidden' }, 'Published comparisons of coated versus uncoated surfaces, matching the current filters'),
      h('thead', {}, h('tr', {}, ...head.map((t) => h('th', { scope: 'col' }, t)))),
      h(
        'tbody',
        {},
        ...items.map((r) =>
          h(
            'tr',
            {},
            h('th', { scope: 'row' }, r.paperKey),
            h('td', {}, r.cat),
            h('td', {}, r.assay),
            h('td', {}, r.surface),
            h('td', {}, r.species_or_setting),
            h('td', { class: 'num' }, `${formatNum(r.uncoated)} ${formatUnit(r.unit)}`),
            h('td', { class: 'num' }, `${formatNum(r.coated)} ${formatUnit(r.unit)}`),
            h('td', { class: 'num' }, String(r.pct_reduction)),
            h('td', {}, r.n),
            h('td', {}, r.p_text ?? 'not stated'),
            h('td', {}, r.exact ? 'Exact' : 'Approximate'),
          ),
        ),
      ),
    );
    tableHost.replaceChildren(items.length ? table : h('p', {}, 'No comparisons match these filters.'));
  }

  /* ----- drawing ----- */
  let current: string | null = null;
  let touchWasActive = false;
  let touchGesture = false;
  let marks: HTMLElement[] = [];

  function setActive(id: string | null, showTip: boolean) {
    current = id;
    marks.forEach((m) => m.classList.toggle('is-active', m.dataset.id === id));
    if (!id) {
      tip.hide();
      return;
    }
    if (showTip) {
      const el = marks.find((m) => m.dataset.id === id);
      const r = rows.find((x) => x.id === id);
      if (el && r) tip.show(tipContent(r), el.querySelector('.af-track') ?? el);
    }
  }

  function bindRow(el: HTMLElement, r: Row, idx: number) {
    el.addEventListener('pointerenter', () => setActive(r.id, true));
    el.addEventListener('pointerleave', () => {
      if (document.activeElement !== el) setActive(null, false);
    });
    el.addEventListener('focus', () => {
      marks.forEach((x) => x.setAttribute('tabindex', x === el ? '0' : '-1'));
      setActive(r.id, true);
    });
    el.addEventListener('blur', () => setActive(null, false));
    el.addEventListener('pointerdown', (e) => {
      touchGesture = (e as PointerEvent).pointerType === 'touch';
      touchWasActive = current === r.id;
    });
    el.addEventListener('click', () => {
      if (touchGesture && !touchWasActive) setActive(r.id, true);
    });
    el.addEventListener('keydown', (e) => {
      let next = -1;
      if (e.key === 'ArrowDown' || e.key === 'ArrowRight') next = Math.min(marks.length - 1, idx + 1);
      else if (e.key === 'ArrowUp' || e.key === 'ArrowLeft') next = Math.max(0, idx - 1);
      else if (e.key === 'Home') next = 0;
      else if (e.key === 'End') next = marks.length - 1;
      else if (e.key === 'Escape') {
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
    countEl.textContent = `${shown.length} of ${total} comparisons`;
    renderTable(sorted(shown));

    const children: HTMLElement[] = [];
    marks = [];
    BANDS.forEach((b) => {
      const inBand = sorted(shown.filter((r) => r.cat === b.key));
      if (!inBand.length) return;
      children.push(h('p', { class: 'af-band' }, `${b.title} `, h('span', { class: 'af-band-n' }, `(${inBand.length})`)));
      inBand.forEach((r) => {
        const idx = marks.length;
        const el = h(
          'div',
          {
            class: 'af-row',
            tabindex: idx === 0 ? 0 : -1,
            role: 'img',
            'aria-label': describe(r),
            'data-id': r.id,
          },
          h(
            'span',
            { class: 'af-label' },
            h('span', { class: 'af-assay' }, r.assay),
            h('span', { class: 'af-meta' }, `${r.paperKey} · ${CHEMS[r.chem]}${r.setting === 'invivo' ? ' · in vivo' : ''}`),
          ),
          h('span', { class: 'af-track' }, h('span', { class: 'af-bar', style: `width:${Math.max(0, Math.min(100, r.pct_reduction))}%` })),
          h('span', { class: 'af-val' }, valueText(r)),
        );
        bindRow(el, r, idx);
        marks.push(el);
        children.push(el);
      });
    });
    if (!children.length) children.push(h('p', { class: 'af-empty' }, 'No comparisons match these filters.'));

    list.replaceChildren(...children);
    axisTop.hidden = !marks.length;
    axis.hidden = !marks.length;
    axisNote.hidden = !marks.length;
    current = null;
    tip.hide();
  }

  function redraw() {
    guard(root, draw);
  }

  catCtl.sel.addEventListener('change', () => {
    state.category = catCtl.sel.value;
    redraw();
  });
  chemCtl.sel.addEventListener('change', () => {
    state.chem = chemCtl.sel.value;
    redraw();
  });
  setCtl.sel.addEventListener('change', () => {
    state.setting = setCtl.sel.value;
    redraw();
  });
  paperCtl.sel.addEventListener('change', () => {
    state.paper = paperCtl.sel.value;
    redraw();
  });
  (Object.keys(sortBtns) as SortKey[]).forEach((k) => {
    sortBtns[k].addEventListener('click', () => {
      state.sort = k;
      (Object.keys(sortBtns) as SortKey[]).forEach((j) => sortBtns[j].setAttribute('aria-pressed', String(j === k)));
      redraw();
    });
  });
  document.addEventListener('pointerdown', (e) => {
    if (!(e.target instanceof Element) || !wrap.contains(e.target)) setActive(null, false);
  });

  draw();
}

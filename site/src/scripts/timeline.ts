/*
  Interactive publication timeline (static fallback: W24_publication_timeline.png).
  Data: W24_publications.json, inlined at build time by the evidence page.
  Rows: papers, dissertations, patents. Hover or focus a marker for the finding;
  click, or press Enter, to open the paper (DOI) or the patent (Google Patents).
*/
import { s, h, uid, guard, watchWidth, Tooltip } from './chart-utils';

export interface PubRecord {
  year: number;
  type: 'paper' | 'dissertation' | 'patent';
  first_author: string;
  title: string;
  journal: string;
  doi: string | null;
  finding: string | null;
  open_access: boolean | string;
}

interface Item extends PubRecord {
  id: string;
  url: string | null;
}

const ROWS: { type: Item['type']; label: string; short: string; single: string }[] = [
  { type: 'paper', label: 'Papers', short: 'Papers', single: 'Paper' },
  { type: 'dissertation', label: 'Dissertations', short: 'Theses', single: 'Dissertation' },
  { type: 'patent', label: 'Patents', short: 'Patents', single: 'Patent' },
];

const STACK = 24;

function linkFor(r: PubRecord): string | null {
  if (r.type === 'paper' && r.doi) return `https://doi.org/${r.doi}`;
  if (r.type === 'patent') {
    const m = r.journal.match(/US\s*([\d,]+)/);
    if (m) return `https://patents.google.com/patent/US${m[1].replace(/,/g, '')}`;
  }
  return null;
}

function heading(r: Item): string {
  return r.type === 'dissertation' ? `${r.first_author}, PhD dissertation` : r.title;
}

function sourceLine(r: Item): string {
  if (r.type === 'paper') return `${r.first_author} et al., ${r.journal}, ${r.year}`;
  if (r.type === 'patent') return r.journal;
  return `University of Iowa, ${r.year}`;
}

export function mount(root: HTMLElement, data: PubRecord[]): void {
  const items: Item[] = data.map((r, i) => ({ ...r, id: `pub-${i}`, url: linkFor(r) }));
  if (items.length === 0) throw new Error('Timeline: no data');

  const minYear = Math.min(2017, ...items.map((r) => r.year));
  const maxYear = Math.max(2026, ...items.map((r) => r.year));
  const years = maxYear - minYear + 1;

  const titleId = uid('tl-title');
  const descId = uid('tl-desc');
  const tipId = uid('tl-tip');

  const wrap = h('div', { class: 'ch-wrap' });
  const svgHost = h('div', { class: 'ch-svg-host' });
  wrap.append(svgHost);
  const tip = new Tooltip(wrap, tipId);

  const list = h('ol', { class: 'tl-list', 'aria-label': 'Publications by year' });
  const listItems = new Map<string, HTMLElement>();
  const sorted = [...items].sort(
    (a, b) => a.year - b.year || ROWS.findIndex((r) => r.type === a.type) - ROWS.findIndex((r) => r.type === b.type),
  );
  for (const r of sorted) {
    const rowDef = ROWS.find((x) => x.type === r.type)!;
    const text = r.url
      ? h('a', { href: r.url, target: '_blank', rel: 'noopener' }, heading(r))
      : h('span', {}, heading(r));
    const li = h(
      'li',
      { 'data-year': r.year, 'data-id': r.id, class: `tl-item tl-${r.type}` },
      h('span', { class: 'tl-year' }, String(r.year)),
      h('span', { class: 'tl-type' }, rowDef.single),
      h('span', { class: 'tl-text' }, text, h('span', { class: 'tl-src' }, ` ${sourceLine(r)}.`)),
    );
    li.addEventListener('pointerenter', () => highlight(r.id, false));
    li.addEventListener('pointerleave', () => unhighlight());
    li.addEventListener('focusin', () => highlight(r.id, false));
    li.addEventListener('focusout', () => unhighlight());
    listItems.set(r.id, li);
    list.append(li);
  }

  root.replaceChildren(wrap, list);
  root.classList.add('is-mounted');

  let active: string | null = null;
  let touchWasActive = false;
  let touchGesture = false;

  function markFor(id: string): Element | null {
    return svgHost.querySelector(`[data-id="${id}"]`);
  }

  function highlight(id: string, withTip: boolean) {
    active = id;
    const it = items.find((x) => x.id === id)!;
    svgHost.querySelectorAll('.tl-mark').forEach((m) => {
      m.classList.toggle('is-active', m.getAttribute('data-id') === id);
      m.classList.toggle('is-year', m.getAttribute('data-year') === String(it.year));
    });
    listItems.forEach((li) => {
      li.classList.toggle('is-active', li.getAttribute('data-id') === id);
      li.classList.toggle('is-year', li.getAttribute('data-year') === String(it.year));
    });
    if (withTip) {
      const m = markFor(id);
      if (m) tip.show(tipContent(it), m.querySelector('.dot') ?? m);
    }
  }

  function unhighlight() {
    active = null;
    svgHost.querySelectorAll('.tl-mark').forEach((m) => m.classList.remove('is-active', 'is-year'));
    listItems.forEach((li) => li.classList.remove('is-active', 'is-year'));
    tip.hide();
  }

  function tipContent(r: Item): Node {
    const rowDef = ROWS.find((x) => x.type === r.type)!;
    return h(
      'div',
      { class: 'ch-tip-body' },
      h('p', { class: 'ch-tip-kicker label' }, `${rowDef.single}, ${r.year}`),
      h('p', { class: 'ch-tip-title' }, heading(r)),
      h('p', { class: 'ch-tip-meta' }, sourceLine(r)),
      r.finding ? h('p', { class: 'ch-tip-text' }, r.finding) : null,
      r.open_access === true && r.type === 'paper' ? h('p', { class: 'ch-tip-badge' }, 'Open access') : null,
      r.url
        ? h(
            'p',
            { class: 'ch-tip-hint' },
            r.type === 'patent'
              ? 'Click or press Enter to open the patent on Google Patents.'
              : 'Click or press Enter to open the paper.',
          )
        : null,
    );
  }

  function open(r: Item) {
    if (r.url) window.open(r.url, '_blank', 'noopener');
  }

  function draw(width: number) {
    const W = Math.max(280, width);
    const narrow = W < 560;
    const left = narrow ? 64 : 124;
    const right = 16;
    const top = 8;
    const bottom = 30;
    const iw = W - left - right;
    const slot = iw / years;
    const xOf = (year: number) => left + slot * (year - minYear + 0.5);

    // Row geometry: a row is as tall as its tallest stack of same-year markers.
    const rowInfo = ROWS.map((row) => {
      const inRow = items.filter((r) => r.type === row.type);
      const counts = new Map<number, number>();
      inRow.forEach((r) => counts.set(r.year, (counts.get(r.year) ?? 0) + 1));
      const maxStack = Math.max(1, ...counts.values());
      return { row, inRow, counts, height: maxStack * STACK + 28 };
    });
    const bodyH = rowInfo.reduce((a, r) => a + r.height, 0);
    const H = top + bodyH + bottom;

    const svg = s('svg', {
      class: 'ch-svg tl-svg',
      role: 'group',
      'aria-labelledby': `${titleId} ${descId}`,
      viewBox: `0 0 ${W} ${H}`,
      width: W,
      height: H,
    });
    svg.append(
      s('title', { id: titleId }, 'Timeline of the public record, 2017 to 2026'),
      s(
        'desc',
        { id: descId },
        `Interactive chart with ${items.length} markers in three rows: papers, dissertations and patents. Each marker can be focused with the keyboard. The same records are listed below the chart.`,
      ),
    );

    // Vertical year guides and labels.
    for (let y = minYear; y <= maxYear; y++) {
      const x = xOf(y);
      svg.append(s('line', { class: 'ch-grid', x1: x, x2: x, y1: top, y2: top + bodyH }));
      const showLabel = !narrow || y % 2 === minYear % 2 || y === maxYear;
      if (showLabel) {
        svg.append(s('text', { class: 'ch-tick', x, y: top + bodyH + 18, 'text-anchor': 'middle' }, String(y)));
      }
    }
    svg.append(s('line', { class: 'ch-axis', x1: left - 8, x2: W - right, y1: top + bodyH, y2: top + bodyH }));

    let y0 = top;
    for (const info of rowInfo) {
      const mid = y0 + info.height / 2;
      svg.append(s('line', { class: 'ch-rowline', x1: 0, x2: W - right, y1: y0 + info.height, y2: y0 + info.height }));
      svg.append(
        s('text', { class: 'ch-rowlabel', x: left - 14, y: mid + 4, 'text-anchor': 'end' }, narrow ? info.row.short : info.row.label),
      );
      const seen = new Map<number, number>();
      for (const r of info.inRow) {
        const k = seen.get(r.year) ?? 0;
        seen.set(r.year, k + 1);
        const stackN = info.counts.get(r.year) ?? 1;
        const cy = mid + (k - (stackN - 1) / 2) * STACK;
        const cx = xOf(r.year);
        const label = `${info.row.single}, ${r.year}: ${heading(r)}. ${r.finding ?? ''}${r.open_access === true && r.type === 'paper' ? ' Open access.' : ''}${r.url ? ' Press Enter to open.' : ''}`;
        const g = s(
          'g',
          {
            class: `tl-mark tl-${r.type}`,
            tabindex: 0,
            role: r.url ? 'link' : 'img',
            'aria-label': label.trim(),
            'data-id': r.id,
            'data-year': r.year,
            transform: `translate(${cx} ${cy})`,
          },
          s('circle', { class: 'hit', r: 13 }),
          s('circle', { class: 'dot', r: 7 }),
        );
        g.addEventListener('pointerenter', () => highlight(r.id, true));
        g.addEventListener('pointerleave', () => {
          if (document.activeElement !== g) unhighlight();
        });
        g.addEventListener('focus', () => highlight(r.id, true));
        g.addEventListener('blur', () => unhighlight());
        g.addEventListener('pointerdown', (e) => {
          touchGesture = (e as PointerEvent).pointerType === 'touch';
          touchWasActive = active === r.id;
        });
        g.addEventListener('click', () => {
          if (touchGesture && !touchWasActive) {
            highlight(r.id, true);
            return;
          }
          open(r);
        });
        g.addEventListener('keydown', (e) => {
          const ke = e as KeyboardEvent;
          if (ke.key === 'Enter') {
            ke.preventDefault();
            open(r);
          } else if (ke.key === 'Escape') {
            unhighlight();
          }
        });
        svg.append(g);
      }
      y0 += info.height;
    }

    svgHost.replaceChildren(svg);
    active = null;
  }

  document.addEventListener('pointerdown', (e) => {
    if (!(e.target instanceof Element) || !wrap.contains(e.target)) unhighlight();
  });

  watchWidth(wrap, (w) => guard(root, () => draw(w)));
}

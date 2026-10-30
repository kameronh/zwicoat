/*
  Small helpers shared by the two interactive charts (timeline.ts, studies.ts).
  Vanilla TypeScript, no libraries. Colors are never written here: every color
  comes from a CSS custom property in tokens.css, applied by charts.css.
*/

const SVG_NS = 'http://www.w3.org/2000/svg';

type Attrs = Record<string, string | number | boolean | null | undefined>;
type Child = Node | string | null | undefined | false;

function applyAttrs(el: Element, attrs: Attrs) {
  for (const [k, v] of Object.entries(attrs)) {
    if (v === null || v === undefined || v === false) continue;
    el.setAttribute(k, v === true ? '' : String(v));
  }
}

function appendChildren(el: Element, children: Child[]) {
  for (const c of children) {
    if (c === null || c === undefined || c === false) continue;
    el.append(typeof c === 'string' ? document.createTextNode(c) : c);
  }
}

/** Create an SVG element. */
export function s(tag: string, attrs: Attrs = {}, ...children: Child[]): SVGElement {
  const el = document.createElementNS(SVG_NS, tag) as SVGElement;
  applyAttrs(el, attrs);
  appendChildren(el, children);
  return el;
}

/** Create an HTML element. */
export function h<K extends keyof HTMLElementTagNameMap>(
  tag: K,
  attrs: Attrs = {},
  ...children: Child[]
): HTMLElementTagNameMap[K] {
  const el = document.createElement(tag);
  applyAttrs(el, attrs);
  appendChildren(el, children);
  return el;
}

let counter = 0;
/** A page-unique id for aria-labelledby and friends. */
export function uid(prefix: string): string {
  counter += 1;
  return `${prefix}-${counter}`;
}

/** Replace the chart with its static PNG. Used when mounting throws. */
export function showFallback(root: HTMLElement): void {
  const src = root.dataset.fallbackSrc;
  if (!src) return;
  const img = h('img', {
    src,
    alt: root.dataset.fallbackAlt ?? '',
    width: root.dataset.fallbackWidth,
    height: root.dataset.fallbackHeight,
    class: 'ch-fallback-img',
    decoding: 'async',
  });
  root.replaceChildren(img);
  root.classList.remove('is-mounted');
  root.classList.add('is-fallback');
}

/** Call fn; if it throws, show the static image and report the error once. */
export function guard(root: HTMLElement, fn: () => void): void {
  try {
    fn();
  } catch (err) {
    console.error('Chart failed, showing the static image instead.', err);
    showFallback(root);
  }
}

/** Call cb with the element's width now and whenever the width changes. */
export function watchWidth(el: HTMLElement, cb: (width: number) => void): void {
  let last = -1;
  const run = () => {
    const w = Math.round(el.getBoundingClientRect().width);
    if (w > 0 && w !== last) {
      last = w;
      cb(w);
    }
  };
  run();
  if (typeof ResizeObserver !== 'undefined') {
    let frame = 0;
    new ResizeObserver(() => {
      cancelAnimationFrame(frame);
      frame = requestAnimationFrame(run);
    }).observe(el);
  } else {
    window.addEventListener('resize', run);
  }
}

/** A tooltip div that sits inside a position:relative container. */
export class Tooltip {
  readonly el: HTMLDivElement;
  private container: HTMLElement;

  constructor(container: HTMLElement, id: string) {
    this.container = container;
    this.el = h('div', { class: 'ch-tip', id, role: 'tooltip', 'aria-hidden': 'true', hidden: true });
    container.append(this.el);
  }

  show(content: Node, anchor: Element): void {
    this.el.replaceChildren(content);
    this.el.hidden = false;
    const c = this.container.getBoundingClientRect();
    const a = anchor.getBoundingClientRect();
    const tw = this.el.offsetWidth;
    const th = this.el.offsetHeight;
    const cx = a.left + a.width / 2 - c.left;
    let left = cx - tw / 2;
    left = Math.max(0, Math.min(left, c.width - tw));
    let top = a.top - c.top - th - 8;
    if (top < 0) top = a.bottom - c.top + 8;
    this.el.style.left = `${Math.round(left)}px`;
    this.el.style.top = `${Math.round(top)}px`;
  }

  hide(): void {
    this.el.hidden = true;
  }
}

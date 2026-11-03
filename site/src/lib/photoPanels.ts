/*
  Static photo panel sets, rendered by PhotoPanels.astro through {{panels:name}} tokens.
  Each set is one row of framed photographs (fewer columns on phones), optional label chips,
  one caption and one credit. Sources and crop boxes: assets-staging/lab-media/round8/README.md.
*/
export interface PanelItem { src: string; alt: string; label?: string; w: number; h: number }
export interface PanelSet {
  items: PanelItem[];
  caption: string;
  credit: string;
  /** Cell aspect ratio, CSS syntax ("1 / 1"). */
  aspect: string;
  /** Columns on phones (520 px and below); desktop shows every item in one row. */
  phoneCols: number;
}

export const PANEL_SETS: Record<string, PanelSet> = {
  // Deck "tissue expander figs", slide 3: two pictures, two panels each, 150 to 300 percent of rated volume.
  expander: {
    items: [
      {
        src: '/images/lab/expander-150pct.jpg',
        alt: 'A 100 cc tissue expander with a blue-dyed coating, inflated to 150 percent of its rated volume, resting on white foam. The fill port shows as a small circle on top and the fill tube runs off to the right.',
        label: '150% of rated volume',
        w: 1151,
        h: 1151,
      },
      {
        src: '/images/lab/expander-200pct.jpg',
        alt: 'The same coated expander at 200 percent of rated volume: a rounder, slightly larger blue dome with the coating unbroken.',
        label: '200%',
        w: 1151,
        h: 1151,
      },
      {
        src: '/images/lab/expander-250pct.jpg',
        alt: 'The same coated expander at 250 percent of rated volume: larger again and a paler blue as the shell stretches, with no tears in the coating.',
        label: '250%',
        w: 1150,
        h: 1149,
      },
      {
        src: '/images/lab/expander-300pct.jpg',
        alt: 'The same coated expander at 300 percent of rated volume: the largest and palest of the four, with the coating still continuous across the shell.',
        label: '300%',
        w: 1150,
        h: 1149,
      },
    ],
    caption:
      'A 100 cc tissue expander inflated to 150, 200, 250 and 300 percent of its rated volume: no tearing of the coating. ZwiCoat internal test, 2026.',
    credit: 'ZwiCoat, 2026',
    aspect: '1 / 1',
    phoneCols: 2,
  },
  // Deck "tissue expander figs", slide 6: three coated PEEK parts on grid paper, no labels on the slide.
  peek: {
    items: [
      {
        src: '/images/lab/peek-coated-01.jpg',
        alt: 'A white PEEK part held in tweezers on grid paper, with a dark blue coating along its upper face and the uncoated white edge below.',
        w: 718,
        h: 539,
      },
      {
        src: '/images/lab/peek-coated-02.jpg',
        alt: 'A small rectangular PEEK piece on grid paper, covered by an even, glossy dark blue coating that reaches its edges.',
        w: 712,
        h: 532,
      },
      {
        src: '/images/lab/peek-coated-03.jpg',
        alt: 'Close-up of a coated PEEK part on grid paper, its face a bright, smooth blue, with a tweezer tip touching the lower right.',
        w: 707,
        h: 533,
      },
    ],
    caption: 'Coated PEEK parts, dyed blue so the film is visible. ZwiCoat, 2026.',
    credit: 'ZwiCoat, 2026',
    aspect: '4 / 3',
    phoneCols: 1,
  },
};

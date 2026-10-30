import { defineCollection } from 'astro:content';
import { glob } from 'astro/loaders';
import { z } from 'astro/zod';

const applications = defineCollection({
  loader: glob({ pattern: '*.md', base: './src/content/applications' }),
  schema: z.object({
    title: z.string(),
    slug: z.string(),
    order: z.number(),
    standfirst: z.string(),
    devices: z.string(),
    substrates: z.string(),
    thickness: z.string(),
    sterilization: z.string(),
    regulatory: z.string(),
    evidence: z.string(),
    heroFigure: z.string(),
    figures: z.array(
      z.object({
        name: z.string(),
        caption: z.string(),
        source: z.string(),
        alt: z.string(),
      }),
    ),
    sources: z.array(z.string()),
    cardStat: z.string(),
    cardStatLabel: z.string(),
  }),
});

export const collections = { applications };

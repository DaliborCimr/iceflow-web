import { defineCollection } from 'astro:content';
import { glob } from 'astro/loaders';
import { z } from 'astro/zod';

// Entries live in <collection>/<lang>/<slug>.md, so an entry id is "<lang>/<slug>".
// English is required; other languages fall back to it until translated.

const legal = defineCollection({
  loader: glob({ pattern: '**/*.md', base: './src/content/legal' }),
  schema: z.object({
    title: z.string(),
    updated: z.coerce.date(),
  }),
});

const guide = defineCollection({
  loader: glob({ pattern: '**/*.md', base: './src/content/guide' }),
  schema: z.object({
    title: z.string(),
    description: z.string(),
    order: z.number().default(100),
  }),
});

// The project story: lead, stats and milestones in frontmatter so the page can lay
// them out; the Markdown body is the closing section under the timeline.
const story = defineCollection({
  loader: glob({ pattern: '**/*.md', base: './src/content/story' }),
  schema: z.object({
    title: z.string(),
    description: z.string(),
    lead: z.string(),
    stats: z.array(z.object({ value: z.string(), label: z.string() })),
    timelineTitle: z.string(),
    milestones: z.array(
      z.object({
        date: z.string(),
        phase: z.enum(['idea', 'engine', 'server', 'mobile', 'animation', 'launch']),
        phaseLabel: z.string(),
        title: z.string(),
        text: z.string(),
      }),
    ),
    closingTitle: z.string(),
  }),
});

export const collections = { legal, guide, story };

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
  loader: glob({ pattern: '**/*.{md,mdx}', base: './src/content/guide' }),
  schema: z.object({
    title: z.string(),
    description: z.string(),
    // Sidebar group (labels in ui.ts 'guide.group.*') and position within the whole guide.
    group: z.enum(['basics', 'ice', 'club', 'more']),
    order: z.number().default(100),
    // Material Symbols Rounded name, matching the app's icon for that section.
    icon: z.string(),
  }),
});

// The project story. The Markdown body is the narrative; everything the page lays out
// as cards (stats, game areas, timeline, closing notes) lives in frontmatter.
const story = defineCollection({
  loader: glob({ pattern: '**/*.md', base: './src/content/story' }),
  schema: z.object({
    title: z.string(),
    description: z.string(),
    lead: z.string(),
    stats: z.array(z.object({ value: z.string(), label: z.string() })),
    storyTitle: z.string(),
    areasTitle: z.string(),
    areasIntro: z.string(),
    areas: z.array(z.object({ title: z.string(), text: z.string(), facts: z.array(z.string()) })),
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
    notes: z.array(z.object({ title: z.string(), paragraphs: z.array(z.string()) })),
  }),
});

export const collections = { legal, guide, story };

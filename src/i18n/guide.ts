import { getLocalizedCollection } from './content';
import type { Locale } from './ui';

export const guideGroups = ['basics', 'ice', 'club', 'more'] as const;
export type GuideGroup = (typeof guideGroups)[number];

// Every guide article in reading order, resolved to [lang] (English where not translated).
export async function getGuide(lang: Locale) {
  const items = await getLocalizedCollection('guide', lang);
  return items.sort(
    (a, b) =>
      guideGroups.indexOf(a.entry.data.group) - guideGroups.indexOf(b.entry.data.group) ||
      a.entry.data.order - b.entry.data.order,
  );
}

export type GuideItem = Awaited<ReturnType<typeof getGuide>>[number];

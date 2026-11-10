import { getCollection, getEntry, type CollectionEntry } from 'astro:content';
import { defaultLocale, type Locale } from './ui';

type Localized<C extends 'legal' | 'guide'> = {
  entry: CollectionEntry<C>;
  slug: string;
  // True when the requested language is missing and English is shown instead.
  isFallback: boolean;
};

function split(id: string) {
  const [lang, ...rest] = id.split('/');
  return { lang, slug: rest.join('/') };
}

export async function getLocalizedEntry<C extends 'legal' | 'guide'>(
  collection: C,
  slug: string,
  lang: Locale,
): Promise<Localized<C>> {
  // Check ids first: getEntry warns on every missing translation.
  const ids = new Set((await getCollection(collection)).map((e) => e.id));
  const own = ids.has(`${lang}/${slug}`) ? await getEntry(collection, `${lang}/${slug}`) : undefined;
  if (own) return { entry: own as CollectionEntry<C>, slug, isFallback: false };
  const fallback = await getEntry(collection, `${defaultLocale}/${slug}`);
  if (!fallback) throw new Error(`Missing ${defaultLocale}/${slug} in "${collection}"`);
  return { entry: fallback as CollectionEntry<C>, slug, isFallback: lang !== defaultLocale };
}

// Every English slug in the collection, resolved to the requested language.
export async function getLocalizedCollection<C extends 'legal' | 'guide'>(
  collection: C,
  lang: Locale,
): Promise<Localized<C>[]> {
  const all = await getCollection(collection);
  const slugs = all.map((e) => split(e.id)).filter((p) => p.lang === defaultLocale).map((p) => p.slug);
  return Promise.all(slugs.map((slug) => getLocalizedEntry(collection, slug, lang)));
}

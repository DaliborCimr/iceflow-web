// The site may be served under a sub-path (GitHub Pages: /iceflow-web/), set at build time by
// BASE_PATH - see astro.config.ts. Every root-relative link goes through here.
const base = import.meta.env.BASE_URL.replace(/\/$/, '');

/** A root-relative path ("/en/guide/") with the site's base path in front. */
export const url = (path: string): string => `${base}${path}`;

/** The pathname without the base path, as the routes see it. */
export const stripBase = (pathname: string): string =>
  base && pathname.startsWith(base) ? pathname.slice(base.length) || '/' : pathname;

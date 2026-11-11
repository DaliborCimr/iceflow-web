import { defineConfig } from 'astro/config';
import mdx from '@astrojs/mdx';
import { defaultLocale, locales } from './src/i18n/locales';

export default defineConfig({
  integrations: [mdx()],
  // Both come from the build environment: the GitHub Pages workflow serves the site under
  // /iceflow-web/; a local build and the future Cloudflare domain serve it from the root.
  site: process.env.SITE_URL || undefined,
  base: process.env.BASE_PATH || '/',
  i18n: {
    locales: [...locales],
    defaultLocale,
    routing: {
      prefixDefaultLocale: true,
      redirectToDefaultLocale: false,
    },
  },
});

import { defineConfig } from 'astro/config';
import { defaultLocale, locales } from './src/i18n/locales';

export default defineConfig({
  // Set once the Cloudflare domain exists (canonical and hreflang URLs).
  // site: 'https://iceflow.example',
  i18n: {
    locales: [...locales],
    defaultLocale,
    routing: {
      prefixDefaultLocale: true,
      redirectToDefaultLocale: false,
    },
  },
});

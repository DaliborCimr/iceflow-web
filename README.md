# iceflow-web

Static informational website for IceFlow, an ice hockey management mobile game:
game description, privacy policy, terms of service and a game guide explaining
server-side mechanics the in-app help does not cover. Built with [Astro](https://astro.build).

## Commands

| Command           | What it does                                  |
| ----------------- | --------------------------------------------- |
| `npm install`     | Install dependencies                          |
| `npm run dev`     | Dev server at http://localhost:4321           |
| `npm run build`   | Type-check (`astro check`) and build `dist/`  |
| `npm run preview` | Serve the built `dist/` locally               |

## Structure

```
src/
  i18n/locales.ts        # the 10 languages (same as the mobile app)
  i18n/ui.ts             # UI strings; English is the source, others must have every key
  i18n/content.ts        # per-language content lookup with English fallback
  content/legal/<lang>/  # privacy.md, terms.md
  content/guide/<lang>/  # game guide articles (<slug>.md)
  layouts/Base.astro     # header, language switcher, footer
  pages/index.astro      # / -> saved or browser language, else /en/
  pages/[lang]/...       # every page exists under /<lang>/
  assets/branding/       # logo and wordmark (optimized at build time)
```

## Adding content

- Translation of a legal page or article: add `src/content/<collection>/<lang>/<slug>.md`
  with the same slug as the English file. Until it exists, the English text is shown with a notice.
- New guide article: `src/content/guide/en/<slug>.md` with `title`, `description` and optional `order`.
- New UI string: add the key to `en` in `src/i18n/ui.ts`; `astro check` fails until every language has it.

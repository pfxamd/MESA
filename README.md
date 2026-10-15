# MESA — The Everyday Table

An original, fully static culinary-editorial website for pfxamd, featuring 36 original commissioned concept photographs, 12 original editorial recipe drafts, 4 long-form stories and a functional ingredient-matching kitchen.

**Edition:** Volume 01 — From Market to Table. All recipes remain **untested editorial drafts**, and the publication and photographs are fictional demonstrations. No physical products, real marketplace reporting or endorsements are represented.

## What's included

- Editorial Home, Recipes, The Kitchen, Stories and About.
- 12 dedicated recipe articles with ingredients, methods, portions scaling, checkable ingredients, cooking mode and optional timers.
- 4 authored culinary editorial stories with their own layouts and photography.
- Ingredient matching uses authored ingredient IDs (not vague string matching), shows missing ingredients transparently and assumes only water/salt/pepper as declared pantry staples.
- Locally bundled WebP images under `public/assets/images/` and published images under `docs/assets/images/`.
- Responsive styling, native HTML landmarks, keyboard-usable interactions, reduced motion and core written content visible without JavaScript.
- No accounts, purchases, personal-data transmission, external runtime framework or unnecessary background requests. Google-hosted fonts are optional; system fonts provide fallback.
- Designed & developed by [pfxamd](https://www.pfxamd.com).

## Build and preview

Requires Python 3.10+ (standard library only):

```sh
python3 build.py
python3 serve.py
```

Open `http://127.0.0.1:8075/MESA/`.

Run focused checks:

```sh
python3 tests/check_site.py
node --check assets/site.js
```

`content/recipes.json` and `content/stories.json` are the editable content sources. `data/images.json` records actual asset provenance and original dimensions. `assets/site.css` and `assets/site.js` are the single site-wide visual and interactive sources. `build.py` writes pre-rendered pages to `docs/` with all required images and assets.

To deploy at a different subpath, set `MESA_BASE` before running the build. Default is `/MESA`.

## Publishing

The output in `docs/` is configured for GitHub Pages under `https://pfxamd.github.io/MESA/` when the repository's Pages source is set to the `main` branch and `/docs` folder. Publishing is a separate action; no automated GitHub Actions workflow is installed in this package.

## Scope and integrity

- The cookbook is a design and editorial demonstration. Recipes have **not been kitchen-tested** and require real kitchen and food-safety review before being promoted as verified cooking guidance.
- Chicken recipes require the safe 74°C / 165°F internal-temperature check. Photography of raw preparation is not a cooked-dish serving suggestion.
- All 36 supplied image files are concept imagery. No additional image generation was performed for the site implementation.
- The source media's native dimensions are preserved. The advertised 1600×2000 or 2400×1600 sizes were production targets, not claims about delivered source resolution.
- A site build does not authorize publication to a live hosting service.

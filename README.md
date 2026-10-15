# MESA — The Everyday Table

A fictional independent culinary publication and interactive kitchen. Original editorial website concept by pfxamd.

**Volume 01: From Market to Table**
**Status: Pre-production. No website implementation or images have been produced in this repository.**

## Creative promise

An expressive, photography-led food journal that makes cooking feel tactile, curious and approachable. Visitors can read, browse complete recipes, select ingredients they have, identify viable dishes, and cook with clear step-by-step guidance. It is a publication first, not a SaaS dashboard, generic recipe index, ecommerce storefront or restaurant site.

### Positioning

- Language: English.
- Audience: curious home cooks, design-conscious readers and people exploring seasonal, ingredient-led food.
- Editorial theme: ordinary ingredients, vivid colour, surprising combinations and the pleasure of sharing a table.
- Brand voice: sensory, concise, informed, unpretentious, lightly playful.
- Site identity: MESA / The Everyday Table.
- Fictional demonstration: no false claims of a real publishing company, real contributors, tested recipes, physical kitchen, professional chef endorsements, verified nutrition, third-party reviews or public user content.
- Credits: "Designed & developed by pfxamd" with a real outbound link to https://www.pfxamd.com.

## Art direction

### Palette proposal

| Role | Hex | Treatment |
| --- | --- | --- |
| Tomato / statement | #E9472F | punchy editorial red |
| Saffron / contrast | #F6CA56 | flashes of yellow |
| Herb / grounding | #32634A | deeper green |
| Paper / breathing room | #FFF7E8 | warm light surface |
| Ink / typography | #241D19 | warm almost-black |

Type direction: authored MESA wordmark, bold expressive grotesque for large headlines, readable sans for body copy, occasional contrasting serif for quotes and editorial emphasis. Final typeface selection follows visual testing; do not assume stock brand typography.

Art direction: print-magazine energy, asymmetric editorial layouts, deliberate cropping and visual rhythm; substantial negative space where needed. Never reuse the same generic component grid for each section. Recipe function remains accessible and legible.

Photographic set: believable food, rich natural colour, physical ingredients, real textures, direct soft daylight and occasional hard sun, tactile off-white/butter-yellow paper, washed terracotta, cobalt accents in limited props, olive-green herbs and controlled red cloth. Carefully directed but imperfect enough to feel edible; no levitating ingredients, CGI shine, fake letters, slogans, product packaging, logos, stereotypical apron portraiture or unrelated decorative food. Hands may appear when purposeful. Maintain one credible magazine world, but intentionally vary lenses, heights, table settings and lighting.

## Navigation & page architecture

1. **/** Home: immersive editorial hero; latest volume; featured recipe; kitchen introduction; four story destinations; independent visual compositions.
2. **/recipes/** Recipe discovery: all twelve recipes; ingredient/category discovery and editorial grouping, not filter-heavy SaaS panels.
3. **/recipes/[slug]/** Twelve complete recipe pages: introduction, hero photo, serving controls, ingredients, steps, equipment, times and relevant process imagery.
4. **/kitchen/** Interactive pantry: select a finite set of normalized ingredients, show recipe matches/missing ingredients, open recipe, cooking mode with step-by-step progression, adjustable yield and optional in-page timers.
5. **/stories/** Four stories displayed as an editorial index.
6. **/stories/[slug]/** Four individually composed feature articles.
7. **/about/** Publication premise, visual philosophy, fiction disclaimer and site credits.
8. Custom not-found page.

Home is not a second copy of Recipes. The Kitchen is not a separate decorative app: every suggested dish must map to a real published recipe.

## Volume 01 — twelve recipe concepts

These are editorial subjects, **not yet tested or verified cooking instructions**. Final content must have real measured quantities, timings, coherent steps and appropriate safety information before release. Avoid invented ratings, nutrition or claims of authenticity.

| ID | Working title | Slug | Distinguishing ingredients / appearance | Section |
| --- | --- | --- | --- | --- |
| R01 | Charred Tomato Toast | charred-tomato-toast | blistered tomatoes, thick grilled bread, herbs; juicy red and toasted edges | Small Plates |
| R02 | Lemon & Herb Butter Beans | lemon-herb-butter-beans | soft white beans, lemon, parsley, olive oil; cream and green | Small Plates |
| R03 | Crispy Potato Salad | crispy-potato-salad | smashed golden potatoes, yogurt, mustard, dill; warm yellow and fresh green | Small Plates |
| R04 | Carrot, Orange & Fennel Salad | carrot-orange-fennel-salad | shaved carrot, orange segments, fennel; orange ribbons on pale plate | Small Plates |
| R05 | Roasted Pepper & Tomato Pasta | roasted-pepper-tomato-pasta | tomato, red pepper, garlic, olive oil, pasta, basil; glossy red sauce | The Main Table |
| R06 | Harissa Chickpea Skillet | harissa-chickpea-skillet | chickpeas, harissa, tomato, leafy greens; terracotta skillet | The Main Table |
| R07 | Crispy Aubergine & Herbed Yogurt | crispy-aubergine-herbed-yogurt | browned aubergine, thick herbed yogurt, toasted seeds; purple and cream | The Main Table |
| R08 | Golden Roast Chicken & Lemon | golden-roast-chicken-lemon | roast chicken, wedges of lemon, garlic, thyme; golden Sunday-table hero | The Main Table |
| R09 | Tomato & Saffron Rice | tomato-saffron-rice | saffron rice, roasted tomato, herbs; strong golden red contrast | The Main Table |
| R10 | Orange Olive Oil Cake | orange-olive-oil-cake | golden cake, orange zest, citrus slices; sunny baked texture | Something Sweet |
| R11 | Honey-Roasted Pears | honey-roasted-pears | caramelized pears, yogurt, honey, toasted nuts; amber | Something Sweet |
| R12 | Dark Chocolate Tahini Cookies | chocolate-tahini-cookies | cracked cocoa cookies, sesame/tahini; deep chocolate | Something Sweet |

Each recipe should be photographed as a *different* dish with composition matching ingredients and instructions. No photo substitutes, text-over-food, or ingredient contradictions.

## Four original editorial story outlines

- **S01 — The Market Before Noon** (/stories/the-market-before-noon/): a walking rhythm of choosing, touching and carrying everyday produce; 2 photos (E01, E02).
- **S02 — An Ode to the Lemon** (/stories/an-ode-to-the-lemon/): brightness, zest, acidity and visual character; 2 photos (E03, E04).
- **S03 — The Good Pantry** (/stories/the-good-pantry/): a smaller, more useful core of staples, oils, pulses and grains; 1 photo (E05).
- **S04 — The Table After** (/stories/the-table-after/): conviviality, crumbs, last light and lingering conversation; 1 photo (E06).

Stories should have written introductions, several short sections and factual food claims checked before release. No fabricated interviews, quotations, origins or photojournalism claims.

## Image-production bible — exactly 36 separate assets

The image list is intentionally exhaustive. A numbered image must be generated as a **single independent file**, never a contact sheet, tiled composite or multiple viewpoints in one frame. Each asset carries one assigned purpose; no repetitive photographs that accidentally create a second version of another entry.

### A. Brand & Opening — 6 images

| ID and filename | Ratio | Directed visual |
| --- | --- | --- |
| 01 — 01-opening-shared-table.png | 16:9 | Generous overhead lunch table with several different plates, striking red tomato dish, bread and citrus; lively negative space on left for programmed headline; not a recipe-detail shot |
| 02 — 02-tomato-material-study.png | 4:5 | Tight artistic still-life of split heirloom tomatoes with seeds and wet flesh on matte warm paper; near-macro, no plated meal |
| 03 — 03-citrus-colour-study.png | 4:5 | Halved lemon and orange with visible pulp, angular hard sunlight and pale yellow paper, graphic shadows |
| 04 — 04-bread-and-crumb.png | 3:2 | Torn artisan loaf on a neutral sheet with visible crumb, scattered crumbs and diagonal afternoon light, tactile still life |
| 05 — 05-hands-and-herbs.png | 3:2 | Overhead editorial moment of hands lifting rinsed fresh herbs from a shallow steel bowl, genuine movement, not a dish |
| 06 — 06-after-lunch-table.png | 16:9 | Quiet almost-empty communal table, small bowl, folded coral napkin and late sunshine; emotional closing image, distinct from crowded hero |

### B. Finished Dishes — 12 images

| ID and filename | Ratio | Directed visual |
| --- | --- | --- |
| 07 — 07-charred-tomato-toast.png | 4:5 | R01: two thick diagonal grilled toast slices, blistered red tomatoes, visible olive oil; tight 3/4 angle |
| 08 — 08-lemon-herb-butter-beans.png | 4:5 | R02: shallow cream ceramic bowl, white beans glistening with lemon dressing, leafy herbs; oblique daylight |
| 09 — 09-crispy-potato-salad.png | 4:5 | R03: broken golden roast potatoes with yogurt and dill, top-down on pale butter-yellow surface |
| 10 — 10-carrot-orange-fennel-salad.png | 4:5 | R04: sculptural orange carrot ribbons and juicy orange segments, fine fennel on broad matte plate, overhead |
| 11 — 11-roasted-pepper-tomato-pasta.png | 4:5 | R05: ribbon pasta wrapped in glossy roasted pepper/tomato sauce with basil, blue ceramic plate for contrast, close 3/4 |
| 12 — 12-harissa-chickpea-skillet.png | 4:5 | R06: warmly spiced chickpea skillet with tomato and greens, dark pan on warm surface, slightly wider 3/4 |
| 13 — 13-crispy-aubergine-yogurt.png | 4:5 | R07: burnished aubergine quarters over swirled yogurt, scattered toasted seeds and herbs, sharp side lighting |
| 14 — 14-golden-roast-chicken.png | 3:2 | R08: whole golden roast chicken in heavy shallow roasting tray with lemon and thyme, generous family-table setting |
| 15 — 15-tomato-saffron-rice.png | 4:5 | R09: broad enamel plate of saffron rice, jewel-red roast tomatoes and green herbs, overhead with strong pattern |
| 16 — 16-orange-olive-oil-cake.png | 4:5 | R10: small golden cake with one slice cut, moist crumb visible, thin orange curls, warm directional light |
| 17 — 17-honey-roasted-pears.png | 4:5 | R11: two browned pear halves with glossy honey and yogurt, amber-on-cream styling, low 3/4 angle |
| 18 — 18-chocolate-tahini-cookies.png | 4:5 | R12: irregular dark cracked cookies with tahini/sesame details on crumpled paper, intimate macro |

### C. Ingredients & Process — 12 images

| ID and filename | Ratio | Directed visual |
| --- | --- | --- |
| 19 — 19-char-tomatoes.png | 3:2 | R01: tomato skins blistering in hot skillet; overhead action, no finished toast |
| 20 — 20-dress-butter-beans.png | 3:2 | R02: close hands pouring lemon dressing onto beans and chopped parsley in ceramic bowl |
| 21 — 21-crush-potatoes.png | 3:2 | R03: hand using glass to gently smash parboiled potatoes on oiled baking tray before roasting |
| 22 — 22-shave-vegetables.png | 3:2 | R04: mandoline/peeler producing long carrots and fennel shavings on cutting board, distinct shapes |
| 23 — 23-make-roasted-sauce.png | 3:2 | R05: tray of blistered red peppers, tomatoes and garlic just out of oven, before blending |
| 24 — 24-build-chickpea-skillet.png | 3:2 | R06: spoon folding cooked chickpeas into vivid reddish skillet sauce |
| 25 — 25-sear-aubergine.png | 3:2 | R07: sliced eggplant caramelizing cut-side-down in well-used pan, heat and authentic texture |
| 26 — 26-season-roast-chicken.png | 3:2 | R08: hands adding fresh thyme and lemon to an uncooked chicken in tray, raw-food prep separate from serving |
| 27 — 27-fold-saffron-rice.png | 3:2 | R09: close wooden spoon folding yellow saffron rice in saucepan; steam and distinct grain texture |
| 28 — 28-mix-orange-cake.png | 3:2 | R10: grated zest going into cake batter in plain mixing bowl, overhead close |
| 29 — 29-glaze-roasted-pears.png | 3:2 | R11: pastry brush or spoon applying honey glaze to pear halves in baking dish, before serving |
| 30 — 30-shape-chocolate-cookies.png | 3:2 | R12: raw chocolate/tahini cookie dough portions arranged on parchment with hand in frame |

### D. Editorial Stories — 6 images

| ID and filename | Ratio | Directed visual |
| --- | --- | --- |
| 31 — 31-market-produce-crates.png | 3:2 | S01: close produce-market still life, layered crates of tomatoes, herbs and aubergines; believable documentary-style setting with no identifiable real shop |
| 32 — 32-selecting-produce.png | 4:5 | S01: close anonymous hands choosing ripe produce from market crate, tactile bags and natural sun |
| 33 — 33-lemon-branch-still-life.png | 3:2 | S02: lemons with waxy leaves on sunlit terracotta surface, sculptural physical shadows |
| 34 — 34-zest-lemon.png | 4:5 | S02: hand zesting lemon over small dark bowl; tiny yellow flecks and specific tool in focus |
| 35 — 35-everyday-pantry.png | 3:2 | S03: quiet shelf-level grouping of beans, dried pasta, olive oil, salt and grains in unbranded glass jars |
| 36 — 36-clearing-the-table.png | 3:2 | S04: anonymous hands lifting used small plates from warmly lit shared table; crumbs and empty glasses, not a plated meal |

### Photography production rules

- For every image, freeze subject, exact ingredients, framing, props, light, intended route, image ratio and negative constraints before generation.
- Do not duplicate the opening table as the closing table, or editorial citrus as recipe garnish. Do not repeat camera arrangement across adjacent finished dishes.
- For consistency, define a single palette, physical tabletop vocabulary and material palette, but permit varying shadows and light by story.
- Keep words, logos, UI, graphic borders and typography OUT of images; overlay real text in browser only.
- Do not silently add ingredients absent from final recipes. Review culinary plausibility.
- All 36 assets must be checked individually, renamed and mapped; generated assets are conceptual food photography and must not be described as documentary photos of real restaurants/markets.
- Use web-optimized derivatives for site delivery; preserve best originals. Do not stretch or claim unavailable exact export dimensions.

## Interactivity contract

**Pantry matching:** normalize ingredient IDs (not display strings) and use declared recipe ingredient lists. Match recipes by available ingredients, display missing items truthfully, allow removal and resetting. Main labels should be readable without relying on colour alone. Include useful empty states.

**Recipe reading:** ingredient quantities support predictable serving scaling; note non-linear seasoning and oven settings if required. User can check ingredients off without permanent accounts; cooking mode exposes one clear step at a time and optional timers. Include keyboard operation, focus treatment and reduced-motion behavior. Time calculations and ingredient amounts must come from authored recipe records, not placeholder estimates.

**Editorial functionality:** discover 12 dishes and 4 stories via real working routes; navigation, previous/next relationships and no JavaScript reading fallback. No fake search, ratings, accounts, submissions or purchase actions.

## Content data model (implementation target)

Recipe record: slug, title, deck, category, tags, heroImage, processImage, servesBase, prepMinutes, cookMinutes, ingredient groups (id, amount, unit, displayName, optional notes), equipment, ordered instructions, safety/notes and relevant links. Story record: slug, title, deck, lead media, body sections and media placements. All visible cooking details and optional Recipe structured data should be derived from one coherent source of truth.

For Recipe structured data, use actual authored ingredients and steps, distinguish required from recommended properties, avoid invented author reviews/nutrition and test markup against Google's published guidance:
https://developers.google.com/search/docs/appearance/structured-data/recipe

## Proposed implementation

- Astro + TypeScript, static prerendered pages and shared content collections.
- Custom authored CSS; no generic SaaS interface kit.
- Small targeted browser-native TypeScript components for pantry, serving controls and step/timer logic.
- GSAP only when specific editorial motion improves the experience, progressively enhanced; essential content remains available without JS.
- Real responsive images with source dimensions and loading priorities. Do not lazy-load the first hero image.
- Keyboard-accessible controls and reduced motion. Mobile is a separate, carefully composed editorial layout rather than a scaled desktop grid.
- Build and test locally; deploy to GitHub Pages only after explicit approval. Keep runtime lightweight and avoid unnecessary workflow runs.

## Production sequence / acceptance gates

1. **This pre-production brief:** approve story/recipe direction, image assignments and editorial brand world.
2. **Recipe editorial:** develop and review all measured recipes and instructions; align photographs and final ingredients.
3. **Photography:** author four independent detailed batches (6, 12, 12, 6) from this manifest; review each file against its role before coding against it.
4. **Design & development:** build unique pages and the functional kitchen; no ornamental fake controls.
5. **Validation:** routes, missing ingredients, serving adjustment, cooking flow, image mapping, mobile/desktop, accessibility, no-JS content and performance.
6. **Publishing:** GitHub Pages only when explicitly authorized.

This document locks the working production direction but does not pretend that recipe testing, assets, code or launch have happened.

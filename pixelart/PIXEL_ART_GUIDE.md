# PIXEL_ART_GUIDE.md: pixel sprite creation guide

Everything learned while drawing the `pixelart/` set: the workflow, the
config format reference, the style baseline, and the full list of lessons
(each traced to the sprite that taught it). AGENTS.md carries only the
summary; this file is the source of truth for how sprites are made and
reviewed.

## 1. What the pixel set is

A second, opt-in icon set for zukan: natively small pixel art (height <= 24,
width unlimited; current sprites are 28-36 wide), side view facing left,
near-black outline, flat fills, transparent background. One config per
monster. Contrast with `icons/`, which holds screenshot-derived game card
icons at 48 x 48; those turn muddy at terminal sizes, the pixel set stays
crisp because it is drawn at display resolution.

- Configs are the source of truth. The PNGs are deterministic products.
- Release output (`--out`) emits each sprite at its NATIVE size (never
  scaled, never padded), named by slug, into `icons-pixelart/`.
- Coverage is intentionally partial: zukan falls back to `icons/` per
  uncovered monster, so a sparse set is still usable.

## 2. Studio layout

```
pixelart/
├── spritekit.py        # engine: spans → auto-stroke → flat fills
├── build_sprites.py    # driver: dev previews / --out / --check
├── sprites/<slug>.py   # one config per monster (hand-edited source)
├── README.md           # short usage doc
├── PIXEL_ART_GUIDE.md  # this file
├── roster_preview.png  # numbered review board (regenerated every build)
├── contact_sheet.png   # plain review board (regenerated every build)
└── *_sprite*.png       # dev previews (gitignored, local only)

icons-pixelart/         # release output (gitignored, built by release.yml)
```

## 3. Config format reference

A config is a single dict:

```python
CONFIG = {
    "name": "rathalos",          # must be a slug in data/monsters.json
    "size": (36, 24),            # (width, height); height <= 24 enforced
    "compare_to": "../icons/mh4u/rathalos.png",  # optional review reference
    "palette": {".": (0,0,0,0), "K": ..., "R": ..., ...},  # char -> RGBA
    "base": "R",                 # char every silhouette pixel starts as
    "spans": {                   # silhouette: row -> [(col_start, col_end)]
        1: [(3, 3), (19, 21)],
        ...
    },
    "fills": [                   # ordered ops, executed after the stroke
        ("runs", [(r, c0, c1), ...], "ch"),          # recolor (frm = base)
        ("runs", [(r, c0, c1), ...], "ch", "frm"),   # recolor from frm
        ("put", row, col, "chars"),                  # repaint a char run
    ],
}
```

Engine semantics (`spritekit.py`):

- `_mask` builds the silhouette from spans (`#` cells).
- `_stroke` outlines it: every transparent cell touching the mask becomes
  `K`. A 1px transparent channel between two parts fills in from both
  sides, which is what draws the black separation line between head, wing,
  body and tail; author parts 1px apart and the outline does the rest.
- Fills execute in order; each `runs` op repaints only cells currently
  matching `frm` (default = base). Fill ORDER is part of the design:
  material zones first, then details painted over them.
- `put` ops must land on cells that exist in the final silhouette
  (transparent-cell puts abort the build). They can overwrite `K`; that is
  how fangs land inside the outlined mouth gap.

Derived (subspecies) configs:

```python
from great_jaggi import CONFIG as _base

CONFIG = dict(_base)
CONFIG["name"] = "great-wroggi"
CONFIG["palette"] = dict(_base["palette"])
CONFIG["palette"]["O"] = (205, 105, 105, 255)  # the parent's base char
CONFIG["fills"] = list(_base["fills"]) + [...]  # signature additions
```

Structural patches merge spans explicitly (never assign a partial dict over
the base spans; that wipes every other row):

```python
CONFIG["spans"] = {**_base["spans"], 3: [(3, 5), (15, 21)]}
```

## 4. Creation workflow

1. **Pick the slug** from `data/monsters.json` (grep it; the config name
   must match exactly: `azure-rathalos`, not `rathalos-azure`).
2. **Copy the closest existing config** as the starting point. Current
   archetypes: `rathalos` (flying wyvern + fan wing), `zinogre` (hunched
   quadruped + shell plates), `tigrex` (bulky runner + stripes),
   `great_jaggi` (bird-wyvern leader), `kulu_ya_ku` (biped bird),
   `anjanath` (brute wyvern + sail), `vaal_hazak` (hunched drooper),
   `kirin` (horse), `namielle`/`xenojiiva` (front-symmetric floaters),
   `somnacanth` (sleek swimmer + broad tail fan), `hermitaur` (crab:
   shell dome, face patch, low-hanging pincer with an open slot,
   pointed legs).
3. **Author the silhouette rows**; this is the actual drawing. Follow the
   style baseline in section 5. Side view facing left, subject fully inside
   the frame with a 1px margin, parts 1px apart where they must separate.
4. **Build and look**: `python3 build_sprites.py <name>`; regenerate the
   preview and eyeball it at the terminal. Iterate 2-4 rounds; almost every
   first draft needs them.
5. **Fills** in this order: base (automatic) → material zones (membrane,
   plates, belly) → shading → pattern dashes → face details (eyes, fangs,
   claws) last.
6. **Emit**: `python3 build_sprites.py --out ../icons-pixelart` and commit.
7. **Verify**: `--check ../icons-pixelart` byte-compares against the
   configs; the pixelart-check workflow runs the same in CI.

## 5. Style baseline

Distilled from the 58-sprite review rounds. Every rule below exists because
a draft violated it and was rejected.

### 5.1 View and pose

- Side view facing left is the standard. The 3/4-view experiment (2026-09)
  failed: symmetric formula faces (two equal dot eyes + straight mouth band)
  read 呆 at this scale, and bodies degenerated into head-vs-wing
  diagonals. Reviving 3/4 needs true asymmetric face construction
  (foreshortened snout, near/far eye asymmetry), not a template.
- A few monsters are deliberate front-pose exceptions, accepted in
  2026-09 user reviews (see L17): purple-gypceros (icon front pose) and
  royal-ludroth (sponge ball with the face set into the middle, like its
  icon). Do not convert them back to side view, and do not apply the
  front grammar to other monsters without a fresh user review.

### 5.2 Body grammar: the seven rules

1. Torso is a horizontal mass with a level belly bottom edge. Never let it
   degenerate into a diagonal band between head and tail (kirin v1 had no
   torso at all; just a neck sliver plus legs).
2. Head is an independent mass at the left. Do not continue it into the
   torso as one straight diagonal.
3. Wings/fins are separate structures ABOVE the torso, overlapping it at
   the shoulder; not slabs lying on the back, not floats detached from it.
4. Legs hang vertically from the belly: thick (>= 3px), close-set (gap
   <= 4px), belly dips 1px between them. The leg gap must not eat the
   torso (great-jaggi rows 14-15 read as "no body").
5. Tails/fins overlap-connect to the hip at body height. A transparent gap
   to the tail reads as a detached stripe (odogaron lesson).
6. Belly color band runs along the bottom edge. A pale patch floating
   mid-body reads as a saddle bag.
7. Any diagonal longer than ~5px needs steps, curves, or breaks. A long
   straight cut reads as perfunctory (xenojiiva wing-arm edge).

### 5.3 Anatomy language

- Winged wyverns: fan-shaped wing with finger bones radiating through the
  membrane to the tips and a deep scalloped trailing edge (rathalos
  family). No finger bones = reads as a shell or a bread loaf on the back.
- Neck/chest merges into the torso as one solid mass. A 1-2px channel at
  the joint gets outlined into a black crevasse that reads as "about to
  snap" (bazelgeuse/fatalis lesson).
- Fangs and teeth need a dark mouth gap behind them to show up on pale
  faces (barioth lesson: white fangs on a white face are invisible).
- Undersides need their own color band (belly/chest), lighter or darker
  than the body, running from chest to tail. Without it the sprite reads
  as a flat cutout (barioth/bazelgeuse/fatalis lesson).
- Small monsters may simplify, but the head/eye/mouth trio must stay
  readable; it is the identity anchor at terminal size.

### 5.4 Faces

- Side view: one eye + brow line, positioned above the jaw hinge.
- Front-symmetric faces (two equal dot eyes) read 呆; only use them for
  genuinely front-facing creatures (namielle, paolumu, nergigante).
- Eyes: 1-2px, with a dark pupil or brow next to the light pixel.
- Fangs: white pixels inside a dark mouth gap; upper fangs hang from the
  upper jaw, never float.

### 5.5 Color and palette discipline

- Per-monster palette, 5-8 colors: outline K, body, darker body shade,
  one accent material (membrane/plates/mane), white for eyes/teeth, plus
  eye/paw accents.
- Subspecies and family variants keep the base's skeleton but MUST differ
  in silhouette, not just palette: change the pose (wing flap phase, head
  height, tail angle, mouth state) or add, remove, or notch a signature
  part (crest, spikes, tail lobe). A pure palette swap reads as a
  duplicate in the roster; the span dicts of any two sprites must differ
  (see L20).
- The parent's base color char must exist in the child palette (see L11).
- Undersides and far limbs always take the darker shade; this is what
  separates the body from the background at terminal size.

## 6. Lessons (case studies)

Chronological; each entry names the sprite that paid for it.

- **L1: 16x16 is below the viability floor** (rathalos_16). The first
  redraw was 16x16: too few pixels to carry outline + anatomy at once.
  Verdict: height >= 24 is the floor; the constraint became a build rule.
- **L2: 3/4 view: formula faces read 呆** (all 23 3/4 drafts, archived
  externally). Symmetric two-dot eyes + straight mouth band + square heads
  read dumb, and bodies collapsed into head-vs-wing diagonals. Verdict:
  side view is the standard; reviving 3/4 needs asymmetric face
  construction, not a template.
- **L3: wing anatomy** (rathalos). The first side-view wing was an oval
  slab: no finger bones, shallow notches. Redrawn as a fan: red finger
  bones radiating from the wrist through the cream membrane, 2-4px deep
  scallops between fingers. This is what makes a wyvern read as flying.
- **L4: the leg gap ate the torso** (great-jaggi family). Leveling the
  belly left a transparent notch at rows 14-15 between the legs; the torso
  visually vanished ("no body"). Fix: rows 14-16 solid, notch moved BELOW
  the belly line, legs thick and close-set with a 1px belly dip between
  them. Family-wide fix propagated through the derived configs for free.
- **L5: detached tail** (odogaron). The tail band never overlapped the
  body; a 1-4px gap outlined into a black diagonal seam. Fix: tail root
  overlaps the hip at body height; the tip may droop, the root may not
  float.
- **L6: neck crevasse** (bazelgeuse/fatalis). Head/neck and body authored
  as two separate spans with a 1-2px gap at the joint; the stroke turned it
  into a black crack ("about to snap"). Fix: merge rows so neck/chest is
  one solid mass with the body; keep intentional overlap lines only where
  anatomy wants them (wing over body).
- **L7: belly bands** (barioth/bazelgeuse/fatalis). White or khaki bodies
  with no underside zone read as flat cutouts. Fix: a belly band (lighter
  or darker) along the bottom edge from chest to tail.
- **L8: straight diagonals** (xenojiiva). A 15px straight lower edge read
  as perfunctory. Fix: horizontal belly + hanging legs + a short curved
  neck line; diagonals stay under ~5px.
- **L9: silent fill skips** (kirin). Mane/tail runs referenced cells
  outside the silhouette; the runs op skips them silently, so the mane
  never appeared. Fix: verify fill coordinates against the final spans,
  not the intended ones.
- **L10: slug mismatch** (rathalos-azure). The config said
  `rathalos-azure`; data says `azure-rathalos`. The build-time slug check
  caught it. Always grep data/monsters.json first.
- **L11: palette KeyError on derive** (great-baggi/izuchi/velocidrome/
  gendrome/maccao). `dict(_base)` copies `"base": "O"` but the child
  palette dropped "O". Fix: define the parent's base char in every child
  palette, or override "base" to a char the child defines.
- **L12: fill ordering / frm** (anjanath zigzag, paolumu pads,
  bazelgeuse clusters). A fill defaults to repainting the base color only;
  overpainting an earlier fill needs an explicit frm argument. Three
  sprites lost their details to this before it was written down.
- **L13: spans duplicate row keys** (xenojiiva 3/4 draft). A dict literal
  defining row 6 twice silently keeps the last one; half the body
  vanished. Patch spans with `{**base_spans, 6: [...]}`, never by
  restating rows.
- **L14: put outside the silhouette** (gypceros/hypnocatrice claws).
  Claw puts referenced the old leg positions after the legs moved. The
  build rejects transparent-cell puts; fix the put or the spans together.
- **L15: never review a stale preview** (bazelgeuse/fatalis crops).
  Reviewing an old roster_preview made a fixed sprite look unfixed. The
  preview now regenerates on every dev build; do not screenshot stale
  copies.
- **L16: inherited fills use the parent's palette** (iodrome). A derived
  config inherits the parent's fill ops; any char they reference must
  exist in the child palette (add the char or override the fill op).
- **L17: the front icon pose is per-monster, not a template** (2026-09
  user review of five pilots: gypceros, kut-ku, pukei, rathalos, diablos).
  Four read well, one (rathalos) first read as a moth because its original
  icon is a curled 3/4 with one dominant wing, not a symmetric spread;
  matching the icon composition matters more than the face. Only
  purple-gypceros was accepted for the set; the other four stay side view.
  Front-pose techniques that worked, for reference: head takes half the
  canvas, the mouth is a transparent notch opening through the silhouette
  edge with floating fang-island spans (never a mouth line drawn inside
  the face), parts separate by 1px channels so the stroke draws structure
  lines, and the palest color goes on the face so features pop.
- **L18: family body proportions are the identity** (lagiacrus v1). A
  leviathan drawn with a short stubby body reads as a generic lizard no
  matter how correct the head and spikes are; the family trait IS the
  elongated profile. Leviathans are drawn long and low (44px body at 24px
  height, most of the length is trunk and tail); check each family's
  silhouette proportion before drawing, not just its parts.
- **L19: enclosed holes read as dots, gaps must open** (hermitaur v1
  claw). A 1-2px transparent hole fully surrounded by silhouette becomes
  a black dot after the stroke, not a pincer opening. A claw/scissor gap
  must open through the silhouette edge (rows authored with the gap
  touching the outside), so the stroke draws a wedge. Same round taught:
  wide color bands (the crab's cream rim) eat the body when thicker than
  ~2px; keep underside bands at 1-2 rows and let the base color carry
  the mass.
- **L20: palette-only subspecies read as duplicates** (2026-09 dedup
  round, user review). 50 of 89 sprites shared an exact silhouette with
  a sibling; the roster read as the same monster recolored. Every
  variant got a structural delta: wing flap phase (azure/silver
  rathalos), head height and jaw length (velocidrome, brute-tigrex),
  tail angle (wroggi, maccao, gold-rathian, purple-ludroth), crest
  shape (maccao, gendrome, blue kut-ku, gold/silver hypnocatrice, 
  scarred garuga), added or notched parts (lunastra mane, radobaan
  spikes, deadeye crest notch, glacial-agnaktor ice spikes). Rule: the
  span dicts of any two sprites must differ; fills alone are not
  enough, because at terminal size only the silhouette carries.

## 7. Review process

1. `python3 build_sprites.py`; dev previews + contact sheet + numbered
   roster preview, all regenerated together (never stale).
2. Eyeball the roster preview: silhouette, proportions, palette, face.
3. `zukan` real-render spot check for new batches: the terminal render is
   the acceptance test; preview.py approximates it.
4. `python3 build_sprites.py --check ../icons-pixelart`; byte-identical or
   the build fails.
5. CI (pixelart-check.yml) repeats the slug + build validation on every
   push touching pixelart/ or data/monsters.json.

## 8. Pipeline contract

- Sprite name == `data/monsters.json` slug (build enforces).
- Height <= 24 (build enforces); width unlimited.
- Release output: native-size transparent PNGs in `icons-pixelart/`,
  built by release.yml (`pip install pillow` +
  `build_sprites.py --out icons-pixelart`) and packaged into
  `zukan-assets-bin.tar.gz` alongside `data/` and `icons/`.
- zukan: `--sprites pixel` is the DEFAULT; it tries
  `icons-pixelart/<slug>.png` first and falls back to the game card icons
  per monster. Pixel sprites render 1:1 at native size (no resampling,
  `--width` ignored); game icons keep the configured width.
- Endemic life set: `build_sprites.py --endemic` builds the
  `endemic/` config directory (slugs validated against
  `data/endemic_life.json`, one record per game deduped to one sprite per
  slug) into `icons-pixelart/endemic/<slug>.png`. zukan's endemic renderer
  tries the pixel sprite first and falls back to the game card icon.
  Archetype bases are the `_*.py` modules (skipped by the config loader);
  species configs derive from them like monster variants.

## 9. Coverage status

Monsters: complete, 378 of 378 (finished 2026-09). Archetype families and
their base configs:

- Flagships and solo skeletons (30): nargacuga, tobi-kadachi, zinogre,
  tigrex, anjanath, diablos, paolumu, great-jagras, legiana, kulu-ya-ku,
  rajang, deviljho, bazelgeuse, vaal-hazak, odogaron, mizutsune, kirin,
  teostra, kushala-daora, alatreon, velkhana, gore-magala, shagaru-magala,
  xenojiiva, namielle, fatalis, nergigante, barioth, glavenus, aknosom
- Rathalos family (6): rathalos, azure-rathalos, silver-rathalos, rathian,
  pink-rathian, gold-rathian
- Bird-wyvern leaders + pack prey (11): great-jaggi, great-baggi,
  great-wroggi, great-izuchi, great-maccao, velocidrome, gendrome, iodrome,
  velociprey, genprey, ioprey
- Kut-ku family (5): yian-kut-ku, blue-yian-kut-ku, yian-garuga,
  deadeye-yian-garuga, scarred-yian-garuga
- Bird-wyvern bases + subspecies (8): pukei-pukei, coral-pukei-pukei,
  gypceros, purple-gypceros, hypnocatrice, gold-hypnocatrice,
  silver-hypnocatrice, nightshade-paolumu
- Flagship variants (7): stygian-zinogre, brute-tigrex, fulgur-anjanath,
  black-diablos, shrieking-legiana, lunastra, violet-mizutsune
- Leviathans (20): lagiacrus family, plesioth, gobul, epioth, nibelsnarf,
  somnacanth family, almudron family, balahara, hirabami, uth-duna,
  jin-dahaad
- Carapaceons (10): hermitaur family, ceanataur family, shen-gaoren,
  taikun-zamuza
- Herbivores (16): aptonoth, kelbi, mosswine, slagtoth, apceros, anteka,
  moofah, ceratonoth families
- Small pack archetypes: jagras family (jagras/girros/shamos), dromes and
  prey, jaggi pack (jaggi/jaggia/wroggi/baggi/izuchi/maccao/giadrome/
  giaprey), wingdrakes (mernos family), small leviathan pups
- Neopterons (15): vespoid family, seltas family, konchu, bnahabra,
  ahtal-ka
- Amphibians (9): tetsucabra family, zamtrios family, tetranadon family
- Temnocerans (8): nerscylla family, rakna-kadaki family, lala-barina
- Fanged beasts (23): blangonga family, congalala family, kecha-wacha
  family, gammoth, goss-harag, garangolm, doshaguma family, volvidon,
  bombadgy, bishaten family
- Brute wyverns (13): barroth family, glavenus family, uragaan family,
  brachydios family, duramboros family, banbaro, quematrice, rompopolo
- Flying wyverns (39): khezu family, gigginox family, gravios family,
  basarios family, espinas, astalos family, seregios family, arkveld,
  rey-dau, akantor, ukanlos, monoblos family, and the rath/narga/tigrex/
  barioth/bazel apex + deviant derives
- Elder dragons (43): fatalis family, valstrax family, kushala family,
  teostra/lunastra, chameleos family, malzeno family, nergigante family,
  kirin family, vaal-hazak family, magala family, amatsu, ceadeus family,
  lao-shan family, jhen family, dalamadur family, zorah-magdaros,
  dire-miralis, gogmazios, nakarkos, yama-tsukami, kulve-taroth,
  shara-ishvalda, behemoth, oltura, gaismagorm, safijiiva, narwa family,
  ibushi, leshen family, pietru pair, merphistophelin, estrellian family,
  meraginasu
- Constructs (7): guardian variants + seikret + zoh-shia
- Frontier/GU variants (~40): estrellian family, orugaron pair, chramine
  family, lightenna family, shen-gaoren variants, and the rest

Not covered: nothing; the endemic life set (132 of 132, drawn 2026-09)
lives in `pixelart/endemic/` and ships as `icons-pixelart/endemic/`.
Its archetype bases (the `_*.py` modules): `_fish` (19 species),
`_lampsquid` (4), `_jellyfish` (2), `_snail` (2), `_slug` (1),
`_beetle` (11), `_fly` (hoppers/ants/spiribugs, 10), `_butterfly` (6),
`_crab` (9 incl. helmcrabs), `_gekko` (5), lizards on `_gekko` (3),
`_toad` (6), `_songbird` (16 incl. owls/spiritbirds),
`_raptor` (2), `_penguin` (1), `_macaque` (2), `_hare` (3), `_bat` (3),
`_moly` (7), `_cobra` (2), `_wirebug` (2), `_spider` (2), `_fox` (1),
`_wasp` (3), plus hand-drawn singles (cactuar pair, wiggler pair,
nekker, stinkmink, tsuchinoko, mantagrell, crowned-prawn, trapbugs,
aurortle, andangler).

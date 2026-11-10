# Deckblade Dash hero prompts

Paste **STYLE** first, then one **CHARACTER** block, then one **OUTPUT** block. Attach the pictures in `ref/` as style
references when the tool accepts images (`ref/hero-combo-1.png` and `ref/looks-lineup.png` matter most).

---

## STYLE (always paste this first)

```
Pixel art game sprite for a 2.5D side-scrolling action game, in the tradition of hand-pixelled Korean arcade brawler
sprites (detailed, elegant, slender proportions, rich costume detail), but locked to a strict, small, clean pixel grid
so it sits with the game's existing art.

Hard rules:
- True pixel art. Every pixel is a crisp square on one exact grid. No anti-aliasing, no blur, no soft brushes, no
  gradients, no painterly texture, no glow halos, no sub-pixel detail, no JPEG noise.
- The character is 64 pixels tall from sole to crown at native size. Draw it upscaled exactly 8x (each art pixel =
  an 8 x 8 block), so the figure is 512 px tall. Do not mix pixel sizes.
- Side view facing RIGHT, turned about 20 degrees toward the viewer (three-quarter side view), feet flat on one
  horizontal baseline.
- Proportions: about 6.5 heads tall, slim and long-legged, a small head, readable hands; a heroic, agile swordsman,
  not chibi, not bulky.
- Light comes from the upper left and slightly in front. Each material uses a short ramp of 4 to 6 flat tones (lit
  side, mid, shade, deep shade), shadows shifted cooler and toward blue-violet, highlights warmer. Light dithering
  only on large flat areas such as a cape.
- A 1-pixel outline: near-black #0e0c14 around the whole silhouette; inside the figure, outlines take a darker tone
  of the colour they enclose (selective outline), so details stay crisp but not heavy.
- Limited palette: at most 32 colours for the whole character, flat, no colour that appears only once.
- Clean clusters, not texture: each material gets 3 shading tones plus one highlight; colour patches are mostly 2 x 2
  art pixels or larger and follow the form in clean bands. Single pixels are allowed only as deliberate accents (eyes,
  rivets, buttons, gem and edge glints, seam dots), never as random speckle, checkerboard noise or a downscaled
  painting's grain. Aim for the detail density of the kept sprites such as `assets/standing/hero.png`: interior
  shading on every part, not flat silhouettes.
- Readable at native size: the silhouette and the 2 or 3 key props (weapon, hat, goggles, crest) must read when the
  sprite is shown at 1x. Big simple shapes first, small accents last.
- Contrast with a dark stage: the figure's lit side is clearly lighter than #2a2b33, and the outer outline is a
  continuous #0e0c14 line all round with no gaps.
- Background fully transparent (if transparency is not possible: one flat #ff00ff magenta, no shadow, no floor).
- No text, no logo, no watermark, no frame, no border, no ground shadow, no magic effects, no motion lines, no
  sparkles: the game draws its own effects.
- One character only, the whole body in frame with an empty margin of at least 4 art pixels all round.
```

---

## CHARACTER (pick one)

Colours are the game's own for each look; keep them so the character still reads as itself.

### hero · 晨霜 Dawnfrost (the default)
```
Dawnfrost, a young wandering swordsman in close-fitting ice-blue light armour over a dark navy undersuit: a short
open-faced helm with a small swept crest, layered shoulder plates, a fitted breastplate, segmented tassets over the
hips, armoured boots and gauntlets. A straight longsword with a gold guard held low in the right hand. Short pale hair
under the helm. Palette: lit #e8f4ff, #a9cdea, mid #6f97c6, shade #4a6198, belt #3c4c80, deep #2b3563 and #1d2348,
gold accent #ffcf3a. Calm, sharp, quietly confident.
```

### ironblood · 赤狮 Lionheart (floor 10)
```
Lionheart, a knight in a closed great helm crowned by a tall crimson lion's-mane crest, heavy plated pauldrons,
polished steel plate, a crimson cape lined in gold falling behind him. Palette: steel #eef2f8, #b4bccc, #7a8498,
#4e566a, #22262f; gold trim #ffc23d; crimson cape. Steady, noble, immovable.
```

### jadegale · 青岚 Jade Gale (floor 20)
```
Jade Gale, a forest ranger: a high ponytail with one feather, a hood thrown back, a long green cloak, a leather
jerkin and a quiver strap across the chest, soft boots. Palette: leather #e6d2a8, #b8946a, #80643e, #54402a,
#1e160e; cloak green; accent #9ae07a. Light-footed, alert.
```

### nightcrow · 夜鸦 Nightcrow (floor 30)
```
Nightcrow, a shadow-walker in a deep pointed hood that hides the face but for two cold cyan eyes, a cowl over the
shoulders, dark wrapped clothing and a long tattered cape. Palette: #d0cce6, #9690b4, #686284, #46425e, #18152a;
eyes and trims #6ff0ff. Silent, menacing.
```

### sunforged · 金曜 Sunforged (floor 40)
```
Sunforged, a holy warden in a winged helm open at the face under a thin halo, gold pauldrons, a white surcoat over
gold armour, a long white cape. Palette: gold #fff6d2, #f2d27a, #c8962e, #8a5e18, #3a2208; red accent #c8281f and
#ff4a3a; white cloth. Radiant, solemn.
```

### snowfield · 雪原 Snowfield (floor 60)
```
Snowfield, a watchman of the snowfields in a long blue greatcoat, a great round fur hat, a thick fur collar and fur at
the cuffs and boots. Palette: #c8dcf4, #8aa8d8, #5a78b0, #3a5288, #1a2a4a; fur #ffffff with cool grey shade.
Weathered, patient.
```

### emberwake · 余烬 Emberwake (floor 80)
```
Emberwake, a child of fire: hair of flame that burns white at the tips, a charred dark body with embers glowing in
the cracks, a torn orange sash, bare forearms. Palette: #ffc070, #b85a34, #5e3a34, #3a2828, #160e10; fire #ff5a1d and
#ffc23d. Restless, fierce. (Flames are drawn as flat pixel shapes, not glow.)
```

### frostblade · 霜刃 Frostblade (class: Blade Master)
```
Frostblade, a ronin of the frost: white hair swept back in sharp spikes, a long cyan scarf flying behind, a fitted
dark-blue kimono top, wide hakama trousers, a katana at the hip and one in hand. Palette: #c8d8f4, #8ea4d8, #5a70b0,
#3a4a84, #141a34; scarf #3ad0f0 and #a6ecff. Cold, precise.
```

### brassgun · 铜炮 Brassgun (class: Gunner)
```
Brassgun, a gunslinger: messy hair under brass goggles, a long olive coat with its collar up, a bandolier across the
chest, a heavy brass hand cannon held low. Palette: #d8c8a8, #a8946c, #766444, #4e422c, #1e180e; brass #ffb04a.
Cocky, battle-worn.
```

### mossfist · 苍拳 Moss Fist (class: Brawler)
```
Moss Fist, a monk of the fist: shaven head but for one long braid, a red headband with two trailing tails, bare
muscular arms with wrapped forearms, a green sash, loose trousers and wrapped feet. Palette: skin #ffe6cc, #f0b88c,
#c07c56, #80482e; sash #5a9a3a; headband red. Grounded, disciplined.
```

### runeweave · 秘纹 Runeweave (class: Elementalist)
```
Runeweave, a rune-weaver in a tall wide-brimmed hat with a bent tip and a deep violet robe whose hem carries glowing
gold runes (drawn as flat pixel marks), a staff in one hand. Palette: #f2e2ff, #c08cff, #8a5ad8, #5a32a0, #1e0e3a;
runes #ffcf3a. Mysterious, poised.
```

### starsea · 星海 Starsea (1 rebirth)
```
Starsea, a navigator of the star sea: a black tricorne with a pink plume, a long navy coat with gold buttons and cuffs,
a long tail of hair, a sabre. Palette: #d8f0ff, #7aa8e8, #3e5cb0, #24307a, #0c1238; plume #ff8ad0; gold buttons.
Dashing, adventurous.
```

### voidborn · 虚空 Voidborn (3 rebirths)
```
Voidborn, a lord of the void: a crown of bone horns over a face of shadow with two violet eyes, dark plate under a long
ragged cape, a black greatsword. Palette: #ecebf4, #74748a, #40404f, #28283a, #0a0a10; eyes and trims #c07aff.
Regal, terrifying.
```

---

## OUTPUT (pick one)

### A. Standing sprite (do these first, one per character)
```
Output: the character standing at ease, weapon lowered, facing right, on its own. Image 768 x 640 px.
```

### B. Character sheet (the default hero first)
```
Output: one image with the same character three times on one shared baseline, evenly spaced, identical scale and
palette: (1) standing facing right, (2) facing the viewer, (3) seen from behind. Image 1536 x 640 px.
```

### C. Animation strip (only after A looks right; attach the approved A as the reference)
```
Output: an animation strip of N frames in one row, every frame in an equal 96 x 80 art-pixel cell (768 x 640 px at
8x), the character's feet on the same baseline in every cell, same scale and palette as the reference sprite, no
effects. Frames: <pick one>
- idle, 4 frames: a slow breath, shoulders rise and fall 1 pixel.
- run, 8 frames: a fast forward run, body leaning in, cape and hair streaming back.
- slash, 6 frames: wind-up, the blade raised behind; a fast forward diagonal cut; follow-through; recover.
- cast, 4 frames: the free hand raised forward, palm open.
- hit, 2 frames: knocked back, head thrown back.
- jump, 4 frames: crouch, launch, top of the arc, land.
```

---

## REWORK (second pass, 2026-11-10)

The first batch is in the fork `0xuezhang985/deckblade-art` under `assets/standing/`. Keep these as they are:
hero, ironblood, jadegale, sunforged, snowfield, frostblade, mossfist, runeweave, starsea. Redraw these four, each as
OUTPUT A, with STYLE (its new "Clean clusters", "Readable" and "Contrast" rules) and its CHARACTER block, plus the
fix below. Attach `ref/rework.png` (what to keep and what to fix) and `ref/looks-lineup.png`; attach a kept sprite such
as `assets/standing/hero.png` as the model for cluster size and outline.

### brassgun · 铜炮 (redo)
```
Fix: the coat reads as camouflage noise and the props are lost. Draw the long olive coat as two or three clean flat
tones with one crisp edge highlight down the front and a clear collar; brass goggles pushed up on the forehead as one
bright readable shape (two round lenses); a bandolier as one clear diagonal band with a few brass cartridge marks; a
heavy brass hand cannon held low in the right hand, wider than the forearm, the brightest object on the figure.
```

### voidborn · 虚空 (redo)
```
Fix: the figure is too busy and dissolves into the dark. Make it a clear dark silhouette with large calm shapes: dark
plate in two flat tones with a single violet rim light on the lit (left) edges, a crown of 3 or 4 large pale bone horns
that clearly break the silhouette at the top, a face of solid shadow with exactly two violet eye pixels, a long cape
cut into 4 or 5 big ragged points (not shreds), and a black greatsword with a pale edge line so it reads.
```

### emberwake · 余烬 (redo)
```
Fix: the body is speckled and the fire does not read as fire. Make the body a dark charred form in 2 or 3 flat tones
with a few clean glowing crack lines (1 px wide, orange to yellow, following the limbs), hair as 4 or 5 big flat flame
tongues going from orange at the root to pale yellow at the tips, and a torn orange sash in large clean shapes. No
speckle anywhere.
```

### nightcrow · 夜鸦 (redo)
```
Fix: too dark against a dark stage. Keep the deep pointed hood, cowl and long tattered cape, but give the lit side a
clearly lighter violet-grey (around #9690b4) along hood, shoulder and cape edge, keep the hood's opening black with
two bright cyan eyes, and cut the cape's hem into a few large clean points.
```

### turnaround fix (Dawnfrost)
```
The turnaround sheet's three views are 64 px wide each; redo it as three equal 96 x 80 cells, same scale, feet on
y = 71, so it matches the animation strips.
```

---

## THIRD PASS: add detail (2026-11-10)

The second pass (fork commit e6a6536) cleaned the speckle off brassgun, voidborn, emberwake and nightcrow, but they
came out much flatter than the nine kept sprites (8 to 11 colours against 12 to 15, little interior shading), so the
thirteen no longer read as one set. Keep each second-pass sprite's silhouette, pose, palette family and clean edges,
and add interior detail up to the kept sprites' density. Paste STYLE, the CHARACTER block, then the block below, as
OUTPUT A. Attach `ref/pass3.png` (the target density above, the flat second pass below), the character's second-pass
PNG as the base, and `assets/standing/hero.png` and `assets/standing/ironblood.png` as the density models.

```
Third pass: same silhouette, pose and clean outline as the attached second-pass sprite, but redrawn with the detail
density of the attached model sprites: 12 to 14 colours; every material in 3 shading tones plus a highlight, lit from
the upper left; fold lines, plate seams, straps and edges drawn as short clean lines of tone; single pixels only as
deliberate accents (eyes, rivets, buttons, glints). No speckle, no noise.
```

### brassgun · 铜炮
```
Add: a face with brow, eye and jaw in skin tones, messy dark-brown hair clearly separate from the goggles; brass
goggles as two round lenses with a dark rim and a white glint each, on a strap; the long olive coat in 3 tones with
fold lines down the skirt, a turned-up collar with its own shade and buttons; a bandolier as a clear diagonal leather
band with 5 or 6 brass cartridge caps; the hand cannon as a machine, not a glow: a thick brass barrel with two dark
bands, a muzzle ring, a wooden grip in the hand, highlight along its top. Boots with a sole line and a buckle.
```

### voidborn · 虚空
```
Add: dark plate in 3 tones (#40404f lit, #28283a mid, #0a0a10 deep) with plate seams and a violet #c07aff rim along
the lit edges of the helm, pauldron, gauntlet and greave; exactly two bright violet eye pixels in the shadowed face,
with a faint violet glow pixel under each; the bone-horn crown in 2 pale tones with a dark base; the cape with a darker
inner side, 3 or 4 long fold lines and its big ragged points; the greatsword's grip, crossguard and a pale edge line.
```

### emberwake · 余烬
```
Add: a face: two glowing yellow eyes, a jaw and cheek line; the charred body in 3 tones (#5e3a34 lit, #3a2828 mid,
#160e10 deep) with readable shoulders, elbows, hands, knees and feet; glowing crack lines (orange #ff5a1d into yellow
#ffc23d, 1 px) running along arms, chest and legs; the flame hair as 5 tongues in 3 tones, white-hot at the tips; the
torn orange sash with fold shading and a frayed end; ember dots only where cracks cross.
```

### nightcrow · 夜鸦
```
Add a little, keep it lean: cowl folds over the shoulders, cloth wrappings on forearms and shins as short bands,
a belt with a small cyan buckle, the cape's inner side one tone darker with 2 or 3 fold lines, and cyan trims as short
dotted lines on the hood edge and the blade.
```

---

## PARTS: the hero cut into pieces for the game's skeleton (2026-11-10)

In combat the hero is moved by the game's own skeleton (every skill is a set of poses on it), so instead of animation
strips each character is drawn once as separate parts that the game turns and places on the bones. Start with
Dawnfrost only. The layout is fixed: `parts/parts-template-8x.png` (paint on this, 832 x 992) and
`parts/parts-template-labelled.png` (the same with each cell's name), `parts/parts.json` (each cell, its pivot and end in
native pixels), and `parts/assembly-preview.png` (the grey template assembled on real moves: this is how the parts are
used). Attach the template, the labelled copy, the assembly preview, and `assets/standing/hero.png` (who he is). Paste
STYLE, Dawnfrost's CHARACTER block, then:

```
Output: one parts sheet, exactly the size and layout of the attached template (832 x 992 px at 8x, 104 x 124 art
pixels). Paint each part inside its own cell, over the grey mannequin, the same character, palette and detail as the
attached standing sprite. Every cell keeps the transparent background; nothing crosses a cell's border.

How the parts are used: the game turns each part around its red dot and stretches it a little so the blue dot lands on
the next joint, then stacks the parts. So:
- Pure side view facing right (not three-quarter): the head in profile looking right, the chest's front to the right,
  the foot's toes to the right.
- The red dot is the joint the part hangs from, the blue dot the next joint: keep the part's joints there. Do not draw
  the dots themselves.
- Draw every part whole, as if nothing covered it (no gaps where an arm crossed the chest in the standing sprite).
- Each limb part runs 2 to 3 px past both dots with rounded ends, so joints overlap and never show a gap when turned.
- At least as thick as the grey mannequin: the parts must read when turned at any angle; no 1 px lines.
- Each part has its own 1 px #0e0c14 outline all round.

The cells:
- head: the head in profile with its helm, hair and crest; a short neck stump at the red dot.
- torso: chest, waist, belt and hip armour in one piece, from the hips (red) up to the base of the neck (blue).
- upperArm: from the shoulder (red) to the elbow (blue), with the shoulder plate on top so it turns with the arm.
- foreArm: from the elbow (red) to the wrist, ending in a closed gauntleted fist around the blue dot.
- thigh: from the hip (red) to the knee (blue), with the tasset on top.
- shin: from the knee (red) to the ankle (blue), with the knee plate and the boot's upper.
- foot: the boot, ankle at the red dot, toe at the blue, sole flat along the bottom, pointing right.
- cape: leave empty for Dawnfrost (other characters hang their cape here, from the neck down, seen from the side).
- sword: lying flat, pointing right: the grip centred on the red dot (the fist closes there), a gold crossguard just
  right of it, a straight blade at least 5 px wide out to the tip at the blue dot; flat tones, no glow.
The game uses one set of arm and leg parts for both sides (the far ones darker), so draw them once.
```

To check a sheet before keeping it: `python -I tools/assemble.py <sheet.png> parts/parts.json parts/poses.json
preview.png` (Pillow) puts it on the same real moves as the assembly preview.

---

## Checklist before a picture is kept

- Downscaled to 1/8 with nearest-neighbour, every pixel is one flat colour (no stray in-between tones at the edges).
- The figure is 64 px tall, faces right, feet on the baseline.
- At most 32 colours; the outline is the same near-black all round.
- No random speckle inside the figure; single pixels only as deliberate accents; it matches the kept sprites' detail.
- The key props named in the CHARACTER block can be pointed at in the 1x sprite.
- Next to `ref/looks-lineup.png` at the same pixel size, it looks like the same game, just more detailed.

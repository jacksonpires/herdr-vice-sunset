# Vice Poster

Herdr's default window as a sunset poster: the panes are framed tiles of a collage, laid over a purple-to-orange evening sky with palm silhouettes, and the sky shows in the gaps between them and faintly through them. The focused tile gets a hot pink neon border. Same colors as Vice Sunset, with the window itself as the sky.

![Vice Poster](preview.png)

## What you see

- **The sky** fills the window behind everything: `backgrounds/vice-poster.png`, 2560×1600, drawn to `cover`. A vertical gradient through `#220a3a` (top), `#5c1c70`, `#d64280`, `#f68068` and `#faaa60` (bottom), with a soft warm glow (`#ffc478`) rising from the bottom center. Dark palm fronds (`#160624` at 85%) hang from both top corners and rise from both bottom corners.
- **The panes** are the tiles: 3px radius, a 3px `#120618` border, `#1a0f2e` at 62% behind each one and the terminal at 62% opacity, so the sky glows through the text. 18px between tiles and around them. The focused tile's border is `accent` `#ff4fa3`, 3px. Every pane has Herdr's `pane` header, 30px, on top; a tab's only pane is framed too.
- **The sidebars** (spaces and agents on the left, Files and Changes on the right) are `#14061e` at 55%, so the palms and the sky show behind them. No dividers between the regions.
- **Tabs, status bar and dialogs** use the theme: `chrome` `#16081f` at 80%, `canvas` transparent, `border` `#2a1240`, `selected` `#4a1f6e`, buttons in `solid` `#ff7a3d`.
- **Terminal colors** are Vice Sunset's: background `#1a0f2e`, text `#f3e8ff`, cursor `#ff4fa3`, selection `#4a2a6e`, and the same 16 ANSI colors (red `#ff4f6d`, green `#3ddc97`, yellow `#ffb347`, blue `#4fb3ff`, magenta `#ff4fd8`, cyan `#2de2e6`, and their bright versions).

## How it behaves

- It is Herdr's `main` layout underneath: same blocks, keys, clicks and panels. Nothing animates.
- Agent status colors: working `#ffb347`, done `#3ddc97`, blocked `#ff4f6d`, idle dim.
- The more panes a tab has, the more it looks like the collage; a single pane is one big tile with the sky around its edges.
- Dark only.

## Built from

- `layouts/vice-poster.json`: Herdr's shipped `main` layout (0.1.9) with these changes. Root: `"theme": "vice-poster"`, `"background": {"image": "backgrounds/vice-poster.png", "fit": "cover"}`, `"divider": {"width": 0, "color": "#00000000"}`, `"terminal_opacity": 0.62`, `"preview": "layouts/vice-poster.png"`. Nodes `sidebar` and `panel`: `"background": "#14061e8c"`. Node `work-body`: `padding` and `gap` 18. The `main` block's `pane`: `gap` 18, `radius` 3, `background` `#1a0f2e9e`, `border` `{width: 3, color: "#120618"}`, `focus` `{width: 3, color: "accent"}`, header and `lone` as in `main`. Only Herdr's shipped mods are used.
- `themes/vice-poster.json`: Vice Sunset's theme with `chrome` `#16081fcc`, `canvas` `#00000000`, `border` `#2a1240` and `selected` `#4a1f6e`.
- `backgrounds/vice-poster.png`: the sky. `backgrounds/sky.py` draws it with Pillow (`uv run --no-project --with pillow python backgrounds/sky.py out.png`): the gradient stops above, the glow (a blurred ellipse), and each frond as a drooping curve with leaflets on both sides.
- `layouts/vice-poster.png`: the picture Settings shows (same as `preview.png`).

## Watch out

- **Copy three folders, not one.** Adding it means `layouts/vice-poster.json` and `layouts/vice-poster.png` to `layouts/`, `themes/vice-poster.json` to `themes/`, and `backgrounds/vice-poster.png` to `backgrounds/` in `~/.config/herdr-app`. The background path is relative to that folder; without the image the window is the plain theme.
- Transparency is the look and also the trade-off: on bright parts of the sky (the bottom of the window), text in a terminal is a little less contrasted. Raise `terminal_opacity` and the pane `background` alpha if it gets in the way.
- The theme has the layout's name, so Settings offers it only while this layout shows.
- The sky and palms are original drawings; nothing is taken from any game or brand.

## Done when

- The JSON files are valid and `layout.switch {name: "vice-poster"}` shows the window with no `layout.error`.
- With three panes in a tab, the sky shows between them, the palms show at the top corners behind the tiles, and the focused tile has a pink border.
- `git diff --color` in a terminal is readable over the sky, with the gradient faintly visible behind it.
- `ctrl-shift-l` switches back to the previous layout.

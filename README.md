# Vice Sunset for the Herdr app

A dusk-on-the-coast look for the [Herdr app](https://herdr.dev): deep purple panes, hot pink focus, sunset orange buttons and terminal colors from the same evening. It is Herdr's default layout with this theme on it.

![Vice Sunset](preview.png)

## Install

Tell your agent:

```
Read ~/.config/herdr-app/AGENTS.md, then add this layout: https://github.com/jacksonpires/herdr-vice-sunset
```

Or by hand: copy `layouts/vice-sunset.json` and `layouts/vice-sunset.png` to `~/.config/herdr-app/layouts/`, `themes/vice-sunset.json` to `~/.config/herdr-app/themes/`, then pick **Vice Sunset** in Settings or run `herdr-app do layout.switch --name vice-sunset`. `ctrl-shift-l` switches back.

## Colors

| Role | Color |
|---|---|
| Terminal background | `#1a0f2e` |
| Text | `#f3e8ff` |
| Accent, focus, cursor | `#ff4fa3` |
| Primary buttons | `#ff7a3d` |
| Window gradient | `#2b1145` → `#120821` |
| Working / done / blocked | `#ffb347` / `#3ddc97` / `#ff4f6d` |

The 16 terminal colors are in `themes/vice-sunset.json`. `RECIPE.md` describes the whole look, so an agent can rebuild it from scratch.

The palette is an original take on a sunset mood. It is not affiliated with or taken from any game or brand.

## License

MIT

# Vice Sunset layouts for the Herdr app

Two dusk-on-the-coast layouts for the [Herdr app](https://herdr.dev), both built on Herdr's default layout with the same palette: deep purple, hot pink neon focus, sunset orange buttons and terminal colors from the same evening.

## Vice Poster (recommended)

The window as a sunset poster: panes as framed tiles over a purple-to-orange sky with palm silhouettes, the sky showing between and through them.

![Vice Poster](vice-poster/preview.png)

## Vice Sunset

A calm version: Herdr's usual window with the sunset theme and a purple gradient behind the panes.

![Vice Sunset](vice-sunset/preview.png)

## Install

Tell your agent, with the folder of the one you want:

```
Read ~/.config/herdr-app/AGENTS.md, then add this layout: https://github.com/jacksonpires/herdr-vice-sunset/tree/main/vice-poster
```

Or by hand, from inside `vice-sunset/` or `vice-poster/`: copy `layouts/*` to `~/.config/herdr-app/layouts/`, `themes/*` to `~/.config/herdr-app/themes/` and, for Vice Poster, `backgrounds/vice-poster.png` to `~/.config/herdr-app/backgrounds/`. Then pick it in Settings or run `herdr-app do layout.switch --name vice-poster` (or `vice-sunset` for the calm one). `ctrl-shift-l` switches back.

Each folder has a `RECIPE.md` that describes the layout in full, so an agent can rebuild it from scratch.

The palette and drawings are an original take on a sunset mood. They are not affiliated with or taken from any game or brand.

## License

MIT

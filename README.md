# website
Source for [`mrgrossman.com`](https://www.mrgrossman.com).

## Run locally
1. `uv run zensical serve`

## Layout
Every page is rendered by the standalone template in [`overrides/main.html`](overrides/main.html), which includes all of the site's CSS. It doesn't use the theme's layout, CSS, or JS. Set `layout: resume` in a page's front matter to use the compact resume styles.

## Publish
Pushing to master kicks off a new `zensical build` and automatically pushes the artifacts to `github.com/matthewgrossman/matthewgrossman.github.io`. This is handled in [`.github/workflows/deploy.yml`](.github/workflows/deploy.yml)

# website
Source for [`mrgrossman.com`](https://www.mrgrossman.com).

## Run locally
1. `uv run zensical serve`

## Layout
Every page is rendered by the standalone template in [`overrides/main.html`](overrides/main.html), which includes all of the site's CSS. It doesn't use the theme's layout, CSS, or JS. Set `layout: resume` in a page's front matter for the resume's wider layout.

## Publish
Pushing to master builds the site and deploys it to GitHub Pages from this repo. The custom domain is set in the repo's Pages settings. See [`.github/workflows/deploy.yml`](.github/workflows/deploy.yml).

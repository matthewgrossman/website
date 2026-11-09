# website
Source for [`mrgrossman.com`](https://www.mrgrossman.com).

## Run locally
1. Install [Hugo](https://gohugo.io) (`brew install hugo`). The version used for deploys is pinned in [`.github/workflows/deploy.yml`](.github/workflows/deploy.yml).
2. `hugo server`

## Layout
Pages live in [`docs/`](docs), with the homepage at [`docs/_index.md`](docs/_index.md). Every page is rendered by the single template in [`layouts/all.html`](layouts/all.html), which includes all of the site's CSS. Set `layout: resume` in a page's front matter for the resume's wider layout.

Pages are written to also render on GitHub: use plain HTML attributes like `align="center"` and `width` instead of class tags, and link icons from [`docs/assets/icons`](docs/assets/icons).

## Publish
Pushing to main builds the site and deploys it to GitHub Pages from this repo. The custom domain is set in the repo's Pages settings. See [`.github/workflows/deploy.yml`](.github/workflows/deploy.yml).

# website
Source for [`mrgrossman.com`](https://www.mrgrossman.com).

## Run locally
1. `uv run zensical serve`

## Publish
Pushing to master kicks off a new `zensical build` and automatically pushes the artifacts to `github.com/matthewgrossman/matthewgrossman.github.io`. This is handled in [`.github/workflows/deploy.yml`](.github/workflows/deploy.yml)

# website
Source for [`mrgrossman.com`](https://www.mrgrossman.com).

## Run locally
1. `uv run mkdocs serve -w ./`

## Publish
Pushing to master should kick off a new `mkdocs build` and automatically push the artifacts to `github.com/matthewgrossman/matthewgrossman.github.io`. This is handled in [`.github/workflows/ci.yml`](.github/workflows/ci.yml)

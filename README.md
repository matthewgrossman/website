# website
Source for [`mrgrossman.com`](https://www.mrgrossman.com).

## Installing
1. Clone the repo
1. `poetry install`

## Run locally
1. `poetry run mkdocs serve`

## Publish
Pushing to master should kick off a new `mkdocs build` and automatically push the artifacts to `github.com/matthewgrossman/matthewgrossman.github.io`. This is handled in [`.github/workflows/ci.yml`](.github/workflows/ci.yml)

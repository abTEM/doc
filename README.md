# *ab*TEM Documentation

The source of the documentation at <https://abtem.github.io/doc/>.

## Branches

- `dev` is the default branch. Documentation of unreleased abTEM work is merged here, and every push to it
  publishes the development docs under `/dev/` (`deploy-dev.yml`, built against abTEM's `dev` branch).
- `main` holds the documentation of the released abTEM. It is updated only by merging `dev` (or a
  `release/` or `hotfix/` branch) when abTEM is released, after the release is on PyPI. Every push to it
  publishes the stable docs at the site root (`deploy-book.yml`, built against the abTEM on PyPI).
- Both builds keep the other's part of the site (the `gh-pages` branch is only their output).

For a patch release of abTEM, branch `release/x.y.z` from `main`, apply the corrections and merge it into `main`.

## Changelog

The changelog is `CHANGELOG.md` of the abTEM repository. The docs build mirrors it into
`docs/abtem/changelog.md` (`scripts/fetch_changelog.py`: from abTEM `dev` for the dev docs, from abTEM `main` for
the stable docs). Change it in the abTEM repository; the copy committed here is only the fallback for when
the download fails.

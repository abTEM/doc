"""Mirror the changelog of the abTEM repository into the docs.

The changelog lives in CHANGELOG.md of abTEM/abTEM. The docs build copies it to
docs/abtem/changelog.md: from the ``dev`` branch for the development docs and
from ``main`` (the released state) for the stable docs.

    python scripts/fetch_changelog.py dev
    python scripts/fetch_changelog.py main

If the file cannot be fetched (offline, or the branch has no CHANGELOG.md yet) the
copy that is committed in this repository is kept, with a warning.
"""

import sys
import urllib.error
import urllib.request
from pathlib import Path

URL = "https://raw.githubusercontent.com/abTEM/abTEM/{ref}/CHANGELOG.md"
TARGET = Path(__file__).resolve().parent.parent / "docs" / "abtem" / "changelog.md"


def main(ref: str) -> int:
    url = URL.format(ref=ref)
    try:
        with urllib.request.urlopen(url, timeout=30) as response:
            text = response.read().decode("utf-8")
    except (urllib.error.URLError, TimeoutError) as error:
        print(f"warning: could not fetch {url} ({error}); keeping {TARGET}")
        return 0

    if not text.lstrip().startswith("# Changelog"):
        print(f"warning: {url} does not look like the changelog; keeping {TARGET}")
        return 0

    TARGET.write_text(text, encoding="utf-8")
    print(f"mirrored {url} to {TARGET}")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1] if len(sys.argv) > 1 else "dev"))

#!/usr/bin/env python3
"""Detect (and optionally strip) stale ipywidgets state in notebook metadata.

nbformat notebooks can carry a notebook-level ``metadata.widgets`` blob holding
serialized ipywidgets model state (e.g. tqdm progress bars). When a cell that
used to produce a widget is re-run without it, or edited to no longer produce
one, the old model state is left behind in ``metadata.widgets`` even though no
cell output references it anymore. MyST-NB / nbconvert's widget renderer still
emits that leftover state into the built HTML, so stale widget content (e.g.
an old progress-bar line such as "3738/3738 [00:34<00:00, 87.06it/s]") can
silently reappear in published docs long after the code that produced it is
gone.

This script finds notebooks where ``metadata.widgets`` state is not referenced
by any cell's ``application/vnd.jupyter.widget-view+json`` output ("orphaned"
widget state), and can strip it with ``--fix``.

Usage:
    python scripts/check_notebook_widgets.py            # check docs/, exit 1 on findings
    python scripts/check_notebook_widgets.py --fix       # strip orphaned state in place
    python scripts/check_notebook_widgets.py path/to/one.ipynb --fix
"""
import argparse
import glob
import json
import os
import re
import sys

WIDGET_VIEW_MIME = "application/vnd.jupyter.widget-view+json"
MODEL_REF_RE = re.compile(r"^IPY_MODEL_(?P<model_id>.+)$")

DEFAULT_GLOBS = ["docs/**/*.ipynb"]
EXCLUDE_MARKERS = (".ipynb_checkpoints", f"{os.sep}_build{os.sep}")


def iter_notebook_paths(patterns):
    seen = set()
    for pattern in patterns:
        matches = glob.glob(pattern, recursive=True) or [pattern]
        for path in sorted(matches):
            if any(marker in path for marker in EXCLUDE_MARKERS):
                continue
            if path not in seen and path.endswith(".ipynb"):
                seen.add(path)
                yield path


def referenced_model_ids(nb):
    """model_ids that appear in a live widget-view output somewhere in the notebook."""
    model_ids = set()
    for cell in nb.get("cells", []):
        for output in cell.get("outputs", []):
            view = output.get("data", {}).get(WIDGET_VIEW_MIME)
            if view and "model_id" in view:
                model_ids.add(view["model_id"])
    return model_ids


def widget_state_entries(nb):
    """Yield (mime_key, state_dict) pairs from metadata.widgets, if present."""
    widgets_meta = nb.get("metadata", {}).get("widgets") or {}
    for mime_key, payload in widgets_meta.items():
        yield mime_key, payload.get("state", {})


def _iter_model_refs(obj):
    """Recursively find ipywidgets cross-references (``IPY_MODEL_<id>``
    strings) inside a model's trait state, e.g. a container widget's
    ``children``/``layout``/``style`` traits.
    """
    if isinstance(obj, str):
        match = MODEL_REF_RE.match(obj)
        if match:
            yield match.group("model_id")
    elif isinstance(obj, dict):
        for value in obj.values():
            yield from _iter_model_refs(value)
    elif isinstance(obj, list):
        for value in obj:
            yield from _iter_model_refs(value)


def _reachable_model_ids(root_ids, state):
    """Transitive closure of model ids reachable from root_ids by following
    ipywidgets model-to-model references within ``state`` (e.g. a live HBox
    widget referencing its child progress-bar/label models). Without this,
    stripping "unreferenced" models would delete the internals of widgets
    that are still actually live.
    """
    reachable = set()
    frontier = [mid for mid in root_ids if mid in state]
    while frontier:
        model_id = frontier.pop()
        if model_id in reachable:
            continue
        reachable.add(model_id)
        inner_state = state[model_id].get("state", {})
        for ref in _iter_model_refs(inner_state):
            if ref in state and ref not in reachable:
                frontier.append(ref)
    return reachable


def find_orphaned_widgets(nb):
    """Return {mime_key: [orphaned_model_id, ...]} for state not reachable
    from a live cell output. If no cell has a widget-view output at all,
    every model in every state entry counts as orphaned.
    """
    referenced = referenced_model_ids(nb)
    orphaned = {}
    for mime_key, state in widget_state_entries(nb):
        reachable = _reachable_model_ids(referenced, state)
        stale = sorted(set(state) - reachable)
        if stale:
            orphaned[mime_key] = stale
    return orphaned


def strip_orphaned_widgets(nb):
    """Remove orphaned model state from metadata.widgets in place.

    Drops metadata.widgets entirely once no live widget-view output remains
    in the notebook, since a widget-state blob is useless without any output
    that renders it.

    Returns True if the notebook was modified.
    """
    widgets_meta = nb.get("metadata", {}).get("widgets")
    if not widgets_meta:
        return False

    referenced = referenced_model_ids(nb)
    if not referenced:
        del nb["metadata"]["widgets"]
        return True

    changed = False
    for mime_key in list(widgets_meta):
        state = widgets_meta[mime_key].get("state", {})
        reachable = _reachable_model_ids(referenced, state)
        stale_ids = set(state) - reachable
        for model_id in stale_ids:
            del state[model_id]
            changed = True
        if not state:
            del widgets_meta[mime_key]
            changed = True

    if not widgets_meta:
        del nb["metadata"]["widgets"]
        changed = True

    return changed


def write_notebook(nb, path):
    with open(path, "w", encoding="utf-8") as f:
        json.dump(nb, f, indent=1, ensure_ascii=False)
        f.write("\n")


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "paths",
        nargs="*",
        default=DEFAULT_GLOBS,
        help="Notebook paths or glob patterns to check (default: every notebook under docs/).",
    )
    parser.add_argument(
        "--fix",
        action="store_true",
        help="Strip orphaned widget metadata in place instead of just reporting it.",
    )
    args = parser.parse_args(argv)

    paths = list(iter_notebook_paths(args.paths))
    if not paths:
        print("No notebooks matched.", file=sys.stderr)
        return 0

    failures = []
    for path in paths:
        with open(path, encoding="utf-8") as f:
            nb = json.load(f)

        orphaned = find_orphaned_widgets(nb)
        if not orphaned:
            continue

        if args.fix:
            if strip_orphaned_widgets(nb):
                write_notebook(nb, path)
                print(f"fixed: {path}")
        else:
            total = sum(len(ids) for ids in orphaned.values())
            failures.append((path, total))

    if failures:
        print(
            "Orphaned ipywidgets state found in metadata.widgets: state that no\n"
            "cell's widget-view output references anymore. Stale widget content\n"
            "(e.g. old progress-bar text) can silently reappear in the built docs.\n",
            file=sys.stderr,
        )
        for path, total in failures:
            print(f"  {path}: {total} orphaned widget model(s)", file=sys.stderr)
        print(
            "\nRun `python scripts/check_notebook_widgets.py --fix <path...>` to strip it.",
            file=sys.stderr,
        )
        return 1

    return 0


if __name__ == "__main__":
    raise SystemExit(main())

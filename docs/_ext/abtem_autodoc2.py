"""Point sphinx-autodoc2 at the installed abTEM package.

The package location differs between environments (editable checkout locally,
site-packages on CI and Read the Docs), so the path is resolved at build time
from the abtem import rather than hardcoded in _config.yml.
"""

import os

from autodoc2.render.myst_ import MystRenderer


class AbtemMystRenderer(MystRenderer):
    """MyST renderer that collapses argument lists in signature headings.

    autodoc2 puts the full, fully-qualified argument list (and defaults) in
    the heading of every function/method/class - e.g.
    ``transition_potential_multislice_and_detect(waves: abtem.waves.Waves,
    potential: abtem.potentials.iam.BasePotential, ...)``. That's redundant
    with the Parameters field list rendered from the docstring immediately
    below, and makes headings unreadably long for abTEM's many-argument
    functions. Collapsing the heading to ``name(...)`` (or ``name()`` for
    no-arg callables) keeps the heading scannable; full argument details
    still live in the Parameters section.
    """

    def format_args(self, args_info, include_annotations=True, ignore_self=None):
        args = list(args_info)
        if args and ignore_self is not None and args[0][1] == ignore_self:
            args = args[1:]
        return "..." if args else ""


def _set_autodoc2_packages(app, config):
    import abtem

    pkg_dir = os.path.dirname(os.path.abspath(abtem.__file__))
    # autodoc2 requires the path relative to the Sphinx source dir, POSIX-style
    rel_path = os.path.relpath(pkg_dir, app.srcdir).replace(os.sep, "/")
    config.autodoc2_packages = [
        {"path": rel_path, "module": "abtem", "auto_mode": True}
    ]


def _convert_numpydoc_to_rst(app):
    """Run every collected docstring through napoleon to get RST field lists.

    autodoc2 has no napoleon integration (it never fires the
    autodoc-process-docstring event napoleon hooks into), so abTEM's
    NumPy-style "Parameters" sections are otherwise passed straight through
    as plain text, with docutils/MyST collapsing each section into one
    unbroken paragraph. Rewriting the docstrings in-place, after autodoc2
    has finished analysing the package, restores the per-parameter
    rendering the old sphinx.ext.napoleon setup produced.
    """
    from autodoc2.sphinx.utils import get_database
    from sphinx.ext.napoleon import Config as NapoleonConfig, NumpyDocstring

    napoleon_config = NapoleonConfig()
    db = get_database(app.env)
    for item in db._items.values():
        if item.get("doc"):
            item["doc"] = str(NumpyDocstring(item["doc"], napoleon_config))


def _patch_autodoc2_source_line_bug():
    """Work around a crash in autodoc2's DocstringRenderer.

    When autodoc2 is given an explicit `:parser:` (which we set via
    autodoc2_docstring_parser_regexes, to parse the napoleon-converted RST),
    it points the parsed document's reporter at a `lambda li: (source_path,
    li + source_offset)` for source/line lookups. docutils sometimes emits
    a system_message (e.g. the harmless "Enumerated list start value not
    ordinal-1" INFO notice) without a line number, passing `li=None`, which
    makes that lambda raise `TypeError: unsupported operand type(s) for +:
    'NoneType' and 'int'` - an unhandled exception that aborts the whole
    build. docutils' own system_message() already tolerates this pattern
    for its default reporter (it catches AttributeError and falls back to
    an unknown source/line), so we only need autodoc2's directive to fail
    the same soft way instead of raising. Reported upstream; remove once
    fixed: https://github.com/sphinx-extensions2/sphinx-autodoc2/issues
    """
    from autodoc2.sphinx.docstring import DocstringRenderer

    if getattr(DocstringRenderer.run, "_abtem_patched", False):
        return

    original_run = DocstringRenderer.run

    def patched_run(self):
        try:
            return original_run(self)
        except TypeError as exc:
            if "NoneType" not in str(exc):
                raise
            from sphinx.util import logging

            logging.getLogger(__name__).warning(
                f"[[abtem_autodoc2]] Could not render docstring for "
                f"{self.arguments[0]!r} (hit a known autodoc2/docutils "
                f"line-number bug); rendering it empty instead."
            )
            return []

    patched_run._abtem_patched = True
    DocstringRenderer.run = patched_run


def setup(app):
    app.connect("config-inited", _set_autodoc2_packages)
    _patch_autodoc2_source_line_bug()
    # Must run after autodoc2's own builder-inited handler (default
    # priority 500), which populates the database this reads from.
    app.connect("builder-inited", _convert_numpydoc_to_rst, priority=900)
    return {"parallel_read_safe": True, "parallel_write_safe": True}

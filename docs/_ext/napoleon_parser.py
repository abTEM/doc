"""Docutils parser that runs numpy-style docstrings through napoleon before
rST parsing, for use with sphinx-autodoc2 (which bypasses sphinx.ext.autodoc
and therefore napoleon). Referenced as ``napoleon_parser`` in
``autodoc2_docstring_parser_regexes``.
"""

from docutils import frontend
from docutils.parsers import rst
from sphinx.ext.napoleon.docstring import NumpyDocstring


class Parser(rst.Parser):
    settings_spec = rst.Parser.settings_spec
    settings_default_overrides = getattr(
        rst.Parser, "settings_default_overrides", {}
    )

    def parse(self, inputstring, document):
        converted = str(NumpyDocstring(inputstring))
        super().parse(converted, document)

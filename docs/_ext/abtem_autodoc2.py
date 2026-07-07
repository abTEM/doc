"""Point sphinx-autodoc2 at the installed abTEM package.

The package location differs between environments (editable checkout locally,
site-packages on CI and Read the Docs), so the path is resolved at build time
from the abtem import rather than hardcoded in _config.yml.
"""

import os


def _set_autodoc2_packages(app, config):
    import abtem

    pkg_dir = os.path.dirname(os.path.abspath(abtem.__file__))
    # autodoc2 requires the path relative to the Sphinx source dir, POSIX-style
    rel_path = os.path.relpath(pkg_dir, app.srcdir).replace(os.sep, "/")
    config.autodoc2_packages = [
        {"path": rel_path, "module": "abtem", "auto_mode": True}
    ]


def setup(app):
    app.connect("config-inited", _set_autodoc2_packages)
    return {"parallel_read_safe": True, "parallel_write_safe": True}

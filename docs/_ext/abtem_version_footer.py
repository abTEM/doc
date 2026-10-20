"""Show the installed abTEM version (the one the docs were built/tested against)
in the page footer, replacing the theme's static copyright notice.
"""


def _set_abtem_version_footer(app, config):
    try:
        import abtem

        version = abtem.__version__
    except Exception:
        version = "unknown"

    theme_options = dict(config.html_theme_options or {})
    theme_options["extra_footer"] = (
        "<p>Tested against "
        '<a href="https://github.com/abTEM/abTEM">abTEM</a>'
        f" v{version}.</p>"
    )
    config.html_theme_options = theme_options


def setup(app):
    app.connect("config-inited", _set_abtem_version_footer)
    return {"parallel_read_safe": True, "parallel_write_safe": True}

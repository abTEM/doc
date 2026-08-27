"""Show the installed abTEM version (the one the docs were built/tested against)
in the page footer, replacing the theme's static copyright notice.

Also handles the stable/dev docs versions published on GitHub Pages: the
ABTEM_DOCS_VERSION environment variable ("stable" when unset, so local and
Read the Docs builds behave like today) selects between the stable build at
the site root and the development build served under /dev/. Dev builds get a
warning banner linking back to stable and a robots noindex tag; stable builds
get a footer link to the dev docs.
"""

import os

STABLE_URL = "https://abtem.github.io/doc/"
DEV_URL = STABLE_URL + "dev/"


def _is_dev():
    return os.environ.get("ABTEM_DOCS_VERSION", "stable") == "dev"


def _set_abtem_version_footer(app, config):
    try:
        import abtem

        version = abtem.__version__
    except Exception:
        version = "unknown"

    theme_options = dict(config.html_theme_options or {})
    footer = (
        "<p>Tested against "
        '<a href="https://github.com/abTEM/abTEM">abTEM</a>'
        f" v{version}."
    )
    if _is_dev():
        theme_options["announcement"] = (
            "This is the <strong>development</strong> documentation, built from "
            f'the latest main branch. <a href="{STABLE_URL}">Switch to the '
            "stable version</a>."
        )
        footer += " Development build."
    else:
        footer += (
            f' Also available: <a href="{DEV_URL}">development version</a>.'
        )
    footer += "</p>"
    theme_options["extra_footer"] = footer
    config.html_theme_options = theme_options


def _add_noindex(app, pagename, templatename, context, doctree):
    # Keep the dev docs out of search results so readers land on stable.
    if _is_dev():
        context["metatags"] = (
            context.get("metatags", "")
            + '\n    <meta name="robots" content="noindex">'
        )


def setup(app):
    app.connect("config-inited", _set_abtem_version_footer)
    app.connect("html-page-context", _add_noindex)
    return {"parallel_read_safe": True, "parallel_write_safe": True}

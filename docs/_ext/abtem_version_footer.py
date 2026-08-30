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
ABTEM_DEV_BRANCH_URL = "https://github.com/abTEM/abTEM/tree/dev"
_ANNOUNCEMENT_CLOSE_CLASS = "abtem-announcement-close"
_ANNOUNCEMENT_DISMISSED_KEY = "abtem_dev_announcement_dismissed"


def _is_dev():
    return os.environ.get("ABTEM_DOCS_VERSION", "stable") == "dev"


def _set_abtem_version_footer(app, config):
    try:
        import abtem

        version = abtem.__version__
    except Exception:
        version = "unknown"

    theme_options = dict(config.html_theme_options or {})
    if _is_dev():
        theme_options["announcement"] = (
            "This is the <strong>development</strong> documentation, "
            f'including unreleased work in <a href="{ABTEM_DEV_BRANCH_URL}">'
            f'abTEM/dev</a>. <a href="{STABLE_URL}">Switch to the stable '
            "version</a>."
            f' <a href="#" class="{_ANNOUNCEMENT_CLOSE_CLASS} ms-3 my-1 '
            'align-baseline" aria-label="Dismiss">'
            '<i class="fa-solid fa-xmark"></i></a>'
        )
        footer = (
            "<p>Tested against pre-release "
            f'<a href="{ABTEM_DEV_BRANCH_URL}">abTEM v{version}</a>.'
        )
    else:
        footer = (
            "<p>Tested against "
            '<a href="https://github.com/abTEM/abTEM">abTEM</a>'
            f" v{version}."
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


# Configuring an `announcement` (which only dev builds do, above) makes
# sphinx-book-theme also render pydata-sphinx-theme's own navbar - needed to
# host the banner - alongside its own separate article-header toggle button.
# That leaves two elements matching `.primary-toggle`/`.secondary-toggle` in
# the DOM; on mobile the navbar one is CSS-hidden but pydata-sphinx-theme.js
# wires its dialog-opening click handler to it anyway, since it looks it up
# with a plain (singular) `querySelector`. The one actually visible on
# mobile - sphinx-book-theme's article-header button - is left with no
# listener at all, so tapping it does nothing. Forwarding clicks from any
# extra duplicate to the first (the one the theme's own script wired up)
# fixes this without touching their minified code; a no-op when there's only
# one of each, i.e. on stable builds without the banner.
_SIDEBAR_TOGGLE_DUPLICATE_FIX = """
document.addEventListener("DOMContentLoaded", () => {
  for (const cls of [".primary-toggle", ".secondary-toggle"]) {
    const toggles = document.querySelectorAll(cls);
    for (let i = 1; i < toggles.length; i++) {
      toggles[i].addEventListener("click", () => toggles[0].click());
    }
  }
});
"""

# pydata-sphinx-theme only adds a close button to the announcement banner
# when it's configured as a remote URL it fetches itself; a plain HTML
# string (what _set_abtem_version_footer sets) renders with no way to
# dismiss it. Add one ourselves - clicking it hides the banner and
# remembers that in localStorage so it stays hidden on future visits (a
# closed banner reappearing on every page load would be worse than no
# close button at all).
_ANNOUNCEMENT_CLOSE_FIX = f"""
document.addEventListener("DOMContentLoaded", () => {{
  const banner = document.querySelector(".bd-header-announcement");
  if (!banner) return;
  if (localStorage.getItem("{_ANNOUNCEMENT_DISMISSED_KEY}")) {{
    banner.remove();
    return;
  }}
  const closeBtn = banner.querySelector(".{_ANNOUNCEMENT_CLOSE_CLASS}");
  if (!closeBtn) return;
  closeBtn.addEventListener("click", (event) => {{
    event.preventDefault();
    localStorage.setItem("{_ANNOUNCEMENT_DISMISSED_KEY}", "1");
    banner.remove();
  }});
}});
"""


def _add_dev_banner_scripts(app, pagename, templatename, context, doctree):
    if _is_dev():
        app.add_js_file(None, body=_SIDEBAR_TOGGLE_DUPLICATE_FIX)
        app.add_js_file(None, body=_ANNOUNCEMENT_CLOSE_FIX)


def setup(app):
    app.connect("config-inited", _set_abtem_version_footer)
    app.connect("html-page-context", _add_noindex)
    app.connect("html-page-context", _add_dev_banner_scripts)
    return {"parallel_read_safe": True, "parallel_write_safe": True}

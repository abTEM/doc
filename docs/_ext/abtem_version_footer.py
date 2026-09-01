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
# sphinx-book-theme fall back to also rendering pydata-sphinx-theme's own
# full default navbar - complete with its own search bar and icons - to
# have somewhere to host the banner, alongside its own separate, normally-
# sufficient article-header bar. The two aren't just redundant visually
# (a second search bar, duplicate icons, on desktop where both show): they
# also leave two elements matching `.primary-toggle`/`.secondary-toggle` in
# the DOM, and pydata-sphinx-theme.js wires its dialog-opening click handler
# to whichever one a plain (singular) `querySelector` finds first - the
# navbar copy, which mobile's CSS hides. The one actually visible on
# mobile - sphinx-book-theme's article-header button - was then left with
# no listener at all, so tapping it did nothing.
#
# Tried removing the redundant navbar outright instead of working around
# this, so there'd only ever be one `.primary-toggle` for querySelector to
# find - but pydata-sphinx-theme.js loads with `defer`, so by spec it runs
# right after parsing finishes and BEFORE DOMContentLoaded fires; waiting
# for that event to do the removal was always too late; the theme had
# already wired the copy being removed, orphaning the survivor exactly as
# before. Inline scripts can't be deferred to force a specific order
# either (the attribute is spec'd to have no effect on them). So: hide the
# navbar with plain CSS instead (no timing dependency - the element simply
# never paints) and let the theme wire whatever it finds; forwarding
# clicks from the visible button to that (hidden but correctly wired) one
# makes tapping it work regardless of which element got the listener.
# Both are no-ops when the navbar was never rendered, i.e. on stable
# builds without the banner.
_HIDE_DUPLICATE_NAVBAR_CSS = (
    "<style>header.bd-header.navbar{display:none!important}</style>"
)
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


def _add_dev_banner_extras(app, pagename, templatename, context, doctree):
    if _is_dev():
        # add_css_file() only accepts a real file, not inline content, so
        # this rides along on the same head-injection point as the
        # noindex meta tag above.
        context["metatags"] = (
            context.get("metatags", "") + "\n    " + _HIDE_DUPLICATE_NAVBAR_CSS
        )
        app.add_js_file(None, body=_SIDEBAR_TOGGLE_DUPLICATE_FIX)
        app.add_js_file(None, body=_ANNOUNCEMENT_CLOSE_FIX)


def setup(app):
    app.connect("config-inited", _set_abtem_version_footer)
    app.connect("html-page-context", _add_noindex)
    app.connect("html-page-context", _add_dev_banner_extras)
    return {"parallel_read_safe": True, "parallel_write_safe": True}

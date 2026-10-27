"""Publications list for docs/papers/index.md, built from refs.bib.

Zensical has no BibTeX plugin, so its macros support loads this module (see
[project.plugins.macros] in zensical.toml). The text matches what the
mkdocs-bibtex plugin produced before: entries formatted with pybtex's plain
style, and the full list in the same footnote markup, so each entry keeps its
"#fn:<key>" anchor (but without the back-links, which had nothing to go to).

    {{ cite("roadfilt2022lidar") }}   one formatted entry
    {{ full_bibliography() }}         every entry, in refs.bib order
"""

import re
from pathlib import Path

from pybtex.backends.html import Backend as HtmlBackend
from pybtex.backends.markdown import Backend as MarkdownBackend
from pybtex.database import parse_file
from pybtex.style.formatting.plain import Style

BIB_FILE = Path(__file__).parent / "refs.bib"


def define_env(env):
    entries = parse_file(BIB_FILE).entries
    style = Style()

    def reference(key, backend):
        if key not in entries:
            raise KeyError(f"Unknown key {key!r} in {BIB_FILE.name}")
        return style.format_entry("", entries[key]).text.render(backend).replace("\n", " ")

    @env.macro
    def cite(key):
        text = reference(key, MarkdownBackend())
        # Same clean-up of escape sequences as mkdocs-bibtex
        return text.replace("\\(", "(").replace("\\)", ")").replace("\\.", ".")

    @env.macro
    def full_bibliography():
        items = []
        for key in entries:
            text = reference(key, HtmlBackend())
            # Drop the wrappers pybtex puts around {braced} BibTeX text
            while '<span class="bibtex-protected">' in text:
                text = re.sub(r'<span class="bibtex-protected">((?:(?!<span).)*?)</span>', r"\1", text)
            items.append(f'<li id="fn:{key}"><p>{text}</p></li>')
        return '<div class="footnote">\n<hr>\n<ol>\n' + "\n".join(items) + "\n</ol>\n</div>"

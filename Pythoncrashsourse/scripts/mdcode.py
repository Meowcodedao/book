"""Shared helpers: find fenced code blocks in the book's Markdown files.

Used by check_source.py and qa_translation.py so source and translation are
parsed exactly the same way.
"""
import re

MARKERS = "❶❷❸❹❺❻❼❽❾❿"
FENCE = re.compile(r"^```(\w*)\n(.*?)^```$", re.S | re.M)
LABEL = re.compile(r"\*\*([^*\n]+)\*\*\n\n$")


def code_blocks(md):
    """Yield dicts: lang, code, label (filename shown before the block), line."""
    for m in FENCE.finditer(md):
        before = md[max(0, m.start() - 200):m.start()]
        lab = LABEL.search(before)
        yield {
            "lang": m.group(1),
            "code": m.group(2).rstrip("\n"),
            "label": lab.group(1) if lab else "",
            "line": md.count("\n", 0, m.start()) + 1,
        }


def strip_gutter(code):
    """Remove the 2-char callout gutter ("❶ " or "  ") added when a block has markers."""
    lines = code.split("\n")
    if any(l[:1] in MARKERS for l in lines):
        return "\n".join(l[2:] if l[:1] in MARKERS or l.startswith("  ") else l.lstrip() for l in lines)
    return code

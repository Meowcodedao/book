#!/usr/bin/env python3
"""Check translated chapters against glossary/glossary.md.

A glossary row whose Notes column contains "Tránh: a, b" means the Vietnamese
words a and b must not be used for that term. This script lists every place
a translated chapter uses an avoided word (outside code). It only reports;
it never edits anything.

Usage:
    python3 scripts/glossary_check.py [chapter-01 ...]   (default: all translated files)
"""
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
GLOSSARY = ROOT / "glossary" / "glossary.md"


def load_avoid():
    """{preferred Vietnamese: [avoided words]} from rows with 'Tránh:' in Notes."""
    avoid = {}
    for line in GLOSSARY.read_text(encoding="utf-8").splitlines():
        cells = [c.strip() for c in line.strip().strip("|").split("|")]
        if len(cells) >= 3:
            m = re.search(r"Tránh:\s*(.+)", cells[2])
            if m:
                avoid[cells[1]] = [w.strip() for w in m.group(1).split(",") if w.strip()]
    return avoid


def find_avoided(text, avoid):
    """Yield (preferred, avoided) pairs found in text, ignoring code."""
    text = re.sub(r"```.*?```", "", text, flags=re.S)
    text = re.sub(r"`[^`]*`", "", text).lower()
    for term, words in avoid.items():
        for w in words:
            if re.search(rf"(?<!\w){re.escape(w.lower())}(?!\w)", text):
                yield term, w


def main():
    avoid = load_avoid()
    names = sys.argv[1:] or sorted(p.stem for p in (ROOT / "translated").glob("*.md"))
    found = 0
    for name in names:
        path = ROOT / "translated" / f"{name.removesuffix('.md')}.md"
        if not path.exists():
            continue
        for n, line in enumerate(path.read_text(encoding="utf-8").splitlines(), 1):
            for term, bad in find_avoided(line, avoid):
                found += 1
                print(f"{path.relative_to(ROOT)}:{n}: '{bad}' — glossary: '{term}'")
    print(f"{found} glossary issue(s)")


if __name__ == "__main__":
    main()

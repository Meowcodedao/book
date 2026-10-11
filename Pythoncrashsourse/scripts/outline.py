#!/usr/bin/env python3
"""Read the PDF bookmarks (outline) and build the list of book units.

A "unit" is one translatable file: a chapter, the introduction, a part
opener, an appendix, ... Page ranges come from the bookmarks resolved by
MuPDF (`mutool run`), so nothing is guessed from the text.

Usage:
    python3 scripts/outline.py [book.pdf]

Output:
    original/extracted/outline.tsv   full outline: depth, pdf page (1-based), title
    original/units.json              ordered list of units with page ranges
"""
import json
import re
import subprocess
import sys
import tempfile
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent

JS = r"""
var doc = Document.openDocument(scriptArgs[0]);
function walk(items, depth) {
  for (var i = 0; i < items.length; i++) {
    var it = items[i];
    var p = -1;
    try { p = doc.resolveLink(it.uri); } catch (e) {}
    print(depth + "\t" + (p + 1) + "\t" + it.title.replace(/[\r\n]/g, "").trim());
    if (it.down) walk(it.down, depth + 1);
  }
}
walk(doc.loadOutline(), 0);
print("PAGES\t" + doc.countPages());
"""

# Printed page number = PDF page - OFFSET (checked against page footers:
# PDF page 133 shows printed "100").
PRINTED_OFFSET = 33


def slug_for(title):
    m = re.match(r"Chapter (\d+):", title)
    if m:
        return f"chapter-{int(m.group(1)):02d}"
    m = re.match(r"Part (I+):", title)
    if m:
        return f"part-{len(m.group(1))}"
    m = re.match(r"Project (\d+):", title)
    if m:
        return f"project-{m.group(1)}"
    m = re.match(r"Appendix ([A-Z]):", title)
    if m:
        return f"appendix-{m.group(1).lower()}"
    return {"Acknowledgments": "acknowledgments", "Introduction": "introduction",
            "Afterword": "afterword", "Index": "index"}.get(title)


def main():
    pdf = Path(sys.argv[1]) if len(sys.argv) > 1 else next(ROOT.glob("*.pdf"))
    with tempfile.NamedTemporaryFile("w", suffix=".js", delete=False) as f:
        f.write(JS)
        js = f.name
    out = subprocess.run(["mutool", "run", js, str(pdf)], capture_output=True, text=True, check=True).stdout
    Path(js).unlink()

    rows, n_pages = [], None
    for line in out.splitlines():
        parts = line.split("\t")
        if parts[0] == "PAGES":
            n_pages = int(parts[1])
        elif len(parts) == 3:
            rows.append((int(parts[0]), int(parts[1]), parts[2]))

    extracted = ROOT / "original" / "extracted"
    extracted.mkdir(parents=True, exist_ok=True)
    with open(extracted / "outline.tsv", "w", encoding="utf-8") as f:
        f.write("depth\tpdf_page\tprinted_page\ttitle\n")
        for d, p, t in rows:
            printed = p - PRINTED_OFFSET if p > PRINTED_OFFSET else ""  # front matter uses roman numerals
            f.write(f"{d}\t{p}\t{printed}\t{t}\n")

    starts = []
    for d, p, t in rows:
        slug = slug_for(t)
        if slug and all(s["slug"] != slug for s in starts):
            starts.append({"slug": slug, "title": t, "start": p})
    # Everything before the first unit is front matter (cover, copyright, TOC).
    starts.insert(0, {"slug": "front-matter", "title": "Front Matter", "start": 1})
    for i, u in enumerate(starts):
        u["end"] = starts[i + 1]["start"] - 1 if i + 1 < len(starts) else n_pages
        u["printed_start"] = u["start"] - PRINTED_OFFSET
        u["printed_end"] = u["end"] - PRINTED_OFFSET
        # Units that are reference material, not prose to translate.
        u["translate"] = u["slug"] not in ("front-matter", "index")
        u["order"] = i

    with open(ROOT / "original" / "units.json", "w", encoding="utf-8") as f:
        json.dump({"pdf": pdf.name, "pages": n_pages, "printed_offset": PRINTED_OFFSET,
                   "units": starts}, f, indent=2, ensure_ascii=False)
    for u in starts:
        print(f'{u["order"]:2d} {u["slug"]:16s} pdf {u["start"]:3d}-{u["end"]:3d}  {u["title"]}')


if __name__ == "__main__":
    main()

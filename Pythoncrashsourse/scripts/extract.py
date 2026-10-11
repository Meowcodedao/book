#!/usr/bin/env python3
"""Step 1: extract the PDF into a compact, font-aware JSONL file.

Uses `mutool draw -F stext` (MuPDF) which keeps, for every character, its
font name, size and position. That lets later steps tell code (monospace
font) from prose, and rebuild code indentation from x-coordinates instead
of trusting whitespace in a plain-text dump.

The PDF is only read, never modified.

Usage:
    python3 scripts/extract.py [book.pdf]

Output:
    original/extracted/pages.jsonl   one JSON object per PDF page
    original/extracted/book.txt      plain `pdftotext -layout` dump (reference only)
"""
import json
import subprocess
import sys
import tempfile
import xml.etree.ElementTree as ET
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
OUT_DIR = ROOT / "original" / "extracted"


def find_pdf():
    pdfs = sorted(ROOT.glob("*.pdf"))
    if len(pdfs) != 1:
        sys.exit(f"Expected exactly one PDF in {ROOT}, found {len(pdfs)}; pass the path explicitly.")
    return pdfs[0]


def span_of(font_el):
    chars = list(font_el.iter("char"))
    if not chars:
        return None
    return {
        "font": font_el.get("name"),
        "size": float(font_el.get("size")),
        "x0": round(float(chars[0].get("x")), 2),
        "x1": round(float(chars[-1].get("quad").split()[2]), 2),
        "y": round(float(chars[0].get("y")), 2),
        # x position of every char, needed to rebuild spacing inside code
        "xs": [round(float(c.get("x")), 2) for c in chars],
        "text": "".join(c.get("c") for c in chars),
    }


def main():
    pdf = Path(sys.argv[1]) if len(sys.argv) > 1 else find_pdf()
    OUT_DIR.mkdir(parents=True, exist_ok=True)

    with tempfile.TemporaryDirectory() as tmp:
        xml_path = Path(tmp) / "book.xml"
        subprocess.run(["mutool", "draw", "-q", "-F", "stext", "-o", str(xml_path), str(pdf)],
                       check=True, stderr=subprocess.DEVNULL)

        n_pages = 0
        with open(OUT_DIR / "pages.jsonl", "w", encoding="utf-8") as out:
            for _, el in ET.iterparse(xml_path, events=("end",)):
                if el.tag != "page":
                    continue
                page = {"page": int(el.get("id").removeprefix("page")),
                        "width": float(el.get("width")),
                        "height": float(el.get("height")),
                        "blocks": []}
                for b in el.iter("block"):
                    lines = []
                    for ln in b.iter("line"):
                        spans = [s for s in (span_of(f) for f in ln.iter("font")) if s]
                        if spans:
                            lines.append(spans)
                    if lines:
                        page["blocks"].append(lines)
                out.write(json.dumps(page, ensure_ascii=False) + "\n")
                el.clear()
                n_pages += 1

    subprocess.run(["pdftotext", "-layout", str(pdf), str(OUT_DIR / "book.txt")], check=True)
    print(f"{pdf.name}: {n_pages} pages -> {OUT_DIR.relative_to(ROOT)}/pages.jsonl, book.txt")


if __name__ == "__main__":
    main()

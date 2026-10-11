#!/usr/bin/env python3
"""QA a translated unit against its English source.

Compares original/chapters/<slug>.md with translated/<slug>.md, block by block.
Both files are split into blocks (blank-line separated; a fenced code block
is one block) and every block gets a type. Because the translation must keep
the source structure, the two type sequences must be identical.

Checks (ERROR = must fix, WARN = review by hand):
  ERROR  block structure differs (missing / extra / reordered blocks)
  ERROR  a code block differs from the source in any character
  ERROR  heading level changed
  ERROR  page markers, box markers or callout markers (❶❷...) differ
  ERROR  inline `code` spans of a block differ from the source
  ERROR  URLs differ
  ERROR  a filename label (**name.py** before code) differs
  WARN   a prose block is identical to the English (untranslated?)
  WARN   translation much shorter/longer than the source block
  WARN   [TODO ...] markers left in the text
  WARN   glossary: a term marked "Tránh: ..." in glossary.md is used

Usage:
    python3 scripts/qa_translation.py chapter-01 [chapter-02 ...]
Output:
    qa/<slug>-qa.md       (exit code 1 if any ERROR)
"""
import difflib
import re
import sys
from collections import Counter
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(Path(__file__).resolve().parent))
from glossary_check import load_avoid, find_avoided  # noqa: E402

URL = re.compile(r"https?://[^\s*)`>]+|www\.[^\s*)`>]+")
INLINE = re.compile(r"(`+)(.+?)\1")
MARKERS = re.compile(r"[❶❷❸❹❺❻❼❽❾❿]")


def blocks(md):
    """Split Markdown into blocks; fenced code stays in one block."""
    out, buf, in_code = [], [], False
    for line in md.split("\n"):
        if line.startswith("```"):
            buf.append(line)
            if in_code:
                out.append("\n".join(buf))
                buf = []
            in_code = not in_code
            continue
        if in_code:
            buf.append(line)
        elif line.strip() == "":
            if buf:
                out.append("\n".join(buf))
                buf = []
        else:
            buf.append(line)
    if buf:
        out.append("\n".join(buf))
    return out


def btype(b):
    if b.startswith("```"):
        return "code"
    if b.startswith("<!-- pdf-page"):
        return "page"
    if b.startswith("<!--"):
        return "comment"
    m = re.match(r"(#+) ", b)
    if m:
        return f"h{len(m.group(1))}"
    if b.startswith("> **"):
        return "note"
    if b.startswith(">"):
        return "quote"
    if b.startswith("- "):
        return "bullet"
    if b.startswith("|"):
        return "table"
    if re.fullmatch(r"\*\*[^*\n]+\*\*", b):
        return "label"               # filename label or "Try It Yourself"
    if re.match(r"\*(Figure|Table|Hình|Bảng) ", b):
        return "caption"
    return "para"


def prose(b):
    """Text with code/URLs removed, for length and untranslated checks."""
    b = INLINE.sub("", b)
    b = URL.sub("", b)
    return re.sub(r"[*_>#|\-]", " ", b).strip()


def check(slug):
    src_path = ROOT / "original" / "chapters" / f"{slug}.md"
    tr_path = ROOT / "translated" / f"{slug}.md"
    if not tr_path.exists():
        sys.exit(f"{tr_path.relative_to(ROOT)} does not exist")
    src, tr = blocks(src_path.read_text(encoding="utf-8")), blocks(tr_path.read_text(encoding="utf-8"))
    errors, warns = [], []
    avoid = load_avoid()

    ts, tt = [btype(b) for b in src], [btype(b) for b in tr]
    if ts != tt:
        # first divergence is the useful clue
        i = next((k for k, (a, b) in enumerate(zip(ts, tt)) if a != b), min(len(ts), len(tt)))
        msg = (f"Block structure differs: source has {len(ts)} blocks, translation {len(tt)}. "
               f"First difference at block {i + 1}: source `{ts[i] if i < len(ts) else '-'}` "
               f"vs translation `{tt[i] if i < len(tt) else '-'}`.")
        if i < len(src):
            msg += f"\n  - source: {src[i][:120]!r}"
        if i < len(tr):
            msg += f"\n  - translation: {tr[i][:120]!r}"
        errors.append(msg)

    page = "?"
    for i, (s, t) in enumerate(zip(src, tr)):
        kind = btype(s)
        if kind == "page":
            page = re.search(r"pdf-page: (\d+)", s).group(1)
        where = f"block {i + 1} (pdf-page {page})"
        if btype(t) != kind:
            continue                                   # already reported above
        immutable = kind in ("code", "page", "comment") or (kind == "label" and "." in s)  # filename label
        if immutable:
            if s != t:
                diff = "\n".join(f"    {l}" for l in difflib.unified_diff(
                    s.split("\n"), t.split("\n"), "source", "translation", lineterm="", n=0))
                errors.append(f"{where}: {kind} block changed:\n\n{diff}\n")
            continue
        if MARKERS.findall(s) != MARKERS.findall(t):
            errors.append(f"{where}: callout markers {MARKERS.findall(s)} → {MARKERS.findall(t)}")
        sc = Counter(m.group(2) for m in INLINE.finditer(s))
        tc = Counter(m.group(2) for m in INLINE.finditer(t))
        if sc != tc:
            errors.append(f"{where}: inline code differs; missing {sorted((sc - tc).elements())}, "
                          f"extra {sorted((tc - sc).elements())}")
        su, tu = sorted(URL.findall(s)), sorted(URL.findall(t))
        if su != tu:
            errors.append(f"{where}: URLs differ: {su} → {tu}")
        if kind == "table":
            if [r.count("|") for r in s.split("\n")] != [r.count("|") for r in t.split("\n")]:
                errors.append(f"{where}: table rows/columns changed")
        ps, pt = prose(s), prose(t)
        if len(ps) > 25 and ps == pt:
            warns.append(f"{where}: identical to the English source (untranslated?): {s[:80]!r}")
        elif len(ps) > 80:
            ratio = len(pt) / max(1, len(ps))
            if ratio < 0.7 or ratio > 2.0:
                warns.append(f"{where}: length ratio {ratio:.2f} vs source — check for omissions/additions")
        for term, bad in find_avoided(t, avoid):
            warns.append(f"{where}: glossary — '{bad}' used; glossary says '{term}'")

    todos = re.findall(r"\[TODO[^\]]*\]", "\n".join(tr))
    if todos:
        warns.append(f"{len(todos)} TODO marker(s) left: {todos[:5]}")

    status = "PASS" if not errors else "FAIL"
    lines = [f"# QA: {slug}", "",
             f"- Source: `original/chapters/{slug}.md` ({len(src)} blocks)",
             f"- Translation: `translated/{slug}.md` ({len(tr)} blocks)",
             f"- Code blocks: {ts.count('code')} in source, {tt.count('code')} in translation",
             f"- Automatic result: **{status}** — {len(errors)} error(s), {len(warns)} warning(s)", "",
             "## Errors", ""] + ([f"- {e}" for e in errors] or ["None."]) + \
            ["", "## Warnings", ""] + ([f"- {w}" for w in warns] or ["None."]) + [""]
    out = ROOT / "qa" / f"{slug}-qa.md"
    out.write_text("\n".join(lines), encoding="utf-8")
    print(f"{slug}: {status} ({len(errors)} errors, {len(warns)} warnings) -> {out.relative_to(ROOT)}")
    return not errors


if __name__ == "__main__":
    if len(sys.argv) < 2:
        sys.exit(__doc__)
    ok = all([check(s.removesuffix(".md")) for s in sys.argv[1:]])
    sys.exit(0 if ok else 1)

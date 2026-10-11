#!/usr/bin/env python3
"""Translate by block: export numbered source blocks, assemble the translation.

Immutable blocks (code, page/box comments, filename labels) are never retyped:
`assemble` copies them byte-for-byte from the source, so code cannot drift.

    python3 scripts/segments.py export chapter-01
        -> work/chapter-01.en.md: every source block; translatable ones are
           preceded by [[id]], immutable ones are shown for context only.

    (write translations into work/chapter-01.vi.md, or several files
     work/chapter-01.vi.part1.md, ...part2.md — read in name order:)
        [[12]]
        Bản dịch của block 12.

        [[13]]
        ...

    python3 scripts/segments.py todo chapter-01      ids not translated yet
    python3 scripts/segments.py assemble chapter-01  -> translated/chapter-01.md
"""
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(Path(__file__).resolve().parent))
from qa_translation import blocks, btype  # noqa: E402

WORK = ROOT / "work"
ID = re.compile(r"^\[\[(\d+)\]\]\s*$", re.M)


def translatable(b):
    t = btype(b)
    if t in ("code", "page", "comment"):
        return False
    if t == "label" and "." in b:          # filename label, e.g. **survey.py**
        return False
    return True


def source_blocks(slug):
    return blocks((ROOT / "original" / "chapters" / f"{slug}.md").read_text(encoding="utf-8"))


def load_translations(slug):
    out = {}
    for f in sorted(WORK.glob(f"{slug}.vi*.md")):
        text = f.read_text(encoding="utf-8")
        parts = ID.split(text)
        for i in range(1, len(parts), 2):
            n = int(parts[i])
            if n in out:
                sys.exit(f"{f.name}: block [[{n}]] translated twice")
            out[n] = parts[i + 1].strip()
    return out


def export(slug):
    WORK.mkdir(exist_ok=True)
    lines = []
    for i, b in enumerate(source_blocks(slug), 1):
        lines.append(f"[[{i}]]\n{b}" if translatable(b) else b)
    path = WORK / f"{slug}.en.md"
    path.write_text("\n\n".join(lines) + "\n", encoding="utf-8")
    n = sum(translatable(b) for b in source_blocks(slug))
    print(f"{path.relative_to(ROOT)}: {n} blocks to translate")


def todo(slug):
    src, tr = source_blocks(slug), load_translations(slug)
    need = [i for i, b in enumerate(src, 1) if translatable(b)]
    missing = [i for i in need if i not in tr]
    extra = sorted(set(tr) - set(need))
    print(f"{slug}: {len(need) - len(missing)}/{len(need)} translated"
          + (f"; missing {missing[:20]}{'…' if len(missing) > 20 else ''}" if missing else "")
          + (f"; unknown ids {extra}" if extra else ""))
    return not missing and not extra


def assemble(slug):
    if not todo(slug):
        sys.exit(1)
    src, tr = source_blocks(slug), load_translations(slug)
    out = [tr[i] if translatable(b) else b for i, b in enumerate(src, 1)]
    path = ROOT / "translated" / f"{slug}.md"
    path.write_text("\n\n".join(out) + "\n", encoding="utf-8")
    print(f"-> {path.relative_to(ROOT)}")


if __name__ == "__main__":
    if len(sys.argv) != 3 or sys.argv[1] not in ("export", "todo", "assemble"):
        sys.exit(__doc__)
    {"export": export, "todo": todo, "assemble": assemble}[sys.argv[1]](sys.argv[2])

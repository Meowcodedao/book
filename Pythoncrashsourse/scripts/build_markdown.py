#!/usr/bin/env python3
"""Step 3: turn the font-aware extraction into one Markdown file per unit.

Input : original/extracted/pages.jsonl   (scripts/extract.py)
        original/units.json              (scripts/outline.py)
Output: original/chapters/<slug>.md
        logs/build_markdown.log          (warnings worth checking against the PDF)

How the book's layout maps to Markdown (fonts identified from the PDF):

    Futura-Bold 12                 -> ## heading
    Futura-CondensedBoldOblique 12 -> ### heading
    Futura-CondensedBold 10        -> #### heading
    NewBaskerville (body)          -> paragraphs; italic -> *x*, bold -> **x**
    TheSansMono (inline)           -> `code`
    TheSansMono (whole lines)      -> fenced code block; columns rebuilt from
                                      character x-positions (monospace width =
                                      font size / 2), so indentation is exact
    Wingdings2 u v w x ...         -> callout markers ❶ ❷ ❸ ❹ ...
    "N o t e" (DogmaBold 7.5)      -> > **Note** ... (notes are italic in print; inside a
                                      note, roman words become *x*)
    NewBaskerville 9 (indented)    -> > block quote
    "Try It Yourself" box          -> <!-- box --> ... <!-- /box -->
    Futura-BookOblique "Figure.."  -> *Figure x-y: ...*
    margin filename next to code   -> **filename.py** line before the block
    footer (running head + page #) -> dropped

Every element starting on a new PDF page is preceded by
<!-- pdf-page: N | printed: M --> so any passage can be checked in the PDF.

The PDF itself is never touched; this only reads the JSONL.
"""
import json
import re
import statistics
import sys
from collections import Counter
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
EXTRACTED = ROOT / "original" / "extracted"
CHAPTERS = ROOT / "original" / "chapters"
LOG = ROOT / "logs" / "build_markdown.log"

MARKERS = "❶❷❸❹❺❻❼❽❾❿"
FOOTER_Y = 630          # page height is 666; footers sit at y=642
CODE_LEADING = 10.5     # baseline distance between code lines
warnings = []

# Line-end hyphens that belong to real compounds but never occur mid-line in
# the book, so the vocabulary check cannot see them (from logs review).
KEEP_HYPHEN = {"off-by", "to-follow", "fine-grained", "form-building", "two-step"}


def warn(page, msg):
    warnings.append(f"pdf-page {page}: {msg}")


# ---------------------------------------------------------------- spans ---

def is_mono(s):
    return s["font"].startswith("TheSansMono")


def marker_char(ch):
    """Wingdings2 'u'..'~' (or private-use U+F075..) -> ❶..❿."""
    o = ord(ch)
    if o >= 0xF000:
        o -= 0xF000
    i = o - ord("u")
    return MARKERS[i] if 0 <= i < len(MARKERS) else None


def span_style(s):
    f = s["font"]
    if is_mono(s):
        return "code"
    if f == "Wingdings2":
        return "marker"
    if f.startswith("NewBaskerville-Roman-SC") or f.endswith("-SC750"):
        return "smallcaps"
    if "Bold" in f and "Italic" in f:
        return "bolditalic"
    if f.startswith("NewBaskerville-Bold") or f.startswith("Futura-Heavy"):
        return "bold"
    if "Italic" in f or "Oblique" in f:
        return "italic"
    return "plain"


def span_text(s):
    f, t = s["font"], s["text"]
    if f == "Wingdings2":
        out = "".join(marker_char(c) or (" " if c == " " else c) for c in t)
        return out
    if f == "Webdings":
        return t.replace("4", "▸")            # menu path separator: File▸Save As
    if f == "Symbol" or t.lstrip().startswith("•"):
        return t.replace("•", "", 1).lstrip() if "•" in t else t
    if span_style(s) == "smallcaps":
        return t.upper()                        # keys such as ENTER, CTRL
    return t


# --------------------------------------------------------- inline runs ---

def line_runs(spans):
    """A prose line as a list of (style, text) runs."""
    runs = []
    for s in spans:
        st, tx = span_style(s), span_text(s)
        if st == "marker":
            st = "plain"
        if tx:
            runs.append([st, tx])
    return runs


def join_runs(lines_runs, vocab, page):
    """Join the runs of consecutive lines into one paragraph.

    Handles end-of-line hyphenation: InDesign breaks words with '-' (or a
    soft hyphen U+00AD). The hyphen is dropped unless the hyphenated form is
    attested elsewhere in the book and the joined form is not.
    """
    out = []
    for runs in lines_runs:
        runs = [list(r) for r in runs]
        if not runs:
            continue
        if out:
            prev = out[-1]
            prev[1] = prev[1].rstrip(" ")
            first = runs[0]
            pt, nt = prev[1], first[1]
            if pt.endswith("\xad"):
                prev[1] = pt[:-1]
            elif re.search(r"[A-Za-z]-$", pt) and re.match(r"[a-z]", nt) and prev[0] != "code":
                left = re.search(r"([A-Za-z]+)-$", pt).group(1)
                right = re.match(r"[a-z]+", nt).group(0)
                joined, hyph = (left + right).lower(), f"{left}-{right}".lower()
                if hyph in KEEP_HYPHEN or vocab["hyph"][hyph] and not vocab["word"][joined]:
                    pass                          # genuine compound: keep "-"
                else:
                    prev[1] = pt[:-1]
                    if not vocab["word"][joined]:
                        warn(page, f"dehyphenated unseen word '{left}{right}' (from '{left}-{right}')")
            elif pt.endswith(("—", "/")) or nt.startswith("—") or \
                    re.match(r"\.(com|org|net|io|py|txt|html|json)\b", nt) and re.search(r"\w$", pt):
                # em dash / path / domain or filename broken before its extension
                pass                              # em dash / path: no space
            elif prev[0] == first[0] and prev[0] in ("code", "italic") and (
                    re.match(r"[.,)\]_(:]", nt) or re.search(r"[._(\[/\\]$", pt)):
                pass                              # identifier broken across lines
            else:
                prev[1] = pt + " "
        out.extend(runs)
    # merge adjacent runs with the same style
    merged = []
    for st, tx in out:
        if merged and merged[-1][0] == st:
            merged[-1][1] += tx
        else:
            merged.append([st, tx])
    return merged


def render_runs(runs):
    parts = []
    for st, tx in runs:
        tx = tx.replace("\xad", "")
        if st in ("plain", "smallcaps") or not tx.strip() or st != "code" and not re.search(r"\w", tx):
            parts.append(tx)
            continue
        lead = tx[: len(tx) - len(tx.lstrip())]
        trail = tx[len(tx.rstrip()):]
        core = tx.strip()
        if st == "code":
            fence = "``" if "`" in core else "`"
            pad = " " if core.startswith("`") or core.endswith("`") else ""
            core = f"{fence}{pad}{core}{pad}{fence}"
        elif st == "italic":
            core = f"*{core}*"
        elif st == "bold":
            core = f"**{core}**"
        elif st == "bolditalic":
            core = f"***{core}***"
        parts.append(lead + core + trail)
    text = "".join(parts)
    return re.sub(r"[ \t]+", " ", text).strip()


# ----------------------------------------------------------- vocabulary ---

def build_vocab(pages):
    """Words seen mid-line, used to decide whether to keep a line-end hyphen."""
    word, hyph = Counter(), Counter()
    for p in pages:
        for b in p["blocks"]:
            for ln in b:
                t = "".join(s["text"] for s in ln if not is_mono(s))
                # drop the last token: it may be a line-break fragment
                body = re.sub(r"\S+\s*$", "", t)
                for w in re.findall(r"[A-Za-z]+(?:-[A-Za-z]+)*", body):
                    w = w.lower()
                    if "-" in w:
                        hyph[w] += 1
                    else:
                        word[w] += 1
    return {"word": word, "hyph": hyph}


# ------------------------------------------------------- classification ---

def page_left(page):
    """Left text margin: most common x of body lines (120 odd / 123 even pages)."""
    xs = Counter()
    for b in page["blocks"]:
        for ln in b:
            s = ln[0]
            if s["font"].startswith("NewBaskerville") and s["size"] == 10:
                xs[round(s["x0"])] += 1
    for x, _ in xs.most_common():
        if x in (120, 123):
            return float(x)
    return 120.0 if page["page"] % 2 else 123.0


def classify(ln, left, in_box):
    """Return the kind of one physical line."""
    s0 = ln[0]
    f, size = s0["font"], s0["size"]
    text = "".join(s["text"] for s in ln).strip()
    if not text:
        return "blank"
    if any(s["size"] >= 15 for s in ln if s["text"].strip()):
        return "display"                        # big chapter/part title art
    if f == "Futura-Bold" and size == 12:
        return "h2"
    if f == "Futura-CondensedBoldObli" and size == 12:
        return "h3"
    if f == "Futura-CondensedBold" and size == 10:
        return "h4"
    if f == "DogmaBold" and size == 7.5:
        return "note"
    if f == "DogmaBold" and size == 9:
        return "box"
    if f == "Futura-Heavy" and text.startswith("Table "):
        return "table_caption"
    if f.startswith("Futura-BookOblique") and text.startswith("Figure "):
        return "caption"
    content = [s for s in ln if s["text"].strip() and s["font"] != "Wingdings2"]
    label = [s for s in content if s["font"].startswith("Futura-BookOblique") and s["x0"] < left - 15]
    rest = [s for s in content if s not in label]
    if rest and all(is_mono(s) for s in rest):
        return "code"
    if label and not rest:
        return "label"
    if text.startswith("•"):                    # Symbol font in body, Futura-Book in boxes
        return "bullet"
    if f.startswith("NewBaskerville") and size == 9:
        return "quote"                          # indented block quotes (project specs)
    if f == "NewBaskerville-Roman" and size == 14 or f == "NewBaskerville-Italic" and size == 14:
        return "intro"
    if in_box or f.startswith("Futura-Book") or f.startswith("Futura-Heavy"):
        return "boxtext"
    return "text"


def attach_margin_labels(page, left):
    """Move margin filename labels onto the code line printed at the same height.

    MuPDF sometimes emits a listing's margin label ("favorite_languages.py")
    as a separate block after the following prose; left alone it would
    become an empty listing in the wrong place.
    """
    def is_label(ln):
        content = [s for s in ln if s["text"].strip()]
        return content and all(s["font"].startswith("Futura-BookOblique") and s["x0"] < left - 15
                               for s in content)

    code_lines = [ln for b in page["blocks"] for ln in b
                  if any(is_mono(s) for s in ln) and not is_label(ln)]
    for b in page["blocks"]:
        for ln in list(b):
            if not is_label(ln):
                continue
            target = next((c for c in code_lines if abs(c[0]["y"] - ln[0]["y"]) < 3), None)
            if target is not None and target is not ln:
                target[:0] = ln                 # label spans first, like an inline label
                b.remove(ln)
    page["blocks"] = [b for b in page["blocks"] if b]


def code_line(ln, left):
    """Rebuild one code line from character positions. Returns (marker, text, label)."""
    # Characters inside a span are consecutive columns. Only the start of each
    # span is derived from its x position: long lines are sometimes set with
    # tighter tracking (4.17pt instead of 4.25pt per char), so converting every
    # char's x to a column would make characters collide and vanish.
    marker, label, cells = "", "", {}
    prev_end = prev_x = None
    for s in ln:
        if s["font"] == "Wingdings2":
            m = "".join(c for c in (marker_char(ch) for ch in s["text"]) if c)
            if m:
                marker = m
            continue
        if not is_mono(s):
            if s["font"].startswith("Futura-BookOblique") and s["x0"] < left - 15:
                label += s["text"].strip()
            continue
        chars = list(zip(s["text"], s["xs"]))
        while chars and chars[0][0] == " " and chars[0][1] < left - 1:
            chars.pop(0)                         # separator after a margin marker
        if not chars:
            continue
        cw = s["size"] / 2
        pitch = (chars[-1][1] - chars[0][1]) / (len(chars) - 1) if len(chars) > 1 else cw
        if not 0.8 * cw < pitch < 1.1 * cw:
            pitch = cw
        if prev_end is None:
            start = round((chars[0][1] - left) / cw)
        else:
            start = prev_end + max(0, round((chars[0][1] - prev_x) / pitch) - 1)
        for i, (ch, _) in enumerate(chars):
            if ch != " ":
                cells[start + i] = ch
        prev_end, prev_x = start + len(chars), chars[-1][1]
    if not cells:
        return marker, "", label
    lo = min(cells)
    if lo < 0:                                   # code hanging left of the margin
        cells = {c - lo: v for c, v in cells.items()}
    width = max(cells) + 1
    text = "".join(cells.get(i, " ") for i in range(width))
    return marker, text.rstrip(), label


# ------------------------------------------------------------- builder ---

class Builder:
    def __init__(self, vocab, offset):
        self.vocab = vocab
        self.offset = offset
        self.out = []            # finished markdown chunks
        self.cur = None          # open element: dict(kind=..., ...)
        self.last_page = None    # last page marker written
        self.in_box = False

    # -- element lifecycle
    def flush(self):
        c = self.cur
        self.cur = None
        if not c:
            return
        k = c["kind"]
        if k in ("para", "intro", "boxpara", "bullet", "note", "caption", "heading", "quote"):
            runs = join_runs(c["lines"], self.vocab, c["page"])
            if k == "caption":                    # whole caption is italic; keep only `code`
                runs = [[st if st == "code" else "plain", tx] for st, tx in runs]
            elif k == "note":                     # notes are set in italic: roman words are the emphasis
                swap = {"italic": "plain", "plain": "italic"}
                runs = [[swap.get(st, st), tx] for st, tx in runs]
            text = render_runs(runs)
            if not text:
                return
            if k == "bullet":
                text = "- " + text
            elif k == "note":
                text = "> **Note** " + text
            elif k == "quote":
                text = "> " + text
            elif k == "caption":
                text = f"*{text.strip('*')}*"
            elif k == "heading":
                text = "#" * c["level"] + " " + re.sub(r"[*`]", "", text) if c["level"] else text
            self.emit(text, c["page"])
        elif k == "code":
            self.emit(self.render_code(c), c["page"])
        elif k == "table":
            self.emit(self.render_table(c), c["page"])

    def emit(self, text, page):
        if self.last_page is None or page > self.last_page:
            printed = page - self.offset if page > self.offset else "-"
            self.out.append(f"<!-- pdf-page: {page} | printed: {printed} -->")
            self.last_page = page
        self.out.append(text)

    def open(self, kind, page, **kw):
        self.flush()
        self.cur = {"kind": kind, "page": page, "lines": [], **kw}
        return self.cur

    # -- code
    def render_code(self, c):
        rows = c["rows"]
        while rows and not rows[-1][1].strip():
            rows.pop()
        any_marker = any(m for m, _ in rows)
        body = []
        for m, t in rows:
            prefix = (m or " ") + " " if any_marker else ""
            body.append((prefix + t).rstrip())
        code = "\n".join(body)
        lang = "python" if re.search(r"(^|\n)\W*(def |class |import |from |for |if |print\(|>>> )|\w+ = ", code) \
            or c.get("label", "").endswith(".py") else "text"
        head = f"**{c['label']}**\n\n" if c.get("label") else ""
        return f"{head}```{lang}\n{code}\n```"

    # -- table
    def render_table(self, c):
        rows = []                                  # [(y, [(x, runs)])]
        for ln in c["cells"]:
            y = ln[0]["y"]
            if rows and abs(rows[-1][0] - y) < 3:
                rows[-1][1].append((ln[0]["x0"], line_runs(ln)))
            else:
                rows.append((y, [(ln[0]["x0"], line_runs(ln))]))
        cols = sorted({round(x) for _, cells in rows for x, _ in cells})
        md = []
        for i, (_, cells) in enumerate(rows):
            vals = [""] * len(cols)
            for x, runs in cells:
                j = min(range(len(cols)), key=lambda k: abs(cols[k] - x))
                vals[j] = render_runs(join_runs([runs], self.vocab, c["page"])).replace("|", "\\|")
            md.append("| " + " | ".join(vals) + " |")
            if i == 0:
                md.append("|" + "---|" * len(cols))
        return "\n".join(md)

    # -- main per-line dispatch
    def add_page(self, page):
        pno = page["page"]
        left = page_left(page)
        # left edge of Try It Yourself box text on this page (exercise labels start here)
        box_left = min((l2[0]["x0"] for b in page["blocks"] for l2 in b
                        if l2[0]["font"].startswith("Futura-Heavy") and l2[0]["x0"] > left), default=left + 19)
        attach_margin_labels(page, left)
        prev_y = None
        prev_block = None
        for bi, block in enumerate(page["blocks"]):
            for ln in block:
                y = ln[0]["y"]
                if y > FOOTER_Y:
                    continue                      # running head + page number
                kind = classify(ln, left, self.in_box)
                if kind in ("blank", "display"):
                    continue
                c = self.cur
                x0 = next((s["x0"] for s in ln if s["text"].strip()), ln[0]["x0"])
                gap = (y - prev_y) if prev_y is not None else None
                new_block = prev_block is not None and bi != prev_block
                prev_y, prev_block = y, bi

                # leaving a Try It Yourself box
                if self.in_box and kind not in ("boxtext", "code", "label", "bullet", "box"):
                    self.flush()
                    self.out.append("<!-- /box -->")
                    self.in_box = False
                    c = None

                if kind in ("h2", "h3", "h4"):
                    level = int(kind[1])
                    if c and c["kind"] == "heading" and c["level"] == level and gap is not None and gap < 20:
                        c["lines"].append(line_runs(ln))
                    else:
                        self.open("heading", pno, level=level)["lines"].append(line_runs(ln))
                elif kind == "box":
                    self.flush()
                    self.emit("<!-- box -->", pno)
                    self.in_box = True
                    self.open("heading", pno, level=0)["lines"].append([["bold", "Try It Yourself"]])
                    self.flush()
                elif kind == "note":
                    runs = [r for r in line_runs(ln) if r[1].replace(" ", "") not in ("Note",)]
                    self.open("note", pno)["lines"].append(runs)
                elif kind == "table_caption":
                    self.open("caption", pno)["lines"].append(line_runs(ln))
                    self.flush()
                    self.open("table", pno, cells=[])
                elif c and c["kind"] == "table" and (kind == "code" or kind == "boxtext"
                                                       or ln[0]["font"].startswith("Futura")):
                    c["cells"].append(ln)
                elif kind == "caption":
                    if c and c["kind"] == "caption" and gap is not None and gap < 15:
                        c["lines"].append(line_runs(ln))
                    else:
                        self.open("caption", pno)["lines"].append(line_runs(ln))
                elif kind in ("code", "label"):
                    base = left
                    if self.in_box:
                        base = box_left
                    marker, text, label = code_line(ln, base)
                    # a long margin filename wraps onto the next code line,
                    # e.g. "Python3" + ".sublime-build": extend, don't split
                    last = c.get("label_y") if c and c["kind"] == "code" and c.get("label") else None
                    wrapped = bool(label and last and last[0] == pno and y - last[1] < 15)
                    if kind == "label" and not text:
                        if wrapped:
                            c["label"] += label
                            c["label_y"] = (pno, y)
                        else:
                            # filename label on its own line: attach to next code block
                            self.flush()
                            self.cur = {"kind": "code", "page": pno, "rows": [], "label": label,
                                        "label_y": (pno, y)}
                        continue
                    if wrapped:
                        c["label"] += label
                    if c and c["kind"] == "code" and (gap is None or gap < 40 or not c["rows"]) \
                            and (not label or wrapped or not c["rows"]):
                        if gap is not None and c["rows"]:
                            blanks = round(gap / CODE_LEADING) - 1
                            c["rows"].extend([("", "")] * max(0, min(blanks, 3)))
                        c["rows"].append((marker, text))
                        if label and not wrapped:
                            c["label"] = label
                    else:
                        self.open("code", pno, rows=[(marker, text)], label=label)
                        del self.cur["lines"]
                    if label:
                        self.cur["label_y"] = (pno, y)
                elif kind == "bullet":
                    self.open("bullet", pno)["lines"].append(line_runs(ln))
                elif kind == "quote":
                    if c and c["kind"] == "quote" and (gap is None or gap < 14) and x0 < left + 40:
                        c["lines"].append(line_runs(ln))
                    else:
                        self.open("quote", pno)["lines"].append(line_runs(ln))
                elif kind == "intro":
                    if c and c["kind"] == "intro":
                        c["lines"].append(line_runs(ln))
                    else:
                        self.open("intro", pno)["lines"].append(line_runs(ln))
                else:  # text / boxtext
                    is_box = kind == "boxtext"
                    want = "boxpara" if is_box else "para"
                    label_start = ln[0]["font"].startswith("Futura-Heavy")   # "1-1. python.org:"
                    indented = x0 > (box_left if is_box else left) + 8
                    cont = False
                    if c and c["kind"] in (want, "bullet", "note"):
                        if c["kind"] == "bullet":
                            cont = indented and (gap is None or gap < 14)
                        elif c["kind"] == "note":
                            cont = not new_block or (gap is not None and gap < 14)
                        elif label_start:
                            cont = False
                        elif gap is None:          # first line on a new page
                            cont = not indented
                        else:
                            cont = not indented and gap < 14
                    if cont:
                        c["lines"].append(line_runs(ln))
                    else:
                        self.open(want, pno)["lines"].append(line_runs(ln))

    def finish(self):
        self.flush()
        if self.in_box:
            self.out.append("<!-- /box -->")
            self.in_box = False
        return "\n\n".join(self.out).strip() + "\n"


def main():
    units = json.loads((ROOT / "original" / "units.json").read_text(encoding="utf-8"))
    pages = [json.loads(l) for l in open(EXTRACTED / "pages.jsonl", encoding="utf-8")]
    by_no = {p["page"]: p for p in pages}
    vocab = build_vocab(pages)
    only = set(sys.argv[1:])
    CHAPTERS.mkdir(parents=True, exist_ok=True)

    for u in units["units"]:
        if only and u["slug"] not in only:
            continue
        b = Builder(vocab, units["printed_offset"])
        if u["slug"] != "front-matter":
            b.out.append(f"# {u['title']}")
        for n in range(u["start"], u["end"] + 1):
            b.add_page(by_no[n])
        md = b.finish()
        header = (f"<!-- source: {units['pdf']} | unit: {u['slug']} | pdf pages {u['start']}-{u['end']}"
                  f" | printed {max(u['printed_start'], 1) if u['start'] > units['printed_offset'] else '-'}"
                  f"-{u['printed_end'] if u['end'] > units['printed_offset'] else '-'} -->\n\n")
        (CHAPTERS / f"{u['slug']}.md").write_text(header + md, encoding="utf-8")
        print(f"{u['slug']:16s} {len(md):7d} chars")

    LOG.parent.mkdir(exist_ok=True)
    LOG.write_text("\n".join(warnings) + "\n", encoding="utf-8")
    print(f"{len(warnings)} warnings -> {LOG.relative_to(ROOT)}")


if __name__ == "__main__":
    main()

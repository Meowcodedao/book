# Python Crash Course — bản dịch tiếng Việt

Pipeline chuyển cuốn *Python Crash Course* (ấn bản 1, 2015) từ PDF tiếng Anh thành bản tiếng Việt,
dịch từng chương với QA tự động. Dùng cho học tập cá nhân.

Quy tắc dịch đầy đủ (dành cho Claude Code và người biên tập): xem [CLAUDE.md](CLAUDE.md).

## Cấu trúc thư mục

```
pythoncrashcourse.pdf        PDF gốc — không bao giờ bị sửa
original/
  extracted/
    pages.jsonl              extraction theo font + tọa độ ký tự (MuPDF stext)
    book.txt                 pdftotext -layout, để tra cứu nhanh
    outline.tsv              bookmark của PDF + số trang PDF/trang in
  units.json                 danh sách unit (chương, phụ lục…) và khoảng trang
  chapters/<unit>.md         SOURCE tiếng Anh dạng Markdown
translated/<unit>.md         BẢN DỊCH tiếng Việt
glossary/glossary.md         thuật ngữ thống nhất
qa/
  source-check.md            kiểm tra chất lượng extraction
  <unit>-qa.md               báo cáo QA từng chương
scripts/                     pipeline (Python stdlib, không cần cài thêm gì)
logs/                        log extraction / build
STATUS.md                    trạng thái từng unit
CLAUDE.md                    quy tắc project
```

## Yêu cầu

`python3` (≥ 3.9), `mutool` (MuPDF), `pdftotext` (poppler-utils). Không cần OCR: PDF có text layer đầy đủ.

## Chạy lại extraction

```bash
python3 scripts/extract.py          # PDF -> original/extracted/
python3 scripts/outline.py          # bookmark -> original/units.json
python3 scripts/build_markdown.py   # -> original/chapters/*.md
python3 scripts/check_source.py     # -> qa/source-check.md
```

Cách extraction hoạt động: `mutool draw -F stext` giữ font và tọa độ x của từng ký tự. Nhờ đó:

- code (font TheSansMono) được tách khỏi văn bản, và thụt lề được dựng lại từ tọa độ — không phụ
  thuộc khoảng trắng của bản text;
- heading 3 cấp, Note, hộp *Try It Yourself*, caption, bảng, bullet được nhận diện theo font;
- header/footer (tên chương + số trang) bị loại theo vị trí;
- từ bị ngắt dòng bằng gạch nối được nối lại (`logs/build_markdown.log` liệt kê các trường hợp cần để ý).

## Dịch tiếp

Trong Claude Code, tại thư mục này:

```
Hãy dịch Chapter 1 theo toàn bộ quy tắc trong CLAUDE.md.
```

Claude sẽ đọc `STATUS.md`, glossary, source; dịch vào `translated/`; chạy QA; báo cáo; rồi dừng.
Sau khi xem lại: `Chapter 1 đã ổn. Hãy dịch Chapter 2 theo đúng workflow.`

## Chạy QA

```bash
python3 scripts/qa_translation.py chapter-01   # cấu trúc, code, inline code, URL, marker, độ dài
python3 scripts/glossary_check.py chapter-01   # thuật ngữ bị cấm theo glossary
```

`qa_translation.py` so bản dịch với source theo từng block: code block, inline code, URL, marker
❶❷…, comment trang phải giống hệt; số block và loại block phải khớp 1:1. Exit code 1 nếu có ERROR.

# CLAUDE.md — Dự án dịch *Python Crash Course* sang tiếng Việt

Đọc toàn bộ file này trước khi làm bất cứ việc gì trong project. Người dùng sẽ **không** paste lại
hướng dẫn ban đầu; mọi quy tắc nằm ở đây.

## 1. Project làm gì

Dịch cuốn *Python Crash Course* (Eric Matthes, No Starch Press, 2015 — **ấn bản 1**, Python 2 & 3)
từ PDF tiếng Anh sang tiếng Việt chất lượng cao, phục vụ học tập cá nhân. Dịch **từng chương**, mỗi
chương có QA riêng. Nhiệm vụ là **dịch**, không viết lại sách.

## 2. Bản đồ project

| Đường dẫn | Nội dung | Ai được sửa |
|---|---|---|
| `pythoncrashcourse.pdf` | Nguồn duy nhất của nội dung sách (562 trang) | **Không ai.** Không đổi tên/sửa/nén/xóa |
| `original/extracted/pages.jsonl` | Extraction có font + tọa độ từng ký tự (MuPDF) | Chỉ script |
| `original/extracted/book.txt` | `pdftotext -layout` toàn sách, chỉ để tra cứu | Chỉ script |
| `original/extracted/outline.tsv` | Bookmark của PDF, đã resolve ra số trang | Chỉ script |
| `original/units.json` | Danh sách unit (chương…) + khoảng trang | Chỉ script |
| `original/chapters/<unit>.md` | **Source tiếng Anh** dạng Markdown, mỗi unit một file | Chỉ script — không sửa tay |
| `translated/<unit>.md` | **Bản dịch** tiếng Việt | Claude khi dịch |
| `glossary/glossary.md` | Thuật ngữ thống nhất | Claude (thêm), đổi thì hỏi người dùng |
| `qa/<unit>-qa.md` | Báo cáo QA từng chương | Script + Claude (phần review tay) |
| `qa/source-check.md` | Kiểm tra chất lượng extraction | Script |
| `STATUS.md` | Trạng thái từng unit | Claude |
| `scripts/` | Pipeline | Claude |
| `logs/` | Log extraction / build / dịch | Script + Claude |

Unit: `front-matter` (SKIP), `acknowledgments`, `introduction`, `part-1`, `chapter-01` … `chapter-11`,
`part-2`, `project-1`, `chapter-12` … `chapter-14`, `project-2`, `chapter-15` … `chapter-17`,
`project-3`, `chapter-18` … `chapter-20`, `afterword`, `appendix-a` … `appendix-d`, `index` (SKIP).
Khoảng trang xem `STATUS.md`. **Trang in = trang PDF − 33** (front matter đánh số La Mã).

## 3. Quy tắc an toàn (tuyệt đối)

- Không xóa / đổi tên / ghi đè / sửa PDF. Không `rm -rf`.
- Không sửa tay `original/`. Nếu extraction sai → sửa `scripts/build_markdown.py` rồi chạy lại.
  Nếu chạy lại khi đã có bản dịch: sao lưu `original/chapters/` vào scratchpad trước, so sánh bằng
  `diff -r` sau khi build, và báo người dùng — source thay đổi có thể làm QA của chương đã dịch không
  còn khớp.
- Không dùng Internet để lấy nội dung sách, không tải bản sách khác, không gửi nội dung lên Internet.
  Nguồn duy nhất là PDF.
- Không cài package hệ thống. Pipeline chỉ cần `python3` (stdlib), `mutool`, `pdftotext`.
- Không bao giờ ghi vào `translated/` một unit có trạng thái `COMPLETED`.

## 4. Quy ước của source Markdown (`original/chapters/*.md`)

- `<!-- source: ... -->` dòng đầu: metadata của unit.
- `<!-- pdf-page: 37 | printed: 4 -->`: phần tử tiếp theo bắt đầu ở trang PDF 37. Dùng để đối chiếu PDF.
- `#` = tên chương/phần (từ bookmark). `##`, `###`, `####` = 3 cấp heading của sách (theo font).
- Code block: dựng lại từ tọa độ ký tự nên thụt lề chính xác. Ngôn ngữ fence (`python`/`text`) chỉ là
  đoán, không quan trọng.
- `**survey.py**` ngay trước code block = tên file in ở lề sách cạnh listing.
- `❶ ❷ ❸ …` = marker chú thích của sách. Trong code block có marker, **mọi dòng** có cột lề 2 ký tự
  (`❶ ` hoặc 2 dấu cách) — đó là lề của sách, không phải code. Trong văn bản, "at ❶" trỏ tới marker đó.
- `> **Note** …` = hộp Note. `> …` (không có Note) = trích dẫn thụt lề (mô tả dự án).
- `<!-- box -->` … `<!-- /box -->` = hộp **Try It Yourself**; trong đó `**2-1. Simple Message:** …`
  là bài tập.
- `*Figure 1-1: …*`, `*Table 11-1: …*` = caption. Hình ảnh **không** được trích xuất; xem PDF theo
  marker trang.
- `**File**▸**Save As**` = đường dẫn menu. `CTRL-D`, `ENTER` = phím (chữ in nhỏ trong sách).
- Code chữ đậm (phần người dùng gõ trong terminal session) **không** được phân biệt trong Markdown.
- Hai code block lỗi thụt lề trong chapter-04 (`magicians.py`, `hello_world.py`) là **ví dụ cố ý sai**
  của sách. Không sửa.

## 5. Quy tắc dịch

### 5.1 Nội dung bất biến — copy nguyên văn, từng ký tự

- **Toàn bộ code block** (kể cả comment trong code, chuỗi trong code, output chương trình, traceback,
  lệnh terminal, cột lề marker). Không dịch comment trong code trừ khi người dùng yêu cầu.
- **Mọi inline code** `` `...` ``: tên biến/hàm/class/method/module/package, keyword, lệnh, flag, …
- URL, tên file, đường dẫn, tên lệnh.
- Marker `❶❷…`, mọi comment HTML `<!-- … -->`, nhãn tên file `**name.py**`.
- Text in nghiêng là **output chương trình, tên file/thư mục, URL, hoặc chuỗi người dùng gõ**
  (vd. *Hello world!*, *python_work*, *hello_world.py*) → giữ nguyên tiếng Anh.
- Tên mục menu / nút / hộp thoại của phần mềm tiếng Anh (**File**▸**Save As**, **Build**, Add Python
  to PATH) và tên phím → giữ nguyên.
- Số bài tập, số hình, số bảng, số trang ("on page 15" → "ở trang 15").

Ví dụ: `name = input("What is your name? ")` giữ nguyên; **không** thành `ten = input("Tên bạn? ")`.
Output `Hello, Alice!` giữ nguyên; **không** thành `Xin chào, Alice!`.

### 5.2 Cấu trúc — giữ 1:1

`scripts/qa_translation.py` so **từng block** với source, nên:

- Mỗi block của source (đoạn, heading, bullet, note, caption, bảng, code, comment) → đúng **một** block
  trong bản dịch, **cùng thứ tự, cùng loại**. Không gộp/tách đoạn, không thêm/bớt heading, không đổi
  cấp heading, không thêm dòng trống giữa các dòng của một bullet/bảng.
- Giữ nguyên tiền tố: `## `, `- `, `> **Note** ` → `> **Lưu ý** `, `> `, `| … |`.
- Heading: dịch nội dung, giữ cấp. `# Chapter 1: Getting Started` → `# Chương 1: Bắt đầu`.
- `**Try It Yourself**` → `**Tự mình thực hành**`. Bài tập: `**2-1. Simple Message:**` →
  `**2-1. Thông điệp đơn giản:**`.
- Caption: `*Figure 3-1: A simple Python program*` → `*Hình 3-1: Một chương trình Python đơn giản*`.
- Bảng: giữ số hàng/cột/thứ tự; dịch text, giữ inline code.
- Link: giữ URL, chỉ dịch phần chữ hiển thị nếu có.
- Tham chiếu chéo tới mục khác ("see “Troubleshooting Installation Issues” on page 15"): dịch tên
  mục giống hệt cách đã/ sẽ dịch heading đó; ghi vào bảng "Tiêu đề mục" trong glossary để thống nhất.

### 5.3 Văn phong

Bản dịch phải đọc như một giáo trình Python tiếng Việt do giảng viên giàu kinh nghiệm biên tập:
rõ ràng, tự nhiên, chính xác, dễ hiểu, không hàn lâm, không giống máy dịch, không thêm lời bình.

Ưu tiên: **chính xác kỹ thuật > nhất quán > rõ ràng > tiếng Việt tự nhiên > sát chữ**.

- Không dịch word-by-word. "Python allows you to organize your code into functions." →
  "Python cho phép bạn tổ chức mã nguồn thành các hàm." (không: "…tổ chức mã của bạn vào các hàm").
- Ngôi xưng: tác giả "I" → "tôi"; người đọc "you" → "bạn"; "we/let's" → "chúng ta/hãy".
- Không thêm kiến thức, ví dụ, bài tập, lời giải, lời khuyên, nhận xét, thông tin Python mới hơn
  (kể cả khi sách đã cũ, vd. Python 2). Không rút gọn, không tóm tắt. Không bỏ sót.
- Câu khó: đọc cả ngữ cảnh, xác định ý kỹ thuật, viết lại tự nhiên. Nếu thật sự không chắc:
  `[TODO: Cần kiểm tra ngữ nghĩa.]` ngay sau câu đó. Không bịa.
- Nếu text trong source nghi bị extraction làm hỏng → mở PDF đúng trang (marker `pdf-page`) để
  kiểm tra (`pdftotext -layout -f N -l N pythoncrashcourse.pdf -` hoặc render
  `pdftoppm -f N -l N -r 80 -png …` vào scratchpad rồi xem ảnh). Dịch theo PDF, ghi chú vào QA report.

### 5.4 Thuật ngữ

- Đọc `glossary/glossary.md` trước khi dịch. Dùng đúng cách dịch đã có.
- `list`, `tuple`, `dictionary`, `set`, `module`, `package`, `API`, `terminal`, `traceback` giữ tiếng Anh.
- Lần đầu thuật ngữ quan trọng xuất hiện **trong mỗi chương**: `đối tượng (object)`, `bất biến (immutable)`;
  sau đó chỉ dùng tiếng Việt.
- Thuật ngữ mới quan trọng → thêm vào glossary (ghi chương). Không tự ý đổi thuật ngữ đã thống nhất.

## 6. Workflow

### 6.1 Khi người dùng nói "Dịch Chapter N" (hoặc tên unit khác)

1. Đọc `STATUS.md`. Unit `COMPLETED` → dừng, báo người dùng. `TRANSLATING` → tiếp tục từ trang ghi
   trong Notes (đọc phần đã dịch để giữ giọng văn), không dịch lại phần đã xong.
2. Đọc `glossary/glossary.md` và `original/chapters/<unit>.md`.
3. Đặt `STATUS.md` → `TRANSLATING`.
4. Dịch **toàn bộ** unit vào `translated/<unit>.md`. Chương dài (40–65k ký tự): dịch theo từng
   cụm vài trang PDF (theo marker `pdf-page`), ghi nối tiếp vào file, sau mỗi cụm cập nhật Notes
   `done to pdf-page N` trong `STATUS.md` để có thể resume.
5. Kiểm tra PDF gốc ở những chỗ source đáng ngờ.
6. Cập nhật glossary nếu có thuật ngữ mới. Đặt `STATUS.md` → `TRANSLATED`.
7. Chạy QA:
   ```bash
   python3 scripts/qa_translation.py chapter-01
   python3 scripts/glossary_check.py chapter-01
   ```
8. Sửa mọi ERROR (thường do dịch nhầm inline code, gộp/tách đoạn). Xem từng WARNING; sửa nếu đúng là lỗi.
   Không sửa code block theo phỏng đoán — code phải khớp source; nếu source sai so với PDF thì báo.
9. Review tay theo checklist ở mục 7, ghi kết quả vào cuối `qa/<unit>-qa.md` (mục "Manual review",
   viết **sau** lần chạy script cuối cùng vì script ghi đè file). Đặt `STATUS.md` → `QA`.
10. Báo cáo cho người dùng: số block, số code block, lỗi đã sửa, thuật ngữ mới, chỗ `[TODO]`, chỗ cần
    người dùng quyết định.
11. **Dừng.** Không dịch unit tiếp theo khi chưa được yêu cầu. Chỉ chuyển `COMPLETED` khi người dùng
    xác nhận chương ổn.

### 6.2 Resume ở phiên mới

Đọc `STATUS.md`, liệt kê `translated/` và `qa/`. Không dịch lại unit đã `TRANSLATED`/`QA`/`COMPLETED`
trừ khi người dùng yêu cầu sửa.

## 7. Checklist QA (review tay sau khi script PASS)

- [ ] Không bỏ sót đoạn văn / không dịch trùng
- [ ] Code, output, tên biến/hàm/class/keyword không bị thay đổi (script kiểm tra)
- [ ] Heading đủ và đúng cấp; Markdown hợp lệ; bullet, bảng đầy đủ
- [ ] Thuật ngữ nhất quán với glossary
- [ ] Không thêm kiến thức, không bỏ nội dung
- [ ] Tiếng Việt tự nhiên, không văn phong máy dịch
- [ ] Text in nghiêng là output/tên file/URL vẫn giữ nguyên
- [ ] Tham chiếu chéo (tên mục, số trang, số hình/bài tập) đúng

## 8. Pipeline (chạy lại extraction)

```bash
python3 scripts/extract.py          # PDF -> original/extracted/pages.jsonl + book.txt
python3 scripts/outline.py          # bookmarks -> original/units.json, outline.tsv
python3 scripts/build_markdown.py   # -> original/chapters/*.md  (+ logs/build_markdown.log)
python3 scripts/check_source.py     # -> qa/source-check.md
```

`build_markdown.py [unit ...]` chỉ build lại các unit được chỉ định.

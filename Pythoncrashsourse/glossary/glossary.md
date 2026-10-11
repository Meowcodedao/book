# Glossary — Python Crash Course (bản dịch tiếng Việt)

Quy tắc:

- Đọc file này **trước khi dịch** mỗi chương. Thuật ngữ đã có ở đây thì dùng đúng như vậy.
- Thuật ngữ mới quan trọng → thêm một dòng vào bảng phù hợp (ghi chương xuất hiện lần đầu trong cột Notes).
- Không đổi cách dịch đã thống nhất. Muốn đổi → hỏi người dùng, rồi sửa ở đây **và** ở mọi chương đã dịch.
- Cột Notes có thể chứa `Tránh: a, b` — `scripts/glossary_check.py` sẽ cảnh báo nếu bản dịch dùng `a` hoặc `b`.
- "Giữ nguyên" = viết bằng tiếng Anh như trong sách (không in nghiêng, không thêm ngoặc).
- Lần đầu một thuật ngữ quan trọng xuất hiện trong **mỗi chương**: `tiếng Việt (English)`, ví dụ `đối tượng (object)`. Sau đó chỉ dùng tiếng Việt.

## Nhãn cố định của sách

| English | Vietnamese | Notes |
| --- | --- | --- |
| Chapter N: Title | Chương N: Tên chương | Heading H1 |
| Part I / Part II | Phần I / Phần II | |
| Project 1/2/3 | Dự án 1/2/3 | |
| Appendix A | Phụ lục A | |
| Introduction | Lời giới thiệu | |
| Acknowledgments | Lời cảm ơn | |
| Afterword | Lời kết | |
| Summary | Tổng kết | Heading cuối mỗi chương |
| Try It Yourself | Tự mình thực hành | Tiêu đề box bài tập (`**...**`) |
| Exercise 2-1 / 2-1. Simple Message: | Bài tập 2-1 / 2-1. Thông điệp đơn giản: | Giữ nguyên số bài tập |
| Note | Lưu ý | Trong `> **Note**` → `> **Lưu ý**` |
| Figure 3-1: ... | Hình 3-1: ... | Giữ nguyên số |
| Table 11-1: ... | Bảng 11-1: ... | Giữ nguyên số |
| on page 15 | ở trang 15 | Giữ số trang in của sách gốc |
| at ❶ | tại ❶ | Marker giữ nguyên ký tự |

## Thuật ngữ Python cơ bản

| English | Vietnamese | Notes |
| --- | --- | --- |
| variable | biến | |
| value | giá trị | |
| function | hàm | Không dịch "function" thành "chức năng" (kiểm tra tay; "chức năng" chỉ dùng cho functionality) |
| functionality | chức năng | |
| built-in function | hàm có sẵn (built-in function) | |
| method | phương thức | |
| parameter | tham số | |
| argument | đối số | Tránh: tham đối |
| positional argument | đối số vị trí (positional argument) | Ch 8 |
| keyword argument | đối số từ khóa (keyword argument) | Ch 8 |
| default value | giá trị mặc định | |
| return value | giá trị trả về | |
| loop | vòng lặp | |
| for loop | vòng lặp `for` | |
| while loop | vòng lặp `while` | |
| conditional test | phép kiểm tra điều kiện | Ch 5 |
| conditional statement | câu lệnh điều kiện | |
| if statement | câu lệnh `if` | |
| exception | ngoại lệ | |
| error | lỗi | |
| bug | lỗi (bug) | |
| debugging | gỡ lỗi | |
| traceback | traceback | Giữ nguyên; lần đầu: "traceback (thông báo truy vết lỗi)" |
| syntax | cú pháp | |
| syntax error | lỗi cú pháp | |
| indentation | thụt lề | |
| object | đối tượng | |
| attribute | thuộc tính | |
| instance | thực thể (instance) | Không dùng "thể hiện" cho instance (kiểm tra tay) |
| class | lớp | Lần đầu mỗi chương: "lớp (class)"; giữ `class` khi là từ khóa |
| inheritance | kế thừa | |
| parent class / superclass | lớp cha | Ch 9 |
| child class / subclass | lớp con | Ch 9 |
| override | ghi đè (override) | Ch 9 |
| object-oriented programming | lập trình hướng đối tượng | Ch 9 |
| instantiation | khởi tạo thực thể | Ch 9 |
| docstring | docstring | Giữ nguyên |
| import (verb) | import | Giữ nguyên; lần đầu "import (nhập)" |
| alias | bí danh | Ch 8 |
| standard library | thư viện chuẩn | Ch 9 |
| flag | cờ | Ch 7 |
| prompt (input) | lời nhắc | Ch 7 |
| modulo operator | toán tử chia lấy dư | Ch 7 |
| list comprehension | list comprehension | Giữ nguyên |
| nesting | lồng nhau | Ch 6 |
| expression | biểu thức | |
| statement | câu lệnh | |
| keyword | từ khóa | |
| string | chuỗi | |
| integer | số nguyên | |
| float | số thực (float) | |
| Boolean | Boolean / kiểu Boolean | |
| Boolean expression | biểu thức Boolean | |
| list | list | Giữ nguyên; có thể "danh sách" khi nói chung chung không phải kiểu dữ liệu |
| tuple | tuple | Giữ nguyên |
| dictionary | dictionary | Giữ nguyên |
| key-value pair | cặp khóa–giá trị | |
| key | khóa | |
| set | set | Giữ nguyên |
| element / item | phần tử | |
| index | chỉ mục | |
| slice | lát cắt (slice) | |
| iteration | lần lặp / quá trình lặp | |
| module | module | Giữ nguyên |
| package | package | Giữ nguyên |
| API | API | Giữ nguyên |
| mutable | có thể thay đổi (mutable) | |
| immutable | bất biến (immutable) | |
| comment | chú thích | Comment trong code = "chú thích"; comment của người dùng trên diễn đàn/web = "bình luận" |
| whitespace | khoảng trắng | |
| testing | kiểm thử | |
| unit test | unit test (kiểm thử đơn vị) | |
| test case | test case | Giữ nguyên |
| source code | mã nguồn | |
| code | mã / code | Ưu tiên "mã"; "đoạn code" chấp nhận khi tự nhiên hơn |
| program | chương trình | |
| programmer | lập trình viên | |
| programming language | ngôn ngữ lập trình | |

## Môi trường & công cụ

| English | Vietnamese | Notes |
| --- | --- | --- |
| programming environment | môi trường lập trình | |
| interpreter | trình thông dịch | |
| terminal | terminal | Giữ nguyên |
| terminal session | phiên terminal | |
| terminal window | cửa sổ terminal | |
| command window | cửa sổ lệnh | Windows |
| command | lệnh | |
| text editor | trình soạn thảo văn bản | |
| snippet | đoạn mã ngắn | |
| prompt (`>>>`) | dấu nhắc | |
| output | đầu ra / kết quả | |
| input | đầu vào | |
| syntax highlighting | tô sáng cú pháp | |
| file | file / tệp | Ưu tiên "file" |
| folder | thư mục | |
| directory | thư mục | |
| path | đường dẫn | |
| operating system | hệ điều hành | |
| install | cài đặt | |
| virtual environment | môi trường ảo | Ch 18 |
| version control | quản lý phiên bản | Appendix D |
| repository | kho mã (repository) | |

## Tiêu đề mục được tham chiếu chéo

Khi văn bản nhắc tới tên một mục/chương khác (vd. “Troubleshooting Installation Issues” on page 15),
dịch đúng như heading đó đã/ sẽ được dịch. Ghi lại ở đây để các chương sau dùng giống nhau.

| English | Vietnamese | Notes |
| --- | --- | --- |
| Troubleshooting Installation Issues | Khắc phục sự cố cài đặt | Ch 1 |
| Running Python in a Terminal Session | Chạy Python trong một phiên terminal | Ch 1 |
| Running the Hello World Program | Chạy chương trình Hello World | Ch 1 |
| Python Keywords and Built-in Functions | Từ khóa và hàm có sẵn của Python | Ch 2 → Phụ lục A |
| Forgetting to Indent Additional Lines | Quên thụt lề các dòng bổ sung | Ch 4 |
| Running Python Programs from a Terminal | Chạy chương trình Python từ terminal | Ch 1, 7 |

<!-- source: pythoncrashcourse.pdf | unit: chapter-01 | pdf pages 36-51 | printed 3-18 -->

# Chương 1: Bắt đầu

<!-- pdf-page: 36 | printed: 3 -->

Trong chương này, bạn sẽ chạy chương trình Python đầu tiên của mình, *hello_world.py*. Trước hết, bạn cần kiểm tra xem Python đã được cài trên máy tính hay chưa; nếu chưa, bạn sẽ cài đặt nó. Bạn cũng sẽ cài một trình soạn thảo văn bản để làm việc với các chương trình Python. Trình soạn thảo văn bản nhận biết được mã Python và tô sáng các phần mã ngay khi bạn viết, giúp bạn dễ dàng hiểu cấu trúc mã của mình.

## Thiết lập môi trường lập trình

Python có đôi chút khác biệt trên các hệ điều hành khác nhau, vì vậy bạn cần lưu ý một vài điểm. Ở đây, chúng ta sẽ xem xét hai phiên bản chính của Python đang được sử dụng hiện nay và phác thảo các bước thiết lập Python trên hệ thống của bạn.

<!-- pdf-page: 37 | printed: 4 -->

### Python 2 và Python 3

Hiện nay có hai phiên bản Python: Python 2 và Python 3 mới hơn. Mọi ngôn ngữ lập trình đều phát triển khi những ý tưởng và công nghệ mới xuất hiện, và các nhà phát triển Python đã liên tục làm cho ngôn ngữ này linh hoạt và mạnh mẽ hơn. Phần lớn các thay đổi diễn ra từng chút một và hầu như không đáng chú ý, nhưng trong một số trường hợp, mã viết cho Python 2 có thể không chạy đúng trên những hệ thống cài Python 3. Xuyên suốt cuốn sách, tôi sẽ chỉ ra những điểm khác biệt đáng kể giữa Python 2 và Python 3, để dù dùng phiên bản nào, bạn cũng có thể làm theo hướng dẫn.

Nếu hệ thống của bạn đã cài cả hai phiên bản, hoặc nếu bạn cần cài Python, hãy dùng Python 3. Nếu Python 2 là phiên bản duy nhất có trên hệ thống và bạn muốn bắt tay vào viết mã ngay thay vì cài Python, bạn có thể bắt đầu với Python 2. Nhưng bạn chuyển sang Python 3 càng sớm càng tốt, để làm việc với phiên bản mới nhất.

### Chạy các đoạn mã Python ngắn

Python đi kèm một trình thông dịch chạy trong cửa sổ terminal, cho phép bạn thử từng mẩu Python mà không phải lưu và chạy cả một chương trình.

Xuyên suốt cuốn sách, bạn sẽ thấy những đoạn mã ngắn trông như thế này:

```text
❶ >>> print("Hello Python interpreter!")
  Hello Python interpreter!
```

Phần chữ in đậm là những gì bạn sẽ gõ vào rồi thực thi bằng cách nhấn ENTER. Phần lớn ví dụ trong sách là những chương trình nhỏ, độc lập mà bạn sẽ chạy từ trình soạn thảo, vì đó là cách bạn sẽ viết phần lớn mã của mình. Nhưng đôi khi, các khái niệm cơ bản sẽ được trình bày qua một loạt đoạn mã ngắn chạy trong phiên terminal Python để minh họa từng khái niệm riêng lẻ hiệu quả hơn. Bất cứ khi nào bạn thấy ba dấu ngoặc nhọn trong một đoạn mã ❶, nghĩa là bạn đang xem đầu ra của một phiên terminal. Chúng ta sẽ thử viết mã trong trình thông dịch trên hệ thống của bạn ngay sau đây.

### Hello World!

Từ lâu, giới lập trình vẫn tin rằng in thông điệp *Hello world!* ra màn hình làm chương trình đầu tiên khi học một ngôn ngữ mới sẽ mang lại may mắn cho bạn.

Trong Python, bạn có thể viết chương trình *Hello World* chỉ với một dòng:

```python
print("Hello world!")
```

Một chương trình đơn giản như vậy vẫn có mục đích rất thực tế. Nếu nó chạy đúng trên hệ thống của bạn, thì mọi chương trình Python bạn viết cũng sẽ chạy được. Chúng ta sẽ xem cách viết chương trình này trên hệ thống cụ thể của bạn ngay sau đây.

<!-- pdf-page: 38 | printed: 5 -->

## Python trên các hệ điều hành khác nhau

Python là một ngôn ngữ lập trình đa nền tảng, nghĩa là nó chạy được trên tất cả các hệ điều hành lớn. Bất kỳ chương trình Python nào bạn viết cũng sẽ chạy được trên mọi máy tính hiện đại có cài Python. Tuy nhiên, cách thiết lập Python trên các hệ điều hành khác nhau có đôi chút khác biệt.

Trong phần này, bạn sẽ học cách thiết lập Python và chạy chương trình *Hello World* trên hệ thống của mình. Trước tiên, bạn sẽ kiểm tra xem Python đã được cài trên hệ thống chưa và cài đặt nếu chưa có. Sau đó, bạn sẽ cài một trình soạn thảo văn bản đơn giản và lưu một file Python trống có tên *hello_world.py*. Cuối cùng, bạn sẽ chạy chương trình *Hello World* và khắc phục những gì chưa chạy được. Tôi sẽ hướng dẫn bạn qua quy trình này cho từng hệ điều hành, để bạn có một môi trường lập trình Python thân thiện với người mới bắt đầu.

### Python trên Linux

Các hệ thống Linux được thiết kế cho lập trình, nên Python đã được cài sẵn trên hầu hết máy tính chạy Linux. Những người viết và bảo trì Linux kỳ vọng rằng đến một lúc nào đó bạn sẽ tự lập trình, và họ khuyến khích bạn làm điều đó. Vì thế, bạn chỉ phải cài rất ít thứ và thay đổi rất ít thiết lập để bắt đầu lập trình.

#### Kiểm tra phiên bản Python của bạn

Mở một cửa sổ terminal bằng cách chạy ứng dụng Terminal trên hệ thống (trên Ubuntu, bạn có thể nhấn CTRL-ALT-T). Để biết Python đã được cài hay chưa, hãy nhập `python` với chữ *p* viết thường. Bạn sẽ thấy đầu ra cho biết phiên bản Python nào đã được cài và một dấu nhắc `>>>` nơi bạn có thể bắt đầu nhập các lệnh Python, như thế này:

```text
$ python
Python 2.7.6 (default, Mar 22 2014, 22:59:38)
[GCC 4.8.2] on linux2
Type "help", "copyright", "credits" or "license" for more information.
>>>
```

Đầu ra này cho biết Python 2.7.6 hiện là phiên bản Python mặc định được cài trên máy tính này. Khi đã thấy đầu ra này, hãy nhấn CTRL-D hoặc nhập `exit()` để thoát khỏi dấu nhắc Python và quay về dấu nhắc của terminal.

Để kiểm tra Python 3, có thể bạn phải chỉ rõ phiên bản đó; vì vậy, ngay cả khi đầu ra hiển thị Python 2.7 là phiên bản mặc định, hãy thử lệnh `python3`:

```text
$ python3
Python 3.5.0 (default, Sep 17 2015, 13:05:18)
[GCC 4.8.4] on linux
Type "help", "copyright", "credits" or "license" for more information.
>>>
```

<!-- pdf-page: 39 | printed: 6 -->

Đầu ra này cho biết bạn cũng đã cài Python 3, nên bạn có thể dùng phiên bản nào cũng được. Bất cứ khi nào bạn thấy lệnh `python` trong sách này, hãy nhập `python3` thay thế. Hầu hết các bản phân phối Linux đều cài sẵn Python, nhưng nếu vì lý do nào đó bản của bạn không có, hoặc hệ thống của bạn chỉ có Python 2 và bạn muốn cài Python 3, hãy xem Phụ lục A.

#### Cài đặt trình soạn thảo văn bản

Geany là một trình soạn thảo văn bản đơn giản: nó dễ cài đặt, cho phép bạn chạy hầu hết các chương trình trực tiếp từ trình soạn thảo thay vì qua terminal, dùng tính năng tô sáng cú pháp để tô màu mã của bạn, và chạy mã trong một cửa sổ terminal để bạn làm quen với việc dùng terminal. Phụ lục B cung cấp thông tin về các trình soạn thảo văn bản khác, nhưng tôi khuyên bạn dùng Geany trừ khi bạn có lý do chính đáng để dùng một trình soạn thảo khác.

Trên hầu hết các hệ thống Linux, bạn có thể cài Geany chỉ với một dòng lệnh:

```text
$ sudo apt-get install geany
```

Nếu cách này không được, hãy xem hướng dẫn tại *http://geany.org/Download/ThirdPartyPackages/*.

#### Chạy chương trình Hello World

Để bắt đầu chương trình đầu tiên, hãy mở Geany. Nhấn phím Super (thường gọi là phím Windows) và tìm Geany trên hệ thống của bạn. Tạo một lối tắt bằng cách kéo biểu tượng vào thanh tác vụ hoặc màn hình nền. Sau đó, tạo một thư mục ở đâu đó trên hệ thống để chứa các dự án và đặt tên là *python_work*. (Tốt nhất là dùng chữ thường và dấu gạch dưới thay cho dấu cách trong tên file và tên thư mục, vì đó là các quy ước đặt tên của Python.) Quay lại Geany và lưu một file Python trống (**File**▸**Save As**) có tên *hello_world.py* vào thư mục *python_work*. Phần mở rộng *.py* cho Geany biết file của bạn sẽ chứa một chương trình Python. Nó cũng cho Geany biết cách chạy chương trình và tô sáng văn bản theo cách hữu ích.

Sau khi đã lưu file, hãy nhập dòng sau:

```python
print("Hello Python world!")
```

Nếu hệ thống của bạn cài nhiều phiên bản Python, bạn cần đảm bảo Geany được cấu hình để dùng đúng phiên bản. Vào **Build**▸**Set Build Commands**. Bạn sẽ thấy hai chữ *Compile* và *Execute*, mỗi chữ có một lệnh bên cạnh. Geany mặc định cho rằng lệnh đúng cho cả hai là `python`, nhưng nếu hệ thống của bạn dùng lệnh `python3`, bạn sẽ cần thay đổi điều này.

Nếu lệnh `python3` chạy được trong phiên terminal, hãy thay đổi các lệnh Compile và Execute để Geany dùng trình thông dịch Python 3. Lệnh Compile của bạn sẽ trông như thế này:

```text
python3 -m py_compile "%f"
```

<!-- pdf-page: 40 | printed: 7 -->

Bạn cần gõ lệnh này đúng y như được trình bày. Hãy đảm bảo dấu cách và chữ hoa, chữ thường khớp với những gì hiển thị ở đây.

Lệnh Execute của bạn sẽ trông như thế này:

```text
python3 "%f"
```

Một lần nữa, hãy đảm bảo dấu cách và chữ hoa, chữ thường khớp với những gì hiển thị ở đây. Hình 1-1 cho thấy các lệnh này trông như thế nào trong menu cấu hình của Geany.

*Hình 1-1: Ở đây, Geany được cấu hình để dùng Python 3 trên Linux.*

Bây giờ, hãy chạy *hello_world.py* bằng cách chọn **Build**▸**Execute** trong menu, nhấp vào biểu tượng Execute (biểu tượng hình các bánh răng), hoặc nhấn F5. Một cửa sổ terminal sẽ bật lên với đầu ra sau:

```text
Hello Python world!

------------------
(program exited with code: 0)
Press return to continue
```

Nếu không thấy kết quả này, hãy kiểm tra từng ký tự trên dòng bạn đã nhập. Bạn có vô tình viết hoa chữ `print` không? Bạn có quên một hoặc cả hai dấu ngoặc kép hay dấu ngoặc đơn không? Ngôn ngữ lập trình đòi hỏi cú pháp rất cụ thể, và nếu bạn không tuân theo, bạn sẽ gặp lỗi. Nếu không thể chạy được chương trình, hãy xem mục “Khắc phục sự cố cài đặt” ở trang 15.

<!-- pdf-page: 41 | printed: 8 -->

#### Chạy Python trong một phiên terminal

Bạn có thể thử chạy các đoạn mã Python ngắn bằng cách mở một terminal và gõ `python` hoặc `python3`, giống như khi kiểm tra phiên bản. Hãy làm lại điều đó, nhưng lần này nhập dòng sau vào phiên terminal:

```python
>>> print("Hello Python interpreter!")
Hello Python interpreter!
>>>
```

Bạn sẽ thấy thông điệp được in trực tiếp trong cửa sổ terminal hiện tại. Hãy nhớ rằng bạn có thể đóng trình thông dịch Python bằng cách nhấn CTRL-D hoặc gõ lệnh `exit()`.

### Python trên OS X

Python đã được cài sẵn trên hầu hết các hệ thống OS X. Khi đã biết Python được cài, bạn cần cài một trình soạn thảo văn bản và đảm bảo nó được cấu hình đúng.

#### Kiểm tra xem Python đã được cài chưa

Mở một cửa sổ terminal bằng cách vào **Applications**▸**Utilities**▸**Terminal**. Bạn cũng có thể nhấn COMMAND-phím cách, gõ `terminal`, rồi nhấn ENTER. Để biết Python đã được cài hay chưa, hãy nhập `python` với chữ *p* viết thường. Bạn sẽ thấy đầu ra cho biết phiên bản Python nào được cài trên hệ thống và một dấu nhắc `>>>` nơi bạn có thể bắt đầu nhập các lệnh Python, như thế này:

```text
$ python
Python 2.7.5 (default, Mar  9 2014, 22:15:05)
[GCC  4.2.1 Compatible Apple LLVM 5.0 (clang-500.0.68)] on darwin
Type "help", "copyright", "credits", or "license" for more information.
>>>
```

Đầu ra này cho biết Python 2.7.5 hiện là phiên bản mặc định được cài trên máy tính này. Khi đã thấy đầu ra này, hãy nhấn CTRL-D hoặc nhập `exit()` để thoát khỏi dấu nhắc Python và quay về dấu nhắc của terminal.

Để kiểm tra Python 3, hãy thử lệnh `python3`. Có thể bạn sẽ nhận được thông báo lỗi, nhưng nếu đầu ra cho thấy bạn đã cài Python 3, bạn có thể dùng Python 3 mà không cần cài đặt. Nếu `python3` chạy được trên hệ thống của bạn, thì bất cứ khi nào thấy lệnh `python` trong sách này, hãy nhớ dùng `python3` thay thế. Nếu vì lý do nào đó hệ thống của bạn không có sẵn Python, hoặc bạn chỉ có Python 2 và muốn cài Python 3 ngay bây giờ, hãy xem Phụ lục A.

<!-- pdf-page: 42 | printed: 9 -->

#### Chạy Python trong một phiên terminal

Bạn có thể thử chạy các đoạn mã Python ngắn bằng cách mở một terminal và gõ `python` hoặc `python3`, giống như khi kiểm tra phiên bản. Hãy làm lại điều đó, nhưng lần này nhập dòng sau vào phiên terminal:

```python
>>> print("Hello Python interpreter!")
Hello Python interpreter!
>>>
```

Bạn sẽ thấy thông điệp được in trực tiếp trong cửa sổ terminal hiện tại. Hãy nhớ rằng bạn có thể đóng trình thông dịch Python bằng cách nhấn CTRL-D hoặc gõ lệnh `exit()`.

#### Cài đặt trình soạn thảo văn bản

Sublime Text là một trình soạn thảo văn bản đơn giản: nó dễ cài đặt trên OS X, cho phép bạn chạy hầu hết các chương trình trực tiếp từ trình soạn thảo thay vì qua terminal, dùng tính năng tô sáng cú pháp để tô màu mã, và chạy mã trong một phiên terminal được nhúng ngay trong cửa sổ Sublime Text để bạn dễ dàng xem đầu ra. Phụ lục B cung cấp thông tin về các trình soạn thảo văn bản khác, nhưng tôi khuyên bạn dùng Sublime Text trừ khi bạn có lý do chính đáng để dùng một trình soạn thảo khác.

Bạn có thể tải trình cài đặt Sublime Text tại *http://sublimetext.com/3*. Nhấp vào liên kết tải về và tìm trình cài đặt dành cho OS X. Sublime Text có chính sách cấp phép rất thoáng: bạn có thể dùng trình soạn thảo miễn phí bao lâu tùy thích, nhưng tác giả đề nghị bạn mua giấy phép nếu thích nó và muốn dùng lâu dài. Sau khi tải trình cài đặt về, hãy mở nó rồi kéo biểu tượng Sublime Text vào thư mục *Applications*.

#### Cấu hình Sublime Text cho Python 3

Nếu bạn dùng một lệnh khác `python` để bắt đầu phiên terminal Python, bạn cần cấu hình Sublime Text để nó biết tìm phiên bản Python đúng ở đâu trên hệ thống. Hãy chạy lệnh sau để tìm đường dẫn đầy đủ tới trình thông dịch Python của bạn:

```text
$ type -a python3
python3 is /usr/local/bin/python3
```

Bây giờ, mở Sublime Text và vào **Tools**▸**Build System**▸**New Build System**; thao tác này sẽ mở một file cấu hình mới cho bạn. Xóa những gì bạn thấy và nhập nội dung sau:

**Python3.sublime-build**

```text
{
    "cmd": ["/usr/local/bin/python3", "-u", "$file"],
}
```

<!-- pdf-page: 43 | printed: 10 -->

Đoạn mã này yêu cầu Sublime Text dùng lệnh `python3` của hệ thống khi chạy file đang mở. Hãy đảm bảo bạn dùng đúng đường dẫn đã tìm được khi chạy lệnh `type -a python3` ở bước trước. Lưu file với tên *Python3.sublime-build* trong thư mục mặc định mà Sublime Text mở ra khi bạn chọn Save.

#### Chạy chương trình Hello World

Để bắt đầu chương trình đầu tiên, hãy khởi động Sublime Text bằng cách mở thư mục *Applications* và nhấp đúp vào biểu tượng Sublime Text. Bạn cũng có thể nhấn COMMAND-phím cách và nhập `sublime text` vào thanh tìm kiếm hiện ra.

Tạo một thư mục có tên *python_work* ở đâu đó trên hệ thống để chứa các dự án. (Tốt nhất là dùng chữ thường và dấu gạch dưới thay cho dấu cách trong tên file và tên thư mục, vì đó là các quy ước đặt tên của Python.) Lưu một file Python trống (**File**▸**Save As**) có tên *hello_world.py* vào thư mục *python_work*. Phần mở rộng *.py* cho Sublime Text biết file của bạn sẽ chứa một chương trình Python, đồng thời cho nó biết cách chạy chương trình và tô sáng văn bản theo cách hữu ích.

Sau khi đã lưu file, hãy nhập dòng sau:

```python
print("Hello Python world!")
```

Nếu lệnh `python` chạy được trên hệ thống của bạn, bạn có thể chạy chương trình bằng cách chọn **Tools**▸**Build** trong menu hoặc nhấn CTRL-B. Nếu bạn đã cấu hình Sublime Text để dùng một lệnh khác `python`, hãy chọn **Tools**▸**Build System** rồi chọn **Python 3**. Thao tác này đặt Python 3 làm phiên bản Python mặc định, và từ giờ bạn có thể chọn **Tools**▸**Build** hoặc chỉ cần nhấn COMMAND-B để chạy chương trình.

Một màn hình terminal sẽ xuất hiện ở cuối cửa sổ Sublime Text, hiển thị đầu ra sau:

```text
Hello Python world!
[Finished in 0.1s]
```

Nếu không thấy kết quả này, hãy kiểm tra từng ký tự trên dòng bạn đã nhập. Bạn có vô tình viết hoa chữ `print` không? Bạn có quên một hoặc cả hai dấu ngoặc kép hay dấu ngoặc đơn không? Ngôn ngữ lập trình đòi hỏi cú pháp rất cụ thể, và nếu bạn không tuân theo, bạn sẽ gặp lỗi. Nếu không thể chạy được chương trình, hãy xem mục “Khắc phục sự cố cài đặt” ở trang 15.

### Python trên Windows

Windows không phải lúc nào cũng có sẵn Python, nên có lẽ bạn sẽ cần tải về và cài đặt nó, sau đó tải về và cài một trình soạn thảo văn bản.

<!-- pdf-page: 44 | printed: 11 -->

#### Cài đặt Python

Trước hết, hãy kiểm tra xem Python đã được cài trên hệ thống chưa. Mở một cửa sổ lệnh bằng cách nhập `command` vào menu Start, hoặc giữ phím SHIFT trong khi nhấp chuột phải trên màn hình nền rồi chọn **Open command window here**. Trong cửa sổ terminal, nhập `python` bằng chữ thường. Nếu bạn nhận được dấu nhắc Python (`>>>`), nghĩa là Python đã được cài trên hệ thống. Tuy nhiên, nhiều khả năng bạn sẽ thấy một thông báo lỗi cho biết `python` không phải là một lệnh được nhận dạng.

Trong trường hợp đó, hãy tải trình cài đặt Python dành cho Windows. Truy cập *http://python.org/downloads/.* Bạn sẽ thấy hai nút, một nút để tải Python 3 và một nút để tải Python 2. Nhấp vào nút Python 3; trình cài đặt phù hợp với hệ thống của bạn sẽ tự động được tải về. Sau khi tải file xong, hãy chạy trình cài đặt. Nhớ đánh dấu tùy chọn Add Python to PATH, tùy chọn này sẽ giúp bạn cấu hình hệ thống đúng cách dễ dàng hơn. Hình 1-2 cho thấy tùy chọn này đã được đánh dấu.

*Hình 1-2: Hãy nhớ đánh dấu vào ô có nhãn Add Python to PATH.*

#### Khởi động một phiên terminal Python

Việc thiết lập trình soạn thảo văn bản sẽ đơn giản nếu trước tiên bạn thiết lập hệ thống để chạy Python trong một phiên terminal. Mở một cửa sổ lệnh và nhập `python` bằng chữ thường. Nếu bạn nhận được dấu nhắc Python (`>>>`), Windows đã tìm thấy phiên bản Python bạn vừa cài:

```text
C:\> python
Python 3.5.0 (v3.5.0:374f501f4567, Sep 13 2015, 22:15:05) [MSC v.1900 32 bit
(Intel)] on win32
Type "help", "copyright", "credits" or "license" for more information.
>>>
```

<!-- pdf-page: 45 | printed: 12 -->

Nếu cách này chạy được, bạn có thể chuyển sang mục tiếp theo, “Chạy Python trong một phiên terminal”.

Tuy nhiên, bạn có thể thấy đầu ra trông giống thế này hơn:

```text
C:\> python
'python' is not recognized as an internal or external command, operable
program or batch file.
```

Trong trường hợp này, bạn cần cho Windows biết cách tìm phiên bản Python bạn vừa cài. Lệnh `python` của hệ thống thường được lưu trong ổ *C*, vì vậy hãy mở Windows Explorer và mở ổ *C*. Tìm một thư mục có tên bắt đầu bằng *Python*, mở thư mục đó và tìm file *python* (viết thường). Ví dụ, tôi có một thư mục *Python35* chứa một file tên là *python*, nên đường dẫn tới lệnh `python` trên hệ thống của tôi là *C:\Python35\python*. Nếu không, hãy nhập `python` vào ô tìm kiếm trong Windows Explorer để biết chính xác lệnh `python` được lưu ở đâu trên hệ thống của bạn.

Khi đã nghĩ mình biết đường dẫn, hãy kiểm tra bằng cách nhập đường dẫn đó vào một cửa sổ terminal. Mở một cửa sổ lệnh và nhập đường dẫn đầy đủ bạn vừa tìm được:

```text
C:\> C:\Python35\python
Python 3.5.0 (v3.5.0:374f501f4567, Sep 13 2015, 22:15:05) [MSC v.1900 32 bit
(Intel)] on win32
Type "help", "copyright", "credits" or "license" for more information.
>>>
```

Nếu cách này chạy được, bạn đã biết cách truy cập Python trên hệ thống của mình.

#### Chạy Python trong một phiên terminal

Nhập dòng sau vào phiên Python và đảm bảo bạn thấy đầu ra *Hello Python world!*

```python
>>> print("Hello Python world!")
Hello Python world!
>>>
```

Bất cứ khi nào muốn chạy một đoạn mã Python ngắn, hãy mở một cửa sổ lệnh và khởi động một phiên terminal Python. Để đóng phiên terminal, hãy nhấn CTRL-Z rồi nhấn ENTER, hoặc nhập lệnh `exit()`.

#### Cài đặt trình soạn thảo văn bản

Geany là một trình soạn thảo văn bản đơn giản: nó dễ cài đặt, cho phép bạn chạy hầu hết các chương trình trực tiếp từ trình soạn thảo thay vì qua terminal, dùng tính năng tô sáng cú pháp để tô màu mã của bạn, và chạy mã trong một cửa sổ terminal để bạn làm quen với việc dùng terminal. Phụ lục B cung cấp thông tin về các trình soạn thảo văn bản khác, nhưng tôi khuyên bạn dùng Geany trừ khi bạn có lý do chính đáng để dùng một trình soạn thảo khác.

<!-- pdf-page: 46 | printed: 13 -->

Bạn có thể tải trình cài đặt Geany cho Windows tại *http://geany.org/.* Nhấp vào **Releases** trong menu Download và tìm trình cài đặt *geany-1.25_setup.exe* hoặc một file tương tự. Chạy trình cài đặt và chấp nhận mọi thiết lập mặc định.

Để bắt đầu chương trình đầu tiên, hãy mở Geany: nhấn phím Windows và tìm Geany trên hệ thống. Bạn nên tạo một lối tắt bằng cách kéo biểu tượng vào thanh tác vụ hoặc màn hình nền. Tạo một thư mục có tên *python_work* ở đâu đó trên hệ thống để chứa các dự án. (Tốt nhất là dùng chữ thường và dấu gạch dưới thay cho dấu cách trong tên file và tên thư mục, vì đó là các quy ước đặt tên của Python.) Quay lại Geany và lưu một file Python trống (**File**▸**Save As**) có tên *hello_world.py* vào thư mục *python_work*. Phần mở rộng *.py* cho Geany biết file của bạn sẽ chứa một chương trình Python. Nó cũng cho Geany biết cách chạy chương trình và tô sáng văn bản theo cách hữu ích.

Sau khi đã lưu file, hãy gõ dòng sau:

```python
print("Hello Python world!")
```

Nếu lệnh `python` chạy được trên hệ thống của bạn, bạn không cần cấu hình Geany; hãy bỏ qua mục tiếp theo và chuyển sang mục “Chạy chương trình Hello World” ở trang 14. Nếu bạn phải nhập một đường dẫn như *C:\Python35\python* để khởi động trình thông dịch Python, hãy làm theo hướng dẫn trong mục tiếp theo để cấu hình Geany cho hệ thống của bạn.

#### Cấu hình Geany

Để cấu hình Geany, hãy vào **Build**▸**Set Build Commands**. Bạn sẽ thấy hai chữ *Compile* và *Execute*, mỗi chữ có một lệnh bên cạnh. Các lệnh Compile và Execute bắt đầu bằng `python` viết thường, nhưng Geany không biết hệ thống của bạn lưu lệnh `python` ở đâu. Bạn cần thêm đường dẫn mà bạn đã dùng trong phiên terminal.

Trong các lệnh Compile và Execute, hãy thêm ổ đĩa chứa lệnh `python` và thư mục nơi lệnh `python` được lưu. Lệnh Compile của bạn sẽ trông tương tự như thế này:

```text
C:\Python35\python -m py_compile "%f"
```

Đường dẫn của bạn có thể hơi khác, nhưng hãy đảm bảo dấu cách và chữ hoa, chữ thường khớp với những gì hiển thị ở đây.

Lệnh Execute của bạn sẽ trông tương tự như thế này:

```text
C:\Python35\python "%f"
```

Một lần nữa, hãy đảm bảo dấu cách và chữ hoa, chữ thường trong lệnh Execute khớp với những gì hiển thị ở đây. Hình 1-3 cho thấy các lệnh này trông như thế nào trong menu cấu hình của Geany.

<!-- pdf-page: 47 | printed: 14 -->

*Hình 1-3: Ở đây, Geany được cấu hình để dùng Python 3 trên Windows.*

Sau khi đã thiết lập đúng các lệnh này, hãy nhấp **OK**.

#### Chạy chương trình Hello World

Bây giờ bạn đã có thể chạy chương trình thành công. Chạy *hello_world.py* bằng cách chọn **Build**▸**Execute** trong menu, nhấp vào biểu tượng Execute (biểu tượng hình các bánh răng), hoặc nhấn F5. Một cửa sổ terminal sẽ bật lên với đầu ra sau:

```text
Hello Python world!

------------------
(program exited with code: 0)
Press return to continue
```

Nếu không thấy kết quả này, hãy kiểm tra từng ký tự trên dòng bạn đã nhập. Bạn có vô tình viết hoa chữ `print` không? Bạn có quên một hoặc cả hai dấu ngoặc kép hay dấu ngoặc đơn không? Ngôn ngữ lập trình đòi hỏi cú pháp rất cụ thể, và nếu bạn không tuân theo, bạn sẽ gặp lỗi. Nếu không thể chạy được chương trình, hãy xem mục tiếp theo để được trợ giúp.

<!-- pdf-page: 48 | printed: 15 -->

## Khắc phục sự cố cài đặt

Hy vọng việc thiết lập môi trường lập trình của bạn đã thành công, nhưng nếu bạn chưa chạy được *hello_world.py*, dưới đây là một vài cách khắc phục bạn có thể thử:

- Khi một chương trình có lỗi nghiêm trọng, Python sẽ hiển thị một *traceback* (thông báo truy vết lỗi). Python rà soát file và cố gắng báo cáo vấn đề. Traceback có thể cho bạn manh mối về vấn đề đang khiến chương trình không chạy được.

- Hãy rời khỏi máy tính, nghỉ ngơi một chút rồi thử lại. Hãy nhớ rằng cú pháp rất quan trọng trong lập trình, nên chỉ cần thiếu một dấu hai chấm, một dấu ngoặc kép không khớp hay dấu ngoặc đơn không khớp cũng có thể khiến chương trình không chạy đúng. Hãy đọc lại những phần liên quan trong chương này, xem lại những gì bạn đã làm và thử tìm ra lỗi.

- Bắt đầu lại từ đầu. Có lẽ bạn không cần gỡ cài đặt thứ gì, nhưng có thể nên xóa file *hello_world.py* rồi tạo lại nó từ đầu.

- Nhờ người khác làm theo các bước trong chương này, trên máy tính của bạn hoặc trên một máy khác, và quan sát kỹ những gì họ làm. Có thể bạn đã bỏ lỡ một bước nhỏ mà người khác tình cờ phát hiện ra.

- Tìm một người biết Python và nhờ họ giúp bạn thiết lập. Nếu hỏi quanh, có thể bạn sẽ phát hiện mình quen một người đang dùng Python.

- Hướng dẫn thiết lập trong chương này cũng có sẵn trực tuyến tại *https://www.nostarch.com/pythoncrashcourse/*. Phiên bản trực tuyến của các hướng dẫn này có thể phù hợp với bạn hơn.

- Tìm trợ giúp trực tuyến. Phụ lục C giới thiệu một số tài nguyên và nơi trực tuyến, như diễn đàn và các trang trò chuyện trực tiếp, nơi bạn có thể hỏi cách giải quyết từ những người đã từng gặp đúng vấn đề bạn đang gặp.

Đừng ngại làm phiền những lập trình viên giàu kinh nghiệm. Lập trình viên nào cũng từng bị mắc kẹt ở một thời điểm nào đó, và hầu hết lập trình viên đều sẵn lòng giúp bạn thiết lập hệ thống đúng cách. Chỉ cần bạn trình bày rõ ràng mình đang cố làm gì, đã thử những gì và nhận được kết quả ra sao, thì rất có thể sẽ có người giúp được bạn. Như đã đề cập trong Lời giới thiệu, cộng đồng Python rất thân thiện với người mới bắt đầu.

Python chạy tốt trên mọi máy tính hiện đại, vì vậy hãy tìm cách nhờ giúp đỡ nếu đến giờ bạn vẫn gặp khó khăn. Những vấn đề ban đầu có thể gây nản lòng, nhưng chúng hoàn toàn đáng để giải quyết. Một khi đã chạy được *hello_world.py*, bạn có thể bắt đầu học Python, và công việc lập trình của bạn sẽ trở nên thú vị và đem lại nhiều niềm vui hơn.

<!-- pdf-page: 49 | printed: 16 -->

## Chạy chương trình Python từ terminal

Phần lớn các chương trình bạn viết trong trình soạn thảo văn bản sẽ được chạy trực tiếp từ trình soạn thảo, nhưng đôi khi chạy chương trình từ terminal lại hữu ích hơn. Ví dụ, bạn có thể muốn chạy một chương trình có sẵn mà không cần mở nó ra để chỉnh sửa.

Bạn có thể làm điều này trên mọi hệ thống có cài Python, miễn là bạn biết cách truy cập thư mục nơi lưu file chương trình. Để thử, hãy đảm bảo bạn đã lưu file *hello_world.py* trong thư mục *python_work* trên màn hình nền.

### Trên Linux và OS X

Chạy chương trình Python từ một phiên terminal trên Linux và OS X là như nhau. Lệnh terminal `cd`, viết tắt của *change directory* (đổi thư mục), được dùng để di chuyển trong hệ thống file khi ở một phiên terminal. Lệnh `ls`, viết tắt của *list* (liệt kê), hiển thị tất cả các file không bị ẩn trong thư mục hiện tại.

Mở một cửa sổ terminal mới và chạy các lệnh sau để chạy *hello_world.py*:

```text
❶ ~$ cd Desktop/python_work/
❷ ~/Desktop/python_work$ ls
  hello_world.py
❸ ~/Desktop/python_work$ python hello_world.py
  Hello Python world!
```

Tại ❶, chúng ta dùng lệnh `cd` để di chuyển tới thư mục *python_work*, nằm trong thư mục *Desktop*. Tiếp theo, chúng ta dùng lệnh `ls` để đảm bảo *hello_world.py* có trong thư mục này ❷. Sau đó, chúng ta chạy file bằng lệnh `python hello_world.py` ❸.

Đơn giản vậy thôi. Bạn chỉ cần dùng lệnh `python` (hoặc `python3`) để chạy các chương trình Python.

### Trên Windows

Lệnh terminal `cd`, viết tắt của *change directory* (đổi thư mục), được dùng để di chuyển trong hệ thống file khi ở một cửa sổ lệnh. Lệnh `dir`, viết tắt của *directory* (thư mục), hiển thị tất cả các file có trong thư mục hiện tại.

Mở một cửa sổ terminal mới và chạy các lệnh sau để chạy *hello_world.py*:

```text
❶ C:\> cd Desktop\python_work
❷ C:\Desktop\python_work> dir
  hello_world.py
❸ C:\Desktop\python_work> python hello_world.py
  Hello Python world!
```

Tại ❶, chúng ta dùng lệnh `cd` để di chuyển tới thư mục *python_work*, nằm trong thư mục *Desktop*. Tiếp theo, chúng ta dùng lệnh `dir` để đảm bảo *hello_world.py* có trong thư mục này ❷. Sau đó, chúng ta chạy file bằng lệnh `python hello_world.py` ❸.

<!-- pdf-page: 50 | printed: 17 -->

Nếu bạn chưa cấu hình hệ thống để dùng lệnh ngắn gọn `python`, có thể bạn sẽ cần dùng phiên bản dài hơn của lệnh này:

```text
C:\$ cd Desktop\python_work
C:\Desktop\python_work$ dir
hello_world.py
C:\Desktop\python_work$ C:\Python35\python hello_world.py
Hello Python world!
```

Phần lớn chương trình của bạn sẽ chạy tốt trực tiếp từ trình soạn thảo, nhưng khi công việc trở nên phức tạp hơn, có thể bạn sẽ viết những chương trình cần chạy từ terminal.

<!-- box -->

**Tự mình thực hành**

Các bài tập trong chương này mang tính khám phá. Bắt đầu từ Chương 2, những thử thách bạn giải sẽ dựa trên những gì bạn đã học.

**1-1. python.org:** Khám phá trang chủ của Python (*http://python.org/*) để tìm những chủ đề bạn quan tâm. Khi đã quen thuộc hơn với Python, các phần khác nhau của trang web sẽ ngày càng hữu ích với bạn.

**1-2. Lỗi gõ trong Hello World:** Mở file *hello_world.py* bạn vừa tạo. Gõ sai một chỗ nào đó trên dòng mã và chạy lại chương trình. Bạn có thể tạo ra một lỗi gõ khiến chương trình báo lỗi không? Bạn có hiểu được thông báo lỗi không? Bạn có thể tạo ra một lỗi gõ mà không gây ra lỗi không? Theo bạn, tại sao nó lại không gây ra lỗi?

**1-3. Kỹ năng vô hạn:** Nếu bạn có kỹ năng lập trình vô hạn, bạn sẽ xây dựng gì? Bạn sắp học cách lập trình. Nếu bạn có sẵn một mục tiêu cuối cùng trong đầu, bạn sẽ có ngay chỗ để dùng những kỹ năng mới của mình; bây giờ là thời điểm tuyệt vời để phác thảo mô tả những gì bạn muốn tạo ra. Một thói quen tốt là giữ một cuốn sổ "ý tưởng" để bạn có thể tham khảo bất cứ khi nào muốn bắt đầu một dự án mới. Hãy dành vài phút ngay bây giờ để mô tả ba chương trình bạn muốn tạo ra.

<!-- /box -->

## Tổng kết

Trong chương này, bạn đã tìm hiểu đôi chút về Python nói chung, và đã cài Python lên hệ thống nếu nó chưa có sẵn. Bạn cũng đã cài một trình soạn thảo văn bản để viết mã Python dễ dàng hơn. Bạn đã học cách chạy các đoạn mã Python ngắn trong một phiên terminal, và đã chạy chương trình thực sự đầu tiên của mình, *hello_world.py*. Có lẽ bạn cũng đã học được đôi chút về cách khắc phục sự cố.

Trong chương tiếp theo, bạn sẽ tìm hiểu về các kiểu dữ liệu khác nhau mà bạn có thể làm việc cùng trong chương trình Python, đồng thời học cách sử dụng biến.

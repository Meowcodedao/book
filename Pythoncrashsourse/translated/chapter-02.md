<!-- source: pythoncrashcourse.pdf | unit: chapter-02 | pdf pages 52-69 | printed 19-36 -->

# Chương 2: Biến và các kiểu dữ liệu đơn giản

<!-- pdf-page: 52 | printed: 19 -->

Trong chương này, bạn sẽ tìm hiểu các kiểu dữ liệu khác nhau mà bạn có thể làm việc cùng trong chương trình Python. Bạn cũng sẽ học cách lưu trữ dữ liệu trong biến và cách sử dụng những biến đó trong chương trình.

## Điều gì thực sự xảy ra khi bạn chạy hello_world.py

Hãy xem kỹ hơn những gì Python làm khi bạn chạy *hello_world.py*. Hóa ra, Python phải làm khá nhiều việc, ngay cả khi chạy một chương trình đơn giản:

**hello_world.py**

```python
print("Hello Python world!")
```

<!-- pdf-page: 53 | printed: 20 -->

Khi chạy đoạn mã này, bạn sẽ thấy đầu ra sau:

```text
Hello Python world!
```

Khi bạn chạy file *hello_world.py*, phần đuôi *.py* cho biết file này là một chương trình Python. Trình soạn thảo của bạn sau đó sẽ chạy file thông qua *trình thông dịch Python,* chương trình đọc qua toàn bộ mã và xác định ý nghĩa của từng từ trong đó. Ví dụ, khi trình thông dịch thấy từ `print`, nó sẽ in ra màn hình bất cứ thứ gì nằm bên trong cặp dấu ngoặc đơn.

Khi bạn viết chương trình, trình soạn thảo sẽ tô sáng các phần khác nhau của chương trình theo những cách khác nhau. Ví dụ, nó nhận ra `print` là tên của một hàm và hiển thị từ đó bằng màu xanh dương. Nó nhận ra “Hello Python world!” không phải là mã Python và hiển thị cụm từ đó bằng màu cam. Tính năng này được gọi là *tô sáng cú pháp* (syntax highlighting) và khá hữu ích khi bạn bắt đầu viết chương trình của riêng mình.

## Biến

Hãy thử dùng một biến trong *hello_world.py*. Thêm một dòng mới vào đầu file và sửa dòng thứ hai:

```python
message = "Hello Python world!"
print(message)
```

Chạy chương trình này để xem điều gì xảy ra. Bạn sẽ thấy đầu ra giống như trước:

```text
Hello Python world!
```

Chúng ta vừa thêm một *biến* (variable) tên là `message`. Mỗi biến chứa một *giá trị* (value), tức là thông tin gắn với biến đó. Trong trường hợp này, giá trị là đoạn văn bản “Hello Python world!”

Việc thêm một biến khiến trình thông dịch Python phải làm thêm một chút việc. Khi xử lý dòng đầu tiên, nó gắn đoạn văn bản “Hello Python world!” với biến `message`. Khi tới dòng thứ hai, nó in giá trị gắn với `message` ra màn hình.

Hãy mở rộng chương trình này bằng cách sửa *hello_world.py* để in thêm một thông điệp thứ hai. Thêm một dòng trống vào *hello_world.py*, rồi thêm hai dòng mã mới:

```python
message = "Hello Python world!"
print(message)

message = "Hello Python Crash Course world!"
print(message)
```

<!-- pdf-page: 54 | printed: 21 -->

Bây giờ khi chạy *hello_world.py*, bạn sẽ thấy hai dòng đầu ra:

```text
Hello Python world!
Hello Python Crash Course world!
```

Bạn có thể thay đổi giá trị của một biến trong chương trình bất cứ lúc nào, và Python sẽ luôn theo dõi giá trị hiện tại của nó.

### Đặt tên và sử dụng biến

Khi dùng biến trong Python, bạn cần tuân theo một vài quy tắc và hướng dẫn. Vi phạm một số quy tắc sẽ gây ra lỗi; những hướng dẫn còn lại chỉ giúp bạn viết mã dễ đọc và dễ hiểu hơn. Hãy nhớ kỹ các quy tắc về biến sau đây:

- Tên biến chỉ được chứa chữ cái, chữ số và dấu gạch dưới. Tên biến có thể bắt đầu bằng một chữ cái hoặc dấu gạch dưới, nhưng không được bắt đầu bằng chữ số. Chẳng hạn, bạn có thể đặt tên biến là *message_1* nhưng không thể là *1_message*.

- Tên biến không được chứa dấu cách, nhưng có thể dùng dấu gạch dưới để phân tách các từ trong tên biến. Ví dụ, *greeting_message* thì hợp lệ, còn *greeting message* sẽ gây ra lỗi.

- Tránh dùng từ khóa và tên hàm của Python làm tên biến; nghĩa là đừng dùng những từ mà Python đã dành riêng cho một mục đích lập trình cụ thể, chẳng hạn như từ `print`. (Xem mục “Từ khóa và hàm có sẵn của Python” ở trang 489.)

- Tên biến nên ngắn gọn nhưng mang tính mô tả. Ví dụ, *name* tốt hơn *n*, *student_name* tốt hơn *s_n*, và *name_length* tốt hơn *length_of_persons_name*.

- Hãy cẩn thận khi dùng chữ *l* thường và chữ *O* hoa, vì chúng dễ bị nhầm với các chữ số *1* và *0*.

Có thể bạn sẽ cần luyện tập một thời gian để biết cách đặt tên biến tốt, nhất là khi chương trình của bạn trở nên thú vị và phức tạp hơn. Khi viết nhiều chương trình hơn và bắt đầu đọc mã của người khác, bạn sẽ ngày càng giỏi nghĩ ra những cái tên có ý nghĩa.

> **Lưu ý** Các biến Python bạn đang dùng ở giai đoạn này nên được viết bằng chữ thường. Bạn sẽ không gặp lỗi nếu dùng chữ hoa, nhưng tạm thời nên tránh dùng chúng.

### Tránh lỗi tên khi sử dụng biến

Lập trình viên nào cũng mắc lỗi, và hầu hết đều mắc lỗi mỗi ngày. Dù lập trình viên giỏi vẫn có thể gây ra lỗi, họ biết cách xử lý những lỗi đó một cách hiệu quả. Hãy xem một lỗi mà nhiều khả năng bạn sẽ mắc phải từ sớm và học cách sửa nó.

<!-- pdf-page: 55 | printed: 22 -->

Chúng ta sẽ cố tình viết một đoạn mã gây ra lỗi. Hãy nhập đoạn mã sau, kể cả từ viết sai chính tả *mesage* được in đậm:

```python
message = "Hello Python Crash Course reader!"
print(mesage)
```

Khi chương trình gặp lỗi, trình thông dịch Python sẽ cố hết sức giúp bạn tìm ra vấn đề nằm ở đâu. Trình thông dịch cung cấp một traceback khi chương trình không thể chạy thành công. *Traceback* là bản ghi lại vị trí mà trình thông dịch gặp trục trặc khi cố thực thi mã của bạn. Dưới đây là ví dụ về traceback mà Python đưa ra sau khi bạn vô tình viết sai tên một biến:

```text
  Traceback (most recent call last):
❶   File "hello_world.py", line 2, in <module>
❷     print(mesage)
❸ NameError: name 'mesage' is not defined
```

Đầu ra tại ❶ báo rằng có lỗi xảy ra ở dòng 2 của file *hello_world.py*. Trình thông dịch hiển thị dòng này để giúp chúng ta nhanh chóng phát hiện lỗi ❷ và cho biết nó đã tìm thấy loại lỗi gì ❸. Trong trường hợp này, nó tìm thấy một *lỗi tên* (name error) và báo rằng biến đang được in, `mesage`, chưa được định nghĩa. Python không thể nhận ra tên biến được cung cấp. Lỗi tên thường có nghĩa là chúng ta đã quên gán giá trị cho biến trước khi dùng nó, hoặc đã gõ sai chính tả khi nhập tên biến.

Tất nhiên, trong ví dụ này chúng ta đã bỏ sót chữ *s* trong tên biến `message` ở dòng thứ hai. Trình thông dịch Python không kiểm tra chính tả mã của bạn, nhưng nó đảm bảo rằng tên biến được viết nhất quán. Ví dụ, hãy xem điều gì xảy ra khi chúng ta cũng viết sai *message* ở một chỗ khác trong mã:

```python
mesage = "Hello Python Crash Course reader!"
print(mesage)
```

Trong trường hợp này, chương trình chạy thành công!

```text
Hello Python Crash Course reader!
```

Máy tính rất khắt khe, nhưng chúng không quan tâm chính tả đúng hay sai. Vì vậy, bạn không cần để ý đến các quy tắc chính tả và ngữ pháp tiếng Anh khi đặt tên biến và viết mã.

Rất nhiều lỗi lập trình chỉ là lỗi gõ sai một ký tự trên một dòng của chương trình. Nếu bạn đang mất nhiều thời gian để tìm một lỗi như vậy, hãy biết rằng bạn không hề đơn độc. Nhiều lập trình viên giàu kinh nghiệm và tài năng vẫn mất hàng giờ để săn lùng những lỗi nhỏ xíu kiểu này. Hãy cười cho qua và tiếp tục, vì biết rằng chuyện này sẽ xảy ra thường xuyên trong suốt cuộc đời lập trình của bạn.

<!-- pdf-page: 56 | printed: 23 -->

> **Lưu ý** Cách tốt nhất để hiểu các khái niệm lập trình mới là thử dùng chúng trong chương trình của bạn. Nếu bị mắc kẹt khi làm một bài tập trong sách, hãy thử làm việc khác một lúc. Nếu vẫn bế tắc, hãy xem lại phần liên quan của chương đó. Nếu vẫn cần trợ giúp, hãy xem các gợi ý trong Phụ lục C.

<!-- box -->

**Tự mình thực hành**

Hãy viết một chương trình riêng cho từng bài tập dưới đây. Lưu mỗi chương trình với tên file tuân theo quy ước chuẩn của Python, dùng chữ thường và dấu gạch dưới, chẳng hạn *simple_message.py* và *simple_messages.py*.

**2-1. Thông điệp đơn giản:** Lưu một thông điệp vào một biến, rồi in thông điệp đó ra.

**2-2. Các thông điệp đơn giản:** Lưu một thông điệp vào một biến và in thông điệp đó ra. Sau đó đổi giá trị của biến thành một thông điệp mới và in thông điệp mới ra.

<!-- /box -->

## Chuỗi

Vì hầu hết các chương trình đều định nghĩa và thu thập một loại dữ liệu nào đó rồi làm điều gì đó hữu ích với nó, nên việc phân loại các kiểu dữ liệu khác nhau sẽ rất có ích. Kiểu dữ liệu đầu tiên chúng ta xem xét là chuỗi. Thoạt nhìn, chuỗi khá đơn giản, nhưng bạn có thể dùng chúng theo rất nhiều cách khác nhau.

*Chuỗi* (string) đơn giản là một dãy ký tự. Trong Python, bất cứ thứ gì nằm trong dấu nháy đều được coi là chuỗi, và bạn có thể dùng dấu nháy đơn hoặc dấu nháy kép bao quanh chuỗi như sau:

```text
"This is a string."
'This is also a string.'
```

Sự linh hoạt này cho phép bạn dùng dấu nháy kép và dấu nháy đơn (dấu lược) bên trong chuỗi:

```text
'I told my friend, "Python is my favorite language!"'
"The language 'Python' is named after Monty Python, not the snake."
"One of Python's strengths is its diverse and supportive community."
```

Hãy cùng khám phá một số cách sử dụng chuỗi.

<!-- pdf-page: 57 | printed: 24 -->

### Thay đổi chữ hoa, chữ thường trong chuỗi bằng phương thức

Một trong những việc đơn giản nhất bạn có thể làm với chuỗi là thay đổi kiểu chữ hoa, chữ thường của các từ trong chuỗi. Hãy xem đoạn mã sau và thử đoán xem chuyện gì đang xảy ra:

**name.py**

```python
name = "ada lovelace"
print(name.title())
```

Lưu file này với tên *name.py* rồi chạy nó. Bạn sẽ thấy đầu ra sau:

```text
Ada Lovelace
```

Trong ví dụ này, chuỗi chữ thường `"ada lovelace"` được lưu trong biến `name`. Phương thức `title()` xuất hiện sau tên biến trong câu lệnh `print()`. *Phương thức* (method) là một hành động mà Python có thể thực hiện trên một mẩu dữ liệu. Dấu chấm (`.`) sau `name` trong `name.title()` yêu cầu Python cho phương thức `title()` tác động lên biến `name`. Mọi phương thức đều được theo sau bởi một cặp dấu ngoặc đơn, vì phương thức thường cần thêm thông tin để thực hiện công việc của nó. Thông tin đó được cung cấp bên trong cặp ngoặc đơn. Hàm `title()` không cần thêm thông tin nào, nên cặp ngoặc đơn của nó để trống.

`title()` hiển thị mỗi từ theo kiểu viết hoa chữ cái đầu (titlecase), tức là mỗi từ đều bắt đầu bằng một chữ cái viết hoa. Điều này hữu ích vì bạn thường muốn coi một cái tên là một mẩu thông tin. Ví dụ, bạn có thể muốn chương trình nhận diện các giá trị đầu vào `Ada`, `ADA` và `ada` là cùng một tên, và hiển thị tất cả chúng thành `Ada`.

Ngoài ra còn có một vài phương thức hữu ích khác để xử lý chữ hoa, chữ thường. Ví dụ, bạn có thể chuyển một chuỗi thành toàn chữ hoa hoặc toàn chữ thường như sau:

```python
name = "Ada Lovelace"
print(name.upper())
print(name.lower())
```

Đoạn mã này sẽ hiển thị như sau:

```text
ADA LOVELACE
ada lovelace
```

Phương thức `lower()` đặc biệt hữu ích khi lưu trữ dữ liệu. Nhiều khi bạn sẽ không muốn tin vào cách viết hoa mà người dùng nhập vào, nên bạn sẽ chuyển chuỗi thành chữ thường trước khi lưu. Sau đó, khi muốn hiển thị thông tin, bạn sẽ dùng kiểu chữ hợp lý nhất cho từng chuỗi.

<!-- pdf-page: 58 | printed: 25 -->

### Kết hợp hay nối chuỗi

Việc kết hợp các chuỗi thường rất hữu ích. Ví dụ, bạn có thể muốn lưu tên và họ trong hai biến riêng, rồi kết hợp chúng khi muốn hiển thị họ tên đầy đủ của một người:

```python
  first_name = "ada"
  last_name = "lovelace"
❶ full_name = first_name + " " + last_name

  print(full_name)
```

Python dùng dấu cộng (`+`) để kết hợp các chuỗi. Trong ví dụ này, chúng ta dùng `+` để tạo họ tên đầy đủ bằng cách kết hợp `first_name`, một dấu cách và `last_name` ❶, cho ra kết quả sau:

```text
ada lovelace
```

Cách kết hợp chuỗi này được gọi là *nối chuỗi* (concatenation). Bạn có thể dùng phép nối chuỗi để tạo ra những thông điệp hoàn chỉnh từ thông tin đã lưu trong biến. Hãy xem một ví dụ:

```python
  first_name = "ada"
  last_name = "lovelace"
  full_name = first_name + " " + last_name

❶ print("Hello, " + full_name.title() + "!")
```

Ở đây, họ tên đầy đủ được dùng tại ❶ trong một câu chào người dùng, và phương thức `title()` được dùng để định dạng tên cho phù hợp. Đoạn mã này trả về một lời chào đơn giản nhưng được định dạng đẹp mắt:

```text
Hello, Ada Lovelace!
```

Bạn có thể dùng phép nối chuỗi để tạo một thông điệp rồi lưu toàn bộ thông điệp đó vào một biến:

```python
  first_name = "ada"
  last_name = "lovelace"
  full_name = first_name + " " + last_name

❶ message = "Hello, " + full_name.title() + "!"
❷ print(message)
```

Đoạn mã này cũng hiển thị thông điệp “Hello, Ada Lovelace!”, nhưng việc lưu thông điệp vào một biến tại ❶ giúp câu lệnh `print` cuối cùng tại ❷ đơn giản hơn nhiều.

<!-- pdf-page: 59 | printed: 26 -->

### Thêm khoảng trắng vào chuỗi bằng tab hoặc ký tự xuống dòng

Trong lập trình, *khoảng trắng* (whitespace) là bất kỳ ký tự không in ra được nào, chẳng hạn như dấu cách, tab và ký hiệu cuối dòng. Bạn có thể dùng khoảng trắng để sắp xếp đầu ra sao cho người dùng dễ đọc hơn.

Để thêm một tab vào văn bản, hãy dùng tổ hợp ký tự `\t` như tại ❶:

```python
  >>> print("Python")
  Python
❶ >>> print("\tPython")
      Python
```

Để thêm một dòng mới vào chuỗi, hãy dùng tổ hợp ký tự `\n`:

```python
>>> print("Languages:\nPython\nC\nJavaScript")
Languages:
Python
C
JavaScript
```

Bạn cũng có thể kết hợp tab và ký tự xuống dòng trong cùng một chuỗi. Chuỗi `"\n\t"` yêu cầu Python chuyển sang dòng mới và bắt đầu dòng tiếp theo bằng một tab. Ví dụ sau cho thấy cách dùng một chuỗi trên một dòng để tạo ra bốn dòng đầu ra:

```python
>>> print("Languages:\n\tPython\n\tC\n\tJavaScript")
Languages:
    Python
    C
    JavaScript
```

Ký tự xuống dòng và tab sẽ rất hữu ích trong hai chương tiếp theo, khi bạn bắt đầu tạo ra nhiều dòng đầu ra chỉ từ vài dòng mã.

### Loại bỏ khoảng trắng

Khoảng trắng thừa có thể gây nhầm lẫn trong chương trình. Đối với lập trình viên, `'python'` và `'python '` trông gần như giống hệt nhau. Nhưng đối với chương trình, chúng là hai chuỗi khác nhau. Python phát hiện dấu cách thừa trong `'python '` và coi nó là có ý nghĩa, trừ khi bạn bảo nó điều ngược lại.

Việc lưu ý đến khoảng trắng rất quan trọng, vì bạn thường sẽ muốn so sánh hai chuỗi để xác định chúng có giống nhau không. Một ví dụ quan trọng là kiểm tra tên người dùng khi họ đăng nhập vào một trang web. Khoảng trắng thừa cũng có thể gây nhầm lẫn trong những tình huống đơn giản hơn nhiều. May mắn thay, Python giúp bạn dễ dàng loại bỏ khoảng trắng thừa khỏi dữ liệu mà người dùng nhập vào.

Python có thể tìm khoảng trắng thừa ở phía bên phải và bên trái của một chuỗi. Để đảm bảo không còn khoảng trắng nào ở cuối bên phải của chuỗi, hãy dùng phương thức `rstrip()`.

<!-- pdf-page: 60 | printed: 27 -->

```python
❶ >>> favorite_language = 'python '
❷ >>> favorite_language
  'python '
❸ >>> favorite_language.rstrip()
  'python'
❹ >>> favorite_language
  'python '
```

Giá trị được lưu trong `favorite_language` tại ❶ chứa khoảng trắng thừa ở cuối chuỗi. Khi bạn yêu cầu Python hiển thị giá trị này trong một phiên terminal, bạn có thể thấy dấu cách ở cuối giá trị ❷. Khi phương thức `rstrip()` tác động lên biến `favorite_language` tại ❸, dấu cách thừa này bị loại bỏ. Tuy nhiên, nó chỉ bị loại bỏ tạm thời. Nếu yêu cầu xem lại giá trị của `favorite_language`, bạn sẽ thấy chuỗi vẫn giống như lúc được nhập vào, kể cả khoảng trắng thừa ❹.

Để loại bỏ khoảng trắng khỏi chuỗi một cách vĩnh viễn, bạn phải lưu giá trị đã được loại bỏ khoảng trắng trở lại vào biến:

```python
  >>> favorite_language = 'python '
❶ >>> favorite_language = favorite_language.rstrip()
  >>> favorite_language
  'python'
```

Để loại bỏ khoảng trắng khỏi chuỗi, bạn loại bỏ khoảng trắng ở phía bên phải của chuỗi rồi lưu giá trị đó trở lại vào biến ban đầu, như tại ❶. Việc thay đổi giá trị của một biến rồi lưu giá trị mới trở lại vào chính biến đó được thực hiện rất thường xuyên trong lập trình. Đây là cách giá trị của một biến có thể thay đổi trong khi chương trình được thực thi hoặc để phản hồi đầu vào của người dùng.

Bạn cũng có thể loại bỏ khoảng trắng ở phía bên trái của chuỗi bằng phương thức `lstrip()`, hoặc loại bỏ khoảng trắng ở cả hai phía cùng lúc bằng `strip()`:

```python
❶ >>> favorite_language = ' python '
❷ >>> favorite_language.rstrip()
  ' python'
❸ >>> favorite_language.lstrip()
  'python '
❹ >>> favorite_language.strip()
  'python'
```

Trong ví dụ này, chúng ta bắt đầu với một giá trị có khoảng trắng ở đầu và cuối ❶. Sau đó, chúng ta loại bỏ dấu cách thừa ở phía bên phải tại ❷, ở phía bên trái tại ❸, và ở cả hai phía tại ❹. Thử nghiệm với các hàm loại bỏ khoảng trắng này có thể giúp bạn quen với việc thao tác chuỗi. Trong thực tế, các hàm loại bỏ khoảng trắng này thường được dùng nhất để làm sạch đầu vào của người dùng trước khi lưu nó vào chương trình.

<!-- pdf-page: 61 | printed: 28 -->

### Tránh lỗi cú pháp với chuỗi

Một loại lỗi mà bạn có thể gặp khá thường xuyên là lỗi cú pháp. *Lỗi cú pháp* (syntax error) xảy ra khi Python không nhận ra một phần chương trình của bạn là mã Python hợp lệ. Ví dụ, nếu bạn dùng dấu lược (apostrophe) bên trong cặp dấu nháy đơn, bạn sẽ gây ra lỗi. Điều này xảy ra vì Python hiểu mọi thứ nằm giữa dấu nháy đơn đầu tiên và dấu lược là một chuỗi. Sau đó, nó cố hiểu phần văn bản còn lại như mã Python, và điều đó gây ra lỗi.

Dưới đây là cách dùng dấu nháy đơn và dấu nháy kép đúng cách. Lưu chương trình này với tên *apostrophe.py* rồi chạy nó:

**apostrophe.py**

```python
message = "One of Python's strengths is its diverse community."
print(message)
```

Dấu lược xuất hiện bên trong một cặp dấu nháy kép, nên trình thông dịch Python đọc chuỗi một cách chính xác mà không gặp trở ngại gì:

```text
One of Python's strengths is its diverse community.
```

Tuy nhiên, nếu bạn dùng dấu nháy đơn, Python không thể xác định chuỗi nên kết thúc ở đâu:

```python
message = 'One of Python's strengths is its diverse community.'
print(message)
```

Bạn sẽ thấy đầu ra sau:

```python
    File "apostrophe.py", line 1
      message = 'One of Python's strengths is its diverse community.'
❶                             ^
  SyntaxError: invalid syntax
```

Trong đầu ra, bạn có thể thấy lỗi xảy ra tại ❶, ngay sau dấu nháy đơn thứ hai. *Lỗi cú pháp* này cho biết trình thông dịch không nhận ra một phần nào đó trong mã là mã Python hợp lệ. Lỗi có thể đến từ nhiều nguồn khác nhau, và tôi sẽ chỉ ra một số lỗi phổ biến khi chúng xuất hiện. Có thể bạn sẽ gặp lỗi cú pháp thường xuyên trong lúc học viết mã Python đúng. Lỗi cú pháp cũng là loại lỗi kém cụ thể nhất, nên việc xác định và sửa chúng có thể khó khăn và gây bực bội. Nếu bạn bị mắc kẹt với một lỗi đặc biệt cứng đầu, hãy xem các gợi ý trong Phụ lục C.

> **Lưu ý** Tính năng tô sáng cú pháp của trình soạn thảo sẽ giúp bạn nhanh chóng phát hiện một số lỗi cú pháp ngay khi viết chương trình. Nếu bạn thấy mã Python được tô sáng như thể nó là tiếng Anh, hoặc tiếng Anh được tô sáng như thể nó là mã Python, thì có lẽ ở đâu đó trong file của bạn có một dấu nháy không khớp.

<!-- pdf-page: 62 | printed: 29 -->

### In trong Python 2

Câu lệnh `print` có cú pháp hơi khác trong Python 2:

```python
>>> python2.7
>>> print "Hello Python 2.7 world!"
Hello Python 2.7 world!
```

Trong Python 2, cụm từ bạn muốn in không cần đặt trong dấu ngoặc đơn. Về mặt kỹ thuật, `print` là một hàm trong Python 3, đó là lý do nó cần dấu ngoặc đơn. Một số câu lệnh `print` trong Python 2 có dùng dấu ngoặc đơn, nhưng hành vi có thể hơi khác so với những gì bạn thấy trong Python 3. Nói chung, khi đọc mã viết bằng Python 2, hãy chuẩn bị tinh thần thấy một số câu lệnh `print` có dấu ngoặc đơn và một số thì không.

<!-- box -->

**Tự mình thực hành**

Lưu mỗi bài tập dưới đây thành một file riêng với tên kiểu như *name_cases.py*. Nếu bị mắc kẹt, hãy nghỉ ngơi một chút hoặc xem các gợi ý trong Phụ lục C.

**2-3. Thông điệp cá nhân:** Lưu tên một người vào một biến và in ra một thông điệp gửi tới người đó. Thông điệp nên đơn giản, chẳng hạn như “Hello Eric, would you like to learn some Python today?”

**2-4. Chữ hoa, chữ thường trong tên:** Lưu tên một người vào một biến, rồi in tên người đó ở dạng chữ thường, chữ hoa và viết hoa chữ cái đầu mỗi từ.

**2-5. Câu nói nổi tiếng:** Tìm một câu nói của một người nổi tiếng mà bạn ngưỡng mộ. In câu nói đó cùng tên tác giả. Đầu ra của bạn nên trông giống như sau, kể cả dấu ngoặc kép:

*Albert Einstein once said, “A person who never made a*

*mistake never tried anything new.”*

**2-6. Câu nói nổi tiếng 2:** Làm lại Bài tập 2-5, nhưng lần này lưu tên người nổi tiếng vào một biến có tên `famous_person`. Sau đó tạo thông điệp và lưu nó vào một biến mới có tên `message`. In thông điệp của bạn ra.

**2-7. Loại bỏ khoảng trắng trong tên:** Lưu tên một người, kèm theo một số ký tự khoảng trắng ở đầu và cuối tên. Hãy đảm bảo bạn dùng mỗi tổ hợp ký tự `"\t"` và `"\n"` ít nhất một lần.

In tên đó một lần để khoảng trắng xung quanh tên được hiển thị. Sau đó in tên bằng cách dùng lần lượt từng hàm trong ba hàm loại bỏ khoảng trắng: `lstrip()`, `rstrip()` và `strip()`.

<!-- /box -->

<!-- pdf-page: 63 | printed: 30 -->

## Số

Số được dùng khá thường xuyên trong lập trình để lưu điểm số trong trò chơi, biểu diễn dữ liệu trong trực quan hóa, lưu thông tin trong ứng dụng web, v.v. Python xử lý số theo nhiều cách khác nhau, tùy vào cách chúng được sử dụng. Trước hết, hãy xem Python quản lý số nguyên như thế nào, vì đây là loại số đơn giản nhất để làm việc.

### Số nguyên

Trong Python, bạn có thể cộng (`+`), trừ (`-`), nhân (`*`) và chia (`/`) các số nguyên.

```python
>>> 2 + 3
5
>>> 3 - 2
1
>>> 2 * 3
6
>>> 3 / 2
1.5
```

Trong một phiên terminal, Python đơn giản trả về kết quả của phép toán. Python dùng hai dấu nhân để biểu diễn phép lũy thừa:

```python
>>> 3 ** 2
9
>>> 3 ** 3
27
>>> 10 ** 6
1000000
```

Python cũng hỗ trợ thứ tự thực hiện phép toán, nên bạn có thể dùng nhiều phép toán trong một biểu thức. Bạn cũng có thể dùng dấu ngoặc đơn để thay đổi thứ tự thực hiện, để Python tính biểu thức theo thứ tự bạn chỉ định. Ví dụ:

```python
>>> 2 + 3*4
14
>>> (2 + 3) * 4
20
```

Khoảng cách trong các ví dụ này không ảnh hưởng gì đến cách Python tính biểu thức; nó chỉ giúp bạn nhanh chóng nhận ra những phép toán được ưu tiên khi đọc mã.

### Số thực

Python gọi mọi số có dấu chấm thập phân là *float* (số thực dấu phẩy động). Thuật ngữ này được dùng trong hầu hết các ngôn ngữ lập trình, và nó ám chỉ việc dấu chấm thập phân có thể xuất hiện ở bất kỳ vị trí nào trong một số. Mọi ngôn ngữ lập trình đều phải được thiết kế cẩn thận để quản lý đúng các số thập phân, sao cho chúng hoạt động hợp lý bất kể dấu chấm thập phân nằm ở đâu.

<!-- pdf-page: 64 | printed: 31 -->

Trong hầu hết trường hợp, bạn có thể dùng số thập phân mà không cần lo về cách chúng hoạt động. Chỉ cần nhập những số bạn muốn dùng, và rất có thể Python sẽ làm đúng như bạn mong đợi:

```python
>>> 0.1 + 0.1
0.2
>>> 0.2 + 0.2
0.4
>>> 2 * 0.1
0.2
>>> 2 * 0.2
0.4
```

Nhưng hãy lưu ý rằng đôi khi bạn có thể nhận được một kết quả có số chữ số thập phân bất thường:

```python
>>> 0.2 + 0.1
0.30000000000000004
>>> 3 * 0.1
0.30000000000000004
```

Điều này xảy ra ở mọi ngôn ngữ và không có gì đáng lo. Python cố tìm cách biểu diễn kết quả chính xác nhất có thể, mà đôi khi điều này khá khó do cách máy tính phải biểu diễn số ở bên trong. Tạm thời cứ bỏ qua các chữ số thập phân thừa; bạn sẽ học cách xử lý chúng khi cần trong các dự án ở Phần II.

### Tránh lỗi kiểu dữ liệu bằng hàm str()

Bạn sẽ thường muốn dùng giá trị của một biến bên trong một thông điệp. Ví dụ, giả sử bạn muốn chúc mừng sinh nhật ai đó. Có thể bạn sẽ viết đoạn mã như sau:

**birthday.py**

```python
age = 23
message = "Happy " + age + "rd Birthday!"

print(message)
```

Có thể bạn mong đợi đoạn mã này in ra lời chúc sinh nhật đơn giản `Happy 23rd birthday!` Nhưng nếu chạy đoạn mã này, bạn sẽ thấy nó gây ra lỗi:

```python
  Traceback (most recent call last):
    File "birthday.py", line 2, in <module>
      message = "Happy " + age + "rd Birthday!"
❶ TypeError: Can't convert 'int' object to str implicitly
```

Đây là một *lỗi kiểu dữ liệu* (type error). Nó có nghĩa là Python không thể nhận ra loại thông tin bạn đang dùng. Trong ví dụ này, tại ❶ Python thấy bạn đang dùng một biến có giá trị số nguyên (`int`), nhưng nó không chắc nên hiểu giá trị đó như thế nào. Python biết rằng biến này có thể biểu diễn giá trị số 23 hoặc hai ký tự *2* và *3*. Khi dùng số nguyên bên trong chuỗi như thế này, bạn cần chỉ rõ rằng bạn muốn Python dùng số nguyên đó như một chuỗi ký tự. Bạn có thể làm điều này bằng cách bọc biến trong hàm `str()`, hàm yêu cầu Python biểu diễn các giá trị không phải chuỗi dưới dạng chuỗi:

<!-- pdf-page: 65 | printed: 32 -->

```python
age = 23
message = "Happy " + str(age) + "rd Birthday!"

print(message)
```

Giờ đây Python biết rằng bạn muốn chuyển giá trị số 23 thành chuỗi và hiển thị các ký tự `2` và `3` như một phần của thông điệp chúc mừng sinh nhật. Bây giờ bạn nhận được đúng thông điệp mong đợi mà không gặp lỗi nào:

```text
Happy 23rd Birthday!
```

Phần lớn thời gian, làm việc với số trong Python khá đơn giản. Nếu nhận được kết quả bất ngờ, hãy kiểm tra xem Python có đang hiểu các số của bạn đúng như bạn muốn hay không — là giá trị số hay giá trị chuỗi.

### Số nguyên trong Python 2

Python 2 trả về kết quả hơi khác khi bạn chia hai số nguyên:

```python
>>> python2.7
>>> 3 / 2
1
```

Thay vì `1.5`, Python trả về `1`. Phép chia số nguyên trong Python 2 cho ra một số nguyên với phần dư bị cắt bỏ. Lưu ý rằng kết quả không phải là số nguyên được làm tròn; phần dư đơn giản là bị bỏ đi.

Để tránh hành vi này trong Python 2, hãy đảm bảo ít nhất một trong hai số là số thực. Khi đó, kết quả cũng sẽ là số thực:

```python
>>> 3 / 2
1
>>> 3.0 / 2
1.5
>>> 3 / 2.0
1.5
>>> 3.0 / 2.0
1.5
```

Cách chia này là nguồn gây nhầm lẫn phổ biến khi những người quen dùng Python 3 chuyển sang dùng Python 2, hoặc ngược lại. Nếu bạn dùng hoặc viết mã trộn lẫn số nguyên và số thực, hãy cẩn thận với những hành vi bất thường.

<!-- pdf-page: 66 | printed: 33 -->

<!-- box -->

**Tự mình thực hành**

**2-8. Số tám:** Viết các phép cộng, trừ, nhân và chia sao cho mỗi phép đều cho kết quả là số 8. Nhớ đặt các phép toán bên trong câu lệnh `print` để xem kết quả. Bạn nên tạo bốn dòng trông giống như sau:

```python
print(5 + 3)
```

Đầu ra của bạn chỉ gồm bốn dòng, mỗi dòng có số 8 xuất hiện một lần.

**2-9. Số yêu thích:** Lưu số yêu thích của bạn vào một biến. Sau đó, dùng biến đó để tạo một thông điệp cho biết số yêu thích của bạn. In thông điệp đó ra.

<!-- /box -->

## Chú thích

Chú thích (comment) là một tính năng cực kỳ hữu ích trong hầu hết các ngôn ngữ lập trình. Mọi thứ bạn viết trong chương trình cho đến giờ đều là mã Python. Khi chương trình ngày càng dài và phức tạp, bạn nên thêm các ghi chú vào chương trình để mô tả cách tiếp cận tổng thể của bạn đối với vấn đề đang giải quyết. *Chú thích* cho phép bạn viết ghi chú bằng tiếng Anh bên trong chương trình.

### Viết chú thích như thế nào?

Trong Python, dấu thăng (`#`) đánh dấu một chú thích. Mọi thứ đứng sau dấu thăng trong mã đều bị trình thông dịch Python bỏ qua. Ví dụ:

**comment.py**

```python
# Say hello to everyone.
print("Hello Python people!")
```

Python bỏ qua dòng đầu tiên và thực thi dòng thứ hai.

```text
Hello Python people!
```

### Nên viết chú thích như thế nào?

Lý do chính để viết chú thích là giải thích đoạn mã của bạn có nhiệm vụ gì và bạn làm cho nó hoạt động như thế nào. Khi đang giữa chừng một dự án, bạn hiểu rõ mọi phần khớp với nhau ra sao. Nhưng khi quay lại dự án sau một thời gian, nhiều khả năng bạn sẽ quên một số chi tiết. Bạn luôn có thể nghiên cứu mã một lúc để hiểu các đoạn mã được dự định hoạt động thế nào, nhưng viết chú thích tốt có thể giúp bạn tiết kiệm thời gian nhờ tóm tắt cách tiếp cận tổng thể bằng tiếng Anh rõ ràng.

<!-- pdf-page: 67 | printed: 34 -->

Nếu bạn muốn trở thành lập trình viên chuyên nghiệp hoặc cộng tác với các lập trình viên khác, bạn nên viết những chú thích có ý nghĩa. Ngày nay, hầu hết phần mềm đều được viết theo hình thức cộng tác, dù là bởi một nhóm nhân viên trong một công ty hay một nhóm người cùng làm việc trong một dự án mã nguồn mở. Những lập trình viên lành nghề luôn mong đợi thấy chú thích trong mã, vì vậy tốt nhất là bạn nên bắt đầu thêm chú thích mô tả vào chương trình ngay từ bây giờ. Viết chú thích rõ ràng, súc tích trong mã là một trong những thói quen có lợi nhất mà bạn có thể hình thành khi mới làm lập trình viên.

Khi cân nhắc có nên viết chú thích hay không, hãy tự hỏi liệu bạn có phải cân nhắc nhiều cách tiếp cận trước khi tìm ra một cách hợp lý để làm cho một thứ hoạt động hay không; nếu có, hãy viết chú thích về giải pháp của bạn. Xóa bớt các chú thích thừa về sau dễ hơn nhiều so với việc quay lại viết chú thích cho một chương trình có quá ít chú thích. Từ giờ trở đi, tôi sẽ dùng chú thích trong các ví dụ xuyên suốt cuốn sách để giúp giải thích các đoạn mã.

<!-- box -->

**Tự mình thực hành**

**2-10. Thêm chú thích:** Chọn hai chương trình bạn đã viết và thêm ít nhất một chú thích vào mỗi chương trình. Nếu bạn chưa có gì cụ thể để viết vì chương trình còn quá đơn giản, chỉ cần thêm tên của bạn và ngày hiện tại ở đầu mỗi file chương trình. Sau đó viết một câu mô tả chương trình làm gì.

<!-- /box -->

## Triết lý Zen của Python

Trong một thời gian dài, ngôn ngữ lập trình Perl là trụ cột của Internet. Hầu hết các trang web tương tác thời kỳ đầu đều chạy bằng các script Perl. Phương châm của cộng đồng Perl lúc đó là: “Có nhiều hơn một cách để làm một việc.” Người ta ưa thích tư duy này một thời gian, vì sự linh hoạt được xây dựng sẵn trong ngôn ngữ cho phép giải quyết hầu hết các vấn đề theo nhiều cách khác nhau. Cách tiếp cận này chấp nhận được khi làm các dự án của riêng mình, nhưng rốt cuộc người ta nhận ra rằng việc đề cao sự linh hoạt khiến các dự án lớn trở nên khó bảo trì trong thời gian dài. Việc xem lại mã và cố hiểu người khác đã nghĩ gì khi giải quyết một vấn đề phức tạp trở nên khó khăn, tẻ nhạt và tốn thời gian.

Những lập trình viên Python giàu kinh nghiệm sẽ khuyên bạn tránh sự phức tạp và hướng tới sự đơn giản bất cứ khi nào có thể. Triết lý của cộng đồng Python được đúc kết trong “The Zen of Python” của Tim Peters. Bạn có thể xem bộ nguyên tắc ngắn gọn này về cách viết mã Python tốt bằng cách nhập `import this` vào trình thông dịch. Tôi sẽ không chép lại toàn bộ “Zen of Python” ở đây, nhưng sẽ chia sẻ vài dòng để giúp bạn hiểu vì sao chúng quan trọng đối với bạn khi mới bắt đầu học lập trình Python.

<!-- pdf-page: 68 | printed: 35 -->

```python
>>> import this
The Zen of Python, by Tim Peters

Beautiful is better than ugly.
```

Các lập trình viên Python tâm đắc với quan niệm rằng mã có thể đẹp và thanh lịch. Trong lập trình, người ta giải quyết vấn đề. Lập trình viên luôn trân trọng những giải pháp được thiết kế tốt, hiệu quả, thậm chí đẹp đẽ. Khi bạn hiểu thêm về Python và dùng nó để viết nhiều mã hơn, một ngày nào đó có thể sẽ có người nhìn qua vai bạn và thốt lên: “Ồ, đoạn mã đẹp quá!”

```text
Simple is better than complex.
```

Nếu bạn phải lựa chọn giữa một giải pháp đơn giản và một giải pháp phức tạp, và cả hai đều chạy được, hãy dùng giải pháp đơn giản. Mã của bạn sẽ dễ bảo trì hơn, và về sau bạn cũng như người khác sẽ dễ dàng phát triển tiếp trên đoạn mã đó hơn.

```text
Complex is better than complicated.
```

Cuộc sống thực vốn lộn xộn, và đôi khi không thể có một giải pháp đơn giản cho một vấn đề. Trong trường hợp đó, hãy dùng giải pháp đơn giản nhất mà vẫn chạy được.

```text
Readability counts.
```

Ngay cả khi mã của bạn phức tạp, hãy cố làm cho nó dễ đọc. Khi làm một dự án có phần mã phức tạp, hãy tập trung viết những chú thích giàu thông tin cho phần mã đó.

```text
There should be one-- and preferably only one --obvious way to do it.
```

Nếu hai lập trình viên Python được yêu cầu giải quyết cùng một vấn đề, họ nên đưa ra những giải pháp khá tương đồng. Điều này không có nghĩa là lập trình không có chỗ cho sự sáng tạo. Hoàn toàn ngược lại! Nhưng phần lớn công việc lập trình là áp dụng những cách tiếp cận nhỏ, phổ biến cho các tình huống đơn giản bên trong một dự án lớn hơn, sáng tạo hơn. Những phần cốt lõi trong chương trình của bạn nên dễ hiểu đối với các lập trình viên Python khác.

```text
Now is better than never.
```

Bạn có thể dành cả phần đời còn lại để học mọi ngóc ngách của Python và của lập trình nói chung, nhưng như thế bạn sẽ chẳng bao giờ hoàn thành được dự án nào. Đừng cố viết mã hoàn hảo; hãy viết mã chạy được, rồi quyết định nên cải thiện mã cho dự án đó hay chuyển sang việc mới.

<!-- pdf-page: 69 | printed: 36 -->

Khi bạn tiếp tục sang chương tiếp theo và bắt đầu đi sâu vào những chủ đề phức tạp hơn, hãy cố ghi nhớ triết lý đơn giản và rõ ràng này. Những lập trình viên giàu kinh nghiệm sẽ đánh giá cao mã của bạn hơn và sẵn lòng góp ý cũng như cộng tác với bạn trong các dự án thú vị.

<!-- box -->

**Tự mình thực hành**

**2-11. Zen of Python:** Nhập `import this` vào một phiên terminal Python và đọc lướt qua các nguyên tắc còn lại.

<!-- /box -->

## Tổng kết

Trong chương này, bạn đã học cách làm việc với biến. Bạn đã học cách đặt tên biến mang tính mô tả và cách xử lý lỗi tên cũng như lỗi cú pháp khi chúng xuất hiện. Bạn đã biết chuỗi là gì và cách hiển thị chuỗi ở dạng chữ thường, chữ hoa và viết hoa chữ cái đầu mỗi từ. Bạn đã bắt đầu dùng khoảng trắng để sắp xếp đầu ra gọn gàng, và đã học cách loại bỏ khoảng trắng không cần thiết khỏi các phần khác nhau của chuỗi. Bạn đã bắt đầu làm việc với số nguyên và số thực, và đã đọc về một số hành vi bất ngờ cần lưu ý khi làm việc với dữ liệu số. Bạn cũng đã học cách viết chú thích giải thích để mã của bạn dễ đọc hơn đối với chính bạn và người khác. Cuối cùng, bạn đã đọc về triết lý giữ cho mã đơn giản nhất có thể, bất cứ khi nào có thể.

Trong Chương 3, bạn sẽ học cách lưu trữ các tập hợp thông tin trong những biến được gọi là *list*. Bạn sẽ học cách duyệt qua một list và thao tác với bất kỳ thông tin nào trong list đó.

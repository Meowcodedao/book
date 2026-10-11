<!-- source: pythoncrashcourse.pdf | unit: chapter-10 | pdf pages 222-247 | printed 189-214 -->

# Chương 10: File và ngoại lệ

<!-- pdf-page: 222 | printed: 189 -->

Giờ đây khi đã thành thạo những kỹ năng cơ bản cần thiết để viết các chương trình ngăn nắp, dễ sử dụng, đã đến lúc nghĩ đến việc làm cho chương trình của bạn thiết thực và dễ dùng hơn nữa. Trong chương này, bạn sẽ học cách làm việc với file để chương trình có thể nhanh chóng phân tích lượng lớn dữ liệu.

Bạn sẽ học cách xử lý lỗi để chương trình không bị dừng đột ngột khi gặp những tình huống bất ngờ. Bạn sẽ tìm hiểu về *ngoại lệ* (exception), những đối tượng đặc biệt mà Python tạo ra để quản lý các lỗi phát sinh trong khi chương trình đang chạy. Bạn cũng sẽ tìm hiểu về module `json`, cho phép bạn lưu dữ liệu của người dùng để nó không bị mất khi chương trình ngừng chạy.

Học cách làm việc với file và lưu dữ liệu sẽ giúp chương trình của bạn dễ sử dụng hơn với mọi người. Người dùng sẽ có thể chọn nhập dữ liệu gì và nhập khi nào. Mọi người có thể chạy chương trình của bạn, làm một số việc, rồi đóng chương trình và sau đó tiếp tục từ chỗ đã dừng. Học cách xử lý ngoại lệ sẽ giúp bạn xử lý những tình huống file không tồn tại, cũng như những vấn đề khác có thể khiến chương trình bị dừng đột ngột. Điều này giúp chương trình của bạn vững vàng hơn khi gặp dữ liệu xấu, dù dữ liệu đó đến từ những nhầm lẫn vô tình hay từ những nỗ lực cố ý phá hỏng chương trình. Với những kỹ năng học được trong chương này, bạn sẽ làm cho chương trình của mình hữu dụng hơn, dễ dùng hơn và ổn định hơn.

<!-- pdf-page: 223 | printed: 190 -->

## Đọc từ file

Có một lượng dữ liệu khổng lồ nằm trong các file văn bản. File văn bản có thể chứa dữ liệu thời tiết, dữ liệu giao thông, dữ liệu kinh tế – xã hội, tác phẩm văn học, và nhiều thứ khác. Đọc từ file đặc biệt hữu ích trong các ứng dụng phân tích dữ liệu, nhưng cũng áp dụng được cho mọi tình huống bạn muốn phân tích hoặc sửa đổi thông tin được lưu trong file. Ví dụ, bạn có thể viết một chương trình đọc nội dung của một file văn bản và ghi lại file đó với định dạng cho phép trình duyệt hiển thị nó.

Khi muốn làm việc với thông tin trong một file văn bản, bước đầu tiên là đọc file vào bộ nhớ. Bạn có thể đọc toàn bộ nội dung của file, hoặc duyệt qua file từng dòng một.

### Đọc toàn bộ file

Để bắt đầu, chúng ta cần một file có vài dòng văn bản. Hãy bắt đầu với một file chứa số *pi* đến 30 chữ số thập phân, mỗi dòng 10 chữ số thập phân:

**pi_digits.txt**

```text
3.1415926535
  8979323846
  2643383279
```

Để tự thử các ví dụ sau, bạn có thể nhập các dòng này vào trình soạn thảo và lưu file với tên *pi_digits.txt*, hoặc tải file từ tài nguyên của sách tại *https://www.nostarch.com/pythoncrashcourse/*. Hãy lưu file vào cùng thư mục nơi bạn sẽ lưu các chương trình của chương này.

Đây là một chương trình mở file này, đọc nó, và in nội dung của file ra màn hình:

**file_reader.py**

```python
with open('pi_digits.txt') as file_object:
    contents = file_object.read()
    print(contents)
```

Dòng đầu tiên của chương trình này có rất nhiều điều diễn ra. Hãy bắt đầu bằng việc xem xét hàm `open()`. Để làm bất cứ việc gì với một file, kể cả chỉ in nội dung của nó, trước tiên bạn cần *mở* (open) file để truy cập nó. Hàm `open()` cần một đối số: tên của file bạn muốn mở. Python tìm file này trong thư mục nơi lưu chương trình đang được thực thi. Trong ví dụ này, *file_reader.py* đang chạy, nên Python tìm *pi_digits.txt* trong thư mục nơi lưu *file_reader.py*. Hàm `open()` trả về một đối tượng biểu diễn file. Ở đây, `open('pi_digits.txt')` trả về một đối tượng biểu diễn *pi_digits.txt*. Python lưu đối tượng này vào `file_object`, đối tượng mà chúng ta sẽ làm việc cùng ở phần sau của chương trình.

Từ khóa `with` đóng file khi không còn cần truy cập nó nữa. Hãy để ý cách chúng ta gọi `open()` trong chương trình này nhưng không gọi `close()`. Bạn có thể mở và đóng file bằng cách gọi `open()` và `close()`, nhưng nếu một lỗi trong chương trình khiến câu lệnh `close()` không được thực thi, file có thể sẽ không bao giờ được đóng. Điều này có vẻ nhỏ nhặt, nhưng những file không được đóng đúng cách có thể khiến dữ liệu bị mất hoặc bị hỏng. Và nếu gọi `close()` quá sớm trong chương trình, bạn sẽ thấy mình đang cố làm việc với một file *đã đóng* (một file bạn không thể truy cập), dẫn đến thêm nhiều lỗi khác. Không phải lúc nào cũng dễ biết chính xác khi nào nên đóng file, nhưng với cấu trúc trình bày ở đây, Python sẽ tự xác định điều đó giúp bạn. Tất cả những gì bạn phải làm là mở file và làm việc với nó theo ý muốn, tin tưởng rằng Python sẽ tự động đóng nó vào đúng lúc.

<!-- pdf-page: 224 | printed: 191 -->

Khi đã có một đối tượng file biểu diễn *pi_digits.txt*, chúng ta dùng phương thức `read()` ở dòng thứ hai của chương trình để đọc toàn bộ nội dung của file và lưu nó thành một chuỗi dài trong `contents`. Khi in giá trị của `contents`, ta nhận lại toàn bộ file văn bản:

```text
3.1415926535
  8979323846
  2643383279
```

Điểm khác biệt duy nhất giữa đầu ra này và file gốc là dòng trống thừa ở cuối đầu ra. Dòng trống xuất hiện vì `read()` trả về một chuỗi rỗng khi đọc đến cuối file; chuỗi rỗng này hiển thị thành một dòng trống. Nếu muốn bỏ dòng trống thừa, bạn có thể dùng `rstrip()` trong câu lệnh `print`:

```python
with open('pi_digits.txt') as file_object:
    contents = file_object.read()
    print(contents.rstrip())
```

Hãy nhớ lại rằng phương thức `rstrip()` của Python loại bỏ mọi ký tự khoảng trắng ở phía bên phải của một chuỗi. Giờ đầu ra khớp chính xác với nội dung của file gốc:

```text
3.1415926535
  8979323846
  2643383279
```

### Đường dẫn file

Khi bạn truyền một tên file đơn giản như *pi_digits.txt* cho hàm `open()`, Python tìm trong thư mục nơi lưu file đang được thực thi (tức là file chương trình *.py* của bạn).

Đôi khi, tùy thuộc vào cách bạn tổ chức công việc, file bạn muốn mở sẽ không nằm cùng thư mục với file chương trình. Ví dụ, bạn có thể lưu các file chương trình trong một thư mục có tên *python_work*; bên trong *python_work*, bạn có thể có một thư mục khác có tên *text_files* để phân biệt các file chương trình với các file văn bản mà chúng xử lý. Dù *text_files* nằm trong *python_work*, chỉ truyền cho `open()` tên của một file trong *text_files* sẽ không hoạt động, vì Python sẽ chỉ tìm trong *python_work* rồi dừng lại ở đó; nó sẽ không tiếp tục tìm trong *text_files.* Để Python mở được file từ một thư mục khác với thư mục lưu file chương trình, bạn cần cung cấp một *đường dẫn file* (file path), cho Python biết phải tìm ở một vị trí cụ thể trên hệ thống của bạn.

<!-- pdf-page: 225 | printed: 192 -->

Vì *text_files* nằm bên trong *python_work*, bạn có thể dùng đường dẫn file tương đối để mở một file từ *text_files.* *Đường dẫn file tương đối* (relative file path) yêu cầu Python tìm một vị trí cho trước, tính tương đối so với thư mục nơi lưu file chương trình đang chạy. Trên Linux và OS X, bạn sẽ viết:

```text
with open('text_files/filename.txt') as file_object:
```

Dòng này yêu cầu Python tìm file *.txt* mong muốn trong thư mục *text_files* và giả định rằng *text_files* nằm bên trong *python_work* (đúng là như vậy). Trên các hệ thống Windows, bạn dùng dấu gạch chéo ngược (`\`) thay vì dấu gạch chéo xuôi (`/`) trong đường dẫn file:

```text
with open('text_files\filename.txt') as file_object:
```

Bạn cũng có thể cho Python biết chính xác file nằm ở đâu trên máy tính, bất kể chương trình đang được thực thi được lưu ở đâu. Đây được gọi là *đường dẫn file tuyệt đối* (absolute file path). Bạn dùng đường dẫn tuyệt đối nếu đường dẫn tương đối không hoạt động. Chẳng hạn, nếu bạn đặt *text_files* trong một thư mục khác không phải *python_work* — giả sử một thư mục có tên *other_files* — thì chỉ truyền cho `open()` đường dẫn `'text_files/filename.txt'` sẽ không hoạt động, vì Python sẽ chỉ tìm vị trí đó bên trong *python_work*. Bạn sẽ cần viết ra một đường dẫn đầy đủ để chỉ rõ nơi bạn muốn Python tìm.

Đường dẫn tuyệt đối thường dài hơn đường dẫn tương đối, nên sẽ có ích nếu lưu chúng vào một biến rồi truyền biến đó cho `open()`. Trên Linux và OS X, đường dẫn tuyệt đối trông như sau:

```python
file_path = '/home/ehmatthes/other_files/text_files/filename.txt'
with open(file_path) as file_object:
```

còn trên Windows, chúng trông như sau:

```python
file_path = 'C:\Users\ehmatthes\other_files\text_files\filename.txt'
with open(file_path) as file_object:
```

Dùng đường dẫn tuyệt đối, bạn có thể đọc file từ bất kỳ vị trí nào trên hệ thống. Hiện tại, cách dễ nhất là lưu file vào cùng thư mục với các file chương trình, hoặc vào một thư mục như *text_files* bên trong thư mục chứa các file chương trình.

> **Lưu ý** Các hệ thống Windows đôi khi vẫn hiểu đúng dấu gạch chéo xuôi trong đường dẫn file. Nếu bạn đang dùng Windows và không nhận được kết quả như mong đợi, hãy nhớ thử dùng dấu gạch chéo ngược.

<!-- pdf-page: 226 | printed: 193 -->

### Đọc từng dòng

Khi đọc một file, bạn sẽ thường muốn xem xét từng dòng của file. Có thể bạn đang tìm một thông tin nhất định trong file, hoặc muốn sửa đổi văn bản trong file theo cách nào đó. Ví dụ, bạn có thể muốn đọc qua một file dữ liệu thời tiết và làm việc với mọi dòng có chứa từ *sunny* trong phần mô tả thời tiết của ngày hôm đó. Trong một bản tin, bạn có thể tìm mọi dòng có thẻ `<headline>` và viết lại dòng đó với một kiểu định dạng cụ thể.

Bạn có thể dùng vòng lặp `for` trên đối tượng file để lần lượt xem xét từng dòng của file:

**file_reader.py**

```python
❶ filename = 'pi_digits.txt'

❷ with open(filename) as file_object:
❸     for line in file_object:
         print(line)
```

Tại ❶, chúng ta lưu tên của file đang đọc vào biến `filename`. Đây là một quy ước phổ biến khi làm việc với file. Vì biến `filename` không biểu diễn file thực sự — nó chỉ là một chuỗi cho Python biết nơi tìm file — bạn có thể dễ dàng thay `'pi_digits.txt'` bằng tên của một file khác mà bạn muốn làm việc. Sau khi gọi `open()`, một đối tượng biểu diễn file và nội dung của nó được lưu vào biến `file_object` ❷. Một lần nữa, ta dùng cú pháp `with` để Python mở và đóng file đúng cách. Để xem xét nội dung của file, ta duyệt qua từng dòng trong file bằng cách lặp qua đối tượng file ❸.

Khi in từng dòng, chúng ta lại thấy thêm nhiều dòng trống hơn:

```text
3.1415926535

  8979323846

  2643383279
```

Những dòng trống này xuất hiện vì có một ký tự xuống dòng vô hình ở cuối mỗi dòng trong file văn bản. Câu lệnh `print` tự thêm một ký tự xuống dòng mỗi lần ta gọi nó, nên cuối cùng ta có hai ký tự xuống dòng ở cuối mỗi dòng: một từ file và một từ câu lệnh `print`. Dùng `rstrip()` trên mỗi dòng trong câu lệnh `print` sẽ loại bỏ những dòng trống thừa này:

```python
filename = 'pi_digits.txt'

with open(filename) as file_object:
    for line in file_object:
        print(line.rstrip())
```

<!-- pdf-page: 227 | printed: 194 -->

Giờ đầu ra lại khớp với nội dung của file:

```text
3.1415926535
  8979323846
  2643383279
```

### Tạo list các dòng từ file

Khi bạn dùng `with`, đối tượng file do `open()` trả về chỉ có thể dùng bên trong khối `with` chứa nó. Nếu muốn giữ quyền truy cập nội dung của file bên ngoài khối `with`, bạn có thể lưu các dòng của file vào một list bên trong khối, rồi làm việc với list đó. Bạn có thể xử lý ngay một số phần của file và hoãn một số việc xử lý đến phần sau của chương trình.

Ví dụ sau lưu các dòng của *pi_digits.txt* vào một list bên trong khối `with`, rồi in các dòng đó ra bên ngoài khối `with`:

```python
  filename = 'pi_digits.txt'

  with open(filename) as file_object:
❶     lines = file_object.readlines()

❷ for line in lines:
      print(line.rstrip())
```

Tại ❶, phương thức `readlines()` lấy từng dòng trong file và lưu nó vào một list. List này sau đó được lưu vào `lines`, mà ta có thể tiếp tục làm việc cùng sau khi khối `with` kết thúc. Tại ❷, ta dùng một vòng lặp `for` đơn giản để in từng dòng trong `lines`. Vì mỗi phần tử trong `lines` tương ứng với từng dòng trong file, đầu ra khớp chính xác với nội dung của file.

### Làm việc với nội dung của file

Sau khi đã đọc một file vào bộ nhớ, bạn có thể làm bất cứ điều gì bạn muốn với dữ liệu đó, vậy hãy cùng khám phá nhanh các chữ số của *pi*. Trước tiên, chúng ta sẽ thử tạo một chuỗi duy nhất chứa tất cả các chữ số trong file mà không có khoảng trắng nào:

**pi_string.py**

```python
  filename = 'pi_digits.txt'

  with open(filename) as file_object:
      lines = file_object.readlines()

❶ pi_string = ''
❷ for line in lines:
      pi_string += line.rstrip()

❸ print(pi_string)
  print(len(pi_string))
```

Chúng ta bắt đầu bằng việc mở file và lưu từng dòng chữ số vào một list, giống như trong ví dụ trước. Tại ❶, ta tạo một biến, `pi_string`, để chứa các chữ số của *pi*. Sau đó, ta tạo một vòng lặp cộng từng dòng chữ số vào `pi_string` và loại bỏ ký tự xuống dòng khỏi mỗi dòng ❷. Tại ❸, ta in chuỗi này ra và cho biết chuỗi dài bao nhiêu:

<!-- pdf-page: 228 | printed: 195 -->

```text
3.1415926535  8979323846  2643383279
36
```

Biến `pi_string` chứa khoảng trắng vốn nằm ở phía bên trái các chữ số trên mỗi dòng, nhưng ta có thể bỏ nó đi bằng cách dùng `strip()` thay vì `rstrip()`:

```python
filename = 'pi_30_digits.txt'

with open(filename) as file_object:
    lines = file_object.readlines()

pi_string = ''
for line in lines:
    pi_string += line.strip()

print(pi_string)
print(len(pi_string))
```

Giờ chúng ta có một chuỗi chứa *pi* đến 30 chữ số thập phân. Chuỗi dài 32 ký tự vì nó còn bao gồm chữ số 3 đứng đầu và một dấu chấm thập phân:

```text
3.141592653589793238462643383279
32
```

> **Lưu ý** Khi Python đọc từ một file văn bản, nó hiểu mọi văn bản trong file là chuỗi. Nếu bạn đọc vào một con số và muốn làm việc với giá trị đó trong ngữ cảnh số, bạn sẽ phải chuyển nó thành số nguyên bằng hàm `int()` hoặc chuyển thành số thực bằng hàm `float()`.

### File lớn: Một triệu chữ số

Cho đến giờ, chúng ta mới tập trung phân tích một file văn bản chỉ chứa ba dòng, nhưng đoạn mã trong các ví dụ này cũng sẽ hoạt động tốt như vậy với những file lớn hơn nhiều. Nếu bắt đầu với một file văn bản chứa *pi* đến 1.000.000 chữ số thập phân thay vì chỉ 30, ta có thể tạo một chuỗi duy nhất chứa tất cả các chữ số này. Ta hoàn toàn không cần thay đổi chương trình, ngoại trừ việc truyền cho nó một file khác. Ta cũng sẽ chỉ in ra 50 chữ số thập phân đầu tiên, để không phải nhìn một triệu chữ số cuộn qua trong terminal:

**pi_string.py**

```python
filename = 'pi_million_digits.txt'

with open(filename) as file_object:
    lines = file_object.readlines()
pi_string = ''
for line in lines:
    pi_string += line.strip()

print(pi_string[:52] + "...")
print(len(pi_string))
```

<!-- pdf-page: 229 | printed: 196 -->

Đầu ra cho thấy chúng ta quả thực có một chuỗi chứa *pi* đến 1.000.000 chữ số thập phân:

```text
3.14159265358979323846264338327950288419716939937510...
1000002
```

Python không có giới hạn cố hữu nào về lượng dữ liệu bạn có thể làm việc; bạn có thể làm việc với lượng dữ liệu lớn đến mức bộ nhớ của hệ thống có thể xử lý.

> **Lưu ý** Để chạy chương trình này (và nhiều ví dụ tiếp theo), bạn sẽ cần tải các tài nguyên có tại *https://www.nostarch.com/pythoncrashcourse/*.

### Ngày sinh của bạn có nằm trong số Pi không?

Tôi luôn tò mò muốn biết ngày sinh của mình có xuất hiện ở đâu đó trong các chữ số của *pi* hay không. Hãy dùng chương trình vừa viết để xem ngày sinh của một người có xuất hiện ở đâu đó trong một triệu chữ số đầu tiên của *pi* hay không. Chúng ta có thể làm điều này bằng cách biểu diễn mỗi ngày sinh thành một chuỗi chữ số và xem chuỗi đó có xuất hiện ở đâu đó trong `pi_string` không:

```python
  filename = 'pi_million_digits.txt'

  with open(filename) as file_object:
      lines = file_object.readlines()

  pi_string = ''
  for line in lines:
      pi_string += line.rstrip()

❶ birthday = input("Enter your birthday, in the form mmddyy: ")
❷ if birthday in pi_string:
      print("Your birthday appears in the first million digits of pi!")
  else:
      print("Your birthday does not appear in the first million digits of pi.")
```

Tại ❶, chúng ta yêu cầu người dùng nhập ngày sinh, rồi tại ❷, ta kiểm tra xem chuỗi đó có nằm trong `pi_string` không. Hãy thử xem:

```text
Enter your birthdate, in the form mmddyy: 120372
Your birthday appears in the first million digits of pi!
```

Ngày sinh của tôi quả thực xuất hiện trong các chữ số của *pi*! Khi đã đọc từ một file, bạn có thể phân tích nội dung của nó theo hầu như bất kỳ cách nào bạn có thể tưởng tượng ra.

<!-- pdf-page: 230 | printed: 197 -->

<!-- box -->

**Tự mình thực hành**

**10-1. Học Python:** Mở một file trống trong trình soạn thảo văn bản và viết vài dòng tóm tắt những gì bạn đã học về Python cho đến giờ. Bắt đầu mỗi dòng bằng cụm từ *In Python you can...*. Lưu file với tên *learning_python.txt* trong cùng thư mục với các bài tập của chương này. Viết một chương trình đọc file và in những gì bạn đã viết ba lần. In nội dung một lần bằng cách đọc toàn bộ file, một lần bằng cách lặp qua đối tượng file, và một lần bằng cách lưu các dòng vào một list rồi làm việc với chúng bên ngoài khối `with`.

**10-2. Học C:** Bạn có thể dùng phương thức `replace()` để thay thế bất kỳ từ nào trong một chuỗi bằng một từ khác. Đây là một ví dụ nhanh cho thấy cách thay `'dog'` bằng `'cat'` trong một câu:

```python
>>> message = "I really like dogs."
>>> message.replace('dog', 'cat')
'I really like cats.'
```

Đọc từng dòng từ file bạn vừa tạo, *learning_python.txt*, và thay từ *Python* bằng tên một ngôn ngữ khác, chẳng hạn *C*. In từng dòng đã sửa đổi ra màn hình.

<!-- /box -->

## Ghi vào file

Một trong những cách đơn giản nhất để lưu dữ liệu là ghi nó vào một file. Khi bạn ghi văn bản vào một file, đầu ra vẫn còn đó sau khi bạn đóng terminal chứa đầu ra của chương trình. Bạn có thể xem xét đầu ra sau khi chương trình chạy xong, và cũng có thể chia sẻ các file đầu ra với người khác. Bạn cũng có thể viết những chương trình đọc lại văn bản vào bộ nhớ và làm việc với nó sau này.

### Ghi vào một file trống

Để ghi văn bản vào một file, bạn cần gọi `open()` với một đối số thứ hai cho Python biết bạn muốn ghi vào file. Để xem cách này hoạt động ra sao, hãy viết một thông điệp đơn giản và lưu nó vào một file thay vì in nó ra màn hình:

**write_message.py**

```python
  filename = 'programming.txt'
❶ with open(filename, 'w') as file_object:
❷     file_object.write("I love programming.")
```

Lời gọi `open()` trong ví dụ này có hai đối số ❶. Đối số thứ nhất vẫn là tên của file ta muốn mở. Đối số thứ hai, `'w'`, cho Python biết ta muốn mở file ở *chế độ ghi* (write mode). Bạn có thể mở file ở *chế độ đọc* (`'r'`), *chế độ ghi* (`'w'`), *chế độ nối thêm* (`'a'`), hoặc một chế độ cho phép bạn vừa đọc vừa ghi vào file (`'r+'`). Nếu bạn bỏ qua đối số chế độ, Python mặc định mở file ở chế độ chỉ đọc.

<!-- pdf-page: 231 | printed: 198 -->

Hàm `open()` tự động tạo file bạn đang ghi vào nếu file đó chưa tồn tại. Tuy nhiên, hãy cẩn thận khi mở file ở chế độ ghi (`'w'`), vì nếu file đã tồn tại, Python sẽ xóa sạch nội dung file trước khi trả về đối tượng file.

Tại ❷, chúng ta dùng phương thức `write()` trên đối tượng file để ghi một chuỗi vào file. Chương trình này không có đầu ra trên terminal, nhưng nếu mở file *programming.txt*, bạn sẽ thấy một dòng:

**programming.txt**

```text
I love programming.
```

File này hoạt động giống như mọi file khác trên máy tính của bạn. Bạn có thể mở nó, viết văn bản mới vào đó, sao chép từ nó, dán vào nó, v.v.

> **Lưu ý** Python chỉ có thể ghi chuỗi vào một file văn bản. Nếu muốn lưu dữ liệu số vào file văn bản, trước tiên bạn sẽ phải chuyển dữ liệu sang dạng chuỗi bằng hàm `str()`.

### Ghi nhiều dòng

Hàm `write()` không thêm ký tự xuống dòng nào vào văn bản bạn ghi. Vì vậy, nếu ghi nhiều hơn một dòng mà không thêm ký tự xuống dòng, file của bạn có thể trông không như ý muốn:

```python
filename = 'programming.txt'

with open(filename, 'w') as file_object:
    file_object.write("I love programming.")
    file_object.write("I love creating new games.")
```

Nếu mở *programming.txt*, bạn sẽ thấy hai dòng bị dồn lại với nhau:

```text
I love programming.I love creating new games.
```

Thêm ký tự xuống dòng vào các câu lệnh `write()` sẽ khiến mỗi chuỗi xuất hiện trên một dòng riêng:

```python
filename = 'programming.txt'

with open(filename, 'w') as file_object:
    file_object.write("I love programming.\n")
    file_object.write("I love creating new games.\n")
```

Giờ đầu ra xuất hiện trên các dòng riêng biệt:

```text
I love programming.
I love creating new games.
```

<!-- pdf-page: 232 | printed: 199 -->

Bạn cũng có thể dùng dấu cách, ký tự tab và dòng trống để định dạng đầu ra, giống như bạn vẫn làm với đầu ra trên terminal.

### Nối thêm vào file

Nếu muốn thêm nội dung vào một file thay vì ghi đè lên nội dung hiện có, bạn có thể mở file ở *chế độ nối thêm* (append mode). Khi bạn mở một file ở chế độ nối thêm, Python không xóa nội dung file trước khi trả về đối tượng file. Mọi dòng bạn ghi vào file sẽ được thêm vào cuối file. Nếu file chưa tồn tại, Python sẽ tạo một file rỗng cho bạn.

Hãy sửa *write_message.py* bằng cách thêm vài lý do mới khiến ta yêu thích lập trình vào file *programming.txt* đã có:

**write_message.py**

```python
  filename = 'programming.txt'
❶ with open(filename, 'a') as file_object:
❷     file_object.write("I also love finding meaning in large datasets.\n")
      file_object.write("I love creating apps that can run in a browser.\n")
```

Tại ❶, chúng ta dùng đối số `'a'` để mở file ở chế độ nối thêm thay vì ghi đè lên file hiện có. Tại ❷, ta ghi hai dòng mới, được thêm vào *programming.txt*:

**programming.txt**

```text
I love programming.
I love creating new games.
I also love finding meaning in large datasets.
I love creating apps that can run in a browser.
```

Cuối cùng, chúng ta có nội dung ban đầu của file, theo sau là nội dung mới vừa thêm vào.

<!-- box -->

**Tự mình thực hành**

**10-3. Khách:** Viết một chương trình yêu cầu người dùng nhập tên. Khi họ trả lời, hãy ghi tên của họ vào một file có tên *guest.txt*.

**10-4. Sổ khách:** Viết một vòng lặp `while` yêu cầu người dùng nhập tên. Khi họ nhập tên, in một lời chào ra màn hình và thêm một dòng ghi lại lượt ghé thăm của họ vào một file có tên *guest_book.txt*. Đảm bảo mỗi mục nằm trên một dòng mới trong file.

**10-5. Khảo sát về lập trình:** Viết một vòng lặp `while` hỏi mọi người vì sao họ thích lập trình. Mỗi khi có người nhập một lý do, hãy thêm lý do đó vào một file lưu tất cả các câu trả lời.

<!-- /box -->

<!-- pdf-page: 233 | printed: 200 -->

## Ngoại lệ

Python dùng những đối tượng đặc biệt gọi là *ngoại lệ* (exception) để quản lý các lỗi phát sinh trong quá trình thực thi chương trình. Mỗi khi xảy ra một lỗi khiến Python không chắc phải làm gì tiếp theo, nó tạo ra một đối tượng ngoại lệ. Nếu bạn viết mã xử lý ngoại lệ đó, chương trình sẽ tiếp tục chạy. Nếu bạn không xử lý ngoại lệ, chương trình sẽ dừng lại và hiển thị một *traceback*, trong đó có báo cáo về ngoại lệ đã được phát sinh.

Ngoại lệ được xử lý bằng các khối `try`-`except`. Một khối `try`-`except` yêu cầu Python làm một việc gì đó, nhưng cũng cho Python biết phải làm gì nếu một ngoại lệ được phát sinh. Khi bạn dùng các khối `try`-`except`, chương trình sẽ tiếp tục chạy ngay cả khi mọi thứ bắt đầu trục trặc. Thay vì những traceback có thể gây khó hiểu cho người dùng, họ sẽ thấy những thông báo lỗi thân thiện do bạn viết.

### Xử lý ngoại lệ ZeroDivisionError

Hãy xem một lỗi đơn giản khiến Python phát sinh một ngoại lệ. Có lẽ bạn biết rằng không thể chia một số cho không, nhưng dù sao hãy cứ yêu cầu Python làm điều đó:

**division.py**

```python
print(5/0)
```

Tất nhiên Python không thể làm điều này, nên chúng ta nhận được một traceback:

```python
  Traceback (most recent call last):
    File "division.py", line 1, in <module>
      print(5/0)
❶ ZeroDivisionError: division by zero
```

Lỗi được báo cáo tại ❶ trong traceback, `ZeroDivisionError`, là một đối tượng ngoại lệ. Python tạo ra loại đối tượng này để phản hồi một tình huống mà nó không thể làm những gì ta yêu cầu. Khi điều này xảy ra, Python dừng chương trình và cho ta biết loại ngoại lệ đã được phát sinh. Ta có thể dùng thông tin này để sửa đổi chương trình. Ta sẽ cho Python biết phải làm gì khi loại ngoại lệ này xảy ra; nhờ đó, nếu nó xảy ra lần nữa, ta đã có sự chuẩn bị.

### Dùng khối try-except

Khi nghĩ rằng một lỗi có thể xảy ra, bạn có thể viết một khối `try`-`except` để xử lý ngoại lệ có thể được phát sinh. Bạn yêu cầu Python thử chạy một đoạn mã, và cho nó biết phải làm gì nếu đoạn mã đó gây ra một loại ngoại lệ cụ thể.

Đây là một khối `try`-`except` để xử lý ngoại lệ `ZeroDivisionError`:

```python
try:
    print(5/0)
except ZeroDivisionError:
    print("You can't divide by zero!")
```

<!-- pdf-page: 234 | printed: 201 -->

Chúng ta đặt `print(5/0)`, dòng gây ra lỗi, vào bên trong một khối `try`. Nếu đoạn mã trong khối `try` chạy được, Python bỏ qua khối `except`. Nếu đoạn mã trong khối `try` gây ra lỗi, Python tìm một khối `except` có lỗi khớp với lỗi đã được phát sinh và chạy đoạn mã trong khối đó.

Trong ví dụ này, đoạn mã trong khối `try` gây ra một `ZeroDivisionError`, nên Python tìm một khối `except` cho nó biết cách phản hồi. Sau đó, Python chạy đoạn mã trong khối đó, và người dùng thấy một thông báo lỗi thân thiện thay vì một traceback:

```text
You can't divide by zero!
```

Nếu còn đoạn mã nào khác đứng sau khối `try`-`except`, chương trình sẽ tiếp tục chạy vì chúng ta đã cho Python biết cách xử lý lỗi. Hãy xem một ví dụ mà việc bắt lỗi có thể cho phép chương trình tiếp tục chạy.

### Dùng ngoại lệ để tránh chương trình bị dừng đột ngột

Xử lý lỗi đúng cách đặc biệt quan trọng khi chương trình còn có việc phải làm sau khi lỗi xảy ra. Điều này thường xảy ra trong những chương trình yêu cầu người dùng nhập đầu vào. Nếu chương trình phản hồi phù hợp với đầu vào không hợp lệ, nó có thể yêu cầu nhập thêm đầu vào hợp lệ thay vì bị dừng đột ngột.

Hãy tạo một máy tính đơn giản chỉ làm phép chia:

**division.py**

```python
  print("Give me two numbers, and I'll divide them.")
  print("Enter 'q' to quit.")

  while True:
❶     first_number = input("\nFirst number: ")
      if first_number == 'q':
          break
❷     second_number = input("Second number: ")
      if second_number == 'q':
          break
❸     answer = int(first_number) / int(second_number)
      print(answer)
```

Chương trình này yêu cầu người dùng nhập `first_number` ❶ và, nếu người dùng không nhập *q* để thoát, nhập `second_number` ❷. Sau đó, ta chia hai số này để được `answer` ❸. Chương trình này không làm gì để xử lý lỗi, nên yêu cầu nó chia cho không sẽ khiến nó bị dừng đột ngột:

```python
Give me two numbers, and I'll divide them.
Enter 'q' to quit.

First number: 5
Second number: 0
Traceback (most recent call last):
  File "division.py", line 9, in <module>
    answer = int(first_number) / int(second_number)
ZeroDivisionError: division by zero
```

<!-- pdf-page: 235 | printed: 202 -->

Chương trình bị dừng đột ngột đã là điều tệ, nhưng để người dùng nhìn thấy traceback cũng không phải là ý hay. Những người dùng không rành kỹ thuật sẽ bối rối khi thấy chúng, và trong một bối cảnh có ý đồ xấu, kẻ tấn công sẽ biết được nhiều hơn mức bạn muốn từ một traceback. Ví dụ, họ sẽ biết tên file chương trình của bạn, và sẽ thấy một phần mã đang không hoạt động đúng. Một kẻ tấn công lành nghề đôi khi có thể dùng thông tin này để xác định loại tấn công nào nên dùng để nhắm vào mã của bạn.

### Khối else

Chúng ta có thể làm cho chương trình này chống chịu lỗi tốt hơn bằng cách bọc dòng có thể gây lỗi trong một khối `try`-`except`. Lỗi xảy ra ở dòng thực hiện phép chia, nên đó là chỗ ta sẽ đặt khối `try`-`except`. Ví dụ này cũng có một khối `else`. Mọi đoạn mã phụ thuộc vào việc khối `try` được thực thi thành công đều được đặt trong khối `else`:

```python
  print("Give me two numbers, and I'll divide them.")
  print("Enter 'q' to quit.")

  while True:
      first_number = input("\nFirst number: ")
      if first_number == 'q':
          break
      second_number = input("Second number: ")
❶     try:
          answer = int(first_number) / int(second_number)
❷     except ZeroDivisionError:
          print("You can't divide by 0!")
❸     else:
          print(answer)
```

Chúng ta yêu cầu Python thử hoàn thành phép chia trong một khối `try` ❶, khối này chỉ chứa đoạn mã có thể gây ra lỗi. Mọi đoạn mã phụ thuộc vào việc khối `try` thành công được thêm vào khối `else`. Trong trường hợp này, nếu phép chia thành công, ta dùng khối `else` để in kết quả ❸.

Khối `except` cho Python biết cách phản hồi khi một `ZeroDivisionError` phát sinh ❷. Nếu câu lệnh `try` không thành công do lỗi chia cho không, ta in ra một thông điệp thân thiện cho người dùng biết cách tránh loại lỗi này. Chương trình tiếp tục chạy, và người dùng không bao giờ thấy traceback:

```text
Give me two numbers, and I'll divide them.
Enter 'q' to quit.

First number: 5
Second number: 0
You can't divide by 0!
First number: 5
Second number: 2
2.5

First number: q
```

<!-- pdf-page: 236 | printed: 203 -->

Khối `try`-`except`-`else` hoạt động như sau: Python cố chạy đoạn mã trong câu lệnh `try`. Đoạn mã duy nhất nên đặt trong câu lệnh `try` là đoạn mã có thể khiến một ngoại lệ được phát sinh. Đôi khi bạn sẽ có thêm đoạn mã chỉ nên chạy nếu khối `try` thành công; đoạn mã này được đặt trong khối `else`. Khối `except` cho Python biết phải làm gì trong trường hợp một ngoại lệ nhất định phát sinh khi nó cố chạy đoạn mã trong câu lệnh `try`.

Bằng cách lường trước những nguồn gây lỗi có khả năng xảy ra, bạn có thể viết những chương trình vững vàng, tiếp tục chạy ngay cả khi gặp dữ liệu không hợp lệ hoặc tài nguyên bị thiếu. Mã của bạn sẽ chống chịu được những nhầm lẫn vô tình của người dùng và những cuộc tấn công có chủ đích.

### Xử lý ngoại lệ FileNotFoundError

Một vấn đề thường gặp khi làm việc với file là xử lý những file bị thiếu. File bạn đang tìm có thể nằm ở một vị trí khác, tên file có thể bị gõ sai, hoặc file có thể hoàn toàn không tồn tại. Bạn có thể xử lý tất cả những tình huống này một cách đơn giản bằng một khối `try`-`except`.

Hãy thử đọc một file không tồn tại. Chương trình sau cố đọc nội dung của *Alice in Wonderland*, nhưng tôi chưa lưu file *alice.txt* vào cùng thư mục với *alice.py*:

**alice.py**

```python
filename = 'alice.txt'

with open(filename) as f_obj:
    contents = f_obj.read()
```

Python không thể đọc từ một file bị thiếu, nên nó phát sinh một ngoại lệ:

```text
Traceback (most recent call last):
  File "alice.py", line 3, in <module>
    with open(filename) as f_obj:
FileNotFoundError: [Errno 2] No such file or directory: 'alice.txt'
```

Dòng cuối cùng của traceback báo cáo một `FileNotFoundError`: đây là ngoại lệ Python tạo ra khi không tìm thấy file mà nó đang cố mở. Trong ví dụ này, hàm `open()` gây ra lỗi, nên để xử lý nó, khối `try` sẽ bắt đầu ngay trước dòng chứa `open()`:

```python
filename = 'alice.txt'

try:
    with open(filename) as f_obj:
        contents = f_obj.read()
except FileNotFoundError:
    msg = "Sorry, the file " + filename + " does not exist."
    print(msg)
```

<!-- pdf-page: 237 | printed: 204 -->

Trong ví dụ này, đoạn mã trong khối `try` gây ra một `FileNotFoundError`, nên Python tìm một khối `except` khớp với lỗi đó. Sau đó, Python chạy đoạn mã trong khối đó, và kết quả là một thông báo lỗi thân thiện thay vì một traceback:

```text
Sorry, the file alice.txt does not exist.
```

Chương trình không còn gì để làm nếu file không tồn tại, nên đoạn mã xử lý lỗi không bổ sung được gì nhiều cho chương trình này. Hãy phát triển tiếp ví dụ này và xem việc xử lý ngoại lệ có thể giúp ích thế nào khi bạn làm việc với nhiều hơn một file.

### Phân tích văn bản

Bạn có thể phân tích những file văn bản chứa toàn bộ một cuốn sách. Nhiều tác phẩm văn học kinh điển có sẵn dưới dạng file văn bản đơn giản vì chúng thuộc phạm vi công cộng (public domain). Các văn bản dùng trong mục này lấy từ Project Gutenberg (*http://gutenberg.org/*). Project Gutenberg duy trì một bộ sưu tập các tác phẩm văn học thuộc phạm vi công cộng, và đây là một tài nguyên tuyệt vời nếu bạn muốn làm việc với văn bản văn học trong các dự án lập trình của mình.

Hãy lấy văn bản của *Alice in Wonderland* và thử đếm số từ trong văn bản. Chúng ta sẽ dùng phương thức chuỗi `split()`, phương thức có thể tạo một list các từ từ một chuỗi. Đây là những gì `split()` làm với một chuỗi chỉ chứa tựa đề `"Alice in Wonderland"`:

```python
>>> title = "Alice in Wonderland"
>>> title.split()
['Alice', 'in', 'Wonderland']
```

Phương thức `split()` tách một chuỗi thành nhiều phần ở bất cứ chỗ nào nó tìm thấy dấu cách, và lưu tất cả các phần của chuỗi vào một list. Kết quả là một list các từ trong chuỗi, dù một số dấu câu cũng có thể xuất hiện cùng một số từ. Để đếm số từ trong *Alice in Wonderland*, ta sẽ dùng `split()` trên toàn bộ văn bản. Sau đó, ta sẽ đếm số phần tử trong list để có ý niệm sơ bộ về số từ trong văn bản:

```python
  filename = 'alice.txt'

  try:
      with open(filename) as f_obj:
          contents = f_obj.read()
  except FileNotFoundError:
      msg = "Sorry, the file " + filename + " does not exist."
      print(msg)
  else:
      # Count the approximate number of words in the file.
❶     words = contents.split()
❷     num_words = len(words)
❸     print("The file " + filename + " has about " + str(num_words) + " words.")
```

<!-- pdf-page: 238 | printed: 205 -->

Tôi đã chuyển file *alice.txt* vào đúng thư mục, nên lần này khối `try` sẽ chạy được. Tại ❶, ta lấy chuỗi `contents`, lúc này chứa toàn bộ văn bản của *Alice in Wonderland* dưới dạng một chuỗi dài, và dùng phương thức `split()` để tạo một list tất cả các từ trong cuốn sách. Khi dùng `len()` trên list này để xem độ dài của nó, ta có được một con số xấp xỉ khá tốt về số từ trong chuỗi ban đầu ❷. Tại ❸, ta in ra một câu cho biết đã tìm thấy bao nhiêu từ trong file. Đoạn mã này được đặt trong khối `else` vì nó chỉ hoạt động nếu đoạn mã trong khối `try` được thực thi thành công. Đầu ra cho ta biết có bao nhiêu từ trong *alice.txt*:

```text
The file alice.txt has about 29461 words.
```

Con số này hơi cao một chút vì nhà xuất bản có cung cấp thêm thông tin trong file văn bản được dùng ở đây, nhưng đây là một con số xấp xỉ khá tốt về độ dài của *Alice in Wonderland*.

### Làm việc với nhiều file

Hãy thêm nhiều cuốn sách hơn để phân tích. Nhưng trước khi làm vậy, hãy chuyển phần lớn chương trình này vào một hàm có tên `count_words()`. Nhờ đó, việc chạy phân tích cho nhiều cuốn sách sẽ dễ dàng hơn:

**word_count.py**

```python
  def count_words(filename):
❶     """Count the approximate number of words in a file."""
      try:
          with open(filename) as f_obj:
              contents = f_obj.read()
      except FileNotFoundError:
          msg = "Sorry, the file " + filename + " does not exist."
          print(msg)
      else:
          # Count approximate number of words in the file.
          words = contents.split()
          num_words = len(words)
          print("The file " + filename + " has about " + str(num_words) +
              " words.")

  filename = 'alice.txt'
  count_words(filename)
```

Phần lớn đoạn mã này không thay đổi. Chúng ta chỉ thụt lề nó và chuyển nó vào thân hàm `count_words()`. Giữ cho chú thích luôn được cập nhật khi sửa đổi chương trình là một thói quen tốt, nên ta đã đổi chú thích thành một docstring và diễn đạt lại một chút ❶.

<!-- pdf-page: 239 | printed: 206 -->

Giờ chúng ta có thể viết một vòng lặp đơn giản để đếm số từ trong bất kỳ văn bản nào ta muốn phân tích. Ta làm điều này bằng cách lưu tên các file cần phân tích vào một list, rồi gọi `count_words()` cho từng file trong list. Ta sẽ thử đếm số từ cho *Alice in Wonderland*, *Siddhartha*, *Moby Dick* và *Little Women*, tất cả đều thuộc phạm vi công cộng. Tôi đã cố tình không đặt *siddhartha.txt* vào thư mục chứa *word_count.py*, để ta có thể xem chương trình xử lý một file bị thiếu tốt đến mức nào:

```python
def count_words(filename):
    --snip--

filenames = ['alice.txt', 'siddhartha.txt', 'moby_dick.txt', 'little_women.txt']
for filename in filenames:
    count_words(filename)
```

File *siddhartha.txt* bị thiếu không ảnh hưởng gì đến việc thực thi phần còn lại của chương trình:

```text
The file alice.txt has about 29461 words.
Sorry, the file siddhartha.txt does not exist.
The file moby_dick.txt has about 215136 words.
The file little_women.txt has about 189079 words.
```

Dùng khối `try`-`except` trong ví dụ này mang lại hai ưu điểm đáng kể. Ta ngăn người dùng nhìn thấy traceback, và để chương trình tiếp tục phân tích những văn bản mà nó tìm thấy. Nếu không bắt `FileNotFoundError` do *siddhartha.txt* phát sinh, người dùng sẽ thấy một traceback đầy đủ, và chương trình sẽ ngừng chạy sau khi cố phân tích *Siddhartha*. Nó sẽ không bao giờ phân tích *Moby Dick* hay *Little Women*.

### Thất bại trong im lặng

Trong ví dụ trước, chúng ta đã thông báo cho người dùng rằng một trong các file không có sẵn. Nhưng bạn không cần báo cáo mọi ngoại lệ mà mình bắt được. Đôi khi bạn sẽ muốn chương trình thất bại trong im lặng khi một ngoại lệ xảy ra và tiếp tục chạy như thể không có gì xảy ra. Để làm cho một chương trình thất bại trong im lặng, bạn viết một khối `try` như bình thường, nhưng nói rõ với Python là không làm gì trong khối `except`. Python có một câu lệnh `pass` yêu cầu nó không làm gì trong một khối:

```python
  def count_words(filename):
      """Count the approximate number of words in a file."""
      try:
          --snip--
      except FileNotFoundError:
❶         pass
      else:
          --snip--

  filenames = ['alice.txt', 'siddhartha.txt', 'moby_dick.txt', 'little_women.txt']
  for filename in filenames:
      count_words(filename)
```

<!-- pdf-page: 240 | printed: 207 -->

Điểm khác biệt duy nhất giữa đoạn mã này và đoạn mã trước là câu lệnh `pass` tại ❶. Giờ khi một `FileNotFoundError` được phát sinh, đoạn mã trong khối `except` được chạy, nhưng không có gì xảy ra. Không có traceback nào được tạo ra, và không có đầu ra nào để phản hồi lỗi đã phát sinh. Người dùng thấy số từ của từng file tồn tại, nhưng không thấy bất kỳ dấu hiệu nào cho thấy có một file không được tìm thấy:

```text
The file alice.txt has about 29461 words.
The file moby_dick.txt has about 215136 words.
The file little_women.txt has about 189079 words.
```

Câu lệnh `pass` cũng đóng vai trò giữ chỗ. Nó là lời nhắc rằng bạn đang chọn không làm gì tại một điểm cụ thể trong quá trình thực thi chương trình, và có thể bạn sẽ muốn làm gì đó ở đó sau này. Ví dụ, trong chương trình này, ta có thể quyết định ghi tên các file bị thiếu vào một file có tên *missing_files.txt*. Người dùng sẽ không thấy file này, nhưng ta có thể đọc nó và xử lý những văn bản bị thiếu.

### Quyết định báo cáo những lỗi nào

Làm thế nào để biết khi nào nên báo lỗi cho người dùng và khi nào nên thất bại trong im lặng? Nếu người dùng biết những văn bản nào lẽ ra phải được phân tích, có thể họ sẽ đánh giá cao một thông điệp cho họ biết vì sao một số văn bản không được phân tích. Nếu người dùng mong đợi thấy một số kết quả nhưng không biết những cuốn sách nào lẽ ra phải được phân tích, có thể họ không cần biết rằng một số văn bản không có sẵn. Cung cấp cho người dùng những thông tin họ không tìm kiếm có thể làm giảm tính dễ dùng của chương trình. Các cấu trúc xử lý lỗi của Python cho bạn khả năng kiểm soát tỉ mỉ mức độ chia sẻ với người dùng khi có sự cố; bạn quyết định chia sẻ bao nhiêu thông tin.

Mã được viết tốt và được kiểm thử đúng cách thì không dễ gặp lỗi nội tại, chẳng hạn lỗi cú pháp hay lỗi logic. Nhưng mỗi khi chương trình của bạn phụ thuộc vào một thứ gì đó bên ngoài, chẳng hạn đầu vào của người dùng, sự tồn tại của một file, hay sự sẵn có của kết nối mạng, thì luôn có khả năng một ngoại lệ được phát sinh. Một chút kinh nghiệm sẽ giúp bạn biết nên đặt các khối xử lý ngoại lệ ở đâu trong chương trình và nên báo cáo bao nhiêu cho người dùng về những lỗi phát sinh.

<!-- box -->

**Tự mình thực hành**

**10-6. Phép cộng:** Một vấn đề thường gặp khi yêu cầu nhập đầu vào dạng số là người dùng nhập chữ thay vì số. Khi bạn cố chuyển đầu vào thành `int`, bạn sẽ gặp một `TypeError`. Viết một chương trình yêu cầu nhập hai số. Cộng chúng lại và in kết quả ra. Bắt `TypeError` nếu một trong hai giá trị đầu vào không phải là số, và in ra một thông báo lỗi thân thiện. Kiểm tra chương trình bằng cách nhập hai số, rồi nhập chữ thay vì số.

*(còn tiếp)*

<!-- pdf-page: 241 | printed: 208 -->

**10-7. Máy tính cộng:** Bọc đoạn mã của bạn từ Bài tập 10-6 trong một vòng lặp `while` để người dùng có thể tiếp tục nhập số ngay cả khi họ nhầm lẫn và nhập chữ thay vì số.

**10-8. Mèo và chó:** Tạo hai file, *cats.txt* và *dogs.txt*. Lưu ít nhất ba tên mèo vào file thứ nhất và ba tên chó vào file thứ hai. Viết một chương trình cố đọc các file này và in nội dung của file ra màn hình. Bọc đoạn mã của bạn trong một khối `try-except` để bắt lỗi `FileNotFound`, và in ra một thông điệp thân thiện nếu một file bị thiếu. Chuyển một trong hai file sang một vị trí khác trên hệ thống, và đảm bảo đoạn mã trong khối `except` được thực thi đúng.

**10-9. Mèo và chó im lặng:** Sửa khối `except` của bạn trong Bài tập 10-8 để thất bại trong im lặng nếu một trong hai file bị thiếu.

**10-10. Những từ phổ biến:** Truy cập Project Gutenberg (*http://gutenberg.org/* ) và tìm một vài văn bản bạn muốn phân tích. Tải về các file văn bản của những tác phẩm này, hoặc sao chép văn bản thô từ trình duyệt vào một file văn bản trên máy tính của bạn.

Bạn có thể dùng phương thức `count()` để biết một từ hoặc cụm từ xuất hiện bao nhiêu lần trong một chuỗi. Ví dụ, đoạn mã sau đếm số lần `'row'` xuất hiện trong một chuỗi:

```python
>>> line = "Row, row, row your boat"
>>> line.count('row')
2
>>> line.lower().count('row')
3
```

Hãy để ý rằng việc chuyển chuỗi thành chữ thường bằng `lower()` sẽ bắt được mọi lần xuất hiện của từ bạn đang tìm, bất kể nó được định dạng thế nào.

Viết một chương trình đọc các file bạn tìm được trên Project Gutenberg và xác định từ `'the'` xuất hiện bao nhiêu lần trong mỗi văn bản.

<!-- /box -->

## Lưu trữ dữ liệu

Nhiều chương trình của bạn sẽ yêu cầu người dùng nhập một số loại thông tin nhất định. Bạn có thể cho phép người dùng lưu các tùy chọn trong một trò chơi hoặc cung cấp dữ liệu cho một biểu đồ trực quan. Dù chương trình của bạn tập trung vào điều gì, bạn sẽ lưu thông tin người dùng cung cấp trong các cấu trúc dữ liệu như list và dictionary. Khi người dùng đóng chương trình, hầu như lúc nào bạn cũng sẽ muốn lưu lại thông tin họ đã nhập. Một cách đơn giản để làm điều này là lưu dữ liệu bằng module `json`.

<!-- pdf-page: 242 | printed: 209 -->

Module `json` cho phép bạn ghi (dump) các cấu trúc dữ liệu Python đơn giản vào một file và tải dữ liệu từ file đó ở lần chạy tiếp theo của chương trình. Bạn cũng có thể dùng `json` để chia sẻ dữ liệu giữa các chương trình Python khác nhau. Hay hơn nữa, định dạng dữ liệu JSON không dành riêng cho Python, nên bạn có thể chia sẻ dữ liệu lưu ở định dạng JSON với những người làm việc bằng nhiều ngôn ngữ lập trình khác. Đây là một định dạng hữu ích, dễ chuyển đổi giữa các nền tảng, và dễ học.

> **Lưu ý** Định dạng JSON (JavaScript Object Notation) ban đầu được phát triển cho JavaScript. Tuy nhiên, từ đó đến nay, nó đã trở thành một định dạng phổ biến được nhiều ngôn ngữ sử dụng, kể cả Python.

### Dùng json.dump() và json.load()

Hãy viết một chương trình ngắn lưu một tập hợp số và một chương trình khác đọc lại các số này vào bộ nhớ. Chương trình thứ nhất sẽ dùng `json.dump()` để lưu tập hợp số, và chương trình thứ hai sẽ dùng `json.load()`.

Hàm `json.dump()` nhận hai đối số: một mẩu dữ liệu cần lưu và một đối tượng file mà nó có thể dùng để lưu dữ liệu. Đây là cách bạn có thể dùng `json.dump()` để lưu một list số:

**number_writer.py**

```python
  import json
  numbers = [2, 3, 5, 7, 11, 13]

❶ filename = 'numbers.json'
❷ with open(filename, 'w') as f_obj:
❸     json.dump(numbers, f_obj)
```

Đầu tiên, chúng ta import module `json` rồi tạo một list số để làm việc. Tại ❶, ta chọn một tên file để lưu list số. Theo thông lệ, người ta dùng phần mở rộng *.json* để cho biết dữ liệu trong file được lưu ở định dạng JSON. Sau đó, ta mở file ở chế độ ghi, cho phép `json` ghi dữ liệu vào file ❷. Tại ❸, ta dùng hàm `json.dump()` để lưu list `numbers` vào file *numbers.json*.

Chương trình này không có đầu ra, nhưng hãy mở file *numbers.json* và xem nó. Dữ liệu được lưu theo một định dạng trông giống hệt Python:

```text
[2, 3, 5, 7, 11, 13]
```

Giờ chúng ta sẽ viết một chương trình dùng `json.load()` để đọc list đó trở lại bộ nhớ:

**number_reader.py**

```python
  import json
❶ filename = 'numbers.json'
❷ with open(filename) as f_obj:
❸     numbers = json.load(f_obj)

  print(numbers)
```

<!-- pdf-page: 243 | printed: 210 -->

Tại ❶, chúng ta đảm bảo đọc từ đúng file đã ghi vào. Lần này khi mở file, ta mở nó ở chế độ đọc vì Python chỉ cần đọc từ file ❷. Tại ❸, ta dùng hàm `json.load()` để tải thông tin được lưu trong *numbers.json*, và lưu nó vào biến `numbers`. Cuối cùng, ta in ra list số đã được khôi phục và thấy rằng đó chính là list đã được tạo trong *number_writer.py*:

```text
[2, 3, 5, 7, 11, 13]
```

Đây là một cách đơn giản để chia sẻ dữ liệu giữa hai chương trình.

### Lưu và đọc dữ liệu do người dùng tạo ra

Lưu dữ liệu bằng `json` rất hữu ích khi bạn làm việc với dữ liệu do người dùng tạo ra, vì nếu không lưu thông tin của người dùng theo cách nào đó, bạn sẽ mất nó khi chương trình ngừng chạy. Hãy xem một ví dụ trong đó chúng ta yêu cầu người dùng nhập tên ở lần đầu tiên họ chạy chương trình, rồi ghi nhớ tên của họ khi họ chạy lại chương trình.

Hãy bắt đầu bằng việc lưu tên của người dùng:

**remember_me.py**

```python
  import json
❶ username = input("What is your name? ")

  filename = 'username.json'
  with open(filename, 'w') as f_obj:
❷     json.dump(username, f_obj)
❸     print("We'll remember you when you come back, " + username + "!")
```

Tại ❶, chúng ta yêu cầu nhập một tên người dùng để lưu. Tiếp theo, ta dùng `json.dump()`, truyền cho nó một tên người dùng và một đối tượng file, để lưu tên người dùng vào một file ❷. Sau đó, ta in ra một thông điệp cho người dùng biết ta đã lưu thông tin của họ ❸:

```text
What is your name? Eric
We'll remember you when you come back, Eric!
```

Giờ hãy viết một chương trình mới chào một người dùng có tên đã được lưu:

**greet_user.py**

```python
  import json

  filename = 'username.json'

  with open(filename) as f_obj:
❶     username = json.load(f_obj)
❷     print("Welcome back, " + username + "!")
```

<!-- pdf-page: 244 | printed: 211 -->

Tại ❶, chúng ta dùng `json.load()` để đọc thông tin được lưu trong *username.json* vào biến `username`. Giờ khi đã khôi phục được tên người dùng, ta có thể chào mừng họ trở lại ❷:

```text
Welcome back, Eric!
```

Chúng ta cần kết hợp hai chương trình này vào một file. Khi ai đó chạy *remember_me.py*, ta muốn lấy lại tên người dùng của họ từ bộ nhớ nếu có thể; vì vậy, ta sẽ bắt đầu bằng một khối `try` cố khôi phục tên người dùng. Nếu file *username.json* không tồn tại, ta sẽ để khối `except` yêu cầu nhập tên người dùng và lưu nó vào *username.json* cho lần sau:

**remember_me.py**

```python
  import json
  # Load the username, if it has been stored previously.
  #  Otherwise, prompt for the username and store it.
  filename = 'username.json'
  try:
❶     with open(filename) as f_obj:
❷         username = json.load(f_obj)
❸ except FileNotFoundError:
❹     username = input("What is your name? ")
❺     with open(filename, 'w') as f_obj:
          json.dump(username, f_obj)
          print("We'll remember you when you come back, " + username + "!")
  else:
      print("Welcome back, " + username + "!")
```

Không có đoạn mã mới nào ở đây; các khối mã từ hai ví dụ trước chỉ được kết hợp vào một file. Tại ❶, ta thử mở file *username.json*. Nếu file này tồn tại, ta đọc tên người dùng trở lại bộ nhớ ❷ và in ra thông điệp chào mừng người dùng trở lại trong khối `else`. Nếu đây là lần đầu tiên người dùng chạy chương trình, *username.json* sẽ không tồn tại và một `FileNotFoundError` sẽ xảy ra ❸. Python sẽ chuyển sang khối `except`, nơi ta yêu cầu người dùng nhập tên người dùng ❹. Sau đó, ta dùng `json.dump()` để lưu tên người dùng và in ra một lời chào ❺.

Dù khối nào được thực thi, kết quả đều là một tên người dùng và một lời chào phù hợp. Nếu đây là lần đầu tiên chương trình chạy, đầu ra sẽ là:

```text
What is your name? Eric
We'll remember you when you come back, Eric!
```

Ngược lại:

```text
Welcome back, Eric!
```

Đây là đầu ra bạn thấy nếu chương trình đã được chạy ít nhất một lần.

<!-- pdf-page: 245 | printed: 212 -->

### Tái cấu trúc mã

Bạn sẽ thường đến một thời điểm mà mã của mình đã hoạt động, nhưng bạn nhận ra mình có thể cải thiện nó bằng cách chia nhỏ thành một loạt hàm, mỗi hàm có một nhiệm vụ cụ thể. Quá trình này được gọi là *tái cấu trúc mã* (refactoring). Tái cấu trúc giúp mã của bạn gọn gàng hơn, dễ hiểu hơn và dễ mở rộng hơn.

Chúng ta có thể tái cấu trúc *remember_me.py* bằng cách chuyển phần lớn logic của nó vào một hoặc nhiều hàm. Trọng tâm của *remember_me.py* là chào người dùng, vậy hãy chuyển toàn bộ đoạn mã hiện có vào một hàm có tên `greet_user()`:

**remember_me.py**

```python
  import json
  def greet_user():
❶     """Greet the user by name."""
      filename = 'username.json'
      try:
          with open(filename) as f_obj:
              username = json.load(f_obj)
      except FileNotFoundError:
          username = input("What is your name? ")
          with open(filename, 'w') as f_obj:
              json.dump(username, f_obj)
              print("We'll remember you when you come back, " + username + "!")
      else:
          print("Welcome back, " + username + "!")

  greet_user()
```

Vì giờ đang dùng hàm, chúng ta cập nhật chú thích bằng một docstring phản ánh cách chương trình hiện đang hoạt động ❶. File này gọn gàng hơn một chút, nhưng hàm `greet_user()` đang làm nhiều hơn là chỉ chào người dùng — nó còn lấy tên người dùng đã lưu nếu có, và yêu cầu nhập tên người dùng mới nếu chưa có.

Hãy tái cấu trúc `greet_user()` để nó không phải làm quá nhiều tác vụ khác nhau. Chúng ta sẽ bắt đầu bằng việc chuyển đoạn mã lấy tên người dùng đã lưu sang một hàm riêng:

```python
  import json

  def get_stored_username():
❶     """Get stored username if available."""
      filename = 'username.json'
      try:
          with open(filename) as f_obj:
              username = json.load(f_obj)
      except FileNotFoundError:
❷         return None
      else:
          return username
  def greet_user():
      """Greet the user by name."""
      username = get_stored_username()
❸     if username:
          print("Welcome back, " + username + "!")
      else:
          username = input("What is your name? ")
          filename = 'username.json'
          with open(filename, 'w') as f_obj:
              json.dump(username, f_obj)
              print("We'll remember you when you come back, " + username + "!")

  greet_user()
```

<!-- pdf-page: 246 | printed: 213 -->

Hàm mới `get_stored_username()` có mục đích rõ ràng, như được nêu trong docstring tại ❶. Hàm này lấy tên người dùng đã lưu và trả về tên người dùng nếu tìm thấy. Nếu file *username.json* không tồn tại, hàm trả về `None` ❷. Đây là một thói quen tốt: một hàm nên trả về giá trị bạn mong đợi, hoặc trả về `None`. Điều này cho phép ta thực hiện một phép kiểm tra đơn giản với giá trị trả về của hàm. Tại ❸, ta in ra thông điệp chào mừng người dùng trở lại nếu việc lấy tên người dùng thành công, còn nếu không, ta yêu cầu nhập tên người dùng mới.

Chúng ta nên tách thêm một khối mã nữa ra khỏi `greet_user()`. Nếu tên người dùng không tồn tại, ta nên chuyển đoạn mã yêu cầu nhập tên người dùng mới sang một hàm dành riêng cho mục đích đó:

```python
import json

def get_stored_username():
    """Get stored username if available."""
    --snip--

def get_new_username():
    """Prompt for a new username."""
    username = input("What is your name? ")
    filename = 'username.json'
    with open(filename, 'w') as f_obj:
        json.dump(username, f_obj)
    return username

def greet_user():
    """Greet the user by name."""
    username = get_stored_username()
    if username:
        print("Welcome back, " + username + "!")
    else:
        username = get_new_username()
        print("We'll remember you when you come back, " + username + "!")

greet_user()
```

<!-- pdf-page: 247 | printed: 214 -->

Mỗi hàm trong phiên bản cuối cùng này của *remember_me.py* có một mục đích duy nhất, rõ ràng. Chúng ta gọi `greet_user()`, và hàm đó in ra một thông điệp phù hợp: hoặc chào mừng một người dùng cũ trở lại, hoặc chào một người dùng mới. Nó làm điều này bằng cách gọi `get_stored_username()`, hàm chỉ chịu trách nhiệm lấy tên người dùng đã lưu nếu có. Cuối cùng, `greet_user()` gọi `get_new_username()` nếu cần, hàm chỉ chịu trách nhiệm lấy tên người dùng mới và lưu nó. Việc phân chia công việc thành từng phần như thế này là một phần thiết yếu của việc viết mã rõ ràng, dễ bảo trì và dễ mở rộng.

<!-- box -->

**Tự mình thực hành**

**10-11. Số yêu thích:** Viết một chương trình yêu cầu người dùng nhập số yêu thích của họ. Dùng `json.dump()` để lưu số này vào một file. Viết một chương trình riêng đọc giá trị này và in ra thông điệp, “I know your favorite number! It’s _____.”

**10-12. Ghi nhớ số yêu thích:** Kết hợp hai chương trình từ Bài tập 10-11 vào một file. Nếu số đã được lưu, hãy báo số yêu thích cho người dùng. Nếu chưa, hãy yêu cầu người dùng nhập số yêu thích và lưu nó vào một file. Chạy chương trình hai lần để thấy nó hoạt động.

**10-13. Xác minh người dùng:** Phiên bản cuối cùng của *remember_me.py* giả định rằng hoặc người dùng đã nhập tên người dùng của họ, hoặc chương trình đang chạy lần đầu tiên. Chúng ta nên sửa đổi nó cho trường hợp người dùng hiện tại không phải là người đã dùng chương trình lần gần nhất.

Trước khi in thông điệp chào mừng trở lại trong `greet_user()`, hãy hỏi người dùng xem đây có phải là tên người dùng đúng không. Nếu không phải, hãy gọi `get_new_username()` để lấy tên người dùng đúng.

<!-- /box -->

## Tổng kết

Trong chương này, bạn đã học cách làm việc với file. Bạn đã học cách đọc toàn bộ file một lần và đọc qua nội dung của file từng dòng một. Bạn đã học cách ghi vào file và nối thêm văn bản vào cuối file. Bạn đã tìm hiểu về ngoại lệ và cách xử lý những ngoại lệ mà nhiều khả năng bạn sẽ gặp trong chương trình. Cuối cùng, bạn đã học cách lưu các cấu trúc dữ liệu Python để có thể lưu lại thông tin người dùng cung cấp, giúp họ không phải bắt đầu lại từ đầu mỗi khi chạy chương trình.

Trong Chương 11, bạn sẽ học những cách hiệu quả để kiểm thử mã của mình. Điều này sẽ giúp bạn tin tưởng rằng đoạn mã bạn phát triển là đúng, và giúp bạn xác định những lỗi phát sinh khi bạn tiếp tục phát triển các chương trình đã viết.

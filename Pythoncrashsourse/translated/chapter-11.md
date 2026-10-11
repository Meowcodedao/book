<!-- source: pythoncrashcourse.pdf | unit: chapter-11 | pdf pages 248-263 | printed 215-230 -->

# Chương 11: Kiểm thử mã

<!-- pdf-page: 248 | printed: 215 -->

Khi viết một hàm hoặc một lớp, bạn cũng có thể viết kiểm thử (test) cho đoạn mã đó. Kiểm thử chứng minh rằng mã của bạn hoạt động đúng như mong đợi với mọi loại đầu vào mà nó được thiết kế để nhận. Khi viết kiểm thử, bạn có thể tự tin rằng mã của mình sẽ hoạt động đúng khi ngày càng có nhiều người bắt đầu dùng chương trình của bạn. Bạn cũng sẽ có thể kiểm thử

đoạn mã mới khi thêm nó vào, để đảm bảo những thay đổi của bạn không làm hỏng hành vi hiện có của chương trình. Lập trình viên nào cũng mắc lỗi, vì vậy lập trình viên nào cũng phải thường xuyên kiểm thử mã của mình, phát hiện vấn đề trước khi người dùng gặp phải chúng.

Trong chương này, bạn sẽ học cách kiểm thử mã bằng các công cụ trong module `unittest` của Python. Bạn sẽ học cách xây dựng một test case và kiểm tra xem một tập đầu vào có cho ra đầu ra bạn muốn hay không. Bạn sẽ thấy một bài kiểm thử thành công trông như thế nào và một bài kiểm thử thất bại trông như thế nào, và sẽ học cách một bài kiểm thử thất bại có thể giúp bạn cải thiện mã. Bạn sẽ học cách kiểm thử hàm và lớp, và bắt đầu hiểu nên viết bao nhiêu bài kiểm thử cho một dự án.

<!-- pdf-page: 249 | printed: 216 -->

## Kiểm thử một hàm

Để học về kiểm thử, chúng ta cần một đoạn mã để kiểm thử. Đây là một hàm đơn giản nhận vào tên và họ, rồi trả về họ tên đầy đủ được định dạng gọn gàng:

**name_function.py**

```python
def get_formatted_name(first, last):
    """Generate a neatly formatted full name."""
    full_name = first + ' ' + last
    return full_name.title()
```

Hàm `get_formatted_name()` kết hợp tên và họ với một dấu cách ở giữa để tạo thành họ tên đầy đủ, rồi viết hoa và trả về họ tên đầy đủ đó. Để kiểm tra xem `get_formatted_name()` có hoạt động không, hãy tạo một chương trình dùng hàm này. Chương trình *names.py* cho phép người dùng nhập tên và họ, rồi xem họ tên đầy đủ được định dạng gọn gàng:

**names.py**

```python
from name_function import get_formatted_name

print("Enter 'q' at any time to quit.")
while True:
    first = input("\nPlease give me a first name: ")
    if first == 'q':
        break
    last = input("Please give me a last name: ")
    if last == 'q':
        break

    formatted_name = get_formatted_name(first, last)
    print("\tNeatly formatted name: " + formatted_name + '.')
```

Chương trình này import `get_formatted_name()` từ *name_function.py*. Người dùng có thể nhập một loạt tên và họ, và xem các họ tên đầy đủ đã được định dạng:

```text
Enter 'q' at any time to quit.

Please give me a first name: janis
Please give me a last name: joplin
        Neatly formatted name: Janis Joplin.

Please give me a first name: bob
Please give me a last name: dylan
        Neatly formatted name: Bob Dylan.

Please give me a first name: q
```

Ta có thể thấy những cái tên được tạo ra ở đây là đúng. Nhưng giả sử chúng ta muốn sửa `get_formatted_name()` để nó cũng xử lý được tên đệm. Khi làm vậy, ta muốn đảm bảo không làm hỏng cách hàm xử lý những cái tên chỉ có tên và họ. Ta có thể kiểm thử mã bằng cách chạy *names.py* và nhập một cái tên như `Janis Joplin` mỗi khi sửa `get_formatted_name()`, nhưng việc đó sẽ trở nên tẻ nhạt. May mắn thay, Python cung cấp một cách hiệu quả để tự động hóa việc kiểm thử đầu ra của một hàm. Nếu tự động hóa việc kiểm thử `get_formatted_name()`, ta luôn có thể tự tin rằng hàm sẽ hoạt động khi được cung cấp những loại tên mà ta đã viết kiểm thử.

<!-- pdf-page: 250 | printed: 217 -->

### Unit test và test case

Module `unittest` trong thư viện chuẩn của Python cung cấp các công cụ để kiểm thử mã. Một *unit test* (kiểm thử đơn vị) xác minh rằng một khía cạnh cụ thể trong hành vi của một hàm là đúng. Một *test case* là một tập hợp các unit test cùng nhau chứng minh rằng một hàm hoạt động đúng như mong đợi, trong toàn bộ phạm vi các tình huống mà bạn mong nó xử lý được. Một test case tốt xem xét mọi loại đầu vào có thể có mà một hàm có thể nhận, và có các bài kiểm thử đại diện cho từng tình huống này. Một test case có *độ bao phủ đầy đủ* (full coverage) gồm đủ các unit test bao quát mọi cách có thể dùng một hàm. Đạt được độ bao phủ đầy đủ trong một dự án lớn có thể là việc rất khó khăn. Thường thì chỉ cần viết kiểm thử cho những hành vi quan trọng của mã là đủ, và chỉ hướng tới độ bao phủ đầy đủ nếu dự án bắt đầu được sử dụng rộng rãi.

### Một bài kiểm thử thành công

Cú pháp để thiết lập một test case cần một thời gian để làm quen, nhưng một khi đã thiết lập xong test case, việc thêm các unit test cho hàm của bạn khá đơn giản. Để viết một test case cho một hàm, hãy import module `unittest` và hàm bạn muốn kiểm thử. Sau đó tạo một lớp kế thừa từ `unittest.TestCase`, và viết một loạt phương thức để kiểm thử các khía cạnh khác nhau trong hành vi của hàm.

Đây là một test case với một phương thức xác minh rằng hàm `get_formatted_name()` hoạt động đúng khi được cung cấp tên và họ:

**test_name_function.py**

```python
  import unittest
  from name_function import get_formatted_name

❶ class NamesTestCase(unittest.TestCase):
      """Tests for 'name_function.py'."""

      def test_first_last_name(self):
          """Do names like 'Janis Joplin' work?"""
❷         formatted_name = get_formatted_name('janis', 'joplin')
❸         self.assertEqual(formatted_name, 'Janis Joplin')

  unittest.main()
```

Đầu tiên, chúng ta import `unittest` và hàm muốn kiểm thử, `get_formatted_name()`. Tại ❶, ta tạo một lớp có tên `NamesTestCase`, lớp này sẽ chứa một loạt unit test cho `get_formatted_name()`. Bạn có thể đặt tên lớp tùy ý, nhưng tốt nhất là đặt một cái tên liên quan đến hàm sắp kiểm thử và dùng từ *Test* trong tên lớp. Lớp này phải kế thừa từ lớp `unittest.TestCase` để Python biết cách chạy các bài kiểm thử bạn viết.

<!-- pdf-page: 251 | printed: 218 -->

`NamesTestCase` chứa một phương thức duy nhất kiểm thử một khía cạnh của `get_formatted_name()`. Chúng ta đặt tên phương thức này là `test_first_last_name()` vì ta đang xác minh rằng những cái tên chỉ có tên và họ được định dạng đúng. Mọi phương thức bắt đầu bằng `test_` sẽ được chạy tự động khi ta chạy *test_name_function.py*. Bên trong phương thức kiểm thử này, ta gọi hàm muốn kiểm thử và lưu giá trị trả về mà ta quan tâm. Trong ví dụ này, ta gọi `get_formatted_name()` với các đối số `'janis'` và `'joplin'`, và lưu kết quả vào `formatted_name` ❷.

Tại ❸, chúng ta dùng một trong những tính năng hữu ích nhất của `unittest`: một phương thức *assert* (khẳng định). Các phương thức assert xác minh rằng kết quả bạn nhận được khớp với kết quả bạn mong đợi. Trong trường hợp này, vì biết `get_formatted_name()` phải trả về một họ tên đầy đủ được viết hoa và có khoảng cách đúng, ta mong đợi giá trị trong `formatted_name` là `Janis Joplin`. Để kiểm tra điều này có đúng không, ta dùng phương thức `assertEqual()` của `unittest` và truyền cho nó `formatted_name` và `'Janis Joplin'`. Dòng

```text
self.assertEqual(formatted_name, 'Janis Joplin')
```

có nghĩa là: “Hãy so sánh giá trị trong `formatted_name` với chuỗi `'Janis Joplin'`. Nếu chúng bằng nhau như mong đợi, tốt. Nhưng nếu chúng không khớp, hãy báo cho tôi biết!”

Dòng `unittest.main()` yêu cầu Python chạy các bài kiểm thử trong file này. Khi chạy *test_name_function.py*, chúng ta nhận được đầu ra sau:

```text
.
----------------------------------------------------------------------
Ran 1 test in 0.000s

OK
```

Dấu chấm ở dòng đầu tiên của đầu ra cho ta biết có một bài kiểm thử đã thành công. Dòng tiếp theo cho biết Python đã chạy một bài kiểm thử, và mất chưa đến 0,001 giây để chạy. Chữ `OK` cuối cùng cho ta biết tất cả các unit test trong test case đều đã thành công.

Đầu ra này cho thấy hàm `get_formatted_name()` sẽ luôn hoạt động với những cái tên có tên và họ, trừ khi ta sửa đổi hàm. Khi sửa `get_formatted_name()`, ta có thể chạy lại bài kiểm thử này. Nếu test case thành công, ta biết hàm vẫn sẽ hoạt động với những cái tên như Janis Joplin.

### Một bài kiểm thử thất bại

Một bài kiểm thử thất bại trông như thế nào? Hãy sửa `get_formatted_name()` để nó có thể xử lý tên đệm, nhưng ta sẽ làm theo cách làm hỏng hàm đối với những cái tên chỉ có tên và họ, như Janis Joplin.

<!-- pdf-page: 252 | printed: 219 -->

Đây là phiên bản mới của `get_formatted_name()` yêu cầu một đối số tên đệm:

**name_function.py**

```python
def get_formatted_name(first, middle, last):
    """Generate a neatly formatted full name."""
    full_name = first + ' ' + middle + ' ' + last
    return full_name.title()
```

Phiên bản này lẽ ra sẽ hoạt động với những người có tên đệm, nhưng khi kiểm thử, ta thấy mình đã làm hỏng hàm đối với những người chỉ có tên và họ. Lần này, chạy file *test_name_function.py* cho ra đầu ra sau:

```python
❶ E
  ======================================================================
❷ ERROR: test_first_last_name (__main__.NamesTestCase)
  ----------------------------------------------------------------------
❸ Traceback (most recent call last):
    File "test_name_function.py", line 8, in test_first_last_name
      formatted_name = get_formatted_name('janis', 'joplin')
  TypeError: get_formatted_name() missing 1 required positional argument: 'last'

  ----------------------------------------------------------------------
❹ Ran 1 test in 0.000s

❺ FAILED (errors=1)
```

Có rất nhiều thông tin ở đây vì có nhiều điều bạn có thể cần biết khi một bài kiểm thử thất bại. Mục đầu tiên trong đầu ra là một chữ `E` ❶, cho ta biết một unit test trong test case đã gây ra lỗi. Tiếp theo, ta thấy `test_first_last_name()` trong `NamesTestCase` đã gây ra lỗi ❷. Biết bài kiểm thử nào thất bại là điều cực kỳ quan trọng khi test case của bạn chứa nhiều unit test. Tại ❸, ta thấy một traceback tiêu chuẩn, báo rằng lời gọi hàm `get_formatted_name('janis', 'joplin')` không còn hoạt động nữa vì thiếu một đối số vị trí bắt buộc.

Chúng ta cũng thấy rằng một unit test đã được chạy ❹. Cuối cùng, ta thấy thêm một thông báo cho biết toàn bộ test case đã thất bại và một lỗi đã xảy ra khi chạy test case ❺. Thông tin này xuất hiện ở cuối đầu ra để bạn thấy ngay; bạn sẽ không muốn phải cuộn ngược qua cả một danh sách đầu ra dài để biết có bao nhiêu bài kiểm thử thất bại.

### Phản hồi một bài kiểm thử thất bại

Bạn làm gì khi một bài kiểm thử thất bại? Giả sử bạn đang kiểm tra đúng các điều kiện, một bài kiểm thử thành công nghĩa là hàm đang hoạt động đúng, còn một bài kiểm thử thất bại nghĩa là có lỗi trong đoạn mã mới bạn viết. Vì vậy, khi một bài kiểm thử thất bại, đừng thay đổi bài kiểm thử. Thay vào đó, hãy sửa đoạn mã khiến bài kiểm thử thất bại. Hãy xem xét những thay đổi bạn vừa thực hiện với hàm, và tìm hiểu xem những thay đổi đó đã làm hỏng hành vi mong muốn như thế nào.

<!-- pdf-page: 253 | printed: 220 -->

Trong trường hợp này, `get_formatted_name()` trước đây chỉ yêu cầu hai tham số: tên và họ. Giờ nó yêu cầu tên, tên đệm và họ. Việc thêm tham số tên đệm bắt buộc đó đã làm hỏng hành vi mong muốn của `get_formatted_name()`. Lựa chọn tốt nhất ở đây là làm cho tên đệm trở thành tùy chọn. Khi làm vậy, bài kiểm thử của ta cho những cái tên như `Janis Joplin` sẽ lại thành công, và ta cũng có thể nhận tên đệm. Hãy sửa `get_formatted_name()` để tên đệm là tùy chọn rồi chạy lại test case. Nếu nó thành công, ta sẽ chuyển sang đảm bảo hàm xử lý đúng tên đệm.

Để làm cho tên đệm trở thành tùy chọn, chúng ta chuyển tham số `middle` xuống cuối danh sách tham số trong định nghĩa hàm và cho nó một giá trị mặc định rỗng. Ta cũng thêm một phép kiểm tra `if` để tạo họ tên đầy đủ cho đúng, tùy thuộc vào việc tên đệm có được cung cấp hay không:

**name_function.py**

```python
def get_formatted_name(first, last, middle=''):
    """Generate a neatly formatted full name."""
    if middle:
        full_name = first + ' ' + middle + ' ' + last
    else:
        full_name = first + ' ' + last
    return full_name.title()
```

Trong phiên bản mới này của `get_formatted_name()`, tên đệm là tùy chọn. Nếu tên đệm được truyền cho hàm (`if middle:`), họ tên đầy đủ sẽ gồm tên, tên đệm và họ. Ngược lại, họ tên đầy đủ sẽ chỉ gồm tên và họ. Giờ hàm sẽ hoạt động với cả hai loại tên. Để biết hàm có còn hoạt động với những cái tên như `Janis Joplin` không, hãy chạy lại *test_name_function.py*:

```text
.
----------------------------------------------------------------------
Ran 1 test in 0.000s

OK
```

Giờ test case đã thành công. Đây là điều lý tưởng; nó có nghĩa là hàm lại hoạt động với những cái tên như `Janis Joplin` mà ta không phải kiểm thử hàm bằng tay. Việc sửa hàm thật dễ dàng vì bài kiểm thử thất bại đã giúp ta xác định đoạn mã mới làm hỏng hành vi hiện có.

<!-- pdf-page: 254 | printed: 221 -->

### Thêm bài kiểm thử mới

Giờ khi đã biết `get_formatted_name()` lại hoạt động với những cái tên đơn giản, hãy viết bài kiểm thử thứ hai cho những người có tên đệm. Chúng ta làm điều này bằng cách thêm một phương thức khác vào lớp `NamesTestCase`:

```python
  import unittest
  from name_function import get_formatted_name

  class NamesTestCase(unittest.TestCase):
      """Tests for 'name_function.py'."""

      def test_first_last_name(self):
          """Do names like 'Janis Joplin' work?"""
          formatted_name = get_formatted_name('janis', 'joplin')
          self.assertEqual(formatted_name, 'Janis Joplin')

      def test_first_last_middle_name(self):
          """Do names like 'Wolfgang Amadeus Mozart' work?"""
❶         formatted_name = get_formatted_name(
              'wolfgang', 'mozart', 'amadeus')
          self.assertEqual(formatted_name, 'Wolfgang Amadeus Mozart')

  unittest.main()
```

Chúng ta đặt tên phương thức mới này là `test_first_last_middle_name()`. Tên phương thức phải bắt đầu bằng *test_* để phương thức được chạy tự động khi ta chạy *test_name_function.py*. Ta đặt tên phương thức sao cho rõ ràng hành vi nào của `get_formatted_name()` đang được kiểm thử. Nhờ đó, nếu bài kiểm thử thất bại, ta biết ngay những loại tên nào bị ảnh hưởng. Các phương thức trong lớp `TestCase` có tên dài cũng không sao. Chúng cần mang tính mô tả để bạn hiểu được đầu ra khi các bài kiểm thử thất bại, và vì Python tự động gọi chúng, bạn sẽ không bao giờ phải viết mã gọi những phương thức này.

Để kiểm thử hàm, chúng ta gọi `get_formatted_name()` với tên, họ và tên đệm ❶, rồi dùng `assertEqual()` để kiểm tra xem họ tên đầy đủ được trả về có khớp với họ tên đầy đủ (tên, tên đệm và họ) mà ta mong đợi không. Khi chạy lại *test_name_function.py*, cả hai bài kiểm thử đều thành công:

```text
..
----------------------------------------------------------------------
Ran 2 tests in 0.000s

OK
```

Tuyệt vời! Giờ chúng ta biết rằng hàm vẫn hoạt động với những cái tên như `Janis Joplin`, và có thể tự tin rằng nó cũng sẽ hoạt động với những cái tên như `Wolfgang Amadeus Mozart`.

<!-- pdf-page: 255 | printed: 222 -->

<!-- box -->

**Tự mình thực hành**

**11-1. Thành phố, Quốc gia:** Viết một hàm nhận hai tham số: tên một thành phố và tên một quốc gia. Hàm nên trả về một chuỗi duy nhất có dạng `City, Country`, chẳng hạn `Santiago, Chile`. Lưu hàm trong một module có tên *city_functions.py*.

Tạo một file có tên *test_cities.py* để kiểm thử hàm bạn vừa viết (hãy nhớ rằng bạn cần import `unittest` và hàm muốn kiểm thử). Viết một phương thức có tên `test_city_country()` để xác minh rằng việc gọi hàm với các giá trị như `'santiago'` và `'chile'` cho ra chuỗi đúng. Chạy *test_cities.py*, và đảm bảo `test_city_country()` thành công.

**11-2. Dân số:** Sửa hàm của bạn để nó yêu cầu thêm tham số thứ ba, `population`. Giờ nó nên trả về một chuỗi duy nhất có dạng `City, Country – population xxx`, chẳng hạn `Santiago, Chile – population 5000000`. Chạy lại *test_cities.py*. Đảm bảo lần này `test_city_country()` thất bại.

Sửa hàm để tham số `population` là tùy chọn. Chạy lại *test_cities.py*, và đảm bảo `test_city_country()` lại thành công.

Viết bài kiểm thử thứ hai có tên `test_city_country_population()` để xác minh rằng bạn có thể gọi hàm với các giá trị `'santiago'`, `'chile'` và `'population=5000000'`. Chạy lại *test_cities.py*, và đảm bảo bài kiểm thử mới này thành công.

<!-- /box -->

## Kiểm thử một lớp

Trong phần đầu của chương này, bạn đã viết kiểm thử cho một hàm đơn lẻ. Giờ bạn sẽ viết kiểm thử cho một lớp. Bạn sẽ dùng lớp trong nhiều chương trình của mình, nên việc có thể chứng minh các lớp của bạn hoạt động đúng là rất hữu ích. Nếu có những bài kiểm thử thành công cho một lớp đang làm, bạn có thể tự tin rằng những cải tiến bạn thực hiện với lớp đó sẽ không vô tình làm hỏng hành vi hiện tại của nó.

### Các phương thức assert đa dạng

Python cung cấp một số phương thức assert trong lớp `unittest.TestCase`. Như đã đề cập trước đó, các phương thức assert kiểm tra xem một điều kiện mà bạn tin là đúng tại một điểm cụ thể trong mã có thực sự đúng hay không. Nếu điều kiện đúng như mong đợi, giả định của bạn về cách phần đó của chương trình hoạt động được xác nhận; bạn có thể tự tin rằng không có lỗi nào tồn tại. Nếu điều kiện mà bạn cho là đúng thực ra lại không đúng, Python sẽ phát sinh một ngoại lệ.

Bảng 11-1 mô tả sáu phương thức assert thường dùng. Với các phương thức này, bạn có thể xác minh rằng các giá trị trả về bằng hoặc không bằng các giá trị mong đợi, rằng các giá trị là `True` hoặc `False`, và rằng các giá trị nằm trong (`in`) hoặc không nằm trong (`not in`) một list cho trước. Bạn chỉ có thể dùng các phương thức này trong một lớp kế thừa từ `unittest.TestCase`, vậy hãy xem cách dùng một trong các phương thức này trong bối cảnh kiểm thử một lớp thực sự.

<!-- pdf-page: 256 | printed: 223 -->

*Bảng 11-1: Các phương thức assert có trong module `unittest`*

| **Phương thức** | **Công dụng** |
|---|---|
| `assertEqual(a, b)` | Xác minh rằng `a == b` |
| `assertNotEqual(a, b)` | Xác minh rằng `a != b` |
| `assertTrue(x)` | Xác minh rằng `x` là `True` |
| `assertFalse(x)` | Xác minh rằng `x` là `False` |
| `assertIn(item, list)` | Xác minh rằng `item` nằm trong `list` |
| `assertNotIn(item, list)` | Xác minh rằng `item` không nằm trong `list` |

### Một lớp để kiểm thử

Kiểm thử một lớp tương tự như kiểm thử một hàm — phần lớn công việc của bạn là kiểm thử hành vi của các phương thức trong lớp. Nhưng có một vài điểm khác biệt, vậy hãy viết một lớp để kiểm thử. Hãy xét một lớp giúp quản lý các cuộc khảo sát ẩn danh:

**survey.py**

```python
  class AnonymousSurvey():
      """Collect anonymous answers to a survey question."""

❶     def __init__(self, question):
          """Store a question, and prepare to store responses."""
          self.question = question
          self.responses = []

❷     def show_question(self):
          """Show the survey question."""
          print(question)

❸     def store_response(self, new_response):
          """Store a single response to the survey."""
          self.responses.append(new_response)

❹     def show_results(self):
          """Show all the responses that have been given."""
          print("Survey results:")
          for response in responses:
              print('- ' + response)
```

Lớp này bắt đầu với một câu hỏi khảo sát do bạn cung cấp ❶ và có một list rỗng để lưu các câu trả lời. Lớp có các phương thức để in câu hỏi khảo sát ❷, thêm một câu trả lời mới vào list câu trả lời ❸, và in tất cả các câu trả lời được lưu trong list ❹. Để tạo một thực thể từ lớp này, tất cả những gì bạn phải cung cấp là một câu hỏi. Khi đã có một thực thể biểu diễn một cuộc khảo sát cụ thể, bạn hiển thị câu hỏi khảo sát bằng `show_question()`, lưu một câu trả lời bằng `store_response()`, và hiển thị kết quả bằng `show_results()`.

<!-- pdf-page: 257 | printed: 224 -->

Để cho thấy lớp `AnonymousSurvey` hoạt động, hãy viết một chương trình dùng lớp này:

**language_survey.py**

```python
from survey import AnonymousSurvey
# Define a question, and make a survey.
question = "What language did you first learn to speak?"
my_survey = AnonymousSurvey(question)

# Show the question, and store responses to the question.
my_survey.show_question()
print("Enter 'q' at any time to quit.\n")
while True:
    response = input("Language: ")
    if response == 'q':
        break
    my_survey.store_response(response)

# Show the survey results.
print("\nThank you to everyone who participated in the survey!")
my_survey.show_results()
```

Chương trình này định nghĩa một câu hỏi (`"What language did you first learn to speak?"`) và tạo một đối tượng `AnonymousSurvey` với câu hỏi đó. Chương trình gọi `show_question()` để hiển thị câu hỏi rồi yêu cầu nhập câu trả lời. Mỗi câu trả lời được lưu ngay khi nhận được. Khi tất cả câu trả lời đã được nhập (người dùng nhập `q` để thoát), `show_results()` in ra kết quả khảo sát:

```text
What language did you first learn to speak?
Enter 'q' at any time to quit.

Language: English
Language: Spanish
Language: English
Language: Mandarin
Language: q

Thank you to everyone who participated in the survey!
Survey results:
- English
- Spanish
- English
- Mandarin
```

<!-- pdf-page: 258 | printed: 225 -->

Lớp này hoạt động tốt cho một cuộc khảo sát ẩn danh đơn giản. Nhưng giả sử chúng ta muốn cải tiến `AnonymousSurvey` và module chứa nó, `survey`. Ta có thể cho phép mỗi người dùng nhập nhiều hơn một câu trả lời. Ta có thể viết một phương thức chỉ liệt kê những câu trả lời duy nhất và báo cáo mỗi câu trả lời được đưa ra bao nhiêu lần. Ta có thể viết một lớp khác để quản lý các cuộc khảo sát không ẩn danh.

Thực hiện những thay đổi như vậy có nguy cơ ảnh hưởng đến hành vi hiện tại của lớp `AnonymousSurvey`. Ví dụ, có thể trong khi cố cho phép mỗi người dùng nhập nhiều câu trả lời, ta lại vô tình thay đổi cách xử lý các câu trả lời đơn lẻ. Để đảm bảo không làm hỏng hành vi hiện có trong khi phát triển module này, ta có thể viết kiểm thử cho lớp.

### Kiểm thử lớp AnonymousSurvey

Hãy viết một bài kiểm thử xác minh một khía cạnh trong cách `AnonymousSurvey` hoạt động. Chúng ta sẽ viết một bài kiểm thử để xác minh rằng một câu trả lời đơn lẻ cho câu hỏi khảo sát được lưu đúng. Ta sẽ dùng phương thức `assertIn()` để xác minh rằng câu trả lời nằm trong list câu trả lời sau khi đã được lưu:

**test_survey.py**

```python
  import unittest
  from survey import AnonymousSurvey

❶ class TestAnonmyousSurvey(unittest.TestCase):
      """Tests for the class AnonymousSurvey"""

❷     def test_store_single_response(self):
          """Test that a single response is stored properly."""
          question = "What language did you first learn to speak?"
❸         my_survey = AnonymousSurvey(question)
          my_survey.store_response('English')

❹         self.assertIn('English', my_survey.responses)

  unittest.main()
```

Chúng ta bắt đầu bằng việc import module `unittest` và lớp muốn kiểm thử, `AnonymousSurvey`. Ta đặt tên test case là `TestAnonymousSurvey`, một lần nữa kế thừa từ `unittest.TestCase` ❶. Phương thức kiểm thử đầu tiên sẽ xác minh rằng khi ta lưu một câu trả lời cho câu hỏi khảo sát, câu trả lời đó sẽ có mặt trong list câu trả lời của cuộc khảo sát. Một cái tên mô tả tốt cho phương thức này là `test_store_single_response()` ❷. Nếu bài kiểm thử này thất bại, nhờ tên phương thức hiển thị trong đầu ra của bài kiểm thử thất bại, ta sẽ biết có vấn đề khi lưu một câu trả lời đơn lẻ cho cuộc khảo sát.

Để kiểm thử hành vi của một lớp, chúng ta cần tạo một thực thể của lớp đó. Tại ❸, ta tạo một thực thể có tên `my_survey` với câu hỏi `"What language did you first learn to speak?"` Ta lưu một câu trả lời đơn lẻ, `English`, bằng phương thức `store_response()`. Sau đó, ta xác minh rằng câu trả lời đã được lưu đúng bằng cách khẳng định rằng `English` nằm trong list `my_survey.responses` ❹.

<!-- pdf-page: 259 | printed: 226 -->

Khi chạy *test_survey.py*, bài kiểm thử thành công:

```text
.
----------------------------------------------------------------------
Ran 1 test in 0.001s

OK
```

Điều này tốt, nhưng một cuộc khảo sát chỉ hữu ích nếu nó thu được nhiều hơn một câu trả lời. Hãy xác minh rằng ba câu trả lời có thể được lưu đúng. Để làm điều này, chúng ta thêm một phương thức khác vào `TestAnonymousSurvey`:

```python
  import unittest
  from survey import AnonymousSurvey

  class TestAnonymousSurvey(unittest.TestCase):
      """Tests for the class AnonymousSurvey"""

      def test_store_single_response(self):
          """Test that a single response is stored properly."""
          --snip--

      def test_store_three_responses(self):
          """Test that three individual responses are stored properly."""
          question = "What language did you first learn to speak?"
          my_survey = AnonymousSurvey(question)
❶         responses = ['English', 'Spanish', 'Mandarin']
          for response in responses:
              my_survey.store_response(response)

❷         for response in responses:
              self.assertIn(response, my_survey.responses)

  unittest.main()
```

Chúng ta đặt tên phương thức mới là `test_store_three_responses()`. Ta tạo một đối tượng khảo sát giống như đã làm trong `test_store_single_response()`. Ta định nghĩa một list chứa ba câu trả lời khác nhau ❶, rồi gọi `store_response()` cho từng câu trả lời này. Khi các câu trả lời đã được lưu, ta viết một vòng lặp khác và khẳng định rằng mỗi câu trả lời giờ đều nằm trong `my_survey.responses` ❷.

Khi chạy lại *test_survey.py*, cả hai bài kiểm thử (cho một câu trả lời và cho ba câu trả lời) đều thành công:

```text
..
----------------------------------------------------------------------
Ran 2 tests in 0.000s

OK
```

Mọi thứ hoạt động hoàn hảo. Tuy nhiên, các bài kiểm thử này hơi lặp lại, nên chúng ta sẽ dùng một tính năng khác của `unittest` để làm cho chúng hiệu quả hơn.

<!-- pdf-page: 260 | printed: 227 -->

### Phương thức setUp()

Trong *test_survey.py*, chúng ta đã tạo một thực thể mới của `AnonymousSurvey` trong mỗi phương thức kiểm thử, và tạo các câu trả lời mới trong mỗi phương thức. Lớp `unittest.TestCase` có một phương thức `setUp()` cho phép bạn tạo các đối tượng này một lần rồi dùng chúng trong mỗi phương thức kiểm thử. Khi bạn đưa một phương thức `setUp()` vào một lớp `TestCase`, Python chạy phương thức `setUp()` trước khi chạy mỗi phương thức bắt đầu bằng *test_*. Mọi đối tượng được tạo trong phương thức `setUp()` sau đó đều có thể dùng trong mỗi phương thức kiểm thử mà bạn viết.

Hãy dùng `setUp()` để tạo một thực thể khảo sát và một tập câu trả lời có thể được dùng trong `test_store_single_response()` và `test_store_three_responses()`:

```python
  import unittest
  from survey import AnonymousSurvey

  class TestAnonymousSurvey(unittest.TestCase):
      """Tests for the class AnonymousSurvey."""

      def setUp(self):
          """
          Create a survey and a set of responses for use in all test methods.
          """
          question = "What language did you first learn to speak?"
❶         self.my_survey = AnonymousSurvey(question)
❷         self.responses = ['English', 'Spanish', 'Mandarin']

      def test_store_single_response(self):
          """Test that a single response is stored properly."""
          self.my_survey.store_response(self.responses[0])
          self.assertIn(self.responses[0], self.my_survey.responses)

      def test_store_three_responses(self):
          """Test that three individual responses are stored properly."""
          for response in self.responses:
              self.my_survey.store_response(response)
          for response in self.responses:
              self.assertIn(response, self.my_survey.responses)

  unittest.main()
```

Phương thức `setUp()` làm hai việc: nó tạo một thực thể khảo sát ❶, và tạo một list câu trả lời ❷. Mỗi thứ đều có tiền tố `self`, nên chúng có thể được dùng ở bất cứ đâu trong lớp. Điều này giúp hai phương thức kiểm thử đơn giản hơn, vì không phương thức nào phải tạo thực thể khảo sát hay câu trả lời. Phương thức `test_store_single_response()` xác minh rằng câu trả lời đầu tiên trong `self.responses` — `self.responses[0]` — có thể được lưu đúng, và `test_store_single_response()` xác minh rằng cả ba câu trả lời trong `self.responses` đều có thể được lưu đúng.

Khi chạy lại *test_survey.py*, cả hai bài kiểm thử vẫn thành công. Những bài kiểm thử này sẽ đặc biệt hữu ích khi bạn cố mở rộng `AnonymousSurvey` để xử lý nhiều câu trả lời cho mỗi người. Sau khi sửa mã để nhận nhiều câu trả lời, bạn có thể chạy các bài kiểm thử này và đảm bảo mình không làm ảnh hưởng đến khả năng lưu một câu trả lời đơn lẻ hoặc một loạt câu trả lời riêng lẻ.

<!-- pdf-page: 261 | printed: 228 -->

Khi kiểm thử các lớp của riêng mình, phương thức `setUp()` có thể giúp việc viết các phương thức kiểm thử dễ dàng hơn. Bạn tạo một tập thực thể và thuộc tính trong `setUp()`, rồi dùng các thực thể này trong tất cả các phương thức kiểm thử. Cách này dễ dàng hơn nhiều so với việc tạo một tập thực thể và thuộc tính mới trong mỗi phương thức kiểm thử.

> **Lưu ý** Khi một test case đang chạy, Python in ra một ký tự cho mỗi unit test khi nó hoàn thành. Một bài kiểm thử thành công in ra một dấu chấm, một bài kiểm thử gây ra lỗi in ra chữ `E`, và một bài kiểm thử có phép khẳng định thất bại in ra chữ `F`. Đó là lý do bạn sẽ thấy số lượng dấu chấm và ký tự khác nhau ở dòng đầu tiên của đầu ra khi chạy các test case. Nếu một test case mất nhiều thời gian để chạy vì chứa nhiều unit test, bạn có thể theo dõi các kết quả này để biết có bao nhiêu bài kiểm thử đang thành công.

<!-- box -->

**Tự mình thực hành**

**11-3. Nhân viên:** Viết một lớp có tên `Employee`. Phương thức `__init__()` nên nhận vào tên, họ và mức lương hằng năm, và lưu từng thông tin này thành thuộc tính. Viết một phương thức có tên `give_raise()` mặc định cộng thêm $5000 vào mức lương hằng năm, nhưng cũng chấp nhận một mức tăng lương khác.

Viết một test case cho `Employee`. Viết hai phương thức kiểm thử, `test_give_default_raise()` và `test_give_custom_raise()`. Dùng phương thức `setUp()` để bạn không phải tạo một thực thể nhân viên mới trong mỗi phương thức kiểm thử. Chạy test case của bạn, và đảm bảo cả hai bài kiểm thử đều thành công.

<!-- /box -->

## Tổng kết

Trong chương này, bạn đã học cách viết kiểm thử cho hàm và lớp bằng các công cụ trong module `unittest`. Bạn đã học cách viết một lớp kế thừa từ `unittest.TestCase`, và học cách viết các phương thức kiểm thử xác minh những hành vi cụ thể mà hàm và lớp của bạn phải thể hiện. Bạn đã học cách dùng phương thức `setUp()` để tạo một cách hiệu quả các thực thể và thuộc tính từ lớp của mình, có thể được dùng trong tất cả các phương thức kiểm thử của một lớp.

Kiểm thử là một chủ đề quan trọng mà nhiều người mới bắt đầu không học. Bạn không cần viết kiểm thử cho mọi dự án đơn giản mà mình thử làm khi mới bắt đầu. Nhưng ngay khi bắt đầu làm những dự án đòi hỏi công sức phát triển đáng kể, bạn nên kiểm thử những hành vi quan trọng của hàm và lớp. Bạn sẽ tự tin hơn rằng công việc mới trong dự án sẽ không làm hỏng những phần đang hoạt động, và điều này cho bạn sự tự do để cải tiến mã. Nếu vô tình làm hỏng chức năng hiện có, bạn sẽ biết ngay, nên vẫn có thể dễ dàng sửa vấn đề. Phản hồi một bài kiểm thử thất bại mà bạn đã chạy dễ dàng hơn nhiều so với phản hồi một báo cáo lỗi từ một người dùng không hài lòng.

<!-- pdf-page: 262 | printed: 229 -->

Các lập trình viên khác sẽ đánh giá cao dự án của bạn hơn nếu bạn có đưa vào một số bài kiểm thử ban đầu. Họ sẽ cảm thấy thoải mái hơn khi thử nghiệm với mã của bạn và sẵn lòng hơn khi cùng bạn làm dự án. Nếu bạn muốn đóng góp vào một dự án mà các lập trình viên khác đang thực hiện, bạn sẽ được kỳ vọng chứng minh rằng mã của mình vượt qua các bài kiểm thử hiện có, và thường sẽ được kỳ vọng viết kiểm thử cho những hành vi mới mà bạn đưa vào dự án.

Hãy thử nghiệm với kiểm thử để làm quen với quy trình kiểm thử mã của bạn. Hãy viết kiểm thử cho những hành vi quan trọng nhất của hàm và lớp, nhưng đừng đặt mục tiêu bao phủ đầy đủ trong những dự án đầu tiên trừ khi bạn có lý do cụ thể để làm vậy.

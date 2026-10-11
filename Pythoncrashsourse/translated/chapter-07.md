<!-- source: pythoncrashcourse.pdf | unit: chapter-07 | pdf pages 150-165 | printed 117-132 -->

# Chương 7: Đầu vào của người dùng và vòng lặp while

<!-- pdf-page: 150 | printed: 117 -->

Hầu hết các chương trình được viết ra để giải quyết vấn đề của người dùng cuối. Để làm được điều đó, bạn thường cần lấy một số thông tin từ người dùng. Lấy một ví dụ đơn giản: giả sử ai đó muốn biết mình đã đủ tuổi đi bầu cử chưa. Nếu bạn viết một

chương trình để trả lời câu hỏi này, bạn cần biết tuổi của người dùng trước khi có thể đưa ra câu trả lời. Chương trình sẽ cần yêu cầu người dùng nhập, hay cung cấp *đầu vào* (input), là tuổi của họ; khi đã có đầu vào này, chương trình có thể so sánh nó với độ tuổi được đi bầu cử để xác định người dùng đã đủ tuổi chưa, rồi báo lại kết quả.

Trong chương này, bạn sẽ học cách nhận đầu vào từ người dùng để chương trình có thể làm việc với nó. Khi chương trình cần một cái tên, bạn sẽ có thể yêu cầu người dùng nhập tên. Khi chương trình cần một list tên, bạn sẽ có thể yêu cầu người dùng nhập một loạt tên. Để làm điều này, bạn sẽ dùng hàm `input()`.

Bạn cũng sẽ học cách giữ cho chương trình tiếp tục chạy chừng nào người dùng còn muốn, để họ có thể nhập bao nhiêu thông tin tùy theo nhu cầu; sau đó, chương trình của bạn có thể làm việc với thông tin đó. Bạn sẽ dùng vòng lặp `while` của Python để giữ cho chương trình tiếp tục chạy chừng nào những điều kiện nhất định vẫn còn đúng.

<!-- pdf-page: 151 | printed: 118 -->

Với khả năng làm việc với đầu vào của người dùng và khả năng kiểm soát thời gian chạy của chương trình, bạn sẽ có thể viết những chương trình tương tác hoàn chỉnh.

## Hàm input() hoạt động như thế nào

Hàm `input()` tạm dừng chương trình và chờ người dùng nhập một đoạn văn bản. Khi Python nhận được đầu vào của người dùng, nó lưu đầu vào đó vào một biến để bạn tiện làm việc.

Ví dụ, chương trình sau yêu cầu người dùng nhập một đoạn văn bản, rồi hiển thị lại thông điệp đó cho người dùng:

**parrot.py**

```python
message = input("Tell me something, and I will repeat it back to you: ")
print(message)
```

Hàm `input()` nhận một đối số: *lời nhắc* (prompt), hay chỉ dẫn, mà chúng ta muốn hiển thị cho người dùng để họ biết phải làm gì. Trong ví dụ này, khi Python chạy dòng đầu tiên, người dùng thấy lời nhắc `Tell me something, and I will repeat it back to you:` . Chương trình chờ trong khi người dùng nhập câu trả lời và tiếp tục chạy sau khi người dùng nhấn ENTER. Câu trả lời được lưu vào biến `message`, rồi `print(message)` hiển thị lại đầu vào đó cho người dùng:

```text
Tell me something, and I will repeat it back to you: Hello everyone!
Hello everyone!
```

> **Lưu ý** Sublime Text không chạy được các chương trình yêu cầu người dùng nhập đầu vào. Bạn có thể dùng Sublime Text để viết các chương trình yêu cầu nhập đầu vào, nhưng bạn sẽ cần chạy những chương trình này từ terminal. Xem mục “Chạy chương trình Python từ terminal” ở trang 16.

### Viết lời nhắc rõ ràng

Mỗi khi dùng hàm `input()`, bạn nên đưa vào một lời nhắc rõ ràng, dễ làm theo, cho người dùng biết chính xác bạn đang cần loại thông tin gì. Bất kỳ câu nào cho người dùng biết cần nhập gì đều được. Ví dụ:

**greeter.py**

```python
name = input("Please enter your name: ")
print("Hello, " + name + "!")
```

Hãy thêm một dấu cách vào cuối lời nhắc (sau dấu hai chấm trong ví dụ trên) để tách lời nhắc khỏi câu trả lời của người dùng và giúp người dùng thấy rõ chỗ cần nhập văn bản. Ví dụ:

```text
Please enter your name: Eric
Hello, Eric!
```

Đôi khi bạn sẽ muốn viết một lời nhắc dài hơn một dòng. Ví dụ, bạn có thể muốn cho người dùng biết vì sao bạn yêu cầu một đầu vào nào đó. Bạn có thể lưu lời nhắc vào một biến và truyền biến đó cho hàm `input()`. Cách này cho phép bạn xây dựng lời nhắc qua nhiều dòng, rồi viết một câu lệnh `input()` gọn gàng.

<!-- pdf-page: 152 | printed: 119 -->

**greeter.py**

```python
prompt = "If you tell us who you are, we can personalize the messages you see."
prompt += "\nWhat is your first name? "

name = input(prompt)
print("\nHello, " + name + "!")
```

Ví dụ này cho thấy một cách tạo chuỗi nhiều dòng. Dòng đầu tiên lưu phần đầu của thông điệp vào biến `prompt`. Ở dòng thứ hai, toán tử `+=` lấy chuỗi đã được lưu trong `prompt` và nối thêm chuỗi mới vào cuối.

Giờ lời nhắc trải dài trên hai dòng, và một lần nữa có dấu cách sau dấu chấm hỏi cho rõ ràng:

```text
If you tell us who you are, we can personalize the messages you see.
What is your first name? Eric

Hello, Eric!
```

### Dùng int() để nhận đầu vào dạng số

Khi bạn dùng hàm `input()`, Python hiểu mọi thứ người dùng nhập vào là một chuỗi. Hãy xem phiên làm việc với trình thông dịch sau, yêu cầu người dùng nhập tuổi:

```python
>>> age = input("How old are you? ")
How old are you? 21
>>> age
'21'
```

Người dùng nhập số 21, nhưng khi chúng ta hỏi Python giá trị của `age`, nó trả về `'21'`, dạng biểu diễn chuỗi của giá trị số đã nhập. Ta biết Python hiểu đầu vào là chuỗi vì con số giờ được đặt trong dấu nháy. Nếu bạn chỉ muốn in đầu vào ra thì điều này không sao. Nhưng nếu bạn cố dùng đầu vào như một con số, bạn sẽ gặp lỗi:

```python
  >>> age = input("How old are you? ")
  How old are you? 21
❶ >>> age >= 18
  Traceback (most recent call last):
    File "<stdin>", line 1, in <module>
❷ TypeError: unorderable types: str() >= int()
```

Khi bạn cố dùng đầu vào để thực hiện một phép so sánh số ❶, Python báo lỗi vì nó không thể so sánh một chuỗi với một số nguyên: chuỗi `'21'` được lưu trong `age` không thể được so sánh với giá trị số `18` ❷.

<!-- pdf-page: 153 | printed: 120 -->

Chúng ta có thể giải quyết vấn đề này bằng hàm `int()`, hàm yêu cầu Python coi đầu vào là một giá trị số. Hàm `int()` chuyển dạng biểu diễn chuỗi của một số thành dạng biểu diễn số, như sau:

```python
  >>> age = input("How old are you? ")
  How old are you? 21
❶ >>> age = int(age)
  >>> age >= 18
  True
```

Trong ví dụ này, khi chúng ta nhập `21` tại lời nhắc, Python hiểu con số đó là một chuỗi, nhưng giá trị sau đó được `int()` chuyển thành dạng biểu diễn số ❶. Giờ Python có thể chạy phép kiểm tra điều kiện: nó so sánh `age` (lúc này chứa giá trị số 21) với `18` để xem `age` có lớn hơn hoặc bằng 18 không. Phép kiểm tra này được đánh giá là `True`.

Bạn dùng hàm `int()` trong một chương trình thực tế như thế nào? Hãy xét một chương trình xác định xem một người có đủ cao để đi tàu lượn siêu tốc hay không:

**rollercoaster.py**

```python
height = input("How tall are you, in inches? ")
height = int(height)

if height >= 36:
    print("\nYou're tall enough to ride!")
else:
    print("\nYou'll be able to ride when you're a little older.")
```

Chương trình có thể so sánh `height` với `36` vì `height = int(height)` chuyển giá trị đầu vào thành dạng biểu diễn số trước khi phép so sánh được thực hiện. Nếu số được nhập lớn hơn hoặc bằng 36, chúng ta cho người dùng biết họ đã đủ cao:

```text
How tall are you, in inches? 71

You're tall enough to ride!
```

Khi dùng đầu vào dạng số để tính toán và so sánh, hãy nhớ chuyển giá trị đầu vào thành dạng biểu diễn số trước.

### Toán tử chia lấy dư

Một công cụ hữu ích khi làm việc với thông tin dạng số là *toán tử chia lấy dư* (modulo operator) (`%`), toán tử chia một số cho một số khác và trả về phần dư:

```python
>>> 4 % 3
1
>>> 5 % 3
2
>>> 6 % 3
0
>>> 7 % 3
1
```

<!-- pdf-page: 154 | printed: 121 -->

Toán tử chia lấy dư không cho bạn biết một số chứa được số kia bao nhiêu lần; nó chỉ cho bạn biết phần dư là bao nhiêu.

Khi một số chia hết cho một số khác, phần dư bằng 0, nên toán tử chia lấy dư luôn trả về 0. Bạn có thể dùng điều này để xác định một số là chẵn hay lẻ:

**even_or_odd.py**

```python
number = input("Enter a number, and I'll tell you if it's even or odd: ")
number = int(number)

if number % 2 == 0:
    print("\nThe number " + str(number) + " is even.")
else:
    print("\nThe number " + str(number) + " is odd.")
```

Số chẵn luôn chia hết cho hai, nên nếu phép chia lấy dư của một số cho hai bằng không (ở đây là `if number % 2 == 0`) thì số đó là số chẵn. Ngược lại, nó là số lẻ.

```text
Enter a number, and I'll tell you if it's even or odd: 42

The number 42 is even.
```

### Nhận đầu vào trong Python 2.7

Nếu bạn đang dùng Python 2.7, bạn nên dùng hàm `raw_input()` khi yêu cầu người dùng nhập đầu vào. Hàm này hiểu mọi đầu vào là chuỗi, giống như `input()` trong Python 3.

Python 2.7 cũng có hàm `input()`, nhưng hàm này hiểu đầu vào của người dùng là mã Python và cố chạy đầu vào đó. Tốt nhất thì bạn sẽ gặp lỗi do Python không hiểu đầu vào; tệ nhất thì bạn sẽ chạy đoạn mã mà mình không hề định chạy. Nếu bạn đang dùng Python 2.7, hãy dùng `raw_input()` thay vì `input()`.

<!-- box -->

**Tự mình thực hành**

**7-1. Thuê xe:** Viết một chương trình hỏi người dùng muốn thuê loại xe nào. In ra một thông điệp về chiếc xe đó, chẳng hạn như “Let me see if I can find you a Subaru.”

**7-2. Xếp chỗ ở nhà hàng:** Viết một chương trình hỏi người dùng nhóm ăn tối của họ có bao nhiêu người. Nếu câu trả lời lớn hơn tám, in ra thông điệp cho biết họ sẽ phải chờ bàn. Nếu không, thông báo rằng bàn của họ đã sẵn sàng.

**7-3. Bội số của mười:** Yêu cầu người dùng nhập một số, rồi cho biết số đó có phải là bội số của 10 hay không.

<!-- /box -->

<!-- pdf-page: 155 | printed: 122 -->

## Giới thiệu vòng lặp while

Vòng lặp `for` nhận một tập hợp phần tử và thực thi một khối mã một lần cho mỗi phần tử trong tập hợp đó. Ngược lại, vòng lặp `while` chạy chừng nào, hay *trong khi* (while), một điều kiện nhất định còn đúng.

### Vòng lặp while trong thực tế

Bạn có thể dùng vòng lặp `while` để đếm tăng dần qua một dãy số. Ví dụ, vòng lặp `while` sau đếm từ 1 đến 5:

**counting.py**

```python
current_number = 1
while current_number <= 5:
    print(current_number)
    current_number += 1
```

Ở dòng đầu tiên, chúng ta bắt đầu đếm từ 1 bằng cách gán giá trị của `current_number` là 1. Sau đó, vòng lặp `while` được thiết lập để tiếp tục chạy chừng nào giá trị của `current_number` còn nhỏ hơn hoặc bằng 5. Đoạn mã bên trong vòng lặp in ra giá trị của `current_number`, rồi cộng thêm 1 vào giá trị đó bằng `current_number += 1`. (Toán tử `+=` là cách viết tắt của `current_number = current_number + 1`.)

Python lặp lại vòng lặp chừng nào điều kiện `current_number <= 5` còn đúng. Vì 1 nhỏ hơn 5, Python in ra `1` rồi cộng thêm 1, khiến số hiện tại thành `2`. Vì 2 nhỏ hơn 5, Python in ra `2` và lại cộng thêm 1, khiến số hiện tại thành `3`, và cứ thế tiếp tục. Khi giá trị của `current_number` lớn hơn 5, vòng lặp ngừng chạy và chương trình kết thúc:

```text
1
2
3
4
5
```

Những chương trình bạn dùng hằng ngày rất có thể chứa vòng lặp `while`. Ví dụ, một trò chơi cần vòng lặp `while` để tiếp tục chạy chừng nào bạn còn muốn chơi, và để có thể dừng lại ngay khi bạn yêu cầu thoát. Chương trình sẽ chẳng còn thú vị nếu chúng tự dừng trước khi ta yêu cầu hoặc vẫn tiếp tục chạy ngay cả khi ta muốn thoát, vì vậy vòng lặp `while` khá hữu ích.

### Để người dùng chọn khi nào thoát

Chúng ta có thể làm cho chương trình *parrot.py* chạy chừng nào người dùng còn muốn bằng cách đặt phần lớn chương trình vào trong một vòng lặp `while`. Chúng ta sẽ định nghĩa một *giá trị thoát* (quit value), rồi giữ cho chương trình tiếp tục chạy chừng nào người dùng chưa nhập giá trị thoát:

**parrot.py**

```python
❶ prompt = "\nTell me something, and I will repeat it back to you:"
  prompt += "\nEnter 'quit' to end the program. "
❷ message = ""
❸ while message != 'quit':
      message = input(prompt)
      print(message)
```

<!-- pdf-page: 156 | printed: 123 -->

Tại ❶, chúng ta định nghĩa một lời nhắc cho người dùng biết hai lựa chọn của họ: nhập một thông điệp hoặc nhập giá trị thoát (trong trường hợp này là `'quit'`). Sau đó, ta tạo một biến `message` ❷ để lưu bất kỳ giá trị nào người dùng nhập vào. Ta định nghĩa `message` là một chuỗi rỗng, `""`, để Python có thứ gì đó để kiểm tra khi lần đầu tiên chạy đến dòng `while`. Lần đầu tiên chương trình chạy và Python đến câu lệnh `while`, nó cần so sánh giá trị của `message` với `'quit'`, nhưng người dùng chưa nhập đầu vào nào. Nếu Python không có gì để so sánh, nó sẽ không thể tiếp tục chạy chương trình. Để giải quyết vấn đề này, ta đảm bảo gán cho `message` một giá trị ban đầu. Dù chỉ là một chuỗi rỗng, nó vẫn có nghĩa đối với Python và cho phép Python thực hiện phép so sánh giúp vòng lặp `while` hoạt động. Vòng lặp `while` này ❸ chạy chừng nào giá trị của `message` còn khác `'quit'`.

Ở lần lặp đầu tiên, `message` chỉ là một chuỗi rỗng, nên Python đi vào vòng lặp. Tại `message = input(prompt)`, Python hiển thị lời nhắc và chờ người dùng nhập đầu vào. Bất cứ thứ gì họ nhập đều được lưu vào `message` và được in ra; sau đó, Python đánh giá lại điều kiện trong câu lệnh `while`. Chừng nào người dùng chưa nhập từ `'quit'`, lời nhắc lại được hiển thị và Python chờ thêm đầu vào. Khi người dùng cuối cùng nhập `'quit'`, Python ngừng thực thi vòng lặp `while` và chương trình kết thúc:

```text
Tell me something, and I will repeat it back to you:
Enter 'quit' to end the program. Hello everyone!
Hello everyone!

Tell me something, and I will repeat it back to you:
Enter 'quit' to end the program. Hello again.
Hello again.

Tell me something, and I will repeat it back to you:
Enter 'quit' to end the program. quit
quit
```

Chương trình này hoạt động tốt, chỉ có điều nó in ra từ `'quit'` như thể đó là một thông điệp thực sự. Một phép kiểm tra `if` đơn giản sẽ khắc phục điều này:

```python
prompt = "\nTell me something, and I will repeat it back to you:"
prompt += "\nEnter 'quit' to end the program. "

message = ""
while message != 'quit':
    message = input(prompt)

    if message != 'quit':
        print(message)
```

<!-- pdf-page: 157 | printed: 124 -->

Giờ chương trình kiểm tra nhanh trước khi hiển thị thông điệp và chỉ in thông điệp nếu nó không trùng với giá trị thoát:

```text
Tell me something, and I will repeat it back to you:
Enter 'quit' to end the program. Hello everyone!
Hello everyone!

Tell me something, and I will repeat it back to you:
Enter 'quit' to end the program. Hello again.
Hello again.

Tell me something, and I will repeat it back to you:
Enter 'quit' to end the program. quit
```

### Dùng cờ

Trong ví dụ trước, chúng ta cho chương trình thực hiện một số tác vụ trong khi một điều kiện cho trước còn đúng. Nhưng với những chương trình phức tạp hơn, trong đó nhiều sự kiện khác nhau có thể khiến chương trình ngừng chạy thì sao?

Ví dụ, trong một trò chơi, nhiều sự kiện khác nhau có thể kết thúc trò chơi. Khi người chơi hết tàu, hết thời gian, hoặc tất cả các thành phố mà họ phải bảo vệ đều bị phá hủy, trò chơi sẽ kết thúc. Trò chơi cần kết thúc nếu bất kỳ sự kiện nào trong số này xảy ra. Nếu có nhiều sự kiện có thể xảy ra khiến chương trình dừng lại, việc cố kiểm tra tất cả các điều kiện này trong một câu lệnh `while` sẽ trở nên phức tạp và khó khăn.

Với một chương trình chỉ nên chạy chừng nào nhiều điều kiện còn đúng, bạn có thể định nghĩa một biến quyết định toàn bộ chương trình có đang hoạt động hay không. Biến này, được gọi là *cờ* (flag), đóng vai trò như một tín hiệu cho chương trình. Chúng ta có thể viết chương trình sao cho nó chạy trong khi cờ được đặt là `True`, và ngừng chạy khi bất kỳ sự kiện nào trong số đó đặt giá trị của cờ thành `False`. Nhờ vậy, câu lệnh `while` tổng thể chỉ cần kiểm tra một điều kiện: cờ hiện có đang là `True` hay không. Sau đó, tất cả các phép kiểm tra khác (để xem có sự kiện nào xảy ra khiến cờ phải đặt thành `False` hay không) có thể được tổ chức gọn gàng trong phần còn lại của chương trình.

Hãy thêm một cờ vào *parrot.py* từ mục trước. Cờ này, mà chúng ta sẽ đặt tên là `active` (dù bạn có thể đặt tên gì cũng được), sẽ theo dõi xem chương trình có nên tiếp tục chạy hay không:

```python
  prompt = "\nTell me something, and I will repeat it back to you:"
  prompt += "\nEnter 'quit' to end the program. "

❶ active = True
❷ while active:
      message = input(prompt)

❸     if message == 'quit':
          active = False
❹     else:
          print(message)
```

<!-- pdf-page: 158 | printed: 125 -->

Chúng ta đặt biến `active` thành `True` ❶ để chương trình bắt đầu ở trạng thái hoạt động. Làm vậy giúp câu lệnh `while` đơn giản hơn, vì không có phép so sánh nào được thực hiện trong chính câu lệnh `while`; phần logic được xử lý ở những phần khác của chương trình. Chừng nào biến `active` còn là `True`, vòng lặp sẽ tiếp tục chạy ❷.

Trong câu lệnh `if` bên trong vòng lặp `while`, chúng ta kiểm tra giá trị của `message` sau khi người dùng nhập đầu vào. Nếu người dùng nhập `'quit'` ❸, ta đặt `active` thành `False`, và vòng lặp `while` dừng lại. Nếu người dùng nhập bất cứ thứ gì khác `'quit'` ❹, ta in đầu vào của họ ra như một thông điệp.

Chương trình này có cùng đầu ra như ví dụ trước, khi chúng ta đặt phép kiểm tra điều kiện trực tiếp trong câu lệnh `while`. Nhưng giờ đây khi đã có một cờ cho biết toàn bộ chương trình có đang ở trạng thái hoạt động hay không, việc thêm các phép kiểm tra khác (chẳng hạn các câu lệnh `elif`) cho những sự kiện cần khiến `active` trở thành `False` sẽ rất dễ dàng. Điều này hữu ích trong những chương trình phức tạp như trò chơi, nơi có thể có nhiều sự kiện mà mỗi sự kiện đều phải khiến chương trình ngừng chạy. Khi bất kỳ sự kiện nào trong số này khiến cờ active trở thành `False`, vòng lặp chính của trò chơi sẽ kết thúc, một thông điệp *Game Over* có thể được hiển thị, và người chơi có thể được lựa chọn chơi lại.

### Dùng break để thoát khỏi vòng lặp

Để thoát khỏi vòng lặp `while` ngay lập tức mà không chạy phần mã còn lại trong vòng lặp, bất kể kết quả của bất kỳ phép kiểm tra điều kiện nào, hãy dùng câu lệnh `break`. Câu lệnh `break` điều hướng luồng chạy của chương trình; bạn có thể dùng nó để kiểm soát những dòng mã nào được thực thi và những dòng nào không, để chương trình chỉ thực thi đoạn mã bạn muốn, vào lúc bạn muốn.

Ví dụ, hãy xét một chương trình hỏi người dùng về những nơi họ đã đến thăm. Chúng ta có thể dừng vòng lặp `while` trong chương trình này bằng cách gọi `break` ngay khi người dùng nhập giá trị `'quit'`:

**cities.py**

```python
  prompt = "\nPlease enter the name of a city you have visited:"
  prompt += "\n(Enter 'quit' when you are finished.) "

❶ while True:
      city = input(prompt)

      if city == 'quit':
          break
      else:
          print("I'd love to go to " + city.title() + "!")
```

Một vòng lặp bắt đầu bằng `while True` ❶ sẽ chạy mãi mãi trừ khi nó gặp một câu lệnh `break`. Vòng lặp trong chương trình này tiếp tục yêu cầu người dùng nhập tên các thành phố họ đã đến cho đến khi họ nhập `'quit'`. Khi họ nhập `'quit'`, câu lệnh `break` được chạy, khiến Python thoát khỏi vòng lặp:

```text
Please enter the name of a city you have visited:
(Enter 'quit' when you are finished.) New York
I'd love to go to New York!
Please enter the name of a city you have visited:
(Enter 'quit' when you are finished.) San Francisco
I'd love to go to San Francisco!

Please enter the name of a city you have visited:
(Enter 'quit' when you are finished.) quit
```

<!-- pdf-page: 159 | printed: 126 -->

> **Lưu ý** Bạn có thể dùng câu lệnh `break` trong bất kỳ vòng lặp nào của Python. Ví dụ, bạn có thể dùng `break` để thoát khỏi một vòng lặp `for` đang duyệt qua một list hoặc một dictionary.

### Dùng continue trong vòng lặp

Thay vì thoát hẳn khỏi vòng lặp mà không thực thi phần mã còn lại, bạn có thể dùng câu lệnh `continue` để quay về đầu vòng lặp dựa trên kết quả của một phép kiểm tra điều kiện. Ví dụ, hãy xét một vòng lặp đếm từ 1 đến 10 nhưng chỉ in ra các số lẻ trong khoảng đó:

**counting.py**

```python
  current_number = 0
  while current_number < 10:
❶     current_number += 1
      if current_number % 2 == 0:
          continue

      print(current_number)
```

Đầu tiên, chúng ta đặt `current_number` bằng 0. Vì nó nhỏ hơn 10, Python đi vào vòng lặp `while`. Khi đã ở trong vòng lặp, ta tăng biến đếm thêm 1 tại ❶, nên `current_number` là 1. Sau đó, câu lệnh `if` kiểm tra phần dư của phép chia `current_number` cho 2. Nếu phần dư bằng 0 (nghĩa là `current_number` chia hết cho 2), câu lệnh `continue` yêu cầu Python bỏ qua phần còn lại của vòng lặp và quay về đầu vòng lặp. Nếu số hiện tại không chia hết cho 2, phần còn lại của vòng lặp được thực thi và Python in ra số hiện tại:

```text
1
3
5
7
9
```

### Tránh vòng lặp vô hạn

Mỗi vòng lặp `while` đều cần một cách để dừng lại, để nó không tiếp tục chạy mãi mãi. Ví dụ, vòng lặp đếm này lẽ ra phải đếm từ 1 đến 5:

**counting.py**

```python
x = 1
while x <= 5:
    print(x)
    x += 1
```

<!-- pdf-page: 160 | printed: 127 -->

Nhưng nếu bạn vô tình bỏ sót dòng `x += 1` (như dưới đây), vòng lặp sẽ chạy mãi mãi:

```python
# This loop runs forever!
x = 1
while x <= 5:
    print(x)
```

Giờ giá trị của `x` sẽ bắt đầu từ `1` nhưng không bao giờ thay đổi. Kết quả là phép kiểm tra điều kiện `x <= 5` sẽ luôn được đánh giá là `True` và vòng lặp `while` sẽ chạy mãi mãi, in ra một loạt số 1, như thế này:

```text
1
1
1
1
--snip--
```

Thỉnh thoảng lập trình viên nào cũng vô tình viết ra một vòng lặp `while` vô hạn, đặc biệt khi các vòng lặp trong chương trình có điều kiện thoát khó nhận ra. Nếu chương trình của bạn bị kẹt trong một vòng lặp vô hạn, hãy nhấn CTRL-C hoặc đơn giản là đóng cửa sổ terminal đang hiển thị đầu ra của chương trình.

Để tránh viết vòng lặp vô hạn, hãy kiểm tra mọi vòng lặp `while` và đảm bảo vòng lặp dừng lại đúng lúc bạn mong đợi. Nếu bạn muốn chương trình kết thúc khi người dùng nhập một giá trị đầu vào nhất định, hãy chạy chương trình và nhập giá trị đó. Nếu chương trình không kết thúc, hãy xem xét kỹ cách chương trình xử lý giá trị lẽ ra phải khiến vòng lặp thoát. Hãy đảm bảo ít nhất một phần của chương trình có thể khiến điều kiện của vòng lặp trở thành `False` hoặc khiến vòng lặp gặp một câu lệnh `break`.

> **Lưu ý** Một số trình soạn thảo, chẳng hạn Sublime Text, có cửa sổ đầu ra được nhúng sẵn. Điều này có thể khiến việc dừng một vòng lặp vô hạn trở nên khó khăn, và bạn có thể phải đóng trình soạn thảo để kết thúc vòng lặp.

<!-- box -->

**Tự mình thực hành**

**7-4. Topping pizza:** Viết một vòng lặp yêu cầu người dùng nhập một loạt topping pizza cho đến khi họ nhập giá trị `'quit'`. Khi họ nhập từng topping, in ra một thông điệp cho biết bạn sẽ thêm topping đó vào pizza của họ.

**7-5. Vé xem phim:** Một rạp chiếu phim thu giá vé khác nhau tùy theo tuổi của khán giả. Nếu một người dưới 3 tuổi, vé miễn phí; nếu họ từ 3 đến 12 tuổi, vé là $10; và nếu họ trên 12 tuổi, vé là $15. Viết một vòng lặp hỏi tuổi của người dùng, rồi cho họ biết giá vé xem phim của mình.

*(còn tiếp)*

<!-- pdf-page: 161 | printed: 128 -->

**7-6. Ba lối thoát:** Viết các phiên bản khác nhau của Bài tập 7-4 hoặc Bài tập 7-5, mỗi phiên bản làm ít nhất một lần từng việc sau:

- Dùng một phép kiểm tra điều kiện trong câu lệnh `while` để dừng vòng lặp.

- Dùng một biến `active` để kiểm soát thời gian chạy của vòng lặp.

- Dùng một câu lệnh `break` để thoát khỏi vòng lặp khi người dùng nhập giá trị `'quit'`.

**7-7. Vô hạn:** Viết một vòng lặp không bao giờ kết thúc và chạy nó. (Để kết thúc vòng lặp, hãy nhấn CTRL-C hoặc đóng cửa sổ đang hiển thị đầu ra.)

<!-- /box -->

## Dùng vòng lặp while với list và dictionary

Cho đến giờ, chúng ta mới chỉ làm việc với một mẩu thông tin của người dùng mỗi lần. Ta nhận đầu vào của người dùng rồi in đầu vào đó ra hoặc in một phản hồi cho nó. Ở lần lặp tiếp theo của vòng lặp `while`, ta lại nhận một giá trị đầu vào khác và phản hồi lại. Nhưng để theo dõi nhiều người dùng và nhiều mẩu thông tin, ta sẽ cần dùng list và dictionary cùng với vòng lặp `while`.

Vòng lặp `for` rất hiệu quả để lặp qua một list, nhưng bạn không nên sửa đổi một list bên trong vòng lặp `for`, vì Python sẽ gặp khó khăn trong việc theo dõi các phần tử trong list. Để sửa đổi một list trong khi duyệt qua nó, hãy dùng vòng lặp `while`. Dùng vòng lặp `while` với list và dictionary cho phép bạn thu thập, lưu trữ và sắp xếp nhiều đầu vào để xem xét và báo cáo về sau.

### Chuyển phần tử từ list này sang list khác

Hãy xét một list những người dùng mới đăng ký nhưng chưa được xác minh của một trang web. Sau khi xác minh những người dùng này, làm thế nào để chuyển họ sang một list riêng gồm những người dùng đã được xác nhận? Một cách là dùng vòng lặp `while` để lấy người dùng ra khỏi list người dùng chưa xác nhận trong khi ta xác minh họ, rồi thêm họ vào một list riêng gồm những người dùng đã được xác nhận. Đoạn mã đó có thể trông như thế này:

**confirmed_users.py**

```python
  # Start with users that need to be verified,
  #  and an empty list to hold confirmed users.
❶ unconfirmed_users = ['alice', 'brian', 'candace']
  confirmed_users = []

  # Verify each user until there are no more unconfirmed users.
  #  Move each verified user into the list of confirmed users.
❷ while unconfirmed_users:
❸     current_user = unconfirmed_users.pop()

      print("Verifying user: " + current_user.title())
❹     confirmed_users.append(current_user)
  # Display all confirmed users.
  print("\nThe following users have been confirmed:")
  for confirmed_user in confirmed_users:
      print(confirmed_user.title())
```

<!-- pdf-page: 162 | printed: 129 -->

Chúng ta bắt đầu với một list người dùng chưa xác nhận tại ❶ (Alice, Brian và Candace) và một list rỗng để chứa những người dùng đã được xác nhận. Vòng lặp `while` tại ❷ chạy chừng nào list `unconfirmed_users` còn chưa rỗng. Bên trong vòng lặp này, hàm `pop()` tại ❸ lần lượt xóa từng người dùng chưa được xác minh khỏi cuối `unconfirmed_users`. Ở đây, vì Candace đứng cuối trong list `unconfirmed_users`, tên của cô ấy sẽ là tên đầu tiên bị xóa, được lưu vào `current_user` và được thêm vào list `confirmed_users` tại ❹. Tiếp theo là Brian, rồi đến Alice.

Chúng ta mô phỏng việc xác nhận từng người dùng bằng cách in ra một thông điệp xác minh rồi thêm họ vào list người dùng đã được xác nhận. Khi list người dùng chưa xác nhận ngắn dần, list người dùng đã xác nhận dài ra. Khi list người dùng chưa xác nhận rỗng, vòng lặp dừng lại và list người dùng đã xác nhận được in ra:

```text
Verifying user: Candace
Verifying user: Brian
Verifying user: Alice

The following users have been confirmed:
Candace
Brian
Alice
```

### Xóa mọi phần tử có một giá trị cụ thể khỏi list

Trong Chương 3, chúng ta đã dùng `remove()` để xóa một giá trị cụ thể khỏi list. Hàm `remove()` hoạt động được vì giá trị chúng ta quan tâm chỉ xuất hiện một lần trong list. Nhưng nếu bạn muốn xóa mọi lần xuất hiện của một giá trị khỏi list thì sao?

Giả sử bạn có một list thú cưng trong đó giá trị `'cat'` lặp lại nhiều lần. Để xóa mọi lần xuất hiện của giá trị đó, bạn có thể chạy một vòng lặp `while` cho đến khi `'cat'` không còn trong list, như sau:

**pets.py**

```python
pets = ['dog', 'cat', 'dog', 'goldfish', 'cat', 'rabbit', 'cat']
print(pets)

while 'cat' in pets:
    pets.remove('cat')

print(pets)
```

Chúng ta bắt đầu với một list chứa nhiều lần xuất hiện của `'cat'`. Sau khi in list ra, Python đi vào vòng lặp `while` vì nó tìm thấy giá trị `'cat'` trong list ít nhất một lần. Khi đã ở trong vòng lặp, Python xóa lần xuất hiện đầu tiên của `'cat'`, quay về dòng `while`, rồi lại đi vào vòng lặp khi thấy `'cat'` vẫn còn trong list. Nó xóa từng lần xuất hiện của `'cat'` cho đến khi giá trị này không còn trong list nữa, lúc đó Python thoát khỏi vòng lặp và in list ra một lần nữa:

<!-- pdf-page: 163 | printed: 130 -->

```text
['dog', 'cat', 'dog', 'goldfish', 'cat', 'rabbit', 'cat']
['dog', 'dog', 'goldfish', 'rabbit']
```

### Điền dữ liệu vào dictionary từ đầu vào của người dùng

Bạn có thể yêu cầu nhập bao nhiêu đầu vào tùy ý ở mỗi lần lặp của vòng lặp `while`. Hãy tạo một chương trình khảo sát, trong đó mỗi lần lặp sẽ yêu cầu người tham gia nhập tên và câu trả lời. Chúng ta sẽ lưu dữ liệu thu thập được vào một dictionary, vì muốn gắn mỗi câu trả lời với một người dùng cụ thể:

**mountain_poll.py**

```python
  responses = {}
  # Set a flag to indicate that polling is active.
  polling_active = True

  while polling_active:
      # Prompt for the person's name and response.
❶     name = input("\nWhat is your name? ")
      response = input("Which mountain would you like to climb someday? ")

      # Store the response in the dictionary:
❷     responses[name] = response

      # Find out if anyone else is going to take the poll.
❸     repeat = input("Would you like to let another person respond? (yes/ no) ")
      if repeat == 'no':
          polling_active = False

  # Polling is complete. Show the results.
  print("\n--- Poll Results ---")
❹ for name, response in responses.items():
      print(name + " would like to climb " + response + ".")
```

Đầu tiên, chương trình định nghĩa một dictionary rỗng (`responses`) và đặt một cờ (`polling_active`) để cho biết cuộc khảo sát đang diễn ra. Chừng nào `polling_active` còn là `True`, Python sẽ chạy đoạn mã trong vòng lặp `while`.

Bên trong vòng lặp, người dùng được yêu cầu nhập tên người dùng và một ngọn núi họ muốn leo ❶. Thông tin đó được lưu vào dictionary `responses` ❷, và người dùng được hỏi có muốn tiếp tục cuộc khảo sát hay không ❸. Nếu họ nhập `yes`, chương trình lại đi vào vòng lặp `while`. Nếu họ nhập `no`, cờ `polling_active` được đặt thành `False`, vòng lặp `while` ngừng chạy, và khối mã cuối cùng tại ❹ hiển thị kết quả khảo sát.

<!-- pdf-page: 164 | printed: 131 -->

Nếu chạy chương trình này và nhập các câu trả lời mẫu, bạn sẽ thấy đầu ra như sau:

```text
What is your name? Eric
Which mountain would you like to climb someday? Denali
Would you like to let another person respond? (yes/ no) yes

What is your name? Lynn
Which mountain would you like to climb someday? Devil's Thumb
Would you like to let another person respond? (yes/ no) no

--- Poll Results ---
Lynn would like to climb Devil's Thumb.
Eric would like to climb Denali.
```

<!-- box -->

**Tự mình thực hành**

**7-8. Quầy bánh mì:** Tạo một list có tên `sandwich_orders` và điền vào đó tên của nhiều loại bánh sandwich khác nhau. Sau đó tạo một list rỗng có tên `finished_sandwiches`. Lặp qua list đơn gọi sandwich và in ra một thông điệp cho mỗi đơn, chẳng hạn như `I made your tuna sandwich.` Khi mỗi chiếc sandwich được làm xong, hãy chuyển nó sang list sandwich đã hoàn thành. Sau khi tất cả sandwich đã được làm xong, in ra một thông điệp liệt kê từng chiếc sandwich đã được làm.

**7-9. Hết pastrami:** Dùng list `sandwich_orders` từ Bài tập 7-8, đảm bảo sandwich `'pastrami'` xuất hiện trong list ít nhất ba lần. Thêm đoạn mã gần đầu chương trình để in ra thông điệp cho biết quầy đã hết pastrami, rồi dùng một vòng lặp `while` để xóa mọi lần xuất hiện của `'pastrami'` khỏi `sandwich_orders`. Đảm bảo không có chiếc sandwich pastrami nào nằm trong `finished_sandwiches`.

**7-10. Kỳ nghỉ trong mơ:** Viết một chương trình khảo sát người dùng về kỳ nghỉ trong mơ của họ. Viết một lời nhắc tương tự như *If you could visit one place in the world, where would you go?* Đưa vào một khối mã in ra kết quả của cuộc khảo sát.

<!-- /box -->

## Tổng kết

Trong chương này, bạn đã học cách dùng `input()` để cho phép người dùng cung cấp thông tin của chính họ cho chương trình. Bạn đã học cách làm việc với cả đầu vào dạng văn bản lẫn dạng số, và cách dùng vòng lặp `while` để chương trình chạy chừng nào người dùng còn muốn. Bạn đã thấy một số cách kiểm soát luồng chạy của vòng lặp `while`: đặt cờ `active`, dùng câu lệnh `break` và dùng câu lệnh `continue`. Bạn đã học cách dùng vòng lặp `while` để chuyển phần tử từ list này sang list khác và cách xóa mọi lần xuất hiện của một giá trị khỏi list. Bạn cũng đã học cách dùng vòng lặp `while` với dictionary.

<!-- pdf-page: 165 | printed: 132 -->

Trong Chương 8, bạn sẽ tìm hiểu về *hàm* (function). Hàm cho phép bạn chia chương trình thành những phần nhỏ, mỗi phần làm một việc cụ thể. Bạn có thể gọi một hàm bao nhiêu lần tùy thích, và có thể lưu các hàm của mình trong những file riêng. Nhờ dùng hàm, bạn sẽ có thể viết mã hiệu quả hơn, dễ khắc phục sự cố và bảo trì hơn, và có thể được tái sử dụng trong nhiều chương trình khác nhau.

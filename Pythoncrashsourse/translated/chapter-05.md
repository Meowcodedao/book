<!-- source: pythoncrashcourse.pdf | unit: chapter-05 | pdf pages 108-127 | printed 75-94 -->

# Chương 5: Câu lệnh if

<!-- pdf-page: 108 | printed: 75 -->

Lập trình thường đòi hỏi xem xét một tập hợp điều kiện và quyết định hành động nào cần thực hiện dựa trên các điều kiện đó. Câu lệnh `if` của Python cho phép bạn xem xét trạng thái hiện tại của chương trình và phản hồi phù hợp với trạng thái đó.

Trong chương này, bạn sẽ học cách viết các phép kiểm tra điều kiện (conditional test), cho phép bạn kiểm tra bất kỳ điều kiện nào bạn quan tâm. Bạn sẽ học cách viết những câu lệnh `if` đơn giản, và học cách tạo một chuỗi câu lệnh `if` phức tạp hơn để xác định khi nào đúng những điều kiện bạn muốn đang xảy ra. Sau đó, bạn sẽ áp dụng khái niệm này cho list, để có thể viết một vòng lặp `for` xử lý hầu hết các phần tử trong list theo một cách, nhưng xử lý một số phần tử có giá trị cụ thể theo cách khác.

<!-- pdf-page: 109 | printed: 76 -->

## Một ví dụ đơn giản

Ví dụ ngắn sau cho thấy các phép kiểm tra `if` giúp bạn phản hồi đúng với những tình huống đặc biệt như thế nào. Hãy tưởng tượng bạn có một list ô tô và muốn in ra tên từng chiếc. Tên ô tô là danh từ riêng, nên tên của hầu hết các ô tô nên được in theo kiểu viết hoa chữ cái đầu. Tuy nhiên, giá trị `'bmw'` nên được in toàn chữ hoa. Đoạn mã sau lặp qua một list tên ô tô và tìm giá trị `'bmw'`. Bất cứ khi nào giá trị là `'bmw'`, nó sẽ được in toàn chữ hoa thay vì viết hoa chữ cái đầu:

**cars.py**

```python
  cars = ['audi', 'bmw', 'subaru', 'toyota']

  for car in cars:
❶     if car == 'bmw':
          print(car.upper())
      else:
          print(car.title())
```

Vòng lặp trong ví dụ này trước tiên kiểm tra xem giá trị hiện tại của `car` có phải là `'bmw'` không ❶. Nếu đúng, giá trị được in toàn chữ hoa. Nếu giá trị của `car` là bất cứ thứ gì khác `'bmw'`, nó được in theo kiểu viết hoa chữ cái đầu:

```text
Audi
BMW
Subaru
Toyota
```

Ví dụ này kết hợp một số khái niệm mà bạn sẽ học trong chương này. Hãy bắt đầu bằng việc xem xét các loại phép kiểm tra bạn có thể dùng để xem xét các điều kiện trong chương trình.

## Phép kiểm tra điều kiện

Cốt lõi của mọi câu lệnh `if` là một biểu thức có thể được đánh giá là `True` hoặc `False`, được gọi là *phép kiểm tra điều kiện* (conditional test). Python dùng các giá trị `True` và `False` để quyết định có nên thực thi đoạn mã trong câu lệnh `if` hay không. Nếu một phép kiểm tra điều kiện được đánh giá là `True`, Python thực thi đoạn mã đứng sau câu lệnh `if`. Nếu phép kiểm tra được đánh giá là `False`, Python bỏ qua đoạn mã đứng sau câu lệnh `if`.

### Kiểm tra bằng nhau

Hầu hết các phép kiểm tra điều kiện so sánh giá trị hiện tại của một biến với một giá trị cụ thể mà bạn quan tâm. Phép kiểm tra điều kiện đơn giản nhất kiểm tra xem giá trị của một biến có bằng giá trị mà bạn quan tâm hay không:

```python
❶ >>> car = 'bmw'
❷ >>> car == 'bmw'
  True
```

<!-- pdf-page: 110 | printed: 77 -->

Dòng tại ❶ gán giá trị của `car` là `'bmw'` bằng một dấu bằng, như bạn đã thấy nhiều lần. Dòng tại ❷ kiểm tra xem giá trị của `car` có phải là `'bmw'` không, bằng hai dấu bằng (`==`). *Toán tử so sánh bằng* (equality operator) này trả về `True` nếu các giá trị ở bên trái và bên phải toán tử khớp nhau, và trả về `False` nếu chúng không khớp. Các giá trị trong ví dụ này khớp nhau, nên Python trả về `True`.

Khi giá trị của `car` là bất cứ thứ gì khác `'bmw'`, phép kiểm tra này trả về `False`:

```python
❶ >>> car = 'audi'
❷ >>> car == 'bmw'
  False
```

Một dấu bằng thực chất là một câu lệnh; bạn có thể đọc đoạn mã tại ❶ là “Gán giá trị của car bằng `'audi'`.” Ngược lại, hai dấu bằng, như tại ❷, đặt ra một câu hỏi: “Giá trị của car có bằng `'bmw'` không?” Hầu hết các ngôn ngữ lập trình đều dùng dấu bằng theo cách này.

### Bỏ qua chữ hoa, chữ thường khi kiểm tra bằng nhau

Trong Python, phép kiểm tra bằng nhau có phân biệt chữ hoa, chữ thường. Ví dụ, hai giá trị có cách viết hoa khác nhau không được coi là bằng nhau:

```python
>>> car = 'Audi'
>>> car == 'audi'
False
```

Nếu chữ hoa, chữ thường là quan trọng, hành vi này rất có lợi. Nhưng nếu chữ hoa, chữ thường không quan trọng và bạn chỉ muốn kiểm tra giá trị của một biến, bạn có thể chuyển giá trị của biến thành chữ thường trước khi so sánh:

```python
>>> car = 'Audi'
>>> car.lower() == 'audi'
True
```

Phép kiểm tra này sẽ trả về `True` bất kể giá trị `'Audi'` được định dạng thế nào, vì giờ đây phép kiểm tra không phân biệt chữ hoa, chữ thường. Hàm `lower()` không thay đổi giá trị ban đầu được lưu trong `car`, nên bạn có thể thực hiện loại so sánh này mà không ảnh hưởng đến biến ban đầu:

```python
❶ >>> car = 'Audi'
❷ >>> car.lower() == 'audi'
  True
❸ >>> car
  'Audi'
```

Tại ❶, chúng ta lưu chuỗi viết hoa `'Audi'` vào biến `car`. Tại ❷, chúng ta chuyển giá trị của `car` thành chữ thường và so sánh giá trị chữ thường đó với chuỗi `'audi'`. Hai chuỗi khớp nhau, nên Python trả về `True`. Tại ❸, ta có thể thấy giá trị được lưu trong `car` không bị ảnh hưởng bởi phép kiểm tra điều kiện.

<!-- pdf-page: 111 | printed: 78 -->

Các trang web áp đặt một số quy tắc cho dữ liệu người dùng nhập vào theo cách tương tự như vậy. Ví dụ, một trang web có thể dùng một phép kiểm tra điều kiện như thế này để đảm bảo mỗi người dùng có một tên người dùng thực sự duy nhất, chứ không chỉ là một biến thể về cách viết hoa của tên người dùng của người khác. Khi ai đó gửi một tên người dùng mới, tên đó sẽ được chuyển thành chữ thường và so sánh với phiên bản chữ thường của tất cả các tên người dùng hiện có. Trong lần kiểm tra này, một tên người dùng như `'John'` sẽ bị từ chối nếu bất kỳ biến thể nào của `'john'` đã được sử dụng.

### Kiểm tra khác nhau

Khi muốn xác định hai giá trị có khác nhau hay không, bạn có thể kết hợp một dấu chấm than và một dấu bằng (`!=`). Dấu chấm than biểu thị *not* (phủ định), giống như trong nhiều ngôn ngữ lập trình khác.

Hãy dùng một câu lệnh `if` khác để xem cách dùng toán tử so sánh khác. Chúng ta sẽ lưu loại topping pizza được yêu cầu vào một biến, rồi in ra một thông điệp nếu người đó không gọi cá cơm:

**toppings.py**

```python
  requested_topping = 'mushrooms'

❶ if requested_topping != 'anchovies':
      print("Hold the anchovies!")
```

Dòng tại ❶ so sánh giá trị của `requested_topping` với giá trị `'anchovies'`. Nếu hai giá trị này không khớp nhau, Python trả về `True` và thực thi đoạn mã đứng sau câu lệnh `if`. Nếu hai giá trị khớp nhau, Python trả về `False` và không chạy đoạn mã đứng sau câu lệnh `if`.

Vì giá trị của `requested_topping` không phải là `'anchovies'`, câu lệnh `print` được thực thi:

```text
Hold the anchovies!
```

Hầu hết các biểu thức điều kiện bạn viết sẽ kiểm tra bằng nhau, nhưng đôi khi bạn sẽ thấy kiểm tra khác nhau hiệu quả hơn.

### So sánh số

Kiểm tra giá trị số khá đơn giản. Ví dụ, đoạn mã sau kiểm tra xem một người có đúng 18 tuổi không:

```python
>>> age = 18
>>> age == 18
True
```

<!-- pdf-page: 112 | printed: 79 -->

Bạn cũng có thể kiểm tra xem hai số có khác nhau không. Ví dụ, đoạn mã sau in ra một thông điệp nếu câu trả lời đưa ra không đúng:

**magic_number.py**

```python
  answer = 17
❶ if answer != 42:
      print("That is not the correct answer. Please try again!")
```

Phép kiểm tra điều kiện tại ❶ thành công, vì giá trị của `answer` (`17`) không bằng `42`. Vì phép kiểm tra thành công, khối mã được thụt lề được thực thi:

```text
That is not the correct answer. Please try again!
```

Bạn cũng có thể đưa vào câu lệnh điều kiện nhiều phép so sánh toán học khác nhau, chẳng hạn nhỏ hơn, nhỏ hơn hoặc bằng, lớn hơn, và lớn hơn hoặc bằng:

```python
>>> age = 19
>>> age < 21
True
>>> age <= 21
True
>>> age > 21
False
>>> age >= 21
False
```

Mỗi phép so sánh toán học đều có thể được dùng như một phần của câu lệnh `if`, giúp bạn phát hiện chính xác những điều kiện mà bạn quan tâm.

### Kiểm tra nhiều điều kiện

Có thể bạn sẽ muốn kiểm tra nhiều điều kiện cùng lúc. Ví dụ, đôi khi bạn cần cả hai điều kiện đều là `True` thì mới thực hiện một hành động. Những lúc khác, bạn có thể hài lòng chỉ với một điều kiện là `True`. Các từ khóa `and` và `or` có thể giúp bạn trong những tình huống này.

#### Dùng and để kiểm tra nhiều điều kiện

Để kiểm tra xem cả hai điều kiện có cùng là `True` hay không, hãy dùng từ khóa `and` để kết hợp hai phép kiểm tra điều kiện; nếu từng phép kiểm tra đều thành công, toàn bộ biểu thức được đánh giá là `True`. Nếu một trong hai phép kiểm tra thất bại, hoặc cả hai đều thất bại, biểu thức được đánh giá là `False`.

Ví dụ, bạn có thể kiểm tra xem cả hai người có cùng trên 21 tuổi hay không bằng phép kiểm tra sau:

```python
❶ >>> age_0 = 22
  >>> age_1 = 18
❷ >>> age_0 >= 21 and age_1 >= 21
  False
❸ >>> age_1 = 22
  >>> age_0 >= 21 and age_1 >= 21
  True
```

<!-- pdf-page: 113 | printed: 80 -->

Tại ❶, chúng ta định nghĩa hai độ tuổi, `age_0` và `age_1`. Tại ❷, chúng ta kiểm tra xem cả hai độ tuổi có từ 21 trở lên không. Phép kiểm tra bên trái thành công, nhưng phép kiểm tra bên phải thất bại, nên toàn bộ biểu thức điều kiện được đánh giá là `False`. Tại ❸, chúng ta đổi `age_1` thành 22. Giá trị của `age_1` giờ lớn hơn 21, nên cả hai phép kiểm tra riêng lẻ đều thành công, khiến toàn bộ biểu thức điều kiện được đánh giá là `True`.

Để dễ đọc hơn, bạn có thể đặt dấu ngoặc đơn quanh từng phép kiểm tra riêng lẻ, nhưng điều đó không bắt buộc. Nếu dùng dấu ngoặc đơn, phép kiểm tra của bạn sẽ trông như thế này:

```text
(age_0 >= 21) and (age_1 >= 21)
```

#### Dùng or để kiểm tra nhiều điều kiện

Từ khóa `or` cũng cho phép bạn kiểm tra nhiều điều kiện, nhưng nó thành công khi một trong hai, hoặc cả hai, phép kiểm tra riêng lẻ thành công. Một biểu thức `or` chỉ thất bại khi cả hai phép kiểm tra riêng lẻ đều thất bại.

Hãy xét lại hai độ tuổi, nhưng lần này chúng ta chỉ cần một người trên 21 tuổi:

```python
❶ >>> age_0 = 22
  >>> age_1 = 18
❷ >>> age_0 >= 21 or age_1 >= 21
  True
❸ >>> age_0 = 18
  >>> age_0 >= 21 or age_1 >= 21
  False
```

Chúng ta lại bắt đầu với hai biến độ tuổi tại ❶. Vì phép kiểm tra cho `age_0` tại ❷ thành công, toàn bộ biểu thức được đánh giá là `True`. Sau đó, chúng ta giảm `age_0` xuống 18. Trong phép kiểm tra tại ❸, giờ cả hai phép kiểm tra đều thất bại và toàn bộ biểu thức được đánh giá là `False`.

### Kiểm tra xem một giá trị có nằm trong list không

Đôi khi điều quan trọng là phải kiểm tra xem một list có chứa một giá trị nhất định hay không trước khi thực hiện một hành động. Ví dụ, bạn có thể muốn kiểm tra xem một tên người dùng mới đã tồn tại trong list tên người dùng hiện có hay chưa trước khi hoàn tất việc đăng ký cho ai đó trên một trang web. Trong một dự án bản đồ, bạn có thể muốn kiểm tra xem một địa điểm được gửi lên đã có trong list các địa điểm đã biết hay chưa.

Để biết một giá trị cụ thể đã có trong list hay chưa, hãy dùng từ khóa `in`. Hãy xem một đoạn mã bạn có thể viết cho một tiệm pizza. Chúng ta sẽ tạo một list các topping mà khách hàng yêu cầu cho chiếc pizza, rồi kiểm tra xem một số topping nhất định có nằm trong list hay không.

<!-- pdf-page: 114 | printed: 81 -->

```python
  >>> requested_toppings = ['mushrooms', 'onions', 'pineapple']
❶ >>> 'mushrooms' in requested_toppings
  True
❷ >>> 'pepperoni' in requested_toppings
  False
```

Tại ❶ và ❷, từ khóa `in` yêu cầu Python kiểm tra sự tồn tại của `'mushrooms'` và `'pepperoni'` trong list `requested_toppings`. Kỹ thuật này khá mạnh mẽ, vì bạn có thể tạo một list các giá trị thiết yếu, rồi dễ dàng kiểm tra xem giá trị bạn đang kiểm tra có khớp với một trong các giá trị trong list hay không.

### Kiểm tra xem một giá trị có không nằm trong list không

Những lúc khác, điều quan trọng là phải biết một giá trị có không xuất hiện trong list hay không. Bạn có thể dùng từ khóa `not` trong tình huống này. Ví dụ, hãy xét một list người dùng bị cấm bình luận trên một diễn đàn. Bạn có thể kiểm tra xem một người dùng đã bị cấm hay chưa trước khi cho phép người đó gửi bình luận:

**banned_users.py**

```python
  banned_users = ['andrew', 'carolina', 'david']
  user = 'marie'

❶ if user not in banned_users:
      print(user.title() + ", you can post a response if you wish.")
```

Dòng tại ❶ đọc khá rõ nghĩa. Nếu giá trị của `user` không nằm trong list `banned_users`, Python trả về `True` và thực thi dòng được thụt lề.

Người dùng `'marie'` không nằm trong list `banned_users`, nên cô ấy thấy một thông điệp mời cô gửi phản hồi:

```text
Marie, you can post a response if you wish.
```

### Biểu thức Boolean

Khi học thêm về lập trình, đến một lúc nào đó bạn sẽ nghe thấy thuật ngữ *biểu thức Boolean* (Boolean expression). Biểu thức Boolean chỉ là một tên gọi khác của phép kiểm tra điều kiện. Một *giá trị Boolean* là `True` hoặc `False`, giống như giá trị của một biểu thức điều kiện sau khi đã được đánh giá.

Giá trị Boolean thường được dùng để theo dõi một số điều kiện nhất định, chẳng hạn một trò chơi có đang chạy hay không, hoặc một người dùng có thể chỉnh sửa một nội dung nào đó trên trang web hay không:

```python
game_active = True
can_edit = False
```

Giá trị Boolean cung cấp một cách hiệu quả để theo dõi trạng thái của chương trình hoặc một điều kiện cụ thể quan trọng trong chương trình của bạn.

<!-- pdf-page: 115 | printed: 82 -->

<!-- box -->

**Tự mình thực hành**

**5-1. Phép kiểm tra điều kiện:** Viết một loạt phép kiểm tra điều kiện. In ra một câu mô tả từng phép kiểm tra và dự đoán của bạn về kết quả của từng phép kiểm tra. Mã của bạn nên trông giống như sau:

```python
car = 'subaru'
print("Is car == 'subaru'? I predict True.")
print(car == 'subaru')

print("\nIs car == 'audi'? I predict False.")
print(car == 'audi')
```

- Xem kỹ kết quả và đảm bảo bạn hiểu vì sao mỗi dòng được đánh giá là `True` hoặc `False`.

- Tạo ít nhất 10 phép kiểm tra. Có ít nhất 5 phép kiểm tra được đánh giá là `True` và 5 phép kiểm tra khác được đánh giá là `False`.

**5-2. Thêm phép kiểm tra điều kiện:** Bạn không cần giới hạn số phép kiểm tra ở mức 10. Nếu muốn thử thêm các phép so sánh, hãy viết thêm phép kiểm tra và thêm chúng vào *conditional_tests.py*. Hãy có ít nhất một kết quả `True` và một kết quả `False` cho mỗi loại sau:

- Kiểm tra bằng nhau và khác nhau với chuỗi

- Kiểm tra có dùng hàm `lower()`

- Kiểm tra số liên quan đến bằng nhau và khác nhau, lớn hơn và nhỏ hơn, lớn hơn hoặc bằng, và nhỏ hơn hoặc bằng

- Kiểm tra có dùng từ khóa `and` và từ khóa `or`

- Kiểm tra xem một phần tử có nằm trong list không

- Kiểm tra xem một phần tử có không nằm trong list không

<!-- /box -->

## Câu lệnh if

Khi đã hiểu phép kiểm tra điều kiện, bạn có thể bắt đầu viết câu lệnh `if`. Có nhiều loại câu lệnh `if` khác nhau, và việc bạn chọn loại nào phụ thuộc vào số điều kiện cần kiểm tra. Bạn đã thấy vài ví dụ về câu lệnh `if` khi tìm hiểu phép kiểm tra điều kiện, nhưng giờ hãy đi sâu hơn vào chủ đề này.

### Câu lệnh if đơn giản

Loại câu lệnh `if` đơn giản nhất có một phép kiểm tra và một hành động:

```python
if conditional_test:
    do something
```

<!-- pdf-page: 116 | printed: 83 -->

Bạn có thể đặt bất kỳ phép kiểm tra điều kiện nào vào dòng đầu tiên và hầu như bất kỳ hành động nào vào khối thụt lề đứng sau phép kiểm tra. Nếu phép kiểm tra điều kiện được đánh giá là `True`, Python thực thi đoạn mã đứng sau câu lệnh `if`. Nếu phép kiểm tra được đánh giá là `False`, Python bỏ qua đoạn mã đứng sau câu lệnh `if`.

Giả sử chúng ta có một biến biểu thị tuổi của một người, và muốn biết người đó đã đủ tuổi đi bầu cử chưa. Đoạn mã sau kiểm tra xem người đó có thể đi bầu cử không:

**voting.py**

```python
  age = 19
❶ if age >= 18:
❷     print("You are old enough to vote!")
```

Tại ❶, Python kiểm tra xem giá trị trong `age` có lớn hơn hoặc bằng 18 không. Đúng vậy, nên Python thực thi câu lệnh `print` được thụt lề tại ❷:

```text
You are old enough to vote!
```

Thụt lề đóng vai trò trong câu lệnh `if` giống như trong vòng lặp `for`. Mọi dòng được thụt lề sau một câu lệnh `if` sẽ được thực thi nếu phép kiểm tra thành công, và toàn bộ khối các dòng được thụt lề sẽ bị bỏ qua nếu phép kiểm tra không thành công.

Bạn có thể có bao nhiêu dòng mã tùy thích trong khối đứng sau câu lệnh `if`. Hãy thêm một dòng đầu ra nữa nếu người đó đã đủ tuổi đi bầu cử, hỏi xem người đó đã đăng ký đi bầu chưa:

```python
age = 19
if age >= 18:
    print("You are old enough to vote!")
    print("Have you registered to vote yet?")
```

Phép kiểm tra điều kiện thành công và cả hai câu lệnh `print` đều được thụt lề, nên cả hai dòng đều được in ra:

```text
You are old enough to vote!
Have you registered to vote yet?
```

Nếu giá trị của `age` nhỏ hơn 18, chương trình này sẽ không tạo ra đầu ra nào.

### Câu lệnh if-else

Bạn sẽ thường muốn thực hiện một hành động khi phép kiểm tra điều kiện thành công, và một hành động khác trong mọi trường hợp còn lại. Cú pháp `if`-`else` của Python giúp điều này trở nên khả thi. Một khối `if`-`else` tương tự như một câu lệnh `if` đơn giản, nhưng câu lệnh `else` cho phép bạn định nghĩa một hành động hoặc một nhóm hành động được thực thi khi phép kiểm tra điều kiện thất bại.

<!-- pdf-page: 117 | printed: 84 -->

Chúng ta sẽ hiển thị cùng thông điệp như trước nếu người đó đã đủ tuổi đi bầu cử, nhưng lần này sẽ thêm một thông điệp cho những ai chưa đủ tuổi:

```python
  age = 17
❶ if age >= 18:
      print("You are old enough to vote!")
      print("Have you registered to vote yet?")
❷ else:
      print("Sorry, you are too young to vote.")
      print("Please register to vote as soon as you turn 18!")
```

Nếu phép kiểm tra điều kiện tại ❶ thành công, khối các câu lệnh `print` thụt lề đầu tiên được thực thi. Nếu phép kiểm tra được đánh giá là `False`, khối `else` tại ❷ được thực thi. Vì lần này `age` nhỏ hơn 18, phép kiểm tra điều kiện thất bại và đoạn mã trong khối `else` được thực thi:

```text
Sorry, you are too young to vote.
Please register to vote as soon as you turn 18!
```

Đoạn mã này hoạt động vì nó chỉ có hai tình huống cần đánh giá: một người hoặc đã đủ tuổi đi bầu cử, hoặc chưa đủ tuổi. Cấu trúc `if`-`else` hoạt động tốt trong những tình huống mà bạn muốn Python luôn thực thi một trong hai hành động có thể. Trong một chuỗi `if-else` đơn giản như thế này, một trong hai hành động sẽ luôn được thực thi.

### Chuỗi if-elif-else

Bạn sẽ thường cần kiểm tra nhiều hơn hai tình huống có thể xảy ra, và để đánh giá chúng, bạn có thể dùng cú pháp `if`-`elif`-`else` của Python. Python chỉ thực thi một khối trong một chuỗi `if`-`elif`-`else`. Nó chạy lần lượt từng phép kiểm tra điều kiện cho đến khi có một phép kiểm tra thành công. Khi một phép kiểm tra thành công, đoạn mã đứng sau phép kiểm tra đó được thực thi và Python bỏ qua các phép kiểm tra còn lại.

Nhiều tình huống trong thực tế có nhiều hơn hai điều kiện có thể xảy ra. Ví dụ, hãy xét một công viên giải trí thu giá vé khác nhau cho các nhóm tuổi khác nhau:

- Vào cửa miễn phí cho mọi người dưới 4 tuổi.

- Giá vé vào cửa cho người từ 4 đến 18 tuổi là $5.

- Giá vé vào cửa cho người từ 18 tuổi trở lên là $10.

Làm thế nào để dùng câu lệnh `if` xác định giá vé vào cửa của một người? Đoạn mã sau kiểm tra nhóm tuổi của một người rồi in ra thông điệp về giá vé vào cửa:

**amusement_park.py**

```python
  age = 12
❶ if age < 4:
      print("Your admission cost is $0.")
❷ elif age < 18:
      print("Your admission cost is $5.")
❸ else:
      print("Your admission cost is $10.")
```

<!-- pdf-page: 118 | printed: 85 -->

Phép kiểm tra `if` tại ❶ kiểm tra xem một người có dưới 4 tuổi không. Nếu phép kiểm tra thành công, một thông điệp phù hợp được in ra và Python bỏ qua các phép kiểm tra còn lại. Dòng `elif` tại ❷ thực chất là một phép kiểm tra `if` khác, chỉ chạy khi phép kiểm tra trước đó thất bại. Tại điểm này trong chuỗi, chúng ta biết người đó ít nhất 4 tuổi vì phép kiểm tra đầu tiên đã thất bại. Nếu người đó dưới 18 tuổi, một thông điệp phù hợp được in ra và Python bỏ qua khối `else`. Nếu cả phép kiểm tra `if` và `elif` đều thất bại, Python chạy đoạn mã trong khối `else` tại ❸.

Trong ví dụ này, phép kiểm tra tại ❶ được đánh giá là `False`, nên khối mã của nó không được thực thi. Tuy nhiên, phép kiểm tra thứ hai được đánh giá là `True` (12 nhỏ hơn 18) nên khối mã của nó được thực thi. Đầu ra là một câu, thông báo cho người dùng về giá vé vào cửa:

```text
Your admission cost is $5.
```

Bất kỳ độ tuổi nào lớn hơn 17 sẽ khiến hai phép kiểm tra đầu tiên thất bại. Trong những trường hợp đó, khối `else` sẽ được thực thi và giá vé vào cửa sẽ là $10.

Thay vì in giá vé vào cửa bên trong khối `if`-`elif`-`else`, sẽ ngắn gọn hơn nếu chỉ gán giá vé bên trong chuỗi `if`-`elif`-`else`, rồi dùng một câu lệnh `print` đơn giản chạy sau khi chuỗi đã được đánh giá:

```python
  age = 12

  if age < 4:
❶     price = 0
  elif age < 18:
❷     price = 5
  else:
❸     price = 10

❹ print("Your admission cost is $" + str(price) + ".")
```

Các dòng tại ❶, ❷ và ❸ gán giá trị của `price` theo tuổi của người đó, như trong ví dụ trước. Sau khi giá vé được gán bởi chuỗi `if`-`elif`-`else`, một câu lệnh `print` riêng, không thụt lề ❹ dùng giá trị này để hiển thị thông điệp cho biết giá vé vào cửa của người đó.

Đoạn mã này cho ra cùng đầu ra như ví dụ trước, nhưng mục đích của chuỗi `if`-`elif`-`else` hẹp hơn. Thay vì xác định giá vé và hiển thị thông điệp, nó chỉ đơn giản xác định giá vé vào cửa. Ngoài việc hiệu quả hơn, đoạn mã đã sửa này cũng dễ sửa đổi hơn so với cách ban đầu. Để thay đổi nội dung thông điệp đầu ra, bạn chỉ cần sửa một câu lệnh `print` thay vì ba câu lệnh `print` riêng biệt.

<!-- pdf-page: 119 | printed: 86 -->

### Dùng nhiều khối elif

Bạn có thể dùng bao nhiêu khối `elif` tùy thích trong mã của mình. Ví dụ, nếu công viên giải trí áp dụng giảm giá cho người cao tuổi, bạn có thể thêm một phép kiểm tra điều kiện nữa vào mã để xác định một người có đủ điều kiện nhận giảm giá cho người cao tuổi hay không. Giả sử mọi người từ 65 tuổi trở lên trả một nửa giá vé thông thường, tức $5:

```python
  age = 12

  if age < 4:
      price = 0
  elif age < 18:
      price = 5
❶ elif age < 65:
      price = 10
❷ else:
      price = 5

  print("Your admission cost is $" + str(price) + ".")
```

Phần lớn đoạn mã này không thay đổi. Khối `elif` thứ hai tại ❶ giờ kiểm tra để đảm bảo một người dưới 65 tuổi trước khi áp dụng giá vé đầy đủ $10 cho họ. Hãy để ý rằng giá trị được gán trong khối `else` tại ❷ cần được đổi thành $5, vì những độ tuổi duy nhất đến được khối này là những người từ 65 tuổi trở lên.

### Bỏ qua khối else

Python không bắt buộc phải có khối `else` ở cuối một chuỗi `if`-`elif`. Đôi khi khối `else` hữu ích; đôi khi dùng thêm một câu lệnh `elif` để bắt đúng điều kiện cụ thể mà bạn quan tâm lại rõ ràng hơn:

```python
  age = 12

  if age < 4:
      price = 0
  elif age < 18:
      price = 5
  elif age < 65:
      price = 10
❶ elif age >= 65:
      price = 5

  print("Your admission cost is $" + str(price) + ".")
```

Khối `elif` bổ sung tại ❶ gán giá vé $5 khi người đó từ 65 tuổi trở lên, rõ ràng hơn một chút so với khối `else` chung chung. Với thay đổi này, mọi khối mã đều phải vượt qua một phép kiểm tra cụ thể thì mới được thực thi.

<!-- pdf-page: 120 | printed: 87 -->

Khối `else` là một câu lệnh “hứng tất cả”. Nó khớp với mọi điều kiện không khớp với một phép kiểm tra `if` hay `elif` cụ thể nào, và điều đó đôi khi có thể bao gồm cả dữ liệu không hợp lệ hoặc thậm chí độc hại. Nếu bạn có một điều kiện cuối cùng cụ thể cần kiểm tra, hãy cân nhắc dùng một khối `elif` cuối cùng và bỏ khối `else`. Nhờ đó, bạn sẽ thêm tự tin rằng mã của mình chỉ chạy trong những điều kiện đúng.

### Kiểm tra nhiều điều kiện

Chuỗi `if`-`elif`-`else` rất mạnh mẽ, nhưng chỉ phù hợp khi bạn chỉ cần một phép kiểm tra thành công. Ngay khi Python tìm thấy một phép kiểm tra thành công, nó bỏ qua các phép kiểm tra còn lại. Hành vi này có lợi, vì nó hiệu quả và cho phép bạn kiểm tra một điều kiện cụ thể.

Tuy nhiên, đôi khi điều quan trọng là phải kiểm tra tất cả các điều kiện mà bạn quan tâm. Trong trường hợp này, bạn nên dùng một loạt câu lệnh `if` đơn giản, không có khối `elif` hay `else`. Kỹ thuật này hợp lý khi có thể có nhiều hơn một điều kiện là `True`, và bạn muốn hành động với mọi điều kiện là `True`.

Hãy xét lại ví dụ về tiệm pizza. Nếu ai đó yêu cầu một chiếc pizza có hai loại topping, bạn cần đảm bảo cho cả hai loại topping vào chiếc pizza của họ:

**toppings.py**

```python
❶ requested_toppings = ['mushrooms', 'extra cheese']

❷ if 'mushrooms' in requested_toppings:
      print("Adding mushrooms.")
❸ if 'pepperoni' in requested_toppings:
      print("Adding pepperoni.")
❹ if 'extra cheese' in requested_toppings:
      print("Adding extra cheese.")

  print("\nFinished making your pizza!")
```

Chúng ta bắt đầu tại ❶ với một list chứa các topping được yêu cầu. Câu lệnh `if` tại ❷ kiểm tra xem người đó có yêu cầu nấm trên pizza không. Nếu có, một thông điệp được in ra để xác nhận loại topping đó. Phép kiểm tra pepperoni tại ❸ là một câu lệnh `if` đơn giản khác, không phải câu lệnh `elif` hay `else`, nên phép kiểm tra này được chạy bất kể phép kiểm tra trước đó có thành công hay không. Đoạn mã tại ❹ kiểm tra xem có yêu cầu thêm phô mai hay không, bất kể kết quả của hai phép kiểm tra đầu tiên. Ba phép kiểm tra độc lập này được thực thi mỗi lần chương trình chạy.

Vì mọi điều kiện trong ví dụ này đều được đánh giá, cả nấm và phô mai thêm đều được cho vào pizza:

```text
Adding mushrooms.
Adding extra cheese.

Finished making your pizza!
```

<!-- pdf-page: 121 | printed: 88 -->

Đoạn mã này sẽ không hoạt động đúng nếu chúng ta dùng một khối `if`-`elif`-`else`, vì đoạn mã sẽ ngừng chạy ngay sau khi có một phép kiểm tra thành công. Nó sẽ trông như thế này:

```python
requested_toppings = ['mushrooms', 'extra cheese']

if 'mushrooms' in requested_toppings:
    print("Adding mushrooms.")
elif 'pepperoni' in requested_toppings:
    print("Adding pepperoni.")
elif 'extra cheese' in requested_toppings:
    print("Adding extra cheese.")

print("\nFinished making your pizza!")
```

Phép kiểm tra `'mushrooms'` là phép kiểm tra đầu tiên thành công, nên nấm được cho vào pizza. Tuy nhiên, các giá trị `'extra cheese'` và `'pepperoni'` không bao giờ được kiểm tra, vì Python không chạy bất kỳ phép kiểm tra nào sau phép kiểm tra thành công đầu tiên trong một chuỗi `if-elif-else`. Topping đầu tiên của khách sẽ được thêm vào, nhưng tất cả các topping khác của họ sẽ bị bỏ sót:

```text
Adding mushrooms.

Finished making your pizza!
```

Tóm lại, nếu bạn chỉ muốn một khối mã được chạy, hãy dùng chuỗi `if`-`elif`- `else`. Nếu cần chạy nhiều hơn một khối mã, hãy dùng một loạt câu lệnh `if` độc lập.

<!-- box -->

**Tự mình thực hành**

**5-3. Màu người ngoài hành tinh #1:** Hãy tưởng tượng một người ngoài hành tinh vừa bị bắn hạ trong một trò chơi. Tạo một biến có tên `alien_color` và gán cho nó giá trị `'green'`, `'yellow'` hoặc `'red'`.

- Viết một câu lệnh `if` để kiểm tra xem màu của người ngoài hành tinh có phải là xanh lá không. Nếu đúng, in ra thông điệp cho biết người chơi vừa được 5 điểm.

- Viết một phiên bản của chương trình này vượt qua phép kiểm tra `if` và một phiên bản khác không vượt qua. (Phiên bản không vượt qua sẽ không có đầu ra.)

**5-4. Màu người ngoài hành tinh #2:** Chọn một màu cho người ngoài hành tinh như bạn đã làm trong Bài tập 5-3, và viết một chuỗi `if`-`else`.

- Nếu màu của người ngoài hành tinh là xanh lá, in ra một câu cho biết người chơi vừa được 5 điểm vì bắn trúng người ngoài hành tinh.

- Nếu màu của người ngoài hành tinh không phải xanh lá, in ra một câu cho biết người chơi vừa được 10 điểm.

- Viết một phiên bản của chương trình này chạy khối `if` và một phiên bản khác chạy khối `else`.

<!-- pdf-page: 122 | printed: 89 -->

**5-5. Màu người ngoài hành tinh #3:** Chuyển chuỗi `if`-`else` từ Bài tập 5-4 thành một chuỗi `if`-`elif`- `else`.

- Nếu người ngoài hành tinh màu xanh lá, in ra thông điệp cho biết người chơi được 5 điểm.

- Nếu người ngoài hành tinh màu vàng, in ra thông điệp cho biết người chơi được 10 điểm.

- Nếu người ngoài hành tinh màu đỏ, in ra thông điệp cho biết người chơi được 15 điểm.

- Viết ba phiên bản của chương trình này, đảm bảo mỗi thông điệp được in ra cho đúng màu người ngoài hành tinh.

**5-6. Các giai đoạn cuộc đời:** Viết một chuỗi `if`-`elif`-`else` xác định giai đoạn cuộc đời của một người. Gán một giá trị cho biến `age`, rồi:

- Nếu người đó dưới 2 tuổi, in ra thông điệp cho biết người đó là em bé.

- Nếu người đó từ 2 tuổi trở lên nhưng dưới 4 tuổi, in ra thông điệp cho biết người đó là trẻ mới biết đi.

- Nếu người đó từ 4 tuổi trở lên nhưng dưới 13 tuổi, in ra thông điệp cho biết người đó là trẻ em.

- Nếu người đó từ 13 tuổi trở lên nhưng dưới 20 tuổi, in ra thông điệp cho biết người đó là thiếu niên.

- Nếu người đó từ 20 tuổi trở lên nhưng dưới 65 tuổi, in ra thông điệp cho biết người đó là người trưởng thành.

- Nếu người đó từ 65 tuổi trở lên, in ra thông điệp cho biết người đó là người cao tuổi.

**5-7. Trái cây yêu thích:** Tạo một list các loại trái cây bạn yêu thích, rồi viết một loạt câu lệnh `if` độc lập để kiểm tra một số loại trái cây nhất định có trong list hay không.

- Tạo một list gồm ba loại trái cây bạn yêu thích nhất và đặt tên là `favorite_fruits`.

- Viết năm câu lệnh `if`. Mỗi câu lệnh kiểm tra xem một loại trái cây nhất định có trong list của bạn không. Nếu loại trái cây đó có trong list, khối `if` nên in ra một câu, chẳng hạn như *You really like bananas!*

<!-- /box -->

## Dùng câu lệnh if với list

Bạn có thể làm một số việc thú vị khi kết hợp list với câu lệnh `if`. Bạn có thể để ý những giá trị đặc biệt cần được xử lý khác với các giá trị khác trong list. Bạn có thể quản lý hiệu quả những điều kiện thay đổi, chẳng hạn như tình trạng còn hay hết của một số món trong nhà hàng trong suốt một ca làm việc. Bạn cũng có thể bắt đầu chứng minh rằng mã của mình hoạt động như mong đợi trong mọi tình huống có thể xảy ra.

<!-- pdf-page: 123 | printed: 90 -->

### Kiểm tra các phần tử đặc biệt

Chương này bắt đầu bằng một ví dụ đơn giản cho thấy cách xử lý một giá trị đặc biệt như `'bmw'`, giá trị cần được in theo định dạng khác với các giá trị khác trong list. Giờ đây khi bạn đã hiểu cơ bản về phép kiểm tra điều kiện và câu lệnh `if`, hãy xem kỹ hơn cách bạn có thể để ý những giá trị đặc biệt trong list và xử lý chúng một cách phù hợp.

Hãy tiếp tục với ví dụ về tiệm pizza. Tiệm pizza hiển thị một thông điệp mỗi khi một loại topping được thêm vào chiếc pizza của bạn trong lúc làm bánh. Đoạn mã cho hành động này có thể được viết rất hiệu quả bằng cách tạo một list các topping khách hàng đã yêu cầu và dùng một vòng lặp để thông báo từng topping khi nó được thêm vào pizza:

**toppings.py**

```python
requested_toppings = ['mushrooms', 'green peppers', 'extra cheese']

for requested_topping in requested_toppings:
    print("Adding " + requested_topping + ".")

print("\nFinished making your pizza!")
```

Đầu ra khá đơn giản vì đoạn mã này chỉ là một vòng lặp `for` đơn giản:

```text
Adding mushrooms.
Adding green peppers.
Adding extra cheese.

Finished making your pizza!
```

Nhưng nếu tiệm pizza hết ớt chuông xanh thì sao? Một câu lệnh `if` bên trong vòng lặp `for` có thể xử lý tình huống này một cách phù hợp:

```python
  requested_toppings = ['mushrooms', 'green peppers', 'extra cheese']

  for requested_topping in requested_toppings:
❶     if requested_topping == 'green peppers':
          print("Sorry, we are out of green peppers right now.")
❷     else:
          print("Adding " + requested_topping + ".")

  print("\nFinished making your pizza!")
```

Lần này, chúng ta kiểm tra từng món được yêu cầu trước khi thêm nó vào pizza. Đoạn mã tại ❶ kiểm tra xem người đó có yêu cầu ớt chuông xanh không. Nếu có, chúng ta hiển thị một thông điệp cho họ biết vì sao họ không thể có ớt chuông xanh. Khối `else` tại ❷ đảm bảo tất cả các topping khác sẽ được thêm vào pizza.

<!-- pdf-page: 124 | printed: 91 -->

Đầu ra cho thấy mỗi topping được yêu cầu đều được xử lý phù hợp.

```text
Adding mushrooms.
Sorry, we are out of green peppers right now.
Adding extra cheese.

Finished making your pizza!
```

### Kiểm tra list không rỗng

Chúng ta đã đưa ra một giả định đơn giản về mọi list mà ta làm việc cùng cho đến giờ: ta giả định mỗi list có ít nhất một phần tử. Chẳng bao lâu nữa, chúng ta sẽ để người dùng cung cấp thông tin được lưu trong list, nên ta sẽ không thể giả định rằng list có phần tử nào mỗi khi vòng lặp chạy. Trong tình huống này, việc kiểm tra xem list có rỗng không trước khi chạy vòng lặp `for` là rất hữu ích.

Ví dụ, hãy kiểm tra xem list các topping được yêu cầu có rỗng không trước khi làm pizza. Nếu list rỗng, chúng ta sẽ hỏi người dùng để chắc chắn họ muốn một chiếc pizza không topping. Nếu list không rỗng, ta sẽ làm pizza giống như trong các ví dụ trước:

```python
❶ requested_toppings = []

❷ if requested_toppings:
      for requested_topping in requested_toppings:
          print("Adding " + requested_topping + ".")
      print("\nFinished making your pizza!")
❸ else:
      print("Are you sure you want a plain pizza?")
```

Lần này, chúng ta bắt đầu với một list topping được yêu cầu rỗng tại ❶. Thay vì nhảy ngay vào vòng lặp `for`, ta kiểm tra nhanh tại ❷. Khi tên của một list được dùng trong câu lệnh `if`, Python trả về `True` nếu list chứa ít nhất một phần tử; một list rỗng được đánh giá là `False`. Nếu `requested_toppings` vượt qua phép kiểm tra điều kiện, ta chạy cùng vòng lặp `for` đã dùng trong ví dụ trước. Nếu phép kiểm tra điều kiện thất bại, ta in ra một thông điệp hỏi khách hàng có thực sự muốn một chiếc pizza không có topping nào không ❸.

Trong trường hợp này list rỗng, nên đầu ra hỏi người dùng có thực sự muốn một chiếc pizza không topping không:

```text
Are you sure you want a plain pizza?
```

Nếu list không rỗng, đầu ra sẽ hiển thị từng topping được yêu cầu khi nó được thêm vào pizza.

<!-- pdf-page: 125 | printed: 92 -->

### Dùng nhiều list

Người ta sẽ yêu cầu đủ thứ, đặc biệt là khi nói đến topping pizza. Nếu một khách hàng thực sự muốn có khoai tây chiên trên pizza thì sao? Bạn có thể dùng list và câu lệnh `if` để đảm bảo dữ liệu đầu vào hợp lý trước khi xử lý.

Hãy để ý những yêu cầu topping bất thường trước khi làm pizza. Ví dụ sau định nghĩa hai list. List thứ nhất là list các topping có sẵn ở tiệm pizza, và list thứ hai là list các topping người dùng đã yêu cầu. Lần này, mỗi phần tử trong `requested_toppings` được đối chiếu với list topping có sẵn trước khi được thêm vào pizza:

```python
❶ available_toppings = ['mushrooms', 'olives', 'green peppers',
                        'pepperoni', 'pineapple', 'extra cheese']

❷ requested_toppings = ['mushrooms', 'french fries', 'extra cheese']

❸ for requested_topping in requested_toppings:
❹     if requested_topping in available_toppings:
          print("Adding " + requested_topping + ".")
❺     else:
          print("Sorry, we don't have " + requested_topping + ".")

  print("\nFinished making your pizza!")
```

Tại ❶, chúng ta định nghĩa một list các topping có sẵn ở tiệm pizza này. Lưu ý rằng đây có thể là một tuple nếu tiệm pizza có một lựa chọn topping cố định. Tại ❷, chúng ta tạo một list các topping mà khách hàng đã yêu cầu. Hãy để ý yêu cầu bất thường, `'french fries'`. Tại ❸, chúng ta lặp qua list các topping được yêu cầu. Bên trong vòng lặp, trước tiên ta kiểm tra xem từng topping được yêu cầu có thực sự nằm trong list topping có sẵn không ❹. Nếu có, ta thêm topping đó vào pizza. Nếu topping được yêu cầu không nằm trong list topping có sẵn, khối `else` sẽ chạy ❺. Khối `else` in ra một thông điệp cho người dùng biết những topping nào không có sẵn.

Cú pháp mã này cho ra đầu ra gọn gàng, đầy đủ thông tin:

```text
Adding mushrooms.
Sorry, we don't have french fries.
Adding extra cheese.

Finished making your pizza!
```

Chỉ với vài dòng mã, chúng ta đã xử lý khá hiệu quả một tình huống thực tế!

<!-- pdf-page: 126 | printed: 93 -->

<!-- box -->

**Tự mình thực hành**

**5-8. Chào admin:** Tạo một list gồm năm tên người dùng trở lên, trong đó có tên `'admin'`. Hãy tưởng tượng bạn đang viết mã in ra lời chào cho từng người dùng sau khi họ đăng nhập vào một trang web. Lặp qua list và in ra lời chào cho từng người dùng:

- Nếu tên người dùng là `'admin'`, in ra một lời chào đặc biệt, chẳng hạn như *Hello admin, would you like to see a status report?*

- Nếu không, in ra một lời chào chung, chẳng hạn như *Hello Eric, thank you for logging in again.*

**5-9. Không có người dùng:** Thêm một phép kiểm tra `if` vào *hello_admin.py* để đảm bảo list người dùng không rỗng.

- Nếu list rỗng, in ra thông điệp *We need to find some users!*

- Xóa tất cả các tên người dùng khỏi list và đảm bảo thông điệp đúng được in ra.

**5-10. Kiểm tra tên người dùng:** Làm những việc sau để tạo một chương trình mô phỏng cách các trang web đảm bảo mọi người đều có tên người dùng duy nhất.

- Tạo một list gồm năm tên người dùng trở lên, đặt tên là `current_users`.

- Tạo một list khác gồm năm tên người dùng, đặt tên là `new_users`. Đảm bảo một hoặc hai tên người dùng mới cũng có trong list `current_users`.

- Lặp qua list `new_users` để xem từng tên người dùng mới đã được sử dụng chưa. Nếu đã được sử dụng, in ra thông điệp cho biết người đó cần nhập một tên người dùng mới. Nếu một tên người dùng chưa được sử dụng, in ra thông điệp cho biết tên người dùng đó còn trống.

- Đảm bảo phép so sánh của bạn không phân biệt chữ hoa, chữ thường. Nếu `'John'` đã được sử dụng, `'JOHN'` sẽ không được chấp nhận.

**5-11. Số thứ tự:** Số thứ tự (ordinal number) cho biết vị trí trong một danh sách, chẳng hạn như *1st* hoặc *2nd*. Hầu hết các số thứ tự trong tiếng Anh kết thúc bằng *th*, trừ 1, 2 và 3.

- Lưu các số từ 1 đến 9 vào một list.

- Lặp qua list đó.

- Dùng một chuỗi `if`-`elif`-`else` bên trong vòng lặp để in ra đuôi số thứ tự đúng cho từng số. Đầu ra của bạn nên là `"1st 2nd 3rd 4th 5th 6th 7th 8th 9th"`, và mỗi kết quả nên nằm trên một dòng riêng.

<!-- /box -->

<!-- pdf-page: 127 | printed: 94 -->

## Định dạng phong cách câu lệnh if

Trong mọi ví dụ của chương này, bạn đã thấy những thói quen định dạng tốt. Khuyến nghị duy nhất mà PEP 8 đưa ra về định dạng phép kiểm tra điều kiện là dùng một dấu cách ở hai bên các toán tử so sánh, chẳng hạn `==`, `>=`, `<=`. Ví dụ:

```python
if age < 4:
```

tốt hơn:

```python
if age<4:
```

Khoảng cách như vậy không ảnh hưởng đến cách Python hiểu mã của bạn; nó chỉ giúp bạn và người khác đọc mã dễ dàng hơn.

<!-- box -->

**Tự mình thực hành**

**5-12. Định dạng phong cách câu lệnh** `if`**:** Xem lại các chương trình bạn đã viết trong chương này và đảm bảo bạn đã định dạng các phép kiểm tra điều kiện một cách phù hợp.

**5-13. Ý tưởng của bạn:** Đến lúc này, bạn đã là một lập trình viên có năng lực hơn so với khi bắt đầu đọc cuốn sách này. Giờ đây khi đã hiểu rõ hơn cách các tình huống thực tế được mô hình hóa trong chương trình, có thể bạn đang nghĩ đến một số vấn đề mà mình có thể giải quyết bằng chương trình của riêng mình. Hãy ghi lại mọi ý tưởng mới về những vấn đề bạn có thể muốn giải quyết khi kỹ năng lập trình tiếp tục được nâng cao. Hãy nghĩ đến những trò chơi bạn có thể muốn viết, những tập dữ liệu bạn có thể muốn khám phá, và những ứng dụng web bạn muốn tạo ra.

<!-- /box -->

## Tổng kết

Trong chương này, bạn đã học cách viết các phép kiểm tra điều kiện, luôn được đánh giá là `True` hoặc `False`. Bạn đã học cách viết câu lệnh `if` đơn giản, chuỗi `if`-`else` và chuỗi `if`-`elif`-`else`. Bạn đã bắt đầu dùng các cấu trúc này để xác định những điều kiện cụ thể cần kiểm tra và biết khi nào các điều kiện đó được thỏa mãn trong chương trình. Bạn đã học cách xử lý một số phần tử trong list khác với tất cả các phần tử còn lại, trong khi vẫn tận dụng được sự hiệu quả của vòng lặp `for`. Bạn cũng đã xem lại các khuyến nghị về phong cách của Python để đảm bảo những chương trình ngày càng phức tạp của bạn vẫn tương đối dễ đọc và dễ hiểu.

Trong Chương 6, bạn sẽ tìm hiểu về dictionary của Python. Dictionary tương tự list, nhưng cho phép bạn kết nối các mẩu thông tin với nhau. Bạn sẽ học cách xây dựng dictionary, lặp qua chúng, và dùng chúng kết hợp với list và câu lệnh `if`. Tìm hiểu về dictionary sẽ giúp bạn mô hình hóa được nhiều tình huống thực tế đa dạng hơn nữa.

<!-- source: pythoncrashcourse.pdf | unit: chapter-09 | pdf pages 194-221 | printed 161-188 -->

# Chương 9: Lớp

<!-- pdf-page: 194 | printed: 161 -->

*Lập trình hướng đối tượng* (object-oriented programming) là một trong những cách tiếp cận hiệu quả nhất để viết phần mềm. Trong lập trình hướng đối tượng, bạn viết các *lớp* (class) biểu diễn những sự vật và tình huống trong thế giới thực, rồi tạo ra các *đối tượng* (object) dựa trên những lớp này. Khi viết một lớp, bạn định nghĩa hành vi chung mà cả một nhóm đối tượng có thể có.

Khi tạo các đối tượng riêng lẻ từ lớp, mỗi đối tượng tự động được trang bị hành vi chung đó; sau đó, bạn có thể cho mỗi đối tượng bất kỳ đặc điểm riêng nào bạn muốn. Bạn sẽ ngạc nhiên khi thấy các tình huống thực tế có thể được mô hình hóa tốt đến mức nào bằng lập trình hướng đối tượng.

Việc tạo một đối tượng từ một lớp được gọi là *khởi tạo thực thể* (instantiation), và bạn làm việc với các *thực thể* (instance) của một lớp. Trong chương này, bạn sẽ viết các lớp và tạo thực thể của những lớp đó. Bạn sẽ chỉ định loại thông tin có thể được lưu trong các thực thể, và định nghĩa những hành động có thể thực hiện với các thực thể này. Bạn cũng sẽ viết những lớp mở rộng chức năng của các lớp có sẵn, để các lớp tương tự nhau có thể chia sẻ mã một cách hiệu quả. Bạn sẽ lưu các lớp của mình trong module và import những lớp do các lập trình viên khác viết vào file chương trình của bạn.

<!-- pdf-page: 195 | printed: 162 -->

Hiểu về lập trình hướng đối tượng sẽ giúp bạn nhìn thế giới như một lập trình viên. Nó giúp bạn thực sự hiểu mã của mình — không chỉ những gì đang diễn ra trên từng dòng, mà cả những khái niệm lớn hơn ẩn sau đó. Hiểu được logic đằng sau các lớp sẽ rèn luyện cho bạn tư duy logic, để bạn có thể viết những chương trình giải quyết hiệu quả hầu như mọi vấn đề bạn gặp phải.

Lớp cũng giúp cuộc sống dễ dàng hơn cho bạn và các lập trình viên khác mà bạn sẽ cần cộng tác khi đối mặt với những thử thách ngày càng phức tạp. Khi bạn và các lập trình viên khác viết mã dựa trên cùng một kiểu logic, các bạn sẽ hiểu được công việc của nhau. Chương trình của bạn sẽ dễ hiểu đối với nhiều cộng sự, giúp mọi người cùng làm được nhiều việc hơn.

## Tạo và sử dụng lớp

Bạn có thể mô hình hóa hầu như bất cứ thứ gì bằng lớp. Hãy bắt đầu bằng việc viết một lớp đơn giản, `Dog`, biểu diễn một chú chó — không phải một chú chó cụ thể nào, mà là bất kỳ chú chó nào. Chúng ta biết gì về hầu hết những chú chó nuôi trong nhà? Chà, chúng đều có tên và tuổi. Chúng ta cũng biết rằng hầu hết các chú chó đều biết ngồi và lăn tròn. Hai mẩu thông tin này (tên và tuổi) và hai hành vi này (ngồi và lăn tròn) sẽ được đưa vào lớp `Dog` của chúng ta, vì chúng là điểm chung của hầu hết các chú chó. Lớp này sẽ cho Python biết cách tạo một đối tượng biểu diễn một chú chó. Sau khi viết xong lớp, chúng ta sẽ dùng nó để tạo các thực thể riêng lẻ, mỗi thực thể biểu diễn một chú chó cụ thể.

### Tạo lớp Dog

Mỗi thực thể được tạo từ lớp `Dog` sẽ lưu một `name` và một `age`, và chúng ta sẽ cho mỗi chú chó khả năng `sit()` (ngồi) và `roll_over()` (lăn tròn):

**dog.py**

```python
❶ class Dog():
❷     """A simple attempt to model a dog."""

❸     def __init__(self, name, age):
          """Initialize name and age attributes."""
❹         self.name = name
          self.age = age

❺     def sit(self):
          """Simulate a dog sitting in response to a command."""
          print(self.name.title() + " is now sitting.")

      def roll_over(self):
          """Simulate rolling over in response to a command."""
          print(self.name.title() + " rolled over!")
```

<!-- pdf-page: 196 | printed: 163 -->

Có rất nhiều điều cần để ý ở đây, nhưng đừng lo. Bạn sẽ gặp cấu trúc này xuyên suốt chương này và có nhiều thời gian để làm quen với nó. Tại ❶, chúng ta định nghĩa một lớp có tên `Dog`. Theo quy ước, tên viết hoa chữ cái đầu chỉ lớp trong Python. Cặp ngoặc đơn trong định nghĩa lớp để trống vì chúng ta đang tạo lớp này từ đầu. Tại ❷, ta viết một docstring mô tả lớp này làm gì.

#### Phương thức __init__()

Một hàm là một phần của lớp được gọi là *phương thức* (method). Mọi điều bạn đã học về hàm cũng áp dụng cho phương thức; điểm khác biệt thực tế duy nhất lúc này là cách chúng ta gọi phương thức. Phương thức `__init__()` tại ❸ là một phương thức đặc biệt mà Python tự động chạy mỗi khi chúng ta tạo một thực thể mới dựa trên lớp `Dog`. Phương thức này có hai dấu gạch dưới ở đầu và hai dấu gạch dưới ở cuối, một quy ước giúp tránh việc tên các phương thức mặc định của Python xung đột với tên phương thức của bạn.

Chúng ta định nghĩa phương thức `__init__()` có ba tham số: `self`, `name` và `age`. Tham số `self` là bắt buộc trong định nghĩa phương thức, và nó phải đứng đầu, trước các tham số khác. Nó phải có mặt trong định nghĩa vì khi Python gọi phương thức `__init__()` này về sau (để tạo một thực thể của `Dog`), lời gọi phương thức sẽ tự động truyền đối số `self`. Mọi lời gọi phương thức gắn với một lớp đều tự động truyền `self`, một tham chiếu tới chính thực thể đó; nó cho phép từng thực thể truy cập các thuộc tính và phương thức trong lớp. Khi tạo một thực thể của `Dog`, Python sẽ gọi phương thức `__init__()` từ lớp `Dog`. Chúng ta sẽ truyền cho `Dog()` một cái tên và một độ tuổi làm đối số; `self` được truyền tự động, nên ta không cần truyền nó. Bất cứ khi nào muốn tạo một thực thể từ lớp `Dog`, ta chỉ cần cung cấp giá trị cho hai tham số cuối, `name` và `age`.

Hai biến được định nghĩa tại ❹ đều có tiền tố `self`. Mọi biến có tiền tố `self` đều có thể được dùng trong mọi phương thức của lớp, và chúng ta cũng có thể truy cập các biến này thông qua bất kỳ thực thể nào được tạo từ lớp. `self.name = name` lấy giá trị được lưu trong tham số `name` và lưu nó vào biến `name`, biến này sau đó được gắn với thực thể đang được tạo. Quá trình tương tự xảy ra với `self.age = age`. Những biến có thể truy cập thông qua thực thể như thế này được gọi là *thuộc tính* (attribute).

Lớp `Dog` có hai phương thức khác được định nghĩa: `sit()` và `roll_over()` ❺. Vì các phương thức này không cần thêm thông tin như tên hay tuổi, chúng ta chỉ định nghĩa chúng với một tham số, `self`. Các thực thể mà ta tạo ra sau này sẽ truy cập được các phương thức này. Nói cách khác, chúng sẽ có thể ngồi và lăn tròn. Hiện tại, `sit()` và `roll_over()` chưa làm được gì nhiều. Chúng chỉ in ra một thông điệp cho biết chú chó đang ngồi hoặc đang lăn tròn. Nhưng khái niệm này có thể được mở rộng cho những tình huống thực tế: nếu lớp này là một phần của một trò chơi máy tính thực sự, các phương thức này sẽ chứa mã để làm một chú chó hoạt hình ngồi và lăn tròn. Nếu lớp này được viết để điều khiển robot, các phương thức này sẽ chỉ đạo các chuyển động khiến một chú chó robot ngồi và lăn tròn.

<!-- pdf-page: 197 | printed: 164 -->

#### Tạo lớp trong Python 2.7

Khi tạo lớp trong Python 2.7, bạn cần thực hiện một thay đổi nhỏ. Bạn đưa từ `object` vào trong cặp ngoặc đơn khi tạo lớp:

```python
class ClassName(object):
    --snip--
```

Điều này khiến các lớp trong Python 2.7 hoạt động giống các lớp trong Python 3 hơn, giúp công việc của bạn nhìn chung dễ dàng hơn.

Lớp `Dog` sẽ được định nghĩa như sau trong Python 2.7:

```python
class Dog(object):
    --snip--
```

### Tạo thực thể từ lớp

Hãy coi một lớp như một bộ hướng dẫn về cách tạo thực thể. Lớp `Dog` là một bộ hướng dẫn cho Python biết cách tạo các thực thể riêng lẻ biểu diễn những chú chó cụ thể.

Hãy tạo một thực thể biểu diễn một chú chó cụ thể:

```python
  class Dog():
      --snip--

❶ my_dog = Dog('willie', 6)

❷ print("My dog's name is " + my_dog.name.title() + ".")
❸ print("My dog is " + str(my_dog.age) + " years old.")
```

Lớp `Dog` mà chúng ta dùng ở đây chính là lớp vừa viết trong ví dụ trước. Tại ❶, ta yêu cầu Python tạo một chú chó có tên là `'willie'` và tuổi là `6`. Khi Python đọc dòng này, nó gọi phương thức `__init__()` trong `Dog` với các đối số `'willie'` và `6`. Phương thức `__init__()` tạo một thực thể biểu diễn chú chó cụ thể này và gán các thuộc tính `name` và `age` bằng các giá trị ta đã cung cấp. Phương thức `__init__()` không có câu lệnh `return` tường minh, nhưng Python tự động trả về một thực thể biểu diễn chú chó này. Ta lưu thực thể đó vào biến `my_dog`. Quy ước đặt tên rất hữu ích ở đây: ta thường có thể giả định rằng một tên viết hoa chữ cái đầu như `Dog` chỉ một lớp, còn một tên viết thường như `my_dog` chỉ một thực thể đơn lẻ được tạo từ một lớp.

#### Truy cập thuộc tính

Để truy cập các thuộc tính của một thực thể, bạn dùng ký hiệu dấu chấm. Tại ❷, chúng ta truy cập giá trị của thuộc tính `name` của `my_dog` bằng cách viết:

```text
my_dog.name
```

Ký hiệu dấu chấm được dùng thường xuyên trong Python. Cú pháp này cho thấy cách Python tìm giá trị của một thuộc tính. Ở đây, Python nhìn vào thực thể `my_dog` rồi tìm thuộc tính `name` gắn với `my_dog`. Đây chính là thuộc tính được gọi là `self.name` trong lớp `Dog`. Tại ❸, ta dùng cách tương tự để làm việc với thuộc tính `age`. Trong câu lệnh `print` đầu tiên, `my_dog.name.title()` khiến `'willie'`, giá trị của thuộc tính `name` của `my_dog`, bắt đầu bằng một chữ cái viết hoa. Trong câu lệnh `print` thứ hai, `str(my_dog.age)` chuyển `6`, giá trị của thuộc tính `age` của `my_dog`, thành một chuỗi.

<!-- pdf-page: 198 | printed: 165 -->

Đầu ra là bản tóm tắt những gì chúng ta biết về `my_dog`:

```text
My dog's name is Willie.
My dog is 6 years old.
```

#### Gọi phương thức

Sau khi tạo một thực thể từ lớp `Dog`, chúng ta có thể dùng ký hiệu dấu chấm để gọi bất kỳ phương thức nào được định nghĩa trong `Dog`. Hãy cho chú chó của chúng ta ngồi và lăn tròn:

```python
class Dog():
    --snip--

my_dog = Dog('willie', 6)
my_dog.sit()
my_dog.roll_over()
```

Để gọi một phương thức, hãy viết tên của thực thể (trong trường hợp này là `my_dog`) và phương thức bạn muốn gọi, phân tách bằng một dấu chấm. Khi Python đọc `my_dog.sit()`, nó tìm phương thức `sit()` trong lớp `Dog` và chạy đoạn mã đó. Python hiểu dòng `my_dog.roll_over()` theo cách tương tự.

Giờ Willie làm đúng những gì chúng ta bảo:

```text
Willie is now sitting.
Willie rolled over!
```

Cú pháp này khá hữu ích. Khi các thuộc tính và phương thức được đặt những cái tên mang tính mô tả phù hợp như `name`, `age`, `sit()` và `roll_over()`, ta có thể dễ dàng suy ra một khối mã định làm gì, kể cả khối mã ta chưa từng thấy trước đây.

#### Tạo nhiều thực thể

Bạn có thể tạo bao nhiêu thực thể từ một lớp tùy theo nhu cầu. Hãy tạo chú chó thứ hai có tên `your_dog`:

```python
class Dog():
    --snip--

my_dog = Dog('willie', 6)
your_dog = Dog('lucy', 3)

print("My dog's name is " + my_dog.name.title() + ".")
print("My dog is " + str(my_dog.age) + " years old.")
my_dog.sit()
print("\nYour dog's name is " + your_dog.name.title() + ".")
print("Your dog is " + str(your_dog.age) + " years old.")
your_dog.sit()
```

<!-- pdf-page: 199 | printed: 166 -->

Trong ví dụ này, chúng ta tạo một chú chó tên Willie và một chú chó tên Lucy. Mỗi chú chó là một thực thể riêng biệt với bộ thuộc tính của riêng nó, và có thể thực hiện cùng một tập hành động:

```text
My dog's name is Willie.
My dog is 6 years old.
Willie is now sitting.

Your dog's name is Lucy.
Your dog is 3 years old.
Lucy is now sitting.
```

Ngay cả khi chúng ta dùng cùng tên và tuổi cho chú chó thứ hai, Python vẫn tạo ra một thực thể riêng biệt từ lớp `Dog`. Bạn có thể tạo bao nhiêu thực thể từ một lớp tùy theo nhu cầu, miễn là bạn đặt cho mỗi thực thể một tên biến duy nhất, hoặc mỗi thực thể chiếm một vị trí riêng trong một list hay dictionary.

<!-- box -->

**Tự mình thực hành**

**9-1. Nhà hàng:** Tạo một lớp có tên `Restaurant`. Phương thức `__init__()` của `Restaurant` nên lưu hai thuộc tính: `restaurant_name` và `cuisine_type`. Tạo một phương thức có tên `describe_restaurant()` in ra hai mẩu thông tin này, và một phương thức có tên `open_restaurant()` in ra thông điệp cho biết nhà hàng đang mở cửa.

Tạo một thực thể có tên `restaurant` từ lớp của bạn. In riêng từng thuộc tính trong hai thuộc tính, rồi gọi cả hai phương thức.

**9-2. Ba nhà hàng:** Bắt đầu với lớp của bạn từ Bài tập 9-1. Tạo ba thực thể khác nhau từ lớp đó, và gọi `describe_restaurant()` cho từng thực thể.

**9-3. Người dùng:** Tạo một lớp có tên `User`. Tạo hai thuộc tính có tên `first_name` và `last_name`, rồi tạo thêm vài thuộc tính khác thường được lưu trong hồ sơ người dùng. Tạo một phương thức có tên `describe_user()` in ra bản tóm tắt thông tin của người dùng. Tạo thêm một phương thức có tên `greet_user()` in ra một lời chào được cá nhân hóa dành cho người dùng.

Tạo vài thực thể biểu diễn những người dùng khác nhau, và gọi cả hai phương thức cho từng người dùng.

<!-- /box -->

<!-- pdf-page: 200 | printed: 167 -->

## Làm việc với lớp và thực thể

Bạn có thể dùng lớp để biểu diễn nhiều tình huống trong thế giới thực. Sau khi viết một lớp, bạn sẽ dành phần lớn thời gian làm việc với các thực thể được tạo từ lớp đó. Một trong những việc đầu tiên bạn sẽ muốn làm là sửa đổi các thuộc tính gắn với một thực thể cụ thể. Bạn có thể sửa đổi trực tiếp thuộc tính của một thực thể, hoặc viết các phương thức cập nhật thuộc tính theo những cách cụ thể.

### Lớp Car

Hãy viết một lớp mới biểu diễn một chiếc ô tô. Lớp của chúng ta sẽ lưu thông tin về loại ô tô đang xét, và sẽ có một phương thức tóm tắt thông tin này:

**car.py**

```python
  class Car():
      """A simple attempt to represent a car."""

❶     def __init__(self, make, model, year):
          """Initialize attributes to describe a car."""
          self.make = make
          self.model = model
          self.year = year

❷     def get_descriptive_name(self):
          """Return a neatly formatted descriptive name."""
          long_name = str(self.year) + ' ' + self.make + ' ' + self.model
          return long_name.title()

❸ my_new_car = Car('audi', 'a4', 2016)
  print(my_new_car.get_descriptive_name())
```

Tại ❶ trong lớp `Car`, chúng ta định nghĩa phương thức `__init__()` với tham số `self` đứng đầu, giống như đã làm trước đó với lớp `Dog`. Ta cũng cho nó ba tham số khác: `make` (hãng sản xuất), `model` (mẫu xe) và `year` (năm sản xuất). Phương thức `__init__()` nhận các tham số này và lưu chúng vào các thuộc tính sẽ được gắn với những thực thể được tạo từ lớp này. Khi tạo một thực thể `Car` mới, ta sẽ cần chỉ định hãng sản xuất, mẫu xe và năm sản xuất cho thực thể đó.

Tại ❷, chúng ta định nghĩa một phương thức có tên `get_descriptive_name()` đặt `year`, `make` và `model` của chiếc xe vào một chuỗi mô tả chiếc xe một cách gọn gàng. Điều này giúp ta không phải in riêng giá trị của từng thuộc tính. Để làm việc với các giá trị thuộc tính trong phương thức này, ta dùng `self.make`, `self.model` và `self.year`. Tại ❸, ta tạo một thực thể từ lớp `Car` và lưu nó vào biến `my_new_car`. Sau đó, ta gọi `get_descriptive_name()` để hiển thị loại xe mà ta có:

```text
2016 Audi A4
```

Để lớp thú vị hơn, hãy thêm một thuộc tính thay đổi theo thời gian. Chúng ta sẽ thêm một thuộc tính lưu tổng số dặm mà chiếc xe đã đi.

<!-- pdf-page: 201 | printed: 168 -->

### Đặt giá trị mặc định cho thuộc tính

Mọi thuộc tính trong một lớp đều cần một giá trị ban đầu, ngay cả khi giá trị đó là 0 hoặc một chuỗi rỗng. Trong một số trường hợp, chẳng hạn khi đặt giá trị mặc định, việc chỉ định giá trị ban đầu này trong thân phương thức `__init__()` là hợp lý; nếu làm vậy cho một thuộc tính, bạn không cần thêm tham số cho thuộc tính đó.

Hãy thêm một thuộc tính có tên `odometer_reading` luôn bắt đầu với giá trị 0. Chúng ta cũng sẽ thêm một phương thức `read_odometer()` giúp ta đọc đồng hồ đo quãng đường của từng chiếc xe:

```python
  class Car():

      def __init__(self, make, model, year):
          """Initialize attributes to describe a car."""
          self.make = make
          self.model = model
          self.year = year
❶         self.odometer_reading = 0

      def get_descriptive_name(self):
          --snip--

❷     def read_odometer(self):
          """Print a statement showing the car's mileage."""
          print("This car has " + str(self.odometer_reading) + " miles on it.")

  my_new_car = Car('audi', 'a4', 2016)
  print(my_new_car.get_descriptive_name())
  my_new_car.read_odometer()
```

Lần này, khi Python gọi phương thức `__init__()` để tạo một thực thể mới, nó lưu các giá trị hãng sản xuất, mẫu xe và năm sản xuất làm thuộc tính như trong ví dụ trước. Sau đó, Python tạo một thuộc tính mới có tên `odometer_reading` và đặt giá trị ban đầu của nó là 0 ❶. Chúng ta cũng có một phương thức mới có tên `read_odometer()` tại ❷ giúp dễ dàng đọc số dặm của một chiếc xe.

Chiếc xe của chúng ta bắt đầu với số dặm là 0:

```text
2016 Audi A4
This car has 0 miles on it.
```

Không có nhiều chiếc xe được bán ra với đồng hồ đo quãng đường chỉ đúng 0 dặm, nên chúng ta cần một cách để thay đổi giá trị của thuộc tính này.

### Sửa đổi giá trị thuộc tính

Bạn có thể thay đổi giá trị của một thuộc tính theo ba cách: thay đổi giá trị trực tiếp thông qua một thực thể, gán giá trị thông qua một phương thức, hoặc tăng giá trị (cộng thêm một lượng nhất định vào nó) thông qua một phương thức. Hãy xem xét từng cách.

<!-- pdf-page: 202 | printed: 169 -->

#### Sửa đổi trực tiếp giá trị thuộc tính

Cách đơn giản nhất để sửa đổi giá trị của một thuộc tính là truy cập trực tiếp thuộc tính đó thông qua một thực thể. Ở đây, chúng ta đặt trực tiếp số đo trên đồng hồ thành 23:

```python
  class Car():
      --snip--

  my_new_car = Car('audi', 'a4', 2016)
  print(my_new_car.get_descriptive_name())

❶ my_new_car.odometer_reading = 23
  my_new_car.read_odometer()
```

Tại ❶, chúng ta dùng ký hiệu dấu chấm để truy cập thuộc tính `odometer_reading` của chiếc xe và đặt trực tiếp giá trị của nó. Dòng này yêu cầu Python lấy thực thể `my_new_car`, tìm thuộc tính `odometer_reading` gắn với nó, và đặt giá trị của thuộc tính đó thành 23:

```text
2016 Audi A4
This car has 23 miles on it.
```

Đôi khi bạn sẽ muốn truy cập trực tiếp thuộc tính như thế này, nhưng những lúc khác, bạn sẽ muốn viết một phương thức cập nhật giá trị giúp bạn.

#### Sửa đổi giá trị thuộc tính thông qua phương thức

Có những phương thức cập nhật một số thuộc tính nhất định giúp bạn có thể rất hữu ích. Thay vì truy cập trực tiếp thuộc tính, bạn truyền giá trị mới cho một phương thức xử lý việc cập nhật bên trong.

Đây là một ví dụ cho thấy một phương thức có tên `update_odometer()`:

```python
  class Car():
      --snip--

❶     def update_odometer(self, mileage):
          """Set the odometer reading to the given value."""
          self.odometer_reading = mileage

  my_new_car = Car('audi', 'a4', 2016)
  print(my_new_car.get_descriptive_name())

❷ my_new_car.update_odometer(23)
  my_new_car.read_odometer()
```

Sửa đổi duy nhất đối với `Car` là việc thêm `update_odometer()` tại ❶. Phương thức này nhận vào một giá trị số dặm và lưu nó vào `self.odometer_reading`. Tại ❷, chúng ta gọi `update_odometer()` và truyền cho nó `23` làm đối số (tương ứng với tham số `mileage` trong định nghĩa phương thức). Nó đặt số đo trên đồng hồ thành 23, và `read_odometer()` in số đo đó ra:

<!-- pdf-page: 203 | printed: 170 -->

```text
2016 Audi A4
This car has 23 miles on it.
```

Chúng ta có thể mở rộng phương thức `update_odometer()` để làm thêm việc mỗi khi số đo trên đồng hồ được sửa đổi. Hãy thêm một chút logic để đảm bảo không ai cố quay ngược số đo trên đồng hồ:

```python
  class Car():
      --snip--

      def update_odometer(self, mileage):
          """
          Set the odometer reading to the given value.
          Reject the change if it attempts to roll the odometer back.
          """
❶         if mileage >= self.odometer_reading:
              self.odometer_reading = mileage
          else:
❷             print("You can't roll back an odometer!")
```

Giờ `update_odometer()` kiểm tra xem số đo mới có hợp lý không trước khi sửa đổi thuộc tính. Nếu số dặm mới, `mileage`, lớn hơn hoặc bằng số dặm hiện có, `self.odometer_reading`, bạn có thể cập nhật số đo trên đồng hồ thành số dặm mới ❶. Nếu số dặm mới nhỏ hơn số dặm hiện có, bạn sẽ nhận được cảnh báo rằng bạn không thể quay ngược đồng hồ đo quãng đường ❷.

#### Tăng giá trị thuộc tính thông qua phương thức

Đôi khi bạn sẽ muốn tăng giá trị của một thuộc tính thêm một lượng nhất định thay vì đặt một giá trị hoàn toàn mới. Giả sử chúng ta mua một chiếc xe cũ và chạy thêm 100 dặm trong khoảng thời gian từ lúc mua đến lúc đăng ký xe. Đây là một phương thức cho phép ta truyền lượng tăng thêm này và cộng giá trị đó vào số đo trên đồng hồ:

```python
  class Car():
      --snip--

      def update_odometer(self, mileage):
          --snip--

❶     def increment_odometer(self, miles):
          """Add the given amount to the odometer reading."""
          self.odometer_reading += miles

❷ my_used_car = Car('subaru', 'outback', 2013)
  print(my_used_car.get_descriptive_name())

❸ my_used_car.update_odometer(23500)
  my_used_car.read_odometer()
❹ my_used_car.increment_odometer(100)
  my_used_car.read_odometer()
```

<!-- pdf-page: 204 | printed: 171 -->

Phương thức mới `increment_odometer()` tại ❶ nhận vào một số dặm và cộng giá trị này vào `self.odometer_reading`. Tại ❷, chúng ta tạo một chiếc xe cũ, `my_used_car`. Ta đặt đồng hồ của nó thành 23.500 bằng cách gọi `update_odometer()` và truyền cho nó `23500` tại ❸. Tại ❹, ta gọi `increment_odometer()` và truyền cho nó `100` để cộng thêm 100 dặm mà ta đã lái trong khoảng thời gian từ lúc mua xe đến lúc đăng ký:

```text
2013 Subaru Outback
This car has 23500 miles on it.
This car has 23600 miles on it.
```

Bạn có thể dễ dàng sửa đổi phương thức này để từ chối các lượng tăng âm, để không ai dùng hàm này để quay ngược đồng hồ đo quãng đường.

> **Lưu ý** Bạn có thể dùng những phương thức như thế này để kiểm soát cách người dùng chương trình cập nhật các giá trị như số đo trên đồng hồ, nhưng bất kỳ ai có quyền truy cập chương trình đều có thể đặt số đo trên đồng hồ thành bất kỳ giá trị nào bằng cách truy cập trực tiếp thuộc tính. Bảo mật hiệu quả đòi hỏi sự chú ý cực kỳ cẩn thận đến từng chi tiết, bên cạnh những kiểm tra cơ bản như ở đây.

<!-- box -->

**Tự mình thực hành**

**9-4. Số khách đã phục vụ:** Bắt đầu với chương trình của bạn từ Bài tập 9-1 (trang 166). Thêm một thuộc tính có tên `number_served` với giá trị mặc định là 0. Tạo một thực thể có tên `restaurant` từ lớp này. In ra số khách mà nhà hàng đã phục vụ, rồi thay đổi giá trị này và in ra một lần nữa.

Thêm một phương thức có tên `set_number_served()` cho phép bạn đặt số khách đã được phục vụ. Gọi phương thức này với một số mới và in giá trị ra một lần nữa.

Thêm một phương thức có tên `increment_number_served()` cho phép bạn tăng số khách đã được phục vụ. Gọi phương thức này với bất kỳ số nào bạn thích, có thể biểu thị số khách được phục vụ trong, chẳng hạn, một ngày kinh doanh.

**9-5. Số lần đăng nhập:** Thêm một thuộc tính có tên `login_attempts` vào lớp `User` của bạn từ Bài tập 9-3 (trang 166). Viết một phương thức có tên `increment_login_attempts()` tăng giá trị của `login_attempts` thêm 1. Viết một phương thức khác có tên `reset_login_attempts()` đặt lại giá trị của `login_attempts` về 0.

Tạo một thực thể của lớp `User` và gọi `increment_login_attempts()` vài lần. In giá trị của `login_attempts` ra để đảm bảo nó được tăng đúng, rồi gọi `reset_login_attempts()`. In `login_attempts` ra một lần nữa để đảm bảo nó đã được đặt lại về 0.

<!-- /box -->

<!-- pdf-page: 205 | printed: 172 -->

## Kế thừa

Không phải lúc nào bạn cũng phải bắt đầu từ đầu khi viết một lớp. Nếu lớp bạn đang viết là một phiên bản chuyên biệt hóa của một lớp khác mà bạn đã viết, bạn có thể dùng *kế thừa* (inheritance). Khi một lớp *kế thừa* từ một lớp khác, nó tự động nhận tất cả các thuộc tính và phương thức của lớp thứ nhất. Lớp ban đầu được gọi là *lớp cha* (parent class), và lớp mới là *lớp con* (child class). Lớp con kế thừa mọi thuộc tính và phương thức từ lớp cha, nhưng cũng được tự do định nghĩa các thuộc tính và phương thức mới của riêng nó.

### Phương thức __init__() của lớp con

Nhiệm vụ đầu tiên của Python khi tạo một thực thể từ lớp con là gán giá trị cho tất cả các thuộc tính trong lớp cha. Để làm điều này, phương thức `__init__()` của lớp con cần sự trợ giúp từ lớp cha của nó.

Ví dụ, hãy mô hình hóa một chiếc ô tô điện. Ô tô điện chỉ là một loại ô tô cụ thể, nên chúng ta có thể xây dựng lớp `ElectricCar` mới dựa trên lớp `Car` đã viết trước đó. Khi đó, ta chỉ phải viết mã cho các thuộc tính và hành vi riêng của ô tô điện.

Hãy bắt đầu bằng việc tạo một phiên bản đơn giản của lớp `ElectricCar`, làm được mọi thứ mà lớp `Car` làm được:

**electric_car.py**

```python
❶ class Car():
      """A simple attempt to represent a car."""

      def __init__(self, make, model, year):
          self.make = make
          self.model = model
          self.year = year
          self.odometer_reading = 0

      def get_descriptive_name(self):
          long_name = str(self.year) + ' ' + self.make + ' ' + self.model
          return long_name.title()

      def read_odometer(self):
          print("This car has " + str(self.odometer_reading) + " miles on it.")

      def update_odometer(self, mileage):
          if mileage >= self.odometer_reading:
              self.odometer_reading = mileage
          else:
              print("You can't roll back an odometer!")

      def increment_odometer(self, miles):
          self.odometer_reading += miles

❷ class ElectricCar(Car):
      """Represent aspects of a car, specific to electric vehicles."""
❸     def __init__(self, make, model, year):
          """Initialize attributes of the parent class."""
❹         super().__init__(make, model, year)


❺ my_tesla = ElectricCar('tesla', 'model s', 2016)
  print(my_tesla.get_descriptive_name())
```

<!-- pdf-page: 206 | printed: 173 -->

Tại ❶, chúng ta bắt đầu với `Car`. Khi tạo một lớp con, lớp cha phải là một phần của file hiện tại và phải xuất hiện trước lớp con trong file. Tại ❷, ta định nghĩa lớp con, `ElectricCar`. Tên của lớp cha phải được đặt trong cặp ngoặc đơn trong định nghĩa của lớp con. Phương thức `__init__()` tại ❸ nhận vào những thông tin cần thiết để tạo một thực thể `Car`.

Hàm `super()` tại ❹ là một hàm đặc biệt giúp Python tạo liên kết giữa lớp cha và lớp con. Dòng này yêu cầu Python gọi phương thức `__init__()` từ lớp cha của `ElectricCar`, giúp một thực thể `ElectricCar` có tất cả các thuộc tính của lớp cha. Cái tên *super* xuất phát từ quy ước gọi lớp cha là *superclass* (lớp cha) và lớp con là *subclass* (lớp con).

Chúng ta kiểm tra xem kế thừa có hoạt động đúng không bằng cách thử tạo một chiếc ô tô điện với cùng loại thông tin mà ta sẽ cung cấp khi tạo một chiếc ô tô thông thường. Tại ❺, ta tạo một thực thể của lớp `ElectricCar` và lưu nó vào `my_tesla`. Dòng này gọi phương thức `__init__()` được định nghĩa trong `ElectricCar`, phương thức này đến lượt nó yêu cầu Python gọi phương thức `__init__()` được định nghĩa trong lớp cha `Car`. Ta cung cấp các đối số `'tesla'`, `'model s'` và `2016`.

Ngoài `__init__()`, hiện chưa có thuộc tính hay phương thức nào dành riêng cho ô tô điện. Ở thời điểm này, chúng ta chỉ đang đảm bảo rằng ô tô điện có các hành vi phù hợp của `Car`:

```text
2016 Tesla Model S
```

Thực thể `ElectricCar` hoạt động giống hệt một thực thể của `Car`, nên giờ chúng ta có thể bắt đầu định nghĩa các thuộc tính và phương thức dành riêng cho ô tô điện.

### Kế thừa trong Python 2.7

Trong Python 2.7, kế thừa hơi khác một chút. Lớp `ElectricCar` sẽ trông như thế này:

```python
class Car(object):
    def __init__(self, make, model, year):
        --snip--

class ElectricCar(Car):
    def __init__(self, make, model, year):
        super(ElectricCar, self).__init__(make, model, year)
        --snip--
```

<!-- pdf-page: 207 | printed: 174 -->

Hàm `super()` cần hai đối số: một tham chiếu tới lớp con và đối tượng `self`. Các đối số này là cần thiết để giúp Python tạo liên kết đúng đắn giữa lớp cha và lớp con. Khi dùng kế thừa trong Python 2.7, hãy đảm bảo bạn cũng định nghĩa lớp cha bằng cú pháp `object`.

### Định nghĩa thuộc tính và phương thức cho lớp con

Khi đã có một lớp con kế thừa từ một lớp cha, bạn có thể thêm bất kỳ thuộc tính và phương thức mới nào cần thiết để phân biệt lớp con với lớp cha.

Hãy thêm một thuộc tính dành riêng cho ô tô điện (chẳng hạn một bộ pin) và một phương thức báo cáo về thuộc tính này. Chúng ta sẽ lưu dung lượng pin và viết một phương thức in ra mô tả về bộ pin:

```python
  class Car():
      --snip--

  class ElectricCar(Car):
      """Represent aspects of a car, specific to electric vehicles."""

      def __init__(self, make, model, year):
          """
          Initialize attributes of the parent class.
          Then initialize attributes specific to an electric car.
          """
          super().__init__(make, model, year)
❶         self.battery_size = 70

❷     def describe_battery(self):
          """Print a statement describing the battery size."""
          print("This car has a " + str(self.battery_size) + "-kWh battery.")

  my_tesla = ElectricCar('tesla', 'model s', 2016)
  print(my_tesla.get_descriptive_name())
  my_tesla.describe_battery()
```

Tại ❶, chúng ta thêm một thuộc tính mới `self.battery_size` và đặt giá trị ban đầu của nó là, chẳng hạn, `70`. Thuộc tính này sẽ được gắn với mọi thực thể được tạo từ lớp `ElectricCar`, nhưng sẽ không được gắn với bất kỳ thực thể nào của `Car`. Ta cũng thêm một phương thức có tên `describe_battery()` in ra thông tin về bộ pin tại ❷. Khi gọi phương thức này, ta nhận được một mô tả rõ ràng là dành riêng cho ô tô điện:

```text
2016 Tesla Model S
This car has a 70-kWh battery.
```

Không có giới hạn nào về mức độ chuyên biệt hóa lớp `ElectricCar`. Bạn có thể thêm bao nhiêu thuộc tính và phương thức tùy ý để mô hình hóa một chiếc ô tô điện ở bất kỳ mức độ chính xác nào bạn cần. Một thuộc tính hoặc phương thức có thể thuộc về bất kỳ chiếc ô tô nào, chứ không chỉ riêng ô tô điện, nên được thêm vào lớp `Car` thay vì lớp `ElectricCar`. Khi đó, bất kỳ ai dùng lớp `Car` cũng sẽ có sẵn chức năng đó, và lớp `ElectricCar` sẽ chỉ chứa mã cho những thông tin và hành vi dành riêng cho xe điện.

<!-- pdf-page: 208 | printed: 175 -->

### Ghi đè phương thức của lớp cha

Bạn có thể ghi đè (override) bất kỳ phương thức nào của lớp cha không phù hợp với những gì bạn đang cố mô hình hóa bằng lớp con. Để làm điều này, bạn định nghĩa một phương thức trong lớp con có cùng tên với phương thức bạn muốn ghi đè trong lớp cha. Python sẽ bỏ qua phương thức của lớp cha và chỉ để ý đến phương thức bạn định nghĩa trong lớp con.

Giả sử lớp `Car` có một phương thức tên là `fill_gas_tank()` (đổ đầy bình xăng). Phương thức này vô nghĩa đối với một chiếc xe chạy hoàn toàn bằng điện, nên bạn có thể muốn ghi đè phương thức này. Đây là một cách để làm điều đó:

```python
def ElectricCar(Car):
    --snip--

    def fill_gas_tank():
        """Electric cars don't have gas tanks."""
        print("This car doesn't need a gas tank!")
```

Giờ nếu ai đó cố gọi `fill_gas_tank()` với một chiếc ô tô điện, Python sẽ bỏ qua phương thức `fill_gas_tank()` trong `Car` và chạy đoạn mã này thay thế. Khi dùng kế thừa, bạn có thể làm cho các lớp con giữ lại những gì bạn cần và ghi đè bất cứ thứ gì bạn không cần từ lớp cha.

### Dùng thực thể làm thuộc tính

Khi mô hình hóa một thứ gì đó trong thế giới thực bằng mã, bạn có thể thấy mình đang thêm ngày càng nhiều chi tiết vào một lớp. Bạn sẽ thấy list các thuộc tính và phương thức ngày càng dài ra và các file của mình trở nên dài dòng. Trong những tình huống này, bạn có thể nhận ra rằng một phần của một lớp có thể được viết thành một lớp riêng. Bạn có thể chia lớp lớn của mình thành những lớp nhỏ hơn làm việc cùng nhau.

Ví dụ, nếu tiếp tục thêm chi tiết vào lớp `ElectricCar`, chúng ta có thể nhận thấy mình đang thêm nhiều thuộc tính và phương thức dành riêng cho bộ pin của xe. Khi thấy điều này xảy ra, ta có thể dừng lại và chuyển những thuộc tính và phương thức đó sang một lớp riêng có tên `Battery`. Sau đó, ta có thể dùng một thực thể `Battery` làm thuộc tính trong lớp `ElectricCar`:

```python
  class Car():
      --snip--

❶ class Battery():
      """A simple attempt to model a battery for an electric car."""

❷     def __init__(self, battery_size=70):
          """Initialize the battery's attributes."""
          self.battery_size = battery_size
❸     def describe_battery(self):
          """Print a statement describing the battery size."""
          print("This car has a " + str(self.battery_size) + "-kWh battery.")


  class ElectricCar(Car):
      """Represent aspects of a car, specific to electric vehicles."""

      def __init__(self, make, model, year):
          """
          Initialize attributes of the parent class.
          Then initialize attributes specific to an electric car.
          """
          super().__init__(make, model, year)
❹         self.battery = Battery()


  my_tesla = ElectricCar('tesla', 'model s', 2016)

  print(my_tesla.get_descriptive_name())
  my_tesla.battery.describe_battery()
```

<!-- pdf-page: 209 | printed: 176 -->

Tại ❶, chúng ta định nghĩa một lớp mới có tên `Battery` không kế thừa từ lớp nào khác. Phương thức `__init__()` tại ❷ có một tham số, `battery_size`, ngoài `self`. Đây là một tham số tùy chọn, đặt dung lượng pin là 70 nếu không có giá trị nào được cung cấp. Phương thức `describe_battery()` cũng đã được chuyển sang lớp này ❸.

Trong lớp `ElectricCar`, giờ chúng ta thêm một thuộc tính có tên `self.battery` ❹. Dòng này yêu cầu Python tạo một thực thể mới của `Battery` (với dung lượng mặc định là 70, vì ta không chỉ định giá trị) và lưu thực thể đó vào thuộc tính `self.battery`. Điều này sẽ xảy ra mỗi khi phương thức `__init__()` được gọi; giờ đây mọi thực thể `ElectricCar` đều sẽ có một thực thể `Battery` được tạo tự động.

Chúng ta tạo một chiếc ô tô điện và lưu nó vào biến `my_tesla`. Khi muốn mô tả bộ pin, ta cần làm việc thông qua thuộc tính `battery` của chiếc xe:

```text
my_tesla.battery.describe_battery()
```

Dòng này yêu cầu Python nhìn vào thực thể `my_tesla`, tìm thuộc tính `battery` của nó, và gọi phương thức `describe_battery()` gắn với thực thể `Battery` được lưu trong thuộc tính đó.

Đầu ra giống hệt những gì chúng ta đã thấy trước đó:

```text
2016 Tesla Model S
This car has a 70-kWh battery.
```

<!-- pdf-page: 210 | printed: 177 -->

Trông có vẻ phải làm thêm khá nhiều việc, nhưng giờ chúng ta có thể mô tả bộ pin chi tiết đến mức nào tùy thích mà không làm lớp `ElectricCar` trở nên rối rắm. Hãy thêm một phương thức khác vào `Battery` để báo cáo quãng đường xe có thể đi được dựa trên dung lượng pin:

```python
  class Car():
      --snip--

  class Battery():
      --snip--

❶     def get_range(self):
          """Print a statement about the range this battery provides."""
         if self.battery_size == 70:
              range = 240
          elif self.battery_size == 85:
              range = 270

          message = "This car can go approximately " + str(range)
          message += " miles on a full charge."
          print(message)

  class ElectricCar(Car):
      --snip--

  my_tesla = ElectricCar('tesla', 'model s', 2016)
  print(my_tesla.get_descriptive_name())
  my_tesla.battery.describe_battery()
❷ my_tesla.battery.get_range()
```

Phương thức mới `get_range()` tại ❶ thực hiện một số phân tích đơn giản. Nếu dung lượng pin là 70 kWh, `get_range()` đặt quãng đường là 240 dặm, và nếu dung lượng là 85 kWh, nó đặt quãng đường là 270 dặm. Sau đó, nó báo cáo giá trị này. Khi muốn dùng phương thức này, một lần nữa ta phải gọi nó thông qua thuộc tính `battery` của chiếc xe tại ❷.

Đầu ra cho chúng ta biết quãng đường xe có thể đi được dựa trên dung lượng pin:

```text
2016 Tesla Model S
This car has a 70-kWh battery.
This car can go approximately 240 miles on a full charge.
```

### Mô hình hóa các đối tượng trong thế giới thực

Khi bắt đầu mô hình hóa những thứ phức tạp hơn như ô tô điện, bạn sẽ phải vật lộn với những câu hỏi thú vị. Quãng đường đi được của một chiếc ô tô điện là thuộc tính của bộ pin hay của chiếc xe? Nếu chỉ mô tả một chiếc xe, có lẽ giữ phương thức `get_range()` gắn với lớp `Battery` là được. Nhưng nếu mô tả toàn bộ dòng xe của một nhà sản xuất, có lẽ ta sẽ muốn chuyển `get_range()` sang lớp `ElectricCar`. Phương thức `get_range()` vẫn sẽ kiểm tra dung lượng pin trước khi xác định quãng đường, nhưng nó sẽ báo cáo quãng đường dành riêng cho loại xe mà nó gắn với. Hoặc, ta có thể giữ phương thức `get_range()` gắn với bộ pin nhưng truyền cho nó một tham số như `car_model`. Khi đó, phương thức `get_range()` sẽ báo cáo quãng đường dựa trên dung lượng pin và mẫu xe.

<!-- pdf-page: 211 | printed: 178 -->

Điều này đưa bạn đến một điểm thú vị trong quá trình trưởng thành của một lập trình viên. Khi vật lộn với những câu hỏi như thế này, bạn đang tư duy ở mức logic cao hơn, chứ không phải ở mức tập trung vào cú pháp. Bạn không nghĩ về Python, mà nghĩ về cách biểu diễn thế giới thực bằng mã. Khi đạt đến điểm này, bạn sẽ nhận ra rằng thường không có cách tiếp cận nào đúng hay sai khi mô hình hóa các tình huống thực tế. Một số cách tiếp cận hiệu quả hơn những cách khác, nhưng cần luyện tập để tìm ra những cách biểu diễn hiệu quả nhất. Nếu mã của bạn đang hoạt động như bạn muốn, bạn đang làm tốt rồi! Đừng nản lòng nếu thấy mình phải đập đi các lớp và viết lại chúng nhiều lần theo những cách khác nhau. Trên hành trình viết mã chính xác và hiệu quả, ai cũng phải trải qua quá trình này.

<!-- box -->

**Tự mình thực hành**

**9-6. Quầy kem:** Một quầy kem là một loại nhà hàng đặc biệt. Viết một lớp có tên `IceCreamStand` kế thừa từ lớp `Restaurant` mà bạn đã viết trong Bài tập 9-1 (trang 166) hoặc Bài tập 9-4 (trang 171). Phiên bản nào của lớp cũng được; chỉ cần chọn phiên bản bạn thích hơn. Thêm một thuộc tính có tên `flavors` lưu một list các hương vị kem. Viết một phương thức hiển thị các hương vị này. Tạo một thực thể của `IceCreamStand` và gọi phương thức này.

**9-7. Quản trị viên:** Quản trị viên là một loại người dùng đặc biệt. Viết một lớp có tên `Admin` kế thừa từ lớp `User` mà bạn đã viết trong Bài tập 9-3 (trang 166) hoặc Bài tập 9-5 (trang 171). Thêm một thuộc tính, `privileges`, lưu một list các chuỗi như `"can add post"`, `"can delete post"`, `"can ban user"`, v.v. Viết một phương thức có tên `show_privileges()` liệt kê tập quyền hạn của quản trị viên. Tạo một thực thể của `Admin` và gọi phương thức của bạn.

**9-8. Quyền hạn:** Viết một lớp `Privileges` riêng. Lớp này nên có một thuộc tính, `privileges`, lưu một list các chuỗi như mô tả trong Bài tập 9-7. Chuyển phương thức `show_privileges()` sang lớp này. Tạo một thực thể `Privileges` làm thuộc tính trong lớp `Admin`. Tạo một thực thể mới của `Admin` và dùng phương thức của bạn để hiển thị các quyền hạn của nó.

**9-9. Nâng cấp pin:** Dùng phiên bản cuối cùng của *electric_car.py* trong mục này. Thêm một phương thức có tên `upgrade_battery()` vào lớp `Battery`. Phương thức này nên kiểm tra dung lượng pin và đặt dung lượng thành 85 nếu nó chưa phải là 85. Tạo một chiếc ô tô điện với dung lượng pin mặc định, gọi `get_range()` một lần, rồi gọi `get_range()` lần thứ hai sau khi nâng cấp pin. Bạn sẽ thấy quãng đường xe đi được tăng lên.

<!-- /box -->

<!-- pdf-page: 212 | printed: 179 -->

## Import lớp

Khi bạn thêm nhiều chức năng hơn vào các lớp, file của bạn có thể trở nên dài, ngay cả khi bạn dùng kế thừa đúng cách. Để phù hợp với triết lý chung của Python, bạn sẽ muốn giữ cho các file gọn gàng nhất có thể. Để giúp bạn, Python cho phép lưu các lớp trong module rồi import những lớp cần thiết vào chương trình chính.

### Import một lớp duy nhất

Hãy tạo một module chỉ chứa lớp `Car`. Điều này làm nảy sinh một vấn đề nhỏ về đặt tên: chúng ta đã có một file tên là *car.py* trong chương này, nhưng module này nên được đặt tên là *car.py* vì nó chứa mã biểu diễn một chiếc ô tô. Chúng ta sẽ giải quyết vấn đề đặt tên này bằng cách lưu lớp `Car` vào một module có tên *car.py*, thay thế file *car.py* mà ta đã dùng trước đó. Từ giờ trở đi, mọi chương trình dùng module này sẽ cần một tên file cụ thể hơn, chẳng hạn *my_car.py*. Đây là *car.py* chỉ với mã của lớp `Car`:

**car.py**

```python
❶ """A class that can be used to represent a car."""

  class Car():
      """A simple attempt to represent a car."""

      def __init__(self, make, model, year):
          """Initialize attributes to describe a car."""
          self.make = make
          self.model = model
          self.year = year
          self.odometer_reading = 0

      def get_descriptive_name(self):
          """Return a neatly formatted descriptive name."""
          long_name = str(self.year) + ' ' + self.make + ' ' + self.model
          return long_name.title()

      def read_odometer(self):
          """Print a statement showing the car's mileage."""
          print("This car has " + str(self.odometer_reading) + " miles on it.")

      def update_odometer(self, mileage):
          """
          Set the odometer reading to the given value.
          Reject the change if it attempts to roll the odometer back.
          """
          if mileage >= self.odometer_reading:
              self.odometer_reading = mileage
          else:
              print("You can't roll back an odometer!")

      def increment_odometer(self, miles):
          """Add the given amount to the odometer reading."""
          self.odometer_reading += miles
```

<!-- pdf-page: 213 | printed: 180 -->

Tại ❶, chúng ta đưa vào một docstring cấp module mô tả ngắn gọn nội dung của module này. Bạn nên viết một docstring cho mỗi module bạn tạo ra.

Giờ chúng ta tạo một file riêng có tên *my_car.py*. File này sẽ import lớp `Car` rồi tạo một thực thể từ lớp đó:

**my_car.py**

```python
❶ from car import Car

  my_new_car = Car('audi', 'a4', 2016)
  print(my_new_car.get_descriptive_name())

  my_new_car.odometer_reading = 23
  my_new_car.read_odometer()
```

Câu lệnh `import` tại ❶ yêu cầu Python mở module `car` và import lớp `Car`. Giờ chúng ta có thể dùng lớp `Car` như thể nó được định nghĩa trong file này. Đầu ra giống như những gì ta đã thấy trước đó:

```text
2016 Audi A4
This car has 23 miles on it.
```

Import lớp là một cách lập trình hiệu quả. Hãy hình dung file chương trình này sẽ dài đến mức nào nếu toàn bộ lớp `Car` được đưa vào. Khi bạn chuyển lớp vào một module và import module đó, bạn vẫn có đầy đủ chức năng như cũ, nhưng giữ được file chương trình chính gọn gàng và dễ đọc. Bạn cũng lưu phần lớn logic trong các file riêng; một khi các lớp đã hoạt động như bạn muốn, bạn có thể để yên những file đó và tập trung vào logic ở mức cao hơn của chương trình chính.

### Lưu nhiều lớp trong một module

Bạn có thể lưu bao nhiêu lớp tùy nhu cầu trong một module, dù các lớp trong một module nên có liên quan đến nhau theo cách nào đó. Cả hai lớp `Battery` và `ElectricCar` đều giúp biểu diễn ô tô, nên hãy thêm chúng vào module *car.py*:

**car.py**

```python
"""A set of classes used to represent gas and electric cars."""

class Car():
    --snip--

class Battery():
    """A simple attempt to model a battery for an electric car."""

    def __init__(self, battery_size=60):
        """Initialize the batteery's attributes."""
        self.battery_size = battery_size

    def describe_battery(self):
        """Print a statement describing the battery size."""
        print("This car has a " + str(self.battery_size) + "-kWh battery.")

    def get_range(self):
        """Print a statement about the range this battery provides."""
        if self.battery_size == 70:
            range = 240
        elif self.battery_size == 85:
            range = 270

        message = "This car can go approximately " + str(range)
        message += " miles on a full charge."
        print(message)

class ElectricCar(Car):
    """Models aspects of a car, specific to electric vehicles."""

    def __init__(self, make, model, year):
        """
        Initialize attributes of the parent class.
        Then initialize attributes specific to an electric car.
        """
        super().__init__(make, model, year)
        self.battery = Battery()
```

<!-- pdf-page: 214 | printed: 181 -->

Giờ chúng ta có thể tạo một file mới có tên *my_electric_car.py*, import lớp `ElectricCar` và tạo một chiếc ô tô điện:

**my_electric_car.py**

```python
from car import ElectricCar
my_tesla = ElectricCar('tesla', 'model s', 2016)

print(my_tesla.get_descriptive_name())
my_tesla.battery.describe_battery()
my_tesla.battery.get_range()
```

Đoạn mã này có cùng đầu ra như những gì ta đã thấy trước đó, dù phần lớn logic đã được ẩn trong một module:

```text
2016 Tesla Model S
This car has a 70-kWh battery.
This car can go approximately 240 miles on a full charge.
```

### Import nhiều lớp từ một module

Bạn có thể import bao nhiêu lớp tùy nhu cầu vào một file chương trình. Nếu muốn tạo một chiếc ô tô thông thường và một chiếc ô tô điện trong cùng một file, ta cần import cả hai lớp, `Car` và `ElectricCar`:

**my_cars.py**

```python
❶ from car import Car, ElectricCar

❷ my_beetle = Car('volkswagen', 'beetle', 2016)
  print(my_beetle.get_descriptive_name())

❸ my_tesla = ElectricCar('tesla', 'roadster', 2016)
  print(my_tesla.get_descriptive_name())
```

<!-- pdf-page: 215 | printed: 182 -->

Bạn import nhiều lớp từ một module bằng cách phân tách các lớp bằng dấu phẩy ❶. Khi đã import các lớp cần thiết, bạn có thể tự do tạo bao nhiêu thực thể của mỗi lớp tùy nhu cầu.

Trong ví dụ này, chúng ta tạo một chiếc Volkswagen Beetle thông thường tại ❷ và một chiếc Tesla Roadster chạy điện tại ❸:

```text
2016 Volkswagen Beetle
2016 Tesla Roadster
```

### Import toàn bộ module

Bạn cũng có thể import toàn bộ một module rồi truy cập các lớp cần thiết bằng ký hiệu dấu chấm. Cách này đơn giản và cho ra mã dễ đọc. Vì mọi lời gọi tạo thực thể của một lớp đều có kèm tên module, bạn sẽ không gặp xung đột tên với bất kỳ tên nào được dùng trong file hiện tại.

Đây là cách import toàn bộ module `car` rồi tạo một chiếc ô tô thông thường và một chiếc ô tô điện:

**my_cars.py**

```python
❶ import car

❷ my_beetle = car.Car('volkswagen', 'beetle', 2016)
  print(my_beetle.get_descriptive_name())

❸ my_tesla = car.ElectricCar('tesla', 'roadster', 2016)
  print(my_tesla.get_descriptive_name())
```

Tại ❶, chúng ta import toàn bộ module `car`. Sau đó, ta truy cập các lớp cần thiết thông qua cú pháp `module_name`.`class_name`. Tại ❷, ta lại tạo một chiếc Volkswagen Beetle, và tại ❸, ta tạo một chiếc Tesla Roadster.

### Import tất cả các lớp từ một module

Bạn có thể import mọi lớp từ một module bằng cú pháp sau:

```python
from module_name import *
```

Cách này không được khuyến khích vì hai lý do. Thứ nhất, việc có thể đọc các câu lệnh `import` ở đầu file và nắm rõ chương trình dùng những lớp nào là rất hữu ích. Với cách này, không rõ bạn đang dùng những lớp nào từ module. Cách này cũng có thể gây nhầm lẫn với các tên trong file. Nếu bạn vô tình import một lớp có cùng tên với một thứ khác trong file chương trình, bạn có thể tạo ra những lỗi khó chẩn đoán. Tôi trình bày cách này ở đây vì dù không được khuyến khích, bạn vẫn có khả năng gặp nó trong mã của người khác.

Nếu cần import nhiều lớp từ một module, tốt hơn hết là bạn import toàn bộ module và dùng cú pháp `module_name.class_name`. Bạn sẽ không thấy tất cả các lớp được dùng ở đầu file, nhưng sẽ thấy rõ module được dùng ở đâu trong chương trình. Bạn cũng sẽ tránh được những xung đột tên tiềm ẩn có thể phát sinh khi import mọi lớp trong một module.

<!-- pdf-page: 216 | printed: 183 -->

### Import một module vào một module khác

Đôi khi bạn sẽ muốn phân bố các lớp của mình vào nhiều module để không file nào trở nên quá lớn và tránh lưu những lớp không liên quan trong cùng một module. Khi lưu các lớp trong nhiều module, bạn có thể thấy một lớp trong module này phụ thuộc vào một lớp trong module khác. Khi điều này xảy ra, bạn có thể import lớp cần thiết vào module thứ nhất.

Ví dụ, hãy lưu lớp `Car` trong một module và các lớp `ElectricCar` và `Battery` trong một module riêng. Chúng ta sẽ tạo một module mới có tên *electric_car.py* — thay thế file *electric_car.py* đã tạo trước đó — và chỉ sao chép các lớp `Battery` và `ElectricCar` vào file này:

**electric_car.py**

```python
  """A set of classes that can be used to represent electric cars."""

❶ from car import Car

  class Battery():
      --snip--

  class ElectricCar(Car):
      --snip--
```

Lớp `ElectricCar` cần truy cập lớp cha của nó là `Car`, nên chúng ta import `Car` trực tiếp vào module tại ❶. Nếu quên dòng này, Python sẽ báo lỗi khi ta thử tạo một thực thể `ElectricCar`. Ta cũng cần cập nhật module `Car` để nó chỉ chứa lớp `Car`:

**car.py**

```python
"""A class that can be used to represent a car."""

class Car():
    --snip--
```

Giờ chúng ta có thể import riêng từ mỗi module và tạo bất kỳ loại ô tô nào cần thiết:

**my_cars.py**

```python
❶ from car import Car
  from electric_car import ElectricCar

  my_beetle = Car('volkswagen', 'beetle', 2016)
  print(my_beetle.get_descriptive_name())

  my_tesla = ElectricCar('tesla', 'roadster', 2016)
  print(my_tesla.get_descriptive_name())
```

<!-- pdf-page: 217 | printed: 184 -->

Tại ❶, chúng ta import `Car` từ module của nó, và `ElectricCar` từ module của nó. Sau đó, ta tạo một chiếc ô tô thông thường và một chiếc ô tô điện. Cả hai loại ô tô đều được tạo đúng:

```text
2016 Volkswagen Beetle
2016 Tesla Roadster
```

### Tìm ra quy trình làm việc của riêng bạn

Như bạn thấy, Python cho bạn nhiều lựa chọn về cách tổ chức cấu trúc mã trong một dự án lớn. Biết tất cả những khả năng này là điều quan trọng, để bạn có thể xác định cách tốt nhất để tổ chức các dự án của mình, cũng như hiểu được dự án của người khác.

Khi mới bắt đầu, hãy giữ cho cấu trúc mã đơn giản. Hãy thử làm mọi thứ trong một file và chuyển các lớp sang các module riêng khi mọi thứ đã hoạt động. Nếu bạn thích cách các module và file tương tác với nhau, hãy thử lưu các lớp trong module ngay khi bắt đầu một dự án. Hãy tìm một cách tiếp cận cho phép bạn viết mã chạy được, rồi phát triển tiếp từ đó.

<!-- box -->

**Tự mình thực hành**

**9-10. Import nhà hàng:** Dùng lớp `Restaurant` mới nhất của bạn, lưu nó vào một module. Tạo một file riêng import `Restaurant`. Tạo một thực thể `Restaurant` và gọi một trong các phương thức của `Restaurant` để cho thấy câu lệnh `import` hoạt động đúng.

**9-11. Import Admin:** Bắt đầu với bài làm của bạn từ Bài tập 9-8 (trang 178). Lưu các lớp `User`, `Privileges` và `Admin` vào một module. Tạo một file riêng, tạo một thực thể `Admin` và gọi `show_privileges()` để cho thấy mọi thứ đang hoạt động đúng.

**9-12. Nhiều module:** Lưu lớp `User` vào một module, và lưu các lớp `Privileges` và `Admin` vào một module riêng. Trong một file riêng, tạo một thực thể `Admin` và gọi `show_privileges()` để cho thấy mọi thứ vẫn hoạt động đúng.

<!-- /box -->

## Thư viện chuẩn của Python

*Thư viện chuẩn của Python* (Python standard library) là một tập hợp các module đi kèm với mọi bản cài đặt Python. Giờ đây khi đã hiểu cơ bản về cách lớp hoạt động, bạn có thể bắt đầu dùng những module như thế này do các lập trình viên khác viết. Bạn có thể dùng bất kỳ hàm hoặc lớp nào trong thư viện chuẩn bằng cách thêm một câu lệnh `import` đơn giản ở đầu file. Hãy xem một lớp, `OrderedDict`, từ module `collections`.

<!-- pdf-page: 218 | printed: 185 -->

Dictionary cho phép bạn kết nối các mẩu thông tin, nhưng chúng không theo dõi thứ tự bạn thêm các cặp khóa–giá trị. Nếu bạn đang tạo một dictionary và muốn theo dõi thứ tự các cặp khóa–giá trị được thêm vào, bạn có thể dùng lớp `OrderedDict` từ module `collections`. Các thực thể của lớp `OrderedDict` hoạt động gần như giống hệt dictionary, chỉ khác là chúng theo dõi thứ tự các cặp khóa–giá trị được thêm vào.

Hãy xem lại ví dụ *favorite_languages.py* từ Chương 6. Lần này, chúng ta sẽ theo dõi thứ tự mọi người trả lời khảo sát:

**favorite_languages.py**

```python
❶ from collections import OrderedDict
❷ favorite_languages = OrderedDict()

❸ favorite_languages['jen'] = 'python'
  favorite_languages['sarah'] = 'c'
  favorite_languages['edward'] = 'ruby'
  favorite_languages['phil'] = 'python'

❹ for name, language in favorite_languages.items():
      print(name.title() + "'s favorite language is " +
          language.title() + ".")
```

Chúng ta bắt đầu bằng việc import lớp `OrderedDict` từ module `collections` tại ❶. Tại ❷, ta tạo một thực thể của lớp `OrderedDict` và lưu thực thể này vào `favorite_languages`. Hãy để ý rằng không có dấu ngoặc nhọn nào; lời gọi `OrderedDict()` tạo một dictionary có thứ tự rỗng cho chúng ta và lưu nó vào `favorite_languages`. Sau đó, ta lần lượt thêm từng tên và ngôn ngữ vào `favorite_languages` ❸. Giờ khi lặp qua `favorite_languages` tại ❹, ta biết mình sẽ luôn nhận lại các câu trả lời theo đúng thứ tự chúng được thêm vào:

```text
Jen's favorite language is Python.
Sarah's favorite language is C.
Edward's favorite language is Ruby.
Phil's favorite language is Python.
```

Đây là một lớp rất đáng biết, vì nó kết hợp lợi ích chính của list (giữ nguyên thứ tự ban đầu) với tính năng chính của dictionary (kết nối các mẩu thông tin). Khi bắt đầu mô hình hóa những tình huống thực tế mà bạn quan tâm, có lẽ bạn sẽ gặp một tình huống mà dictionary có thứ tự chính là thứ bạn cần. Khi tìm hiểu thêm về thư viện chuẩn, bạn sẽ quen thuộc với nhiều module như thế này giúp bạn xử lý những tình huống thường gặp.

> **Lưu ý** Bạn cũng có thể tải module từ các nguồn bên ngoài. Bạn sẽ thấy một số ví dụ như vậy trong Phần II, nơi chúng ta sẽ cần các module bên ngoài để hoàn thành từng dự án.

<!-- pdf-page: 219 | printed: 186 -->

<!-- box -->

**Tự mình thực hành**

**9-13. Viết lại bằng OrderedDict:** Bắt đầu với Bài tập 6-4 (trang 108), nơi bạn đã dùng một dictionary thông thường để biểu diễn một bảng thuật ngữ. Viết lại chương trình bằng lớp `OrderedDict` và đảm bảo thứ tự của đầu ra khớp với thứ tự các cặp khóa–giá trị được thêm vào dictionary.

**9-14. Xúc xắc:** Module `random` chứa các hàm tạo số ngẫu nhiên theo nhiều cách khác nhau. Hàm `randint()` trả về một số nguyên trong khoảng mà bạn cung cấp. Đoạn mã sau trả về một số từ 1 đến 6:

```python
from random import randint
x = randint(1, 6)
```

Tạo một lớp `Die` (con xúc xắc) với một thuộc tính có tên `sides`, có giá trị mặc định là 6. Viết một phương thức có tên `roll_die()` in ra một số ngẫu nhiên từ 1 đến số mặt của con xúc xắc. Tạo một con xúc xắc 6 mặt và gieo nó 10 lần.

Tạo một con xúc xắc 10 mặt và một con xúc xắc 20 mặt. Gieo mỗi con xúc xắc 10 lần.

**9-15. Python Module of the Week:** Một tài nguyên tuyệt vời để khám phá thư viện chuẩn của Python là trang web có tên *Python Module of the Week*. Hãy truy cập *http://pymotw.com/* và xem mục lục. Tìm một module bạn thấy thú vị và đọc về nó, hoặc khám phá tài liệu của các module `collections` và `random`.

<!-- /box -->

## Định dạng phong cách lớp

Có một vài vấn đề về phong cách liên quan đến lớp đáng được làm rõ, đặc biệt khi chương trình của bạn ngày càng phức tạp.

Tên lớp nên được viết theo kiểu *CamelCaps*. Để làm điều này, hãy viết hoa chữ cái đầu của mỗi từ trong tên và không dùng dấu gạch dưới. Tên thực thể và tên module nên được viết bằng chữ thường, với dấu gạch dưới giữa các từ.

Mỗi lớp nên có một docstring ngay sau định nghĩa lớp. Docstring nên là một mô tả ngắn gọn về những gì lớp làm, và bạn nên tuân theo các quy ước định dạng giống như khi viết docstring cho hàm. Mỗi module cũng nên có một docstring mô tả các lớp trong module có thể được dùng vào việc gì.

Bạn có thể dùng dòng trống để tổ chức mã, nhưng đừng lạm dụng. Bên trong một lớp, bạn có thể dùng một dòng trống giữa các phương thức, và bên trong một module, bạn có thể dùng hai dòng trống để phân tách các lớp.

Nếu cần import một module từ thư viện chuẩn và một module do bạn viết, hãy đặt câu lệnh import cho module của thư viện chuẩn trước. Sau đó thêm một dòng trống và câu lệnh import cho module do bạn viết. Trong những chương trình có nhiều câu lệnh import, quy ước này giúp dễ thấy các module khác nhau được dùng trong chương trình đến từ đâu.

<!-- pdf-page: 220 | printed: 187 -->

## Tổng kết

Trong chương này, bạn đã học cách viết lớp của riêng mình. Bạn đã học cách lưu thông tin trong một lớp bằng thuộc tính và cách viết các phương thức mang lại cho lớp những hành vi cần thiết. Bạn đã học cách viết phương thức `__init__()` để tạo thực thể từ lớp với đúng những thuộc tính bạn muốn. Bạn đã thấy cách sửa đổi các thuộc tính của một thực thể một cách trực tiếp và thông qua phương thức. Bạn đã biết rằng kế thừa có thể đơn giản hóa việc tạo những lớp có liên quan đến nhau, và đã học cách dùng thực thể của một lớp làm thuộc tính trong một lớp khác để giữ cho mỗi lớp đơn giản.

Bạn đã thấy việc lưu các lớp trong module và import những lớp cần thiết vào các file sẽ dùng chúng có thể giúp dự án của bạn ngăn nắp như thế nào. Bạn đã bắt đầu tìm hiểu về thư viện chuẩn của Python, và đã thấy một ví dụ dựa trên lớp `OrderedDict` từ module `collections`. Cuối cùng, bạn đã học cách định dạng phong cách cho lớp theo các quy ước của Python.

Trong Chương 10, bạn sẽ học cách làm việc với file để có thể lưu lại công việc bạn đã làm trong một chương trình và công việc bạn đã cho phép người dùng thực hiện. Bạn cũng sẽ tìm hiểu về *ngoại lệ* (exception), một lớp Python đặc biệt được thiết kế để giúp bạn phản hồi các lỗi khi chúng xảy ra.

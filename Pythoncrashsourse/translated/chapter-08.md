<!-- source: pythoncrashcourse.pdf | unit: chapter-08 | pdf pages 166-193 | printed 133-160 -->

# Chương 8: Hàm

<!-- pdf-page: 166 | printed: 133 -->

Trong chương này, bạn sẽ học cách viết *hàm* (function) — những khối mã có tên, được thiết kế để làm một công việc cụ thể. Khi muốn thực hiện một tác vụ cụ thể mà bạn đã định nghĩa trong một hàm, bạn *gọi* (call) tên của hàm phụ trách tác vụ đó. Nếu bạn cần

thực hiện tác vụ đó nhiều lần trong chương trình, bạn không cần gõ đi gõ lại toàn bộ mã cho cùng một tác vụ; bạn chỉ cần gọi hàm chuyên xử lý tác vụ đó, và lời gọi hàm sẽ yêu cầu Python chạy đoạn mã bên trong hàm. Bạn sẽ thấy dùng hàm giúp chương trình dễ viết, dễ đọc, dễ kiểm thử và dễ sửa hơn.

Trong chương này, bạn cũng sẽ học các cách truyền thông tin cho hàm. Bạn sẽ học cách viết những hàm có nhiệm vụ chính là hiển thị thông tin, và những hàm khác được thiết kế để xử lý dữ liệu và trả về một giá trị hoặc một tập giá trị. Cuối cùng, bạn sẽ học cách lưu các hàm trong những file riêng gọi là *module* để giúp sắp xếp các file chương trình chính.

<!-- pdf-page: 167 | printed: 134 -->

## Định nghĩa hàm

Đây là một hàm đơn giản có tên `greet_user()` in ra một lời chào:

**greeter.py**

```python
❶ def greet_user():
❷     """Display a simple greeting."""
❸     print("Hello!")

❹ greet_user()
```

Ví dụ này cho thấy cấu trúc đơn giản nhất của một hàm. Dòng tại ❶ dùng từ khóa `def` để báo cho Python biết bạn đang định nghĩa một hàm. Đây là *định nghĩa hàm* (function definition), cho Python biết tên của hàm và, nếu có, loại thông tin mà hàm cần để thực hiện công việc của nó. Cặp dấu ngoặc đơn chứa thông tin đó. Trong trường hợp này, tên hàm là `greet_user()`, và nó không cần thông tin nào để làm việc, nên cặp ngoặc đơn để trống. (Dù vậy, cặp ngoặc đơn vẫn là bắt buộc.) Cuối cùng, định nghĩa hàm kết thúc bằng một dấu hai chấm.

Mọi dòng thụt lề đứng sau `def greet_user():` tạo thành *thân* (body) của hàm. Đoạn văn bản tại ❷ là một chú thích được gọi là *docstring*, mô tả hàm làm gì. Docstring được bao trong ba dấu nháy kép, thứ mà Python tìm kiếm khi tạo tài liệu cho các hàm trong chương trình của bạn.

Dòng `print("Hello!")` ❸ là dòng mã thực sự duy nhất trong thân hàm này, nên `greet_user()` chỉ có một việc: `print("Hello!")`.

Khi muốn dùng hàm này, bạn gọi nó. Một *lời gọi hàm* (function call) yêu cầu Python thực thi đoạn mã trong hàm. Để *gọi* một hàm, bạn viết tên hàm, theo sau là mọi thông tin cần thiết đặt trong cặp ngoặc đơn, như tại ❹. Vì ở đây không cần thông tin nào, việc gọi hàm chỉ đơn giản là nhập `greet_user()`. Đúng như mong đợi, nó in ra `Hello!`:

```text
Hello!
```

### Truyền thông tin cho hàm

Chỉ cần sửa đổi một chút, hàm `greet_user()` không chỉ có thể nói `Hello!` với người dùng mà còn chào họ bằng tên. Để hàm làm được điều này, bạn nhập `username` vào trong cặp ngoặc đơn của định nghĩa hàm tại `def greet_user()`. Bằng cách thêm `username` vào đây, bạn cho phép hàm nhận bất kỳ giá trị `username` nào bạn chỉ định. Giờ hàm mong đợi bạn cung cấp một giá trị cho `username` mỗi khi gọi nó. Khi gọi `greet_user()`, bạn có thể truyền cho nó một cái tên, chẳng hạn `'jesse'`, bên trong cặp ngoặc đơn:

```python
def greet_user(username):
    """Display a simple greeting."""
    print("Hello, " + username.title() + "!")

greet_user('jesse')
```

<!-- pdf-page: 168 | printed: 135 -->

Nhập `greet_user('jesse')` sẽ gọi `greet_user()` và cung cấp cho hàm thông tin cần thiết để thực thi câu lệnh `print`. Hàm nhận cái tên bạn đã truyền vào và hiển thị lời chào cho tên đó:

```text
Hello, Jesse!
```

Tương tự, nhập `greet_user('sarah')` sẽ gọi `greet_user()`, truyền cho nó `'sarah'`, và in ra `Hello, Sarah!` Bạn có thể gọi `greet_user()` bao nhiêu lần tùy thích và truyền cho nó bất kỳ cái tên nào bạn muốn để mỗi lần đều cho ra một đầu ra có thể đoán trước.

### Đối số và tham số

Trong hàm `greet_user()` ở trên, chúng ta đã định nghĩa `greet_user()` để yêu cầu một giá trị cho biến `username`. Khi ta gọi hàm và cung cấp cho nó thông tin (tên một người), nó đã in ra đúng lời chào.

Biến `username` trong định nghĩa của `greet_user()` là một ví dụ về *tham số* (parameter) — một mẩu thông tin mà hàm cần để thực hiện công việc của nó. Giá trị `'jesse'` trong `greet_user('jesse')` là một ví dụ về *đối số* (argument). Đối số là một mẩu thông tin được truyền từ lời gọi hàm tới hàm. Khi gọi hàm, chúng ta đặt giá trị muốn hàm làm việc cùng vào trong cặp ngoặc đơn. Trong trường hợp này, đối số `'jesse'` được truyền cho hàm `greet_user()`, và giá trị đó được lưu vào tham số `username`.

> **Lưu ý** Đôi khi người ta dùng lẫn lộn hai từ đối số và tham số. Đừng ngạc nhiên nếu bạn thấy các biến trong định nghĩa hàm được gọi là đối số, hoặc các biến trong lời gọi hàm được gọi là tham số.

<!-- box -->

**Tự mình thực hành**

**8-1. Thông điệp:** Viết một hàm có tên `display_message()` in ra một câu cho mọi người biết bạn đang học gì trong chương này. Gọi hàm và đảm bảo thông điệp được hiển thị đúng.

**8-2. Cuốn sách yêu thích:** Viết một hàm có tên `favorite_book()` nhận một tham số, `title`. Hàm nên in ra một thông điệp, chẳng hạn như `One of my favorite books is Alice in Wonderland`. Gọi hàm, nhớ đưa tên một cuốn sách làm đối số trong lời gọi hàm.

<!-- /box -->

## Truyền đối số

Vì một định nghĩa hàm có thể có nhiều tham số, nên một lời gọi hàm có thể cần nhiều đối số. Bạn có thể truyền đối số cho hàm theo nhiều cách. Bạn có thể dùng *đối số vị trí* (positional argument), cần được viết đúng thứ tự như các tham số; *đối số từ khóa* (keyword argument), trong đó mỗi đối số gồm một tên biến và một giá trị; và list hoặc dictionary chứa các giá trị. Hãy lần lượt xem xét từng cách.

<!-- pdf-page: 169 | printed: 136 -->

### Đối số vị trí

Khi bạn gọi một hàm, Python phải ghép mỗi đối số trong lời gọi hàm với một tham số trong định nghĩa hàm. Cách đơn giản nhất để làm điều này là dựa vào thứ tự của các đối số được cung cấp. Những giá trị được ghép theo cách này được gọi là *đối số vị trí*.

Để xem cách này hoạt động ra sao, hãy xét một hàm hiển thị thông tin về thú cưng. Hàm cho chúng ta biết mỗi con thú cưng là loài vật gì và tên của nó, như sau:

**pets.py**

```python
❶ def describe_pet(animal_type, pet_name):
      """Display information about a pet."""
      print("\nI have a " + animal_type + ".")
      print("My " + animal_type + "'s name is " + pet_name.title() + ".")

❷ describe_pet('hamster', 'harry')
```

Định nghĩa cho thấy hàm này cần một loài vật và tên của con vật ❶. Khi gọi `describe_pet()`, chúng ta cần cung cấp loài vật và tên, theo đúng thứ tự đó. Ví dụ, trong lời gọi hàm, đối số `'hamster'` được lưu vào tham số `animal_type` và đối số `'harry'` được lưu vào tham số `pet_name` ❷. Trong thân hàm, hai tham số này được dùng để hiển thị thông tin về con thú cưng đang được mô tả.

Đầu ra mô tả một chú chuột hamster tên là Harry:

```text
I have a hamster.
My hamster's name is Harry.
```

#### Gọi hàm nhiều lần

Bạn có thể gọi một hàm bao nhiêu lần tùy nhu cầu. Để mô tả một con thú cưng thứ hai khác, chỉ cần thêm một lời gọi `describe_pet()` nữa:

```python
def describe_pet(animal_type, pet_name):
    """Display information about a pet."""
    print("\nI have a " + animal_type + ".")
    print("My " + animal_type + "'s name is " + pet_name.title() + ".")

describe_pet('hamster', 'harry')
describe_pet('dog', 'willie')
```

Trong lời gọi hàm thứ hai này, chúng ta truyền cho `describe_pet()` các đối số `'dog'` và `'willie'`. Giống như với nhóm đối số trước, Python ghép `'dog'` với tham số `animal_type` và `'willie'` với tham số `pet_name`. Như trước, hàm thực hiện công việc của mình, nhưng lần này nó in ra các giá trị cho một chú chó tên là Willie. Giờ chúng ta có một chú hamster tên Harry và một chú chó tên Willie:

<!-- pdf-page: 170 | printed: 137 -->

```text
I have a hamster.
My hamster's name is Harry.

I have a dog.
My dog's name is Willie.
```

Gọi một hàm nhiều lần là một cách làm việc rất hiệu quả. Đoạn mã mô tả một con thú cưng chỉ được viết một lần trong hàm. Sau đó, bất cứ khi nào muốn mô tả một con thú cưng mới, bạn gọi hàm với thông tin của con thú cưng mới đó. Ngay cả khi đoạn mã mô tả thú cưng có mở rộng thành mười dòng, bạn vẫn có thể mô tả một con thú cưng mới chỉ bằng một dòng, bằng cách gọi lại hàm.

Bạn có thể dùng bao nhiêu đối số vị trí tùy theo nhu cầu trong các hàm của mình. Python duyệt qua các đối số bạn cung cấp khi gọi hàm và ghép mỗi đối số với tham số tương ứng trong định nghĩa hàm.

#### Thứ tự quan trọng với đối số vị trí

Bạn có thể nhận được kết quả bất ngờ nếu đảo lộn thứ tự các đối số trong lời gọi hàm khi dùng đối số vị trí:

```python
def describe_pet(animal_type, pet_name):
    """Display information about a pet."""
    print("\nI have a " + animal_type + ".")
    print("My " + animal_type + "'s name is " + pet_name.title() + ".")

describe_pet('harry', 'hamster')
```

Trong lời gọi hàm này, chúng ta liệt kê tên trước và loài vật sau. Vì lần này đối số `'harry'` được liệt kê trước, giá trị đó được lưu vào tham số `animal_type`. Tương tự, `'hamster'` được lưu vào `pet_name`. Giờ chúng ta có một con “harry” tên là “Hamster”:

```text
I have a harry.
My harry's name is Hamster.
```

Nếu bạn nhận được những kết quả buồn cười như thế này, hãy kiểm tra để đảm bảo thứ tự các đối số trong lời gọi hàm khớp với thứ tự các tham số trong định nghĩa hàm.

### Đối số từ khóa

*Đối số từ khóa* (keyword argument) là một cặp tên–giá trị mà bạn truyền cho hàm. Bạn gắn trực tiếp tên với giá trị ngay trong đối số, nên khi truyền đối số cho hàm sẽ không có sự nhầm lẫn nào (bạn sẽ không bị một con harry tên là Hamster). Đối số từ khóa giúp bạn không phải lo sắp xếp đúng thứ tự các đối số trong lời gọi hàm, đồng thời làm rõ vai trò của từng giá trị trong lời gọi hàm.

<!-- pdf-page: 171 | printed: 138 -->

Hãy viết lại *pets.py*, dùng đối số từ khóa để gọi `describe_pet()`:

```python
def describe_pet(animal_type, pet_name):
    """Display information about a pet."""
    print("\nI have a " + animal_type + ".")
    print("My " + animal_type + "'s name is " + pet_name.title() + ".")

describe_pet(animal_type='hamster', pet_name='harry')
```

Hàm `describe_pet()` không thay đổi. Nhưng khi gọi hàm, chúng ta nói rõ cho Python biết mỗi đối số nên được ghép với tham số nào. Khi đọc lời gọi hàm, Python biết phải lưu đối số `'hamster'` vào tham số `animal_type` và đối số `'harry'` vào `pet_name`. Đầu ra cho thấy chính xác rằng chúng ta có một chú hamster tên Harry.

Thứ tự của các đối số từ khóa không quan trọng vì Python biết mỗi giá trị nên đi đâu. Hai lời gọi hàm sau là tương đương:

```text
describe_pet(animal_type='hamster', pet_name='harry')
describe_pet(pet_name='harry', animal_type='hamster')
```

> **Lưu ý** Khi dùng đối số từ khóa, hãy đảm bảo dùng đúng chính xác tên của các tham số trong định nghĩa hàm.

### Giá trị mặc định

Khi viết một hàm, bạn có thể định nghĩa một *giá trị mặc định* (default value) cho mỗi tham số. Nếu một đối số cho tham số được cung cấp trong lời gọi hàm, Python dùng giá trị của đối số đó. Nếu không, nó dùng giá trị mặc định của tham số. Vì vậy, khi định nghĩa giá trị mặc định cho một tham số, bạn có thể bỏ qua đối số tương ứng mà thường phải viết trong lời gọi hàm. Dùng giá trị mặc định có thể đơn giản hóa lời gọi hàm và làm rõ cách hàm thường được sử dụng.

Ví dụ, nếu nhận thấy hầu hết các lời gọi `describe_pet()` đều dùng để mô tả chó, bạn có thể đặt giá trị mặc định của `animal_type` là `'dog'`. Giờ bất kỳ ai gọi `describe_pet()` cho một chú chó đều có thể bỏ qua thông tin đó:

```python
def describe_pet(pet_name, animal_type='dog'):
    """Display information about a pet."""
    print("\nI have a " + animal_type + ".")
    print("My " + animal_type + "'s name is " + pet_name.title() + ".")

describe_pet(pet_name='willie')
```

<!-- pdf-page: 172 | printed: 139 -->

Chúng ta đã thay đổi định nghĩa của `describe_pet()` để thêm giá trị mặc định `'dog'` cho `animal_type`. Giờ khi hàm được gọi mà không chỉ định `animal_type`, Python biết phải dùng giá trị `'dog'` cho tham số này:

```text
I have a dog.
My dog's name is Willie.
```

Lưu ý rằng thứ tự các tham số trong định nghĩa hàm đã phải thay đổi. Vì giá trị mặc định khiến việc chỉ định loài vật làm đối số trở nên không cần thiết, đối số duy nhất còn lại trong lời gọi hàm là tên của con thú cưng. Python vẫn hiểu đây là một đối số vị trí, nên nếu hàm được gọi chỉ với tên thú cưng, đối số đó sẽ được ghép với tham số đầu tiên được liệt kê trong định nghĩa hàm. Đó là lý do tham số đầu tiên cần phải là `pet_name`.

Cách đơn giản nhất để dùng hàm này bây giờ là chỉ cung cấp tên của chú chó trong lời gọi hàm:

```text
describe_pet('willie')
```

Lời gọi hàm này sẽ có cùng đầu ra như ví dụ trước. Đối số duy nhất được cung cấp là `'willie'`, nên nó được ghép với tham số đầu tiên trong định nghĩa, `pet_name`. Vì không có đối số nào được cung cấp cho `animal_type`, Python dùng giá trị mặc định `'dog'`.

Để mô tả một con vật khác không phải chó, bạn có thể dùng một lời gọi hàm như sau:

```text
describe_pet(pet_name='harry', animal_type='hamster')
```

Vì một đối số tường minh cho `animal_type` đã được cung cấp, Python sẽ bỏ qua giá trị mặc định của tham số.

> **Lưu ý** Khi dùng giá trị mặc định, mọi tham số có giá trị mặc định cần được liệt kê sau tất cả các tham số không có giá trị mặc định. Điều này cho phép Python tiếp tục hiểu đúng các đối số vị trí.

### Các lời gọi hàm tương đương

Vì đối số vị trí, đối số từ khóa và giá trị mặc định đều có thể được dùng cùng nhau, bạn thường sẽ có nhiều cách tương đương để gọi một hàm. Hãy xét định nghĩa sau của `describe_pets()` với một giá trị mặc định:

```python
def describe_pet(pet_name, animal_type='dog'):
```

Với định nghĩa này, luôn cần cung cấp một đối số cho `pet_name`, và giá trị này có thể được cung cấp theo dạng vị trí hoặc dạng từ khóa. Nếu con vật được mô tả không phải là chó, lời gọi phải có một đối số cho `animal_type`, và đối số này cũng có thể được chỉ định theo dạng vị trí hoặc dạng từ khóa.

<!-- pdf-page: 173 | printed: 140 -->

Tất cả các lời gọi sau đều hoạt động với hàm này:

```text
# A dog named Willie.
describe_pet('willie')
describe_pet(pet_name='willie')

# A hamster named Harry.
describe_pet('harry', 'hamster')
describe_pet(pet_name='harry', animal_type='hamster')
describe_pet(animal_type='hamster', pet_name='harry')
```

Mỗi lời gọi hàm này đều sẽ có cùng đầu ra như các ví dụ trước.

> **Lưu ý** Bạn dùng kiểu gọi hàm nào thực ra không quan trọng lắm. Miễn là lời gọi hàm cho ra đầu ra bạn muốn, hãy dùng kiểu mà bạn thấy dễ hiểu nhất.

### Tránh lỗi đối số

Khi bắt đầu dùng hàm, đừng ngạc nhiên nếu bạn gặp lỗi về đối số không khớp. Đối số không khớp xảy ra khi bạn cung cấp ít hơn hoặc nhiều hơn số đối số mà hàm cần để làm việc. Ví dụ, đây là điều xảy ra nếu chúng ta thử gọi `describe_pet()` mà không có đối số nào:

```python
def describe_pet(animal_type, pet_name):
    """Display information about a pet."""
    print("\nI have a " + animal_type + ".")
    print("My " + animal_type + "'s name is " + pet_name.title() + ".")

describe_pet()
```

Python nhận ra rằng lời gọi hàm thiếu một số thông tin, và traceback cho chúng ta biết điều đó:

```text
  Traceback (most recent call last):
❶   File "pets.py", line 6, in <module>
❷     describe_pet()
❸ TypeError: describe_pet() missing 2 required positional arguments: 'animal_
  type' and 'pet_name'
```

Tại ❶, traceback cho chúng ta biết vị trí của vấn đề, giúp ta xem lại và thấy rằng lời gọi hàm có chỗ sai. Tại ❷, lời gọi hàm gây lỗi được viết ra để ta xem. Tại ❸, traceback cho biết lời gọi hàm thiếu hai đối số và nêu tên của các đối số bị thiếu. Nếu hàm này nằm trong một file riêng, có lẽ ta vẫn có thể viết lại lời gọi cho đúng mà không cần mở file đó ra đọc mã của hàm.

<!-- pdf-page: 174 | printed: 141 -->

Python thật hữu ích ở chỗ nó đọc mã của hàm giúp chúng ta và cho biết tên của các đối số cần cung cấp. Đây là thêm một lý do để đặt tên mang tính mô tả cho biến và hàm. Nếu làm vậy, các thông báo lỗi của Python sẽ hữu ích hơn đối với bạn và bất kỳ ai khác có thể dùng mã của bạn.

Nếu cung cấp quá nhiều đối số, bạn sẽ nhận được một traceback tương tự, có thể giúp bạn sửa lời gọi hàm cho khớp với định nghĩa hàm.

<!-- box -->

**Tự mình thực hành**

**8-3. Áo phông:** Viết một hàm có tên `make_shirt()` nhận vào một cỡ áo và nội dung của một thông điệp sẽ được in lên áo. Hàm nên in ra một câu tóm tắt cỡ áo và thông điệp được in trên áo.

Gọi hàm một lần bằng đối số vị trí để làm một chiếc áo. Gọi hàm lần thứ hai bằng đối số từ khóa.

**8-4. Áo cỡ lớn:** Sửa hàm `make_shirt()` sao cho mặc định áo là cỡ lớn với thông điệp *I love Python*. Làm một chiếc áo cỡ lớn và một chiếc áo cỡ vừa với thông điệp mặc định, và một chiếc áo cỡ bất kỳ với một thông điệp khác.

**8-5. Thành phố:** Viết một hàm có tên `describe_city()` nhận vào tên một thành phố và quốc gia của nó. Hàm nên in ra một câu đơn giản, chẳng hạn như `Reykjavik is in Iceland`. Đặt giá trị mặc định cho tham số quốc gia. Gọi hàm cho ba thành phố khác nhau, trong đó ít nhất một thành phố không thuộc quốc gia mặc định.

<!-- /box -->

## Giá trị trả về

Không phải lúc nào hàm cũng phải hiển thị đầu ra trực tiếp. Thay vào đó, nó có thể xử lý một số dữ liệu rồi trả về một giá trị hoặc một tập giá trị. Giá trị mà hàm trả về được gọi là *giá trị trả về* (return value). Câu lệnh `return` lấy một giá trị từ bên trong hàm và gửi nó trở lại dòng đã gọi hàm. Giá trị trả về cho phép bạn chuyển phần lớn những công việc nặng nhọc của chương trình vào các hàm, giúp đơn giản hóa phần thân chương trình.

<!-- pdf-page: 175 | printed: 142 -->

### Trả về một giá trị đơn giản

Hãy xem một hàm nhận vào tên và họ, rồi trả về họ tên đầy đủ được định dạng gọn gàng:

**formatted_name.py**

```python
❶ def get_formatted_name(first_name, last_name):
      """Return a full name, neatly formatted."""
❷     full_name = first_name + ' ' + last_name
❸     return full_name.title()

❹ musician = get_formatted_name('jimi', 'hendrix')
  print(musician)
```

Định nghĩa của `get_formatted_name()` nhận tên và họ làm tham số ❶. Hàm kết hợp hai phần tên này, thêm một dấu cách vào giữa, và lưu kết quả vào `full_name` ❷. Giá trị của `full_name` được chuyển sang kiểu viết hoa chữ cái đầu, rồi được trả về dòng gọi hàm tại ❸.

Khi gọi một hàm có trả về giá trị, bạn cần cung cấp một biến để lưu giá trị trả về. Trong trường hợp này, giá trị trả về được lưu vào biến `musician` tại ❹. Đầu ra hiển thị một cái tên được định dạng gọn gàng, ghép từ các phần trong tên của một người:

```text
Jimi Hendrix
```

Có vẻ như phải làm khá nhiều việc chỉ để có một cái tên được định dạng gọn gàng, trong khi ta có thể chỉ cần viết:

```python
print("Jimi Hendrix")
```

Nhưng khi bạn làm việc với một chương trình lớn cần lưu riêng nhiều tên và họ, những hàm như `get_formatted_name()` trở nên rất hữu ích. Bạn lưu riêng tên và họ, rồi gọi hàm này bất cứ khi nào muốn hiển thị họ tên đầy đủ.

### Làm cho một đối số trở thành tùy chọn

Đôi khi việc làm cho một đối số trở thành tùy chọn là hợp lý, để những người dùng hàm có thể chọn cung cấp thêm thông tin chỉ khi họ muốn. Bạn có thể dùng giá trị mặc định để làm cho một đối số trở thành tùy chọn.

Ví dụ, giả sử chúng ta muốn mở rộng `get_formatted_name()` để xử lý cả tên đệm. Lần thử đầu tiên để thêm tên đệm có thể trông như thế này:

```python
def get_formatted_name(first_name, middle_name, last_name):
    """Return a full name, neatly formatted."""
    full_name = first_name + ' ' + middle_name + ' ' + last_name
    return full_name.title()

musician = get_formatted_name('john', 'lee', 'hooker')
print(musician)
```

<!-- pdf-page: 176 | printed: 143 -->

Hàm này hoạt động khi được cung cấp tên, tên đệm và họ. Hàm nhận cả ba phần của tên rồi tạo một chuỗi từ chúng. Hàm thêm dấu cách ở những chỗ thích hợp và chuyển họ tên đầy đủ sang kiểu viết hoa chữ cái đầu:

```text
John Lee Hooker
```

Nhưng không phải lúc nào cũng cần tên đệm, và hàm được viết như trên sẽ không hoạt động nếu bạn thử gọi nó chỉ với tên và họ. Để làm cho tên đệm trở thành tùy chọn, ta có thể cho đối số `middle_name` một giá trị mặc định rỗng và bỏ qua đối số này trừ khi người dùng cung cấp giá trị. Để `get_formatted_name()` hoạt động khi không có tên đệm, ta đặt giá trị mặc định của `middle_name` là một chuỗi rỗng và chuyển nó xuống cuối danh sách tham số:

```python
❶ def get_formatted_name(first_name, last_name, middle_name=''):
      """Return a full name, neatly formatted."""
❷     if middle_name:
          full_name = first_name + ' ' + middle_name + ' ' + last_name
❸     else:
          full_name = first_name + ' ' + last_name
      return full_name.title()

  musician = get_formatted_name('jimi', 'hendrix')
  print(musician)

❹ musician = get_formatted_name('john', 'hooker', 'lee')
  print(musician)
```

Trong ví dụ này, cái tên được tạo từ ba phần có thể có. Vì luôn có tên và họ, các tham số này được liệt kê trước trong định nghĩa hàm. Tên đệm là tùy chọn, nên nó được liệt kê cuối cùng trong định nghĩa, và giá trị mặc định của nó là một chuỗi rỗng ❶.

Trong thân hàm, chúng ta kiểm tra xem tên đệm có được cung cấp hay không. Python hiểu chuỗi không rỗng là `True`, nên `if middle_name` được đánh giá là `True` nếu lời gọi hàm có đối số tên đệm ❷. Nếu tên đệm được cung cấp, tên, tên đệm và họ được kết hợp để tạo thành họ tên đầy đủ. Tên này sau đó được chuyển sang kiểu viết hoa chữ cái đầu và được trả về dòng gọi hàm, nơi nó được lưu vào biến `musician` và được in ra. Nếu không có tên đệm, chuỗi rỗng không vượt qua phép kiểm tra `if` và khối `else` được chạy ❸. Họ tên đầy đủ được tạo chỉ từ tên và họ, và tên đã định dạng được trả về dòng gọi hàm, nơi nó được lưu vào `musician` và được in ra.

Gọi hàm này với tên và họ khá đơn giản. Tuy nhiên, nếu dùng tên đệm, ta phải đảm bảo tên đệm là đối số cuối cùng được truyền vào để Python ghép đúng các đối số vị trí ❹.

<!-- pdf-page: 177 | printed: 144 -->

Phiên bản đã sửa đổi này của hàm hoạt động với những người chỉ có tên và họ, và cũng hoạt động với những người có tên đệm:

```text
Jimi Hendrix
John Lee Hooker
```

Các giá trị tùy chọn cho phép hàm xử lý nhiều trường hợp sử dụng khác nhau, trong khi vẫn giữ cho lời gọi hàm đơn giản nhất có thể.

### Trả về một dictionary

Một hàm có thể trả về bất kỳ loại giá trị nào bạn cần, kể cả những cấu trúc dữ liệu phức tạp hơn như list và dictionary. Ví dụ, hàm sau nhận vào các phần của tên và trả về một dictionary biểu diễn một người:

**person.py**

```python
  def build_person(first_name, last_name):
      """Return a dictionary of information about a person."""
❶     person = {'first': first_name, 'last': last_name}
❷     return person

  musician = build_person('jimi', 'hendrix')
❸ print(musician)
```

Hàm `build_person()` nhận vào tên và họ, rồi đóng gói các giá trị này vào một dictionary tại ❶. Giá trị của `first_name` được lưu với khóa `'first'`, và giá trị của `last_name` được lưu với khóa `'last'`. Toàn bộ dictionary biểu diễn người đó được trả về tại ❷. Giá trị trả về được in ra tại ❸, với hai mẩu thông tin văn bản ban đầu giờ được lưu trong một dictionary:

```text
{'first': 'jimi', 'last': 'hendrix'}
```

Hàm này nhận vào những thông tin văn bản đơn giản và đặt chúng vào một cấu trúc dữ liệu có ý nghĩa hơn, cho phép bạn làm nhiều việc với thông tin chứ không chỉ in nó ra. Các chuỗi `'jimi'` và `'hendrix'` giờ được gắn nhãn là tên và họ. Bạn có thể dễ dàng mở rộng hàm này để nhận các giá trị tùy chọn như tên đệm, tuổi, nghề nghiệp, hoặc bất kỳ thông tin nào khác bạn muốn lưu về một người. Ví dụ, thay đổi sau cho phép bạn lưu thêm tuổi của một người:

```python
def build_person(first_name, last_name, age=''):
    """Return a dictionary of information about a person."""
    person = {'first': first_name, 'last': last_name}
    if age:
        person['age'] = age
    return person

musician = build_person('jimi', 'hendrix', age=27)
print(musician)
```

<!-- pdf-page: 178 | printed: 145 -->

Chúng ta thêm một tham số tùy chọn mới `age` vào định nghĩa hàm và gán cho tham số này một giá trị mặc định rỗng. Nếu lời gọi hàm có giá trị cho tham số này, giá trị đó được lưu vào dictionary. Hàm này luôn lưu tên của một người, nhưng cũng có thể được sửa đổi để lưu bất kỳ thông tin nào khác bạn muốn về một người.

### Dùng hàm với vòng lặp while

Bạn có thể dùng hàm với mọi cấu trúc Python mà bạn đã học cho đến giờ. Ví dụ, hãy dùng hàm `get_formatted_name()` với một vòng lặp `while` để chào người dùng một cách trang trọng hơn. Đây là lần thử đầu tiên để chào mọi người bằng tên và họ của họ:

**greeter.py**

```python
  def get_formatted_name(first_name, last_name):
      """Return a full name, neatly formatted."""
      full_name = first_name + ' ' + last_name
      return full_name.title()

  # This is an infinite loop!
  while True:
❶     print("\nPlease tell me your name:")
      f_name = input("First name: ")
      l_name = input("Last name: ")

      formatted_name = get_formatted_name(f_name, l_name)
      print("\nHello, " + formatted_name + "!")
```

Trong ví dụ này, chúng ta dùng một phiên bản đơn giản của `get_formatted_name()` không có tên đệm. Vòng lặp `while` yêu cầu người dùng nhập tên, và ta yêu cầu nhập riêng tên và họ ❶.

Nhưng có một vấn đề với vòng lặp `while` này: Chúng ta chưa định nghĩa điều kiện thoát. Khi yêu cầu nhập một loạt đầu vào, bạn đặt điều kiện thoát ở đâu? Ta muốn người dùng có thể thoát dễ dàng nhất có thể, nên mỗi lời nhắc nên cung cấp một cách để thoát. Câu lệnh `break` cung cấp một cách đơn giản để thoát khỏi vòng lặp tại bất kỳ lời nhắc nào:

```python
def get_formatted_name(first_name, last_name):
    """Return a full name, neatly formatted."""
    full_name = first_name + ' ' + last_name
    return full_name.title()

while True:
    print("\nPlease tell me your name:")
    print("(enter 'q' at any time to quit)")

    f_name = input("First name: ")
    if f_name == 'q':
        break

    l_name = input("Last name: ")
    if l_name == 'q':
        break
    formatted_name = get_formatted_name(f_name, l_name)
    print("\nHello, " + formatted_name + "!")
```

<!-- pdf-page: 179 | printed: 146 -->

Chúng ta thêm một thông điệp cho người dùng biết cách thoát, rồi thoát khỏi vòng lặp nếu người dùng nhập giá trị thoát tại bất kỳ lời nhắc nào. Giờ chương trình sẽ tiếp tục chào mọi người cho đến khi có ai đó nhập `'q'` cho tên hoặc họ:

```text
Please tell me your name:
(enter 'q' at any time to quit)
First name: eric
Last name: matthes

Hello, Eric Matthes!

Please tell me your name:
(enter 'q' at any time to quit)
First name: q
```

<!-- box -->

**Tự mình thực hành**

**8-6. Tên thành phố:** Viết một hàm có tên `city_country()` nhận vào tên một thành phố và quốc gia của nó. Hàm nên trả về một chuỗi được định dạng như sau:

```text
"Santiago, Chile"
```

Gọi hàm với ít nhất ba cặp thành phố–quốc gia, và in ra giá trị được trả về.

**8-7. Album:** Viết một hàm có tên `make_album()` xây dựng một dictionary mô tả một album nhạc. Hàm nên nhận vào tên nghệ sĩ và tên album, và trả về một dictionary chứa hai mẩu thông tin này. Dùng hàm để tạo ba dictionary biểu diễn ba album khác nhau. In ra từng giá trị trả về để cho thấy các dictionary đang lưu thông tin album một cách chính xác.

Thêm một tham số tùy chọn cho `make_album()` cho phép bạn lưu số bài hát trong một album. Nếu dòng gọi hàm có giá trị cho số bài hát, hãy thêm giá trị đó vào dictionary của album. Thực hiện ít nhất một lời gọi hàm mới có kèm số bài hát trong album.

**8-8. Album của người dùng:** Bắt đầu với chương trình của bạn từ Bài tập 8-7. Viết một vòng lặp `while` cho phép người dùng nhập tên nghệ sĩ và tên album. Khi đã có thông tin đó, gọi `make_album()` với đầu vào của người dùng và in ra dictionary được tạo. Nhớ đưa vào một giá trị thoát trong vòng lặp `while`.

<!-- /box -->

<!-- pdf-page: 180 | printed: 147 -->

## Truyền một list

Bạn sẽ thường thấy hữu ích khi truyền một list cho hàm, dù đó là list tên, list số hay list các đối tượng phức tạp hơn, chẳng hạn dictionary. Khi bạn truyền một list cho hàm, hàm được truy cập trực tiếp vào nội dung của list. Hãy dùng hàm để làm việc với list hiệu quả hơn.

Giả sử chúng ta có một list người dùng và muốn in lời chào cho từng người. Ví dụ sau gửi một list tên tới một hàm có tên `greet_users()`, hàm chào riêng từng người trong list:

**greet_users.py**

```python
  def greet_users(names):
      """Print a simple greeting to each user in the list."""
      for name in names:
          msg = "Hello, " + name.title() + "!"
          print(msg)

❶ usernames = ['hannah', 'ty', 'margot']
  greet_users(usernames)
```

Chúng ta định nghĩa `greet_users()` sao cho nó mong đợi một list tên, được lưu vào tham số `names`. Hàm lặp qua list nhận được và in lời chào cho từng người dùng. Tại ❶, ta định nghĩa một list người dùng rồi truyền list `usernames` cho `greet_users()` trong lời gọi hàm:

```text
Hello, Hannah!
Hello, Ty!
Hello, Margot!
```

Đây chính là đầu ra chúng ta muốn. Mỗi người dùng đều thấy một lời chào được cá nhân hóa, và bạn có thể gọi hàm bất cứ lúc nào muốn chào một nhóm người dùng cụ thể.

### Sửa đổi list trong hàm

Khi bạn truyền một list cho hàm, hàm có thể sửa đổi list đó. Mọi thay đổi được thực hiện trên list bên trong thân hàm đều là vĩnh viễn, cho phép bạn làm việc hiệu quả ngay cả khi xử lý lượng dữ liệu lớn.

Hãy xét một công ty tạo ra các mô hình in 3D từ những thiết kế do người dùng gửi lên. Các thiết kế cần in được lưu trong một list, và sau khi được in, chúng được chuyển sang một list riêng. Đoạn mã sau làm điều này mà không dùng hàm:

**printing_models.py**

```python
# Start with some designs that need to be printed.
unprinted_designs = ['iphone case', 'robot pendant', 'dodecahedron']
completed_models = []

# Simulate printing each design, until none are left.
#  Move each design to completed_models after printing.
while unprinted_designs:
    current_design = unprinted_designs.pop()
    # Simulate creating a 3D print from the design.
    print("Printing model: " + current_design)
    completed_models.append(current_design)

# Display all completed models.
print("\nThe following models have been printed:")
for completed_model in completed_models:
    print(completed_model)
```

<!-- pdf-page: 181 | printed: 148 -->

Chương trình này bắt đầu với một list các thiết kế cần in và một list rỗng có tên `completed_models`, nơi mỗi thiết kế sẽ được chuyển vào sau khi in xong. Chừng nào trong `unprinted_designs` vẫn còn thiết kế, vòng lặp `while` mô phỏng việc in từng thiết kế bằng cách xóa một thiết kế khỏi cuối list, lưu nó vào `current_design`, và hiển thị một thông điệp cho biết thiết kế hiện tại đang được in. Sau đó, nó thêm thiết kế vào list các mô hình đã hoàn thành. Khi vòng lặp chạy xong, một list các thiết kế đã được in sẽ được hiển thị:

```text
Printing model: dodecahedron
Printing model: robot pendant
Printing model: iphone case

The following models have been printed:
dodecahedron
robot pendant
iphone case
```

Chúng ta có thể tổ chức lại đoạn mã này bằng cách viết hai hàm, mỗi hàm làm một việc cụ thể. Phần lớn mã sẽ không thay đổi; chúng ta chỉ làm cho nó hiệu quả hơn. Hàm thứ nhất sẽ xử lý việc in các thiết kế, và hàm thứ hai sẽ tổng kết những bản in đã được thực hiện:

```python
❶ def print_models(unprinted_designs, completed_models):
      """
      Simulate printing each design, until none are left.
      Move each design to completed_models after printing.
      """
      while unprinted_designs:
          current_design = unprinted_designs.pop()

          # Simulate creating a 3D print from the design.
          print("Printing model: " + current_design)
          completed_models.append(current_design)

❷ def show_completed_models(completed_models):
      """Show all the models that were printed."""
      print("\nThe following models have been printed:")
      for completed_model in completed_models:
          print(completed_model)

  unprinted_designs = ['iphone case', 'robot pendant', 'dodecahedron']
  completed_models = []
  print_models(unprinted_designs, completed_models)
  show_completed_models(completed_models)
```

<!-- pdf-page: 182 | printed: 149 -->

Tại ❶, chúng ta định nghĩa hàm `print_models()` với hai tham số: một list các thiết kế cần in và một list các mô hình đã hoàn thành. Với hai list này, hàm mô phỏng việc in từng thiết kế bằng cách làm rỗng list thiết kế chưa in và lấp đầy list mô hình đã hoàn thành. Tại ❷, chúng ta định nghĩa hàm `show_completed_models()` với một tham số: list các mô hình đã hoàn thành. Với list này, `show_completed_models()` hiển thị tên của từng mô hình đã được in.

Chương trình này có cùng đầu ra như phiên bản không dùng hàm, nhưng mã được tổ chức tốt hơn nhiều. Đoạn mã làm phần lớn công việc đã được chuyển vào hai hàm riêng biệt, giúp phần chính của chương trình dễ hiểu hơn. Hãy nhìn vào phần thân chương trình để thấy việc hiểu chương trình này đang làm gì đã trở nên dễ dàng hơn biết bao:

```python
unprinted_designs = ['iphone case', 'robot pendant', 'dodecahedron']
completed_models = []

print_models(unprinted_designs, completed_models)
show_completed_models(completed_models)
```

Chúng ta thiết lập một list các thiết kế chưa in và một list rỗng sẽ chứa các mô hình đã hoàn thành. Sau đó, vì đã định nghĩa sẵn hai hàm, tất cả những gì ta phải làm là gọi chúng và truyền cho chúng đúng đối số. Ta gọi `print_models()` và truyền cho nó hai list mà nó cần; đúng như mong đợi, `print_models()` mô phỏng việc in các thiết kế. Sau đó, ta gọi `show_completed_models()` và truyền cho nó list các mô hình đã hoàn thành để nó có thể báo cáo những mô hình đã được in. Tên hàm mang tính mô tả cho phép người khác đọc và hiểu đoạn mã này, ngay cả khi không có chú thích.

Chương trình này dễ mở rộng và bảo trì hơn phiên bản không dùng hàm. Nếu sau này cần in thêm thiết kế, ta chỉ cần gọi lại `print_models()`. Nếu nhận ra đoạn mã in cần được sửa đổi, ta chỉ cần sửa một lần, và thay đổi sẽ có hiệu lực ở mọi nơi hàm được gọi. Kỹ thuật này hiệu quả hơn việc phải cập nhật mã riêng rẽ ở nhiều chỗ trong chương trình.

Ví dụ này cũng minh họa ý tưởng rằng mỗi hàm nên có một nhiệm vụ cụ thể. Hàm thứ nhất in từng thiết kế, và hàm thứ hai hiển thị các mô hình đã hoàn thành. Điều này có lợi hơn so với dùng một hàm để làm cả hai việc. Nếu bạn đang viết một hàm và nhận thấy hàm đó làm quá nhiều tác vụ khác nhau, hãy thử tách mã thành hai hàm. Hãy nhớ rằng bạn luôn có thể gọi một hàm từ một hàm khác, điều này có thể hữu ích khi chia một tác vụ phức tạp thành một loạt bước.

### Ngăn hàm sửa đổi list

Đôi khi bạn sẽ muốn ngăn một hàm sửa đổi list. Ví dụ, giả sử bạn bắt đầu với một list các thiết kế chưa in và viết một hàm để chuyển chúng sang list các mô hình đã hoàn thành, như trong ví dụ trước. Có thể bạn quyết định rằng dù đã in tất cả các thiết kế, bạn vẫn muốn giữ list thiết kế chưa in ban đầu để lưu hồ sơ. Nhưng vì bạn đã chuyển hết tên thiết kế ra khỏi `unprinted_designs`, list giờ đã rỗng, và list rỗng là phiên bản duy nhất bạn có; bản gốc đã mất. Trong trường hợp này, bạn có thể giải quyết vấn đề bằng cách truyền cho hàm một bản sao của list chứ không phải bản gốc. Mọi thay đổi mà hàm thực hiện trên list sẽ chỉ ảnh hưởng đến bản sao, còn list gốc vẫn được giữ nguyên.

<!-- pdf-page: 183 | printed: 150 -->

Bạn có thể gửi một bản sao của list cho hàm như sau:

```text
function_name(list_name[:])
```

Ký hiệu lát cắt `[:]` tạo một bản sao của list để gửi cho hàm. Nếu không muốn làm rỗng list thiết kế chưa in trong *print_models.py*, ta có thể gọi `print_models()` như sau:

```text
print_models(unprinted_designs[:], completed_models)
```

Hàm `print_models()` vẫn có thể làm việc của mình vì nó vẫn nhận được tên của tất cả các thiết kế chưa in. Nhưng lần này nó dùng một bản sao của list thiết kế chưa in ban đầu, chứ không phải list `unprinted_designs` thực sự. List `completed_models` sẽ được lấp đầy bằng tên các mô hình đã in như trước, nhưng list thiết kế chưa in ban đầu sẽ không bị hàm làm ảnh hưởng.

Dù bạn có thể giữ nguyên nội dung của một list bằng cách truyền bản sao của nó cho hàm, bạn nên truyền list gốc cho hàm trừ khi có lý do cụ thể để truyền bản sao. Để hàm làm việc với một list có sẵn sẽ hiệu quả hơn, tránh tốn thời gian và bộ nhớ cần thiết để tạo một bản sao riêng, đặc biệt khi bạn làm việc với list lớn.

<!-- box -->

**Tự mình thực hành**

**8-9. Ảo thuật gia:** Tạo một list tên các ảo thuật gia. Truyền list đó cho một hàm có tên `show_magicians()`, hàm in ra tên của từng ảo thuật gia trong list.

**8-10. Ảo thuật gia vĩ đại:** Bắt đầu với một bản sao chương trình của bạn từ Bài tập 8-9. Viết một hàm có tên `make_great()` sửa đổi list ảo thuật gia bằng cách thêm cụm từ *the Great* vào tên của từng ảo thuật gia. Gọi `show_magicians()` để thấy list đã thực sự được sửa đổi.

**8-11. Ảo thuật gia không thay đổi:** Bắt đầu với bài làm của bạn từ Bài tập 8-10. Gọi hàm `make_great()` với một bản sao của list tên ảo thuật gia. Vì list gốc sẽ không thay đổi, hãy trả về list mới và lưu nó vào một list riêng. Gọi `show_magicians()` với mỗi list để cho thấy bạn có một list tên gốc và một list có *the Great* được thêm vào tên của từng ảo thuật gia.

<!-- /box -->

<!-- pdf-page: 184 | printed: 151 -->

## Truyền số lượng đối số tùy ý

Đôi khi bạn sẽ không biết trước một hàm cần nhận bao nhiêu đối số. May mắn thay, Python cho phép một hàm thu thập số lượng đối số tùy ý từ câu lệnh gọi hàm.

Ví dụ, hãy xét một hàm làm pizza. Nó cần nhận một số topping, nhưng bạn không thể biết trước một người sẽ muốn bao nhiêu topping. Hàm trong ví dụ sau có một tham số, `*toppings`, nhưng tham số này thu thập tất cả các đối số mà dòng gọi hàm cung cấp, bất kể bao nhiêu:

**pizza.py**

```python
def make_pizza(*toppings):
    """Print the list of toppings that have been requested."""
    print(toppings)

make_pizza('pepperoni')
make_pizza('mushrooms', 'green peppers', 'extra cheese')
```

Dấu sao trong tên tham số `*toppings` yêu cầu Python tạo một tuple rỗng có tên `toppings` và đóng gói mọi giá trị nhận được vào tuple này. Câu lệnh `print` trong thân hàm tạo ra đầu ra cho thấy Python có thể xử lý cả lời gọi hàm có một giá trị lẫn lời gọi có ba giá trị. Nó xử lý các lời gọi khác nhau theo cách tương tự. Lưu ý rằng Python đóng gói các đối số vào một tuple, ngay cả khi hàm chỉ nhận một giá trị:

```text
('pepperoni',)
('mushrooms', 'green peppers', 'extra cheese')
```

Giờ chúng ta có thể thay câu lệnh `print` bằng một vòng lặp duyệt qua list topping và mô tả chiếc pizza đang được gọi:

```python
def make_pizza(*toppings):
    """Summarize the pizza we are about to make."""
    print("\nMaking a pizza with the following toppings:")
    for topping in toppings:
        print("- " + topping)

make_pizza('pepperoni')
make_pizza('mushrooms', 'green peppers', 'extra cheese')
```

Hàm phản hồi phù hợp, dù nó nhận một giá trị hay ba giá trị:

```text
Making a pizza with the following toppings:
- pepperoni

Making a pizza with the following toppings:
- mushrooms
- green peppers
- extra cheese
```

<!-- pdf-page: 185 | printed: 152 -->

Cú pháp này hoạt động bất kể hàm nhận được bao nhiêu đối số.

### Kết hợp đối số vị trí và đối số tùy ý

Nếu bạn muốn một hàm nhận nhiều loại đối số khác nhau, tham số nhận số lượng đối số tùy ý phải được đặt cuối cùng trong định nghĩa hàm. Python ghép các đối số vị trí và đối số từ khóa trước, rồi thu thập mọi đối số còn lại vào tham số cuối cùng.

Ví dụ, nếu hàm cần nhận kích thước của chiếc pizza, tham số đó phải đứng trước tham số `*toppings`:

```python
def make_pizza(size, *toppings):
    """Summarize the pizza we are about to make."""
    print("\nMaking a " + str(size) +
          "-inch pizza with the following toppings:")
    for topping in toppings:
        print("- " + topping)

make_pizza(16, 'pepperoni')
make_pizza(12, 'mushrooms', 'green peppers', 'extra cheese')
```

Trong định nghĩa hàm, Python lưu giá trị đầu tiên nhận được vào tham số `size`. Tất cả các giá trị khác đứng sau đó được lưu vào tuple `toppings`. Các lời gọi hàm có một đối số cho kích thước trước, theo sau là bao nhiêu topping tùy ý.

Giờ mỗi chiếc pizza có một kích thước và một số topping, và từng mẩu thông tin được in ở đúng chỗ, hiển thị kích thước trước và topping sau:

```text
Making a 16-inch pizza with the following toppings:
- pepperoni

Making a 12-inch pizza with the following toppings:
- mushrooms
- green peppers
- extra cheese
```

### Dùng đối số từ khóa tùy ý

Đôi khi bạn sẽ muốn nhận số lượng đối số tùy ý, nhưng không biết trước loại thông tin nào sẽ được truyền cho hàm. Trong trường hợp này, bạn có thể viết hàm nhận bao nhiêu cặp khóa–giá trị tùy theo câu lệnh gọi hàm cung cấp. Một ví dụ là xây dựng hồ sơ người dùng: bạn biết mình sẽ nhận được thông tin về một người dùng, nhưng không chắc sẽ nhận được loại thông tin gì. Hàm `build_profile()` trong ví dụ sau luôn nhận vào tên và họ, nhưng cũng nhận số lượng đối số từ khóa tùy ý:

<!-- pdf-page: 186 | printed: 153 -->

**user_profile.py**

```python
  def build_profile(first, last, **user_info):
      """Build a dictionary containing everything we know about a user."""
      profile = {}
❶     profile['first_name'] = first
      profile['last_name'] = last
❷     for key, value in user_info.items():
          profile[key] = value
      return profile

  user_profile = build_profile('albert', 'einstein',
                               location='princeton',
                               field='physics')
  print(user_profile)
```

Định nghĩa của `build_profile()` mong đợi tên và họ, rồi cho phép người dùng truyền vào bao nhiêu cặp tên–giá trị tùy thích. Hai dấu sao trước tham số `**user_info` khiến Python tạo một dictionary rỗng có tên `user_info` và đóng gói mọi cặp tên–giá trị nhận được vào dictionary này. Bên trong hàm, bạn có thể truy cập các cặp tên–giá trị trong `user_info` giống như với bất kỳ dictionary nào.

Trong thân `build_profile()`, chúng ta tạo một dictionary rỗng có tên `profile` để chứa hồ sơ của người dùng. Tại ❶, ta thêm tên và họ vào dictionary này vì luôn nhận được hai mẩu thông tin này từ người dùng. Tại ❷, ta lặp qua các cặp khóa–giá trị bổ sung trong dictionary `user_info` và thêm từng cặp vào dictionary `profile`. Cuối cùng, ta trả dictionary `profile` về dòng gọi hàm.

Chúng ta gọi `build_profile()`, truyền cho nó tên `'albert'`, họ `'einstein'`, và hai cặp khóa–giá trị `location='princeton'` và `field='physics'`. Ta lưu `profile` được trả về vào `user_profile` và in `user_profile` ra:

```text
{'first_name': 'albert', 'last_name': 'einstein',
'location': 'princeton', 'field': 'physics'}
```

Dictionary được trả về chứa tên và họ của người dùng, và trong trường hợp này còn có cả nơi ở và lĩnh vực nghiên cứu. Hàm vẫn sẽ hoạt động bất kể có bao nhiêu cặp khóa–giá trị bổ sung được cung cấp trong lời gọi hàm.

Bạn có thể kết hợp các giá trị vị trí, từ khóa và tùy ý theo nhiều cách khác nhau khi viết hàm của riêng mình. Biết rằng tất cả các loại đối số này tồn tại là điều hữu ích, vì bạn sẽ thường gặp chúng khi bắt đầu đọc mã của người khác. Cần luyện tập để học cách dùng đúng các loại khác nhau và biết khi nào nên dùng loại nào. Hiện tại, hãy nhớ dùng cách đơn giản nhất mà vẫn hoàn thành được công việc. Khi tiến bộ hơn, bạn sẽ học được cách dùng phương pháp hiệu quả nhất trong từng trường hợp.

<!-- pdf-page: 187 | printed: 154 -->

<!-- box -->

**Tự mình thực hành**

**8-12. Sandwich:** Viết một hàm nhận một list các món mà một người muốn có trong chiếc sandwich. Hàm nên có một tham số thu thập tất cả các món mà lời gọi hàm cung cấp, và in ra bản tóm tắt chiếc sandwich đang được gọi. Gọi hàm ba lần, mỗi lần dùng một số lượng đối số khác nhau.

**8-13. Hồ sơ người dùng:** Bắt đầu với một bản sao của *user_profile.py* từ trang 153. Xây dựng hồ sơ của chính bạn bằng cách gọi `build_profile()`, dùng tên và họ của bạn cùng ba cặp khóa–giá trị khác mô tả về bạn.

**8-14. Ô tô:** Viết một hàm lưu thông tin về một chiếc ô tô vào một dictionary. Hàm luôn nhận tên nhà sản xuất và tên mẫu xe. Sau đó, nó nhận số lượng đối số từ khóa tùy ý. Gọi hàm với thông tin bắt buộc và hai cặp tên–giá trị khác, chẳng hạn màu sắc hoặc một tính năng tùy chọn. Hàm của bạn nên hoạt động với một lời gọi như sau:

```python
car = make_car('subaru', 'outback', color='blue', tow_package=True)
```

In dictionary được trả về ra để đảm bảo mọi thông tin đã được lưu đúng.

<!-- /box -->

## Lưu hàm trong module

Một ưu điểm của hàm là cách chúng tách các khối mã khỏi chương trình chính. Nhờ dùng tên mang tính mô tả cho hàm, chương trình chính của bạn sẽ dễ theo dõi hơn nhiều. Bạn có thể tiến thêm một bước bằng cách lưu các hàm trong một file riêng được gọi là *module*, rồi *import* (nhập) module đó vào chương trình chính. Câu lệnh `import` yêu cầu Python cung cấp mã trong một module cho file chương trình đang chạy.

Lưu hàm trong một file riêng cho phép bạn ẩn đi chi tiết mã của chương trình và tập trung vào logic ở mức cao hơn. Nó cũng cho phép bạn tái sử dụng hàm trong nhiều chương trình khác nhau. Khi lưu hàm trong các file riêng, bạn có thể chia sẻ những file đó với các lập trình viên khác mà không phải chia sẻ toàn bộ chương trình. Biết cách import hàm cũng cho phép bạn sử dụng các thư viện hàm do các lập trình viên khác viết.

Có nhiều cách để import một module, và tôi sẽ giới thiệu ngắn gọn từng cách.

### Import toàn bộ module

Để bắt đầu import hàm, trước tiên chúng ta cần tạo một module. *Module* là một file có đuôi *.py* chứa đoạn mã mà bạn muốn import vào chương trình. Hãy tạo một module chứa hàm `make_pizza()`. Để tạo module này, chúng ta sẽ xóa mọi thứ khỏi file *pizza.py* trừ hàm `make_pizza()`:

<!-- pdf-page: 188 | printed: 155 -->

**pizza.py**

```python
def make_pizza(size, *toppings):
    """Summarize the pizza we are about to make."""
    print("\nMaking a " + str(size) +
          "-inch pizza with the following toppings:")
    for topping in toppings:
        print("- " + topping)
```

Giờ chúng ta sẽ tạo một file riêng có tên *making_pizzas.py* trong cùng thư mục với *pizza.py*. File này import module vừa tạo rồi gọi `make_pizza()` hai lần:

**making_pizzas.py**

```python
  import pizza
❶ pizza.make_pizza(16, 'pepperoni')
  pizza.make_pizza(12, 'mushrooms', 'green peppers', 'extra cheese')
```

Khi Python đọc file này, dòng `import pizza` yêu cầu Python mở file *pizza.py* và sao chép tất cả các hàm trong đó vào chương trình này. Bạn không thực sự thấy mã được sao chép giữa các file, vì Python sao chép mã ở hậu trường khi chương trình chạy. Tất cả những gì bạn cần biết là mọi hàm được định nghĩa trong *pizza.py* giờ đều có thể dùng trong *making_pizzas.py*.

Để gọi một hàm từ một module đã import, hãy nhập tên module đã import, `pizza`, theo sau là tên hàm, `make_pizza()`, phân tách bằng một dấu chấm ❶. Đoạn mã này cho ra cùng đầu ra như chương trình ban đầu không import module:

```text
Making a 16-inch pizza with the following toppings:
- pepperoni

Making a 12-inch pizza with the following toppings:
- mushrooms
- green peppers
- extra cheese
```

Cách import thứ nhất này, trong đó bạn chỉ cần viết `import` theo sau là tên module, giúp mọi hàm trong module đều dùng được trong chương trình của bạn. Nếu bạn dùng kiểu câu lệnh `import` này để import toàn bộ một module có tên *module_name.py*, mỗi hàm trong module đều có thể được dùng thông qua cú pháp sau:

```text
module_name.function_name()
```

<!-- pdf-page: 189 | printed: 156 -->

### Import các hàm cụ thể

Bạn cũng có thể import một hàm cụ thể từ một module. Đây là cú pháp chung cho cách này:

```python
from module_name import function_name
```

Bạn có thể import bao nhiêu hàm tùy thích từ một module bằng cách phân tách tên từng hàm bằng dấu phẩy:

```python
from module_name import function_0, function_1, function_2
```

Ví dụ *making_pizzas.py* sẽ trông như thế này nếu chúng ta chỉ muốn import hàm mà mình sẽ dùng:

```python
from pizza import make_pizza

make_pizza(16, 'pepperoni')
make_pizza(12, 'mushrooms', 'green peppers', 'extra cheese')
```

Với cú pháp này, bạn không cần dùng ký hiệu dấu chấm khi gọi hàm. Vì chúng ta đã import tường minh hàm `make_pizza()` trong câu lệnh `import`, ta có thể gọi nó bằng tên khi dùng hàm.

### Dùng as để đặt bí danh cho hàm

Nếu tên của một hàm bạn đang import có thể xung đột với một tên đã có trong chương trình, hoặc nếu tên hàm dài, bạn có thể dùng một *bí danh* (alias) ngắn gọn, duy nhất — một cái tên thay thế giống như biệt danh của hàm. Bạn sẽ đặt cho hàm biệt danh đặc biệt này khi import hàm.

Ở đây, chúng ta đặt cho hàm `make_pizza()` một bí danh, `mp()`, bằng cách import `make_pizza as mp`. Từ khóa `as` đổi tên một hàm bằng bí danh mà bạn cung cấp:

```python
from pizza import make_pizza as mp

mp(16, 'pepperoni')
mp(12, 'mushrooms', 'green peppers', 'extra cheese')
```

Câu lệnh `import` ở đây đổi tên hàm `make_pizza()` thành `mp()` trong chương trình này. Bất cứ khi nào muốn gọi `make_pizza()`, ta chỉ cần viết `mp()` thay thế, và Python sẽ chạy đoạn mã trong `make_pizza()`, đồng thời tránh mọi nhầm lẫn với một hàm `make_pizza()` khác mà bạn có thể đã viết trong file chương trình này.

Cú pháp chung để đặt bí danh là:

```python
from module_name import function_name as fn
```

<!-- pdf-page: 190 | printed: 157 -->

### Dùng as để đặt bí danh cho module

Bạn cũng có thể đặt bí danh cho tên module. Đặt cho module một bí danh ngắn, chẳng hạn `p` cho `pizza`, cho phép bạn gọi các hàm của module nhanh hơn. Gọi `p.make_pizza()` ngắn gọn hơn gọi `pizza.make_pizza()`:

```python
import pizza as p

p.make_pizza(16, 'pepperoni')
p.make_pizza(12, 'mushrooms', 'green peppers', 'extra cheese')
```

Module `pizza` được đặt bí danh `p` trong câu lệnh `import`, nhưng tất cả các hàm của module vẫn giữ tên gốc. Gọi các hàm bằng cách viết `p.make_pizza()` không chỉ ngắn gọn hơn viết `pizza.make_pizza()`, mà còn chuyển sự chú ý của bạn khỏi tên module và cho phép bạn tập trung vào tên mang tính mô tả của các hàm. Những tên hàm này, vốn cho bạn biết rõ mỗi hàm làm gì, quan trọng đối với khả năng đọc hiểu mã hơn là việc dùng tên đầy đủ của module.

Cú pháp chung cho cách này là:

```python
import module_name as mn
```

### Import tất cả các hàm trong module

Bạn có thể yêu cầu Python import mọi hàm trong một module bằng cách dùng toán tử dấu sao (`*`):

```python
from pizza import *

make_pizza(16, 'pepperoni')
make_pizza(12, 'mushrooms', 'green peppers', 'extra cheese')
```

Dấu sao trong câu lệnh `import` yêu cầu Python sao chép mọi hàm từ module `pizza` vào file chương trình này. Vì mọi hàm đều được import, bạn có thể gọi từng hàm bằng tên mà không cần dùng ký hiệu dấu chấm. Tuy nhiên, tốt nhất là không nên dùng cách này khi bạn làm việc với những module lớn hơn mà mình không viết: nếu module có một tên hàm trùng với một tên đã có trong dự án của bạn, bạn có thể nhận được những kết quả bất ngờ. Python có thể thấy nhiều hàm hoặc biến có cùng tên, và thay vì import riêng từng hàm, nó sẽ ghi đè các hàm.

Cách tốt nhất là import hàm hoặc các hàm mà bạn muốn, hoặc import toàn bộ module và dùng ký hiệu dấu chấm. Điều này giúp mã rõ ràng, dễ đọc và dễ hiểu. Tôi đưa mục này vào để bạn nhận ra những câu lệnh `import` như sau khi gặp chúng trong mã của người khác:

```python
from module_name import *
```

<!-- pdf-page: 191 | printed: 158 -->

## Định dạng phong cách hàm

Bạn cần lưu ý một vài chi tiết khi định dạng phong cách cho hàm. Hàm nên có tên mang tính mô tả, và những tên này nên dùng chữ thường và dấu gạch dưới. Tên mang tính mô tả giúp bạn và người khác hiểu đoạn mã của bạn đang cố làm gì. Tên module cũng nên tuân theo các quy ước này.

Mỗi hàm nên có một chú thích giải thích ngắn gọn hàm đó làm gì. Chú thích này nên xuất hiện ngay sau định nghĩa hàm và dùng định dạng docstring. Với một hàm được viết tài liệu tốt, các lập trình viên khác có thể sử dụng hàm chỉ bằng cách đọc phần mô tả trong docstring. Họ có thể tin rằng đoạn mã hoạt động đúng như mô tả, và miễn là họ biết tên hàm, các đối số mà hàm cần và loại giá trị mà hàm trả về, họ sẽ có thể dùng nó trong chương trình của mình.

Nếu bạn chỉ định giá trị mặc định cho một tham số, không nên dùng dấu cách ở hai bên dấu bằng:

```python
def function_name(parameter_0, parameter_1='default value')
```

Quy ước tương tự nên được dùng cho các đối số từ khóa trong lời gọi hàm:

```text
function_name(value_0, parameter_1='value')
```

PEP 8 (*https://www.python.org/dev/peps/pep-0008/* ) khuyến nghị giới hạn các dòng mã ở 79 ký tự để mọi dòng đều hiển thị trọn vẹn trong một cửa sổ trình soạn thảo có kích thước hợp lý. Nếu một nhóm tham số khiến định nghĩa hàm dài hơn 79 ký tự, hãy nhấn ENTER sau dấu ngoặc đơn mở trên dòng định nghĩa. Ở dòng tiếp theo, nhấn TAB hai lần để tách danh sách đối số khỏi thân hàm, vốn chỉ được thụt lề một cấp.

Hầu hết các trình soạn thảo tự động căn các dòng tham số bổ sung cho khớp với mức thụt lề bạn đã thiết lập ở dòng đầu tiên:

```python
def function_name(
        parameter_0, parameter_1, parameter_2,
        parameter_3, parameter_4, parameter_5):
    function body...
```

Nếu chương trình hoặc module của bạn có nhiều hơn một hàm, bạn có thể tách các hàm bằng hai dòng trống để dễ thấy chỗ một hàm kết thúc và hàm tiếp theo bắt đầu.

Mọi câu lệnh `import` nên được viết ở đầu file. Ngoại lệ duy nhất là khi bạn dùng chú thích ở đầu file để mô tả toàn bộ chương trình.

<!-- pdf-page: 192 | printed: 159 -->

<!-- box -->

**Tự mình thực hành**

**8-15. In mô hình:** Đặt các hàm của ví dụ *print_models.py* vào một file riêng có tên *printing_functions.py*. Viết một câu lệnh `import` ở đầu *print_models.py*, và sửa file để dùng các hàm đã import.

**8-16. Import:** Dùng một chương trình bạn đã viết có một hàm trong đó, lưu hàm đó vào một file riêng. Import hàm vào file chương trình chính, và gọi hàm theo từng cách sau:

```python
import module_name
from module_name import function_name
from module_name import function_name as fn
import module_name as mn
from module_name import *
```

**8-17. Định dạng phong cách hàm:** Chọn ba chương trình bất kỳ bạn đã viết trong chương này, và đảm bảo chúng tuân theo các hướng dẫn về phong cách được mô tả trong mục này.

<!-- /box -->

## Tổng kết

Trong chương này, bạn đã học cách viết hàm và truyền đối số để hàm có được thông tin cần thiết cho công việc của mình. Bạn đã học cách dùng đối số vị trí và đối số từ khóa, và cách nhận số lượng đối số tùy ý. Bạn đã thấy những hàm hiển thị đầu ra và những hàm trả về giá trị. Bạn đã học cách dùng hàm với list, dictionary, câu lệnh `if` và vòng lặp `while`. Bạn cũng đã thấy cách lưu hàm trong những file riêng gọi là *module*, để các file chương trình của bạn đơn giản và dễ hiểu hơn. Cuối cùng, bạn đã học cách định dạng phong cách cho hàm để chương trình tiếp tục có cấu trúc tốt và dễ đọc nhất có thể đối với bạn và người khác.

Một trong những mục tiêu của bạn với tư cách lập trình viên nên là viết mã đơn giản mà làm đúng điều bạn muốn, và hàm giúp bạn làm được điều đó. Hàm cho phép bạn viết các khối mã và để yên chúng một khi đã biết chúng hoạt động. Khi biết một hàm làm đúng công việc của nó, bạn có thể tin rằng nó sẽ tiếp tục hoạt động và chuyển sang nhiệm vụ lập trình tiếp theo.

Hàm cho phép bạn viết mã một lần rồi tái sử dụng đoạn mã đó bao nhiêu lần tùy thích. Khi cần chạy đoạn mã trong một hàm, tất cả những gì bạn phải làm là viết một lời gọi hàm trên một dòng và hàm sẽ làm công việc của nó. Khi cần sửa đổi hành vi của một hàm, bạn chỉ phải sửa một khối mã, và thay đổi đó có hiệu lực ở mọi nơi bạn đã gọi hàm đó.

Dùng hàm giúp chương trình của bạn dễ đọc hơn, và những tên hàm tốt sẽ tóm tắt những gì mỗi phần của chương trình làm. Đọc một loạt lời gọi hàm giúp bạn nắm được chương trình làm gì nhanh hơn nhiều so với đọc một loạt dài các khối mã.

<!-- pdf-page: 193 | printed: 160 -->

Hàm cũng giúp mã của bạn dễ kiểm thử và gỡ lỗi hơn. Khi phần lớn công việc của chương trình được thực hiện bởi một nhóm hàm, mỗi hàm có một nhiệm vụ cụ thể, việc kiểm thử và bảo trì mã bạn đã viết sẽ dễ dàng hơn nhiều. Bạn có thể viết một chương trình riêng gọi từng hàm và kiểm tra xem mỗi hàm có hoạt động đúng trong mọi tình huống mà nó có thể gặp hay không. Khi làm như vậy, bạn có thể tự tin rằng các hàm của mình sẽ hoạt động đúng mỗi khi bạn gọi chúng.

Trong Chương 9, bạn sẽ học cách viết class. *Class* (lớp) kết hợp hàm và dữ liệu vào một gói gọn gàng có thể được sử dụng theo những cách linh hoạt và hiệu quả.

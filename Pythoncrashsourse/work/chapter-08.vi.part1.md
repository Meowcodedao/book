[[2]]
# Chương 8: Hàm

[[4]]
Trong chương này, bạn sẽ học cách viết *hàm* (function) — những khối mã có tên, được thiết kế để làm một công việc cụ thể. Khi muốn thực hiện một tác vụ cụ thể mà bạn đã định nghĩa trong một hàm, bạn *gọi* (call) tên của hàm phụ trách tác vụ đó. Nếu bạn cần

[[5]]
thực hiện tác vụ đó nhiều lần trong chương trình, bạn không cần gõ đi gõ lại toàn bộ mã cho cùng một tác vụ; bạn chỉ cần gọi hàm chuyên xử lý tác vụ đó, và lời gọi hàm sẽ yêu cầu Python chạy đoạn mã bên trong hàm. Bạn sẽ thấy dùng hàm giúp chương trình dễ viết, dễ đọc, dễ kiểm thử và dễ sửa hơn.

[[6]]
Trong chương này, bạn cũng sẽ học các cách truyền thông tin cho hàm. Bạn sẽ học cách viết những hàm có nhiệm vụ chính là hiển thị thông tin, và những hàm khác được thiết kế để xử lý dữ liệu và trả về một giá trị hoặc một tập giá trị. Cuối cùng, bạn sẽ học cách lưu các hàm trong những file riêng gọi là *module* để giúp sắp xếp các file chương trình chính.

[[8]]
## Định nghĩa hàm

[[9]]
Đây là một hàm đơn giản có tên `greet_user()` in ra một lời chào:

[[12]]
Ví dụ này cho thấy cấu trúc đơn giản nhất của một hàm. Dòng tại ❶ dùng từ khóa `def` để báo cho Python biết bạn đang định nghĩa một hàm. Đây là *định nghĩa hàm* (function definition), cho Python biết tên của hàm và, nếu có, loại thông tin mà hàm cần để thực hiện công việc của nó. Cặp dấu ngoặc đơn chứa thông tin đó. Trong trường hợp này, tên hàm là `greet_user()`, và nó không cần thông tin nào để làm việc, nên cặp ngoặc đơn để trống. (Dù vậy, cặp ngoặc đơn vẫn là bắt buộc.) Cuối cùng, định nghĩa hàm kết thúc bằng một dấu hai chấm.

[[13]]
Mọi dòng thụt lề đứng sau `def greet_user():` tạo thành *thân* (body) của hàm. Đoạn văn bản tại ❷ là một chú thích được gọi là *docstring*, mô tả hàm làm gì. Docstring được bao trong ba dấu nháy kép, thứ mà Python tìm kiếm khi tạo tài liệu cho các hàm trong chương trình của bạn.

[[14]]
Dòng `print("Hello!")` ❸ là dòng mã thực sự duy nhất trong thân hàm này, nên `greet_user()` chỉ có một việc: `print("Hello!")`.

[[15]]
Khi muốn dùng hàm này, bạn gọi nó. Một *lời gọi hàm* (function call) yêu cầu Python thực thi đoạn mã trong hàm. Để *gọi* một hàm, bạn viết tên hàm, theo sau là mọi thông tin cần thiết đặt trong cặp ngoặc đơn, như tại ❹. Vì ở đây không cần thông tin nào, việc gọi hàm chỉ đơn giản là nhập `greet_user()`. Đúng như mong đợi, nó in ra `Hello!`:

[[17]]
### Truyền thông tin cho hàm

[[18]]
Chỉ cần sửa đổi một chút, hàm `greet_user()` không chỉ có thể nói `Hello!` với người dùng mà còn chào họ bằng tên. Để hàm làm được điều này, bạn nhập `username` vào trong cặp ngoặc đơn của định nghĩa hàm tại `def greet_user()`. Bằng cách thêm `username` vào đây, bạn cho phép hàm nhận bất kỳ giá trị `username` nào bạn chỉ định. Giờ hàm mong đợi bạn cung cấp một giá trị cho `username` mỗi khi gọi nó. Khi gọi `greet_user()`, bạn có thể truyền cho nó một cái tên, chẳng hạn `'jesse'`, bên trong cặp ngoặc đơn:

[[21]]
Nhập `greet_user('jesse')` sẽ gọi `greet_user()` và cung cấp cho hàm thông tin cần thiết để thực thi câu lệnh `print`. Hàm nhận cái tên bạn đã truyền vào và hiển thị lời chào cho tên đó:

[[23]]
Tương tự, nhập `greet_user('sarah')` sẽ gọi `greet_user()`, truyền cho nó `'sarah'`, và in ra `Hello, Sarah!` Bạn có thể gọi `greet_user()` bao nhiêu lần tùy thích và truyền cho nó bất kỳ cái tên nào bạn muốn để mỗi lần đều cho ra một đầu ra có thể đoán trước.

[[24]]
### Đối số và tham số

[[25]]
Trong hàm `greet_user()` ở trên, chúng ta đã định nghĩa `greet_user()` để yêu cầu một giá trị cho biến `username`. Khi ta gọi hàm và cung cấp cho nó thông tin (tên một người), nó đã in ra đúng lời chào.

[[26]]
Biến `username` trong định nghĩa của `greet_user()` là một ví dụ về *tham số* (parameter) — một mẩu thông tin mà hàm cần để thực hiện công việc của nó. Giá trị `'jesse'` trong `greet_user('jesse')` là một ví dụ về *đối số* (argument). Đối số là một mẩu thông tin được truyền từ lời gọi hàm tới hàm. Khi gọi hàm, chúng ta đặt giá trị muốn hàm làm việc cùng vào trong cặp ngoặc đơn. Trong trường hợp này, đối số `'jesse'` được truyền cho hàm `greet_user()`, và giá trị đó được lưu vào tham số `username`.

[[27]]
> **Lưu ý** Đôi khi người ta dùng lẫn lộn hai từ đối số và tham số. Đừng ngạc nhiên nếu bạn thấy các biến trong định nghĩa hàm được gọi là đối số, hoặc các biến trong lời gọi hàm được gọi là tham số.

[[29]]
**Tự mình thực hành**

[[30]]
**8-1. Thông điệp:** Viết một hàm có tên `display_message()` in ra một câu cho mọi người biết bạn đang học gì trong chương này. Gọi hàm và đảm bảo thông điệp được hiển thị đúng.

[[31]]
**8-2. Cuốn sách yêu thích:** Viết một hàm có tên `favorite_book()` nhận một tham số, `title`. Hàm nên in ra một thông điệp, chẳng hạn như `One of my favorite books is Alice in Wonderland`. Gọi hàm, nhớ đưa tên một cuốn sách làm đối số trong lời gọi hàm.

[[33]]
## Truyền đối số

[[34]]
Vì một định nghĩa hàm có thể có nhiều tham số, nên một lời gọi hàm có thể cần nhiều đối số. Bạn có thể truyền đối số cho hàm theo nhiều cách. Bạn có thể dùng *đối số vị trí* (positional argument), cần được viết đúng thứ tự như các tham số; *đối số từ khóa* (keyword argument), trong đó mỗi đối số gồm một tên biến và một giá trị; và list hoặc dictionary chứa các giá trị. Hãy lần lượt xem xét từng cách.

[[36]]
### Đối số vị trí

[[37]]
Khi bạn gọi một hàm, Python phải ghép mỗi đối số trong lời gọi hàm với một tham số trong định nghĩa hàm. Cách đơn giản nhất để làm điều này là dựa vào thứ tự của các đối số được cung cấp. Những giá trị được ghép theo cách này được gọi là *đối số vị trí*.

[[38]]
Để xem cách này hoạt động ra sao, hãy xét một hàm hiển thị thông tin về thú cưng. Hàm cho chúng ta biết mỗi con thú cưng là loài vật gì và tên của nó, như sau:

[[41]]
Định nghĩa cho thấy hàm này cần một loài vật và tên của con vật ❶. Khi gọi `describe_pet()`, chúng ta cần cung cấp loài vật và tên, theo đúng thứ tự đó. Ví dụ, trong lời gọi hàm, đối số `'hamster'` được lưu vào tham số `animal_type` và đối số `'harry'` được lưu vào tham số `pet_name` ❷. Trong thân hàm, hai tham số này được dùng để hiển thị thông tin về con thú cưng đang được mô tả.

[[42]]
Đầu ra mô tả một chú chuột hamster tên là Harry:

[[44]]
#### Gọi hàm nhiều lần

[[45]]
Bạn có thể gọi một hàm bao nhiêu lần tùy nhu cầu. Để mô tả một con thú cưng thứ hai khác, chỉ cần thêm một lời gọi `describe_pet()` nữa:

[[47]]
Trong lời gọi hàm thứ hai này, chúng ta truyền cho `describe_pet()` các đối số `'dog'` và `'willie'`. Giống như với nhóm đối số trước, Python ghép `'dog'` với tham số `animal_type` và `'willie'` với tham số `pet_name`. Như trước, hàm thực hiện công việc của mình, nhưng lần này nó in ra các giá trị cho một chú chó tên là Willie. Giờ chúng ta có một chú hamster tên Harry và một chú chó tên Willie:

[[50]]
Gọi một hàm nhiều lần là một cách làm việc rất hiệu quả. Đoạn mã mô tả một con thú cưng chỉ được viết một lần trong hàm. Sau đó, bất cứ khi nào muốn mô tả một con thú cưng mới, bạn gọi hàm với thông tin của con thú cưng mới đó. Ngay cả khi đoạn mã mô tả thú cưng có mở rộng thành mười dòng, bạn vẫn có thể mô tả một con thú cưng mới chỉ bằng một dòng, bằng cách gọi lại hàm.

[[51]]
Bạn có thể dùng bao nhiêu đối số vị trí tùy theo nhu cầu trong các hàm của mình. Python duyệt qua các đối số bạn cung cấp khi gọi hàm và ghép mỗi đối số với tham số tương ứng trong định nghĩa hàm.

[[52]]
#### Thứ tự quan trọng với đối số vị trí

[[53]]
Bạn có thể nhận được kết quả bất ngờ nếu đảo lộn thứ tự các đối số trong lời gọi hàm khi dùng đối số vị trí:

[[55]]
Trong lời gọi hàm này, chúng ta liệt kê tên trước và loài vật sau. Vì lần này đối số `'harry'` được liệt kê trước, giá trị đó được lưu vào tham số `animal_type`. Tương tự, `'hamster'` được lưu vào `pet_name`. Giờ chúng ta có một con “harry” tên là “Hamster”:

[[57]]
Nếu bạn nhận được những kết quả buồn cười như thế này, hãy kiểm tra để đảm bảo thứ tự các đối số trong lời gọi hàm khớp với thứ tự các tham số trong định nghĩa hàm.

[[58]]
### Đối số từ khóa

[[59]]
*Đối số từ khóa* (keyword argument) là một cặp tên–giá trị mà bạn truyền cho hàm. Bạn gắn trực tiếp tên với giá trị ngay trong đối số, nên khi truyền đối số cho hàm sẽ không có sự nhầm lẫn nào (bạn sẽ không bị một con harry tên là Hamster). Đối số từ khóa giúp bạn không phải lo sắp xếp đúng thứ tự các đối số trong lời gọi hàm, đồng thời làm rõ vai trò của từng giá trị trong lời gọi hàm.

[[61]]
Hãy viết lại *pets.py*, dùng đối số từ khóa để gọi `describe_pet()`:

[[63]]
Hàm `describe_pet()` không thay đổi. Nhưng khi gọi hàm, chúng ta nói rõ cho Python biết mỗi đối số nên được ghép với tham số nào. Khi đọc lời gọi hàm, Python biết phải lưu đối số `'hamster'` vào tham số `animal_type` và đối số `'harry'` vào `pet_name`. Đầu ra cho thấy chính xác rằng chúng ta có một chú hamster tên Harry.

[[64]]
Thứ tự của các đối số từ khóa không quan trọng vì Python biết mỗi giá trị nên đi đâu. Hai lời gọi hàm sau là tương đương:

[[66]]
> **Lưu ý** Khi dùng đối số từ khóa, hãy đảm bảo dùng đúng chính xác tên của các tham số trong định nghĩa hàm.

[[67]]
### Giá trị mặc định

[[68]]
Khi viết một hàm, bạn có thể định nghĩa một *giá trị mặc định* (default value) cho mỗi tham số. Nếu một đối số cho tham số được cung cấp trong lời gọi hàm, Python dùng giá trị của đối số đó. Nếu không, nó dùng giá trị mặc định của tham số. Vì vậy, khi định nghĩa giá trị mặc định cho một tham số, bạn có thể bỏ qua đối số tương ứng mà thường phải viết trong lời gọi hàm. Dùng giá trị mặc định có thể đơn giản hóa lời gọi hàm và làm rõ cách hàm thường được sử dụng.

[[69]]
Ví dụ, nếu nhận thấy hầu hết các lời gọi `describe_pet()` đều dùng để mô tả chó, bạn có thể đặt giá trị mặc định của `animal_type` là `'dog'`. Giờ bất kỳ ai gọi `describe_pet()` cho một chú chó đều có thể bỏ qua thông tin đó:

[[72]]
Chúng ta đã thay đổi định nghĩa của `describe_pet()` để thêm giá trị mặc định `'dog'` cho `animal_type`. Giờ khi hàm được gọi mà không chỉ định `animal_type`, Python biết phải dùng giá trị `'dog'` cho tham số này:

[[74]]
Lưu ý rằng thứ tự các tham số trong định nghĩa hàm đã phải thay đổi. Vì giá trị mặc định khiến việc chỉ định loài vật làm đối số trở nên không cần thiết, đối số duy nhất còn lại trong lời gọi hàm là tên của con thú cưng. Python vẫn hiểu đây là một đối số vị trí, nên nếu hàm được gọi chỉ với tên thú cưng, đối số đó sẽ được ghép với tham số đầu tiên được liệt kê trong định nghĩa hàm. Đó là lý do tham số đầu tiên cần phải là `pet_name`.

[[75]]
Cách đơn giản nhất để dùng hàm này bây giờ là chỉ cung cấp tên của chú chó trong lời gọi hàm:

[[77]]
Lời gọi hàm này sẽ có cùng đầu ra như ví dụ trước. Đối số duy nhất được cung cấp là `'willie'`, nên nó được ghép với tham số đầu tiên trong định nghĩa, `pet_name`. Vì không có đối số nào được cung cấp cho `animal_type`, Python dùng giá trị mặc định `'dog'`.

[[78]]
Để mô tả một con vật khác không phải chó, bạn có thể dùng một lời gọi hàm như sau:

[[80]]
Vì một đối số tường minh cho `animal_type` đã được cung cấp, Python sẽ bỏ qua giá trị mặc định của tham số.

[[81]]
> **Lưu ý** Khi dùng giá trị mặc định, mọi tham số có giá trị mặc định cần được liệt kê sau tất cả các tham số không có giá trị mặc định. Điều này cho phép Python tiếp tục hiểu đúng các đối số vị trí.

[[82]]
### Các lời gọi hàm tương đương

[[83]]
Vì đối số vị trí, đối số từ khóa và giá trị mặc định đều có thể được dùng cùng nhau, bạn thường sẽ có nhiều cách tương đương để gọi một hàm. Hãy xét định nghĩa sau của `describe_pets()` với một giá trị mặc định:

[[85]]
Với định nghĩa này, luôn cần cung cấp một đối số cho `pet_name`, và giá trị này có thể được cung cấp theo dạng vị trí hoặc dạng từ khóa. Nếu con vật được mô tả không phải là chó, lời gọi phải có một đối số cho `animal_type`, và đối số này cũng có thể được chỉ định theo dạng vị trí hoặc dạng từ khóa.

[[87]]
Tất cả các lời gọi sau đều hoạt động với hàm này:

[[89]]
Mỗi lời gọi hàm này đều sẽ có cùng đầu ra như các ví dụ trước.

[[90]]
> **Lưu ý** Bạn dùng kiểu gọi hàm nào thực ra không quan trọng lắm. Miễn là lời gọi hàm cho ra đầu ra bạn muốn, hãy dùng kiểu mà bạn thấy dễ hiểu nhất.

[[91]]
### Tránh lỗi đối số

[[92]]
Khi bắt đầu dùng hàm, đừng ngạc nhiên nếu bạn gặp lỗi về đối số không khớp. Đối số không khớp xảy ra khi bạn cung cấp ít hơn hoặc nhiều hơn số đối số mà hàm cần để làm việc. Ví dụ, đây là điều xảy ra nếu chúng ta thử gọi `describe_pet()` mà không có đối số nào:

[[94]]
Python nhận ra rằng lời gọi hàm thiếu một số thông tin, và traceback cho chúng ta biết điều đó:

[[96]]
Tại ❶, traceback cho chúng ta biết vị trí của vấn đề, giúp ta xem lại và thấy rằng lời gọi hàm có chỗ sai. Tại ❷, lời gọi hàm gây lỗi được viết ra để ta xem. Tại ❸, traceback cho biết lời gọi hàm thiếu hai đối số và nêu tên của các đối số bị thiếu. Nếu hàm này nằm trong một file riêng, có lẽ ta vẫn có thể viết lại lời gọi cho đúng mà không cần mở file đó ra đọc mã của hàm.

[[98]]
Python thật hữu ích ở chỗ nó đọc mã của hàm giúp chúng ta và cho biết tên của các đối số cần cung cấp. Đây là thêm một lý do để đặt tên mang tính mô tả cho biến và hàm. Nếu làm vậy, các thông báo lỗi của Python sẽ hữu ích hơn đối với bạn và bất kỳ ai khác có thể dùng mã của bạn.

[[99]]
Nếu cung cấp quá nhiều đối số, bạn sẽ nhận được một traceback tương tự, có thể giúp bạn sửa lời gọi hàm cho khớp với định nghĩa hàm.

[[101]]
**Tự mình thực hành**

[[102]]
**8-3. Áo phông:** Viết một hàm có tên `make_shirt()` nhận vào một cỡ áo và nội dung của một thông điệp sẽ được in lên áo. Hàm nên in ra một câu tóm tắt cỡ áo và thông điệp được in trên áo.

[[103]]
Gọi hàm một lần bằng đối số vị trí để làm một chiếc áo. Gọi hàm lần thứ hai bằng đối số từ khóa.

[[104]]
**8-4. Áo cỡ lớn:** Sửa hàm `make_shirt()` sao cho mặc định áo là cỡ lớn với thông điệp *I love Python*. Làm một chiếc áo cỡ lớn và một chiếc áo cỡ vừa với thông điệp mặc định, và một chiếc áo cỡ bất kỳ với một thông điệp khác.

[[105]]
**8-5. Thành phố:** Viết một hàm có tên `describe_city()` nhận vào tên một thành phố và quốc gia của nó. Hàm nên in ra một câu đơn giản, chẳng hạn như `Reykjavik is in Iceland`. Đặt giá trị mặc định cho tham số quốc gia. Gọi hàm cho ba thành phố khác nhau, trong đó ít nhất một thành phố không thuộc quốc gia mặc định.

[[107]]
## Giá trị trả về

[[108]]
Không phải lúc nào hàm cũng phải hiển thị đầu ra trực tiếp. Thay vào đó, nó có thể xử lý một số dữ liệu rồi trả về một giá trị hoặc một tập giá trị. Giá trị mà hàm trả về được gọi là *giá trị trả về* (return value). Câu lệnh `return` lấy một giá trị từ bên trong hàm và gửi nó trở lại dòng đã gọi hàm. Giá trị trả về cho phép bạn chuyển phần lớn những công việc nặng nhọc của chương trình vào các hàm, giúp đơn giản hóa phần thân chương trình.

[[110]]
### Trả về một giá trị đơn giản

[[111]]
Hãy xem một hàm nhận vào tên và họ, rồi trả về họ tên đầy đủ được định dạng gọn gàng:

[[114]]
Định nghĩa của `get_formatted_name()` nhận tên và họ làm tham số ❶. Hàm kết hợp hai phần tên này, thêm một dấu cách vào giữa, và lưu kết quả vào `full_name` ❷. Giá trị của `full_name` được chuyển sang kiểu viết hoa chữ cái đầu, rồi được trả về dòng gọi hàm tại ❸.

[[115]]
Khi gọi một hàm có trả về giá trị, bạn cần cung cấp một biến để lưu giá trị trả về. Trong trường hợp này, giá trị trả về được lưu vào biến `musician` tại ❹. Đầu ra hiển thị một cái tên được định dạng gọn gàng, ghép từ các phần trong tên của một người:

[[117]]
Có vẻ như phải làm khá nhiều việc chỉ để có một cái tên được định dạng gọn gàng, trong khi ta có thể chỉ cần viết:

[[119]]
Nhưng khi bạn làm việc với một chương trình lớn cần lưu riêng nhiều tên và họ, những hàm như `get_formatted_name()` trở nên rất hữu ích. Bạn lưu riêng tên và họ, rồi gọi hàm này bất cứ khi nào muốn hiển thị họ tên đầy đủ.

[[120]]
### Làm cho một đối số trở thành tùy chọn

[[121]]
Đôi khi việc làm cho một đối số trở thành tùy chọn là hợp lý, để những người dùng hàm có thể chọn cung cấp thêm thông tin chỉ khi họ muốn. Bạn có thể dùng giá trị mặc định để làm cho một đối số trở thành tùy chọn.

[[122]]
Ví dụ, giả sử chúng ta muốn mở rộng `get_formatted_name()` để xử lý cả tên đệm. Lần thử đầu tiên để thêm tên đệm có thể trông như thế này:

[[125]]
Hàm này hoạt động khi được cung cấp tên, tên đệm và họ. Hàm nhận cả ba phần của tên rồi tạo một chuỗi từ chúng. Hàm thêm dấu cách ở những chỗ thích hợp và chuyển họ tên đầy đủ sang kiểu viết hoa chữ cái đầu:

[[127]]
Nhưng không phải lúc nào cũng cần tên đệm, và hàm được viết như trên sẽ không hoạt động nếu bạn thử gọi nó chỉ với tên và họ. Để làm cho tên đệm trở thành tùy chọn, ta có thể cho đối số `middle_name` một giá trị mặc định rỗng và bỏ qua đối số này trừ khi người dùng cung cấp giá trị. Để `get_formatted_name()` hoạt động khi không có tên đệm, ta đặt giá trị mặc định của `middle_name` là một chuỗi rỗng và chuyển nó xuống cuối danh sách tham số:

[[129]]
Trong ví dụ này, cái tên được tạo từ ba phần có thể có. Vì luôn có tên và họ, các tham số này được liệt kê trước trong định nghĩa hàm. Tên đệm là tùy chọn, nên nó được liệt kê cuối cùng trong định nghĩa, và giá trị mặc định của nó là một chuỗi rỗng ❶.

[[130]]
Trong thân hàm, chúng ta kiểm tra xem tên đệm có được cung cấp hay không. Python hiểu chuỗi không rỗng là `True`, nên `if middle_name` được đánh giá là `True` nếu lời gọi hàm có đối số tên đệm ❷. Nếu tên đệm được cung cấp, tên, tên đệm và họ được kết hợp để tạo thành họ tên đầy đủ. Tên này sau đó được chuyển sang kiểu viết hoa chữ cái đầu và được trả về dòng gọi hàm, nơi nó được lưu vào biến `musician` và được in ra. Nếu không có tên đệm, chuỗi rỗng không vượt qua phép kiểm tra `if` và khối `else` được chạy ❸. Họ tên đầy đủ được tạo chỉ từ tên và họ, và tên đã định dạng được trả về dòng gọi hàm, nơi nó được lưu vào `musician` và được in ra.

[[131]]
Gọi hàm này với tên và họ khá đơn giản. Tuy nhiên, nếu dùng tên đệm, ta phải đảm bảo tên đệm là đối số cuối cùng được truyền vào để Python ghép đúng các đối số vị trí ❹.

[[133]]
Phiên bản đã sửa đổi này của hàm hoạt động với những người chỉ có tên và họ, và cũng hoạt động với những người có tên đệm:

[[135]]
Các giá trị tùy chọn cho phép hàm xử lý nhiều trường hợp sử dụng khác nhau, trong khi vẫn giữ cho lời gọi hàm đơn giản nhất có thể.

[[136]]
### Trả về một dictionary

[[137]]
Một hàm có thể trả về bất kỳ loại giá trị nào bạn cần, kể cả những cấu trúc dữ liệu phức tạp hơn như list và dictionary. Ví dụ, hàm sau nhận vào các phần của tên và trả về một dictionary biểu diễn một người:

[[140]]
Hàm `build_person()` nhận vào tên và họ, rồi đóng gói các giá trị này vào một dictionary tại ❶. Giá trị của `first_name` được lưu với khóa `'first'`, và giá trị của `last_name` được lưu với khóa `'last'`. Toàn bộ dictionary biểu diễn người đó được trả về tại ❷. Giá trị trả về được in ra tại ❸, với hai mẩu thông tin văn bản ban đầu giờ được lưu trong một dictionary:

[[142]]
Hàm này nhận vào những thông tin văn bản đơn giản và đặt chúng vào một cấu trúc dữ liệu có ý nghĩa hơn, cho phép bạn làm nhiều việc với thông tin chứ không chỉ in nó ra. Các chuỗi `'jimi'` và `'hendrix'` giờ được gắn nhãn là tên và họ. Bạn có thể dễ dàng mở rộng hàm này để nhận các giá trị tùy chọn như tên đệm, tuổi, nghề nghiệp, hoặc bất kỳ thông tin nào khác bạn muốn lưu về một người. Ví dụ, thay đổi sau cho phép bạn lưu thêm tuổi của một người:

[[145]]
Chúng ta thêm một tham số tùy chọn mới `age` vào định nghĩa hàm và gán cho tham số này một giá trị mặc định rỗng. Nếu lời gọi hàm có giá trị cho tham số này, giá trị đó được lưu vào dictionary. Hàm này luôn lưu tên của một người, nhưng cũng có thể được sửa đổi để lưu bất kỳ thông tin nào khác bạn muốn về một người.

[[146]]
### Dùng hàm với vòng lặp while

[[147]]
Bạn có thể dùng hàm với mọi cấu trúc Python mà bạn đã học cho đến giờ. Ví dụ, hãy dùng hàm `get_formatted_name()` với một vòng lặp `while` để chào người dùng một cách trang trọng hơn. Đây là lần thử đầu tiên để chào mọi người bằng tên và họ của họ:

[[150]]
Trong ví dụ này, chúng ta dùng một phiên bản đơn giản của `get_formatted_name()` không có tên đệm. Vòng lặp `while` yêu cầu người dùng nhập tên, và ta yêu cầu nhập riêng tên và họ ❶.

[[151]]
Nhưng có một vấn đề với vòng lặp `while` này: Chúng ta chưa định nghĩa điều kiện thoát. Khi yêu cầu nhập một loạt đầu vào, bạn đặt điều kiện thoát ở đâu? Ta muốn người dùng có thể thoát dễ dàng nhất có thể, nên mỗi lời nhắc nên cung cấp một cách để thoát. Câu lệnh `break` cung cấp một cách đơn giản để thoát khỏi vòng lặp tại bất kỳ lời nhắc nào:

[[154]]
Chúng ta thêm một thông điệp cho người dùng biết cách thoát, rồi thoát khỏi vòng lặp nếu người dùng nhập giá trị thoát tại bất kỳ lời nhắc nào. Giờ chương trình sẽ tiếp tục chào mọi người cho đến khi có ai đó nhập `'q'` cho tên hoặc họ:

[[157]]
**Tự mình thực hành**

[[158]]
**8-6. Tên thành phố:** Viết một hàm có tên `city_country()` nhận vào tên một thành phố và quốc gia của nó. Hàm nên trả về một chuỗi được định dạng như sau:

[[160]]
Gọi hàm với ít nhất ba cặp thành phố–quốc gia, và in ra giá trị được trả về.

[[161]]
**8-7. Album:** Viết một hàm có tên `make_album()` xây dựng một dictionary mô tả một album nhạc. Hàm nên nhận vào tên nghệ sĩ và tên album, và trả về một dictionary chứa hai mẩu thông tin này. Dùng hàm để tạo ba dictionary biểu diễn ba album khác nhau. In ra từng giá trị trả về để cho thấy các dictionary đang lưu thông tin album một cách chính xác.

[[162]]
Thêm một tham số tùy chọn cho `make_album()` cho phép bạn lưu số bài hát trong một album. Nếu dòng gọi hàm có giá trị cho số bài hát, hãy thêm giá trị đó vào dictionary của album. Thực hiện ít nhất một lời gọi hàm mới có kèm số bài hát trong album.

[[163]]
**8-8. Album của người dùng:** Bắt đầu với chương trình của bạn từ Bài tập 8-7. Viết một vòng lặp `while` cho phép người dùng nhập tên nghệ sĩ và tên album. Khi đã có thông tin đó, gọi `make_album()` với đầu vào của người dùng và in ra dictionary được tạo. Nhớ đưa vào một giá trị thoát trong vòng lặp `while`.

[[166]]
## Truyền một list

[[167]]
Bạn sẽ thường thấy hữu ích khi truyền một list cho hàm, dù đó là list tên, list số hay list các đối tượng phức tạp hơn, chẳng hạn dictionary. Khi bạn truyền một list cho hàm, hàm được truy cập trực tiếp vào nội dung của list. Hãy dùng hàm để làm việc với list hiệu quả hơn.

[[168]]
Giả sử chúng ta có một list người dùng và muốn in lời chào cho từng người. Ví dụ sau gửi một list tên tới một hàm có tên `greet_users()`, hàm chào riêng từng người trong list:

[[171]]
Chúng ta định nghĩa `greet_users()` sao cho nó mong đợi một list tên, được lưu vào tham số `names`. Hàm lặp qua list nhận được và in lời chào cho từng người dùng. Tại ❶, ta định nghĩa một list người dùng rồi truyền list `usernames` cho `greet_users()` trong lời gọi hàm:

[[173]]
Đây chính là đầu ra chúng ta muốn. Mỗi người dùng đều thấy một lời chào được cá nhân hóa, và bạn có thể gọi hàm bất cứ lúc nào muốn chào một nhóm người dùng cụ thể.

[[174]]
### Sửa đổi list trong hàm

[[175]]
Khi bạn truyền một list cho hàm, hàm có thể sửa đổi list đó. Mọi thay đổi được thực hiện trên list bên trong thân hàm đều là vĩnh viễn, cho phép bạn làm việc hiệu quả ngay cả khi xử lý lượng dữ liệu lớn.

[[176]]
Hãy xét một công ty tạo ra các mô hình in 3D từ những thiết kế do người dùng gửi lên. Các thiết kế cần in được lưu trong một list, và sau khi được in, chúng được chuyển sang một list riêng. Đoạn mã sau làm điều này mà không dùng hàm:

[[2]]
# Chương 9: Lớp

[[4]]
*Lập trình hướng đối tượng* (object-oriented programming) là một trong những cách tiếp cận hiệu quả nhất để viết phần mềm. Trong lập trình hướng đối tượng, bạn viết các *lớp* (class) biểu diễn những sự vật và tình huống trong thế giới thực, rồi tạo ra các *đối tượng* (object) dựa trên những lớp này. Khi viết một lớp, bạn định nghĩa hành vi chung mà cả một nhóm đối tượng có thể có.

[[5]]
Khi tạo các đối tượng riêng lẻ từ lớp, mỗi đối tượng tự động được trang bị hành vi chung đó; sau đó, bạn có thể cho mỗi đối tượng bất kỳ đặc điểm riêng nào bạn muốn. Bạn sẽ ngạc nhiên khi thấy các tình huống thực tế có thể được mô hình hóa tốt đến mức nào bằng lập trình hướng đối tượng.

[[6]]
Việc tạo một đối tượng từ một lớp được gọi là *khởi tạo thực thể* (instantiation), và bạn làm việc với các *thực thể* (instance) của một lớp. Trong chương này, bạn sẽ viết các lớp và tạo thực thể của những lớp đó. Bạn sẽ chỉ định loại thông tin có thể được lưu trong các thực thể, và định nghĩa những hành động có thể thực hiện với các thực thể này. Bạn cũng sẽ viết những lớp mở rộng chức năng của các lớp có sẵn, để các lớp tương tự nhau có thể chia sẻ mã một cách hiệu quả. Bạn sẽ lưu các lớp của mình trong module và import những lớp do các lập trình viên khác viết vào file chương trình của bạn.

[[8]]
Hiểu về lập trình hướng đối tượng sẽ giúp bạn nhìn thế giới như một lập trình viên. Nó giúp bạn thực sự hiểu mã của mình — không chỉ những gì đang diễn ra trên từng dòng, mà cả những khái niệm lớn hơn ẩn sau đó. Hiểu được logic đằng sau các lớp sẽ rèn luyện cho bạn tư duy logic, để bạn có thể viết những chương trình giải quyết hiệu quả hầu như mọi vấn đề bạn gặp phải.

[[9]]
Lớp cũng giúp cuộc sống dễ dàng hơn cho bạn và các lập trình viên khác mà bạn sẽ cần cộng tác khi đối mặt với những thử thách ngày càng phức tạp. Khi bạn và các lập trình viên khác viết mã dựa trên cùng một kiểu logic, các bạn sẽ hiểu được công việc của nhau. Chương trình của bạn sẽ dễ hiểu đối với nhiều cộng sự, giúp mọi người cùng làm được nhiều việc hơn.

[[10]]
## Tạo và sử dụng lớp

[[11]]
Bạn có thể mô hình hóa hầu như bất cứ thứ gì bằng lớp. Hãy bắt đầu bằng việc viết một lớp đơn giản, `Dog`, biểu diễn một chú chó — không phải một chú chó cụ thể nào, mà là bất kỳ chú chó nào. Chúng ta biết gì về hầu hết những chú chó nuôi trong nhà? Chà, chúng đều có tên và tuổi. Chúng ta cũng biết rằng hầu hết các chú chó đều biết ngồi và lăn tròn. Hai mẩu thông tin này (tên và tuổi) và hai hành vi này (ngồi và lăn tròn) sẽ được đưa vào lớp `Dog` của chúng ta, vì chúng là điểm chung của hầu hết các chú chó. Lớp này sẽ cho Python biết cách tạo một đối tượng biểu diễn một chú chó. Sau khi viết xong lớp, chúng ta sẽ dùng nó để tạo các thực thể riêng lẻ, mỗi thực thể biểu diễn một chú chó cụ thể.

[[12]]
### Tạo lớp Dog

[[13]]
Mỗi thực thể được tạo từ lớp `Dog` sẽ lưu một `name` và một `age`, và chúng ta sẽ cho mỗi chú chó khả năng `sit()` (ngồi) và `roll_over()` (lăn tròn):

[[17]]
Có rất nhiều điều cần để ý ở đây, nhưng đừng lo. Bạn sẽ gặp cấu trúc này xuyên suốt chương này và có nhiều thời gian để làm quen với nó. Tại ❶, chúng ta định nghĩa một lớp có tên `Dog`. Theo quy ước, tên viết hoa chữ cái đầu chỉ lớp trong Python. Cặp ngoặc đơn trong định nghĩa lớp để trống vì chúng ta đang tạo lớp này từ đầu. Tại ❷, ta viết một docstring mô tả lớp này làm gì.

[[18]]
#### Phương thức __init__()

[[19]]
Một hàm là một phần của lớp được gọi là *phương thức* (method). Mọi điều bạn đã học về hàm cũng áp dụng cho phương thức; điểm khác biệt thực tế duy nhất lúc này là cách chúng ta gọi phương thức. Phương thức `__init__()` tại ❸ là một phương thức đặc biệt mà Python tự động chạy mỗi khi chúng ta tạo một thực thể mới dựa trên lớp `Dog`. Phương thức này có hai dấu gạch dưới ở đầu và hai dấu gạch dưới ở cuối, một quy ước giúp tránh việc tên các phương thức mặc định của Python xung đột với tên phương thức của bạn.

[[20]]
Chúng ta định nghĩa phương thức `__init__()` có ba tham số: `self`, `name` và `age`. Tham số `self` là bắt buộc trong định nghĩa phương thức, và nó phải đứng đầu, trước các tham số khác. Nó phải có mặt trong định nghĩa vì khi Python gọi phương thức `__init__()` này về sau (để tạo một thực thể của `Dog`), lời gọi phương thức sẽ tự động truyền đối số `self`. Mọi lời gọi phương thức gắn với một lớp đều tự động truyền `self`, một tham chiếu tới chính thực thể đó; nó cho phép từng thực thể truy cập các thuộc tính và phương thức trong lớp. Khi tạo một thực thể của `Dog`, Python sẽ gọi phương thức `__init__()` từ lớp `Dog`. Chúng ta sẽ truyền cho `Dog()` một cái tên và một độ tuổi làm đối số; `self` được truyền tự động, nên ta không cần truyền nó. Bất cứ khi nào muốn tạo một thực thể từ lớp `Dog`, ta chỉ cần cung cấp giá trị cho hai tham số cuối, `name` và `age`.

[[21]]
Hai biến được định nghĩa tại ❹ đều có tiền tố `self`. Mọi biến có tiền tố `self` đều có thể được dùng trong mọi phương thức của lớp, và chúng ta cũng có thể truy cập các biến này thông qua bất kỳ thực thể nào được tạo từ lớp. `self.name = name` lấy giá trị được lưu trong tham số `name` và lưu nó vào biến `name`, biến này sau đó được gắn với thực thể đang được tạo. Quá trình tương tự xảy ra với `self.age = age`. Những biến có thể truy cập thông qua thực thể như thế này được gọi là *thuộc tính* (attribute).

[[22]]
Lớp `Dog` có hai phương thức khác được định nghĩa: `sit()` và `roll_over()` ❺. Vì các phương thức này không cần thêm thông tin như tên hay tuổi, chúng ta chỉ định nghĩa chúng với một tham số, `self`. Các thực thể mà ta tạo ra sau này sẽ truy cập được các phương thức này. Nói cách khác, chúng sẽ có thể ngồi và lăn tròn. Hiện tại, `sit()` và `roll_over()` chưa làm được gì nhiều. Chúng chỉ in ra một thông điệp cho biết chú chó đang ngồi hoặc đang lăn tròn. Nhưng khái niệm này có thể được mở rộng cho những tình huống thực tế: nếu lớp này là một phần của một trò chơi máy tính thực sự, các phương thức này sẽ chứa mã để làm một chú chó hoạt hình ngồi và lăn tròn. Nếu lớp này được viết để điều khiển robot, các phương thức này sẽ chỉ đạo các chuyển động khiến một chú chó robot ngồi và lăn tròn.

[[24]]
#### Tạo lớp trong Python 2.7

[[25]]
Khi tạo lớp trong Python 2.7, bạn cần thực hiện một thay đổi nhỏ. Bạn đưa từ `object` vào trong cặp ngoặc đơn khi tạo lớp:

[[27]]
Điều này khiến các lớp trong Python 2.7 hoạt động giống các lớp trong Python 3 hơn, giúp công việc của bạn nhìn chung dễ dàng hơn.

[[28]]
Lớp `Dog` sẽ được định nghĩa như sau trong Python 2.7:

[[30]]
### Tạo thực thể từ lớp

[[31]]
Hãy coi một lớp như một bộ hướng dẫn về cách tạo thực thể. Lớp `Dog` là một bộ hướng dẫn cho Python biết cách tạo các thực thể riêng lẻ biểu diễn những chú chó cụ thể.

[[32]]
Hãy tạo một thực thể biểu diễn một chú chó cụ thể:

[[34]]
Lớp `Dog` mà chúng ta dùng ở đây chính là lớp vừa viết trong ví dụ trước. Tại ❶, ta yêu cầu Python tạo một chú chó có tên là `'willie'` và tuổi là `6`. Khi Python đọc dòng này, nó gọi phương thức `__init__()` trong `Dog` với các đối số `'willie'` và `6`. Phương thức `__init__()` tạo một thực thể biểu diễn chú chó cụ thể này và gán các thuộc tính `name` và `age` bằng các giá trị ta đã cung cấp. Phương thức `__init__()` không có câu lệnh `return` tường minh, nhưng Python tự động trả về một thực thể biểu diễn chú chó này. Ta lưu thực thể đó vào biến `my_dog`. Quy ước đặt tên rất hữu ích ở đây: ta thường có thể giả định rằng một tên viết hoa chữ cái đầu như `Dog` chỉ một lớp, còn một tên viết thường như `my_dog` chỉ một thực thể đơn lẻ được tạo từ một lớp.

[[35]]
#### Truy cập thuộc tính

[[36]]
Để truy cập các thuộc tính của một thực thể, bạn dùng ký hiệu dấu chấm. Tại ❷, chúng ta truy cập giá trị của thuộc tính `name` của `my_dog` bằng cách viết:

[[38]]
Ký hiệu dấu chấm được dùng thường xuyên trong Python. Cú pháp này cho thấy cách Python tìm giá trị của một thuộc tính. Ở đây, Python nhìn vào thực thể `my_dog` rồi tìm thuộc tính `name` gắn với `my_dog`. Đây chính là thuộc tính được gọi là `self.name` trong lớp `Dog`. Tại ❸, ta dùng cách tương tự để làm việc với thuộc tính `age`. Trong câu lệnh `print` đầu tiên, `my_dog.name.title()` khiến `'willie'`, giá trị của thuộc tính `name` của `my_dog`, bắt đầu bằng một chữ cái viết hoa. Trong câu lệnh `print` thứ hai, `str(my_dog.age)` chuyển `6`, giá trị của thuộc tính `age` của `my_dog`, thành một chuỗi.

[[40]]
Đầu ra là bản tóm tắt những gì chúng ta biết về `my_dog`:

[[42]]
#### Gọi phương thức

[[43]]
Sau khi tạo một thực thể từ lớp `Dog`, chúng ta có thể dùng ký hiệu dấu chấm để gọi bất kỳ phương thức nào được định nghĩa trong `Dog`. Hãy cho chú chó của chúng ta ngồi và lăn tròn:

[[45]]
Để gọi một phương thức, hãy viết tên của thực thể (trong trường hợp này là `my_dog`) và phương thức bạn muốn gọi, phân tách bằng một dấu chấm. Khi Python đọc `my_dog.sit()`, nó tìm phương thức `sit()` trong lớp `Dog` và chạy đoạn mã đó. Python hiểu dòng `my_dog.roll_over()` theo cách tương tự.

[[46]]
Giờ Willie làm đúng những gì chúng ta bảo:

[[48]]
Cú pháp này khá hữu ích. Khi các thuộc tính và phương thức được đặt những cái tên mang tính mô tả phù hợp như `name`, `age`, `sit()` và `roll_over()`, ta có thể dễ dàng suy ra một khối mã định làm gì, kể cả khối mã ta chưa từng thấy trước đây.

[[49]]
#### Tạo nhiều thực thể

[[50]]
Bạn có thể tạo bao nhiêu thực thể từ một lớp tùy theo nhu cầu. Hãy tạo chú chó thứ hai có tên `your_dog`:

[[53]]
Trong ví dụ này, chúng ta tạo một chú chó tên Willie và một chú chó tên Lucy. Mỗi chú chó là một thực thể riêng biệt với bộ thuộc tính của riêng nó, và có thể thực hiện cùng một tập hành động:

[[55]]
Ngay cả khi chúng ta dùng cùng tên và tuổi cho chú chó thứ hai, Python vẫn tạo ra một thực thể riêng biệt từ lớp `Dog`. Bạn có thể tạo bao nhiêu thực thể từ một lớp tùy theo nhu cầu, miễn là bạn đặt cho mỗi thực thể một tên biến duy nhất, hoặc mỗi thực thể chiếm một vị trí riêng trong một list hay dictionary.

[[57]]
**Tự mình thực hành**

[[58]]
**9-1. Nhà hàng:** Tạo một lớp có tên `Restaurant`. Phương thức `__init__()` của `Restaurant` nên lưu hai thuộc tính: `restaurant_name` và `cuisine_type`. Tạo một phương thức có tên `describe_restaurant()` in ra hai mẩu thông tin này, và một phương thức có tên `open_restaurant()` in ra thông điệp cho biết nhà hàng đang mở cửa.

[[59]]
Tạo một thực thể có tên `restaurant` từ lớp của bạn. In riêng từng thuộc tính trong hai thuộc tính, rồi gọi cả hai phương thức.

[[60]]
**9-2. Ba nhà hàng:** Bắt đầu với lớp của bạn từ Bài tập 9-1. Tạo ba thực thể khác nhau từ lớp đó, và gọi `describe_restaurant()` cho từng thực thể.

[[61]]
**9-3. Người dùng:** Tạo một lớp có tên `User`. Tạo hai thuộc tính có tên `first_name` và `last_name`, rồi tạo thêm vài thuộc tính khác thường được lưu trong hồ sơ người dùng. Tạo một phương thức có tên `describe_user()` in ra bản tóm tắt thông tin của người dùng. Tạo thêm một phương thức có tên `greet_user()` in ra một lời chào được cá nhân hóa dành cho người dùng.

[[62]]
Tạo vài thực thể biểu diễn những người dùng khác nhau, và gọi cả hai phương thức cho từng người dùng.

[[65]]
## Làm việc với lớp và thực thể

[[66]]
Bạn có thể dùng lớp để biểu diễn nhiều tình huống trong thế giới thực. Sau khi viết một lớp, bạn sẽ dành phần lớn thời gian làm việc với các thực thể được tạo từ lớp đó. Một trong những việc đầu tiên bạn sẽ muốn làm là sửa đổi các thuộc tính gắn với một thực thể cụ thể. Bạn có thể sửa đổi trực tiếp thuộc tính của một thực thể, hoặc viết các phương thức cập nhật thuộc tính theo những cách cụ thể.

[[67]]
### Lớp Car

[[68]]
Hãy viết một lớp mới biểu diễn một chiếc ô tô. Lớp của chúng ta sẽ lưu thông tin về loại ô tô đang xét, và sẽ có một phương thức tóm tắt thông tin này:

[[71]]
Tại ❶ trong lớp `Car`, chúng ta định nghĩa phương thức `__init__()` với tham số `self` đứng đầu, giống như đã làm trước đó với lớp `Dog`. Ta cũng cho nó ba tham số khác: `make` (hãng sản xuất), `model` (mẫu xe) và `year` (năm sản xuất). Phương thức `__init__()` nhận các tham số này và lưu chúng vào các thuộc tính sẽ được gắn với những thực thể được tạo từ lớp này. Khi tạo một thực thể `Car` mới, ta sẽ cần chỉ định hãng sản xuất, mẫu xe và năm sản xuất cho thực thể đó.

[[72]]
Tại ❷, chúng ta định nghĩa một phương thức có tên `get_descriptive_name()` đặt `year`, `make` và `model` của chiếc xe vào một chuỗi mô tả chiếc xe một cách gọn gàng. Điều này giúp ta không phải in riêng giá trị của từng thuộc tính. Để làm việc với các giá trị thuộc tính trong phương thức này, ta dùng `self.make`, `self.model` và `self.year`. Tại ❸, ta tạo một thực thể từ lớp `Car` và lưu nó vào biến `my_new_car`. Sau đó, ta gọi `get_descriptive_name()` để hiển thị loại xe mà ta có:

[[74]]
Để lớp thú vị hơn, hãy thêm một thuộc tính thay đổi theo thời gian. Chúng ta sẽ thêm một thuộc tính lưu tổng số dặm mà chiếc xe đã đi.

[[76]]
### Đặt giá trị mặc định cho thuộc tính

[[77]]
Mọi thuộc tính trong một lớp đều cần một giá trị ban đầu, ngay cả khi giá trị đó là 0 hoặc một chuỗi rỗng. Trong một số trường hợp, chẳng hạn khi đặt giá trị mặc định, việc chỉ định giá trị ban đầu này trong thân phương thức `__init__()` là hợp lý; nếu làm vậy cho một thuộc tính, bạn không cần thêm tham số cho thuộc tính đó.

[[78]]
Hãy thêm một thuộc tính có tên `odometer_reading` luôn bắt đầu với giá trị 0. Chúng ta cũng sẽ thêm một phương thức `read_odometer()` giúp ta đọc đồng hồ đo quãng đường của từng chiếc xe:

[[80]]
Lần này, khi Python gọi phương thức `__init__()` để tạo một thực thể mới, nó lưu các giá trị hãng sản xuất, mẫu xe và năm sản xuất làm thuộc tính như trong ví dụ trước. Sau đó, Python tạo một thuộc tính mới có tên `odometer_reading` và đặt giá trị ban đầu của nó là 0 ❶. Chúng ta cũng có một phương thức mới có tên `read_odometer()` tại ❷ giúp dễ dàng đọc số dặm của một chiếc xe.

[[81]]
Chiếc xe của chúng ta bắt đầu với số dặm là 0:

[[83]]
Không có nhiều chiếc xe được bán ra với đồng hồ đo quãng đường chỉ đúng 0 dặm, nên chúng ta cần một cách để thay đổi giá trị của thuộc tính này.

[[84]]
### Sửa đổi giá trị thuộc tính

[[85]]
Bạn có thể thay đổi giá trị của một thuộc tính theo ba cách: thay đổi giá trị trực tiếp thông qua một thực thể, gán giá trị thông qua một phương thức, hoặc tăng giá trị (cộng thêm một lượng nhất định vào nó) thông qua một phương thức. Hãy xem xét từng cách.

[[87]]
#### Sửa đổi trực tiếp giá trị thuộc tính

[[88]]
Cách đơn giản nhất để sửa đổi giá trị của một thuộc tính là truy cập trực tiếp thuộc tính đó thông qua một thực thể. Ở đây, chúng ta đặt trực tiếp số đo trên đồng hồ thành 23:

[[90]]
Tại ❶, chúng ta dùng ký hiệu dấu chấm để truy cập thuộc tính `odometer_reading` của chiếc xe và đặt trực tiếp giá trị của nó. Dòng này yêu cầu Python lấy thực thể `my_new_car`, tìm thuộc tính `odometer_reading` gắn với nó, và đặt giá trị của thuộc tính đó thành 23:

[[92]]
Đôi khi bạn sẽ muốn truy cập trực tiếp thuộc tính như thế này, nhưng những lúc khác, bạn sẽ muốn viết một phương thức cập nhật giá trị giúp bạn.

[[93]]
#### Sửa đổi giá trị thuộc tính thông qua phương thức

[[94]]
Có những phương thức cập nhật một số thuộc tính nhất định giúp bạn có thể rất hữu ích. Thay vì truy cập trực tiếp thuộc tính, bạn truyền giá trị mới cho một phương thức xử lý việc cập nhật bên trong.

[[95]]
Đây là một ví dụ cho thấy một phương thức có tên `update_odometer()`:

[[97]]
Sửa đổi duy nhất đối với `Car` là việc thêm `update_odometer()` tại ❶. Phương thức này nhận vào một giá trị số dặm và lưu nó vào `self.odometer_reading`. Tại ❷, chúng ta gọi `update_odometer()` và truyền cho nó `23` làm đối số (tương ứng với tham số `mileage` trong định nghĩa phương thức). Nó đặt số đo trên đồng hồ thành 23, và `read_odometer()` in số đo đó ra:

[[100]]
Chúng ta có thể mở rộng phương thức `update_odometer()` để làm thêm việc mỗi khi số đo trên đồng hồ được sửa đổi. Hãy thêm một chút logic để đảm bảo không ai cố quay ngược số đo trên đồng hồ:

[[102]]
Giờ `update_odometer()` kiểm tra xem số đo mới có hợp lý không trước khi sửa đổi thuộc tính. Nếu số dặm mới, `mileage`, lớn hơn hoặc bằng số dặm hiện có, `self.odometer_reading`, bạn có thể cập nhật số đo trên đồng hồ thành số dặm mới ❶. Nếu số dặm mới nhỏ hơn số dặm hiện có, bạn sẽ nhận được cảnh báo rằng bạn không thể quay ngược đồng hồ đo quãng đường ❷.

[[103]]
#### Tăng giá trị thuộc tính thông qua phương thức

[[104]]
Đôi khi bạn sẽ muốn tăng giá trị của một thuộc tính thêm một lượng nhất định thay vì đặt một giá trị hoàn toàn mới. Giả sử chúng ta mua một chiếc xe cũ và chạy thêm 100 dặm trong khoảng thời gian từ lúc mua đến lúc đăng ký xe. Đây là một phương thức cho phép ta truyền lượng tăng thêm này và cộng giá trị đó vào số đo trên đồng hồ:

[[107]]
Phương thức mới `increment_odometer()` tại ❶ nhận vào một số dặm và cộng giá trị này vào `self.odometer_reading`. Tại ❷, chúng ta tạo một chiếc xe cũ, `my_used_car`. Ta đặt đồng hồ của nó thành 23.500 bằng cách gọi `update_odometer()` và truyền cho nó `23500` tại ❸. Tại ❹, ta gọi `increment_odometer()` và truyền cho nó `100` để cộng thêm 100 dặm mà ta đã lái trong khoảng thời gian từ lúc mua xe đến lúc đăng ký:

[[109]]
Bạn có thể dễ dàng sửa đổi phương thức này để từ chối các lượng tăng âm, để không ai dùng hàm này để quay ngược đồng hồ đo quãng đường.

[[110]]
> **Lưu ý** Bạn có thể dùng những phương thức như thế này để kiểm soát cách người dùng chương trình cập nhật các giá trị như số đo trên đồng hồ, nhưng bất kỳ ai có quyền truy cập chương trình đều có thể đặt số đo trên đồng hồ thành bất kỳ giá trị nào bằng cách truy cập trực tiếp thuộc tính. Bảo mật hiệu quả đòi hỏi sự chú ý cực kỳ cẩn thận đến từng chi tiết, bên cạnh những kiểm tra cơ bản như ở đây.

[[112]]
**Tự mình thực hành**

[[113]]
**9-4. Số khách đã phục vụ:** Bắt đầu với chương trình của bạn từ Bài tập 9-1 (trang 166). Thêm một thuộc tính có tên `number_served` với giá trị mặc định là 0. Tạo một thực thể có tên `restaurant` từ lớp này. In ra số khách mà nhà hàng đã phục vụ, rồi thay đổi giá trị này và in ra một lần nữa.

[[114]]
Thêm một phương thức có tên `set_number_served()` cho phép bạn đặt số khách đã được phục vụ. Gọi phương thức này với một số mới và in giá trị ra một lần nữa.

[[115]]
Thêm một phương thức có tên `increment_number_served()` cho phép bạn tăng số khách đã được phục vụ. Gọi phương thức này với bất kỳ số nào bạn thích, có thể biểu thị số khách được phục vụ trong, chẳng hạn, một ngày kinh doanh.

[[116]]
**9-5. Số lần đăng nhập:** Thêm một thuộc tính có tên `login_attempts` vào lớp `User` của bạn từ Bài tập 9-3 (trang 166). Viết một phương thức có tên `increment_login_attempts()` tăng giá trị của `login_attempts` thêm 1. Viết một phương thức khác có tên `reset_login_attempts()` đặt lại giá trị của `login_attempts` về 0.

[[117]]
Tạo một thực thể của lớp `User` và gọi `increment_login_attempts()` vài lần. In giá trị của `login_attempts` ra để đảm bảo nó được tăng đúng, rồi gọi `reset_login_attempts()`. In `login_attempts` ra một lần nữa để đảm bảo nó đã được đặt lại về 0.

[[120]]
## Kế thừa

[[121]]
Không phải lúc nào bạn cũng phải bắt đầu từ đầu khi viết một lớp. Nếu lớp bạn đang viết là một phiên bản chuyên biệt hóa của một lớp khác mà bạn đã viết, bạn có thể dùng *kế thừa* (inheritance). Khi một lớp *kế thừa* từ một lớp khác, nó tự động nhận tất cả các thuộc tính và phương thức của lớp thứ nhất. Lớp ban đầu được gọi là *lớp cha* (parent class), và lớp mới là *lớp con* (child class). Lớp con kế thừa mọi thuộc tính và phương thức từ lớp cha, nhưng cũng được tự do định nghĩa các thuộc tính và phương thức mới của riêng nó.

[[122]]
### Phương thức __init__() của lớp con

[[123]]
Nhiệm vụ đầu tiên của Python khi tạo một thực thể từ lớp con là gán giá trị cho tất cả các thuộc tính trong lớp cha. Để làm điều này, phương thức `__init__()` của lớp con cần sự trợ giúp từ lớp cha của nó.

[[124]]
Ví dụ, hãy mô hình hóa một chiếc ô tô điện. Ô tô điện chỉ là một loại ô tô cụ thể, nên chúng ta có thể xây dựng lớp `ElectricCar` mới dựa trên lớp `Car` đã viết trước đó. Khi đó, ta chỉ phải viết mã cho các thuộc tính và hành vi riêng của ô tô điện.

[[125]]
Hãy bắt đầu bằng việc tạo một phiên bản đơn giản của lớp `ElectricCar`, làm được mọi thứ mà lớp `Car` làm được:

[[129]]
Tại ❶, chúng ta bắt đầu với `Car`. Khi tạo một lớp con, lớp cha phải là một phần của file hiện tại và phải xuất hiện trước lớp con trong file. Tại ❷, ta định nghĩa lớp con, `ElectricCar`. Tên của lớp cha phải được đặt trong cặp ngoặc đơn trong định nghĩa của lớp con. Phương thức `__init__()` tại ❸ nhận vào những thông tin cần thiết để tạo một thực thể `Car`.

[[130]]
Hàm `super()` tại ❹ là một hàm đặc biệt giúp Python tạo liên kết giữa lớp cha và lớp con. Dòng này yêu cầu Python gọi phương thức `__init__()` từ lớp cha của `ElectricCar`, giúp một thực thể `ElectricCar` có tất cả các thuộc tính của lớp cha. Cái tên *super* xuất phát từ quy ước gọi lớp cha là *superclass* (lớp cha) và lớp con là *subclass* (lớp con).

[[131]]
Chúng ta kiểm tra xem kế thừa có hoạt động đúng không bằng cách thử tạo một chiếc ô tô điện với cùng loại thông tin mà ta sẽ cung cấp khi tạo một chiếc ô tô thông thường. Tại ❺, ta tạo một thực thể của lớp `ElectricCar` và lưu nó vào `my_tesla`. Dòng này gọi phương thức `__init__()` được định nghĩa trong `ElectricCar`, phương thức này đến lượt nó yêu cầu Python gọi phương thức `__init__()` được định nghĩa trong lớp cha `Car`. Ta cung cấp các đối số `'tesla'`, `'model s'` và `2016`.

[[132]]
Ngoài `__init__()`, hiện chưa có thuộc tính hay phương thức nào dành riêng cho ô tô điện. Ở thời điểm này, chúng ta chỉ đang đảm bảo rằng ô tô điện có các hành vi phù hợp của `Car`:

[[134]]
Thực thể `ElectricCar` hoạt động giống hệt một thực thể của `Car`, nên giờ chúng ta có thể bắt đầu định nghĩa các thuộc tính và phương thức dành riêng cho ô tô điện.

[[135]]
### Kế thừa trong Python 2.7

[[136]]
Trong Python 2.7, kế thừa hơi khác một chút. Lớp `ElectricCar` sẽ trông như thế này:

[[139]]
Hàm `super()` cần hai đối số: một tham chiếu tới lớp con và đối tượng `self`. Các đối số này là cần thiết để giúp Python tạo liên kết đúng đắn giữa lớp cha và lớp con. Khi dùng kế thừa trong Python 2.7, hãy đảm bảo bạn cũng định nghĩa lớp cha bằng cú pháp `object`.

[[140]]
### Định nghĩa thuộc tính và phương thức cho lớp con

[[141]]
Khi đã có một lớp con kế thừa từ một lớp cha, bạn có thể thêm bất kỳ thuộc tính và phương thức mới nào cần thiết để phân biệt lớp con với lớp cha.

[[142]]
Hãy thêm một thuộc tính dành riêng cho ô tô điện (chẳng hạn một bộ pin) và một phương thức báo cáo về thuộc tính này. Chúng ta sẽ lưu dung lượng pin và viết một phương thức in ra mô tả về bộ pin:

[[144]]
Tại ❶, chúng ta thêm một thuộc tính mới `self.battery_size` và đặt giá trị ban đầu của nó là, chẳng hạn, `70`. Thuộc tính này sẽ được gắn với mọi thực thể được tạo từ lớp `ElectricCar`, nhưng sẽ không được gắn với bất kỳ thực thể nào của `Car`. Ta cũng thêm một phương thức có tên `describe_battery()` in ra thông tin về bộ pin tại ❷. Khi gọi phương thức này, ta nhận được một mô tả rõ ràng là dành riêng cho ô tô điện:

[[146]]
Không có giới hạn nào về mức độ chuyên biệt hóa lớp `ElectricCar`. Bạn có thể thêm bao nhiêu thuộc tính và phương thức tùy ý để mô hình hóa một chiếc ô tô điện ở bất kỳ mức độ chính xác nào bạn cần. Một thuộc tính hoặc phương thức có thể thuộc về bất kỳ chiếc ô tô nào, chứ không chỉ riêng ô tô điện, nên được thêm vào lớp `Car` thay vì lớp `ElectricCar`. Khi đó, bất kỳ ai dùng lớp `Car` cũng sẽ có sẵn chức năng đó, và lớp `ElectricCar` sẽ chỉ chứa mã cho những thông tin và hành vi dành riêng cho xe điện.

[[148]]
### Ghi đè phương thức của lớp cha

[[149]]
Bạn có thể ghi đè (override) bất kỳ phương thức nào của lớp cha không phù hợp với những gì bạn đang cố mô hình hóa bằng lớp con. Để làm điều này, bạn định nghĩa một phương thức trong lớp con có cùng tên với phương thức bạn muốn ghi đè trong lớp cha. Python sẽ bỏ qua phương thức của lớp cha và chỉ để ý đến phương thức bạn định nghĩa trong lớp con.

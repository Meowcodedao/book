[[150]]
Giả sử lớp `Car` có một phương thức tên là `fill_gas_tank()` (đổ đầy bình xăng). Phương thức này vô nghĩa đối với một chiếc xe chạy hoàn toàn bằng điện, nên bạn có thể muốn ghi đè phương thức này. Đây là một cách để làm điều đó:

[[152]]
Giờ nếu ai đó cố gọi `fill_gas_tank()` với một chiếc ô tô điện, Python sẽ bỏ qua phương thức `fill_gas_tank()` trong `Car` và chạy đoạn mã này thay thế. Khi dùng kế thừa, bạn có thể làm cho các lớp con giữ lại những gì bạn cần và ghi đè bất cứ thứ gì bạn không cần từ lớp cha.

[[153]]
### Dùng thực thể làm thuộc tính

[[154]]
Khi mô hình hóa một thứ gì đó trong thế giới thực bằng mã, bạn có thể thấy mình đang thêm ngày càng nhiều chi tiết vào một lớp. Bạn sẽ thấy list các thuộc tính và phương thức ngày càng dài ra và các file của mình trở nên dài dòng. Trong những tình huống này, bạn có thể nhận ra rằng một phần của một lớp có thể được viết thành một lớp riêng. Bạn có thể chia lớp lớn của mình thành những lớp nhỏ hơn làm việc cùng nhau.

[[155]]
Ví dụ, nếu tiếp tục thêm chi tiết vào lớp `ElectricCar`, chúng ta có thể nhận thấy mình đang thêm nhiều thuộc tính và phương thức dành riêng cho bộ pin của xe. Khi thấy điều này xảy ra, ta có thể dừng lại và chuyển những thuộc tính và phương thức đó sang một lớp riêng có tên `Battery`. Sau đó, ta có thể dùng một thực thể `Battery` làm thuộc tính trong lớp `ElectricCar`:

[[158]]
Tại ❶, chúng ta định nghĩa một lớp mới có tên `Battery` không kế thừa từ lớp nào khác. Phương thức `__init__()` tại ❷ có một tham số, `battery_size`, ngoài `self`. Đây là một tham số tùy chọn, đặt dung lượng pin là 70 nếu không có giá trị nào được cung cấp. Phương thức `describe_battery()` cũng đã được chuyển sang lớp này ❸.

[[159]]
Trong lớp `ElectricCar`, giờ chúng ta thêm một thuộc tính có tên `self.battery` ❹. Dòng này yêu cầu Python tạo một thực thể mới của `Battery` (với dung lượng mặc định là 70, vì ta không chỉ định giá trị) và lưu thực thể đó vào thuộc tính `self.battery`. Điều này sẽ xảy ra mỗi khi phương thức `__init__()` được gọi; giờ đây mọi thực thể `ElectricCar` đều sẽ có một thực thể `Battery` được tạo tự động.

[[160]]
Chúng ta tạo một chiếc ô tô điện và lưu nó vào biến `my_tesla`. Khi muốn mô tả bộ pin, ta cần làm việc thông qua thuộc tính `battery` của chiếc xe:

[[162]]
Dòng này yêu cầu Python nhìn vào thực thể `my_tesla`, tìm thuộc tính `battery` của nó, và gọi phương thức `describe_battery()` gắn với thực thể `Battery` được lưu trong thuộc tính đó.

[[163]]
Đầu ra giống hệt những gì chúng ta đã thấy trước đó:

[[166]]
Trông có vẻ phải làm thêm khá nhiều việc, nhưng giờ chúng ta có thể mô tả bộ pin chi tiết đến mức nào tùy thích mà không làm lớp `ElectricCar` trở nên rối rắm. Hãy thêm một phương thức khác vào `Battery` để báo cáo quãng đường xe có thể đi được dựa trên dung lượng pin:

[[168]]
Phương thức mới `get_range()` tại ❶ thực hiện một số phân tích đơn giản. Nếu dung lượng pin là 70 kWh, `get_range()` đặt quãng đường là 240 dặm, và nếu dung lượng là 85 kWh, nó đặt quãng đường là 270 dặm. Sau đó, nó báo cáo giá trị này. Khi muốn dùng phương thức này, một lần nữa ta phải gọi nó thông qua thuộc tính `battery` của chiếc xe tại ❷.

[[169]]
Đầu ra cho chúng ta biết quãng đường xe có thể đi được dựa trên dung lượng pin:

[[171]]
### Mô hình hóa các đối tượng trong thế giới thực

[[172]]
Khi bắt đầu mô hình hóa những thứ phức tạp hơn như ô tô điện, bạn sẽ phải vật lộn với những câu hỏi thú vị. Quãng đường đi được của một chiếc ô tô điện là thuộc tính của bộ pin hay của chiếc xe? Nếu chỉ mô tả một chiếc xe, có lẽ giữ phương thức `get_range()` gắn với lớp `Battery` là được. Nhưng nếu mô tả toàn bộ dòng xe của một nhà sản xuất, có lẽ ta sẽ muốn chuyển `get_range()` sang lớp `ElectricCar`. Phương thức `get_range()` vẫn sẽ kiểm tra dung lượng pin trước khi xác định quãng đường, nhưng nó sẽ báo cáo quãng đường dành riêng cho loại xe mà nó gắn với. Hoặc, ta có thể giữ phương thức `get_range()` gắn với bộ pin nhưng truyền cho nó một tham số như `car_model`. Khi đó, phương thức `get_range()` sẽ báo cáo quãng đường dựa trên dung lượng pin và mẫu xe.

[[174]]
Điều này đưa bạn đến một điểm thú vị trong quá trình trưởng thành của một lập trình viên. Khi vật lộn với những câu hỏi như thế này, bạn đang tư duy ở mức logic cao hơn, chứ không phải ở mức tập trung vào cú pháp. Bạn không nghĩ về Python, mà nghĩ về cách biểu diễn thế giới thực bằng mã. Khi đạt đến điểm này, bạn sẽ nhận ra rằng thường không có cách tiếp cận nào đúng hay sai khi mô hình hóa các tình huống thực tế. Một số cách tiếp cận hiệu quả hơn những cách khác, nhưng cần luyện tập để tìm ra những cách biểu diễn hiệu quả nhất. Nếu mã của bạn đang hoạt động như bạn muốn, bạn đang làm tốt rồi! Đừng nản lòng nếu thấy mình phải đập đi các lớp và viết lại chúng nhiều lần theo những cách khác nhau. Trên hành trình viết mã chính xác và hiệu quả, ai cũng phải trải qua quá trình này.

[[176]]
**Tự mình thực hành**

[[177]]
**9-6. Quầy kem:** Một quầy kem là một loại nhà hàng đặc biệt. Viết một lớp có tên `IceCreamStand` kế thừa từ lớp `Restaurant` mà bạn đã viết trong Bài tập 9-1 (trang 166) hoặc Bài tập 9-4 (trang 171). Phiên bản nào của lớp cũng được; chỉ cần chọn phiên bản bạn thích hơn. Thêm một thuộc tính có tên `flavors` lưu một list các hương vị kem. Viết một phương thức hiển thị các hương vị này. Tạo một thực thể của `IceCreamStand` và gọi phương thức này.

[[178]]
**9-7. Quản trị viên:** Quản trị viên là một loại người dùng đặc biệt. Viết một lớp có tên `Admin` kế thừa từ lớp `User` mà bạn đã viết trong Bài tập 9-3 (trang 166) hoặc Bài tập 9-5 (trang 171). Thêm một thuộc tính, `privileges`, lưu một list các chuỗi như `"can add post"`, `"can delete post"`, `"can ban user"`, v.v. Viết một phương thức có tên `show_privileges()` liệt kê tập quyền hạn của quản trị viên. Tạo một thực thể của `Admin` và gọi phương thức của bạn.

[[179]]
**9-8. Quyền hạn:** Viết một lớp `Privileges` riêng. Lớp này nên có một thuộc tính, `privileges`, lưu một list các chuỗi như mô tả trong Bài tập 9-7. Chuyển phương thức `show_privileges()` sang lớp này. Tạo một thực thể `Privileges` làm thuộc tính trong lớp `Admin`. Tạo một thực thể mới của `Admin` và dùng phương thức của bạn để hiển thị các quyền hạn của nó.

[[180]]
**9-9. Nâng cấp pin:** Dùng phiên bản cuối cùng của *electric_car.py* trong mục này. Thêm một phương thức có tên `upgrade_battery()` vào lớp `Battery`. Phương thức này nên kiểm tra dung lượng pin và đặt dung lượng thành 85 nếu nó chưa phải là 85. Tạo một chiếc ô tô điện với dung lượng pin mặc định, gọi `get_range()` một lần, rồi gọi `get_range()` lần thứ hai sau khi nâng cấp pin. Bạn sẽ thấy quãng đường xe đi được tăng lên.

[[183]]
## Import lớp

[[184]]
Khi bạn thêm nhiều chức năng hơn vào các lớp, file của bạn có thể trở nên dài, ngay cả khi bạn dùng kế thừa đúng cách. Để phù hợp với triết lý chung của Python, bạn sẽ muốn giữ cho các file gọn gàng nhất có thể. Để giúp bạn, Python cho phép lưu các lớp trong module rồi import những lớp cần thiết vào chương trình chính.

[[185]]
### Import một lớp duy nhất

[[186]]
Hãy tạo một module chỉ chứa lớp `Car`. Điều này làm nảy sinh một vấn đề nhỏ về đặt tên: chúng ta đã có một file tên là *car.py* trong chương này, nhưng module này nên được đặt tên là *car.py* vì nó chứa mã biểu diễn một chiếc ô tô. Chúng ta sẽ giải quyết vấn đề đặt tên này bằng cách lưu lớp `Car` vào một module có tên *car.py*, thay thế file *car.py* mà ta đã dùng trước đó. Từ giờ trở đi, mọi chương trình dùng module này sẽ cần một tên file cụ thể hơn, chẳng hạn *my_car.py*. Đây là *car.py* chỉ với mã của lớp `Car`:

[[190]]
Tại ❶, chúng ta đưa vào một docstring cấp module mô tả ngắn gọn nội dung của module này. Bạn nên viết một docstring cho mỗi module bạn tạo ra.

[[191]]
Giờ chúng ta tạo một file riêng có tên *my_car.py*. File này sẽ import lớp `Car` rồi tạo một thực thể từ lớp đó:

[[194]]
Câu lệnh `import` tại ❶ yêu cầu Python mở module `car` và import lớp `Car`. Giờ chúng ta có thể dùng lớp `Car` như thể nó được định nghĩa trong file này. Đầu ra giống như những gì ta đã thấy trước đó:

[[196]]
Import lớp là một cách lập trình hiệu quả. Hãy hình dung file chương trình này sẽ dài đến mức nào nếu toàn bộ lớp `Car` được đưa vào. Khi bạn chuyển lớp vào một module và import module đó, bạn vẫn có đầy đủ chức năng như cũ, nhưng giữ được file chương trình chính gọn gàng và dễ đọc. Bạn cũng lưu phần lớn logic trong các file riêng; một khi các lớp đã hoạt động như bạn muốn, bạn có thể để yên những file đó và tập trung vào logic ở mức cao hơn của chương trình chính.

[[197]]
### Lưu nhiều lớp trong một module

[[198]]
Bạn có thể lưu bao nhiêu lớp tùy nhu cầu trong một module, dù các lớp trong một module nên có liên quan đến nhau theo cách nào đó. Cả hai lớp `Battery` và `ElectricCar` đều giúp biểu diễn ô tô, nên hãy thêm chúng vào module *car.py*:

[[202]]
Giờ chúng ta có thể tạo một file mới có tên *my_electric_car.py*, import lớp `ElectricCar` và tạo một chiếc ô tô điện:

[[205]]
Đoạn mã này có cùng đầu ra như những gì ta đã thấy trước đó, dù phần lớn logic đã được ẩn trong một module:

[[207]]
### Import nhiều lớp từ một module

[[208]]
Bạn có thể import bao nhiêu lớp tùy nhu cầu vào một file chương trình. Nếu muốn tạo một chiếc ô tô thông thường và một chiếc ô tô điện trong cùng một file, ta cần import cả hai lớp, `Car` và `ElectricCar`:

[[212]]
Bạn import nhiều lớp từ một module bằng cách phân tách các lớp bằng dấu phẩy ❶. Khi đã import các lớp cần thiết, bạn có thể tự do tạo bao nhiêu thực thể của mỗi lớp tùy nhu cầu.

[[213]]
Trong ví dụ này, chúng ta tạo một chiếc Volkswagen Beetle thông thường tại ❷ và một chiếc Tesla Roadster chạy điện tại ❸:

[[215]]
### Import toàn bộ module

[[216]]
Bạn cũng có thể import toàn bộ một module rồi truy cập các lớp cần thiết bằng ký hiệu dấu chấm. Cách này đơn giản và cho ra mã dễ đọc. Vì mọi lời gọi tạo thực thể của một lớp đều có kèm tên module, bạn sẽ không gặp xung đột tên với bất kỳ tên nào được dùng trong file hiện tại.

[[217]]
Đây là cách import toàn bộ module `car` rồi tạo một chiếc ô tô thông thường và một chiếc ô tô điện:

[[220]]
Tại ❶, chúng ta import toàn bộ module `car`. Sau đó, ta truy cập các lớp cần thiết thông qua cú pháp `module_name`.`class_name`. Tại ❷, ta lại tạo một chiếc Volkswagen Beetle, và tại ❸, ta tạo một chiếc Tesla Roadster.

[[221]]
### Import tất cả các lớp từ một module

[[222]]
Bạn có thể import mọi lớp từ một module bằng cú pháp sau:

[[224]]
Cách này không được khuyến khích vì hai lý do. Thứ nhất, việc có thể đọc các câu lệnh `import` ở đầu file và nắm rõ chương trình dùng những lớp nào là rất hữu ích. Với cách này, không rõ bạn đang dùng những lớp nào từ module. Cách này cũng có thể gây nhầm lẫn với các tên trong file. Nếu bạn vô tình import một lớp có cùng tên với một thứ khác trong file chương trình, bạn có thể tạo ra những lỗi khó chẩn đoán. Tôi trình bày cách này ở đây vì dù không được khuyến khích, bạn vẫn có khả năng gặp nó trong mã của người khác.

[[225]]
Nếu cần import nhiều lớp từ một module, tốt hơn hết là bạn import toàn bộ module và dùng cú pháp `module_name.class_name`. Bạn sẽ không thấy tất cả các lớp được dùng ở đầu file, nhưng sẽ thấy rõ module được dùng ở đâu trong chương trình. Bạn cũng sẽ tránh được những xung đột tên tiềm ẩn có thể phát sinh khi import mọi lớp trong một module.

[[227]]
### Import một module vào một module khác

[[228]]
Đôi khi bạn sẽ muốn phân bố các lớp của mình vào nhiều module để không file nào trở nên quá lớn và tránh lưu những lớp không liên quan trong cùng một module. Khi lưu các lớp trong nhiều module, bạn có thể thấy một lớp trong module này phụ thuộc vào một lớp trong module khác. Khi điều này xảy ra, bạn có thể import lớp cần thiết vào module thứ nhất.

[[229]]
Ví dụ, hãy lưu lớp `Car` trong một module và các lớp `ElectricCar` và `Battery` trong một module riêng. Chúng ta sẽ tạo một module mới có tên *electric_car.py* — thay thế file *electric_car.py* đã tạo trước đó — và chỉ sao chép các lớp `Battery` và `ElectricCar` vào file này:

[[232]]
Lớp `ElectricCar` cần truy cập lớp cha của nó là `Car`, nên chúng ta import `Car` trực tiếp vào module tại ❶. Nếu quên dòng này, Python sẽ báo lỗi khi ta thử tạo một thực thể `ElectricCar`. Ta cũng cần cập nhật module `Car` để nó chỉ chứa lớp `Car`:

[[235]]
Giờ chúng ta có thể import riêng từ mỗi module và tạo bất kỳ loại ô tô nào cần thiết:

[[239]]
Tại ❶, chúng ta import `Car` từ module của nó, và `ElectricCar` từ module của nó. Sau đó, ta tạo một chiếc ô tô thông thường và một chiếc ô tô điện. Cả hai loại ô tô đều được tạo đúng:

[[241]]
### Tìm ra quy trình làm việc của riêng bạn

[[242]]
Như bạn thấy, Python cho bạn nhiều lựa chọn về cách tổ chức cấu trúc mã trong một dự án lớn. Biết tất cả những khả năng này là điều quan trọng, để bạn có thể xác định cách tốt nhất để tổ chức các dự án của mình, cũng như hiểu được dự án của người khác.

[[243]]
Khi mới bắt đầu, hãy giữ cho cấu trúc mã đơn giản. Hãy thử làm mọi thứ trong một file và chuyển các lớp sang các module riêng khi mọi thứ đã hoạt động. Nếu bạn thích cách các module và file tương tác với nhau, hãy thử lưu các lớp trong module ngay khi bắt đầu một dự án. Hãy tìm một cách tiếp cận cho phép bạn viết mã chạy được, rồi phát triển tiếp từ đó.

[[245]]
**Tự mình thực hành**

[[246]]
**9-10. Import nhà hàng:** Dùng lớp `Restaurant` mới nhất của bạn, lưu nó vào một module. Tạo một file riêng import `Restaurant`. Tạo một thực thể `Restaurant` và gọi một trong các phương thức của `Restaurant` để cho thấy câu lệnh `import` hoạt động đúng.

[[247]]
**9-11. Import Admin:** Bắt đầu với bài làm của bạn từ Bài tập 9-8 (trang 178). Lưu các lớp `User`, `Privileges` và `Admin` vào một module. Tạo một file riêng, tạo một thực thể `Admin` và gọi `show_privileges()` để cho thấy mọi thứ đang hoạt động đúng.

[[248]]
**9-12. Nhiều module:** Lưu lớp `User` vào một module, và lưu các lớp `Privileges` và `Admin` vào một module riêng. Trong một file riêng, tạo một thực thể `Admin` và gọi `show_privileges()` để cho thấy mọi thứ vẫn hoạt động đúng.

[[250]]
## Thư viện chuẩn của Python

[[251]]
*Thư viện chuẩn của Python* (Python standard library) là một tập hợp các module đi kèm với mọi bản cài đặt Python. Giờ đây khi đã hiểu cơ bản về cách lớp hoạt động, bạn có thể bắt đầu dùng những module như thế này do các lập trình viên khác viết. Bạn có thể dùng bất kỳ hàm hoặc lớp nào trong thư viện chuẩn bằng cách thêm một câu lệnh `import` đơn giản ở đầu file. Hãy xem một lớp, `OrderedDict`, từ module `collections`.

[[253]]
Dictionary cho phép bạn kết nối các mẩu thông tin, nhưng chúng không theo dõi thứ tự bạn thêm các cặp khóa–giá trị. Nếu bạn đang tạo một dictionary và muốn theo dõi thứ tự các cặp khóa–giá trị được thêm vào, bạn có thể dùng lớp `OrderedDict` từ module `collections`. Các thực thể của lớp `OrderedDict` hoạt động gần như giống hệt dictionary, chỉ khác là chúng theo dõi thứ tự các cặp khóa–giá trị được thêm vào.

[[254]]
Hãy xem lại ví dụ *favorite_languages.py* từ Chương 6. Lần này, chúng ta sẽ theo dõi thứ tự mọi người trả lời khảo sát:

[[257]]
Chúng ta bắt đầu bằng việc import lớp `OrderedDict` từ module `collections` tại ❶. Tại ❷, ta tạo một thực thể của lớp `OrderedDict` và lưu thực thể này vào `favorite_languages`. Hãy để ý rằng không có dấu ngoặc nhọn nào; lời gọi `OrderedDict()` tạo một dictionary có thứ tự rỗng cho chúng ta và lưu nó vào `favorite_languages`. Sau đó, ta lần lượt thêm từng tên và ngôn ngữ vào `favorite_languages` ❸. Giờ khi lặp qua `favorite_languages` tại ❹, ta biết mình sẽ luôn nhận lại các câu trả lời theo đúng thứ tự chúng được thêm vào:

[[259]]
Đây là một lớp rất đáng biết, vì nó kết hợp lợi ích chính của list (giữ nguyên thứ tự ban đầu) với tính năng chính của dictionary (kết nối các mẩu thông tin). Khi bắt đầu mô hình hóa những tình huống thực tế mà bạn quan tâm, có lẽ bạn sẽ gặp một tình huống mà dictionary có thứ tự chính là thứ bạn cần. Khi tìm hiểu thêm về thư viện chuẩn, bạn sẽ quen thuộc với nhiều module như thế này giúp bạn xử lý những tình huống thường gặp.

[[260]]
> **Lưu ý** Bạn cũng có thể tải module từ các nguồn bên ngoài. Bạn sẽ thấy một số ví dụ như vậy trong Phần II, nơi chúng ta sẽ cần các module bên ngoài để hoàn thành từng dự án.

[[263]]
**Tự mình thực hành**

[[264]]
**9-13. Viết lại bằng OrderedDict:** Bắt đầu với Bài tập 6-4 (trang 108), nơi bạn đã dùng một dictionary thông thường để biểu diễn một bảng thuật ngữ. Viết lại chương trình bằng lớp `OrderedDict` và đảm bảo thứ tự của đầu ra khớp với thứ tự các cặp khóa–giá trị được thêm vào dictionary.

[[265]]
**9-14. Xúc xắc:** Module `random` chứa các hàm tạo số ngẫu nhiên theo nhiều cách khác nhau. Hàm `randint()` trả về một số nguyên trong khoảng mà bạn cung cấp. Đoạn mã sau trả về một số từ 1 đến 6:

[[267]]
Tạo một lớp `Die` (con xúc xắc) với một thuộc tính có tên `sides`, có giá trị mặc định là 6. Viết một phương thức có tên `roll_die()` in ra một số ngẫu nhiên từ 1 đến số mặt của con xúc xắc. Tạo một con xúc xắc 6 mặt và gieo nó 10 lần.

[[268]]
Tạo một con xúc xắc 10 mặt và một con xúc xắc 20 mặt. Gieo mỗi con xúc xắc 10 lần.

[[269]]
**9-15. Python Module of the Week:** Một tài nguyên tuyệt vời để khám phá thư viện chuẩn của Python là trang web có tên *Python Module of the Week*. Hãy truy cập *http://pymotw.com/* và xem mục lục. Tìm một module bạn thấy thú vị và đọc về nó, hoặc khám phá tài liệu của các module `collections` và `random`.

[[271]]
## Định dạng phong cách lớp

[[272]]
Có một vài vấn đề về phong cách liên quan đến lớp đáng được làm rõ, đặc biệt khi chương trình của bạn ngày càng phức tạp.

[[273]]
Tên lớp nên được viết theo kiểu *CamelCaps*. Để làm điều này, hãy viết hoa chữ cái đầu của mỗi từ trong tên và không dùng dấu gạch dưới. Tên thực thể và tên module nên được viết bằng chữ thường, với dấu gạch dưới giữa các từ.

[[274]]
Mỗi lớp nên có một docstring ngay sau định nghĩa lớp. Docstring nên là một mô tả ngắn gọn về những gì lớp làm, và bạn nên tuân theo các quy ước định dạng giống như khi viết docstring cho hàm. Mỗi module cũng nên có một docstring mô tả các lớp trong module có thể được dùng vào việc gì.

[[275]]
Bạn có thể dùng dòng trống để tổ chức mã, nhưng đừng lạm dụng. Bên trong một lớp, bạn có thể dùng một dòng trống giữa các phương thức, và bên trong một module, bạn có thể dùng hai dòng trống để phân tách các lớp.

[[276]]
Nếu cần import một module từ thư viện chuẩn và một module do bạn viết, hãy đặt câu lệnh import cho module của thư viện chuẩn trước. Sau đó thêm một dòng trống và câu lệnh import cho module do bạn viết. Trong những chương trình có nhiều câu lệnh import, quy ước này giúp dễ thấy các module khác nhau được dùng trong chương trình đến từ đâu.

[[278]]
## Tổng kết

[[279]]
Trong chương này, bạn đã học cách viết lớp của riêng mình. Bạn đã học cách lưu thông tin trong một lớp bằng thuộc tính và cách viết các phương thức mang lại cho lớp những hành vi cần thiết. Bạn đã học cách viết phương thức `__init__()` để tạo thực thể từ lớp với đúng những thuộc tính bạn muốn. Bạn đã thấy cách sửa đổi các thuộc tính của một thực thể một cách trực tiếp và thông qua phương thức. Bạn đã biết rằng kế thừa có thể đơn giản hóa việc tạo những lớp có liên quan đến nhau, và đã học cách dùng thực thể của một lớp làm thuộc tính trong một lớp khác để giữ cho mỗi lớp đơn giản.

[[280]]
Bạn đã thấy việc lưu các lớp trong module và import những lớp cần thiết vào các file sẽ dùng chúng có thể giúp dự án của bạn ngăn nắp như thế nào. Bạn đã bắt đầu tìm hiểu về thư viện chuẩn của Python, và đã thấy một ví dụ dựa trên lớp `OrderedDict` từ module `collections`. Cuối cùng, bạn đã học cách định dạng phong cách cho lớp theo các quy ước của Python.

[[281]]
Trong Chương 10, bạn sẽ học cách làm việc với file để có thể lưu lại công việc bạn đã làm trong một chương trình và công việc bạn đã cho phép người dùng thực hiện. Bạn cũng sẽ tìm hiểu về *ngoại lệ* (exception), một lớp Python đặc biệt được thiết kế để giúp bạn phản hồi các lỗi khi chúng xảy ra.

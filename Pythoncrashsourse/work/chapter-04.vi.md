[[2]]
# Chương 4: Làm việc với list

[[4]]
Trong Chương 3, bạn đã học cách tạo một list đơn giản và làm việc với từng phần tử trong list. Trong chương này, bạn sẽ học cách *lặp* (loop) qua toàn bộ một list chỉ với vài dòng mã, bất kể

[[5]]
list đó dài bao nhiêu. Vòng lặp cho phép bạn thực hiện cùng một hành động, hoặc một nhóm hành động, với mọi phần tử trong list. Nhờ đó, bạn có thể làm việc hiệu quả với list ở mọi độ dài, kể cả những list có hàng nghìn hay thậm chí hàng triệu phần tử.

[[6]]
## Lặp qua toàn bộ list

[[7]]
Bạn sẽ thường muốn duyệt qua tất cả các mục trong một list và thực hiện cùng một tác vụ với từng phần tử. Ví dụ, trong một trò chơi, bạn có thể muốn di chuyển mọi đối tượng trên màn hình một khoảng như nhau; hoặc với một list số, bạn có thể muốn thực hiện cùng một phép tính thống kê trên mọi phần tử. Hay có thể bạn muốn hiển thị từng tiêu đề trong một list bài viết trên trang web. Khi muốn thực hiện cùng một hành động với mọi phần tử trong list, bạn có thể dùng vòng lặp `for` của Python.

[[9]]
Giả sử chúng ta có một list tên các ảo thuật gia và muốn in ra từng tên trong list. Chúng ta có thể làm điều này bằng cách lấy từng tên ra khỏi list một cách riêng lẻ, nhưng cách này có thể gây ra vài vấn đề. Thứ nhất, làm như vậy với một list tên dài sẽ rất lặp đi lặp lại. Thứ hai, chúng ta sẽ phải sửa mã mỗi khi độ dài của list thay đổi. Vòng lặp `for` tránh được cả hai vấn đề này bằng cách để Python tự xử lý chúng bên trong.

[[10]]
Hãy dùng vòng lặp `for` để in ra từng tên trong list ảo thuật gia:

[[13]]
Chúng ta bắt đầu bằng việc định nghĩa một list tại ❶, giống như đã làm ở Chương 3. Tại ❷, chúng ta định nghĩa một vòng lặp `for`. Dòng này yêu cầu Python lấy một tên từ list `magicians` và lưu nó vào biến `magician`. Tại ❸, chúng ta yêu cầu Python in ra cái tên vừa được lưu vào `magician`. Sau đó Python lặp lại các dòng ❷ và ❸, mỗi lần cho một tên trong list. Có thể sẽ dễ hiểu hơn nếu bạn đọc đoạn mã này là “Với mỗi ảo thuật gia trong list các ảo thuật gia, hãy in ra tên của ảo thuật gia đó.” Đầu ra chỉ đơn giản là từng tên trong list được in ra:

[[15]]
### Xem kỹ hơn về vòng lặp

[[16]]
Khái niệm vòng lặp rất quan trọng, vì đây là một trong những cách phổ biến nhất để máy tính tự động hóa các tác vụ lặp đi lặp lại. Ví dụ, trong một vòng lặp đơn giản như vòng lặp chúng ta đã dùng trong *magicians.py*, đầu tiên Python đọc dòng đầu tiên của vòng lặp:

[[18]]
Dòng này yêu cầu Python lấy giá trị đầu tiên từ list `magicians` và lưu nó vào biến `magician`. Giá trị đầu tiên này là `'alice'`. Sau đó Python đọc dòng tiếp theo:

[[20]]
Python in ra giá trị hiện tại của `magician`, vẫn là `'alice'`. Vì list còn chứa thêm giá trị, Python quay lại dòng đầu tiên của vòng lặp:

[[22]]
Python lấy tên tiếp theo trong list, `'david'`, và lưu giá trị đó vào `magician`. Sau đó Python thực thi dòng:

[[25]]
Python lại in ra giá trị hiện tại của `magician`, lúc này là `'david'`. Python lặp lại toàn bộ vòng lặp thêm một lần nữa với giá trị cuối cùng trong list, `'carolina'`. Vì list không còn giá trị nào nữa, Python chuyển sang dòng tiếp theo của chương trình. Trong trường hợp này, không có gì đứng sau vòng lặp `for`, nên chương trình đơn giản là kết thúc.

[[26]]
Khi dùng vòng lặp lần đầu, hãy nhớ rằng nhóm các bước sẽ được lặp lại một lần cho mỗi phần tử trong list, bất kể list có bao nhiêu phần tử. Nếu list của bạn có một triệu phần tử, Python sẽ lặp lại các bước này một triệu lần — và thường là rất nhanh.

[[27]]
Ngoài ra, khi tự viết vòng lặp `for`, hãy nhớ rằng bạn có thể chọn bất kỳ tên nào bạn muốn cho biến tạm giữ từng giá trị trong list. Tuy nhiên, chọn một cái tên có ý nghĩa, biểu thị một phần tử đơn lẻ của list, sẽ rất có ích. Ví dụ, đây là cách tốt để bắt đầu một vòng lặp `for` cho một list mèo, một list chó và một list phần tử nói chung:

[[29]]
Những quy ước đặt tên này giúp bạn dễ theo dõi hành động được thực hiện trên từng phần tử bên trong vòng lặp `for`. Dùng tên số ít và số nhiều giúp bạn nhận biết một đoạn mã đang làm việc với một phần tử đơn lẻ của list hay với toàn bộ list.

[[30]]
### Làm thêm nhiều việc bên trong vòng lặp for

[[31]]
Bạn có thể làm hầu như bất cứ điều gì với từng phần tử trong vòng lặp `for`. Hãy mở rộng ví dụ trước bằng cách in ra một thông điệp gửi tới từng ảo thuật gia, khen rằng họ đã biểu diễn một màn ảo thuật tuyệt vời:

[[33]]
Điểm khác biệt duy nhất trong đoạn mã này nằm ở ❶, nơi chúng ta soạn một thông điệp gửi tới từng ảo thuật gia, bắt đầu bằng tên của người đó. Ở lần lặp đầu tiên, giá trị của magician là `'alice'`, nên Python bắt đầu thông điệp đầu tiên bằng tên `'Alice'`. Ở lần lặp thứ hai, thông điệp sẽ bắt đầu bằng `'David'`, và ở lần lặp thứ ba, thông điệp sẽ bắt đầu bằng `'Carolina'`.

[[34]]
Đầu ra hiển thị một thông điệp được cá nhân hóa cho từng ảo thuật gia trong list:

[[36]]
Bạn cũng có thể viết bao nhiêu dòng mã tùy thích trong vòng lặp `for`. Mọi dòng được thụt lề đứng sau dòng `for magician in magicians` đều được coi là nằm *bên trong vòng lặp*, và mỗi dòng thụt lề sẽ được thực thi một lần cho mỗi giá trị trong list. Vì vậy, bạn có thể làm bao nhiêu việc tùy ý với từng giá trị trong list.

[[38]]
Hãy thêm dòng thứ hai vào thông điệp, nói với từng ảo thuật gia rằng chúng ta rất mong được xem màn ảo thuật tiếp theo của họ:

[[40]]
Vì chúng ta đã thụt lề cả hai câu lệnh `print`, mỗi dòng sẽ được thực thi một lần cho mỗi ảo thuật gia trong list. Ký tự xuống dòng (`"\n"`) trong câu lệnh `print` thứ hai ❶ chèn một dòng trống sau mỗi lượt lặp. Nhờ đó, ta có một loạt thông điệp được nhóm gọn gàng cho từng người trong list:

[[42]]
Bạn có thể dùng bao nhiêu dòng tùy thích trong vòng lặp `for`. Trong thực tế, khi dùng vòng lặp `for`, bạn sẽ thường thấy hữu ích khi thực hiện nhiều thao tác khác nhau với từng phần tử trong list.

[[43]]
### Làm điều gì đó sau vòng lặp for

[[44]]
Điều gì xảy ra khi vòng lặp `for` đã chạy xong? Thường thì bạn sẽ muốn tổng kết một khối đầu ra hoặc chuyển sang những việc khác mà chương trình phải hoàn thành.

[[45]]
Mọi dòng mã đứng sau vòng lặp `for` mà không được thụt lề sẽ được thực thi một lần, không lặp lại. Hãy viết lời cảm ơn gửi tới cả nhóm ảo thuật gia vì đã mang đến một buổi biểu diễn xuất sắc. Để hiển thị thông điệp chung này sau khi tất cả các thông điệp riêng đã được in, chúng ta đặt lời cảm ơn sau vòng lặp `for` và không thụt lề:

[[48]]
Hai câu lệnh `print` đầu tiên được lặp lại một lần cho mỗi ảo thuật gia trong list, như bạn đã thấy trước đó. Tuy nhiên, vì dòng tại ❶ không được thụt lề, nó chỉ được in một lần:

[[50]]
Khi xử lý dữ liệu bằng vòng lặp `for`, bạn sẽ thấy đây là một cách tốt để tổng kết một thao tác đã được thực hiện trên toàn bộ tập dữ liệu. Ví dụ, bạn có thể dùng vòng lặp `for` để khởi tạo một trò chơi bằng cách duyệt qua list các nhân vật và hiển thị từng nhân vật lên màn hình. Sau đó, bạn có thể viết một khối không thụt lề đứng sau vòng lặp này để hiển thị nút Play Now sau khi tất cả các nhân vật đã được vẽ lên màn hình.

[[51]]
## Tránh lỗi thụt lề

[[52]]
Python dùng thụt lề để xác định khi nào một dòng mã có liên kết với dòng phía trên nó. Trong các ví dụ trước, những dòng in thông điệp gửi tới từng ảo thuật gia là một phần của vòng lặp `for` vì chúng được thụt lề. Cách Python dùng thụt lề khiến mã rất dễ đọc. Về cơ bản, Python dùng khoảng trắng để buộc bạn viết mã được định dạng gọn gàng với cấu trúc trực quan rõ ràng. Trong những chương trình Python dài hơn, bạn sẽ thấy các khối mã được thụt lề ở nhiều cấp khác nhau. Các cấp thụt lề này giúp bạn nắm được cách tổ chức tổng thể của chương trình.

[[53]]
Khi bắt đầu viết mã phụ thuộc vào việc thụt lề đúng, bạn cần để ý một vài *lỗi thụt lề* (indentation error) phổ biến. Ví dụ, đôi khi người ta thụt lề những khối mã không cần thụt lề, hoặc quên thụt lề những khối mã cần thụt lề. Xem ví dụ về những lỗi này ngay bây giờ sẽ giúp bạn tránh chúng trong tương lai và sửa được chúng khi chúng xuất hiện trong chương trình của bạn.

[[54]]
Hãy cùng xem xét một số lỗi thụt lề phổ biến hơn cả.

[[55]]
### Quên thụt lề

[[56]]
Luôn thụt lề dòng đứng sau câu lệnh `for` trong một vòng lặp. Nếu bạn quên, Python sẽ nhắc bạn:

[[60]]
Câu lệnh `print` tại ❶ lẽ ra phải được thụt lề, nhưng nó lại không được thụt lề. Khi Python mong đợi một khối được thụt lề mà không tìm thấy, nó sẽ cho bạn biết dòng nào gặp vấn đề.

[[62]]
Bạn thường có thể khắc phục loại lỗi thụt lề này bằng cách thụt lề dòng hoặc các dòng ngay sau câu lệnh `for`.

[[63]]
### Quên thụt lề các dòng bổ sung

[[64]]
Đôi khi vòng lặp của bạn chạy mà không có lỗi nào nhưng lại không cho ra kết quả mong đợi. Điều này có thể xảy ra khi bạn cố làm nhiều tác vụ trong một vòng lặp và quên thụt lề một vài dòng trong đó.

[[65]]
Ví dụ, đây là điều xảy ra khi chúng ta quên thụt lề dòng thứ hai trong vòng lặp nói với từng ảo thuật gia rằng chúng ta rất mong được xem màn ảo thuật tiếp theo của họ:

[[67]]
Câu lệnh `print` tại ❶ lẽ ra phải được thụt lề, nhưng vì Python tìm thấy ít nhất một dòng được thụt lề sau câu lệnh `for`, nó không báo lỗi. Kết quả là câu lệnh `print` đầu tiên được thực thi một lần cho mỗi tên trong list vì nó được thụt lề. Câu lệnh `print` thứ hai không được thụt lề, nên nó chỉ được thực thi một lần sau khi vòng lặp đã chạy xong. Vì giá trị cuối cùng của `magician` là `'carolina'`, cô ấy là người duy nhất nhận được thông điệp “mong được xem màn ảo thuật tiếp theo”:

[[69]]
Đây là một *lỗi logic* (logical error). Cú pháp là mã Python hợp lệ, nhưng đoạn mã không cho ra kết quả mong muốn vì có vấn đề trong logic của nó. Nếu bạn mong đợi một hành động nào đó được lặp lại một lần cho mỗi phần tử trong list nhưng nó chỉ được thực thi một lần, hãy xác định xem bạn có chỉ cần thụt lề một dòng hay một nhóm dòng hay không.

[[71]]
### Thụt lề không cần thiết

[[72]]
Nếu bạn vô tình thụt lề một dòng không cần thụt lề, Python sẽ báo cho bạn về việc thụt lề bất ngờ:

[[75]]
Chúng ta không cần thụt lề câu lệnh `print` tại ❶, vì nó không *thuộc về* dòng phía trên; do đó, Python báo lỗi:

[[77]]
Bạn có thể tránh lỗi thụt lề bất ngờ bằng cách chỉ thụt lề khi có lý do cụ thể. Trong những chương trình bạn đang viết ở giai đoạn này, những dòng duy nhất cần thụt lề là các hành động bạn muốn lặp lại cho từng phần tử trong vòng lặp `for`.

[[78]]
### Thụt lề không cần thiết sau vòng lặp

[[79]]
Nếu bạn vô tình thụt lề đoạn mã lẽ ra phải chạy sau khi vòng lặp kết thúc, đoạn mã đó sẽ bị lặp lại một lần cho mỗi phần tử trong list. Đôi khi điều này khiến Python báo lỗi, nhưng thường thì bạn chỉ gặp một lỗi logic đơn giản.

[[80]]
Ví dụ, hãy xem điều gì xảy ra khi chúng ta vô tình thụt lề dòng cảm ơn cả nhóm ảo thuật gia vì đã mang đến một buổi biểu diễn hay:

[[82]]
Vì dòng tại ❶ được thụt lề, nó được in một lần cho mỗi người trong list, như bạn có thể thấy tại ❷:

[[85]]
Đây là một lỗi logic khác, tương tự lỗi trong mục “Quên thụt lề các dòng bổ sung” ở trang 58. Vì Python không biết bạn đang cố đạt được điều gì với đoạn mã của mình, nó sẽ chạy mọi đoạn mã được viết đúng cú pháp. Nếu một hành động bị lặp lại nhiều lần trong khi lẽ ra chỉ được thực thi một lần, hãy xác định xem bạn có chỉ cần bỏ thụt lề đoạn mã cho hành động đó hay không.

[[86]]
### Quên dấu hai chấm

[[87]]
Dấu hai chấm ở cuối câu lệnh `for` cho Python biết rằng dòng tiếp theo là điểm bắt đầu của một vòng lặp.

[[89]]
Nếu bạn vô tình quên dấu hai chấm, như tại ❶, bạn sẽ gặp lỗi cú pháp vì Python không biết bạn đang cố làm gì. Dù đây là một lỗi dễ sửa, nó không phải lúc nào cũng dễ tìm. Bạn sẽ ngạc nhiên về lượng thời gian mà lập trình viên bỏ ra để săn lùng những lỗi chỉ một ký tự như thế này. Những lỗi như vậy khó tìm vì chúng ta thường chỉ nhìn thấy những gì mình mong đợi.

[[91]]
**Tự mình thực hành**

[[92]]
**4-1. Pizza:** Hãy nghĩ ra ít nhất ba loại pizza bạn yêu thích. Lưu tên các loại pizza này vào một list, rồi dùng vòng lặp `for` để in ra tên từng loại pizza.

[[93]]
- Sửa vòng lặp `for` để in ra một câu có dùng tên loại pizza thay vì chỉ in tên loại pizza. Với mỗi loại pizza, bạn nên có một dòng đầu ra chứa một câu đơn giản như *I like pepperoni pizza*.

[[94]]
- Thêm một dòng vào cuối chương trình, bên ngoài vòng lặp `for`, nói rằng bạn thích pizza đến mức nào. Đầu ra nên gồm ba dòng trở lên về các loại pizza bạn thích, rồi thêm một câu nữa, chẳng hạn *I really love pizza!*

[[95]]
**4-2. Động vật:** Hãy nghĩ ra ít nhất ba loài động vật khác nhau có chung một đặc điểm. Lưu tên các loài này vào một list, rồi dùng vòng lặp `for` để in ra tên từng loài.

[[96]]
- Sửa chương trình để in ra một câu về từng loài, chẳng hạn *A dog would make a great pet.*

[[97]]
- Thêm một dòng vào cuối chương trình nêu điểm chung của các loài này. Bạn có thể in ra một câu như *Any of these animals would make a great pet!*

[[100]]
## Tạo list số

[[101]]
Có nhiều lý do để lưu trữ một tập hợp số. Ví dụ, bạn sẽ cần theo dõi vị trí của từng nhân vật trong trò chơi, và có thể bạn cũng muốn theo dõi các điểm cao của người chơi. Trong trực quan hóa dữ liệu, hầu như lúc nào bạn cũng làm việc với các tập hợp số, chẳng hạn nhiệt độ, khoảng cách, dân số, hay các giá trị vĩ độ và kinh độ, cùng nhiều loại tập số khác.

[[102]]
List rất lý tưởng để lưu trữ các tập hợp số, và Python cung cấp một số công cụ giúp bạn làm việc hiệu quả với list số. Một khi đã hiểu cách dùng hiệu quả các công cụ này, mã của bạn sẽ chạy tốt ngay cả khi list chứa hàng triệu phần tử.

[[103]]
### Sử dụng hàm range()

[[104]]
Hàm `range()` của Python giúp bạn dễ dàng tạo ra một dãy số. Ví dụ, bạn có thể dùng hàm `range()` để in ra một dãy số như sau:

[[107]]
Dù đoạn mã này trông như sẽ in ra các số từ 1 đến 5, nó lại không in ra số 5:

[[109]]
Trong ví dụ này, `range()` chỉ in ra các số từ 1 đến 4. Đây là một kết quả khác của hành vi lệch một đơn vị mà bạn sẽ thường gặp trong các ngôn ngữ lập trình. Hàm `range()` khiến Python bắt đầu đếm từ giá trị đầu tiên bạn đưa vào, và dừng lại khi đạt tới giá trị thứ hai bạn cung cấp. Vì dừng tại giá trị thứ hai đó, đầu ra không bao giờ chứa giá trị kết thúc, mà trong trường hợp này là 5.

[[110]]
Để in ra các số từ 1 đến 5, bạn sẽ dùng `range(1,6)`:

[[112]]
Lần này đầu ra bắt đầu từ 1 và kết thúc ở 5:

[[115]]
Nếu đầu ra khác với mong đợi khi bạn dùng `range()`, hãy thử điều chỉnh giá trị kết thúc đi 1 đơn vị.

[[116]]
### Dùng range() để tạo list số

[[117]]
Nếu muốn tạo một list số, bạn có thể chuyển trực tiếp kết quả của `range()` thành list bằng hàm `list()`. Khi bọc `list()` quanh một lời gọi hàm `range()`, đầu ra sẽ là một list số.

[[118]]
Trong ví dụ ở mục trước, chúng ta chỉ đơn giản in ra một dãy số. Chúng ta có thể dùng `list()` để chuyển chính tập số đó thành một list:

[[120]]
Và đây là kết quả:

[[122]]
Chúng ta cũng có thể dùng hàm `range()` để yêu cầu Python bỏ qua một số số trong một khoảng cho trước. Ví dụ, đây là cách liệt kê các số chẵn từ 1 đến 10:

[[125]]
Trong ví dụ này, hàm `range()` bắt đầu với giá trị 2 rồi cộng thêm 2 vào giá trị đó. Nó cộng 2 liên tục cho đến khi đạt tới hoặc vượt qua giá trị kết thúc, 11, và cho ra kết quả sau:

[[127]]
Bạn có thể tạo hầu như bất kỳ tập số nào mình muốn bằng hàm `range()`. Ví dụ, hãy xem cách bạn có thể tạo một list gồm 10 số chính phương đầu tiên (tức là bình phương của từng số nguyên từ 1 đến 10). Trong Python, hai dấu sao (`**`) biểu diễn phép lũy thừa. Đây là cách bạn có thể đưa 10 số chính phương đầu tiên vào một list:

[[130]]
Chúng ta bắt đầu với một list rỗng có tên `squares` tại ❶. Tại ❷, chúng ta yêu cầu Python lặp qua từng giá trị từ 1 đến 10 bằng hàm `range()`. Bên trong vòng lặp, giá trị hiện tại được nâng lên lũy thừa bậc hai và lưu vào biến `square` tại ❸. Tại ❹, mỗi giá trị mới của `square` được nối vào list `squares`. Cuối cùng, khi vòng lặp chạy xong, list các số chính phương được in ra tại ❺:

[[133]]
Để viết đoạn mã này ngắn gọn hơn, hãy bỏ biến tạm `square` và nối trực tiếp từng giá trị mới vào list:

[[135]]
Đoạn mã tại ❶ làm cùng công việc với các dòng tại ❸ và ❹ trong *squares.py*. Mỗi giá trị trong vòng lặp được nâng lên lũy thừa bậc hai rồi ngay lập tức được nối vào list các số chính phương.

[[136]]
Bạn có thể dùng cách nào trong hai cách này khi tạo những list phức tạp hơn. Đôi khi dùng biến tạm giúp mã dễ đọc hơn; những lúc khác nó lại khiến mã dài một cách không cần thiết. Trước hết, hãy tập trung viết mã mà bạn hiểu rõ ràng và làm đúng những gì bạn muốn. Sau đó, hãy tìm những cách hiệu quả hơn khi xem lại mã của mình.

[[137]]
### Thống kê đơn giản với list số

[[138]]
Có một vài hàm Python dành riêng cho list số. Ví dụ, bạn có thể dễ dàng tìm giá trị nhỏ nhất, lớn nhất và tổng của một list số:

[[140]]
> **Lưu ý** Các ví dụ trong mục này dùng những list số ngắn để vừa vặn trên trang sách. Chúng vẫn sẽ hoạt động tốt như vậy nếu list của bạn chứa một triệu số hoặc nhiều hơn.

[[141]]
### List comprehension

[[142]]
Cách tạo list `squares` được mô tả ở trên cần dùng ba hoặc bốn dòng mã. *List comprehension* cho phép bạn tạo ra chính list này chỉ với một dòng mã. List comprehension kết hợp vòng lặp `for` và việc tạo các phần tử mới vào một dòng, đồng thời tự động nối từng phần tử mới vào list. List comprehension không phải lúc nào cũng được giới thiệu cho người mới bắt đầu, nhưng tôi vẫn đưa vào đây vì nhiều khả năng bạn sẽ gặp chúng ngay khi bắt đầu đọc mã của người khác.

[[144]]
Ví dụ sau tạo ra cùng list các số chính phương mà bạn đã thấy trước đó, nhưng dùng list comprehension:

[[147]]
Để dùng cú pháp này, hãy bắt đầu bằng một tên mang tính mô tả cho list, chẳng hạn `squares`. Tiếp theo, mở một cặp dấu ngoặc vuông và định nghĩa biểu thức cho các giá trị bạn muốn lưu vào list mới. Trong ví dụ này, biểu thức là `value**2`, nâng giá trị lên lũy thừa bậc hai. Sau đó, viết một vòng lặp `for` để tạo ra các số bạn muốn đưa vào biểu thức, rồi đóng cặp dấu ngoặc vuông. Vòng lặp `for` trong ví dụ này là `for value in range(1,11)`, đưa các giá trị từ 1 đến 10 vào biểu thức `value**2`. Hãy để ý rằng không có dấu hai chấm ở cuối câu lệnh `for`.

[[148]]
Kết quả là cùng list các số chính phương mà bạn đã thấy trước đó:

[[150]]
Cần luyện tập để tự viết list comprehension, nhưng bạn sẽ thấy chúng rất đáng giá một khi đã thành thạo việc tạo các list thông thường. Khi bạn phải viết ba hoặc bốn dòng mã để tạo list và bắt đầu thấy lặp đi lặp lại, hãy cân nhắc tự viết list comprehension.

[[152]]
**Tự mình thực hành**

[[153]]
**4-3. Đếm đến hai mươi:** Dùng vòng lặp `for` để in ra các số từ 1 đến 20, bao gồm cả hai số này.

[[154]]
**4-4. Một triệu:** Tạo một list các số từ một đến một triệu, rồi dùng vòng lặp `for` để in các số đó ra. (Nếu việc in ra mất quá nhiều thời gian, hãy dừng lại bằng cách nhấn CTRL-C hoặc đóng cửa sổ đầu ra.)

[[155]]
**4-5. Tính tổng một triệu số:** Tạo một list các số từ một đến một triệu, rồi dùng `min()` và `max()` để đảm bảo list của bạn thực sự bắt đầu từ một và kết thúc ở một triệu. Ngoài ra, hãy dùng hàm `sum()` để xem Python có thể cộng một triệu số nhanh đến mức nào.

[[156]]
**4-6. Số lẻ:** Dùng đối số thứ ba của hàm `range()` để tạo một list các số lẻ từ 1 đến 20. Dùng vòng lặp `for` để in ra từng số.

[[157]]
**4-7. Bội số của ba:** Tạo một list các bội số của 3 từ 3 đến 30. Dùng vòng lặp `for` để in ra các số trong list.

[[158]]
**4-8. Lập phương:** Một số được nâng lên lũy thừa bậc ba được gọi là *lập phương* (cube). Ví dụ, lập phương của 2 được viết là `2**3` trong Python. Tạo một list gồm 10 số lập phương đầu tiên (tức là lập phương của từng số nguyên từ 1 đến 10), và dùng vòng lặp `for` để in ra giá trị của từng số lập phương.

[[159]]
**4-9. Comprehension cho lập phương:** Dùng list comprehension để tạo một list gồm 10 số lập phương đầu tiên.

[[162]]
## Làm việc với một phần của list

[[163]]
Trong Chương 3, bạn đã học cách truy cập từng phần tử đơn lẻ trong list, và trong chương này, bạn đã học cách duyệt qua tất cả các phần tử trong list. Bạn cũng có thể làm việc với một nhóm phần tử cụ thể trong list, mà Python gọi là *lát cắt* (slice).

[[164]]
### Cắt lát list

[[165]]
Để tạo một lát cắt, bạn chỉ định chỉ mục của phần tử đầu tiên và phần tử cuối cùng mà bạn muốn làm việc. Giống như với hàm `range()`, Python dừng lại ở phần tử ngay trước chỉ mục thứ hai mà bạn chỉ định. Để xuất ra ba phần tử đầu tiên trong list, bạn sẽ yêu cầu các chỉ mục từ `0` đến `3`, và kết quả trả về là các phần tử `0`, `1` và `2`.

[[166]]
Ví dụ sau dùng một list các cầu thủ trong một đội:

[[169]]
Đoạn mã tại ❶ in ra một lát cắt của list này, chỉ gồm ba cầu thủ đầu tiên. Đầu ra giữ nguyên cấu trúc của list và gồm ba cầu thủ đầu tiên trong list:

[[171]]
Bạn có thể tạo ra bất kỳ tập con nào của list. Ví dụ, nếu muốn lấy phần tử thứ hai, thứ ba và thứ tư trong list, bạn sẽ bắt đầu lát cắt tại chỉ mục `1` và kết thúc tại chỉ mục `4`:

[[173]]
Lần này lát cắt bắt đầu bằng `'martina'` và kết thúc bằng `'florence'`:

[[175]]
Nếu bạn bỏ qua chỉ mục đầu tiên trong lát cắt, Python sẽ tự động bắt đầu lát cắt từ đầu list:

[[177]]
Khi không có chỉ mục bắt đầu, Python bắt đầu từ đầu list:

[[180]]
Một cú pháp tương tự cũng áp dụng được nếu bạn muốn một lát cắt bao gồm phần cuối của list. Ví dụ, nếu muốn lấy tất cả các phần tử từ phần tử thứ ba đến phần tử cuối cùng, bạn có thể bắt đầu với chỉ mục `2` và bỏ qua chỉ mục thứ hai:

[[182]]
Python trả về tất cả các phần tử từ phần tử thứ ba đến cuối list:

[[184]]
Cú pháp này cho phép bạn xuất ra tất cả các phần tử từ bất kỳ vị trí nào trong list đến cuối list, bất kể độ dài của list. Hãy nhớ lại rằng một chỉ mục âm trả về phần tử cách cuối list một khoảng nhất định; do đó, bạn có thể xuất ra bất kỳ lát cắt nào tính từ cuối list. Ví dụ, nếu muốn xuất ra ba cầu thủ cuối cùng trong danh sách đội, ta có thể dùng lát cắt `players[-3:]`:

[[186]]
Đoạn mã này in ra tên của ba cầu thủ cuối cùng và vẫn tiếp tục hoạt động khi kích thước của list cầu thủ thay đổi.

[[187]]
### Lặp qua một lát cắt

[[188]]
Bạn có thể dùng một lát cắt trong vòng lặp `for` nếu muốn lặp qua một tập con các phần tử trong list. Trong ví dụ tiếp theo, chúng ta lặp qua ba cầu thủ đầu tiên và in tên của họ như một phần của danh sách đội đơn giản:

[[190]]
Thay vì lặp qua toàn bộ list cầu thủ tại ❶, Python chỉ lặp qua ba cái tên đầu tiên:

[[192]]
Lát cắt rất hữu ích trong nhiều tình huống. Chẳng hạn, khi tạo một trò chơi, bạn có thể thêm điểm số cuối cùng của người chơi vào một list mỗi khi người đó chơi xong. Sau đó, bạn có thể lấy ba điểm số cao nhất của người chơi bằng cách sắp xếp list theo thứ tự giảm dần và lấy một lát cắt chỉ gồm ba điểm số đầu tiên. Khi làm việc với dữ liệu, bạn có thể dùng lát cắt để xử lý dữ liệu theo từng khối có kích thước cụ thể. Hoặc khi xây dựng một ứng dụng web, bạn có thể dùng lát cắt để hiển thị thông tin trên một loạt trang, mỗi trang có một lượng thông tin phù hợp.

[[194]]
### Sao chép list

[[195]]
Bạn sẽ thường muốn bắt đầu từ một list có sẵn và tạo ra một list hoàn toàn mới dựa trên list đầu tiên. Hãy cùng khám phá cách sao chép list và xem xét một tình huống mà việc sao chép list tỏ ra hữu ích.

[[196]]
Để sao chép một list, bạn có thể tạo một lát cắt bao gồm toàn bộ list ban đầu bằng cách bỏ qua cả chỉ mục đầu tiên lẫn chỉ mục thứ hai (`[:]`). Cách này yêu cầu Python tạo một lát cắt bắt đầu từ phần tử đầu tiên và kết thúc ở phần tử cuối cùng, tạo ra một bản sao của toàn bộ list.

[[197]]
Ví dụ, hãy tưởng tượng chúng ta có một list các món ăn yêu thích và muốn tạo một list riêng gồm các món mà một người bạn thích. Người bạn này thích mọi món trong list của chúng ta tính đến giờ, nên ta có thể tạo list của họ bằng cách sao chép list của mình:

[[200]]
Tại ❶, chúng ta tạo một list các món ăn mình thích có tên `my_foods`. Tại ❷, chúng ta tạo một list mới có tên `friend_foods`. Chúng ta tạo một bản sao của `my_foods` bằng cách yêu cầu một lát cắt của `my_foods` mà không chỉ định chỉ mục nào, rồi lưu bản sao đó vào `friend_foods`. Khi in từng list ra, ta thấy cả hai đều chứa cùng các món ăn:

[[202]]
Để chứng minh rằng chúng ta thực sự có hai list riêng biệt, ta sẽ thêm một món ăn mới vào mỗi list và cho thấy mỗi list theo dõi đúng các món ăn yêu thích của người tương ứng:

[[205]]
Tại ❶, chúng ta sao chép các phần tử ban đầu trong `my_foods` sang list mới `friend_foods`, như đã làm trong ví dụ trước. Tiếp theo, chúng ta thêm một món ăn mới vào mỗi list: tại ❷, ta thêm `'cannoli'` vào `my_foods`, và tại ❸, ta thêm `'ice cream'` vào `friend_foods`. Sau đó, chúng ta in hai list ra để xem mỗi món ăn này có nằm đúng list hay không.

[[207]]
Đầu ra tại ❹ cho thấy `'cannoli'` giờ đã xuất hiện trong list món ăn yêu thích của chúng ta, còn `'ice cream'` thì không. Tại ❺, ta có thể thấy `'ice cream'` giờ đã xuất hiện trong list của người bạn, còn `'cannoli'` thì không. Nếu chúng ta chỉ đơn giản gán `friend_foods` bằng `my_foods`, ta sẽ không tạo ra được hai list riêng biệt. Ví dụ, đây là điều xảy ra khi bạn cố sao chép một list mà không dùng lát cắt:

[[209]]
Thay vì lưu một bản sao của `my_foods` vào `friend_foods` tại ❶, chúng ta gán `friend_foods` bằng `my_foods`. Cú pháp này thực chất yêu cầu Python liên kết biến mới `friend_foods` với list đã được chứa trong `my_foods`, nên giờ cả hai biến đều trỏ tới cùng một list. Kết quả là khi chúng ta thêm `'cannoli'` vào `my_foods`, nó cũng sẽ xuất hiện trong `friend_foods`. Tương tự, `'ice cream'` sẽ xuất hiện trong cả hai list, dù trông như nó chỉ được thêm vào `friend_foods`.

[[210]]
Đầu ra cho thấy cả hai list giờ giống hệt nhau, và đó không phải điều chúng ta muốn:

[[213]]
> **Lưu ý** Tạm thời đừng bận tâm về các chi tiết trong ví dụ này. Về cơ bản, nếu bạn đang cố làm việc với một bản sao của list và thấy hành vi bất ngờ, hãy đảm bảo rằng bạn đang sao chép list bằng lát cắt, như chúng ta đã làm trong ví dụ đầu tiên.

[[215]]
**Tự mình thực hành**

[[216]]
**4-10. Lát cắt:** Dùng một trong các chương trình bạn đã viết trong chương này, thêm vài dòng vào cuối chương trình để làm những việc sau:

[[217]]
- In ra thông điệp *The first three items in the list are:*. Sau đó dùng một lát cắt để in ra ba phần tử đầu tiên trong list của chương trình đó.

[[218]]
- In ra thông điệp *Three items from the middle of the list are:*. Dùng một lát cắt để in ra ba phần tử ở giữa list.

[[219]]
- In ra thông điệp *The last three items in the list are:*. Dùng một lát cắt để in ra ba phần tử cuối cùng trong list.

[[220]]
**4-11. Pizza của tôi, pizza của bạn:** Bắt đầu với chương trình của bạn từ Bài tập 4-1 (trang 60). Tạo một bản sao của list pizza và đặt tên là `friend_pizzas`. Sau đó làm những việc sau:

[[221]]
- Thêm một loại pizza mới vào list ban đầu.

[[222]]
- Thêm một loại pizza khác vào list `friend_pizzas`.

[[223]]
- Chứng minh rằng bạn có hai list riêng biệt. In ra thông điệp *My favorite pizzas are:*, rồi dùng vòng lặp `for` để in list thứ nhất. In ra thông điệp *My friend’s favorite pizzas are:*, rồi dùng vòng lặp `for` để in list thứ hai. Hãy đảm bảo mỗi loại pizza mới được lưu đúng list.

[[224]]
**4-12. Thêm vòng lặp:** Để tiết kiệm chỗ, mọi phiên bản của *foods.py* trong mục này đều không dùng vòng lặp `for` khi in. Hãy chọn một phiên bản của *foods.py* và viết hai vòng lặp `for` để in ra từng list món ăn.

[[226]]
## Tuple

[[227]]
List rất phù hợp để lưu trữ các tập hợp phần tử có thể thay đổi trong suốt vòng đời của chương trình. Khả năng sửa đổi list đặc biệt quan trọng khi bạn làm việc với một list người dùng trên trang web hoặc một list nhân vật trong trò chơi. Tuy nhiên, đôi khi bạn sẽ muốn tạo một list các phần tử không thể thay đổi. Tuple cho phép bạn làm đúng điều đó. Python gọi những giá trị không thể thay đổi là *bất biến* (immutable), và một list bất biến được gọi là *tuple*.

[[228]]
### Định nghĩa tuple

[[229]]
Tuple trông giống hệt list, chỉ khác là bạn dùng dấu ngoặc đơn thay vì dấu ngoặc vuông. Sau khi định nghĩa một tuple, bạn có thể truy cập từng phần tử bằng chỉ mục của nó, giống như với list.

[[231]]
Ví dụ, nếu có một hình chữ nhật luôn phải có một kích thước nhất định, ta có thể đảm bảo kích thước của nó không thay đổi bằng cách đặt các kích thước vào một tuple:

[[234]]
Chúng ta định nghĩa tuple `dimensions` tại ❶, dùng dấu ngoặc đơn thay vì dấu ngoặc vuông. Tại ❷, chúng ta in từng phần tử trong tuple, dùng cùng cú pháp mà ta vẫn dùng để truy cập phần tử trong list:

[[236]]
Hãy xem điều gì xảy ra nếu ta thử thay đổi một phần tử trong tuple `dimensions`:

[[238]]
Đoạn mã tại ❶ cố thay đổi giá trị của kích thước thứ nhất, nhưng Python trả về một lỗi kiểu dữ liệu. Về cơ bản, vì chúng ta đang cố thay đổi một tuple — điều không thể làm với loại đối tượng này — Python cho biết ta không thể gán giá trị mới cho một phần tử trong tuple:

[[240]]
Điều này có lợi, vì chúng ta muốn Python báo lỗi khi có một dòng mã cố thay đổi kích thước của hình chữ nhật.

[[241]]
### Lặp qua tất cả các giá trị trong tuple

[[242]]
Bạn có thể lặp qua tất cả các giá trị trong một tuple bằng vòng lặp `for`, giống như đã làm với list:

[[244]]
Python trả về tất cả các phần tử trong tuple, giống như với list:

[[247]]
### Ghi đè một tuple

[[248]]
Dù không thể sửa đổi một tuple, bạn có thể gán một giá trị mới cho biến đang giữ tuple đó. Vì vậy, nếu muốn thay đổi kích thước, ta có thể định nghĩa lại toàn bộ tuple:

[[250]]
Khối mã tại ❶ định nghĩa tuple ban đầu và in ra các kích thước ban đầu. Tại ❷, chúng ta lưu một tuple mới vào biến `dimensions`. Sau đó, ta in ra các kích thước mới tại ❸. Lần này Python không báo lỗi nào, vì ghi đè một biến là thao tác hợp lệ:

[[252]]
So với list, tuple là những cấu trúc dữ liệu đơn giản. Hãy dùng chúng khi bạn muốn lưu trữ một tập giá trị không được phép thay đổi trong suốt vòng đời của chương trình.

[[254]]
**Tự mình thực hành**

[[255]]
**4-13. Buffet:** Một nhà hàng buffet chỉ phục vụ năm món ăn cơ bản. Hãy nghĩ ra năm món ăn đơn giản và lưu chúng vào một tuple.

[[256]]
- Dùng vòng lặp `for` để in ra từng món mà nhà hàng phục vụ.

[[257]]
- Thử sửa đổi một trong các phần tử và đảm bảo rằng Python từ chối thay đổi đó.

[[258]]
- Nhà hàng thay đổi thực đơn, thay hai món bằng những món khác. Thêm một khối mã ghi đè tuple, rồi dùng vòng lặp `for` để in ra từng món trong thực đơn đã được sửa đổi.

[[261]]
## Định dạng phong cách mã

[[262]]
Giờ đây khi bạn đã viết những chương trình dài hơn, việc biết cách định dạng phong cách mã là điều đáng giá. Hãy dành thời gian để làm cho mã của bạn dễ đọc nhất có thể. Viết mã dễ đọc giúp bạn theo dõi được chương trình của mình đang làm gì, đồng thời giúp người khác hiểu mã của bạn.

[[263]]
Các lập trình viên Python đã thống nhất một số quy ước về phong cách để đảm bảo mã của mọi người có cấu trúc gần như giống nhau. Một khi đã học cách viết mã Python sạch, bạn sẽ có thể hiểu được cấu trúc tổng thể của mã Python do bất kỳ ai khác viết, miễn là họ tuân theo cùng các hướng dẫn. Nếu bạn mong một lúc nào đó trở thành lập trình viên chuyên nghiệp, bạn nên bắt đầu tuân theo các hướng dẫn này càng sớm càng tốt để hình thành thói quen tốt.

[[264]]
### Hướng dẫn phong cách

[[265]]
Khi ai đó muốn thay đổi ngôn ngữ Python, họ sẽ viết một *Python Enhancement Proposal (PEP)* — đề xuất cải tiến Python. Một trong những PEP lâu đời nhất là *PEP 8*, hướng dẫn các lập trình viên Python cách định dạng phong cách mã. PEP 8 khá dài, nhưng phần lớn nội dung liên quan đến những cấu trúc mã phức tạp hơn những gì bạn đã thấy cho đến giờ.

[[266]]
Hướng dẫn phong cách của Python được viết dựa trên nhận thức rằng mã được đọc thường xuyên hơn là được viết. Bạn sẽ viết mã một lần, rồi bắt đầu đọc lại nó khi tiến hành gỡ lỗi. Khi thêm tính năng cho chương trình, bạn sẽ dành nhiều thời gian hơn để đọc mã. Khi chia sẻ mã với các lập trình viên khác, họ cũng sẽ đọc mã của bạn.

[[267]]
Giữa việc viết mã dễ viết hơn và mã dễ đọc hơn, các lập trình viên Python hầu như luôn khuyến khích bạn viết mã dễ đọc hơn. Các hướng dẫn sau sẽ giúp bạn viết mã rõ ràng ngay từ đầu.

[[268]]
### Thụt lề

[[269]]
PEP 8 khuyến nghị dùng bốn dấu cách cho mỗi cấp thụt lề. Dùng bốn dấu cách giúp mã dễ đọc hơn mà vẫn chừa chỗ cho nhiều cấp thụt lề trên mỗi dòng.

[[270]]
Trong tài liệu soạn thảo văn bản, người ta thường dùng tab thay vì dấu cách để thụt lề. Cách này phù hợp với tài liệu văn bản, nhưng trình thông dịch Python sẽ bị nhầm lẫn khi tab bị trộn lẫn với dấu cách. Mọi trình soạn thảo văn bản đều có một thiết lập cho phép bạn dùng phím TAB nhưng sau đó chuyển mỗi tab thành một số dấu cách nhất định. Bạn chắc chắn nên dùng phím TAB, nhưng cũng cần đảm bảo trình soạn thảo được thiết lập để chèn dấu cách thay vì tab vào tài liệu.

[[271]]
Trộn lẫn tab và dấu cách trong file có thể gây ra những vấn đề rất khó chẩn đoán. Nếu nghĩ rằng file của mình đang trộn lẫn tab và dấu cách, bạn có thể chuyển tất cả các tab trong file thành dấu cách ở hầu hết các trình soạn thảo.

[[273]]
### Độ dài dòng

[[274]]
Nhiều lập trình viên Python khuyến nghị mỗi dòng nên ngắn hơn 80 ký tự. Về mặt lịch sử, hướng dẫn này ra đời vì hầu hết máy tính chỉ chứa được 79 ký tự trên một dòng trong cửa sổ terminal. Hiện nay, người ta có thể hiển thị những dòng dài hơn nhiều trên màn hình, nhưng vẫn có những lý do khác để tuân theo độ dài dòng chuẩn 79 ký tự. Lập trình viên chuyên nghiệp thường mở nhiều file trên cùng một màn hình, và việc dùng độ dài dòng chuẩn giúp họ nhìn thấy trọn vẹn các dòng trong hai hoặc ba file mở cạnh nhau trên màn hình. PEP 8 cũng khuyến nghị giới hạn mọi chú thích ở 72 ký tự mỗi dòng, vì một số công cụ tự động tạo tài liệu cho các dự án lớn sẽ thêm ký tự định dạng vào đầu mỗi dòng chú thích.

[[275]]
Các hướng dẫn về độ dài dòng của PEP 8 không phải là bất di bất dịch, và một số nhóm ưa dùng giới hạn 99 ký tự. Đừng quá lo lắng về độ dài dòng trong mã khi bạn đang học, nhưng hãy biết rằng những người làm việc theo nhóm hầu như luôn tuân theo các hướng dẫn của PEP 8. Hầu hết các trình soạn thảo cho phép bạn thiết lập một dấu hiệu trực quan, thường là một đường thẳng đứng trên màn hình, cho bạn thấy các giới hạn này nằm ở đâu.

[[276]]
> **Lưu ý** Phụ lục B hướng dẫn bạn cách cấu hình trình soạn thảo văn bản để nó luôn chèn bốn dấu cách mỗi khi bạn nhấn phím tab, và hiển thị một đường gióng thẳng đứng để giúp bạn tuân theo giới hạn 79 ký tự.

[[277]]
### Dòng trống

[[278]]
Để nhóm các phần của chương trình một cách trực quan, hãy dùng dòng trống. Bạn nên dùng dòng trống để sắp xếp file, nhưng đừng lạm dụng. Nếu làm theo các ví dụ trong cuốn sách này, bạn sẽ đạt được sự cân bằng hợp lý. Ví dụ, nếu bạn có năm dòng mã xây dựng một list, rồi ba dòng khác làm gì đó với list đó, thì đặt một dòng trống giữa hai phần là hợp lý. Tuy nhiên, bạn không nên đặt ba hoặc bốn dòng trống giữa hai phần.

[[279]]
Dòng trống không ảnh hưởng đến cách mã chạy, nhưng chúng ảnh hưởng đến khả năng đọc hiểu mã. Trình thông dịch Python dùng thụt lề theo chiều ngang để hiểu ý nghĩa của mã, nhưng bỏ qua khoảng cách theo chiều dọc.

[[280]]
### Các hướng dẫn phong cách khác

[[281]]
PEP 8 còn nhiều khuyến nghị khác về phong cách, nhưng phần lớn hướng dẫn đề cập đến những chương trình phức tạp hơn những gì bạn đang viết ở giai đoạn này. Khi bạn học những cấu trúc Python phức tạp hơn, tôi sẽ chia sẻ những phần liên quan của các hướng dẫn trong PEP 8.

[[284]]
**Tự mình thực hành**

[[285]]
**4-14. PEP 8:** Hãy đọc qua bản hướng dẫn phong cách PEP 8 gốc tại *https://python.org/dev/peps/pep-0008/*. Lúc này bạn sẽ chưa dùng đến nhiều nội dung trong đó, nhưng đọc lướt qua có thể sẽ thú vị.

[[286]]
**4-15. Xem xét lại mã:** Chọn ba chương trình bạn đã viết trong chương này và sửa từng chương trình để tuân thủ PEP 8:

[[287]]
- Dùng bốn dấu cách cho mỗi cấp thụt lề. Thiết lập trình soạn thảo văn bản để chèn bốn dấu cách mỗi khi bạn nhấn TAB, nếu bạn chưa làm (xem Phụ lục B để biết cách làm).

[[288]]
- Dùng ít hơn 80 ký tự trên mỗi dòng, và thiết lập trình soạn thảo để hiển thị một đường gióng thẳng đứng tại vị trí ký tự thứ 80.

[[289]]
- Đừng lạm dụng dòng trống trong các file chương trình của bạn.

[[291]]
## Tổng kết

[[292]]
Trong chương này, bạn đã học cách làm việc hiệu quả với các phần tử trong list. Bạn đã học cách duyệt qua một list bằng vòng lặp `for`, cách Python dùng thụt lề để tổ chức cấu trúc chương trình, và cách tránh một số lỗi thụt lề phổ biến. Bạn đã học cách tạo những list số đơn giản, cũng như một vài thao tác có thể thực hiện trên list số. Bạn đã học cách cắt lát một list để làm việc với một tập con các phần tử, và cách sao chép list đúng cách bằng lát cắt. Bạn cũng đã tìm hiểu về tuple — cấu trúc giúp bảo vệ ở một mức độ nhất định cho một tập giá trị không nên thay đổi — và cách định dạng phong cách cho mã ngày càng phức tạp của mình để nó dễ đọc.

[[293]]
Trong Chương 5, bạn sẽ học cách phản hồi phù hợp với các điều kiện khác nhau bằng câu lệnh `if`. Bạn sẽ học cách kết hợp những tập hợp phép kiểm tra điều kiện tương đối phức tạp để phản hồi đúng với chính xác loại tình huống hoặc thông tin bạn đang tìm kiếm. Bạn cũng sẽ học cách dùng câu lệnh `if` trong khi lặp qua một list để thực hiện những hành động cụ thể với các phần tử được chọn trong list.

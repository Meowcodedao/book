[[2]]
# Chương 6: Dictionary

[[4]]
Trong chương này, bạn sẽ học cách dùng dictionary của Python, cấu trúc cho phép bạn kết nối những mẩu thông tin có liên quan với nhau. Bạn sẽ học cách truy cập thông tin khi nó đã nằm trong dictionary và cách sửa đổi thông tin đó. Vì dictionary có thể lưu trữ một lượng thông tin gần như không giới

[[5]]
hạn, tôi sẽ hướng dẫn bạn cách lặp qua dữ liệu trong một dictionary. Ngoài ra, bạn sẽ học cách lồng dictionary bên trong list, lồng list bên trong dictionary, và thậm chí lồng dictionary bên trong một dictionary khác.

[[6]]
Hiểu về dictionary giúp bạn mô hình hóa chính xác hơn nhiều loại đối tượng trong thế giới thực. Bạn sẽ có thể tạo một dictionary biểu diễn một người, rồi lưu bao nhiêu thông tin tùy thích về người đó. Bạn có thể lưu tên, tuổi, nơi ở, nghề nghiệp và bất kỳ khía cạnh nào khác mà bạn có thể mô tả về một người. Bạn sẽ có thể lưu trữ bất kỳ hai loại thông tin nào có thể ghép cặp với nhau, chẳng hạn một list các từ và nghĩa của chúng, một list tên người và số yêu thích của họ, một list các ngọn núi và độ cao của chúng, v.v.

[[8]]
## Một dictionary đơn giản

[[9]]
Hãy xét một trò chơi có những người ngoài hành tinh với màu sắc và số điểm khác nhau. Dictionary đơn giản sau lưu trữ thông tin về một người ngoài hành tinh cụ thể:

[[12]]
Dictionary `alien_0` lưu màu sắc và số điểm của người ngoài hành tinh. Hai câu lệnh `print` truy cập và hiển thị thông tin đó, như sau:

[[14]]
Như với hầu hết các khái niệm lập trình mới, sử dụng dictionary cần có sự luyện tập. Khi đã làm việc với dictionary một thời gian, bạn sẽ sớm thấy chúng mô hình hóa các tình huống thực tế hiệu quả đến mức nào.

[[15]]
## Làm việc với dictionary

[[16]]
Trong Python, *dictionary* là một tập hợp các *cặp khóa–giá trị* (key-value pair). Mỗi *khóa* (key) được kết nối với một giá trị, và bạn có thể dùng khóa để truy cập giá trị gắn với khóa đó. Giá trị của một khóa có thể là số, chuỗi, list, hoặc thậm chí là một dictionary khác. Thực tế, bạn có thể dùng bất kỳ đối tượng nào tạo được trong Python làm giá trị trong dictionary.

[[17]]
Trong Python, dictionary được bao trong cặp dấu ngoặc nhọn, `{}`, với một loạt cặp khóa–giá trị bên trong, như trong ví dụ trước:

[[19]]
*Cặp khóa–giá trị* là một nhóm giá trị gắn với nhau. Khi bạn cung cấp một khóa, Python trả về giá trị gắn với khóa đó. Mỗi khóa được nối với giá trị của nó bằng dấu hai chấm, và các cặp khóa–giá trị được phân tách bằng dấu phẩy. Bạn có thể lưu bao nhiêu cặp khóa–giá trị tùy thích trong một dictionary.

[[20]]
Dictionary đơn giản nhất có đúng một cặp khóa–giá trị, như trong phiên bản đã sửa đổi này của dictionary `alien_0`:

[[22]]
Dictionary này lưu một mẩu thông tin về `alien_0`, cụ thể là màu của người ngoài hành tinh. Chuỗi `'color'` là một khóa trong dictionary này, và giá trị gắn với nó là `'green'`.

[[24]]
### Truy cập giá trị trong dictionary

[[25]]
Để lấy giá trị gắn với một khóa, hãy viết tên dictionary rồi đặt khóa bên trong một cặp dấu ngoặc vuông, như sau:

[[27]]
Đoạn mã này trả về giá trị gắn với khóa `'color'` từ dictionary `alien_0`:

[[29]]
Một dictionary có thể có số lượng cặp khóa–giá trị không giới hạn. Ví dụ, đây là dictionary `alien_0` ban đầu với hai cặp khóa–giá trị:

[[31]]
Giờ bạn có thể truy cập màu hoặc số điểm của `alien_0`. Nếu người chơi bắn hạ người ngoài hành tinh này, bạn có thể tra xem họ được bao nhiêu điểm bằng đoạn mã như sau:

[[33]]
Sau khi dictionary đã được định nghĩa, đoạn mã tại ❶ lấy giá trị gắn với khóa `'points'` từ dictionary. Giá trị này sau đó được lưu vào biến `new_points`. Dòng tại ❷ chuyển giá trị số nguyên này thành chuỗi và in ra một câu cho biết người chơi vừa được bao nhiêu điểm:

[[35]]
Nếu bạn chạy đoạn mã này mỗi khi một người ngoài hành tinh bị bắn hạ, số điểm của người ngoài hành tinh đó sẽ được lấy ra.

[[36]]
### Thêm cặp khóa–giá trị mới

[[37]]
Dictionary là cấu trúc động, và bạn có thể thêm cặp khóa–giá trị mới vào dictionary bất cứ lúc nào. Ví dụ, để thêm một cặp khóa–giá trị mới, bạn viết tên dictionary, theo sau là khóa mới trong cặp dấu ngoặc vuông cùng với giá trị mới.

[[38]]
Hãy thêm hai mẩu thông tin mới vào dictionary `alien_0`: tọa độ x và y của người ngoài hành tinh, giúp chúng ta hiển thị người ngoài hành tinh ở một vị trí cụ thể trên màn hình. Hãy đặt người ngoài hành tinh ở mép trái màn hình, cách mép trên 25 pixel. Vì tọa độ màn hình thường bắt đầu từ góc trên bên trái, chúng ta sẽ đặt người ngoài hành tinh ở mép trái màn hình bằng cách gán tọa độ x bằng 0, và cách mép trên 25 pixel bằng cách gán tọa độ y bằng dương 25, như sau:

[[41]]
Chúng ta bắt đầu bằng việc định nghĩa cùng dictionary mà ta vẫn đang làm việc. Sau đó, ta in dictionary này ra, hiển thị một ảnh chụp nhanh thông tin của nó. Tại ❶, ta thêm một cặp khóa–giá trị mới vào dictionary: khóa `'x_position'` và giá trị `0`. Ta làm tương tự với khóa `'y_position'` tại ❷. Khi in dictionary đã sửa đổi, ta thấy hai cặp khóa–giá trị được thêm vào:

[[43]]
Phiên bản cuối cùng của dictionary chứa bốn cặp khóa–giá trị. Hai cặp ban đầu chỉ định màu sắc và số điểm, còn hai cặp nữa chỉ định vị trí của người ngoài hành tinh. Hãy để ý rằng thứ tự của các cặp khóa–giá trị không khớp với thứ tự chúng ta thêm chúng vào. Python không quan tâm đến thứ tự bạn lưu từng cặp khóa–giá trị; nó chỉ quan tâm đến liên kết giữa mỗi khóa và giá trị của nó.

[[44]]
### Bắt đầu với một dictionary rỗng

[[45]]
Đôi khi sẽ thuận tiện, hoặc thậm chí cần thiết, khi bắt đầu với một dictionary rỗng rồi thêm từng phần tử mới vào. Để bắt đầu điền vào một dictionary rỗng, hãy định nghĩa một dictionary với cặp dấu ngoặc nhọn trống, rồi thêm từng cặp khóa–giá trị trên một dòng riêng. Ví dụ, đây là cách xây dựng dictionary `alien_0` theo cách này:

[[47]]
Ở đây, chúng ta định nghĩa một dictionary `alien_0` rỗng, rồi thêm giá trị màu sắc và số điểm vào. Kết quả là dictionary mà ta đã dùng trong các ví dụ trước:

[[49]]
Thông thường, bạn sẽ dùng dictionary rỗng khi lưu dữ liệu do người dùng cung cấp vào dictionary, hoặc khi viết mã tự động tạo ra một số lượng lớn cặp khóa–giá trị.

[[51]]
### Sửa đổi giá trị trong dictionary

[[52]]
Để sửa đổi một giá trị trong dictionary, hãy viết tên dictionary kèm khóa trong cặp dấu ngoặc vuông, rồi đến giá trị mới mà bạn muốn gắn với khóa đó. Ví dụ, hãy xét một người ngoài hành tinh chuyển từ màu xanh lá sang màu vàng khi trò chơi tiến triển:

[[54]]
Đầu tiên, chúng ta định nghĩa một dictionary cho `alien_0` chỉ chứa màu của người ngoài hành tinh; sau đó, ta thay đổi giá trị gắn với khóa `'color'` thành `'yellow'`. Đầu ra cho thấy người ngoài hành tinh quả thực đã chuyển từ xanh lá sang vàng:

[[56]]
Để có một ví dụ thú vị hơn, hãy theo dõi vị trí của một người ngoài hành tinh có thể di chuyển với các tốc độ khác nhau. Chúng ta sẽ lưu một giá trị biểu thị tốc độ hiện tại của người ngoài hành tinh, rồi dùng nó để xác định người ngoài hành tinh nên di chuyển sang phải bao xa:

[[58]]
Chúng ta bắt đầu bằng việc định nghĩa một người ngoài hành tinh với vị trí *x* và vị trí *y* ban đầu, và tốc độ `'medium'`. Để đơn giản, chúng ta đã bỏ qua màu sắc và số điểm, nhưng ví dụ này vẫn hoạt động y như vậy nếu bạn đưa cả các cặp khóa–giá trị đó vào. Chúng ta cũng in ra giá trị ban đầu của `x_position` để xem người ngoài hành tinh di chuyển sang phải bao xa.

[[59]]
Tại ❶, một chuỗi `if`-`elif`-`else` xác định người ngoài hành tinh nên di chuyển sang phải bao xa và lưu giá trị này vào biến `x_increment`. Nếu tốc độ của người ngoài hành tinh là `'slow'`, nó di chuyển sang phải một đơn vị; nếu tốc độ là `'medium'`, nó di chuyển sang phải hai đơn vị; và nếu là `'fast'`, nó di chuyển sang phải ba đơn vị. Sau khi lượng tăng được tính toán, nó được cộng vào giá trị của `x_position` tại ❷, và kết quả được lưu vào `x_position` của dictionary.

[[61]]
Vì đây là một người ngoài hành tinh tốc độ trung bình, vị trí của nó dịch sang phải hai đơn vị:

[[63]]
Kỹ thuật này khá hay: chỉ bằng cách thay đổi một giá trị trong dictionary của người ngoài hành tinh, bạn có thể thay đổi toàn bộ hành vi của nó. Ví dụ, để biến người ngoài hành tinh tốc độ trung bình này thành một người ngoài hành tinh tốc độ nhanh, bạn sẽ thêm dòng:

[[65]]
Khi đó, khối `if`-`elif`-`else` sẽ gán một giá trị lớn hơn cho `x_increment` ở lần chạy mã tiếp theo.

[[66]]
### Xóa cặp khóa–giá trị

[[67]]
Khi không còn cần một mẩu thông tin được lưu trong dictionary nữa, bạn có thể dùng câu lệnh `del` để xóa hoàn toàn một cặp khóa–giá trị. Tất cả những gì `del` cần là tên dictionary và khóa mà bạn muốn xóa.

[[68]]
Ví dụ, hãy xóa khóa `'points'` cùng giá trị của nó khỏi dictionary `alien_0`:

[[70]]
Dòng tại ❶ yêu cầu Python xóa khóa `'points'` khỏi dictionary `alien_0`, đồng thời xóa luôn giá trị gắn với khóa đó. Đầu ra cho thấy khóa `'points'` và giá trị `5` của nó đã bị xóa khỏi dictionary, còn phần còn lại của dictionary không bị ảnh hưởng:

[[72]]
> **Lưu ý** Hãy nhớ rằng cặp khóa–giá trị đã xóa sẽ bị xóa vĩnh viễn.

[[73]]
### Một dictionary gồm các đối tượng tương tự nhau

[[74]]
Ví dụ trước liên quan đến việc lưu nhiều loại thông tin khác nhau về một đối tượng — một người ngoài hành tinh trong trò chơi. Bạn cũng có thể dùng dictionary để lưu một loại thông tin về nhiều đối tượng. Ví dụ, giả sử bạn muốn khảo sát một số người và hỏi họ ngôn ngữ lập trình yêu thích của họ là gì. Một dictionary rất hữu ích để lưu kết quả của một cuộc khảo sát đơn giản, như sau:

[[77]]
Như bạn thấy, chúng ta đã tách một dictionary lớn thành nhiều dòng. Mỗi khóa là tên của một người đã trả lời khảo sát, và mỗi giá trị là ngôn ngữ họ chọn. Khi biết mình sẽ cần nhiều hơn một dòng để định nghĩa một dictionary, hãy nhấn ENTER sau dấu ngoặc nhọn mở. Sau đó, thụt lề dòng tiếp theo một cấp (bốn dấu cách), và viết cặp khóa–giá trị đầu tiên, theo sau là một dấu phẩy. Từ đây trở đi, khi bạn nhấn ENTER, trình soạn thảo văn bản sẽ tự động thụt lề tất cả các cặp khóa–giá trị tiếp theo cho khớp với cặp khóa–giá trị đầu tiên.

[[78]]
Khi đã định nghĩa xong dictionary, hãy thêm dấu ngoặc nhọn đóng trên một dòng mới sau cặp khóa–giá trị cuối cùng và thụt lề nó một cấp để nó thẳng hàng với các khóa trong dictionary. Một thói quen tốt là thêm cả dấu phẩy sau cặp khóa–giá trị cuối cùng, để bạn sẵn sàng thêm một cặp khóa–giá trị mới ở dòng tiếp theo.

[[79]]
> **Lưu ý** Hầu hết các trình soạn thảo đều có tính năng giúp bạn định dạng các list và dictionary dài theo cách tương tự như ví dụ này. Cũng có những cách định dạng dictionary dài khác được chấp nhận, nên bạn có thể thấy cách định dạng hơi khác trong trình soạn thảo của mình hoặc trong các nguồn khác.

[[80]]
Để sử dụng dictionary này, khi biết tên một người đã tham gia khảo sát, bạn có thể dễ dàng tra ra ngôn ngữ yêu thích của họ:

[[83]]
Để xem Sarah đã chọn ngôn ngữ nào, chúng ta yêu cầu giá trị tại:

[[85]]
Cú pháp này được dùng trong câu lệnh `print` tại ❷, và đầu ra hiển thị ngôn ngữ yêu thích của Sarah:

[[88]]
Ví dụ này cũng cho thấy cách bạn có thể tách một câu lệnh `print` dài thành nhiều dòng. Từ `print` ngắn hơn tên của hầu hết các dictionary, nên việc đặt phần đầu tiên của nội dung muốn in ngay sau dấu ngoặc đơn mở là hợp lý ❶. Hãy chọn một điểm thích hợp để ngắt nội dung đang in, và thêm một toán tử nối chuỗi (`+`) vào cuối dòng đầu tiên ❷. Nhấn ENTER rồi nhấn TAB để căn tất cả các dòng tiếp theo thụt lề một cấp dưới câu lệnh `print`. Khi đã soạn xong đầu ra, bạn có thể đặt dấu ngoặc đơn đóng ở dòng cuối cùng của khối `print` ❸.

[[90]]
**Tự mình thực hành**

[[91]]
**6-1. Người:** Dùng một dictionary để lưu thông tin về một người mà bạn biết. Lưu tên, họ, tuổi và thành phố nơi họ sống. Bạn nên có các khóa như `first_name`, `last_name`, `age` và `city`. In ra từng mẩu thông tin được lưu trong dictionary của bạn.

[[92]]
**6-2. Số yêu thích:** Dùng một dictionary để lưu số yêu thích của mọi người. Hãy nghĩ ra năm cái tên và dùng chúng làm khóa trong dictionary. Nghĩ ra một số yêu thích cho mỗi người và lưu từng số làm giá trị trong dictionary. In ra tên của từng người và số yêu thích của họ. Để thú vị hơn nữa, hãy khảo sát vài người bạn và lấy dữ liệu thực tế cho chương trình của bạn.

[[93]]
**6-3. Bảng thuật ngữ:** Một dictionary của Python có thể được dùng để mô hình hóa một cuốn từ điển thực sự. Tuy nhiên, để tránh nhầm lẫn, hãy gọi nó là bảng thuật ngữ (glossary).

[[94]]
- Hãy nghĩ ra năm từ lập trình mà bạn đã học trong các chương trước. Dùng các từ này làm khóa trong bảng thuật ngữ, và lưu nghĩa của chúng làm giá trị.

[[95]]
- In ra từng từ và nghĩa của nó dưới dạng đầu ra được định dạng gọn gàng. Bạn có thể in từ, theo sau là dấu hai chấm rồi đến nghĩa của nó, hoặc in từ trên một dòng rồi in nghĩa của nó thụt lề trên dòng thứ hai. Dùng ký tự xuống dòng (`\n`) để chèn một dòng trống giữa mỗi cặp từ–nghĩa trong đầu ra.

[[97]]
## Lặp qua dictionary

[[98]]
Một dictionary Python có thể chỉ chứa vài cặp khóa–giá trị hoặc hàng triệu cặp. Vì dictionary có thể chứa lượng dữ liệu lớn, Python cho phép bạn lặp qua dictionary. Dictionary có thể được dùng để lưu thông tin theo nhiều cách khác nhau; do đó, cũng có nhiều cách khác nhau để lặp qua chúng. Bạn có thể lặp qua tất cả các cặp khóa–giá trị của dictionary, qua các khóa của nó, hoặc qua các giá trị của nó.

[[100]]
### Lặp qua tất cả các cặp khóa–giá trị

[[101]]
Trước khi khám phá các cách lặp khác nhau, hãy xét một dictionary mới được thiết kế để lưu thông tin về một người dùng trên trang web. Dictionary sau sẽ lưu tên người dùng, tên và họ của một người:

[[103]]
Bạn có thể truy cập bất kỳ mẩu thông tin riêng lẻ nào về `user_0` dựa trên những gì đã học trong chương này. Nhưng nếu bạn muốn xem mọi thứ được lưu trong dictionary của người dùng này thì sao? Để làm điều đó, bạn có thể lặp qua dictionary bằng vòng lặp `for`:

[[106]]
Như tại ❶, để viết vòng lặp `for` cho một dictionary, bạn đặt tên cho hai biến sẽ giữ khóa và giá trị trong mỗi cặp khóa–giá trị. Bạn có thể chọn bất kỳ tên nào bạn muốn cho hai biến này. Đoạn mã này vẫn hoạt động tốt như vậy nếu bạn dùng tên viết tắt cho các biến, như sau:

[[108]]
Nửa sau của câu lệnh `for` tại ❶ gồm tên dictionary, theo sau là phương thức `items()`, phương thức trả về một list các cặp khóa–giá trị. Sau đó, vòng lặp `for` lưu từng cặp này vào hai biến được cung cấp. Trong ví dụ trên, ta dùng các biến để in ra từng `key` ❷, theo sau là `value` tương ứng ❸. Ký tự `"\n"` trong câu lệnh `print` đầu tiên đảm bảo một dòng trống được chèn vào trước mỗi cặp khóa–giá trị trong đầu ra:

[[111]]
Một lần nữa, hãy để ý rằng các cặp khóa–giá trị không được trả về theo thứ tự chúng được lưu, ngay cả khi lặp qua dictionary. Python không quan tâm đến thứ tự lưu các cặp khóa–giá trị; nó chỉ theo dõi liên kết giữa từng khóa và giá trị của nó.

[[112]]
Lặp qua tất cả các cặp khóa–giá trị đặc biệt hiệu quả với những dictionary như ví dụ *favorite_languages.py* ở trang 101, lưu cùng một loại thông tin cho nhiều khóa khác nhau. Nếu lặp qua dictionary `favorite_languages`, bạn sẽ có tên của từng người trong dictionary và ngôn ngữ lập trình yêu thích của họ. Vì khóa luôn là tên một người và giá trị luôn là một ngôn ngữ, chúng ta sẽ dùng các biến `name` và `language` trong vòng lặp thay vì `key` và `value`. Điều này giúp dễ theo dõi những gì đang diễn ra bên trong vòng lặp hơn:

[[115]]
Đoạn mã tại ❶ yêu cầu Python lặp qua từng cặp khóa–giá trị trong dictionary. Khi duyệt qua từng cặp, khóa được lưu vào biến `name`, còn giá trị được lưu vào biến `language`. Những cái tên mang tính mô tả này giúp ta dễ thấy câu lệnh `print` tại ❷ đang làm gì hơn nhiều.

[[116]]
Giờ đây, chỉ với vài dòng mã, chúng ta có thể hiển thị toàn bộ thông tin từ cuộc khảo sát:

[[118]]
Kiểu lặp này vẫn hoạt động tốt như vậy nếu dictionary của chúng ta lưu kết quả khảo sát một nghìn hay thậm chí một triệu người.

[[119]]
### Lặp qua tất cả các khóa trong dictionary

[[120]]
Phương thức `keys()` hữu ích khi bạn không cần làm việc với tất cả các giá trị trong dictionary. Hãy lặp qua dictionary `favorite_languages` và in ra tên của tất cả những người đã tham gia khảo sát:

[[123]]
Dòng tại ❶ yêu cầu Python lấy tất cả các khóa từ dictionary `favorite_languages` và lần lượt lưu từng khóa vào biến `name`. Đầu ra hiển thị tên của tất cả những người đã tham gia khảo sát:

[[125]]
Lặp qua các khóa thực ra là hành vi mặc định khi lặp qua một dictionary, nên đoạn mã này sẽ có đầu ra giống hệt nếu bạn viết . . .

[[127]]
thay vì . . .

[[129]]
Bạn có thể chọn dùng phương thức `keys()` một cách tường minh nếu nó giúp mã dễ đọc hơn, hoặc bỏ nó đi nếu muốn.

[[130]]
Bạn có thể truy cập giá trị gắn với bất kỳ khóa nào bạn quan tâm bên trong vòng lặp bằng cách dùng khóa hiện tại. Hãy in một thông điệp gửi tới vài người bạn về ngôn ngữ họ đã chọn. Chúng ta sẽ lặp qua các tên trong dictionary như trước, nhưng khi tên trùng với một người bạn của ta, ta sẽ hiển thị một thông điệp về ngôn ngữ yêu thích của họ:

[[132]]
Tại ❶, chúng ta tạo một list những người bạn mà ta muốn gửi thông điệp. Bên trong vòng lặp, ta in tên của từng người. Sau đó tại ❷, ta kiểm tra xem `name` đang xét có nằm trong list `friends` không. Nếu có, ta in một lời chào đặc biệt, kèm theo nhắc đến ngôn ngữ họ đã chọn. Để truy cập ngôn ngữ yêu thích tại ❸, ta dùng tên dictionary và giá trị hiện tại của `name` làm khóa. Tên của mọi người đều được in ra, nhưng bạn bè của chúng ta nhận được một thông điệp đặc biệt:

[[135]]
Bạn cũng có thể dùng phương thức `keys()` để biết một người cụ thể đã được khảo sát hay chưa. Lần này, hãy xem Erin đã tham gia khảo sát chưa:

[[137]]
Phương thức `keys()` không chỉ dùng để lặp: Nó thực sự trả về một list tất cả các khóa, và dòng tại ❶ chỉ đơn giản kiểm tra xem `'erin'` có nằm trong list này không. Vì cô ấy không có trong đó, một thông điệp được in ra mời cô tham gia khảo sát:

[[139]]
### Lặp qua các khóa của dictionary theo thứ tự

[[140]]
Một dictionary luôn duy trì liên kết rõ ràng giữa mỗi khóa và giá trị gắn với nó, nhưng bạn không bao giờ nhận được các phần tử từ dictionary theo một thứ tự có thể đoán trước. Điều đó không thành vấn đề, vì bạn thường chỉ muốn lấy đúng giá trị gắn với từng khóa.

[[141]]
Một cách để trả về các phần tử theo một thứ tự nhất định là sắp xếp các khóa khi chúng được trả về trong vòng lặp `for`. Bạn có thể dùng hàm `sorted()` để có một bản sao các khóa theo thứ tự:

[[144]]
Câu lệnh `for` này giống các câu lệnh `for` khác, chỉ khác là chúng ta đã bọc hàm `sorted()` quanh phương thức `dictionary.keys()`. Điều này yêu cầu Python liệt kê tất cả các khóa trong dictionary và sắp xếp list đó trước khi lặp qua nó. Đầu ra hiển thị tất cả những người đã tham gia khảo sát, với tên được sắp xếp theo thứ tự:

[[146]]
### Lặp qua tất cả các giá trị trong dictionary

[[147]]
Nếu chủ yếu quan tâm đến các giá trị mà dictionary chứa, bạn có thể dùng phương thức `values()` để trả về một list các giá trị mà không kèm khóa nào. Ví dụ, giả sử chúng ta chỉ muốn có một list tất cả các ngôn ngữ đã được chọn trong cuộc khảo sát về ngôn ngữ lập trình, mà không cần tên người chọn từng ngôn ngữ:

[[149]]
Câu lệnh `for` ở đây lấy từng giá trị từ dictionary và lưu nó vào biến `language`. Khi các giá trị này được in ra, ta có một list tất cả các ngôn ngữ đã được chọn:

[[151]]
Cách này lấy tất cả các giá trị từ dictionary mà không kiểm tra trùng lặp. Điều đó có thể ổn với số lượng giá trị nhỏ, nhưng trong một cuộc khảo sát có nhiều người trả lời, kết quả sẽ là một list lặp đi lặp lại rất nhiều. Để xem từng ngôn ngữ được chọn mà không bị lặp lại, chúng ta có thể dùng một *set*. Set tương tự list, chỉ khác là mỗi phần tử trong set phải là duy nhất:

[[154]]
Khi bạn bọc `set()` quanh một list chứa các phần tử trùng lặp, Python xác định các phần tử duy nhất trong list và xây dựng một set từ các phần tử đó. Tại ❶, chúng ta dùng `set()` để lấy ra các ngôn ngữ duy nhất trong `favorite_languages.values()`.

[[155]]
Kết quả là một list không trùng lặp gồm các ngôn ngữ đã được những người tham gia khảo sát nhắc đến:

[[157]]
Khi tiếp tục học Python, bạn sẽ thường tìm thấy một tính năng có sẵn của ngôn ngữ giúp bạn làm đúng điều mình muốn với dữ liệu.

[[159]]
**Tự mình thực hành**

[[160]]
**6-4. Bảng thuật ngữ 2:** Giờ đây khi đã biết cách lặp qua dictionary, hãy dọn dẹp đoạn mã từ Bài tập 6-3 (trang 102) bằng cách thay loạt câu lệnh `print` bằng một vòng lặp chạy qua các khóa và giá trị của dictionary. Khi đã chắc vòng lặp hoạt động, hãy thêm năm thuật ngữ Python nữa vào bảng thuật ngữ. Khi chạy lại chương trình, những từ mới này cùng nghĩa của chúng sẽ tự động có mặt trong đầu ra.

[[161]]
**6-5. Sông:** Tạo một dictionary chứa ba con sông lớn và quốc gia mà mỗi con sông chảy qua. Một cặp khóa–giá trị có thể là `'nile': 'egypt'`.

[[162]]
- Dùng một vòng lặp để in ra một câu về từng con sông, chẳng hạn *The Nile runs through Egypt*.

[[163]]
- Dùng một vòng lặp để in ra tên của từng con sông có trong dictionary.

[[164]]
- Dùng một vòng lặp để in ra tên của từng quốc gia có trong dictionary.

[[165]]
**6-6. Khảo sát:** Dùng đoạn mã trong *favorite_languages.py* (trang 104).

[[166]]
- Tạo một list những người nên tham gia khảo sát về ngôn ngữ yêu thích. Đưa vào một số tên đã có trong dictionary và một số tên chưa có.

[[167]]
- Lặp qua list những người nên tham gia khảo sát. Nếu họ đã tham gia khảo sát, in ra thông điệp cảm ơn họ đã trả lời. Nếu họ chưa tham gia khảo sát, in ra thông điệp mời họ tham gia.

[[170]]
## Lồng nhau

[[171]]
Đôi khi bạn sẽ muốn lưu một tập hợp dictionary trong một list, hoặc một list các phần tử làm giá trị trong một dictionary. Điều này được gọi là *lồng nhau* (nesting). Bạn có thể lồng một tập hợp dictionary bên trong một list, một list các phần tử bên trong một dictionary, hoặc thậm chí một dictionary bên trong một dictionary khác. Lồng nhau là một tính năng mạnh mẽ, như các ví dụ sau sẽ chứng minh.

[[172]]
### List chứa các dictionary

[[173]]
Dictionary `alien_0` chứa nhiều thông tin về một người ngoài hành tinh, nhưng không có chỗ để lưu thông tin về người ngoài hành tinh thứ hai, chứ đừng nói đến cả một màn hình đầy người ngoài hành tinh. Làm thế nào để quản lý cả một đội quân người ngoài hành tinh? Một cách là tạo một list người ngoài hành tinh, trong đó mỗi người ngoài hành tinh là một dictionary chứa thông tin về người đó. Ví dụ, đoạn mã sau xây dựng một list gồm ba người ngoài hành tinh:

[[176]]
Đầu tiên, chúng ta tạo ba dictionary, mỗi dictionary biểu diễn một người ngoài hành tinh khác nhau. Tại ❶, ta đóng gói từng dictionary này vào một list có tên `aliens`. Cuối cùng, ta lặp qua list và in ra từng người ngoài hành tinh:

[[178]]
Một ví dụ thực tế hơn sẽ có nhiều hơn ba người ngoài hành tinh, với đoạn mã tự động tạo ra từng người. Trong ví dụ sau, chúng ta dùng `range()` để tạo một đội quân gồm 30 người ngoài hành tinh:

[[181]]
Ví dụ này bắt đầu bằng một list rỗng để chứa tất cả những người ngoài hành tinh sẽ được tạo ra. Tại ❶, `range()` trả về một tập hợp số, chỉ đơn giản cho Python biết chúng ta muốn vòng lặp lặp lại bao nhiêu lần. Mỗi lần vòng lặp chạy, ta tạo một người ngoài hành tinh mới ❷ rồi nối từng người mới vào list `aliens` ❸. Tại ❹, ta dùng một lát cắt để in ra năm người ngoài hành tinh đầu tiên, rồi tại ❺, ta in ra độ dài của list để chứng minh rằng ta đã thực sự tạo ra đủ đội quân 30 người ngoài hành tinh:

[[183]]
Những người ngoài hành tinh này đều có cùng đặc điểm, nhưng Python coi mỗi người là một đối tượng riêng biệt, cho phép chúng ta sửa đổi từng người một cách riêng lẻ.

[[184]]
Bạn có thể làm việc với một nhóm người ngoài hành tinh như thế này ra sao? Hãy tưởng tượng một khía cạnh của trò chơi là có một số người ngoài hành tinh đổi màu và di chuyển nhanh hơn khi trò chơi tiến triển. Khi đến lúc đổi màu, ta có thể dùng một vòng lặp `for` và một câu lệnh `if` để thay đổi màu của người ngoài hành tinh. Ví dụ, để biến ba người ngoài hành tinh đầu tiên thành những người ngoài hành tinh màu vàng, tốc độ trung bình, mỗi người đáng giá 10 điểm, ta có thể làm như sau:

[[186]]
Vì muốn sửa đổi ba người ngoài hành tinh đầu tiên, chúng ta lặp qua một lát cắt chỉ gồm ba người ngoài hành tinh đầu tiên. Hiện tại tất cả người ngoài hành tinh đều màu xanh lá, nhưng không phải lúc nào cũng vậy, nên ta viết một câu lệnh `if` để đảm bảo chỉ sửa đổi những người ngoài hành tinh màu xanh lá. Nếu người ngoài hành tinh màu xanh lá, ta đổi màu thành `'yellow'`, tốc độ thành `'medium'`, và số điểm thành `10`, như trong đầu ra sau:

[[189]]
Bạn có thể mở rộng vòng lặp này bằng cách thêm một khối `elif` biến những người ngoài hành tinh màu vàng thành màu đỏ, di chuyển nhanh, mỗi người đáng giá 15 điểm. Không cần trình bày lại toàn bộ chương trình, vòng lặp đó sẽ trông như thế này:

[[191]]
Việc lưu nhiều dictionary trong một list là điều phổ biến khi mỗi dictionary chứa nhiều loại thông tin về một đối tượng. Ví dụ, bạn có thể tạo một dictionary cho mỗi người dùng trên một trang web, như chúng ta đã làm trong *user.py* ở trang 103, và lưu các dictionary riêng lẻ đó trong một list có tên `users`. Tất cả các dictionary trong list nên có cấu trúc giống hệt nhau để bạn có thể lặp qua list và làm việc với từng đối tượng dictionary theo cùng một cách.

[[192]]
### List bên trong dictionary

[[193]]
Thay vì đặt một dictionary bên trong một list, đôi khi đặt một list bên trong một dictionary lại hữu ích. Ví dụ, hãy xem cách bạn có thể mô tả một chiếc pizza mà ai đó đang gọi. Nếu chỉ dùng một list, tất cả những gì bạn thực sự lưu được là một list các topping của chiếc pizza. Với một dictionary, list các topping chỉ là một khía cạnh của chiếc pizza mà bạn đang mô tả.

[[194]]
Trong ví dụ sau, hai loại thông tin được lưu cho mỗi chiếc pizza: loại đế bánh và một list các topping. List topping là giá trị gắn với khóa `'toppings'`. Để dùng các phần tử trong list, chúng ta viết tên dictionary và khóa `'toppings'`, giống như với bất kỳ giá trị nào trong dictionary. Thay vì trả về một giá trị đơn lẻ, ta nhận được một list topping:

[[198]]
Chúng ta bắt đầu tại ❶ với một dictionary chứa thông tin về một chiếc pizza đã được gọi. Một khóa trong dictionary là `'crust'`, và giá trị gắn với nó là chuỗi `'thick'`. Khóa tiếp theo, `'toppings'`, có giá trị là một list lưu tất cả các topping được yêu cầu. Tại ❷, ta tóm tắt đơn hàng trước khi làm pizza. Để in các topping, ta viết một vòng lặp `for` ❸. Để truy cập list topping, ta dùng khóa `'toppings'`, và Python lấy list topping từ dictionary.

[[199]]
Đầu ra sau tóm tắt chiếc pizza mà chúng ta dự định làm:

[[201]]
Bạn có thể lồng một list bên trong dictionary bất cứ khi nào muốn gắn nhiều hơn một giá trị với một khóa duy nhất trong dictionary. Trong ví dụ trước về ngôn ngữ lập trình yêu thích, nếu chúng ta lưu câu trả lời của từng người trong một list, mọi người có thể chọn nhiều hơn một ngôn ngữ yêu thích. Khi lặp qua dictionary, giá trị gắn với mỗi người sẽ là một list ngôn ngữ thay vì một ngôn ngữ duy nhất. Bên trong vòng lặp `for` của dictionary, chúng ta dùng một vòng lặp `for` khác để duyệt qua list ngôn ngữ gắn với từng người:

[[204]]
Như bạn thấy tại ❶, giá trị gắn với mỗi tên giờ là một list. Hãy để ý rằng một số người có một ngôn ngữ yêu thích, còn những người khác có nhiều ngôn ngữ yêu thích. Khi lặp qua dictionary tại ❷, chúng ta dùng tên biến `languages` để giữ từng giá trị từ dictionary, vì ta biết mỗi giá trị sẽ là một list. Bên trong vòng lặp chính của dictionary, ta dùng một vòng lặp `for` khác ❸ để duyệt qua list ngôn ngữ yêu thích của từng người. Giờ đây mỗi người có thể liệt kê bao nhiêu ngôn ngữ yêu thích tùy thích:

[[207]]
Để hoàn thiện chương trình này hơn nữa, bạn có thể thêm một câu lệnh `if` ở đầu vòng lặp `for` của dictionary để xem mỗi người có nhiều hơn một ngôn ngữ yêu thích hay không bằng cách xét giá trị của `len(languages)`. Nếu một người có nhiều hơn một ngôn ngữ yêu thích, đầu ra sẽ giữ nguyên. Nếu người đó chỉ có một ngôn ngữ yêu thích, bạn có thể thay đổi cách diễn đạt cho phù hợp. Ví dụ, bạn có thể viết `Sarah's favorite language is C`.

[[208]]
> **Lưu ý** Bạn không nên lồng list và dictionary quá sâu. Nếu bạn đang lồng các phần tử sâu hơn nhiều so với những gì thấy trong các ví dụ trên, hoặc đang làm việc với mã của người khác có nhiều cấp lồng nhau, thì nhiều khả năng có một cách đơn giản hơn để giải quyết vấn đề.

[[209]]
### Dictionary bên trong dictionary

[[210]]
Bạn có thể lồng một dictionary bên trong một dictionary khác, nhưng khi làm vậy, mã của bạn có thể nhanh chóng trở nên phức tạp. Ví dụ, nếu bạn có nhiều người dùng cho một trang web, mỗi người có một tên người dùng duy nhất, bạn có thể dùng tên người dùng làm khóa trong một dictionary. Sau đó, bạn có thể lưu thông tin về từng người dùng bằng cách dùng một dictionary làm giá trị gắn với tên người dùng của họ. Trong đoạn mã sau, chúng ta lưu ba mẩu thông tin về mỗi người dùng: tên, họ và nơi ở. Ta sẽ truy cập thông tin này bằng cách lặp qua các tên người dùng và dictionary thông tin gắn với mỗi tên người dùng:

[[214]]
Đầu tiên, chúng ta định nghĩa một dictionary có tên `users` với hai khóa: mỗi khóa cho một tên người dùng `'aeinstein'` và `'mcurie'`. Giá trị gắn với mỗi khóa là một dictionary gồm tên, họ và nơi ở của từng người dùng. Tại ❶, ta lặp qua dictionary `users`. Python lưu từng khóa vào biến `username`, và dictionary gắn với mỗi tên người dùng được đưa vào biến `user_info`. Khi đã ở bên trong vòng lặp chính của dictionary, ta in tên người dùng tại ❷.

[[215]]
Tại ❸, chúng ta bắt đầu truy cập dictionary bên trong. Biến `user_info`, chứa dictionary thông tin người dùng, có ba khóa: `'first'`, `'last'` và `'location'`. Ta dùng từng khóa để tạo ra họ tên đầy đủ và nơi ở được định dạng gọn gàng cho mỗi người, rồi in ra bản tóm tắt những gì ta biết về từng người dùng ❹:

[[217]]
Hãy để ý rằng cấu trúc dictionary của mỗi người dùng là giống hệt nhau. Dù Python không bắt buộc điều này, cấu trúc như vậy giúp các dictionary lồng nhau dễ làm việc hơn. Nếu dictionary của mỗi người dùng có các khóa khác nhau, đoạn mã bên trong vòng lặp `for` sẽ phức tạp hơn.

[[219]]
**Tự mình thực hành**

[[220]]
**6-7. Mọi người:** Bắt đầu với chương trình bạn đã viết cho Bài tập 6-1 (trang 102). Tạo hai dictionary mới biểu diễn hai người khác nhau, và lưu cả ba dictionary vào một list có tên `people`. Lặp qua list người đó. Trong khi lặp qua list, hãy in ra mọi thứ bạn biết về từng người.

[[222]]
**6-8. Thú cưng:** Tạo vài dictionary, trong đó tên của mỗi dictionary là tên của một con thú cưng. Trong mỗi dictionary, hãy đưa vào loài vật và tên của chủ nhân. Lưu các dictionary này vào một list có tên `pets`. Tiếp theo, lặp qua list đó và trong khi lặp, in ra mọi thứ bạn biết về từng con thú cưng.

[[223]]
**6-9. Địa điểm yêu thích:** Tạo một dictionary có tên `favorite_places`. Hãy nghĩ ra ba cái tên để dùng làm khóa trong dictionary, và lưu từ một đến ba địa điểm yêu thích cho mỗi người. Để bài tập này thú vị hơn một chút, hãy nhờ vài người bạn kể tên vài địa điểm họ yêu thích. Lặp qua dictionary và in ra tên của từng người cùng các địa điểm yêu thích của họ.

[[224]]
**6-10. Số yêu thích:** Sửa chương trình của bạn từ Bài tập 6-2 (trang 102) để mỗi người có thể có nhiều hơn một số yêu thích. Sau đó in ra tên của từng người cùng các số yêu thích của họ.

[[225]]
**6-11. Thành phố:** Tạo một dictionary có tên `cities`. Dùng tên của ba thành phố làm khóa trong dictionary. Tạo một dictionary thông tin về mỗi thành phố, gồm quốc gia mà thành phố thuộc về, dân số ước tính, và một sự thật về thành phố đó. Các khóa cho dictionary của mỗi thành phố nên là những thứ như `country`, `population` và `fact`. In ra tên của từng thành phố và tất cả thông tin bạn đã lưu về nó.

[[226]]
**6-12. Mở rộng:** Giờ chúng ta đang làm việc với những ví dụ đủ phức tạp để có thể được mở rộng theo vô số cách. Hãy dùng một trong các chương trình ví dụ trong chương này và mở rộng nó bằng cách thêm khóa và giá trị mới, thay đổi bối cảnh của chương trình, hoặc cải thiện cách định dạng đầu ra.

[[228]]
## Tổng kết

[[229]]
Trong chương này, bạn đã học cách định nghĩa một dictionary và cách làm việc với thông tin được lưu trong dictionary. Bạn đã học cách truy cập và sửa đổi từng phần tử trong dictionary, và cách lặp qua toàn bộ thông tin trong dictionary. Bạn đã học cách lặp qua các cặp khóa–giá trị, các khóa và các giá trị của dictionary. Bạn cũng đã học cách lồng nhiều dictionary trong một list, lồng list trong dictionary, và lồng một dictionary bên trong một dictionary.

[[230]]
Trong chương tiếp theo, bạn sẽ học về vòng lặp `while` và cách nhận đầu vào từ những người đang dùng chương trình của bạn. Đây sẽ là một chương thú vị, vì bạn sẽ học cách làm cho mọi chương trình của mình có tính tương tác: chúng sẽ có thể phản hồi đầu vào của người dùng.

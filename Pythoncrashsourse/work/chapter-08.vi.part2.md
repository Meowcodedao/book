[[180]]
Chương trình này bắt đầu với một list các thiết kế cần in và một list rỗng có tên `completed_models`, nơi mỗi thiết kế sẽ được chuyển vào sau khi in xong. Chừng nào trong `unprinted_designs` vẫn còn thiết kế, vòng lặp `while` mô phỏng việc in từng thiết kế bằng cách xóa một thiết kế khỏi cuối list, lưu nó vào `current_design`, và hiển thị một thông điệp cho biết thiết kế hiện tại đang được in. Sau đó, nó thêm thiết kế vào list các mô hình đã hoàn thành. Khi vòng lặp chạy xong, một list các thiết kế đã được in sẽ được hiển thị:

[[182]]
Chúng ta có thể tổ chức lại đoạn mã này bằng cách viết hai hàm, mỗi hàm làm một việc cụ thể. Phần lớn mã sẽ không thay đổi; chúng ta chỉ làm cho nó hiệu quả hơn. Hàm thứ nhất sẽ xử lý việc in các thiết kế, và hàm thứ hai sẽ tổng kết những bản in đã được thực hiện:

[[185]]
Tại ❶, chúng ta định nghĩa hàm `print_models()` với hai tham số: một list các thiết kế cần in và một list các mô hình đã hoàn thành. Với hai list này, hàm mô phỏng việc in từng thiết kế bằng cách làm rỗng list thiết kế chưa in và lấp đầy list mô hình đã hoàn thành. Tại ❷, chúng ta định nghĩa hàm `show_completed_models()` với một tham số: list các mô hình đã hoàn thành. Với list này, `show_completed_models()` hiển thị tên của từng mô hình đã được in.

[[186]]
Chương trình này có cùng đầu ra như phiên bản không dùng hàm, nhưng mã được tổ chức tốt hơn nhiều. Đoạn mã làm phần lớn công việc đã được chuyển vào hai hàm riêng biệt, giúp phần chính của chương trình dễ hiểu hơn. Hãy nhìn vào phần thân chương trình để thấy việc hiểu chương trình này đang làm gì đã trở nên dễ dàng hơn biết bao:

[[188]]
Chúng ta thiết lập một list các thiết kế chưa in và một list rỗng sẽ chứa các mô hình đã hoàn thành. Sau đó, vì đã định nghĩa sẵn hai hàm, tất cả những gì ta phải làm là gọi chúng và truyền cho chúng đúng đối số. Ta gọi `print_models()` và truyền cho nó hai list mà nó cần; đúng như mong đợi, `print_models()` mô phỏng việc in các thiết kế. Sau đó, ta gọi `show_completed_models()` và truyền cho nó list các mô hình đã hoàn thành để nó có thể báo cáo những mô hình đã được in. Tên hàm mang tính mô tả cho phép người khác đọc và hiểu đoạn mã này, ngay cả khi không có chú thích.

[[189]]
Chương trình này dễ mở rộng và bảo trì hơn phiên bản không dùng hàm. Nếu sau này cần in thêm thiết kế, ta chỉ cần gọi lại `print_models()`. Nếu nhận ra đoạn mã in cần được sửa đổi, ta chỉ cần sửa một lần, và thay đổi sẽ có hiệu lực ở mọi nơi hàm được gọi. Kỹ thuật này hiệu quả hơn việc phải cập nhật mã riêng rẽ ở nhiều chỗ trong chương trình.

[[190]]
Ví dụ này cũng minh họa ý tưởng rằng mỗi hàm nên có một nhiệm vụ cụ thể. Hàm thứ nhất in từng thiết kế, và hàm thứ hai hiển thị các mô hình đã hoàn thành. Điều này có lợi hơn so với dùng một hàm để làm cả hai việc. Nếu bạn đang viết một hàm và nhận thấy hàm đó làm quá nhiều tác vụ khác nhau, hãy thử tách mã thành hai hàm. Hãy nhớ rằng bạn luôn có thể gọi một hàm từ một hàm khác, điều này có thể hữu ích khi chia một tác vụ phức tạp thành một loạt bước.

[[191]]
### Ngăn hàm sửa đổi list

[[192]]
Đôi khi bạn sẽ muốn ngăn một hàm sửa đổi list. Ví dụ, giả sử bạn bắt đầu với một list các thiết kế chưa in và viết một hàm để chuyển chúng sang list các mô hình đã hoàn thành, như trong ví dụ trước. Có thể bạn quyết định rằng dù đã in tất cả các thiết kế, bạn vẫn muốn giữ list thiết kế chưa in ban đầu để lưu hồ sơ. Nhưng vì bạn đã chuyển hết tên thiết kế ra khỏi `unprinted_designs`, list giờ đã rỗng, và list rỗng là phiên bản duy nhất bạn có; bản gốc đã mất. Trong trường hợp này, bạn có thể giải quyết vấn đề bằng cách truyền cho hàm một bản sao của list chứ không phải bản gốc. Mọi thay đổi mà hàm thực hiện trên list sẽ chỉ ảnh hưởng đến bản sao, còn list gốc vẫn được giữ nguyên.

[[194]]
Bạn có thể gửi một bản sao của list cho hàm như sau:

[[196]]
Ký hiệu lát cắt `[:]` tạo một bản sao của list để gửi cho hàm. Nếu không muốn làm rỗng list thiết kế chưa in trong *print_models.py*, ta có thể gọi `print_models()` như sau:

[[198]]
Hàm `print_models()` vẫn có thể làm việc của mình vì nó vẫn nhận được tên của tất cả các thiết kế chưa in. Nhưng lần này nó dùng một bản sao của list thiết kế chưa in ban đầu, chứ không phải list `unprinted_designs` thực sự. List `completed_models` sẽ được lấp đầy bằng tên các mô hình đã in như trước, nhưng list thiết kế chưa in ban đầu sẽ không bị hàm làm ảnh hưởng.

[[199]]
Dù bạn có thể giữ nguyên nội dung của một list bằng cách truyền bản sao của nó cho hàm, bạn nên truyền list gốc cho hàm trừ khi có lý do cụ thể để truyền bản sao. Để hàm làm việc với một list có sẵn sẽ hiệu quả hơn, tránh tốn thời gian và bộ nhớ cần thiết để tạo một bản sao riêng, đặc biệt khi bạn làm việc với list lớn.

[[201]]
**Tự mình thực hành**

[[202]]
**8-9. Ảo thuật gia:** Tạo một list tên các ảo thuật gia. Truyền list đó cho một hàm có tên `show_magicians()`, hàm in ra tên của từng ảo thuật gia trong list.

[[203]]
**8-10. Ảo thuật gia vĩ đại:** Bắt đầu với một bản sao chương trình của bạn từ Bài tập 8-9. Viết một hàm có tên `make_great()` sửa đổi list ảo thuật gia bằng cách thêm cụm từ *the Great* vào tên của từng ảo thuật gia. Gọi `show_magicians()` để thấy list đã thực sự được sửa đổi.

[[204]]
**8-11. Ảo thuật gia không thay đổi:** Bắt đầu với bài làm của bạn từ Bài tập 8-10. Gọi hàm `make_great()` với một bản sao của list tên ảo thuật gia. Vì list gốc sẽ không thay đổi, hãy trả về list mới và lưu nó vào một list riêng. Gọi `show_magicians()` với mỗi list để cho thấy bạn có một list tên gốc và một list có *the Great* được thêm vào tên của từng ảo thuật gia.

[[207]]
## Truyền số lượng đối số tùy ý

[[208]]
Đôi khi bạn sẽ không biết trước một hàm cần nhận bao nhiêu đối số. May mắn thay, Python cho phép một hàm thu thập số lượng đối số tùy ý từ câu lệnh gọi hàm.

[[209]]
Ví dụ, hãy xét một hàm làm pizza. Nó cần nhận một số topping, nhưng bạn không thể biết trước một người sẽ muốn bao nhiêu topping. Hàm trong ví dụ sau có một tham số, `*toppings`, nhưng tham số này thu thập tất cả các đối số mà dòng gọi hàm cung cấp, bất kể bao nhiêu:

[[212]]
Dấu sao trong tên tham số `*toppings` yêu cầu Python tạo một tuple rỗng có tên `toppings` và đóng gói mọi giá trị nhận được vào tuple này. Câu lệnh `print` trong thân hàm tạo ra đầu ra cho thấy Python có thể xử lý cả lời gọi hàm có một giá trị lẫn lời gọi có ba giá trị. Nó xử lý các lời gọi khác nhau theo cách tương tự. Lưu ý rằng Python đóng gói các đối số vào một tuple, ngay cả khi hàm chỉ nhận một giá trị:

[[214]]
Giờ chúng ta có thể thay câu lệnh `print` bằng một vòng lặp duyệt qua list topping và mô tả chiếc pizza đang được gọi:

[[216]]
Hàm phản hồi phù hợp, dù nó nhận một giá trị hay ba giá trị:

[[219]]
Cú pháp này hoạt động bất kể hàm nhận được bao nhiêu đối số.

[[220]]
### Kết hợp đối số vị trí và đối số tùy ý

[[221]]
Nếu bạn muốn một hàm nhận nhiều loại đối số khác nhau, tham số nhận số lượng đối số tùy ý phải được đặt cuối cùng trong định nghĩa hàm. Python ghép các đối số vị trí và đối số từ khóa trước, rồi thu thập mọi đối số còn lại vào tham số cuối cùng.

[[222]]
Ví dụ, nếu hàm cần nhận kích thước của chiếc pizza, tham số đó phải đứng trước tham số `*toppings`:

[[224]]
Trong định nghĩa hàm, Python lưu giá trị đầu tiên nhận được vào tham số `size`. Tất cả các giá trị khác đứng sau đó được lưu vào tuple `toppings`. Các lời gọi hàm có một đối số cho kích thước trước, theo sau là bao nhiêu topping tùy ý.

[[225]]
Giờ mỗi chiếc pizza có một kích thước và một số topping, và từng mẩu thông tin được in ở đúng chỗ, hiển thị kích thước trước và topping sau:

[[227]]
### Dùng đối số từ khóa tùy ý

[[228]]
Đôi khi bạn sẽ muốn nhận số lượng đối số tùy ý, nhưng không biết trước loại thông tin nào sẽ được truyền cho hàm. Trong trường hợp này, bạn có thể viết hàm nhận bao nhiêu cặp khóa–giá trị tùy theo câu lệnh gọi hàm cung cấp. Một ví dụ là xây dựng hồ sơ người dùng: bạn biết mình sẽ nhận được thông tin về một người dùng, nhưng không chắc sẽ nhận được loại thông tin gì. Hàm `build_profile()` trong ví dụ sau luôn nhận vào tên và họ, nhưng cũng nhận số lượng đối số từ khóa tùy ý:

[[232]]
Định nghĩa của `build_profile()` mong đợi tên và họ, rồi cho phép người dùng truyền vào bao nhiêu cặp tên–giá trị tùy thích. Hai dấu sao trước tham số `**user_info` khiến Python tạo một dictionary rỗng có tên `user_info` và đóng gói mọi cặp tên–giá trị nhận được vào dictionary này. Bên trong hàm, bạn có thể truy cập các cặp tên–giá trị trong `user_info` giống như với bất kỳ dictionary nào.

[[233]]
Trong thân `build_profile()`, chúng ta tạo một dictionary rỗng có tên `profile` để chứa hồ sơ của người dùng. Tại ❶, ta thêm tên và họ vào dictionary này vì luôn nhận được hai mẩu thông tin này từ người dùng. Tại ❷, ta lặp qua các cặp khóa–giá trị bổ sung trong dictionary `user_info` và thêm từng cặp vào dictionary `profile`. Cuối cùng, ta trả dictionary `profile` về dòng gọi hàm.

[[234]]
Chúng ta gọi `build_profile()`, truyền cho nó tên `'albert'`, họ `'einstein'`, và hai cặp khóa–giá trị `location='princeton'` và `field='physics'`. Ta lưu `profile` được trả về vào `user_profile` và in `user_profile` ra:

[[236]]
Dictionary được trả về chứa tên và họ của người dùng, và trong trường hợp này còn có cả nơi ở và lĩnh vực nghiên cứu. Hàm vẫn sẽ hoạt động bất kể có bao nhiêu cặp khóa–giá trị bổ sung được cung cấp trong lời gọi hàm.

[[237]]
Bạn có thể kết hợp các giá trị vị trí, từ khóa và tùy ý theo nhiều cách khác nhau khi viết hàm của riêng mình. Biết rằng tất cả các loại đối số này tồn tại là điều hữu ích, vì bạn sẽ thường gặp chúng khi bắt đầu đọc mã của người khác. Cần luyện tập để học cách dùng đúng các loại khác nhau và biết khi nào nên dùng loại nào. Hiện tại, hãy nhớ dùng cách đơn giản nhất mà vẫn hoàn thành được công việc. Khi tiến bộ hơn, bạn sẽ học được cách dùng phương pháp hiệu quả nhất trong từng trường hợp.

[[240]]
**Tự mình thực hành**

[[241]]
**8-12. Sandwich:** Viết một hàm nhận một list các món mà một người muốn có trong chiếc sandwich. Hàm nên có một tham số thu thập tất cả các món mà lời gọi hàm cung cấp, và in ra bản tóm tắt chiếc sandwich đang được gọi. Gọi hàm ba lần, mỗi lần dùng một số lượng đối số khác nhau.

[[242]]
**8-13. Hồ sơ người dùng:** Bắt đầu với một bản sao của *user_profile.py* từ trang 153. Xây dựng hồ sơ của chính bạn bằng cách gọi `build_profile()`, dùng tên và họ của bạn cùng ba cặp khóa–giá trị khác mô tả về bạn.

[[243]]
**8-14. Ô tô:** Viết một hàm lưu thông tin về một chiếc ô tô vào một dictionary. Hàm luôn nhận tên nhà sản xuất và tên mẫu xe. Sau đó, nó nhận số lượng đối số từ khóa tùy ý. Gọi hàm với thông tin bắt buộc và hai cặp tên–giá trị khác, chẳng hạn màu sắc hoặc một tính năng tùy chọn. Hàm của bạn nên hoạt động với một lời gọi như sau:

[[245]]
In dictionary được trả về ra để đảm bảo mọi thông tin đã được lưu đúng.

[[247]]
## Lưu hàm trong module

[[248]]
Một ưu điểm của hàm là cách chúng tách các khối mã khỏi chương trình chính. Nhờ dùng tên mang tính mô tả cho hàm, chương trình chính của bạn sẽ dễ theo dõi hơn nhiều. Bạn có thể tiến thêm một bước bằng cách lưu các hàm trong một file riêng được gọi là *module*, rồi *import* (nhập) module đó vào chương trình chính. Câu lệnh `import` yêu cầu Python cung cấp mã trong một module cho file chương trình đang chạy.

[[249]]
Lưu hàm trong một file riêng cho phép bạn ẩn đi chi tiết mã của chương trình và tập trung vào logic ở mức cao hơn. Nó cũng cho phép bạn tái sử dụng hàm trong nhiều chương trình khác nhau. Khi lưu hàm trong các file riêng, bạn có thể chia sẻ những file đó với các lập trình viên khác mà không phải chia sẻ toàn bộ chương trình. Biết cách import hàm cũng cho phép bạn sử dụng các thư viện hàm do các lập trình viên khác viết.

[[250]]
Có nhiều cách để import một module, và tôi sẽ giới thiệu ngắn gọn từng cách.

[[251]]
### Import toàn bộ module

[[252]]
Để bắt đầu import hàm, trước tiên chúng ta cần tạo một module. *Module* là một file có đuôi *.py* chứa đoạn mã mà bạn muốn import vào chương trình. Hãy tạo một module chứa hàm `make_pizza()`. Để tạo module này, chúng ta sẽ xóa mọi thứ khỏi file *pizza.py* trừ hàm `make_pizza()`:

[[256]]
Giờ chúng ta sẽ tạo một file riêng có tên *making_pizzas.py* trong cùng thư mục với *pizza.py*. File này import module vừa tạo rồi gọi `make_pizza()` hai lần:

[[259]]
Khi Python đọc file này, dòng `import pizza` yêu cầu Python mở file *pizza.py* và sao chép tất cả các hàm trong đó vào chương trình này. Bạn không thực sự thấy mã được sao chép giữa các file, vì Python sao chép mã ở hậu trường khi chương trình chạy. Tất cả những gì bạn cần biết là mọi hàm được định nghĩa trong *pizza.py* giờ đều có thể dùng trong *making_pizzas.py*.

[[260]]
Để gọi một hàm từ một module đã import, hãy nhập tên module đã import, `pizza`, theo sau là tên hàm, `make_pizza()`, phân tách bằng một dấu chấm ❶. Đoạn mã này cho ra cùng đầu ra như chương trình ban đầu không import module:

[[262]]
Cách import thứ nhất này, trong đó bạn chỉ cần viết `import` theo sau là tên module, giúp mọi hàm trong module đều dùng được trong chương trình của bạn. Nếu bạn dùng kiểu câu lệnh `import` này để import toàn bộ một module có tên *module_name.py*, mỗi hàm trong module đều có thể được dùng thông qua cú pháp sau:

[[265]]
### Import các hàm cụ thể

[[266]]
Bạn cũng có thể import một hàm cụ thể từ một module. Đây là cú pháp chung cho cách này:

[[268]]
Bạn có thể import bao nhiêu hàm tùy thích từ một module bằng cách phân tách tên từng hàm bằng dấu phẩy:

[[270]]
Ví dụ *making_pizzas.py* sẽ trông như thế này nếu chúng ta chỉ muốn import hàm mà mình sẽ dùng:

[[272]]
Với cú pháp này, bạn không cần dùng ký hiệu dấu chấm khi gọi hàm. Vì chúng ta đã import tường minh hàm `make_pizza()` trong câu lệnh `import`, ta có thể gọi nó bằng tên khi dùng hàm.

[[273]]
### Dùng as để đặt bí danh cho hàm

[[274]]
Nếu tên của một hàm bạn đang import có thể xung đột với một tên đã có trong chương trình, hoặc nếu tên hàm dài, bạn có thể dùng một *bí danh* (alias) ngắn gọn, duy nhất — một cái tên thay thế giống như biệt danh của hàm. Bạn sẽ đặt cho hàm biệt danh đặc biệt này khi import hàm.

[[275]]
Ở đây, chúng ta đặt cho hàm `make_pizza()` một bí danh, `mp()`, bằng cách import `make_pizza as mp`. Từ khóa `as` đổi tên một hàm bằng bí danh mà bạn cung cấp:

[[277]]
Câu lệnh `import` ở đây đổi tên hàm `make_pizza()` thành `mp()` trong chương trình này. Bất cứ khi nào muốn gọi `make_pizza()`, ta chỉ cần viết `mp()` thay thế, và Python sẽ chạy đoạn mã trong `make_pizza()`, đồng thời tránh mọi nhầm lẫn với một hàm `make_pizza()` khác mà bạn có thể đã viết trong file chương trình này.

[[278]]
Cú pháp chung để đặt bí danh là:

[[281]]
### Dùng as để đặt bí danh cho module

[[282]]
Bạn cũng có thể đặt bí danh cho tên module. Đặt cho module một bí danh ngắn, chẳng hạn `p` cho `pizza`, cho phép bạn gọi các hàm của module nhanh hơn. Gọi `p.make_pizza()` ngắn gọn hơn gọi `pizza.make_pizza()`:

[[284]]
Module `pizza` được đặt bí danh `p` trong câu lệnh `import`, nhưng tất cả các hàm của module vẫn giữ tên gốc. Gọi các hàm bằng cách viết `p.make_pizza()` không chỉ ngắn gọn hơn viết `pizza.make_pizza()`, mà còn chuyển sự chú ý của bạn khỏi tên module và cho phép bạn tập trung vào tên mang tính mô tả của các hàm. Những tên hàm này, vốn cho bạn biết rõ mỗi hàm làm gì, quan trọng đối với khả năng đọc hiểu mã hơn là việc dùng tên đầy đủ của module.

[[285]]
Cú pháp chung cho cách này là:

[[287]]
### Import tất cả các hàm trong module

[[288]]
Bạn có thể yêu cầu Python import mọi hàm trong một module bằng cách dùng toán tử dấu sao (`*`):

[[290]]
Dấu sao trong câu lệnh `import` yêu cầu Python sao chép mọi hàm từ module `pizza` vào file chương trình này. Vì mọi hàm đều được import, bạn có thể gọi từng hàm bằng tên mà không cần dùng ký hiệu dấu chấm. Tuy nhiên, tốt nhất là không nên dùng cách này khi bạn làm việc với những module lớn hơn mà mình không viết: nếu module có một tên hàm trùng với một tên đã có trong dự án của bạn, bạn có thể nhận được những kết quả bất ngờ. Python có thể thấy nhiều hàm hoặc biến có cùng tên, và thay vì import riêng từng hàm, nó sẽ ghi đè các hàm.

[[291]]
Cách tốt nhất là import hàm hoặc các hàm mà bạn muốn, hoặc import toàn bộ module và dùng ký hiệu dấu chấm. Điều này giúp mã rõ ràng, dễ đọc và dễ hiểu. Tôi đưa mục này vào để bạn nhận ra những câu lệnh `import` như sau khi gặp chúng trong mã của người khác:

[[294]]
## Định dạng phong cách hàm

[[295]]
Bạn cần lưu ý một vài chi tiết khi định dạng phong cách cho hàm. Hàm nên có tên mang tính mô tả, và những tên này nên dùng chữ thường và dấu gạch dưới. Tên mang tính mô tả giúp bạn và người khác hiểu đoạn mã của bạn đang cố làm gì. Tên module cũng nên tuân theo các quy ước này.

[[296]]
Mỗi hàm nên có một chú thích giải thích ngắn gọn hàm đó làm gì. Chú thích này nên xuất hiện ngay sau định nghĩa hàm và dùng định dạng docstring. Với một hàm được viết tài liệu tốt, các lập trình viên khác có thể sử dụng hàm chỉ bằng cách đọc phần mô tả trong docstring. Họ có thể tin rằng đoạn mã hoạt động đúng như mô tả, và miễn là họ biết tên hàm, các đối số mà hàm cần và loại giá trị mà hàm trả về, họ sẽ có thể dùng nó trong chương trình của mình.

[[297]]
Nếu bạn chỉ định giá trị mặc định cho một tham số, không nên dùng dấu cách ở hai bên dấu bằng:

[[299]]
Quy ước tương tự nên được dùng cho các đối số từ khóa trong lời gọi hàm:

[[301]]
PEP 8 (*https://www.python.org/dev/peps/pep-0008/* ) khuyến nghị giới hạn các dòng mã ở 79 ký tự để mọi dòng đều hiển thị trọn vẹn trong một cửa sổ trình soạn thảo có kích thước hợp lý. Nếu một nhóm tham số khiến định nghĩa hàm dài hơn 79 ký tự, hãy nhấn ENTER sau dấu ngoặc đơn mở trên dòng định nghĩa. Ở dòng tiếp theo, nhấn TAB hai lần để tách danh sách đối số khỏi thân hàm, vốn chỉ được thụt lề một cấp.

[[302]]
Hầu hết các trình soạn thảo tự động căn các dòng tham số bổ sung cho khớp với mức thụt lề bạn đã thiết lập ở dòng đầu tiên:

[[304]]
Nếu chương trình hoặc module của bạn có nhiều hơn một hàm, bạn có thể tách các hàm bằng hai dòng trống để dễ thấy chỗ một hàm kết thúc và hàm tiếp theo bắt đầu.

[[305]]
Mọi câu lệnh `import` nên được viết ở đầu file. Ngoại lệ duy nhất là khi bạn dùng chú thích ở đầu file để mô tả toàn bộ chương trình.

[[308]]
**Tự mình thực hành**

[[309]]
**8-15. In mô hình:** Đặt các hàm của ví dụ *print_models.py* vào một file riêng có tên *printing_functions.py*. Viết một câu lệnh `import` ở đầu *print_models.py*, và sửa file để dùng các hàm đã import.

[[310]]
**8-16. Import:** Dùng một chương trình bạn đã viết có một hàm trong đó, lưu hàm đó vào một file riêng. Import hàm vào file chương trình chính, và gọi hàm theo từng cách sau:

[[312]]
**8-17. Định dạng phong cách hàm:** Chọn ba chương trình bất kỳ bạn đã viết trong chương này, và đảm bảo chúng tuân theo các hướng dẫn về phong cách được mô tả trong mục này.

[[314]]
## Tổng kết

[[315]]
Trong chương này, bạn đã học cách viết hàm và truyền đối số để hàm có được thông tin cần thiết cho công việc của mình. Bạn đã học cách dùng đối số vị trí và đối số từ khóa, và cách nhận số lượng đối số tùy ý. Bạn đã thấy những hàm hiển thị đầu ra và những hàm trả về giá trị. Bạn đã học cách dùng hàm với list, dictionary, câu lệnh `if` và vòng lặp `while`. Bạn cũng đã thấy cách lưu hàm trong những file riêng gọi là *module*, để các file chương trình của bạn đơn giản và dễ hiểu hơn. Cuối cùng, bạn đã học cách định dạng phong cách cho hàm để chương trình tiếp tục có cấu trúc tốt và dễ đọc nhất có thể đối với bạn và người khác.

[[316]]
Một trong những mục tiêu của bạn với tư cách lập trình viên nên là viết mã đơn giản mà làm đúng điều bạn muốn, và hàm giúp bạn làm được điều đó. Hàm cho phép bạn viết các khối mã và để yên chúng một khi đã biết chúng hoạt động. Khi biết một hàm làm đúng công việc của nó, bạn có thể tin rằng nó sẽ tiếp tục hoạt động và chuyển sang nhiệm vụ lập trình tiếp theo.

[[317]]
Hàm cho phép bạn viết mã một lần rồi tái sử dụng đoạn mã đó bao nhiêu lần tùy thích. Khi cần chạy đoạn mã trong một hàm, tất cả những gì bạn phải làm là viết một lời gọi hàm trên một dòng và hàm sẽ làm công việc của nó. Khi cần sửa đổi hành vi của một hàm, bạn chỉ phải sửa một khối mã, và thay đổi đó có hiệu lực ở mọi nơi bạn đã gọi hàm đó.

[[318]]
Dùng hàm giúp chương trình của bạn dễ đọc hơn, và những tên hàm tốt sẽ tóm tắt những gì mỗi phần của chương trình làm. Đọc một loạt lời gọi hàm giúp bạn nắm được chương trình làm gì nhanh hơn nhiều so với đọc một loạt dài các khối mã.

[[320]]
Hàm cũng giúp mã của bạn dễ kiểm thử và gỡ lỗi hơn. Khi phần lớn công việc của chương trình được thực hiện bởi một nhóm hàm, mỗi hàm có một nhiệm vụ cụ thể, việc kiểm thử và bảo trì mã bạn đã viết sẽ dễ dàng hơn nhiều. Bạn có thể viết một chương trình riêng gọi từng hàm và kiểm tra xem mỗi hàm có hoạt động đúng trong mọi tình huống mà nó có thể gặp hay không. Khi làm như vậy, bạn có thể tự tin rằng các hàm của mình sẽ hoạt động đúng mỗi khi bạn gọi chúng.

[[321]]
Trong Chương 9, bạn sẽ học cách viết class. *Class* (lớp) kết hợp hàm và dữ liệu vào một gói gọn gàng có thể được sử dụng theo những cách linh hoạt và hiệu quả.

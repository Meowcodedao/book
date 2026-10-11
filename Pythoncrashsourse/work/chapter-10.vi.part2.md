[[165]]
Chương trình bị dừng đột ngột đã là điều tệ, nhưng để người dùng nhìn thấy traceback cũng không phải là ý hay. Những người dùng không rành kỹ thuật sẽ bối rối khi thấy chúng, và trong một bối cảnh có ý đồ xấu, kẻ tấn công sẽ biết được nhiều hơn mức bạn muốn từ một traceback. Ví dụ, họ sẽ biết tên file chương trình của bạn, và sẽ thấy một phần mã đang không hoạt động đúng. Một kẻ tấn công lành nghề đôi khi có thể dùng thông tin này để xác định loại tấn công nào nên dùng để nhắm vào mã của bạn.

[[166]]
### Khối else

[[167]]
Chúng ta có thể làm cho chương trình này chống chịu lỗi tốt hơn bằng cách bọc dòng có thể gây lỗi trong một khối `try`-`except`. Lỗi xảy ra ở dòng thực hiện phép chia, nên đó là chỗ ta sẽ đặt khối `try`-`except`. Ví dụ này cũng có một khối `else`. Mọi đoạn mã phụ thuộc vào việc khối `try` được thực thi thành công đều được đặt trong khối `else`:

[[169]]
Chúng ta yêu cầu Python thử hoàn thành phép chia trong một khối `try` ❶, khối này chỉ chứa đoạn mã có thể gây ra lỗi. Mọi đoạn mã phụ thuộc vào việc khối `try` thành công được thêm vào khối `else`. Trong trường hợp này, nếu phép chia thành công, ta dùng khối `else` để in kết quả ❸.

[[170]]
Khối `except` cho Python biết cách phản hồi khi một `ZeroDivisionError` phát sinh ❷. Nếu câu lệnh `try` không thành công do lỗi chia cho không, ta in ra một thông điệp thân thiện cho người dùng biết cách tránh loại lỗi này. Chương trình tiếp tục chạy, và người dùng không bao giờ thấy traceback:

[[173]]
Khối `try`-`except`-`else` hoạt động như sau: Python cố chạy đoạn mã trong câu lệnh `try`. Đoạn mã duy nhất nên đặt trong câu lệnh `try` là đoạn mã có thể khiến một ngoại lệ được phát sinh. Đôi khi bạn sẽ có thêm đoạn mã chỉ nên chạy nếu khối `try` thành công; đoạn mã này được đặt trong khối `else`. Khối `except` cho Python biết phải làm gì trong trường hợp một ngoại lệ nhất định phát sinh khi nó cố chạy đoạn mã trong câu lệnh `try`.

[[174]]
Bằng cách lường trước những nguồn gây lỗi có khả năng xảy ra, bạn có thể viết những chương trình vững vàng, tiếp tục chạy ngay cả khi gặp dữ liệu không hợp lệ hoặc tài nguyên bị thiếu. Mã của bạn sẽ chống chịu được những nhầm lẫn vô tình của người dùng và những cuộc tấn công có chủ đích.

[[175]]
### Xử lý ngoại lệ FileNotFoundError

[[176]]
Một vấn đề thường gặp khi làm việc với file là xử lý những file bị thiếu. File bạn đang tìm có thể nằm ở một vị trí khác, tên file có thể bị gõ sai, hoặc file có thể hoàn toàn không tồn tại. Bạn có thể xử lý tất cả những tình huống này một cách đơn giản bằng một khối `try`-`except`.

[[177]]
Hãy thử đọc một file không tồn tại. Chương trình sau cố đọc nội dung của *Alice in Wonderland*, nhưng tôi chưa lưu file *alice.txt* vào cùng thư mục với *alice.py*:

[[180]]
Python không thể đọc từ một file bị thiếu, nên nó phát sinh một ngoại lệ:

[[182]]
Dòng cuối cùng của traceback báo cáo một `FileNotFoundError`: đây là ngoại lệ Python tạo ra khi không tìm thấy file mà nó đang cố mở. Trong ví dụ này, hàm `open()` gây ra lỗi, nên để xử lý nó, khối `try` sẽ bắt đầu ngay trước dòng chứa `open()`:

[[185]]
Trong ví dụ này, đoạn mã trong khối `try` gây ra một `FileNotFoundError`, nên Python tìm một khối `except` khớp với lỗi đó. Sau đó, Python chạy đoạn mã trong khối đó, và kết quả là một thông báo lỗi thân thiện thay vì một traceback:

[[187]]
Chương trình không còn gì để làm nếu file không tồn tại, nên đoạn mã xử lý lỗi không bổ sung được gì nhiều cho chương trình này. Hãy phát triển tiếp ví dụ này và xem việc xử lý ngoại lệ có thể giúp ích thế nào khi bạn làm việc với nhiều hơn một file.

[[188]]
### Phân tích văn bản

[[189]]
Bạn có thể phân tích những file văn bản chứa toàn bộ một cuốn sách. Nhiều tác phẩm văn học kinh điển có sẵn dưới dạng file văn bản đơn giản vì chúng thuộc phạm vi công cộng (public domain). Các văn bản dùng trong mục này lấy từ Project Gutenberg (*http://gutenberg.org/*). Project Gutenberg duy trì một bộ sưu tập các tác phẩm văn học thuộc phạm vi công cộng, và đây là một tài nguyên tuyệt vời nếu bạn muốn làm việc với văn bản văn học trong các dự án lập trình của mình.

[[190]]
Hãy lấy văn bản của *Alice in Wonderland* và thử đếm số từ trong văn bản. Chúng ta sẽ dùng phương thức chuỗi `split()`, phương thức có thể tạo một list các từ từ một chuỗi. Đây là những gì `split()` làm với một chuỗi chỉ chứa tựa đề `"Alice in Wonderland"`:

[[192]]
Phương thức `split()` tách một chuỗi thành nhiều phần ở bất cứ chỗ nào nó tìm thấy dấu cách, và lưu tất cả các phần của chuỗi vào một list. Kết quả là một list các từ trong chuỗi, dù một số dấu câu cũng có thể xuất hiện cùng một số từ. Để đếm số từ trong *Alice in Wonderland*, ta sẽ dùng `split()` trên toàn bộ văn bản. Sau đó, ta sẽ đếm số phần tử trong list để có ý niệm sơ bộ về số từ trong văn bản:

[[195]]
Tôi đã chuyển file *alice.txt* vào đúng thư mục, nên lần này khối `try` sẽ chạy được. Tại ❶, ta lấy chuỗi `contents`, lúc này chứa toàn bộ văn bản của *Alice in Wonderland* dưới dạng một chuỗi dài, và dùng phương thức `split()` để tạo một list tất cả các từ trong cuốn sách. Khi dùng `len()` trên list này để xem độ dài của nó, ta có được một con số xấp xỉ khá tốt về số từ trong chuỗi ban đầu ❷. Tại ❸, ta in ra một câu cho biết đã tìm thấy bao nhiêu từ trong file. Đoạn mã này được đặt trong khối `else` vì nó chỉ hoạt động nếu đoạn mã trong khối `try` được thực thi thành công. Đầu ra cho ta biết có bao nhiêu từ trong *alice.txt*:

[[197]]
Con số này hơi cao một chút vì nhà xuất bản có cung cấp thêm thông tin trong file văn bản được dùng ở đây, nhưng đây là một con số xấp xỉ khá tốt về độ dài của *Alice in Wonderland*.

[[198]]
### Làm việc với nhiều file

[[199]]
Hãy thêm nhiều cuốn sách hơn để phân tích. Nhưng trước khi làm vậy, hãy chuyển phần lớn chương trình này vào một hàm có tên `count_words()`. Nhờ đó, việc chạy phân tích cho nhiều cuốn sách sẽ dễ dàng hơn:

[[202]]
Phần lớn đoạn mã này không thay đổi. Chúng ta chỉ thụt lề nó và chuyển nó vào thân hàm `count_words()`. Giữ cho chú thích luôn được cập nhật khi sửa đổi chương trình là một thói quen tốt, nên ta đã đổi chú thích thành một docstring và diễn đạt lại một chút ❶.

[[204]]
Giờ chúng ta có thể viết một vòng lặp đơn giản để đếm số từ trong bất kỳ văn bản nào ta muốn phân tích. Ta làm điều này bằng cách lưu tên các file cần phân tích vào một list, rồi gọi `count_words()` cho từng file trong list. Ta sẽ thử đếm số từ cho *Alice in Wonderland*, *Siddhartha*, *Moby Dick* và *Little Women*, tất cả đều thuộc phạm vi công cộng. Tôi đã cố tình không đặt *siddhartha.txt* vào thư mục chứa *word_count.py*, để ta có thể xem chương trình xử lý một file bị thiếu tốt đến mức nào:

[[206]]
File *siddhartha.txt* bị thiếu không ảnh hưởng gì đến việc thực thi phần còn lại của chương trình:

[[208]]
Dùng khối `try`-`except` trong ví dụ này mang lại hai ưu điểm đáng kể. Ta ngăn người dùng nhìn thấy traceback, và để chương trình tiếp tục phân tích những văn bản mà nó tìm thấy. Nếu không bắt `FileNotFoundError` do *siddhartha.txt* phát sinh, người dùng sẽ thấy một traceback đầy đủ, và chương trình sẽ ngừng chạy sau khi cố phân tích *Siddhartha*. Nó sẽ không bao giờ phân tích *Moby Dick* hay *Little Women*.

[[209]]
### Thất bại trong im lặng

[[210]]
Trong ví dụ trước, chúng ta đã thông báo cho người dùng rằng một trong các file không có sẵn. Nhưng bạn không cần báo cáo mọi ngoại lệ mà mình bắt được. Đôi khi bạn sẽ muốn chương trình thất bại trong im lặng khi một ngoại lệ xảy ra và tiếp tục chạy như thể không có gì xảy ra. Để làm cho một chương trình thất bại trong im lặng, bạn viết một khối `try` như bình thường, nhưng nói rõ với Python là không làm gì trong khối `except`. Python có một câu lệnh `pass` yêu cầu nó không làm gì trong một khối:

[[213]]
Điểm khác biệt duy nhất giữa đoạn mã này và đoạn mã trước là câu lệnh `pass` tại ❶. Giờ khi một `FileNotFoundError` được phát sinh, đoạn mã trong khối `except` được chạy, nhưng không có gì xảy ra. Không có traceback nào được tạo ra, và không có đầu ra nào để phản hồi lỗi đã phát sinh. Người dùng thấy số từ của từng file tồn tại, nhưng không thấy bất kỳ dấu hiệu nào cho thấy có một file không được tìm thấy:

[[215]]
Câu lệnh `pass` cũng đóng vai trò giữ chỗ. Nó là lời nhắc rằng bạn đang chọn không làm gì tại một điểm cụ thể trong quá trình thực thi chương trình, và có thể bạn sẽ muốn làm gì đó ở đó sau này. Ví dụ, trong chương trình này, ta có thể quyết định ghi tên các file bị thiếu vào một file có tên *missing_files.txt*. Người dùng sẽ không thấy file này, nhưng ta có thể đọc nó và xử lý những văn bản bị thiếu.

[[216]]
### Quyết định báo cáo những lỗi nào

[[217]]
Làm thế nào để biết khi nào nên báo lỗi cho người dùng và khi nào nên thất bại trong im lặng? Nếu người dùng biết những văn bản nào lẽ ra phải được phân tích, có thể họ sẽ đánh giá cao một thông điệp cho họ biết vì sao một số văn bản không được phân tích. Nếu người dùng mong đợi thấy một số kết quả nhưng không biết những cuốn sách nào lẽ ra phải được phân tích, có thể họ không cần biết rằng một số văn bản không có sẵn. Cung cấp cho người dùng những thông tin họ không tìm kiếm có thể làm giảm tính dễ dùng của chương trình. Các cấu trúc xử lý lỗi của Python cho bạn khả năng kiểm soát tỉ mỉ mức độ chia sẻ với người dùng khi có sự cố; bạn quyết định chia sẻ bao nhiêu thông tin.

[[218]]
Mã được viết tốt và được kiểm thử đúng cách thì không dễ gặp lỗi nội tại, chẳng hạn lỗi cú pháp hay lỗi logic. Nhưng mỗi khi chương trình của bạn phụ thuộc vào một thứ gì đó bên ngoài, chẳng hạn đầu vào của người dùng, sự tồn tại của một file, hay sự sẵn có của kết nối mạng, thì luôn có khả năng một ngoại lệ được phát sinh. Một chút kinh nghiệm sẽ giúp bạn biết nên đặt các khối xử lý ngoại lệ ở đâu trong chương trình và nên báo cáo bao nhiêu cho người dùng về những lỗi phát sinh.

[[220]]
**Tự mình thực hành**

[[221]]
**10-6. Phép cộng:** Một vấn đề thường gặp khi yêu cầu nhập đầu vào dạng số là người dùng nhập chữ thay vì số. Khi bạn cố chuyển đầu vào thành `int`, bạn sẽ gặp một `TypeError`. Viết một chương trình yêu cầu nhập hai số. Cộng chúng lại và in kết quả ra. Bắt `TypeError` nếu một trong hai giá trị đầu vào không phải là số, và in ra một thông báo lỗi thân thiện. Kiểm tra chương trình bằng cách nhập hai số, rồi nhập chữ thay vì số.

[[222]]
*(còn tiếp)*

[[224]]
**10-7. Máy tính cộng:** Bọc đoạn mã của bạn từ Bài tập 10-6 trong một vòng lặp `while` để người dùng có thể tiếp tục nhập số ngay cả khi họ nhầm lẫn và nhập chữ thay vì số.

[[225]]
**10-8. Mèo và chó:** Tạo hai file, *cats.txt* và *dogs.txt*. Lưu ít nhất ba tên mèo vào file thứ nhất và ba tên chó vào file thứ hai. Viết một chương trình cố đọc các file này và in nội dung của file ra màn hình. Bọc đoạn mã của bạn trong một khối `try-except` để bắt lỗi `FileNotFound`, và in ra một thông điệp thân thiện nếu một file bị thiếu. Chuyển một trong hai file sang một vị trí khác trên hệ thống, và đảm bảo đoạn mã trong khối `except` được thực thi đúng.

[[226]]
**10-9. Mèo và chó im lặng:** Sửa khối `except` của bạn trong Bài tập 10-8 để thất bại trong im lặng nếu một trong hai file bị thiếu.

[[227]]
**10-10. Những từ phổ biến:** Truy cập Project Gutenberg (*http://gutenberg.org/* ) và tìm một vài văn bản bạn muốn phân tích. Tải về các file văn bản của những tác phẩm này, hoặc sao chép văn bản thô từ trình duyệt vào một file văn bản trên máy tính của bạn.

[[228]]
Bạn có thể dùng phương thức `count()` để biết một từ hoặc cụm từ xuất hiện bao nhiêu lần trong một chuỗi. Ví dụ, đoạn mã sau đếm số lần `'row'` xuất hiện trong một chuỗi:

[[230]]
Hãy để ý rằng việc chuyển chuỗi thành chữ thường bằng `lower()` sẽ bắt được mọi lần xuất hiện của từ bạn đang tìm, bất kể nó được định dạng thế nào.

[[231]]
Viết một chương trình đọc các file bạn tìm được trên Project Gutenberg và xác định từ `'the'` xuất hiện bao nhiêu lần trong mỗi văn bản.

[[233]]
## Lưu trữ dữ liệu

[[234]]
Nhiều chương trình của bạn sẽ yêu cầu người dùng nhập một số loại thông tin nhất định. Bạn có thể cho phép người dùng lưu các tùy chọn trong một trò chơi hoặc cung cấp dữ liệu cho một biểu đồ trực quan. Dù chương trình của bạn tập trung vào điều gì, bạn sẽ lưu thông tin người dùng cung cấp trong các cấu trúc dữ liệu như list và dictionary. Khi người dùng đóng chương trình, hầu như lúc nào bạn cũng sẽ muốn lưu lại thông tin họ đã nhập. Một cách đơn giản để làm điều này là lưu dữ liệu bằng module `json`.

[[236]]
Module `json` cho phép bạn ghi (dump) các cấu trúc dữ liệu Python đơn giản vào một file và tải dữ liệu từ file đó ở lần chạy tiếp theo của chương trình. Bạn cũng có thể dùng `json` để chia sẻ dữ liệu giữa các chương trình Python khác nhau. Hay hơn nữa, định dạng dữ liệu JSON không dành riêng cho Python, nên bạn có thể chia sẻ dữ liệu lưu ở định dạng JSON với những người làm việc bằng nhiều ngôn ngữ lập trình khác. Đây là một định dạng hữu ích, dễ chuyển đổi giữa các nền tảng, và dễ học.

[[237]]
> **Lưu ý** Định dạng JSON (JavaScript Object Notation) ban đầu được phát triển cho JavaScript. Tuy nhiên, từ đó đến nay, nó đã trở thành một định dạng phổ biến được nhiều ngôn ngữ sử dụng, kể cả Python.

[[238]]
### Dùng json.dump() và json.load()

[[239]]
Hãy viết một chương trình ngắn lưu một tập hợp số và một chương trình khác đọc lại các số này vào bộ nhớ. Chương trình thứ nhất sẽ dùng `json.dump()` để lưu tập hợp số, và chương trình thứ hai sẽ dùng `json.load()`.

[[240]]
Hàm `json.dump()` nhận hai đối số: một mẩu dữ liệu cần lưu và một đối tượng file mà nó có thể dùng để lưu dữ liệu. Đây là cách bạn có thể dùng `json.dump()` để lưu một list số:

[[243]]
Đầu tiên, chúng ta import module `json` rồi tạo một list số để làm việc. Tại ❶, ta chọn một tên file để lưu list số. Theo thông lệ, người ta dùng phần mở rộng *.json* để cho biết dữ liệu trong file được lưu ở định dạng JSON. Sau đó, ta mở file ở chế độ ghi, cho phép `json` ghi dữ liệu vào file ❷. Tại ❸, ta dùng hàm `json.dump()` để lưu list `numbers` vào file *numbers.json*.

[[244]]
Chương trình này không có đầu ra, nhưng hãy mở file *numbers.json* và xem nó. Dữ liệu được lưu theo một định dạng trông giống hệt Python:

[[246]]
Giờ chúng ta sẽ viết một chương trình dùng `json.load()` để đọc list đó trở lại bộ nhớ:

[[250]]
Tại ❶, chúng ta đảm bảo đọc từ đúng file đã ghi vào. Lần này khi mở file, ta mở nó ở chế độ đọc vì Python chỉ cần đọc từ file ❷. Tại ❸, ta dùng hàm `json.load()` để tải thông tin được lưu trong *numbers.json*, và lưu nó vào biến `numbers`. Cuối cùng, ta in ra list số đã được khôi phục và thấy rằng đó chính là list đã được tạo trong *number_writer.py*:

[[252]]
Đây là một cách đơn giản để chia sẻ dữ liệu giữa hai chương trình.

[[253]]
### Lưu và đọc dữ liệu do người dùng tạo ra

[[254]]
Lưu dữ liệu bằng `json` rất hữu ích khi bạn làm việc với dữ liệu do người dùng tạo ra, vì nếu không lưu thông tin của người dùng theo cách nào đó, bạn sẽ mất nó khi chương trình ngừng chạy. Hãy xem một ví dụ trong đó chúng ta yêu cầu người dùng nhập tên ở lần đầu tiên họ chạy chương trình, rồi ghi nhớ tên của họ khi họ chạy lại chương trình.

[[255]]
Hãy bắt đầu bằng việc lưu tên của người dùng:

[[258]]
Tại ❶, chúng ta yêu cầu nhập một tên người dùng để lưu. Tiếp theo, ta dùng `json.dump()`, truyền cho nó một tên người dùng và một đối tượng file, để lưu tên người dùng vào một file ❷. Sau đó, ta in ra một thông điệp cho người dùng biết ta đã lưu thông tin của họ ❸:

[[260]]
Giờ hãy viết một chương trình mới chào một người dùng có tên đã được lưu:

[[264]]
Tại ❶, chúng ta dùng `json.load()` để đọc thông tin được lưu trong *username.json* vào biến `username`. Giờ khi đã khôi phục được tên người dùng, ta có thể chào mừng họ trở lại ❷:

[[266]]
Chúng ta cần kết hợp hai chương trình này vào một file. Khi ai đó chạy *remember_me.py*, ta muốn lấy lại tên người dùng của họ từ bộ nhớ nếu có thể; vì vậy, ta sẽ bắt đầu bằng một khối `try` cố khôi phục tên người dùng. Nếu file *username.json* không tồn tại, ta sẽ để khối `except` yêu cầu nhập tên người dùng và lưu nó vào *username.json* cho lần sau:

[[269]]
Không có đoạn mã mới nào ở đây; các khối mã từ hai ví dụ trước chỉ được kết hợp vào một file. Tại ❶, ta thử mở file *username.json*. Nếu file này tồn tại, ta đọc tên người dùng trở lại bộ nhớ ❷ và in ra thông điệp chào mừng người dùng trở lại trong khối `else`. Nếu đây là lần đầu tiên người dùng chạy chương trình, *username.json* sẽ không tồn tại và một `FileNotFoundError` sẽ xảy ra ❸. Python sẽ chuyển sang khối `except`, nơi ta yêu cầu người dùng nhập tên người dùng ❹. Sau đó, ta dùng `json.dump()` để lưu tên người dùng và in ra một lời chào ❺.

[[270]]
Dù khối nào được thực thi, kết quả đều là một tên người dùng và một lời chào phù hợp. Nếu đây là lần đầu tiên chương trình chạy, đầu ra sẽ là:

[[272]]
Ngược lại:

[[274]]
Đây là đầu ra bạn thấy nếu chương trình đã được chạy ít nhất một lần.

[[276]]
### Tái cấu trúc mã

[[277]]
Bạn sẽ thường đến một thời điểm mà mã của mình đã hoạt động, nhưng bạn nhận ra mình có thể cải thiện nó bằng cách chia nhỏ thành một loạt hàm, mỗi hàm có một nhiệm vụ cụ thể. Quá trình này được gọi là *tái cấu trúc mã* (refactoring). Tái cấu trúc giúp mã của bạn gọn gàng hơn, dễ hiểu hơn và dễ mở rộng hơn.

[[278]]
Chúng ta có thể tái cấu trúc *remember_me.py* bằng cách chuyển phần lớn logic của nó vào một hoặc nhiều hàm. Trọng tâm của *remember_me.py* là chào người dùng, vậy hãy chuyển toàn bộ đoạn mã hiện có vào một hàm có tên `greet_user()`:

[[281]]
Vì giờ đang dùng hàm, chúng ta cập nhật chú thích bằng một docstring phản ánh cách chương trình hiện đang hoạt động ❶. File này gọn gàng hơn một chút, nhưng hàm `greet_user()` đang làm nhiều hơn là chỉ chào người dùng — nó còn lấy tên người dùng đã lưu nếu có, và yêu cầu nhập tên người dùng mới nếu chưa có.

[[282]]
Hãy tái cấu trúc `greet_user()` để nó không phải làm quá nhiều tác vụ khác nhau. Chúng ta sẽ bắt đầu bằng việc chuyển đoạn mã lấy tên người dùng đã lưu sang một hàm riêng:

[[285]]
Hàm mới `get_stored_username()` có mục đích rõ ràng, như được nêu trong docstring tại ❶. Hàm này lấy tên người dùng đã lưu và trả về tên người dùng nếu tìm thấy. Nếu file *username.json* không tồn tại, hàm trả về `None` ❷. Đây là một thói quen tốt: một hàm nên trả về giá trị bạn mong đợi, hoặc trả về `None`. Điều này cho phép ta thực hiện một phép kiểm tra đơn giản với giá trị trả về của hàm. Tại ❸, ta in ra thông điệp chào mừng người dùng trở lại nếu việc lấy tên người dùng thành công, còn nếu không, ta yêu cầu nhập tên người dùng mới.

[[286]]
Chúng ta nên tách thêm một khối mã nữa ra khỏi `greet_user()`. Nếu tên người dùng không tồn tại, ta nên chuyển đoạn mã yêu cầu nhập tên người dùng mới sang một hàm dành riêng cho mục đích đó:

[[289]]
Mỗi hàm trong phiên bản cuối cùng này của *remember_me.py* có một mục đích duy nhất, rõ ràng. Chúng ta gọi `greet_user()`, và hàm đó in ra một thông điệp phù hợp: hoặc chào mừng một người dùng cũ trở lại, hoặc chào một người dùng mới. Nó làm điều này bằng cách gọi `get_stored_username()`, hàm chỉ chịu trách nhiệm lấy tên người dùng đã lưu nếu có. Cuối cùng, `greet_user()` gọi `get_new_username()` nếu cần, hàm chỉ chịu trách nhiệm lấy tên người dùng mới và lưu nó. Việc phân chia công việc thành từng phần như thế này là một phần thiết yếu của việc viết mã rõ ràng, dễ bảo trì và dễ mở rộng.

[[291]]
**Tự mình thực hành**

[[292]]
**10-11. Số yêu thích:** Viết một chương trình yêu cầu người dùng nhập số yêu thích của họ. Dùng `json.dump()` để lưu số này vào một file. Viết một chương trình riêng đọc giá trị này và in ra thông điệp, “I know your favorite number! It’s _____.”

[[293]]
**10-12. Ghi nhớ số yêu thích:** Kết hợp hai chương trình từ Bài tập 10-11 vào một file. Nếu số đã được lưu, hãy báo số yêu thích cho người dùng. Nếu chưa, hãy yêu cầu người dùng nhập số yêu thích và lưu nó vào một file. Chạy chương trình hai lần để thấy nó hoạt động.

[[294]]
**10-13. Xác minh người dùng:** Phiên bản cuối cùng của *remember_me.py* giả định rằng hoặc người dùng đã nhập tên người dùng của họ, hoặc chương trình đang chạy lần đầu tiên. Chúng ta nên sửa đổi nó cho trường hợp người dùng hiện tại không phải là người đã dùng chương trình lần gần nhất.

[[295]]
Trước khi in thông điệp chào mừng trở lại trong `greet_user()`, hãy hỏi người dùng xem đây có phải là tên người dùng đúng không. Nếu không phải, hãy gọi `get_new_username()` để lấy tên người dùng đúng.

[[297]]
## Tổng kết

[[298]]
Trong chương này, bạn đã học cách làm việc với file. Bạn đã học cách đọc toàn bộ file một lần và đọc qua nội dung của file từng dòng một. Bạn đã học cách ghi vào file và nối thêm văn bản vào cuối file. Bạn đã tìm hiểu về ngoại lệ và cách xử lý những ngoại lệ mà nhiều khả năng bạn sẽ gặp trong chương trình. Cuối cùng, bạn đã học cách lưu các cấu trúc dữ liệu Python để có thể lưu lại thông tin người dùng cung cấp, giúp họ không phải bắt đầu lại từ đầu mỗi khi chạy chương trình.

[[299]]
Trong Chương 11, bạn sẽ học những cách hiệu quả để kiểm thử mã của mình. Điều này sẽ giúp bạn tin tưởng rằng đoạn mã bạn phát triển là đúng, và giúp bạn xác định những lỗi phát sinh khi bạn tiếp tục phát triển các chương trình đã viết.

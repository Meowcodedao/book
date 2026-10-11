[[2]]
# Chương 10: File và ngoại lệ

[[4]]
Giờ đây khi đã thành thạo những kỹ năng cơ bản cần thiết để viết các chương trình ngăn nắp, dễ sử dụng, đã đến lúc nghĩ đến việc làm cho chương trình của bạn thiết thực và dễ dùng hơn nữa. Trong chương này, bạn sẽ học cách làm việc với file để chương trình có thể nhanh chóng phân tích lượng lớn dữ liệu.

[[5]]
Bạn sẽ học cách xử lý lỗi để chương trình không bị dừng đột ngột khi gặp những tình huống bất ngờ. Bạn sẽ tìm hiểu về *ngoại lệ* (exception), những đối tượng đặc biệt mà Python tạo ra để quản lý các lỗi phát sinh trong khi chương trình đang chạy. Bạn cũng sẽ tìm hiểu về module `json`, cho phép bạn lưu dữ liệu của người dùng để nó không bị mất khi chương trình ngừng chạy.

[[6]]
Học cách làm việc với file và lưu dữ liệu sẽ giúp chương trình của bạn dễ sử dụng hơn với mọi người. Người dùng sẽ có thể chọn nhập dữ liệu gì và nhập khi nào. Mọi người có thể chạy chương trình của bạn, làm một số việc, rồi đóng chương trình và sau đó tiếp tục từ chỗ đã dừng. Học cách xử lý ngoại lệ sẽ giúp bạn xử lý những tình huống file không tồn tại, cũng như những vấn đề khác có thể khiến chương trình bị dừng đột ngột. Điều này giúp chương trình của bạn vững vàng hơn khi gặp dữ liệu xấu, dù dữ liệu đó đến từ những nhầm lẫn vô tình hay từ những nỗ lực cố ý phá hỏng chương trình. Với những kỹ năng học được trong chương này, bạn sẽ làm cho chương trình của mình hữu dụng hơn, dễ dùng hơn và ổn định hơn.

[[8]]
## Đọc từ file

[[9]]
Có một lượng dữ liệu khổng lồ nằm trong các file văn bản. File văn bản có thể chứa dữ liệu thời tiết, dữ liệu giao thông, dữ liệu kinh tế – xã hội, tác phẩm văn học, và nhiều thứ khác. Đọc từ file đặc biệt hữu ích trong các ứng dụng phân tích dữ liệu, nhưng cũng áp dụng được cho mọi tình huống bạn muốn phân tích hoặc sửa đổi thông tin được lưu trong file. Ví dụ, bạn có thể viết một chương trình đọc nội dung của một file văn bản và ghi lại file đó với định dạng cho phép trình duyệt hiển thị nó.

[[10]]
Khi muốn làm việc với thông tin trong một file văn bản, bước đầu tiên là đọc file vào bộ nhớ. Bạn có thể đọc toàn bộ nội dung của file, hoặc duyệt qua file từng dòng một.

[[11]]
### Đọc toàn bộ file

[[12]]
Để bắt đầu, chúng ta cần một file có vài dòng văn bản. Hãy bắt đầu với một file chứa số *pi* đến 30 chữ số thập phân, mỗi dòng 10 chữ số thập phân:

[[15]]
Để tự thử các ví dụ sau, bạn có thể nhập các dòng này vào trình soạn thảo và lưu file với tên *pi_digits.txt*, hoặc tải file từ tài nguyên của sách tại *https://www.nostarch.com/pythoncrashcourse/*. Hãy lưu file vào cùng thư mục nơi bạn sẽ lưu các chương trình của chương này.

[[16]]
Đây là một chương trình mở file này, đọc nó, và in nội dung của file ra màn hình:

[[19]]
Dòng đầu tiên của chương trình này có rất nhiều điều diễn ra. Hãy bắt đầu bằng việc xem xét hàm `open()`. Để làm bất cứ việc gì với một file, kể cả chỉ in nội dung của nó, trước tiên bạn cần *mở* (open) file để truy cập nó. Hàm `open()` cần một đối số: tên của file bạn muốn mở. Python tìm file này trong thư mục nơi lưu chương trình đang được thực thi. Trong ví dụ này, *file_reader.py* đang chạy, nên Python tìm *pi_digits.txt* trong thư mục nơi lưu *file_reader.py*. Hàm `open()` trả về một đối tượng biểu diễn file. Ở đây, `open('pi_digits.txt')` trả về một đối tượng biểu diễn *pi_digits.txt*. Python lưu đối tượng này vào `file_object`, đối tượng mà chúng ta sẽ làm việc cùng ở phần sau của chương trình.

[[20]]
Từ khóa `with` đóng file khi không còn cần truy cập nó nữa. Hãy để ý cách chúng ta gọi `open()` trong chương trình này nhưng không gọi `close()`. Bạn có thể mở và đóng file bằng cách gọi `open()` và `close()`, nhưng nếu một lỗi trong chương trình khiến câu lệnh `close()` không được thực thi, file có thể sẽ không bao giờ được đóng. Điều này có vẻ nhỏ nhặt, nhưng những file không được đóng đúng cách có thể khiến dữ liệu bị mất hoặc bị hỏng. Và nếu gọi `close()` quá sớm trong chương trình, bạn sẽ thấy mình đang cố làm việc với một file *đã đóng* (một file bạn không thể truy cập), dẫn đến thêm nhiều lỗi khác. Không phải lúc nào cũng dễ biết chính xác khi nào nên đóng file, nhưng với cấu trúc trình bày ở đây, Python sẽ tự xác định điều đó giúp bạn. Tất cả những gì bạn phải làm là mở file và làm việc với nó theo ý muốn, tin tưởng rằng Python sẽ tự động đóng nó vào đúng lúc.

[[22]]
Khi đã có một đối tượng file biểu diễn *pi_digits.txt*, chúng ta dùng phương thức `read()` ở dòng thứ hai của chương trình để đọc toàn bộ nội dung của file và lưu nó thành một chuỗi dài trong `contents`. Khi in giá trị của `contents`, ta nhận lại toàn bộ file văn bản:

[[24]]
Điểm khác biệt duy nhất giữa đầu ra này và file gốc là dòng trống thừa ở cuối đầu ra. Dòng trống xuất hiện vì `read()` trả về một chuỗi rỗng khi đọc đến cuối file; chuỗi rỗng này hiển thị thành một dòng trống. Nếu muốn bỏ dòng trống thừa, bạn có thể dùng `rstrip()` trong câu lệnh `print`:

[[26]]
Hãy nhớ lại rằng phương thức `rstrip()` của Python loại bỏ mọi ký tự khoảng trắng ở phía bên phải của một chuỗi. Giờ đầu ra khớp chính xác với nội dung của file gốc:

[[28]]
### Đường dẫn file

[[29]]
Khi bạn truyền một tên file đơn giản như *pi_digits.txt* cho hàm `open()`, Python tìm trong thư mục nơi lưu file đang được thực thi (tức là file chương trình *.py* của bạn).

[[30]]
Đôi khi, tùy thuộc vào cách bạn tổ chức công việc, file bạn muốn mở sẽ không nằm cùng thư mục với file chương trình. Ví dụ, bạn có thể lưu các file chương trình trong một thư mục có tên *python_work*; bên trong *python_work*, bạn có thể có một thư mục khác có tên *text_files* để phân biệt các file chương trình với các file văn bản mà chúng xử lý. Dù *text_files* nằm trong *python_work*, chỉ truyền cho `open()` tên của một file trong *text_files* sẽ không hoạt động, vì Python sẽ chỉ tìm trong *python_work* rồi dừng lại ở đó; nó sẽ không tiếp tục tìm trong *text_files.* Để Python mở được file từ một thư mục khác với thư mục lưu file chương trình, bạn cần cung cấp một *đường dẫn file* (file path), cho Python biết phải tìm ở một vị trí cụ thể trên hệ thống của bạn.

[[32]]
Vì *text_files* nằm bên trong *python_work*, bạn có thể dùng đường dẫn file tương đối để mở một file từ *text_files.* *Đường dẫn file tương đối* (relative file path) yêu cầu Python tìm một vị trí cho trước, tính tương đối so với thư mục nơi lưu file chương trình đang chạy. Trên Linux và OS X, bạn sẽ viết:

[[34]]
Dòng này yêu cầu Python tìm file *.txt* mong muốn trong thư mục *text_files* và giả định rằng *text_files* nằm bên trong *python_work* (đúng là như vậy). Trên các hệ thống Windows, bạn dùng dấu gạch chéo ngược (`\`) thay vì dấu gạch chéo xuôi (`/`) trong đường dẫn file:

[[36]]
Bạn cũng có thể cho Python biết chính xác file nằm ở đâu trên máy tính, bất kể chương trình đang được thực thi được lưu ở đâu. Đây được gọi là *đường dẫn file tuyệt đối* (absolute file path). Bạn dùng đường dẫn tuyệt đối nếu đường dẫn tương đối không hoạt động. Chẳng hạn, nếu bạn đặt *text_files* trong một thư mục khác không phải *python_work* — giả sử một thư mục có tên *other_files* — thì chỉ truyền cho `open()` đường dẫn `'text_files/filename.txt'` sẽ không hoạt động, vì Python sẽ chỉ tìm vị trí đó bên trong *python_work*. Bạn sẽ cần viết ra một đường dẫn đầy đủ để chỉ rõ nơi bạn muốn Python tìm.

[[37]]
Đường dẫn tuyệt đối thường dài hơn đường dẫn tương đối, nên sẽ có ích nếu lưu chúng vào một biến rồi truyền biến đó cho `open()`. Trên Linux và OS X, đường dẫn tuyệt đối trông như sau:

[[39]]
còn trên Windows, chúng trông như sau:

[[41]]
Dùng đường dẫn tuyệt đối, bạn có thể đọc file từ bất kỳ vị trí nào trên hệ thống. Hiện tại, cách dễ nhất là lưu file vào cùng thư mục với các file chương trình, hoặc vào một thư mục như *text_files* bên trong thư mục chứa các file chương trình.

[[42]]
> **Lưu ý** Các hệ thống Windows đôi khi vẫn hiểu đúng dấu gạch chéo xuôi trong đường dẫn file. Nếu bạn đang dùng Windows và không nhận được kết quả như mong đợi, hãy nhớ thử dùng dấu gạch chéo ngược.

[[44]]
### Đọc từng dòng

[[45]]
Khi đọc một file, bạn sẽ thường muốn xem xét từng dòng của file. Có thể bạn đang tìm một thông tin nhất định trong file, hoặc muốn sửa đổi văn bản trong file theo cách nào đó. Ví dụ, bạn có thể muốn đọc qua một file dữ liệu thời tiết và làm việc với mọi dòng có chứa từ *sunny* trong phần mô tả thời tiết của ngày hôm đó. Trong một bản tin, bạn có thể tìm mọi dòng có thẻ `<headline>` và viết lại dòng đó với một kiểu định dạng cụ thể.

[[46]]
Bạn có thể dùng vòng lặp `for` trên đối tượng file để lần lượt xem xét từng dòng của file:

[[49]]
Tại ❶, chúng ta lưu tên của file đang đọc vào biến `filename`. Đây là một quy ước phổ biến khi làm việc với file. Vì biến `filename` không biểu diễn file thực sự — nó chỉ là một chuỗi cho Python biết nơi tìm file — bạn có thể dễ dàng thay `'pi_digits.txt'` bằng tên của một file khác mà bạn muốn làm việc. Sau khi gọi `open()`, một đối tượng biểu diễn file và nội dung của nó được lưu vào biến `file_object` ❷. Một lần nữa, ta dùng cú pháp `with` để Python mở và đóng file đúng cách. Để xem xét nội dung của file, ta duyệt qua từng dòng trong file bằng cách lặp qua đối tượng file ❸.

[[50]]
Khi in từng dòng, chúng ta lại thấy thêm nhiều dòng trống hơn:

[[52]]
Những dòng trống này xuất hiện vì có một ký tự xuống dòng vô hình ở cuối mỗi dòng trong file văn bản. Câu lệnh `print` tự thêm một ký tự xuống dòng mỗi lần ta gọi nó, nên cuối cùng ta có hai ký tự xuống dòng ở cuối mỗi dòng: một từ file và một từ câu lệnh `print`. Dùng `rstrip()` trên mỗi dòng trong câu lệnh `print` sẽ loại bỏ những dòng trống thừa này:

[[55]]
Giờ đầu ra lại khớp với nội dung của file:

[[57]]
### Tạo list các dòng từ file

[[58]]
Khi bạn dùng `with`, đối tượng file do `open()` trả về chỉ có thể dùng bên trong khối `with` chứa nó. Nếu muốn giữ quyền truy cập nội dung của file bên ngoài khối `with`, bạn có thể lưu các dòng của file vào một list bên trong khối, rồi làm việc với list đó. Bạn có thể xử lý ngay một số phần của file và hoãn một số việc xử lý đến phần sau của chương trình.

[[59]]
Ví dụ sau lưu các dòng của *pi_digits.txt* vào một list bên trong khối `with`, rồi in các dòng đó ra bên ngoài khối `with`:

[[61]]
Tại ❶, phương thức `readlines()` lấy từng dòng trong file và lưu nó vào một list. List này sau đó được lưu vào `lines`, mà ta có thể tiếp tục làm việc cùng sau khi khối `with` kết thúc. Tại ❷, ta dùng một vòng lặp `for` đơn giản để in từng dòng trong `lines`. Vì mỗi phần tử trong `lines` tương ứng với từng dòng trong file, đầu ra khớp chính xác với nội dung của file.

[[62]]
### Làm việc với nội dung của file

[[63]]
Sau khi đã đọc một file vào bộ nhớ, bạn có thể làm bất cứ điều gì bạn muốn với dữ liệu đó, vậy hãy cùng khám phá nhanh các chữ số của *pi*. Trước tiên, chúng ta sẽ thử tạo một chuỗi duy nhất chứa tất cả các chữ số trong file mà không có khoảng trắng nào:

[[66]]
Chúng ta bắt đầu bằng việc mở file và lưu từng dòng chữ số vào một list, giống như trong ví dụ trước. Tại ❶, ta tạo một biến, `pi_string`, để chứa các chữ số của *pi*. Sau đó, ta tạo một vòng lặp cộng từng dòng chữ số vào `pi_string` và loại bỏ ký tự xuống dòng khỏi mỗi dòng ❷. Tại ❸, ta in chuỗi này ra và cho biết chuỗi dài bao nhiêu:

[[69]]
Biến `pi_string` chứa khoảng trắng vốn nằm ở phía bên trái các chữ số trên mỗi dòng, nhưng ta có thể bỏ nó đi bằng cách dùng `strip()` thay vì `rstrip()`:

[[71]]
Giờ chúng ta có một chuỗi chứa *pi* đến 30 chữ số thập phân. Chuỗi dài 32 ký tự vì nó còn bao gồm chữ số 3 đứng đầu và một dấu chấm thập phân:

[[73]]
> **Lưu ý** Khi Python đọc từ một file văn bản, nó hiểu mọi văn bản trong file là chuỗi. Nếu bạn đọc vào một con số và muốn làm việc với giá trị đó trong ngữ cảnh số, bạn sẽ phải chuyển nó thành số nguyên bằng hàm `int()` hoặc chuyển thành số thực bằng hàm `float()`.

[[74]]
### File lớn: Một triệu chữ số

[[75]]
Cho đến giờ, chúng ta mới tập trung phân tích một file văn bản chỉ chứa ba dòng, nhưng đoạn mã trong các ví dụ này cũng sẽ hoạt động tốt như vậy với những file lớn hơn nhiều. Nếu bắt đầu với một file văn bản chứa *pi* đến 1.000.000 chữ số thập phân thay vì chỉ 30, ta có thể tạo một chuỗi duy nhất chứa tất cả các chữ số này. Ta hoàn toàn không cần thay đổi chương trình, ngoại trừ việc truyền cho nó một file khác. Ta cũng sẽ chỉ in ra 50 chữ số thập phân đầu tiên, để không phải nhìn một triệu chữ số cuộn qua trong terminal:

[[79]]
Đầu ra cho thấy chúng ta quả thực có một chuỗi chứa *pi* đến 1.000.000 chữ số thập phân:

[[81]]
Python không có giới hạn cố hữu nào về lượng dữ liệu bạn có thể làm việc; bạn có thể làm việc với lượng dữ liệu lớn đến mức bộ nhớ của hệ thống có thể xử lý.

[[82]]
> **Lưu ý** Để chạy chương trình này (và nhiều ví dụ tiếp theo), bạn sẽ cần tải các tài nguyên có tại *https://www.nostarch.com/pythoncrashcourse/*.

[[83]]
### Ngày sinh của bạn có nằm trong số Pi không?

[[84]]
Tôi luôn tò mò muốn biết ngày sinh của mình có xuất hiện ở đâu đó trong các chữ số của *pi* hay không. Hãy dùng chương trình vừa viết để xem ngày sinh của một người có xuất hiện ở đâu đó trong một triệu chữ số đầu tiên của *pi* hay không. Chúng ta có thể làm điều này bằng cách biểu diễn mỗi ngày sinh thành một chuỗi chữ số và xem chuỗi đó có xuất hiện ở đâu đó trong `pi_string` không:

[[86]]
Tại ❶, chúng ta yêu cầu người dùng nhập ngày sinh, rồi tại ❷, ta kiểm tra xem chuỗi đó có nằm trong `pi_string` không. Hãy thử xem:

[[88]]
Ngày sinh của tôi quả thực xuất hiện trong các chữ số của *pi*! Khi đã đọc từ một file, bạn có thể phân tích nội dung của nó theo hầu như bất kỳ cách nào bạn có thể tưởng tượng ra.

[[91]]
**Tự mình thực hành**

[[92]]
**10-1. Học Python:** Mở một file trống trong trình soạn thảo văn bản và viết vài dòng tóm tắt những gì bạn đã học về Python cho đến giờ. Bắt đầu mỗi dòng bằng cụm từ *In Python you can...*. Lưu file với tên *learning_python.txt* trong cùng thư mục với các bài tập của chương này. Viết một chương trình đọc file và in những gì bạn đã viết ba lần. In nội dung một lần bằng cách đọc toàn bộ file, một lần bằng cách lặp qua đối tượng file, và một lần bằng cách lưu các dòng vào một list rồi làm việc với chúng bên ngoài khối `with`.

[[93]]
**10-2. Học C:** Bạn có thể dùng phương thức `replace()` để thay thế bất kỳ từ nào trong một chuỗi bằng một từ khác. Đây là một ví dụ nhanh cho thấy cách thay `'dog'` bằng `'cat'` trong một câu:

[[95]]
Đọc từng dòng từ file bạn vừa tạo, *learning_python.txt*, và thay từ *Python* bằng tên một ngôn ngữ khác, chẳng hạn *C*. In từng dòng đã sửa đổi ra màn hình.

[[97]]
## Ghi vào file

[[98]]
Một trong những cách đơn giản nhất để lưu dữ liệu là ghi nó vào một file. Khi bạn ghi văn bản vào một file, đầu ra vẫn còn đó sau khi bạn đóng terminal chứa đầu ra của chương trình. Bạn có thể xem xét đầu ra sau khi chương trình chạy xong, và cũng có thể chia sẻ các file đầu ra với người khác. Bạn cũng có thể viết những chương trình đọc lại văn bản vào bộ nhớ và làm việc với nó sau này.

[[99]]
### Ghi vào một file trống

[[100]]
Để ghi văn bản vào một file, bạn cần gọi `open()` với một đối số thứ hai cho Python biết bạn muốn ghi vào file. Để xem cách này hoạt động ra sao, hãy viết một thông điệp đơn giản và lưu nó vào một file thay vì in nó ra màn hình:

[[103]]
Lời gọi `open()` trong ví dụ này có hai đối số ❶. Đối số thứ nhất vẫn là tên của file ta muốn mở. Đối số thứ hai, `'w'`, cho Python biết ta muốn mở file ở *chế độ ghi* (write mode). Bạn có thể mở file ở *chế độ đọc* (`'r'`), *chế độ ghi* (`'w'`), *chế độ nối thêm* (`'a'`), hoặc một chế độ cho phép bạn vừa đọc vừa ghi vào file (`'r+'`). Nếu bạn bỏ qua đối số chế độ, Python mặc định mở file ở chế độ chỉ đọc.

[[105]]
Hàm `open()` tự động tạo file bạn đang ghi vào nếu file đó chưa tồn tại. Tuy nhiên, hãy cẩn thận khi mở file ở chế độ ghi (`'w'`), vì nếu file đã tồn tại, Python sẽ xóa sạch nội dung file trước khi trả về đối tượng file.

[[106]]
Tại ❷, chúng ta dùng phương thức `write()` trên đối tượng file để ghi một chuỗi vào file. Chương trình này không có đầu ra trên terminal, nhưng nếu mở file *programming.txt*, bạn sẽ thấy một dòng:

[[109]]
File này hoạt động giống như mọi file khác trên máy tính của bạn. Bạn có thể mở nó, viết văn bản mới vào đó, sao chép từ nó, dán vào nó, v.v.

[[110]]
> **Lưu ý** Python chỉ có thể ghi chuỗi vào một file văn bản. Nếu muốn lưu dữ liệu số vào file văn bản, trước tiên bạn sẽ phải chuyển dữ liệu sang dạng chuỗi bằng hàm `str()`.

[[111]]
### Ghi nhiều dòng

[[112]]
Hàm `write()` không thêm ký tự xuống dòng nào vào văn bản bạn ghi. Vì vậy, nếu ghi nhiều hơn một dòng mà không thêm ký tự xuống dòng, file của bạn có thể trông không như ý muốn:

[[114]]
Nếu mở *programming.txt*, bạn sẽ thấy hai dòng bị dồn lại với nhau:

[[116]]
Thêm ký tự xuống dòng vào các câu lệnh `write()` sẽ khiến mỗi chuỗi xuất hiện trên một dòng riêng:

[[118]]
Giờ đầu ra xuất hiện trên các dòng riêng biệt:

[[121]]
Bạn cũng có thể dùng dấu cách, ký tự tab và dòng trống để định dạng đầu ra, giống như bạn vẫn làm với đầu ra trên terminal.

[[122]]
### Nối thêm vào file

[[123]]
Nếu muốn thêm nội dung vào một file thay vì ghi đè lên nội dung hiện có, bạn có thể mở file ở *chế độ nối thêm* (append mode). Khi bạn mở một file ở chế độ nối thêm, Python không xóa nội dung file trước khi trả về đối tượng file. Mọi dòng bạn ghi vào file sẽ được thêm vào cuối file. Nếu file chưa tồn tại, Python sẽ tạo một file rỗng cho bạn.

[[124]]
Hãy sửa *write_message.py* bằng cách thêm vài lý do mới khiến ta yêu thích lập trình vào file *programming.txt* đã có:

[[127]]
Tại ❶, chúng ta dùng đối số `'a'` để mở file ở chế độ nối thêm thay vì ghi đè lên file hiện có. Tại ❷, ta ghi hai dòng mới, được thêm vào *programming.txt*:

[[130]]
Cuối cùng, chúng ta có nội dung ban đầu của file, theo sau là nội dung mới vừa thêm vào.

[[132]]
**Tự mình thực hành**

[[133]]
**10-3. Khách:** Viết một chương trình yêu cầu người dùng nhập tên. Khi họ trả lời, hãy ghi tên của họ vào một file có tên *guest.txt*.

[[134]]
**10-4. Sổ khách:** Viết một vòng lặp `while` yêu cầu người dùng nhập tên. Khi họ nhập tên, in một lời chào ra màn hình và thêm một dòng ghi lại lượt ghé thăm của họ vào một file có tên *guest_book.txt*. Đảm bảo mỗi mục nằm trên một dòng mới trong file.

[[135]]
**10-5. Khảo sát về lập trình:** Viết một vòng lặp `while` hỏi mọi người vì sao họ thích lập trình. Mỗi khi có người nhập một lý do, hãy thêm lý do đó vào một file lưu tất cả các câu trả lời.

[[138]]
## Ngoại lệ

[[139]]
Python dùng những đối tượng đặc biệt gọi là *ngoại lệ* (exception) để quản lý các lỗi phát sinh trong quá trình thực thi chương trình. Mỗi khi xảy ra một lỗi khiến Python không chắc phải làm gì tiếp theo, nó tạo ra một đối tượng ngoại lệ. Nếu bạn viết mã xử lý ngoại lệ đó, chương trình sẽ tiếp tục chạy. Nếu bạn không xử lý ngoại lệ, chương trình sẽ dừng lại và hiển thị một *traceback*, trong đó có báo cáo về ngoại lệ đã được phát sinh.

[[140]]
Ngoại lệ được xử lý bằng các khối `try`-`except`. Một khối `try`-`except` yêu cầu Python làm một việc gì đó, nhưng cũng cho Python biết phải làm gì nếu một ngoại lệ được phát sinh. Khi bạn dùng các khối `try`-`except`, chương trình sẽ tiếp tục chạy ngay cả khi mọi thứ bắt đầu trục trặc. Thay vì những traceback có thể gây khó hiểu cho người dùng, họ sẽ thấy những thông báo lỗi thân thiện do bạn viết.

[[141]]
### Xử lý ngoại lệ ZeroDivisionError

[[142]]
Hãy xem một lỗi đơn giản khiến Python phát sinh một ngoại lệ. Có lẽ bạn biết rằng không thể chia một số cho không, nhưng dù sao hãy cứ yêu cầu Python làm điều đó:

[[145]]
Tất nhiên Python không thể làm điều này, nên chúng ta nhận được một traceback:

[[147]]
Lỗi được báo cáo tại ❶ trong traceback, `ZeroDivisionError`, là một đối tượng ngoại lệ. Python tạo ra loại đối tượng này để phản hồi một tình huống mà nó không thể làm những gì ta yêu cầu. Khi điều này xảy ra, Python dừng chương trình và cho ta biết loại ngoại lệ đã được phát sinh. Ta có thể dùng thông tin này để sửa đổi chương trình. Ta sẽ cho Python biết phải làm gì khi loại ngoại lệ này xảy ra; nhờ đó, nếu nó xảy ra lần nữa, ta đã có sự chuẩn bị.

[[148]]
### Dùng khối try-except

[[149]]
Khi nghĩ rằng một lỗi có thể xảy ra, bạn có thể viết một khối `try`-`except` để xử lý ngoại lệ có thể được phát sinh. Bạn yêu cầu Python thử chạy một đoạn mã, và cho nó biết phải làm gì nếu đoạn mã đó gây ra một loại ngoại lệ cụ thể.

[[150]]
Đây là một khối `try`-`except` để xử lý ngoại lệ `ZeroDivisionError`:

[[153]]
Chúng ta đặt `print(5/0)`, dòng gây ra lỗi, vào bên trong một khối `try`. Nếu đoạn mã trong khối `try` chạy được, Python bỏ qua khối `except`. Nếu đoạn mã trong khối `try` gây ra lỗi, Python tìm một khối `except` có lỗi khớp với lỗi đã được phát sinh và chạy đoạn mã trong khối đó.

[[154]]
Trong ví dụ này, đoạn mã trong khối `try` gây ra một `ZeroDivisionError`, nên Python tìm một khối `except` cho nó biết cách phản hồi. Sau đó, Python chạy đoạn mã trong khối đó, và người dùng thấy một thông báo lỗi thân thiện thay vì một traceback:

[[156]]
Nếu còn đoạn mã nào khác đứng sau khối `try`-`except`, chương trình sẽ tiếp tục chạy vì chúng ta đã cho Python biết cách xử lý lỗi. Hãy xem một ví dụ mà việc bắt lỗi có thể cho phép chương trình tiếp tục chạy.

[[157]]
### Dùng ngoại lệ để tránh chương trình bị dừng đột ngột

[[158]]
Xử lý lỗi đúng cách đặc biệt quan trọng khi chương trình còn có việc phải làm sau khi lỗi xảy ra. Điều này thường xảy ra trong những chương trình yêu cầu người dùng nhập đầu vào. Nếu chương trình phản hồi phù hợp với đầu vào không hợp lệ, nó có thể yêu cầu nhập thêm đầu vào hợp lệ thay vì bị dừng đột ngột.

[[159]]
Hãy tạo một máy tính đơn giản chỉ làm phép chia:

[[162]]
Chương trình này yêu cầu người dùng nhập `first_number` ❶ và, nếu người dùng không nhập *q* để thoát, nhập `second_number` ❷. Sau đó, ta chia hai số này để được `answer` ❸. Chương trình này không làm gì để xử lý lỗi, nên yêu cầu nó chia cho không sẽ khiến nó bị dừng đột ngột:

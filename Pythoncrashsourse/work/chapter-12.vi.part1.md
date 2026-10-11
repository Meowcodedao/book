[[2]]
# Chương 12: Con tàu biết bắn đạn

[[4]]
Hãy cùng xây dựng một trò chơi! Chúng ta sẽ dùng Pygame, một tập hợp các module Python thú vị và mạnh mẽ quản lý đồ họa, hoạt ảnh và thậm chí cả âm thanh, giúp bạn dễ dàng xây dựng những trò chơi phức tạp hơn. Khi Pygame lo những tác vụ như vẽ hình ảnh lên màn hình, bạn có thể bỏ qua phần lớn những đoạn mã tẻ nhạt, khó nhằn và tập trung vào logic ở mức cao hơn của cơ chế trò chơi.

[[5]]
Trong chương này, bạn sẽ cài đặt Pygame rồi tạo một con tàu di chuyển sang phải, sang trái và bắn đạn theo thao tác của người chơi. Trong hai chương tiếp theo, bạn sẽ tạo một đội quân người ngoài hành tinh để tiêu diệt, rồi tiếp tục hoàn thiện trò chơi, chẳng hạn như giới hạn số tàu bạn có thể dùng và thêm bảng điểm.

[[6]]
Từ chương này, bạn cũng sẽ học cách quản lý những dự án lớn trải dài trên nhiều file. Chúng ta sẽ tái cấu trúc khá nhiều mã và quản lý nội dung các file để giữ cho dự án ngăn nắp và mã hiệu quả.

[[8]]
Làm trò chơi là một cách lý tưởng để vừa vui vừa học một ngôn ngữ. Được nhìn người khác chơi trò chơi do mình viết mang lại niềm vui sâu sắc, và viết một trò chơi đơn giản sẽ giúp bạn hiểu các trò chơi chuyên nghiệp được viết như thế nào. Khi học qua chương này, hãy nhập và chạy mã để hiểu mỗi khối mã đóng góp như thế nào vào lối chơi tổng thể. Hãy thử nghiệm với các giá trị và thiết lập khác nhau để hiểu rõ hơn cách tinh chỉnh các tương tác trong trò chơi của riêng bạn.

[[9]]
> **Lưu ý** Alien Invasion sẽ trải dài trên nhiều file khác nhau, vì vậy hãy tạo một thư mục mới trên hệ thống có tên *alien_invasion*. Hãy nhớ lưu tất cả các file của dự án vào thư mục này để các câu lệnh `import` hoạt động đúng.

[[10]]
## Lập kế hoạch cho dự án

[[11]]
Khi xây dựng một dự án lớn, việc chuẩn bị một kế hoạch trước khi bắt đầu viết mã là rất quan trọng. Kế hoạch sẽ giúp bạn tập trung và tăng khả năng bạn hoàn thành dự án.

[[12]]
Hãy viết một mô tả về lối chơi tổng thể. Dù mô tả này không bao quát mọi chi tiết của Alien Invasion, nó cho ta một ý niệm rõ ràng về cách bắt đầu xây dựng trò chơi:

[[13]]
> Trong Alien Invasion, người chơi điều khiển một con tàu xuất hiện ở chính giữa phía dưới màn hình. Người chơi có thể di chuyển con tàu sang phải, sang trái bằng các phím mũi tên và bắn đạn bằng phím cách. Khi trò chơi bắt đầu, một đội quân người ngoài hành tinh tràn ngập bầu trời và di chuyển ngang qua, rồi xuống dần phía dưới màn hình. Người chơi bắn và tiêu diệt những người ngoài hành tinh. Nếu người chơi bắn hạ tất cả người ngoài hành tinh, một đội quân mới xuất hiện và di chuyển nhanh hơn đội quân trước. Nếu bất kỳ người ngoài hành tinh nào đâm vào tàu của người chơi hoặc chạm tới đáy màn hình, người chơi mất một con tàu. Nếu người chơi mất ba con tàu, trò chơi kết thúc.

[[14]]
Trong giai đoạn phát triển đầu tiên, chúng ta sẽ tạo một con tàu có thể di chuyển sang phải và sang trái. Con tàu phải có thể bắn đạn khi người chơi nhấn phím cách. Sau khi thiết lập hành vi này, ta có thể chuyển sự chú ý sang những người ngoài hành tinh và hoàn thiện lối chơi.

[[15]]
## Cài đặt Pygame

[[16]]
Trước khi bắt đầu viết mã, hãy cài đặt Pygame. Dưới đây là cách cài đặt trên Linux, OS X và Microsoft Windows.

[[17]]
Nếu bạn dùng Python 3 trên Linux hoặc dùng OS X, bạn sẽ cần dùng pip để cài đặt Pygame. pip là một chương trình lo việc tải về và cài đặt các package Python giúp bạn. Các mục sau sẽ hướng dẫn bạn cách cài đặt package bằng pip.

[[18]]
Nếu bạn dùng Python 2.7 trên Linux hoặc dùng Windows, bạn sẽ không cần pip để cài đặt Pygame. Thay vào đó, hãy chuyển sang mục “Cài đặt Pygame trên Linux” ở trang 238 hoặc “Cài đặt Pygame trên Windows” ở trang 240.

[[20]]
> **Lưu ý** Hướng dẫn cài đặt pip trên mọi hệ thống có trong các mục tiếp theo, vì bạn sẽ cần pip cho các dự án trực quan hóa dữ liệu và ứng dụng web. Các hướng dẫn này cũng có trong tài nguyên trực tuyến tại *https://www.nostarch.com/pythoncrashcourse/*. Nếu gặp khó khăn với hướng dẫn ở đây, hãy xem hướng dẫn trực tuyến có phù hợp với bạn không.

[[21]]
### Cài đặt package Python bằng pip

[[22]]
Các phiên bản Python mới nhất đều có cài sẵn pip, vì vậy trước tiên hãy kiểm tra xem pip đã có trên hệ thống của bạn chưa. Với Python 3, pip đôi khi được gọi là *pip3*.

[[23]]
#### Kiểm tra pip trên Linux và OS X

[[24]]
Mở một cửa sổ terminal và nhập lệnh sau:

[[26]]
Nếu hệ thống của bạn chỉ cài một phiên bản Python và bạn thấy đầu ra tương tự như thế này, hãy chuyển sang mục “Cài đặt Pygame trên Linux” ở trang 238 hoặc “Cài đặt Pygame trên OS X” ở trang 239. Nếu nhận được thông báo lỗi, hãy thử dùng `pip3` thay vì `pip`. Nếu cả hai đều chưa được cài trên hệ thống, hãy chuyển sang mục “Cài đặt pip” ở trang 238.

[[27]]
Nếu hệ thống của bạn có nhiều hơn một phiên bản Python, hãy xác minh rằng pip được gắn với phiên bản Python bạn đang dùng — ví dụ, `python 3.5` tại ❶. Nếu pip được gắn với đúng phiên bản Python, hãy chuyển sang mục “Cài đặt Pygame trên Linux” ở trang 238 hoặc “Cài đặt Pygame trên OS X” ở trang 239. Nếu pip được gắn với sai phiên bản Python, hãy thử dùng `pip3` thay vì `pip`. Nếu không lệnh nào hoạt động với phiên bản Python bạn đang dùng, hãy chuyển sang mục “Cài đặt pip” ở trang 238.

[[28]]
#### Kiểm tra pip trên Windows

[[29]]
Mở một cửa sổ terminal và nhập lệnh sau:

[[31]]
Nếu hệ thống của bạn chỉ cài một phiên bản Python và bạn thấy đầu ra tương tự như thế này, hãy chuyển sang mục “Cài đặt Pygame trên Windows” ở trang 240. Nếu nhận được thông báo lỗi, hãy thử dùng `pip3` thay vì `pip`. Nếu cả hai đều chưa được cài trên hệ thống, hãy chuyển sang mục “Cài đặt pip” ở trang 238.

[[32]]
Nếu hệ thống của bạn cài nhiều hơn một phiên bản Python, hãy xác minh rằng pip được gắn với phiên bản Python bạn đang dùng — ví dụ, `python 3.5` tại ❶. Nếu pip được gắn với đúng phiên bản Python, hãy chuyển sang mục “Cài đặt Pygame trên Windows” ở trang 240. Nếu pip được gắn với sai phiên bản Python, hãy thử dùng `pip3` thay vì `pip`. Nếu không lệnh nào hoạt động với phiên bản Python bạn đang dùng, hãy chuyển sang mục “Cài đặt pip” ngay sau đây.

[[34]]
#### Cài đặt pip

[[35]]
Để cài đặt pip, hãy truy cập *https://bootstrap.pypa.io/get-pip.py*. Lưu file nếu được yêu cầu. Nếu mã của *get-pip.py* hiện ra trong trình duyệt, hãy sao chép và dán chương trình vào trình soạn thảo văn bản rồi lưu file với tên *get-pip.py*. Khi *get-pip.py* đã được lưu trên máy tính, bạn sẽ cần chạy nó với quyền quản trị, vì pip sẽ cài đặt các package mới vào hệ thống của bạn.

[[36]]
> **Lưu ý** Nếu không tìm thấy *get-pip.py*, hãy truy cập *https://pip.pypa.io/*, nhấp vào **Installation** ở bảng bên trái, rồi ở mục “Install pip”, đi theo liên kết tới *get-pip.py*.

[[37]]
#### Cài đặt pip trên Linux và OS X

[[38]]
Dùng lệnh sau để chạy *get-pip.py* với quyền quản trị:

[[40]]
> **Lưu ý** Nếu bạn dùng lệnh `python3` để bắt đầu một phiên terminal, bạn nên dùng `sudo python3 get-pip.py` ở đây.

[[41]]
Sau khi chương trình chạy xong, hãy dùng lệnh `pip --version` (hoặc `pip3 --version`) để đảm bảo pip đã được cài đặt đúng.

[[42]]
#### Cài đặt pip trên Windows

[[43]]
Dùng lệnh sau để chạy *get-pip.py*:

[[45]]
Nếu bạn dùng một lệnh khác để chạy Python trong terminal, hãy đảm bảo bạn dùng lệnh đó để chạy *get-pip.py*. Ví dụ, lệnh của bạn có thể là `python3 get-pip.py` hoặc `C:\Python35\python get-pip.py`.

[[46]]
Sau khi chương trình chạy xong, hãy chạy lệnh `python -m pip --version` để đảm bảo pip đã được cài đặt thành công.

[[47]]
### Cài đặt Pygame trên Linux

[[48]]
Nếu bạn dùng Python 2.7, hãy cài đặt Pygame bằng trình quản lý package. Mở một cửa sổ terminal và chạy lệnh sau; lệnh này sẽ tải về và cài đặt Pygame vào hệ thống của bạn:

[[51]]
Kiểm tra bản cài đặt trong một phiên terminal bằng cách nhập như sau:

[[53]]
Nếu không có đầu ra nào xuất hiện, Python đã import Pygame và bạn đã sẵn sàng chuyển sang mục “Bắt đầu dự án trò chơi” ở trang 240.

[[54]]
Nếu bạn đang dùng Python 3, cần thực hiện hai bước: cài đặt các thư viện mà Pygame phụ thuộc, rồi tải về và cài đặt Pygame.

[[55]]
Nhập lệnh sau để cài đặt các thư viện Pygame cần. (Nếu hệ thống của bạn dùng một lệnh như `python3.5`, hãy thay `python3-dev` bằng `python3.5-dev`.)

[[57]]
Lệnh này sẽ cài đặt các thư viện cần thiết để chạy Alien Invasion thành công. Nếu muốn bật thêm một số chức năng nâng cao hơn trong Pygame, chẳng hạn khả năng thêm âm thanh, bạn cũng có thể cài thêm các thư viện sau:

[[59]]
Giờ hãy cài đặt Pygame bằng cách nhập lệnh sau (dùng `pip3` nếu điều đó phù hợp với hệ thống của bạn):

[[61]]
Đầu ra sẽ tạm dừng một chút sau khi thông báo cho bạn những thư viện mà Pygame tìm thấy. Hãy nhấn ENTER, dù một số thư viện bị thiếu. Bạn sẽ thấy một thông báo cho biết Pygame đã được cài đặt thành công.

[[62]]
Để xác nhận việc cài đặt, hãy chạy một phiên terminal Python và thử import Pygame bằng cách nhập như sau:

[[64]]
Nếu cách này hoạt động, hãy chuyển sang mục “Bắt đầu dự án trò chơi” ở trang 240.

[[65]]
### Cài đặt Pygame trên OS X

[[66]]
Bạn sẽ cần Homebrew để cài đặt một số package mà Pygame phụ thuộc. Nếu chưa cài Homebrew, hãy xem hướng dẫn trong Phụ lục A.

[[67]]
Để cài đặt các thư viện mà Pygame phụ thuộc, hãy nhập lệnh sau:

[[70]]
Lệnh này sẽ cài đặt các thư viện cần thiết để chạy Alien Invasion. Bạn sẽ thấy đầu ra cuộn qua khi từng thư viện được cài đặt.

[[71]]
Nếu bạn cũng muốn bật những chức năng nâng cao hơn, chẳng hạn đưa âm thanh vào trò chơi, bạn có thể cài thêm hai thư viện:

[[73]]
Dùng lệnh sau để cài đặt Pygame (dùng `pip` thay vì `pip3` nếu bạn đang chạy Python 2.7):

[[75]]
Khởi động một phiên terminal Python và import Pygame để kiểm tra việc cài đặt có thành công không (nhập `python` thay vì `python3` nếu bạn đang chạy Python 2.7):

[[77]]
Nếu câu lệnh `import` hoạt động, hãy chuyển sang mục “Bắt đầu dự án trò chơi” ngay dưới đây.

[[78]]
### Cài đặt Pygame trên Windows

[[79]]
Dự án Pygame được lưu trữ trên một trang chia sẻ mã có tên Bitbucket. Để cài đặt Pygame trên phiên bản Windows của bạn, hãy tìm một trình cài đặt cho Windows tại *https://bitbucket.org/pygame/pygame/downloads/* khớp với phiên bản Python bạn đang chạy. Nếu không thấy trình cài đặt phù hợp nào được liệt kê trên Bitbucket, hãy xem tại *http://www.lfd.uci.edu/~gohlke/pythonlibs/#pygame*.

[[80]]
Sau khi tải file phù hợp về, hãy chạy trình cài đặt nếu đó là file *.exe*.

[[81]]
Nếu bạn có một file có đuôi *.whl*, hãy sao chép file đó vào thư mục dự án. Mở một cửa sổ lệnh, di chuyển tới thư mục bạn đã sao chép trình cài đặt vào, và dùng pip để chạy trình cài đặt:

[[83]]
## Bắt đầu dự án trò chơi

[[84]]
Giờ chúng ta sẽ bắt đầu xây dựng trò chơi bằng cách trước tiên tạo một cửa sổ Pygame trống, nơi ta có thể vẽ các thành phần của trò chơi như con tàu và người ngoài hành tinh sau này. Ta cũng sẽ cho trò chơi phản hồi đầu vào của người dùng, đặt màu nền và tải hình ảnh con tàu.

[[86]]
### Tạo cửa sổ Pygame và phản hồi đầu vào của người dùng

[[87]]
Đầu tiên, chúng ta sẽ tạo một cửa sổ Pygame trống. Đây là cấu trúc cơ bản của một trò chơi viết bằng Pygame:

[[90]]
Đầu tiên, chúng ta import các module `sys` và `pygame`. Module `pygame` chứa các chức năng cần thiết để làm một trò chơi. Ta sẽ dùng module `sys` để thoát trò chơi khi người chơi thoát.

[[91]]
Alien Invasion bắt đầu bằng hàm `run_game()`. Dòng `pygame.init()` tại ❶ khởi tạo các thiết lập nền mà Pygame cần để hoạt động đúng. Tại ❷, ta gọi `pygame.display.set_mode()` để tạo một cửa sổ hiển thị có tên `screen`, nơi ta sẽ vẽ tất cả các thành phần đồ họa của trò chơi. Đối số `(1200, 800)` là một tuple xác định kích thước của cửa sổ trò chơi. Bằng cách truyền các kích thước này cho `pygame.display.set_mode()`, ta tạo một cửa sổ trò chơi rộng 1200 pixel và cao 800 pixel. (Bạn có thể điều chỉnh các giá trị này tùy theo kích thước màn hình của mình.)

[[92]]
Đối tượng `screen` được gọi là một surface. Trong Pygame, *surface* (bề mặt) là một phần của màn hình nơi bạn hiển thị một thành phần của trò chơi. Mỗi thành phần trong trò chơi, như người ngoài hành tinh hay con tàu, đều là một surface. Surface do `display.set_mode()` trả về biểu diễn toàn bộ cửa sổ trò chơi. Khi ta kích hoạt vòng lặp hoạt ảnh của trò chơi, surface này sẽ tự động được vẽ lại ở mỗi lượt lặp.

[[93]]
Trò chơi được điều khiển bởi một vòng lặp `while` ❸ chứa một vòng lặp sự kiện và đoạn mã quản lý việc cập nhật màn hình. Một *sự kiện* (event) là một hành động người dùng thực hiện trong khi chơi, chẳng hạn nhấn một phím hoặc di chuyển chuột. Để chương trình phản hồi các sự kiện, ta sẽ viết một *vòng lặp sự kiện* (event loop) để *lắng nghe* sự kiện và thực hiện một tác vụ phù hợp tùy theo loại sự kiện đã xảy ra. Vòng lặp `for` tại ❹ là một vòng lặp sự kiện.

[[95]]
Để truy cập các sự kiện mà Pygame phát hiện được, chúng ta sẽ dùng phương thức `pygame.event.get()`. Bất kỳ sự kiện bàn phím hay chuột nào cũng sẽ khiến vòng lặp `for` chạy. Bên trong vòng lặp, ta sẽ viết một loạt câu lệnh `if` để phát hiện và phản hồi các sự kiện cụ thể. Ví dụ, khi người chơi nhấp vào nút đóng của cửa sổ trò chơi, một sự kiện `pygame.QUIT` được phát hiện và ta gọi `sys.exit()` để thoát trò chơi ❺.

[[96]]
Lời gọi `pygame.display.flip()` tại ❻ yêu cầu Pygame hiển thị màn hình vừa được vẽ gần đây nhất. Trong trường hợp này, nó vẽ một màn hình trống ở mỗi lượt lặp của vòng lặp `while` để xóa màn hình cũ, sao cho chỉ màn hình mới được nhìn thấy. Khi ta di chuyển các thành phần của trò chơi, `pygame.display.flip()` sẽ liên tục cập nhật màn hình để hiển thị vị trí mới của các thành phần và ẩn vị trí cũ, tạo ra ảo giác chuyển động mượt mà.

[[97]]
Dòng cuối cùng trong cấu trúc trò chơi cơ bản này gọi `run_game()`, hàm khởi tạo trò chơi và bắt đầu vòng lặp chính.

[[98]]
Hãy chạy đoạn mã này ngay bây giờ, và bạn sẽ thấy một cửa sổ Pygame trống.

[[99]]
### Đặt màu nền

[[100]]
Mặc định Pygame tạo ra một màn hình màu đen, nhưng như vậy thì nhàm chán. Hãy đặt một màu nền khác:

[[103]]
Đầu tiên, chúng ta tạo một màu nền và lưu nó vào `bg_color` ❶. Màu này chỉ cần được chỉ định một lần, nên ta định nghĩa giá trị của nó trước khi đi vào vòng lặp `while` chính.

[[104]]
Màu sắc trong Pygame được chỉ định theo dạng màu RGB: một hỗn hợp của đỏ, xanh lá và xanh dương. Mỗi giá trị màu có thể nằm trong khoảng từ 0 đến 255. Giá trị màu (255, 0, 0) là đỏ, (0, 255, 0) là xanh lá, và (0, 0, 255) là xanh dương. Bạn có thể pha trộn các giá trị RGB để tạo ra 16 triệu màu. Giá trị màu (230, 230, 230) pha trộn lượng đỏ, xanh dương và xanh lá bằng nhau, tạo ra một màu nền xám nhạt.

[[106]]
Tại ❷, chúng ta tô màn hình bằng màu nền thông qua phương thức `screen.fill()`, phương thức chỉ nhận một đối số: một màu.

[[107]]
### Tạo lớp Settings

[[108]]
Mỗi lần đưa thêm chức năng mới vào trò chơi, thông thường chúng ta cũng sẽ đưa vào một số thiết lập mới. Thay vì thêm các thiết lập rải rác khắp mã, hãy viết một module có tên `settings` chứa một lớp có tên `Settings` để lưu tất cả các thiết lập ở một chỗ. Cách này cho phép ta truyền đi một đối tượng thiết lập duy nhất thay vì nhiều thiết lập riêng lẻ. Ngoài ra, nó giúp các lời gọi hàm đơn giản hơn và giúp việc sửa đổi giao diện của trò chơi dễ dàng hơn khi dự án phát triển. Để sửa đổi trò chơi, ta chỉ cần thay đổi một số giá trị trong *settings.py* thay vì phải tìm các thiết lập khác nhau rải rác trong các file.

[[109]]
Đây là lớp `Settings` ban đầu:

[[112]]
Để tạo một thực thể của `Settings` và dùng nó để truy cập các thiết lập, hãy sửa *alien_invasion.py* như sau:

[[116]]
Chúng ta import `Settings` vào file chương trình chính, rồi tạo một thực thể của `Settings` và lưu nó vào `ai_settings` sau khi gọi `pygame.init()` ❶. Khi tạo màn hình ❷, ta dùng các thuộc tính `screen_width` và `screen_height` của `ai_settings`, và ta cũng dùng `ai_settings` để truy cập màu nền khi tô màn hình tại ❸.

[[117]]
## Thêm hình ảnh con tàu

[[118]]
Giờ hãy thêm con tàu vào trò chơi. Để vẽ con tàu của người chơi lên màn hình, chúng ta sẽ tải một hình ảnh rồi dùng phương thức `blit()` của Pygame để vẽ hình ảnh đó.

[[119]]
Khi chọn hình ảnh đồ họa cho trò chơi, hãy nhớ chú ý đến giấy phép sử dụng. Cách an toàn và rẻ nhất để bắt đầu là dùng các hình đồ họa có giấy phép tự do mà bạn có thể sửa đổi, lấy từ một trang web như *http://pixabay.com/*.

[[120]]
Bạn có thể dùng hầu như bất kỳ loại file hình ảnh nào trong trò chơi, nhưng dễ nhất là dùng file bitmap (*.bmp*) vì Pygame mặc định tải được bitmap. Dù có thể cấu hình Pygame để dùng các loại file khác, một số loại file phụ thuộc vào những thư viện hình ảnh nhất định phải được cài trên máy tính của bạn. (Hầu hết hình ảnh bạn tìm được đều ở định dạng *.jpg*, *.png* hoặc *.gif*, nhưng bạn có thể chuyển chúng sang bitmap bằng các công cụ như Photoshop, GIMP và Paint.)

[[121]]
Hãy đặc biệt chú ý đến màu nền trong hình ảnh bạn chọn. Hãy cố tìm một file có nền trong suốt mà bạn có thể thay bằng bất kỳ màu nền nào bằng một trình chỉnh sửa ảnh. Trò chơi của bạn sẽ trông đẹp nhất nếu màu nền của hình ảnh khớp với màu nền của trò chơi. Hoặc, bạn có thể chỉnh màu nền của trò chơi cho khớp với màu nền của hình ảnh.

[[122]]
Với Alien Invasion, bạn có thể dùng file *ship.bmp* (Hình 12-1), có trong tài nguyên của sách tại *https://www.nostarch.com/pythoncrashcourse/*. Màu nền của file khớp với các thiết lập chúng ta đang dùng trong dự án này. Hãy tạo một thư mục có tên *images* bên trong thư mục dự án chính (*alien_invasion*). Lưu file *ship.bmp* vào thư mục *images*.

[[123]]
*Hình 12-1: Con tàu trong Alien Invasion*

[[125]]
### Tạo lớp Ship

[[126]]
Sau khi chọn hình ảnh cho con tàu, chúng ta cần hiển thị nó lên màn hình. Để dùng con tàu, ta sẽ viết một module có tên `ship`, chứa lớp `Ship`. Lớp này sẽ quản lý phần lớn hành vi của con tàu của người chơi.

[[129]]
Đầu tiên, chúng ta import module `pygame`. Phương thức `__init__()` của `Ship` nhận hai tham số: tham chiếu `self` và `screen` nơi ta sẽ vẽ con tàu. Để tải hình ảnh, ta gọi `pygame.image.load()` ❶. Hàm này trả về một surface biểu diễn con tàu, mà ta lưu vào `self.image`.

[[130]]
Khi hình ảnh đã được tải, chúng ta dùng `get_rect()` để truy cập thuộc tính `rect` của surface ❷. Một lý do khiến Pygame hiệu quả là nó cho phép bạn coi các thành phần trò chơi như những hình chữ nhật (*rect*), ngay cả khi chúng không có hình dạng chính xác là hình chữ nhật. Coi một thành phần là hình chữ nhật rất hiệu quả vì hình chữ nhật là hình học đơn giản. Cách này thường hoạt động đủ tốt để không người chơi nào nhận ra rằng ta không làm việc với hình dạng chính xác của từng thành phần trò chơi.

[[131]]
Khi làm việc với một đối tượng `rect`, bạn có thể dùng tọa độ x và y của các cạnh trên, dưới, trái, phải của hình chữ nhật, cũng như của tâm. Bạn có thể đặt bất kỳ giá trị nào trong số này để xác định vị trí hiện tại của rect.

[[132]]
Khi căn giữa một thành phần trò chơi, hãy làm việc với các thuộc tính `center`, `centerx` hoặc `centery` của rect. Khi làm việc ở một cạnh của màn hình, hãy làm việc với các thuộc tính `top`, `bottom`, `left` hoặc `right`. Khi điều chỉnh vị trí theo chiều ngang hoặc chiều dọc của rect, bạn chỉ cần dùng các thuộc tính `x` và `y`, là tọa độ x và y của góc trên bên trái của nó. Các thuộc tính này giúp bạn không phải tự tính toán những thứ mà trước đây các nhà phát triển trò chơi phải làm bằng tay, và bạn sẽ thấy mình dùng chúng thường xuyên.

[[134]]
> **Lưu ý** Trong Pygame, gốc tọa độ (0, 0) nằm ở góc trên bên trái của màn hình, và tọa độ tăng dần khi đi xuống dưới và sang phải. Trên một màn hình 1200 x 800, gốc tọa độ nằm ở góc trên bên trái, và góc dưới bên phải có tọa độ (1200, 800).

[[135]]
Chúng ta sẽ đặt con tàu ở chính giữa phía dưới màn hình. Để làm điều đó, trước tiên hãy lưu rect của màn hình vào `self.screen_rect` ❸, rồi làm cho giá trị của `self.rect.centerx` (tọa độ x của tâm con tàu) khớp với thuộc tính `centerx` của rect màn hình ❹. Làm cho giá trị của `self.rect.bottom` (tọa độ y của đáy con tàu) bằng giá trị thuộc tính `bottom` của rect màn hình. Pygame sẽ dùng các thuộc tính `rect` này để đặt hình ảnh con tàu sao cho nó được căn giữa theo chiều ngang và thẳng hàng với đáy màn hình.

[[136]]
Tại ❺, chúng ta định nghĩa phương thức `blitme()`, phương thức sẽ vẽ hình ảnh lên màn hình tại vị trí được chỉ định bởi `self.rect`.

[[137]]
### Vẽ con tàu lên màn hình

[[138]]
Giờ hãy cập nhật *alien_invasion.py* để nó tạo một con tàu và gọi phương thức `blitme()` của con tàu:

[[141]]
Chúng ta import `Ship` rồi tạo một thực thể của `Ship` (có tên `ship`) sau khi màn hình đã được tạo. Việc này phải đứng trước vòng lặp `while` chính ❶ để ta không tạo một thực thể con tàu mới ở mỗi lượt lặp. Ta vẽ con tàu lên màn hình bằng cách gọi `ship.blitme()` sau khi tô nền, để con tàu xuất hiện phía trên nền ❷.

[[142]]
Khi chạy *alien_invasion.py* lúc này, bạn sẽ thấy một màn hình trò chơi trống với con tàu tên lửa của chúng ta nằm ở chính giữa phía dưới, như trong Hình 12-2.

[[144]]
*Hình 12-2: Alien Invasion với con tàu ở chính giữa phía dưới màn hình*

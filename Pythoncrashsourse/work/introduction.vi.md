[[2]]
# Lời giới thiệu

[[4]]
Lập trình viên nào cũng có một câu chuyện về cách họ học viết chương trình đầu tiên của mình. Tôi bắt đầu học từ khi còn nhỏ, lúc cha tôi đang làm việc cho Digital Equipment Corporation, một trong những công ty tiên phong của kỷ nguyên điện toán hiện đại. Tôi viết chương trình đầu tiên của mình trên một

[[5]]
chiếc máy tính tự lắp mà cha tôi đã ráp dưới tầng hầm nhà. Chiếc máy chỉ gồm một bo mạch chủ trần nối với bàn phím không có vỏ, và màn hình là một ống tia âm cực trần. Chương trình đầu tiên của tôi là một trò chơi đoán số đơn giản, trông giống như thế này:

[[8]]
Tôi sẽ luôn nhớ cảm giác mãn nguyện khi nhìn gia đình mình chơi trò chơi do chính tôi tạo ra và nó hoạt động đúng như tôi mong muốn.

[[9]]
Trải nghiệm ban đầu ấy đã để lại ảnh hưởng lâu dài. Có một niềm vui thực sự khi xây dựng một thứ gì đó có mục đích, một thứ giải quyết được vấn đề. Phần mềm tôi viết bây giờ đáp ứng những nhu cầu quan trọng hơn nhiều so với những nỗ lực thời thơ ấu, nhưng cảm giác mãn nguyện khi tạo ra một chương trình chạy được thì về cơ bản vẫn như xưa.

[[10]]
## Cuốn sách này dành cho ai?

[[11]]
Mục tiêu của cuốn sách này là giúp bạn làm chủ Python nhanh nhất có thể để bạn có thể xây dựng những chương trình chạy được — trò chơi, trực quan hóa dữ liệu và ứng dụng web — đồng thời xây dựng một nền tảng lập trình sẽ có ích cho bạn suốt đời. *Python Crash Course* được viết cho người ở mọi lứa tuổi chưa từng lập trình bằng Python, hoặc chưa từng lập trình bao giờ. Nếu bạn muốn học nhanh những kiến thức cơ bản về lập trình để có thể tập trung vào các dự án thú vị, và bạn thích kiểm tra hiểu biết của mình về các khái niệm mới bằng cách giải quyết những bài toán có ý nghĩa, thì cuốn sách này dành cho bạn. *Python Crash Course* cũng rất phù hợp với giáo viên trung học cơ sở và trung học phổ thông muốn giới thiệu lập trình cho học sinh theo hướng học qua dự án.

[[12]]
## Bạn có thể học được gì?

[[13]]
Mục đích của cuốn sách này là giúp bạn trở thành một lập trình viên giỏi nói chung và một lập trình viên Python giỏi nói riêng. Bạn sẽ học một cách hiệu quả và hình thành những thói quen tốt khi tôi trang bị cho bạn một nền tảng vững chắc về các khái niệm lập trình chung. Sau khi học hết *Python Crash Course*, bạn sẽ sẵn sàng chuyển sang những kỹ thuật Python nâng cao hơn, và ngôn ngữ lập trình tiếp theo của bạn sẽ còn dễ nắm bắt hơn nữa.

[[14]]
Trong phần đầu của cuốn sách, bạn sẽ học những khái niệm lập trình cơ bản cần biết để viết chương trình Python. Đây cũng chính là những khái niệm bạn sẽ học khi bắt đầu với hầu hết mọi ngôn ngữ lập trình. Bạn sẽ tìm hiểu các kiểu dữ liệu khác nhau và cách lưu trữ dữ liệu trong list và dictionary bên trong chương trình. Bạn sẽ học cách xây dựng các tập hợp dữ liệu và duyệt qua chúng một cách hiệu quả. Bạn sẽ học cách dùng vòng lặp `while` và `if` để kiểm tra những điều kiện nhất định, nhờ đó có thể chạy những đoạn mã cụ thể khi các điều kiện đó đúng và chạy những đoạn khác khi chúng không đúng — một kỹ thuật giúp ích rất nhiều cho việc tự động hóa các quy trình.

[[15]]
Bạn sẽ học cách nhận đầu vào từ người dùng để chương trình có tính tương tác, và giữ cho chương trình tiếp tục chạy chừng nào người dùng còn hoạt động. Bạn sẽ tìm hiểu cách viết hàm để tái sử dụng các phần của chương trình, nhờ đó những khối mã thực hiện một việc nhất định chỉ cần viết một lần và có thể dùng bao nhiêu lần tùy ý. Sau đó, bạn sẽ mở rộng khái niệm này cho những hành vi phức tạp hơn bằng class, giúp những chương trình khá đơn giản có thể phản hồi nhiều tình huống khác nhau. Bạn sẽ học cách viết chương trình xử lý êm thấm các lỗi thường gặp. Sau khi học xong từng khái niệm cơ bản này, bạn sẽ viết một vài chương trình ngắn để giải quyết một số bài toán được xác định rõ ràng. Cuối cùng, bạn sẽ bước bước đầu tiên lên trình độ trung cấp bằng cách học viết kiểm thử cho mã của mình, để có thể tiếp tục phát triển chương trình mà không phải lo đưa thêm lỗi vào. Toàn bộ kiến thức trong Phần I sẽ chuẩn bị cho bạn bắt tay vào những dự án lớn hơn, phức tạp hơn.

[[17]]
Trong Phần II, bạn sẽ áp dụng những gì đã học ở Phần I vào ba dự án. Bạn có thể làm một vài hoặc tất cả các dự án này theo bất kỳ thứ tự nào phù hợp nhất với mình. Trong dự án thứ nhất (Chương 12–14), bạn sẽ tạo một trò chơi bắn súng theo phong cách Space Invaders có tên Alien Invasion, gồm nhiều màn với độ khó tăng dần. Sau khi hoàn thành dự án này, bạn sẽ đi được một chặng dài trên con đường tự phát triển các trò chơi 2D của riêng mình.

[[18]]
Dự án thứ hai (Chương 15–17) giới thiệu với bạn về trực quan hóa dữ liệu. Các nhà khoa học dữ liệu tìm cách hiểu được khối lượng thông tin khổng lồ mà họ có trong tay thông qua nhiều kỹ thuật trực quan hóa khác nhau. Bạn sẽ làm việc với các tập dữ liệu do bạn tạo ra bằng mã, các tập dữ liệu tải về từ những nguồn trực tuyến, và các tập dữ liệu mà chương trình của bạn tự động tải về. Sau khi hoàn thành dự án này, bạn sẽ có thể viết chương trình sàng lọc những tập dữ liệu lớn và biểu diễn trực quan thông tin được lưu trữ trong đó.

[[19]]
Trong dự án thứ ba (Chương 18–20), bạn sẽ xây dựng một ứng dụng web nhỏ có tên Learning Log. Dự án này cho phép bạn ghi nhật ký về những ý tưởng và khái niệm đã học được về một chủ đề cụ thể. Bạn sẽ có thể giữ những nhật ký riêng cho từng chủ đề và cho phép người khác tạo tài khoản để bắt đầu nhật ký của riêng họ. Bạn cũng sẽ học cách triển khai (deploy) dự án để bất kỳ ai cũng có thể truy cập trực tuyến từ bất cứ đâu.

[[20]]
## Tại sao lại là Python?

[[21]]
Năm nào tôi cũng cân nhắc xem nên tiếp tục dùng Python hay chuyển sang một ngôn ngữ khác — có lẽ là một ngôn ngữ mới hơn trong thế giới lập trình. Nhưng tôi vẫn tiếp tục tập trung vào Python vì nhiều lý do. Python là một ngôn ngữ vô cùng hiệu quả: chương trình của bạn sẽ làm được nhiều việc hơn với ít dòng mã hơn so với nhiều ngôn ngữ khác. Cú pháp của Python cũng giúp bạn viết mã "sạch". So với các ngôn ngữ khác, mã của bạn sẽ dễ đọc, dễ gỡ lỗi, dễ mở rộng và phát triển thêm.

[[22]]
Người ta dùng Python cho rất nhiều mục đích: làm trò chơi, xây dựng ứng dụng web, giải quyết các bài toán kinh doanh và phát triển công cụ nội bộ tại đủ loại công ty thú vị. Python cũng được dùng rất nhiều trong các lĩnh vực khoa học, cho cả nghiên cứu học thuật lẫn công việc ứng dụng.

[[24]]
Một trong những lý do quan trọng nhất khiến tôi tiếp tục dùng Python là cộng đồng Python — một cộng đồng vô cùng đa dạng và cởi mở. Cộng đồng rất quan trọng đối với lập trình viên, vì lập trình không phải là công việc đơn độc. Hầu hết chúng ta, kể cả những lập trình viên giàu kinh nghiệm nhất, đều cần xin lời khuyên từ những người đã giải quyết các vấn đề tương tự. Có một cộng đồng gắn kết và sẵn lòng hỗ trợ là điều cực kỳ quan trọng giúp bạn giải quyết vấn đề, và cộng đồng Python luôn hết lòng hỗ trợ những người như bạn — những người đang học Python như ngôn ngữ lập trình đầu tiên.

[[25]]
Python là một ngôn ngữ tuyệt vời để học, vậy hãy bắt đầu thôi!

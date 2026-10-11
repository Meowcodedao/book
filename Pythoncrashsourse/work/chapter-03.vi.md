[[2]]
# Chương 3: Giới thiệu về list

[[4]]
Trong chương này và chương tiếp theo, bạn sẽ tìm hiểu list là gì và cách bắt đầu làm việc với các phần tử trong một list. List cho phép bạn lưu trữ các tập hợp thông tin ở một chỗ, dù bạn chỉ có vài phần tử hay hàng triệu phần tử. List là một trong những tính năng mạnh mẽ nhất của Python mà người mới lập trình có thể dễ dàng tiếp cận, và chúng kết nối nhiều khái niệm quan trọng trong lập trình.

[[5]]
## List là gì?

[[6]]
*List* là một tập hợp các phần tử được sắp xếp theo một thứ tự cụ thể. Bạn có thể tạo một list gồm các chữ cái trong bảng chữ cái, các chữ số từ 0–9, hoặc tên của tất cả mọi người trong gia đình bạn. Bạn có thể đặt bất cứ thứ gì vào một list, và các phần tử trong list không cần phải liên quan đến nhau theo bất kỳ cách cụ thể nào. Vì một list thường chứa nhiều hơn một phần tử, nên đặt tên list ở dạng số nhiều là một ý hay, chẳng hạn như `letters`, `digits` hoặc `names`.

[[8]]
Trong Python, cặp dấu ngoặc vuông (`[]`) biểu thị một list, và các phần tử riêng lẻ trong list được phân tách bằng dấu phẩy. Dưới đây là một ví dụ đơn giản về một list chứa vài loại xe đạp:

[[11]]
Nếu bạn yêu cầu Python in một list, Python sẽ trả về cách biểu diễn list đó, bao gồm cả cặp dấu ngoặc vuông:

[[13]]
Vì đây không phải là đầu ra bạn muốn người dùng nhìn thấy, hãy học cách truy cập từng phần tử riêng lẻ trong một list.

[[14]]
### Truy cập các phần tử trong list

[[15]]
List là những tập hợp có thứ tự, nên bạn có thể truy cập bất kỳ phần tử nào trong list bằng cách cho Python biết vị trí, hay *chỉ mục* (index), của phần tử mong muốn. Để truy cập một phần tử trong list, hãy viết tên list, theo sau là chỉ mục của phần tử đặt trong cặp dấu ngoặc vuông.

[[16]]
Ví dụ, hãy lấy ra chiếc xe đạp đầu tiên trong list `bicycles`:

[[18]]
Cú pháp để làm điều này được trình bày tại ❶. Khi chúng ta yêu cầu một phần tử duy nhất từ list, Python chỉ trả về phần tử đó, không kèm dấu ngoặc vuông hay dấu nháy:

[[20]]
Đây là kết quả bạn muốn người dùng nhìn thấy — đầu ra sạch sẽ, được định dạng gọn gàng.

[[21]]
Bạn cũng có thể dùng các phương thức chuỗi đã học ở Chương 2 trên bất kỳ phần tử nào trong list. Ví dụ, bạn có thể định dạng phần tử `'trek'` gọn gàng hơn bằng phương thức `title()`:

[[23]]
Ví dụ này cho ra đầu ra giống ví dụ trước, chỉ khác là `'Trek'` được viết hoa.

[[25]]
### Vị trí chỉ mục bắt đầu từ 0, không phải 1

[[26]]
Python coi phần tử đầu tiên trong list nằm ở vị trí 0, chứ không phải vị trí 1. Điều này đúng với hầu hết các ngôn ngữ lập trình, và lý do nằm ở cách các thao tác trên list được cài đặt ở tầng thấp hơn. Nếu bạn nhận được kết quả bất ngờ, hãy xem liệu mình có đang mắc lỗi lệch một đơn vị (off-by-one error) đơn giản hay không.

[[27]]
Phần tử thứ hai trong list có chỉ mục là 1. Với cách đếm đơn giản này, bạn có thể lấy bất kỳ phần tử nào bạn muốn từ list bằng cách lấy vị trí của nó trong list trừ đi một. Chẳng hạn, để truy cập phần tử thứ tư trong list, bạn yêu cầu phần tử ở chỉ mục 3.

[[28]]
Đoạn mã sau yêu cầu các xe đạp ở chỉ mục `1` và chỉ mục `3`:

[[30]]
Đoạn mã này trả về chiếc xe đạp thứ hai và thứ tư trong list:

[[32]]
Python có một cú pháp đặc biệt để truy cập phần tử cuối cùng trong list. Khi bạn yêu cầu phần tử ở chỉ mục `-1`, Python luôn trả về phần tử cuối cùng trong list:

[[34]]
Đoạn mã này trả về giá trị `'specialized'`. Cú pháp này khá hữu ích, vì bạn sẽ thường muốn truy cập những phần tử cuối cùng trong list mà không biết chính xác list dài bao nhiêu. Quy ước này cũng áp dụng cho các chỉ mục âm khác. Chỉ mục -`2` trả về phần tử thứ hai tính từ cuối list, chỉ mục -`3` trả về phần tử thứ ba tính từ cuối, và cứ thế tiếp tục.

[[35]]
### Sử dụng từng giá trị trong list

[[36]]
Bạn có thể dùng từng giá trị trong list giống như bất kỳ biến nào khác. Ví dụ, bạn có thể dùng phép nối chuỗi để tạo một thông điệp dựa trên một giá trị trong list.

[[37]]
Hãy thử lấy chiếc xe đạp đầu tiên từ list và tạo một thông điệp bằng giá trị đó.

[[40]]
Tại ❶, chúng ta xây dựng một câu bằng giá trị ở `bicycles[0]` và lưu nó vào biến `message`. Đầu ra là một câu đơn giản về chiếc xe đạp đầu tiên trong list:

[[43]]
**Tự mình thực hành**

[[44]]
Hãy thử những chương trình ngắn sau để có trải nghiệm trực tiếp với list của Python. Có thể bạn sẽ muốn tạo một thư mục mới cho bài tập của mỗi chương để giữ chúng ngăn nắp.

[[45]]
**3-1. Tên:** Lưu tên của một vài người bạn vào một list có tên `names`. In tên từng người bằng cách lần lượt truy cập từng phần tử trong list.

[[46]]
**3-2. Lời chào:** Bắt đầu với list bạn đã dùng trong Bài tập 3-1, nhưng thay vì chỉ in tên từng người, hãy in một thông điệp gửi tới họ. Nội dung các thông điệp nên giống nhau, nhưng mỗi thông điệp phải được cá nhân hóa bằng tên của người nhận.

[[47]]
**3-3. List của riêng bạn:** Hãy nghĩ về phương tiện đi lại yêu thích của bạn, chẳng hạn xe máy hoặc ô tô, và tạo một list lưu trữ vài ví dụ. Dùng list đó để in ra một loạt câu về các phần tử này, chẳng hạn như “I would like to own a Honda motorcycle.”

[[49]]
## Thay đổi, thêm và xóa phần tử

[[50]]
Hầu hết các list bạn tạo ra sẽ là list động, nghĩa là bạn sẽ xây dựng một list rồi thêm và xóa các phần tử khỏi nó trong quá trình chương trình chạy. Ví dụ, bạn có thể tạo một trò chơi trong đó người chơi phải bắn hạ những người ngoài hành tinh trên bầu trời. Bạn có thể lưu nhóm người ngoài hành tinh ban đầu trong một list, rồi xóa một người ngoài hành tinh khỏi list mỗi khi có một kẻ bị bắn hạ. Mỗi khi một người ngoài hành tinh mới xuất hiện trên màn hình, bạn thêm nó vào list. List người ngoài hành tinh của bạn sẽ ngắn đi và dài ra liên tục trong suốt trò chơi.

[[51]]
### Sửa đổi phần tử trong list

[[52]]
Cú pháp để sửa đổi một phần tử tương tự như cú pháp để truy cập một phần tử trong list. Để thay đổi một phần tử, hãy dùng tên list, theo sau là chỉ mục của phần tử bạn muốn thay đổi, rồi cung cấp giá trị mới mà bạn muốn phần tử đó có.

[[54]]
Ví dụ, giả sử chúng ta có một list xe máy, và phần tử đầu tiên trong list là `'honda'`. Làm thế nào để thay đổi giá trị của phần tử đầu tiên này?

[[57]]
Đoạn mã tại ❶ định nghĩa list ban đầu, với `'honda'` là phần tử đầu tiên. Đoạn mã tại ❷ thay đổi giá trị của phần tử đầu tiên thành `'ducati'`. Đầu ra cho thấy phần tử đầu tiên quả thực đã được thay đổi, còn phần còn lại của list vẫn giữ nguyên:

[[59]]
Bạn có thể thay đổi giá trị của bất kỳ phần tử nào trong list, không chỉ phần tử đầu tiên.

[[60]]
### Thêm phần tử vào list

[[61]]
Bạn có thể muốn thêm một phần tử mới vào list vì nhiều lý do. Ví dụ, bạn có thể muốn làm xuất hiện những người ngoài hành tinh mới trong trò chơi, thêm dữ liệu mới vào một biểu đồ trực quan, hoặc thêm người dùng mới đăng ký vào trang web bạn đã xây dựng. Python cung cấp một vài cách để thêm dữ liệu mới vào list có sẵn.

[[62]]
#### Nối phần tử vào cuối list

[[63]]
Cách đơn giản nhất để thêm một phần tử mới vào list là *nối* (append) phần tử đó vào list. Khi bạn nối một phần tử vào list, phần tử mới sẽ được thêm vào cuối list. Dùng chính list trong ví dụ trước, chúng ta sẽ thêm phần tử mới `'ducati'` vào cuối list:

[[65]]
Phương thức `append()` tại ❶ thêm `'ducati'` vào cuối list mà không ảnh hưởng đến bất kỳ phần tử nào khác trong list:

[[68]]
Phương thức `append()` giúp bạn dễ dàng xây dựng list một cách động. Ví dụ, bạn có thể bắt đầu với một list rỗng rồi thêm phần tử vào list bằng một loạt câu lệnh `append()`. Bắt đầu từ một list rỗng, hãy thêm các phần tử `'honda'`, `'yamaha'` và `'suzuki'` vào list:

[[70]]
List thu được trông giống hệt các list trong những ví dụ trước:

[[72]]
Xây dựng list theo cách này rất phổ biến, vì bạn thường không biết người dùng muốn lưu dữ liệu gì trong chương trình cho đến khi chương trình đang chạy. Để người dùng nắm quyền kiểm soát, hãy bắt đầu bằng cách định nghĩa một list rỗng để chứa các giá trị của người dùng. Sau đó nối từng giá trị mới được cung cấp vào list bạn vừa tạo.

[[73]]
#### Chèn phần tử vào list

[[74]]
Bạn có thể thêm một phần tử mới vào bất kỳ vị trí nào trong list bằng phương thức `insert()`. Bạn làm điều này bằng cách chỉ định chỉ mục và giá trị của phần tử mới.

[[76]]
Trong ví dụ này, đoạn mã tại ❶ chèn giá trị `'ducati'` vào đầu list. Phương thức `insert()` mở ra một chỗ trống ở vị trí `0` và lưu giá trị `'ducati'` vào vị trí đó. Thao tác này dịch mọi giá trị khác trong list sang phải một vị trí:

[[78]]
### Xóa phần tử khỏi list

[[79]]
Bạn sẽ thường muốn xóa một phần tử hoặc một nhóm phần tử khỏi list. Ví dụ, khi người chơi bắn hạ một người ngoài hành tinh trên bầu trời, nhiều khả năng bạn sẽ muốn xóa nó khỏi list những người ngoài hành tinh đang hoạt động. Hoặc khi người dùng quyết định hủy tài khoản trên một ứng dụng web bạn tạo ra, bạn sẽ muốn xóa người dùng đó khỏi list người dùng đang hoạt động. Bạn có thể xóa một phần tử theo vị trí của nó trong list hoặc theo giá trị của nó.

[[81]]
#### Xóa phần tử bằng câu lệnh del

[[82]]
Nếu bạn biết vị trí của phần tử muốn xóa khỏi list, bạn có thể dùng câu lệnh `del`.

[[84]]
Đoạn mã tại ❶ dùng `del` để xóa phần tử đầu tiên, `'honda'`, khỏi list xe máy:

[[86]]
Bạn có thể xóa một phần tử ở bất kỳ vị trí nào trong list bằng câu lệnh `del` nếu biết chỉ mục của nó. Ví dụ, đây là cách xóa phần tử thứ hai, `'yamaha'`, trong list:

[[88]]
Chiếc xe máy thứ hai bị xóa khỏi list:

[[90]]
Trong cả hai ví dụ, bạn không thể truy cập giá trị đã bị xóa khỏi list nữa sau khi dùng câu lệnh `del`.

[[91]]
#### Xóa phần tử bằng phương thức pop()

[[92]]
Đôi khi bạn sẽ muốn dùng giá trị của một phần tử sau khi xóa nó khỏi list. Ví dụ, bạn có thể muốn lấy vị trí *x* và *y* của một người ngoài hành tinh vừa bị bắn hạ để vẽ một vụ nổ tại vị trí đó. Trong một ứng dụng web, bạn có thể muốn xóa một người dùng khỏi list thành viên đang hoạt động rồi thêm người dùng đó vào list thành viên không hoạt động.

[[93]]
Phương thức `pop()` xóa phần tử cuối cùng trong list, nhưng cho phép bạn làm việc với phần tử đó sau khi xóa. Thuật ngữ *pop* xuất phát từ việc hình dung list như một chồng các phần tử và nhấc (pop) một phần tử ra khỏi đỉnh chồng. Trong phép so sánh này, đỉnh chồng tương ứng với cuối list.

[[95]]
Hãy pop một chiếc xe máy ra khỏi list xe máy:

[[97]]
Chúng ta bắt đầu bằng việc định nghĩa và in list `motorcycles` tại ❶. Tại ❷, chúng ta pop một giá trị ra khỏi list và lưu giá trị đó vào biến `popped_motorcycle`. Chúng ta in list tại ❸ để cho thấy một giá trị đã bị xóa khỏi list. Sau đó, chúng ta in giá trị vừa được pop tại ❹ để chứng minh rằng ta vẫn truy cập được giá trị đã bị xóa.

[[98]]
Đầu ra cho thấy giá trị `'suzuki'` đã bị xóa khỏi cuối list và giờ được lưu trong biến `popped_motorcycle`:

[[100]]
Phương thức `pop()` này có thể hữu ích như thế nào? Hãy tưởng tượng các xe máy trong list được lưu theo thứ tự thời gian mà chúng ta sở hữu chúng. Nếu vậy, chúng ta có thể dùng phương thức `pop()` để in ra một câu về chiếc xe máy mua gần đây nhất:

[[102]]
Đầu ra là một câu đơn giản về chiếc xe máy chúng ta sở hữu gần đây nhất:

[[104]]
#### Pop phần tử ở bất kỳ vị trí nào trong list

[[105]]
Thực ra, bạn có thể dùng `pop()` để xóa một phần tử ở bất kỳ vị trí nào trong list bằng cách đặt chỉ mục của phần tử muốn xóa vào trong cặp dấu ngoặc đơn.

[[108]]
Chúng ta bắt đầu bằng việc pop chiếc xe máy đầu tiên trong list tại ❶, rồi in một thông điệp về chiếc xe máy đó tại ❷. Đầu ra là một câu đơn giản mô tả chiếc xe máy đầu tiên tôi từng sở hữu:

[[110]]
Hãy nhớ rằng mỗi khi bạn dùng `pop()`, phần tử bạn làm việc cùng sẽ không còn được lưu trong list nữa.

[[111]]
Nếu bạn không chắc nên dùng câu lệnh `del` hay phương thức `pop()`, đây là một cách đơn giản để quyết định: khi bạn muốn xóa một phần tử khỏi list và không dùng phần tử đó vào việc gì, hãy dùng câu lệnh `del`; nếu bạn muốn dùng phần tử đó ngay khi xóa nó, hãy dùng phương thức `pop()`.

[[112]]
#### Xóa phần tử theo giá trị

[[113]]
Đôi khi bạn sẽ không biết vị trí của giá trị muốn xóa khỏi list. Nếu chỉ biết giá trị của phần tử muốn xóa, bạn có thể dùng phương thức `remove()`.

[[114]]
Ví dụ, giả sử chúng ta muốn xóa giá trị `'ducati'` khỏi list xe máy.

[[116]]
Đoạn mã tại ❶ yêu cầu Python tìm xem `'ducati'` xuất hiện ở đâu trong list và xóa phần tử đó:

[[118]]
Bạn cũng có thể dùng phương thức `remove()` để làm việc với một giá trị đang bị xóa khỏi list. Hãy xóa giá trị `'ducati'` và in ra lý do xóa nó khỏi list:

[[120]]
Sau khi định nghĩa list tại ❶, chúng ta lưu giá trị `'ducati'` vào một biến có tên `too_expensive` ❷. Sau đó, chúng ta dùng biến này để cho Python biết giá trị nào cần xóa khỏi list tại ❸. Tại ❹, giá trị `'ducati'` đã bị xóa khỏi list nhưng vẫn được lưu trong biến `too_expensive`, cho phép chúng ta in ra một câu giải thích lý do xóa `'ducati'` khỏi list xe máy:

[[123]]
> **Lưu ý** Phương thức `remove()` chỉ xóa lần xuất hiện đầu tiên của giá trị bạn chỉ định. Nếu có khả năng giá trị đó xuất hiện nhiều hơn một lần trong list, bạn sẽ cần dùng một vòng lặp để xác định xem mọi lần xuất hiện của giá trị đã bị xóa hết chưa. Bạn sẽ học cách làm điều này trong Chương 7.

[[125]]
**Tự mình thực hành**

[[126]]
Các bài tập sau phức tạp hơn một chút so với các bài tập trong Chương 2, nhưng chúng cho bạn cơ hội sử dụng list theo mọi cách đã được mô tả.

[[127]]
**3-4. Danh sách khách mời:** Nếu có thể mời bất kỳ ai, dù còn sống hay đã khuất, đến dự bữa tối, bạn sẽ mời ai? Hãy tạo một list gồm ít nhất ba người bạn muốn mời đến dự bữa tối. Sau đó dùng list đó để in ra một thông điệp gửi tới từng người, mời họ đến dự bữa tối.

[[128]]
**3-5. Thay đổi danh sách khách mời:** Bạn vừa nghe tin một vị khách không thể đến dự bữa tối, nên bạn cần gửi một loạt lời mời mới. Bạn sẽ phải nghĩ ra một người khác để mời.

[[129]]
- Bắt đầu với chương trình của bạn từ Bài tập 3-4. Thêm một câu lệnh `print` vào cuối chương trình, nêu tên vị khách không thể đến.

[[130]]
- Sửa list của bạn, thay tên của vị khách không thể đến bằng tên của người mới mà bạn đang mời.

[[131]]
- In loạt thông điệp mời thứ hai, mỗi thông điệp cho một người vẫn còn trong list.

[[132]]
**3-6. Thêm khách:** Bạn vừa tìm được một chiếc bàn ăn lớn hơn, nên giờ đã có thêm chỗ. Hãy nghĩ thêm ba vị khách nữa để mời đến dự bữa tối.

[[133]]
- Bắt đầu với chương trình của bạn từ Bài tập 3-4 hoặc Bài tập 3-5. Thêm một câu lệnh `print` vào cuối chương trình để thông báo với mọi người rằng bạn đã tìm được một chiếc bàn ăn lớn hơn.

[[134]]
- Dùng `insert()` để thêm một vị khách mới vào đầu list.

[[135]]
- Dùng `insert()` để thêm một vị khách mới vào giữa list.

[[136]]
- Dùng `append()` để thêm một vị khách mới vào cuối list.

[[137]]
- In một loạt thông điệp mời mới, mỗi thông điệp cho một người trong list.

[[139]]
**3-7. Thu hẹp danh sách khách mời:** Bạn vừa biết rằng chiếc bàn ăn mới sẽ không đến kịp cho bữa tối, và bạn chỉ còn chỗ cho hai vị khách.

[[140]]
- Bắt đầu với chương trình của bạn từ Bài tập 3-6. Thêm một dòng mới in ra thông điệp cho biết bạn chỉ có thể mời hai người đến dự bữa tối.

[[141]]
- Dùng `pop()` để lần lượt xóa từng vị khách khỏi list cho đến khi trong list chỉ còn hai cái tên. Mỗi lần pop một cái tên ra khỏi list, hãy in một thông điệp gửi tới người đó, cho họ biết bạn rất tiếc vì không thể mời họ đến dự bữa tối.

[[142]]
- In một thông điệp gửi tới từng người trong hai người vẫn còn trong list, cho họ biết họ vẫn được mời.

[[143]]
- Dùng `del` để xóa hai cái tên cuối cùng khỏi list, để bạn có một list rỗng. In list ra để đảm bảo rằng bạn thực sự có một list rỗng ở cuối chương trình.

[[145]]
## Sắp xếp list

[[146]]
Các list của bạn thường sẽ được tạo ra theo một thứ tự khó đoán trước, vì không phải lúc nào bạn cũng kiểm soát được thứ tự mà người dùng cung cấp dữ liệu. Dù điều này khó tránh khỏi trong hầu hết các tình huống, bạn sẽ thường muốn trình bày thông tin theo một thứ tự cụ thể. Đôi khi bạn sẽ muốn giữ nguyên thứ tự ban đầu của list, và những lúc khác bạn lại muốn thay đổi thứ tự ban đầu. Python cung cấp nhiều cách khác nhau để sắp xếp list, tùy theo tình huống.

[[147]]
### Sắp xếp list vĩnh viễn bằng phương thức sort()

[[148]]
Phương thức `sort()` của Python giúp việc sắp xếp list trở nên tương đối dễ dàng. Hãy tưởng tượng chúng ta có một list ô tô và muốn thay đổi thứ tự của list để lưu chúng theo thứ tự bảng chữ cái. Để giữ cho công việc đơn giản, hãy giả sử rằng mọi giá trị trong list đều là chữ thường.

[[151]]
Phương thức `sort()`, như tại ❶, thay đổi thứ tự của list một cách vĩnh viễn. Các ô tô giờ được xếp theo thứ tự bảng chữ cái, và chúng ta không bao giờ có thể quay lại thứ tự ban đầu:

[[154]]
Bạn cũng có thể sắp xếp list này theo thứ tự bảng chữ cái đảo ngược bằng cách truyền đối số `reverse=True` cho phương thức `sort()`. Ví dụ sau sắp xếp list ô tô theo thứ tự bảng chữ cái đảo ngược:

[[156]]
Một lần nữa, thứ tự của list bị thay đổi vĩnh viễn:

[[158]]
### Sắp xếp list tạm thời bằng hàm sorted()

[[159]]
Để giữ nguyên thứ tự ban đầu của list nhưng vẫn trình bày nó theo thứ tự đã sắp xếp, bạn có thể dùng hàm `sorted()`. Hàm `sorted()` cho phép bạn hiển thị list theo một thứ tự cụ thể nhưng không ảnh hưởng đến thứ tự thực sự của list.

[[160]]
Hãy thử hàm này trên list ô tô.

[[162]]
Đầu tiên, chúng ta in list theo thứ tự ban đầu tại ❶, rồi theo thứ tự bảng chữ cái tại ❷. Sau khi list được hiển thị theo thứ tự mới, chúng ta cho thấy list vẫn được lưu theo thứ tự ban đầu tại ❸.

[[164]]
Hãy để ý rằng list vẫn giữ thứ tự ban đầu tại ❹ sau khi hàm `sorted()` được sử dụng. Hàm `sorted()` cũng có thể nhận đối số `reverse=True` nếu bạn muốn hiển thị list theo thứ tự bảng chữ cái đảo ngược.

[[166]]
> **Lưu ý** Sắp xếp list theo bảng chữ cái phức tạp hơn một chút khi không phải mọi giá trị đều là chữ thường. Có nhiều cách để xử lý chữ hoa khi quyết định thứ tự sắp xếp, và việc chỉ định chính xác thứ tự có thể phức tạp hơn mức chúng ta muốn xử lý lúc này. Tuy nhiên, hầu hết các cách sắp xếp đều xây dựng trực tiếp trên những gì bạn đã học trong phần này.

[[167]]
### In list theo thứ tự đảo ngược

[[168]]
Để đảo ngược thứ tự ban đầu của list, bạn có thể dùng phương thức `reverse()`. Nếu ban đầu chúng ta lưu list ô tô theo thứ tự thời gian mà chúng ta sở hữu chúng, ta có thể dễ dàng sắp xếp lại list theo thứ tự thời gian đảo ngược:

[[170]]
Hãy để ý rằng `reverse()` không sắp xếp ngược theo bảng chữ cái; nó chỉ đơn giản đảo ngược thứ tự của list:

[[172]]
Phương thức `reverse()` thay đổi thứ tự của list một cách vĩnh viễn, nhưng bạn có thể quay lại thứ tự ban đầu bất cứ lúc nào bằng cách áp dụng `reverse()` lên cùng list đó lần thứ hai.

[[173]]
### Tìm độ dài của list

[[174]]
Bạn có thể nhanh chóng tìm độ dài của list bằng hàm `len()`. List trong ví dụ này có bốn phần tử, nên độ dài của nó là `4`:

[[176]]
Bạn sẽ thấy `len()` hữu ích khi cần xác định số người ngoài hành tinh còn phải bắn hạ trong một trò chơi, xác định lượng dữ liệu cần quản lý trong một biểu đồ trực quan, hoặc tính số người dùng đã đăng ký trên một trang web, cùng nhiều việc khác.

[[177]]
> **Lưu ý** Python đếm các phần tử trong list bắt đầu từ một, nên bạn sẽ không gặp lỗi lệch một đơn vị khi xác định độ dài của list.

[[180]]
**Tự mình thực hành**

[[181]]
**3-8. Ngắm nhìn thế giới:** Hãy nghĩ ra ít nhất năm nơi trên thế giới mà bạn muốn đến thăm.

[[182]]
- Lưu các địa điểm đó vào một list. Hãy đảm bảo list không theo thứ tự bảng chữ cái.

[[183]]
- In list theo thứ tự ban đầu. Đừng bận tâm việc in list cho đẹp, chỉ cần in nó ra dưới dạng một list Python thô.

[[184]]
- Dùng `sorted()` để in list theo thứ tự bảng chữ cái mà không sửa đổi list thực sự.

[[185]]
- Cho thấy list vẫn giữ thứ tự ban đầu bằng cách in nó ra.

[[186]]
- Dùng `sorted()` để in list theo thứ tự bảng chữ cái đảo ngược mà không thay đổi thứ tự của list ban đầu.

[[187]]
- Cho thấy list vẫn giữ thứ tự ban đầu bằng cách in nó ra một lần nữa.

[[188]]
- Dùng `reverse()` để thay đổi thứ tự của list. In list ra để cho thấy thứ tự của nó đã thay đổi.

[[189]]
- Dùng `reverse()` để thay đổi thứ tự của list một lần nữa. In list ra để cho thấy nó đã trở về thứ tự ban đầu.

[[190]]
- Dùng `sort()` để thay đổi list sao cho nó được lưu theo thứ tự bảng chữ cái. In list ra để cho thấy thứ tự của nó đã được thay đổi.

[[191]]
- Dùng `sort()` để thay đổi list sao cho nó được lưu theo thứ tự bảng chữ cái đảo ngược. In list ra để cho thấy thứ tự của nó đã thay đổi.

[[192]]
**3-9. Khách dự tiệc tối:** Dựa trên một trong các chương trình từ Bài tập 3-4 đến 3-7 (trang 46), dùng `len()` để in ra một thông điệp cho biết số người bạn đang mời đến dự bữa tối.

[[193]]
**3-10. Mọi hàm:** Hãy nghĩ về một thứ gì đó bạn có thể lưu trong list. Ví dụ, bạn có thể tạo một list các ngọn núi, dòng sông, quốc gia, thành phố, ngôn ngữ hoặc bất cứ thứ gì bạn thích. Viết một chương trình tạo một list chứa các phần tử này, rồi dùng mỗi hàm được giới thiệu trong chương này ít nhất một lần.

[[195]]
## Tránh lỗi chỉ mục khi làm việc với list

[[196]]
Có một loại lỗi thường gặp khi bạn làm việc với list lần đầu. Giả sử bạn có một list gồm ba phần tử và bạn yêu cầu phần tử thứ tư:

[[199]]
Ví dụ này gây ra một *lỗi chỉ mục* (index error):

[[201]]
Python cố gắng trả về cho bạn phần tử ở chỉ mục 3. Nhưng khi tìm trong list, không có phần tử nào trong `motorcycles` có chỉ mục 3. Do bản chất lệch một đơn vị của việc đánh chỉ mục trong list, lỗi này rất điển hình. Mọi người nghĩ phần tử thứ ba là phần tử số 3, vì họ bắt đầu đếm từ 1. Nhưng trong Python, phần tử thứ ba là số 2, vì Python bắt đầu đánh chỉ mục từ 0.

[[202]]
Lỗi chỉ mục nghĩa là Python không thể tìm ra chỉ mục mà bạn yêu cầu. Nếu chương trình của bạn gặp lỗi chỉ mục, hãy thử điều chỉnh chỉ mục bạn yêu cầu đi một đơn vị. Sau đó chạy lại chương trình để xem kết quả có đúng không.

[[203]]
Hãy nhớ rằng bất cứ khi nào muốn truy cập phần tử cuối cùng trong list, bạn dùng chỉ mục `-1`. Cách này luôn hoạt động, ngay cả khi kích thước list đã thay đổi kể từ lần cuối bạn truy cập nó:

[[205]]
Chỉ mục `-1` luôn trả về phần tử cuối cùng trong list, trong trường hợp này là giá trị `'suzuki'`:

[[207]]
Trường hợp duy nhất cách này gây ra lỗi là khi bạn yêu cầu phần tử cuối cùng từ một list rỗng:

[[209]]
Không có phần tử nào trong `motorcycles`, nên Python trả về một lỗi chỉ mục khác:

[[211]]
> **Lưu ý** Nếu xảy ra lỗi chỉ mục mà bạn không biết cách giải quyết, hãy thử in list ra hoặc chỉ in độ dài của list. List của bạn có thể trông khác nhiều so với bạn nghĩ, đặc biệt nếu nó được chương trình quản lý một cách động. Việc nhìn thấy list thực tế, hoặc chính xác số phần tử trong list, có thể giúp bạn gỡ rối những lỗi logic như vậy.

[[214]]
**Tự mình thực hành**

[[215]]
**3-11. Lỗi cố ý:** Nếu bạn chưa gặp lỗi chỉ mục nào trong các chương trình của mình, hãy thử tạo ra một lỗi. Thay đổi một chỉ mục trong một chương trình của bạn để tạo ra lỗi chỉ mục. Nhớ sửa lỗi trước khi đóng chương trình.

[[217]]
## Tổng kết

[[218]]
Trong chương này, bạn đã biết list là gì và cách làm việc với từng phần tử trong list. Bạn đã học cách định nghĩa một list, cách thêm và xóa phần tử. Bạn đã học cách sắp xếp list vĩnh viễn và sắp xếp tạm thời để hiển thị. Bạn cũng đã học cách tìm độ dài của list và cách tránh lỗi chỉ mục khi làm việc với list.

[[219]]
Trong Chương 4, bạn sẽ học cách làm việc với các phần tử trong list hiệu quả hơn. Bằng cách lặp qua từng phần tử trong list chỉ với vài dòng mã, bạn sẽ có thể làm việc hiệu quả, ngay cả khi list của bạn chứa hàng nghìn hoặc hàng triệu phần tử.

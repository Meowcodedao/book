[[145]]
## Tái cấu trúc: module game_functions

[[146]]
Trong những dự án lớn hơn, bạn sẽ thường tái cấu trúc đoạn mã đã viết trước khi thêm mã mới. *Tái cấu trúc* (refactoring) đơn giản hóa cấu trúc của đoạn mã bạn đã viết, giúp việc phát triển tiếp trên đó dễ dàng hơn. Trong mục này, chúng ta sẽ tạo một module mới có tên `game_functions`, lưu một số hàm giúp Alien Invasion hoạt động. Module `game_functions` sẽ ngăn *alien_invasion.py* trở nên quá dài và giúp logic trong *alien_invasion.py* dễ theo dõi hơn.

[[147]]
### Hàm check_events()

[[148]]
Chúng ta sẽ bắt đầu bằng việc chuyển đoạn mã quản lý sự kiện sang một hàm riêng có tên `check_events()`. Điều này sẽ đơn giản hóa `run_game()` và tách riêng vòng lặp quản lý sự kiện. Tách riêng vòng lặp sự kiện cho phép bạn quản lý sự kiện độc lập với những khía cạnh khác của trò chơi, chẳng hạn việc cập nhật màn hình.

[[149]]
Đặt `check_events()` vào một module riêng có tên `game_functions`:

[[153]]
Module này import `sys` và `pygame`, được dùng trong vòng lặp kiểm tra sự kiện. Hiện tại hàm không cần tham số nào, và phần thân hàm được sao chép từ vòng lặp sự kiện trong *alien_invasion.py*.

[[154]]
Giờ hãy sửa *alien_invasion.py* để nó import module `game_functions`, và chúng ta sẽ thay vòng lặp sự kiện bằng một lời gọi `check_events()`:

[[157]]
Chúng ta không còn cần import `sys` trực tiếp vào file chương trình chính nữa, vì giờ nó chỉ được dùng trong module `game_functions`. Ta đặt cho module `game_functions` được import bí danh `gf` cho đơn giản.

[[158]]
### Hàm update_screen()

[[159]]
Hãy chuyển đoạn mã cập nhật màn hình sang một hàm riêng có tên `update_screen()` trong *game_functions.py* để đơn giản hóa `run_game()` hơn nữa:

[[162]]
Hàm mới `update_screen()` nhận ba tham số: `ai_settings`, `screen` và `ship`. Giờ chúng ta cần cập nhật vòng lặp `while` trong *alien_invasion.py* bằng một lời gọi `update_screen()`:

[[166]]
Hai hàm này giúp vòng lặp `while` đơn giản hơn và sẽ giúp việc phát triển tiếp theo dễ dàng hơn. Thay vì làm việc bên trong `run_game()`, giờ ta có thể làm phần lớn công việc trong module `game_functions`.

[[167]]
Vì muốn bắt đầu làm việc với mã trong một file duy nhất, chúng ta đã không giới thiệu module `game_functions` ngay từ đầu. Cách tiếp cận này cho bạn ý niệm về một quy trình phát triển thực tế: bạn bắt đầu viết mã đơn giản nhất có thể, rồi tái cấu trúc nó khi dự án trở nên phức tạp hơn.

[[168]]
Giờ đây khi mã đã được tái cấu trúc để dễ thêm vào hơn, chúng ta có thể làm việc với những khía cạnh động của trò chơi!

[[170]]
**Tự mình thực hành**

[[171]]
**12-1. Bầu trời xanh:** Tạo một cửa sổ Pygame với nền màu xanh dương.

[[172]]
**12-2. Nhân vật trò chơi:** Tìm một hình ảnh bitmap của một nhân vật trò chơi bạn thích, hoặc chuyển một hình ảnh sang bitmap. Tạo một lớp vẽ nhân vật đó ở giữa màn hình, và chỉnh màu nền của hình ảnh cho khớp với màu nền của màn hình, hoặc ngược lại.

[[174]]
## Điều khiển con tàu

[[175]]
Hãy cho người chơi khả năng di chuyển con tàu sang phải và sang trái. Để làm điều này, chúng ta sẽ viết mã phản hồi khi người chơi nhấn phím mũi tên phải hoặc trái. Trước tiên, ta sẽ tập trung vào việc di chuyển sang phải, rồi áp dụng cùng nguyên tắc để điều khiển việc di chuyển sang trái. Khi làm điều này, bạn sẽ học cách điều khiển chuyển động của hình ảnh trên màn hình.

[[176]]
### Phản hồi một lần nhấn phím

[[177]]
Bất cứ khi nào người chơi nhấn một phím, lần nhấn phím đó được ghi nhận trong Pygame như một sự kiện. Mỗi sự kiện được phương thức `pygame.event.get()` thu nhận, nên chúng ta cần chỉ định trong hàm `check_events()` loại sự kiện nào cần kiểm tra. Mỗi lần nhấn phím được ghi nhận là một sự kiện `KEYDOWN`.

[[178]]
Khi phát hiện một sự kiện `KEYDOWN`, chúng ta cần kiểm tra xem phím được nhấn có phải là phím kích hoạt một sự kiện nào đó không. Ví dụ, nếu phím mũi tên phải được nhấn, ta tăng giá trị `rect.centerx` của con tàu để di chuyển con tàu sang phải:

[[182]]
Chúng ta cho hàm `check_events()` một tham số `ship`, vì con tàu cần di chuyển sang phải khi phím mũi tên phải được nhấn. Bên trong `check_events()`, ta thêm một khối `elif` vào vòng lặp sự kiện để phản hồi khi Pygame phát hiện một sự kiện `KEYDOWN` ❶. Ta kiểm tra xem phím được nhấn có phải là phím mũi tên phải (`pygame.K_RIGHT`) hay không bằng cách đọc thuộc tính `event.key` ❷. Nếu phím mũi tên phải được nhấn, ta di chuyển con tàu sang phải bằng cách tăng giá trị của `ship.rect.centerx` thêm 1 ❸.

[[183]]
Chúng ta cần cập nhật lời gọi `check_events()` trong *alien_invasion.py* để nó truyền `ship` làm đối số:

[[186]]
Nếu chạy *alien_invasion.py* lúc này, bạn sẽ thấy con tàu di chuyển sang phải một pixel mỗi khi bạn nhấn phím mũi tên phải. Đó là một khởi đầu, nhưng không phải là cách hiệu quả để điều khiển con tàu. Hãy cải thiện cách điều khiển này bằng cách cho phép chuyển động liên tục.

[[187]]
### Cho phép chuyển động liên tục

[[188]]
Khi người chơi giữ phím mũi tên phải, chúng ta muốn con tàu tiếp tục di chuyển sang phải cho đến khi người chơi nhả phím. Ta sẽ cho trò chơi phát hiện sự kiện `pygame.KEYUP` để biết khi nào phím mũi tên phải được nhả ra; sau đó, ta sẽ dùng các sự kiện `KEYDOWN` và `KEYUP` cùng với một cờ có tên `moving_right` để thực hiện chuyển động liên tục.

[[189]]
Khi con tàu đứng yên, cờ `moving_right` sẽ là `False`. Khi phím mũi tên phải được nhấn, ta sẽ đặt cờ thành `True`, và khi phím được nhả ra, ta sẽ đặt lại cờ thành `False`.

[[190]]
Lớp `Ship` kiểm soát tất cả các thuộc tính của con tàu, nên chúng ta sẽ cho nó một thuộc tính có tên `moving_right` và một phương thức `update()` để kiểm tra trạng thái của cờ `moving_right`. Phương thức `update()` sẽ thay đổi vị trí của con tàu nếu cờ được đặt là `True`. Ta sẽ gọi phương thức này bất cứ khi nào muốn cập nhật vị trí của con tàu.

[[192]]
Đây là những thay đổi đối với lớp `Ship`:

[[195]]
Chúng ta thêm một thuộc tính `self.moving_right` vào phương thức `__init__()` và ban đầu đặt nó là `False` ❶. Sau đó, ta thêm `update()`, phương thức di chuyển con tàu sang phải nếu cờ là `True` ❷.

[[196]]
Giờ hãy sửa `check_events()` sao cho `moving_right` được đặt thành `True` khi phím mũi tên phải được nhấn và thành `False` khi phím được nhả ra:

[[199]]
Tại ❶, chúng ta sửa cách trò chơi phản hồi khi người chơi nhấn phím mũi tên phải: thay vì thay đổi trực tiếp vị trí của con tàu, ta chỉ đặt `moving_right` thành `True`. Tại ❷, ta thêm một khối `elif` mới phản hồi các sự kiện `KEYUP`. Khi người chơi nhả phím mũi tên phải (`K_RIGHT`), ta đặt `moving_right` thành `False`.

[[200]]
Cuối cùng, chúng ta sửa vòng lặp `while` trong *alien_invasion.py* để nó gọi phương thức `update()` của con tàu ở mỗi lượt lặp:

[[204]]
Vị trí của con tàu sẽ được cập nhật sau khi chúng ta kiểm tra các sự kiện bàn phím và trước khi cập nhật màn hình. Điều này cho phép vị trí của con tàu được cập nhật theo đầu vào của người chơi, và đảm bảo vị trí đã cập nhật được dùng khi vẽ con tàu lên màn hình.

[[205]]
Khi chạy *alien_invasion.py* và giữ phím mũi tên phải, con tàu sẽ di chuyển liên tục sang phải cho đến khi bạn nhả phím.

[[206]]
### Di chuyển cả sang trái lẫn sang phải

[[207]]
Giờ khi con tàu đã có thể di chuyển liên tục sang phải, việc thêm chuyển động sang trái rất dễ dàng. Chúng ta sẽ lại sửa lớp `Ship` và hàm `check_events()`. Đây là những thay đổi liên quan đối với `__init__()` và `update()` trong `Ship`:

[[210]]
Trong `__init__()`, chúng ta thêm một cờ `self.moving_left`. Trong `update()`, ta dùng hai khối `if` riêng biệt thay vì một khối `elif`, để giá trị `rect.centerx` của con tàu được tăng rồi lại giảm nếu cả hai phím mũi tên đều được giữ. Kết quả là con tàu đứng yên. Nếu dùng `elif` cho chuyển động sang trái, phím mũi tên phải sẽ luôn được ưu tiên. Làm theo cách này giúp chuyển động chính xác hơn khi chuyển từ trái sang phải, lúc người chơi có thể giữ cả hai phím trong chốc lát.

[[211]]
Chúng ta phải thực hiện hai điều chỉnh đối với `check_events()`:

[[215]]
Nếu một sự kiện `KEYDOWN` xảy ra với phím `K_LEFT`, chúng ta đặt `moving_left` thành `True`. Nếu một sự kiện `KEYUP` xảy ra với phím `K_LEFT`, ta đặt `moving_left` thành `False`. Ta có thể dùng các khối `elif` ở đây vì mỗi sự kiện chỉ gắn với một phím. Nếu người chơi nhấn cả hai phím cùng lúc, hai sự kiện riêng biệt sẽ được phát hiện.

[[216]]
Nếu chạy *alien_invasion.py* lúc này, bạn sẽ có thể di chuyển con tàu liên tục sang phải và sang trái. Nếu giữ cả hai phím, con tàu sẽ ngừng di chuyển.

[[217]]
Tiếp theo, chúng ta sẽ tinh chỉnh thêm chuyển động của con tàu. Hãy điều chỉnh tốc độ của con tàu và giới hạn phạm vi con tàu có thể di chuyển để nó không biến mất khỏi hai bên màn hình.

[[218]]
### Điều chỉnh tốc độ của con tàu

[[219]]
Hiện tại, con tàu di chuyển một pixel mỗi chu kỳ của vòng lặp `while`, nhưng chúng ta có thể kiểm soát tốc độ của con tàu tinh tế hơn bằng cách thêm một thuộc tính `ship_speed_factor` vào lớp `Settings`. Ta sẽ dùng thuộc tính này để xác định con tàu di chuyển bao xa ở mỗi lượt lặp. Đây là thuộc tính mới trong *settings.py*:

[[222]]
Chúng ta đặt giá trị ban đầu của `ship_speed_factor` là `1.5`. Khi muốn di chuyển con tàu, ta sẽ điều chỉnh vị trí của nó 1,5 pixel thay vì 1 pixel.

[[223]]
Chúng ta dùng giá trị thập phân cho thiết lập tốc độ để kiểm soát tốc độ của con tàu tinh tế hơn khi tăng nhịp độ của trò chơi về sau. Tuy nhiên, các thuộc tính của rect như `centerx` chỉ lưu giá trị số nguyên, nên ta cần thực hiện một số sửa đổi đối với `Ship`:

[[227]]
Tại ❶, chúng ta thêm `ai_settings` vào danh sách tham số của `__init__()`, để con tàu có thể truy cập thiết lập tốc độ của nó. Sau đó, ta biến tham số `ai_settings` thành một thuộc tính, để có thể dùng nó trong `update()` ❷. Giờ khi đang điều chỉnh vị trí của con tàu theo những phần lẻ của một pixel, ta cần lưu vị trí trong một biến có thể lưu giá trị thập phân. Bạn có thể dùng một giá trị thập phân để đặt thuộc tính của `rect`, nhưng `rect` sẽ chỉ lưu phần nguyên của giá trị đó. Để lưu chính xác vị trí của con tàu, ta định nghĩa một thuộc tính mới `self.center`, có thể chứa giá trị thập phân ❸. Ta dùng hàm `float()` để chuyển giá trị của `self.rect.centerx` thành số thập phân và lưu giá trị này vào `self.center`.

[[228]]
Giờ khi thay đổi vị trí của con tàu trong `update()`, giá trị của `self.center` được điều chỉnh theo lượng được lưu trong `ai_settings.ship_speed_factor` ❹. Sau khi `self.center` được cập nhật, ta dùng giá trị mới để cập nhật `self.rect.centerx`, thuộc tính kiểm soát vị trí của con tàu ❺. Chỉ phần nguyên của `self.center` mới được lưu vào `self.rect.centerx`, nhưng như vậy là đủ để hiển thị con tàu.

[[229]]
Chúng ta cần truyền `ai_settings` làm đối số khi tạo một thực thể của `Ship` trong *alien_invasion.py*:

[[232]]
Giờ bất kỳ giá trị `ship_speed_factor` nào lớn hơn một cũng sẽ khiến con tàu di chuyển nhanh hơn. Điều này sẽ giúp con tàu phản hồi đủ nhanh để bắn hạ người ngoài hành tinh, và cho phép ta thay đổi nhịp độ của trò chơi khi người chơi tiến bộ.

[[234]]
### Giới hạn phạm vi di chuyển của con tàu

[[235]]
Ở thời điểm này, con tàu sẽ biến mất khỏi một trong hai cạnh màn hình nếu bạn giữ phím mũi tên đủ lâu. Hãy sửa điều này để con tàu ngừng di chuyển khi chạm tới cạnh màn hình. Chúng ta làm điều này bằng cách sửa phương thức `update()` trong `Ship`:

[[238]]
Đoạn mã này kiểm tra vị trí của con tàu trước khi thay đổi giá trị của `self.center`. Đoạn mã `self.rect.right` trả về giá trị tọa độ x của cạnh phải của `rect` con tàu. Nếu giá trị này nhỏ hơn giá trị do `self.screen_rect.right` trả về, con tàu chưa chạm tới cạnh phải của màn hình ❶. Tương tự với cạnh trái: nếu giá trị cạnh trái của `rect` lớn hơn không, con tàu chưa chạm tới cạnh trái của màn hình ❷. Điều này đảm bảo con tàu nằm trong các giới hạn này trước khi điều chỉnh giá trị của `self.center`.

[[239]]
Nếu chạy *alien_invasion.py* lúc này, con tàu sẽ ngừng di chuyển ở cả hai cạnh màn hình.

[[240]]
### Tái cấu trúc check_events()

[[241]]
Hàm `check_events()` sẽ ngày càng dài khi chúng ta tiếp tục phát triển trò chơi, vậy hãy tách `check_events()` thành hai hàm nữa: một hàm xử lý các sự kiện `KEYDOWN` và một hàm khác xử lý các sự kiện `KEYUP`:

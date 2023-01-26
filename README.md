Một vài thông tin để bạn có thể hiểu hơn về project của tôi.

- Vì sao có project này? Do gia đình của tôi có một nhà nghỉ, đợt hè tôi phải về nhà để quản lý nhà nghỉ của gia đình, tôi thấy một công việc cứ lặp đi lặp lại đó là tính tiền ở bộ phận lễ tân, nhưng lại tính thủ công và đôi khi khách hàng phải chờ đợi từ 1-5 phút.

Do đó tôi đã nãy ra ý tưởng cho project này ^-^

- Cách sử dụng? Bạn chỉ cần cài đặt python và chạy cmd trong folder của project rồi cài đặt thư viện bằng các câu lệnh sau:

pip install sqlite3 prettytable
pip install -r requirements.txt
python -m pip install sqlite3 prettytable

Dưới đây là cách tôi lên ý tưởng cũng như cách giải quyết cho các chức năng có trong chương trình

Viết menu:
- Thêm phòng
- Cập nhật thông tin phòng
- Thanh toán
- Xem tất cả các phòng
- Xem phòng trống
- Thoát khỏi chương trình
Sau đây là cách giải các hàm trên
1. Thêm phòng:
- Yêu cầu người dùng nhập các thông tin sau: 
+ Số phòng (chỉ nhập được các phòng: 02,03,04,07,08,09 nếu người dùng nhập dữ liệu khác thì báo lỗi và yêu cầu nhập lại)
+ Thời gian nhận phòng (định dạng nhập là: HH:mm, ví dụ: 01:00, nếu người dùng nhập sai định dạng giờ, yêu cầu người dùng nhập lại)
+ Loại phòng (chỉ nhập ML hoặc Q, nếu người dùng nhập dữ liệu khác thì báo lỗi và yêu cầu nhập lại)
+ Thêm nước uống ( hỏi người dùng là có muốn sử dùng nước không? nếu có thì nhập Y còn nếu không thì nhập N)
Nếu người dùng có sử dụng nước thì yêu cầu nhập thêm các thông tin như sau:
+ Loại nước ( chỉ được nhập NN hoặc NS nếu người dùng nhập dữ liệu khác thì báo lỗi và yêu cầu nhập lại)
+ Số lượng ( biết rằng 1 NN có giá là 15, 1 NS có giá là 5 )
Các thông tin trên cần được lưu trữ trong cơ sở dữ liệu (viết lệnh tạo đường dẫn đến cơ sở dữ liệu).

2. Cập nhật thông tin phòng:
- Yêu cầu user nhập vào: 
+ số phòng
Sau đó dựa trên dữ liệu đã nhập ở chức năng thêm phòng, cho phép người dùng cập nhật tất cả thông tin của phòng đó

3. Thanh toán: 
+ yêu cầu người dùng nhập số phòng (thông tin dựa trên cơ sở dữ liệu)
+ giờ trả phòng

Sau khi người dùng nhập, tính toán số tiền bằng thuật toán sau:

Đầu tiên lấy giờ trả phòng - Thời gian nhận phòng sau đó quy đổi ra phút rồi tính như sau:

Nếu loại phòng là Q và số phút là từ 1 đến 60, thì giá sẽ là 70

Nếu loại phòng là Q và số phút từ 60 đến 120, thì giá sẽ là 80

Nếu loại phòng là Q và số phút từ 120 đến 180 thì giá sẽ là 90

Nếu loại phòng là Q và số phút từ 180 đến 240 thì giá sẽ là 110

Nếu loại phòng là Q và số phút từ 240 đến 300 thì giá sẽ là 120

Nếu loại phòng là Q và số phút là từ 300 đến 360 thì giá sẽ là 140

Nếu loại phòng là ML và số phút là từ 1 đến 60 thì giá sẽ là 90

Nếu loại phòng là ML và số phút từ 60 đến 120 thì giá sẽ là 100

Nếu loại phòng là ML và số phút từ 120 đến 180thì giá sẽ là 110

Nếu loại phòng là ML và số phút từ 180 đến 240 thì giá sẽ là 120

Nếu loại phòng là ML và số phút từ 240 đến 300 thì giá sẽ là 140

Nếu loại phòng là ML và số phút là từ 300 đến 360 thì giá sẽ là 160

Sau đó cộng giá phòng và nước lại với nhau rồi in tổng tiền ra màn hình

Sau khi thanh toán thành công, xoá phòng đó khỏi databse

4. Xem tất cả các phòng đã thêm:
Để người dùng xem được toàn bộ thông tin của các phòng đã được thêm vào dựa trên cơ sở dữ liệu, hãy trình bày dưới dạng bảng

5. Xem phòng trống:
Dựa vào cơ sở dữ liệu, nếu phòng không tồn tại trong cơ sở dữ liệu thì phòng sẽ hiển thị màn hình như ví dụ sau:
“Các phòng còn trống là:…”

Một vài thông tin để bạn có thể hiểu hơn về project của tôi.

- Vì sao có project này? Do gia đình của tôi có một nhà nghỉ, đợt hè tôi phải về nhà để quản lý nhà nghỉ của gia đình, tôi thấy một công việc cứ lặp đi lặp lại đó là tính tiền ở bộ phận lễ tân, nhưng lại tính thủ công và đôi khi khách hàng phải chờ đợi từ 1-5 phút.

Do đó tôi đã nãy ra ý tưởng cho project này ^-^

- Cách sử dụng? Bạn chỉ cần cài đặt python và chạy cmd trong folder của project rồi cài đặt thư viện bằng các câu lệnh sau:

pip install sqlite3 prettytable
pip install -r requirements.txt
python -m pip install sqlite3 prettytable

- Giới thiệu về các hàm có trong project:

Tập lệnh này là một chương trình đơn giản cho phép người dùng thêm và cập nhật thông tin về các phòng trong khách sạn.

Hàm add_room() nhắc người dùng nhập số phòng, thời gian nhận phòng và loại phòng. Số phòng phải là một trong số "02", "03", "04", "07", "08" hoặc "09". Thời gian nhận phòng phải ở định dạng "giờ:phút" (ví dụ: "01:00"). Loại phòng phải là "ML" hoặc "Q" (tương ứng với "điều hòa" và "quạt"). Nếu thông tin đầu vào hợp lệ, thì chức năng này sẽ thêm thông tin phòng vào cơ sở dữ liệu SQLite có tên "hotel_db.sql".

Hàm update_room_info() cho phép người dùng cập nhật thời gian nhận phòng và loại phòng của một phòng. Người dùng được nhắc nhập số phòng và sau đó chức năng sẽ truy vấn cơ sở dữ liệu để biết thông tin hiện tại của phòng. Sau đó, người dùng có thể nhập các giá trị mới cho thời gian nhận phòng và loại phòng và chức năng này sẽ cập nhật cơ sở dữ liệu với thông tin mới.

Hàm view_all_rooms() hiển thị tất cả các phòng trong cơ sở dữ liệu ở định dạng bảng bằng thư viện prettytable.

Hàm is_valid_time() là một hàm trợ giúp kiểm tra xem chuỗi đầu vào có phải là thời gian hợp lệ ở định dạng "giờ:phút" hay không.

Mã này sử dụng thư viện python sqlite3 để tương tác với cơ sở dữ liệu SQLite và thư viện python prettytable để tạo bảng.
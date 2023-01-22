import sqlite3
from datetime import datetime
from prettytable import PrettyTable

def add_room(): #Hàm chức năng thêm phòng
    room_number = input("Mời bạn nhập số phòng ( lưu ý: chỉ được chọn các phòng: 02, 03, 04, 07, 08, 09): ")
    while room_number not in ["02", "03", "04", "07", "08", "09"]:
        print("Xin lỗi, số phòng bạn nhập không hợp lệ, vui lòng nhập lại!")
        room_number = input("Mời bạn nhập số phòng ( lưu ý: chỉ được chọn các phòng: 02, 03, 04, 07, 08, 09): ")
    check_in_time = input("Mời bạn nhập giờ hiện tại ( định dạng: giờ:phút, ví dụ: 01:00 ): ")
    while not is_valid_time(check_in_time):
        print("Xin lỗi, bạn đã nhập sai định dạng của chức năng này, vui lòng nhập lại!")
        check_in_time = input("Mời bạn nhập giờ hiện tại ( định dạng: giờ:phút, ví dụ: 01:00 ): ")
    room_type = input("Mời bạn nhập loại phòng ( lưu ý: chỉ được nhập ML hoặc Q tức là Máy Lạnh và Quạt ): ")
    while room_type not in ["ML", "Q"]:
        print("Xin lỗi, loại phòng bạn nhập không hợp lệ, vui lòng nhập lại loại phòng!")
        room_type = input("Mời bạn nhập loại phòng ( lưu ý: chỉ được nhập ML hoặc Q tức là Máy Lạnh và Quạt ): ")
    conn = sqlite3.connect("hotel_db.sql")
    c = conn.cursor()
    c.execute("INSERT INTO rooms (room_number, check_in_time, room_type) VALUES (?, ?, ?)", (room_number, check_in_time, room_type))
    conn.commit()
    print("Thêm phòng thành công! Chúc bạn một ngày tốt lành ^-^")
    conn.close()

def update_room_info(): #Hàm chức năng cập nhật thông tin phòng
    room_number = input("Mời bạn nhập số phòng cần cập nhật thông tin ( lưu ý: chỉ được chọn các phòng: 02, 03, 04, 07, 08, 09): ")
    conn = sqlite3.connect("hotel_db.sql")
    c = conn.cursor()
    c.execute("SELECT * FROM rooms WHERE room_number = ?", (room_number,))
    room = c.fetchone()
    if room:
        check_in_time = input("Mời bạn nhập giờ nhận phòng mới ( định dạng: giờ:phút, ví dụ: 01:00 ): ")
        while not is_valid_time(check_in_time):
            print("Xin lỗi, bạn đã nhập sai định dạng của chức năng này, vui lòng nhập lại!")
            check_in_time = input("Mời bạn nhập giờ nhận phòng mới: ")
        room_type = input("Mời bạn nhập loại phòng mới: ")
        while room_type not in ["ML", "Q"]:
            print("Xin lỗi, bạn đã nhập sai loại phòng, vui lòng nhập lại!")
            room_type = input("Mời bạn nhập loại phòng mới: ")
        c.execute("UPDATE rooms SET check_in_time = ?, room_type = ? WHERE room_number = ?", (check_in_time, room_type, room_number))
        conn.commit()
        print("Chúc mừng bạn đã cập nhật thông tin phòng thành công, chúc bạn một ngày vui vẻ ^-^")
    else:
        print("Xin lỗi, phòng này chưa tồn tại trên hệ thống, vui lòng kiểm tra lại ^_^")
    conn.close()

def calculate_room_rate(): #Hàm này để tính tiền phòng
    room_number = input("Bạn muốn tính tiền phòng số mấy? ( lưu ý: chỉ được chọn các phòng: 02, 03, 04, 07, 08, 09) ")
    check_out_time = input("Mời bạn nhập giờ hiện tại: ")
    if is_valid_time(check_out_time):
        conn = sqlite3.connect("hotel_db.sql")
        c = conn.cursor()
        c.execute("SELECT check_in_time, room_type FROM rooms WHERE room_number = ?", (room_number,))
        room = c.fetchone()
        if room:
            check_in_time, room_type = room
            check_in_time = datetime.strptime(check_in_time, "%H:%M")
            check_out_time = datetime.strptime(check_out_time, "%H:%M")
            duration = (check_out_time - check_in_time).seconds / 60
            if room_type == "Q":
                if duration > 0 and duration <= 60:
                    rate = 70
                elif duration > 60 and duration <= 120:
                    rate = 80
                elif duration > 120 and duration <= 180:
                    rate = 90
                elif duration > 180 and duration <= 240:
                    rate = 110
                elif duration > 240 and duration <= 300:
                    rate = 120
                elif duration > 300 and duration <= 360:
                    rate = 140
                else:
                    rate = 0
            elif room_type == "ML":
                if duration > 0 and duration <= 60:
                    rate = 90
                elif duration > 60 and duration <= 120:
                    rate = 100
                elif duration > 120 and duration <= 180:
                    rate = 110
                elif duration > 180 and duration <= 240:
                    rate = 120
                elif duration > 240 and duration <= 300:
                    rate = 140
                elif duration > 300 and duration <= 360:
                    rate = 160
                else:
                    rate = 0
            if rate:
                print(f"Tiền phòng của phòng này là {rate}")
                c.execute("DELETE FROM rooms WHERE room_number = ?", (room_number,))
                conn.commit()
                print("Chúc bạn một ngày tốt lành ^-^")
            else:
                print("Giờ trả phòng mà bạn đã nhập không hợp lệ, giờ trả phòng phải lớn hơn thời gian nhận phòng")
        else:
            print("Số phòng mà bạn đã nhập không hợp lệ ( lưu ý: chỉ được chọn các phòng: 02, 03, 04, 07, 08, 09)")
        conn.close()
    else:
        print("Giờ trả phòng mà bạn đã nhập không hợp lệ ( nhập giờ theo định dạng: giờ:phút, ví dụ: 01:00 )")

def view_all_rooms(): #Hàm chức năng hiển thị tất cả các phòng đã nhập vào và hiển thị theo dạng bảng
    conn = sqlite3.connect("hotel_db.sql")
    c = conn.cursor()
    c.execute("SELECT * FROM rooms")
    rooms = c.fetchall()
    if rooms:
        table = PrettyTable()
        table.field_names = ["Room Number", "Check-in Time", "Room Type"]
        for room in rooms:
            table.add_row(room)
        print(table)
    else:
        print("Hiện chưa có phòng nào được nhập vào ^-^")
    conn.close()


def see_availability(): #Hàm cho chức năng xem tất cả các phòng còn trống
    conn = sqlite3.connect("hotel_db.sql")
    c = conn.cursor()
    c.execute("SELECT room_number FROM rooms")
    occupied_rooms = [room[0] for room in c.fetchall()]
    available_rooms = list(set(["02", "03", "04", "07", "08", "09"]) - set(occupied_rooms))
    if available_rooms:
        print(f"Các phòng trống là: {', '.join(available_rooms)}")
    else:
        print("Hiện không có phòng nào trống")
    conn.close()

def is_valid_time(time):
    try:
        datetime.strptime(time, "%H:%M")
        return True
    except ValueError:
        return False

def main():
    conn = sqlite3.connect("hotel_db.sql")
    c = conn.cursor()
    c.execute("CREATE TABLE IF NOT EXISTS rooms (room_number TEXT PRIMARY KEY, check_in_time TEXT NOT NULL, room_type TEXT NOT NULL)")
    conn.commit()
    conn.close()
    while True:
        print("\nChào Mừng Bạn Đến Với Chương Trình Quản Lý Nhà Nghỉ Được Tạo Bởi Nguyễn Hoàng Huy")
        print("Dưới Đây Là Menu Của Chương Trình")
        print("1. Thêm phòng mới")
        print("2. Cập nhật thông tin phòng")
        print("3. Tính tiền phòng")
        print("4. Xem tất cả các phòng đã thêm")
        print("5. Xem tất cả các phòng còn trống")
        print("6. Thoát chương trình")
        choice = input("Nhập lựa chọn của bạn: ")
        if choice == "1":
            add_room()
        elif choice == "2":
            update_room_info()
        elif choice == "3":
            calculate_room_rate()
        elif choice == "4":
            view_all_rooms()
        elif choice == "5":
            see_availability()
        elif choice == "6":
            print("Đang thoát chương trình...")
            print("Cảm ơn bạn đã sử dụng chương trình của tôi! Hẹn gặp lại ^-^")
            break
        else:
            print("Lựa chọn của bạn không hợp lệ, vui lòng nhập lại!")

if __name__ == "__main__":
    main()

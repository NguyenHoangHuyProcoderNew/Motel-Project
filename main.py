import sqlite3
from datetime import datetime
from prettytable import PrettyTable

# Kết nối đến cơ sở dữ liệu & tạo bảng cho cơ sở dữ liệu
conn = sqlite3.connect("hotel.db")
c = conn.cursor()
if not c.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='rooms'").fetchone():
    c.execute("CREATE TABLE rooms (room_number TEXT, check_in_time TIMESTAMP, room_type TEXT, use_water TEXT, water_type TEXT, water_quantity INTEGER)")
conn.commit()
conn.close()

# Chức năng thêm phòng
def add_room():
    room_number = input("Mời bạn chọn phòng: ")
    while room_number not in ["02", "03", "04", "07", "08", "09"]:
        print("Xin lỗi, phòng bạn chọn hiện đang có khách hoặc không hợp lệ vui lòng chọn lại nếu vẫn không được hãy chọn phòng khác ╯︵╰")       
        room_number = input("Mời bạn chọn lại phòng ( lưu ý: chỉ được chọn các phòng: 02, 03, 04, 07, 08, 09): ")
    check_in_time = input("Hãy cho tôi biết giờ nhận phòng: ")
    while not is_valid_time(check_in_time):
        print("Xin lỗi, bạn đã cung cấp cho tôi giờ nhận phòng với định dạng giờ hoặc một dữ liệu không hợp lệ ╯︵╰")
        check_in_time = input("Mời bạn cung cấp lại giờ nhận phòng: ")
    room_type = input("Mời bạn chọn loại phòng: ")
    while room_type not in ["ML", "Q"]:
        print("Loại phòng bạn chọn không hợp lệ ╯︵╰")
        room_type = input("Vui lòng chọn lại loại phòng ( lưu ý: bạn chỉ có thể chọn loại phòng là ML hoặc Q tương đương với phòng Quạt hoặc Máy Lạnh): ")
    use_water = input("Phòng này có sử dụng nước uống không? Nếu có thì nhập Y còn nếu không thì nhập N: ")
    while use_water not in ["Y", "N"]:
        print("Xin lỗi bạn chỉ có thể chọn Y hoặc N và phải viết hoa bạn nhé ( ╹▽╹ )")
        use_water = input("Mời bạn nhập lại lựa chọn của mình: ")
    if use_water == "Y":
        water_type = input("Mời bạn chọn loại nước: ")
        while water_type not in ["NN", "NS"]:
            print("Loại nước bạn đã chọn không hợp lệ, vui lòng chọn lại loại nước ( lưu ý: bạn chỉ có thể chọn NN hoặc NS tương đương với Nước Ngọt hoặc Nước Suối bạn nhé ( ╹▽╹ ) ")
            water_type = input("Mời bạn chọn lại loại nước: ")
        water_quantity = input("Bạn muốn sử dụng bao nhiêu? Hãy cho tôi biết số lượng: ")
    else:
        water_type = None
        water_quantity = None
    conn = sqlite3.connect("hotel.db")
    c = conn.cursor()
    c.execute("INSERT INTO rooms (room_number, check_in_time, room_type, use_water, water_type, water_quantity) VALUES (?,?,?,?,?,?)", (room_number, check_in_time, room_type, use_water, water_type, water_quantity))
    conn.commit()
    print("Thêm phòng thành công! Chúc bạn một ngày tốt lành ^-^")    
    conn.close()
#Hàm này để check điều kiện giờ nhận phòng cho hàm trên
def is_valid_time(time):
    try:
        datetime.strptime(time, "%H:%M")
        return True
    except ValueError:
        return False

#Cập nhật thông tin cho phòng nếu dữ liệu đã nhập trước đó bị sai hoặc khách muốn đổi phòng,..v..v...
def update_room_info():
    room_number = input("Bạn muốn cập nhật thông tin của phòng số mấy? Hãy cho tôi biết số phòng: ")
    conn = sqlite3.connect("hotel.db")
    c = conn.cursor()
    c.execute("SELECT * FROM rooms WHERE room_number = ?", (room_number,))
    data = c.fetchone()
    if data:
        print("\nThông tin phòng hiện tại:")
        print("Số phòng: ", data[0])
        print("Giờ nhận phòng: ", data[1])
        print("Loại phòng: ", data[2])
        print("Sử dụng nước: ", data[3])
        print("Loại nước: ", data[4])
        print("Số lượng: ", data[5])
        print("Đã Làm Mới Lại Thông Tin Phòng:", data[0])
        print("\nMời Bạn Cung Cấp Thông Tin Mới:")
        # Chọn phòng
        new_room_number = input("Bạn có muốn đổi phòng không? Nếu không hãy nhập lại số phòng cũ: ")
        while new_room_number not in ["02", "03", "04", "07", "08", "09"]:
            print("Xin lỗi, phòng bạn chọn hiện đang có khách hoặc không hợp lệ vui lòng chọn lại nếu vẫn không được hãy chọn phòng khác ╯︵╰")
            new_room_number = input("Mời bạn chọn lại phòng mới ( lưu ý: chỉ được chọn các phòng: 02, 03, 04, 07, 08, 09): ")
        # Giờ nhận phòng         
        new_check_in_time = input("Giờ nhận phòng mới: ")
        while not is_valid_time(new_check_in_time):
            print("Xin lỗi, bạn đã cung cấp cho tôi giờ nhận phòng với định dạng giờ hoặc một dữ liệu không hợp lệ ╯︵╰")
            new_check_in_time = input("Mời bạn cung cấp lại giờ nhận phòng: ")
        # Loại phòng 
        new_room_type = input("Mời bạn chọn loại phòng mới: ")
        while new_room_type not in ["ML", "Q"]:
            print("Loại phòng bạn chọn không hợp lệ ╯︵╰")
            new_room_type = input("Vui lòng chọn lại loại phòng ( lưu ý: bạn chỉ có thể chọn loại phòng là ML hoặc Q tương đương với phòng Quạt hoặc Máy Lạnh): ")
        # Sử dụng nước    
        new_use_water = input("Phòng này có sử dụng nước uống không? Nếu có thì nhập Y còn nếu không thì nhập N: ")
        while new_use_water not in ["Y", "N"]:
            print("Xin lỗi bạn chỉ có thể chọn Y hoặc N và phải viết hoa bạn nhé ( ╹▽╹ )")
            new_use_water = input("Mời bạn nhập lại lựa chọn của mình: ")
        if new_use_water == "Y":
            new_water_type = input("Mời bạn chọn loại nước: ")
            while new_water_type not in ["NN", "NS"]:
                print("Loại nước bạn đã chọn không hợp lệ, vui lòng chọn lại loại nước ( lưu ý: bạn chỉ có thể chọn NN hoặc NS tương đương với Nước Ngọt hoặc Nước Suối bạn nhé ( ╹▽╹ ) ")
                new_water_type = input("Mời bạn chọn lại loại nước: ")
            new_water_quantity = input("Bạn muốn sử dụng bao nhiêu? Hãy cho tôi biết số lượng: ")
        else:
            new_water_type = None
            new_water_quantity = None
        c.execute("UPDATE rooms SET room_number = ?, check_in_time = ?, room_type = ?, use_water = ?, water_type = ?, water_quantity = ? WHERE room_number = ?", (new_room_number, new_check_in_time, new_room_type, new_use_water, new_water_type, new_water_quantity, room_number))
        conn.commit()
        print("Cập nhật thông tin thành công! Chúc bạn có một ngày làm việc vui vẻ ( ╹▽╹ )")
    else:
        print("Không tồn tại phòng này hãy kiểm tra lại bạn nhé ╯︵╰")
    conn.close()

# Thanh toán
def calculate_room_rate():
    room_number = input("Bạn muốn thanh toán phòng số mấy? Hãy cho tôi biết số phòng: ")
    check_out_time = input("Hãy nhập giờ hiện tại: ")
    conn = sqlite3.connect("hotel.db")
    c = conn.cursor()
    c.execute("SELECT * FROM rooms WHERE room_number = ?", (room_number,))
    data = c.fetchone()
    if data:
        check_in_time = data[1]
        room_type = data[2]
        use_water = data[3]
        water_type = data[4]
        water_quantity = data[5]
        check_in_time = datetime.strptime(check_in_time, "%H:%M")
        check_out_time = datetime.strptime(check_out_time, "%H:%M")
        duration = check_out_time - check_in_time
        duration_minutes = duration.seconds / 60
        # Thiết lập giá tiền
        if room_type == "Q": # Giá tiền cho phòng quạt
            if duration_minutes <= 60: # 1 giờ
                room_rate = 80  # Giá tiền
            elif duration_minutes <= 120: # 2 giờ
                room_rate = 100 # Giá tiền
            elif duration_minutes <= 180: # 3 giờ
                room_rate = 100 # Giá tiền
            elif duration_minutes <= 240: # 4 giờ
                room_rate = 110 # Giá tiền
            elif duration_minutes <= 300: # 5 giờ
                room_rate = 120 # Giá tiền
            elif duration_minutes <= 360: # 6 giờ
                room_rate = 160 # Giá tiền
        elif room_type == "ML": # Giá tiền cho phòng máy lạnh
            if duration_minutes <= 60: # 1 giờ
                room_rate = 100
            elif duration_minutes <= 120: # 2 giờ
                room_rate = 110
            elif duration_minutes <= 180: # 3 giờ
                room_rate = 130
            elif duration_minutes <= 240: # 4 giờ
                room_rate = 150
            elif duration_minutes <= 300: # 5 giờ
                room_rate = 160
            elif duration_minutes <= 360: # 6 giờ
                room_rate = 200
        water_rate = 0
        if use_water == "Y":
            if water_type == "NN":
                water_rate = water_quantity * 15
            elif water_type == "NS":
                water_rate = water_quantity * 5
        total_rate = room_rate + water_rate
        print("\nTiền phòng: ", room_rate)
        print("Tiền nước: ", water_rate)
        print("Tổng số tiền phải trả: ", total_rate)
        #removing the room from the database
        c.execute("DELETE FROM rooms WHERE room_number = ?", (room_number,))
        conn.commit()
        print("Thanh toán thành công! Cảm ơn bạn đã sử dụng dịch vụ của chúng tôi. Xin cảm ơn ( ╹▽╹ )")
    else:
        print("Phòng này chưa tồn tại trên hệ thống. Vui lòng kiểm tra lại!")

#Hàm xem tất cả các phòng đang có khách
def view_all_rooms():
    conn = sqlite3.connect("hotel.db")
    c = conn.cursor()
    c.execute("SELECT * FROM rooms")
    data = c.fetchall()
    x = PrettyTable()
    x.field_names = ["Số phòng", "Giờ nhận phòng", "Loại phòng", "Sử dụng nước", "Loại nước", "Số lượng nước"]
    for row in data:
        x.add_row(row)
    print(x)
    conn.close()

#Hàm xem tất cả các phòng còn trống
def see_availability():
    conn = sqlite3.connect("hotel.db")
    c = conn.cursor()
    c.execute("SELECT room_number FROM rooms")
    occupied_rooms = [room[0] for room in c.fetchall()]
    available_rooms = list(set(["02", "03", "04", "07", "08", "09"]) - set(occupied_rooms))
    if available_rooms:
        available_rooms.sort()
        print(f"Các phòng trống là: {' | '.join(available_rooms)}")
    else:
        print("Hiện không có phòng nào trống")
    conn.close()    

# Menu cho chương trình    
def main():
    while True:
        print("\nChào mừng bạn đã đến với chương trình quản lý nhà nghỉ Huy Đức - Chương trình được tạo & vận hành bởi Nguyễn Hoàng Huy")
        print("Dưới Đây Là Menu Của Chương Trình")
        print("1. Check-in phòng")
        print("2. Cập nhật lại thông tin phòng")
        print("3. Thanh toán")
        print("4. Xem danh sách các phòng có khách")
        print("5. Xem danh sách các phòng trống")
        print("6. Thoát chương trình")
        choice = input("Lựa chọn của bạn: ")
        if choice == "1":
            add_room()
        elif choice == "2":
            update_room_info()
        elif choice == "3":
            calculate_room_rate()
        elif choice == "4":
            view_all_rooms()
        elif choice == "6":
            break
        elif choice == "5":
            see_availability()        
        else:
            print("Lựa chọn của bạn không hợp lệ, vui lòng chọn lại!")

if __name__ == '__main__':
    main()

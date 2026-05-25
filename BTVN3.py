"""
Input:
user_choice_str: Chuỗi lựa chọn menu
search_id: Mã nhân viên cần tìm ở chức năng 3
Output: Chuỗi dữ liệu gốc, bảng báo cáo nhân sự, thông tin chi tiết nhân viên tìm được

Luồng chương trình:
Bước 1: Sử dụng vòng lặp vô hạn while hiển thị menu. Nhập user_choice_str, kiểm tra bằng .isdigit() 
trước khi ép kiểu sang số nguyên user_choice
Bước 2: Phân nhánh xử lý bằng match case
Case 1 in trực tiếp chuỗi dữ liệu gốc raw_data
Case 2 cắt chuỗi theo dấu | để duyệt từng nhân viên, rồi tiếp theo cắt theo dấu ;
chuẩn hóa ID/Phòng ban bằng .strip().upper(), họ tên bằng .strip().title().
Riêng Số điện thoại dùng .replace("-", "") trước rồi nếu đạt .isdigit() thì che chuỗi bằng ******, ngược lại báo Invalid Format
In căn lề bằng f-string
Case 3 nhận search_id. Duyệt qua danh sách, bóc tách và chuẩn hóa ID của từng người để so sánh
Khớp thì in thông tin rồi break, không khớp thì báo Không tìm thấy nhân viên
Case 4 in thông báo và dùng break thoát vòng lặp
Case _ báo lỗi nếu nhập số nằm ngoài khoảng 1-4
"""

raw_data = " eMP-001; nguyen van a ;0987654321;sale | Emp-002; Tran Thi B; 0912-345-678 ; mkt | EMP-003 ; le van C ; 0988abc123 ; IT "

while True:
    print("""
===== HỆ THỐNG QUẢN LÝ NHÂN SỰ =====
1. Hiển thị chuỗi dữ liệu gốc
2. Chuẩn hóa dữ liệu và in báo cáo
3. Tìm kiếm nhân viên theo mã ID
4. Thoát chương trình
====================================
""")
    
    user_choice_str = input("Mời chọn chức năng (1-4): ").strip()

    if not user_choice_str.isdigit():
        print("Lựa chọn không hợp lệ, vui lòng nhập lại!")
        continue

    user_choice = int(user_choice_str)

    match user_choice:
        case 1:
            print("\n--- CHUỖI DỮ LIỆU GỐC ---")
            print(raw_data)

        case 2:
            print("\n--- BÁO CÁO NHÂN SỰ ĐÃ CHUẨN HÓA ---")
            print(f"{'MÃ ID':<10}{'HỌ VÀ TÊN':<20}{'SỐ ĐIỆN THOẠI':<18}{'PHÒNG BAN':<10}")
            print("-" * 58)

            employees_raw = raw_data.split("|")
            for emp in employees_raw:
                parts = emp.split(";")
                if len(parts) != 4:
                    continue

                emp_id = parts[0].strip().upper()
                full_name = parts[1].strip().title()
                phone_raw = parts[2].strip()
                department = parts[3].strip().upper()

                phone_clean = phone_raw.replace("-", "")
                if phone_clean.isdigit():
                    phone_display = "******" + phone_clean[6:]
                else:
                    phone_display = "Invalid Format"

                print(f"{emp_id:<10}{full_name:<20}{phone_display:<18}{department:<10}")

        case 3:
            print("\n--- TÌM KIẾM NHÂN VIÊN ---")
            search_id = input("Nhập mã nhân viên cần tìm: ").strip().upper()

            employees_raw = raw_data.split("|")
            found = False

            for emp in employees_raw:
                parts = emp.split(";")
                if len(parts) != 4:
                    continue

                emp_id = parts[0].strip().upper()
                full_name = parts[1].strip().title()
                phone_raw = parts[2].strip()
                department = parts[3].strip().upper()

                phone_clean = phone_raw.replace("-", "")
                if phone_clean.isdigit():
                    phone_display = "******" + phone_clean[6:]
                else:
                    phone_display = "Invalid Format"

                if emp_id == search_id:
                    print(
                        f"\n[ĐÃ TÌM THẤY THÔNG TIN]\n"
                        f"- Mã nhân viên: {emp_id}\n"
                        f"- Họ và tên: {full_name}\n"
                        f"- Số điện thoại: {phone_display}\n"
                        f"- Phòng ban: {department}\n"
                    )
                    found = True
                    break

            if not found:
                print("Không tìm thấy nhân viên")

        case 4:
            print("Thoát chương trình")
            break

        case _:
            print("Lựa chọn không hợp lệ!")

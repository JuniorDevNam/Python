# Viết chương trình nhập số học sinh và họ tên học sinh.
# Sau đó đếm xem trong danh sách có bao nhiêu bạn tên là “Hương”.


# Nhập số học sinh
n = int(input("Nhập số học sinh: "))

# Khởi tạo danh sách học sinh
hoc_sinh = []

# Nhập họ tên học sinh
for i in range(n):
    ho_ten = input(f"Nhập họ tên học sinh {i+1}: ")
    hoc_sinh.append(ho_ten)
so_luong_huong = 0
# Đếm số bạn tên là "Hương"
for ten in hoc_sinh:
    if "Hương" in ten:
        so_luong_huong += 1

# In kết quả
print(f"Số bạn tên là 'Hương' trong danh sách là: {so_luong_huong}")

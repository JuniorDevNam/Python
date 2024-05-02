# Viết chương trình giải phương trình bậc 1: ax+b=0

# Nhập giá trị của a và b từ người dùng
a = float(input("Nhập a: "))
b = float(input("Nhập b: "))

# Kiểm tra xem a có khác 0 không
if a != 0:
    # Tính nghiệm của x
    x = -b / a
    # In kết quả ra màn hình
    print("Nghiệm của x là:", x)
else:
    # Phương trình vô nghiệm hoặc vô số nghiệm
    if b == 0:
        # Phương trình vô số nghiệm
        print("Phương trình vô số nghiệm")
    else:
        # Phương trình vô nghiệm
        print("Phương trình vô nghiệm")
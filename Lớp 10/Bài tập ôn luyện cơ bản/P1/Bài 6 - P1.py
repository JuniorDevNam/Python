# Viết chương trình giải phương trình bậc 2: ax^2 + bx+c = 0 (a khác 0)

import math
# Nhập giá trị của a, b và c từ người dùng
a = float(input("Nhập a: "))
b = float(input("Nhập b: "))
c = float(input("Nhập c: "))

# Kiểm tra xem a có khác 0 không
if a != 0:
    # Tính delta
    delta = b**2 - 4*a*c
    # Kiểm tra xem delta có âm hay không
    if delta < 0:
        # Phương trình vô nghiệm
        print("Phương trình vô nghiệm")
    elif delta == 0:
        # Phương trình có nghiệm kép
        x = -b / (2*a)
        # In kết quả ra màn hình
        print("Phương trình có nghiệm kép x =", x)
    else:
        # Phương trình có hai nghiệm phân biệt
        x1 = (-b + math.sqrt(delta)) / (2*a) #Trừ b cộng căn delta trên 2a 
        x2 = (-b - math.sqrt(delta)) / (2*a)
        # In kết quả ra màn hình
        print("Phương trình có hai nghiệm phân biệt:")
        print("x1 =", x1)
        print("x2 =", x2)
else:
    # Phương trình không phải là phương trình bậc hai
    print("Không phải là phương trình bậc hai")


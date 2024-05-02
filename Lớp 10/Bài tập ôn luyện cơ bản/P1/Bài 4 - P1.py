#  Viết chương trình nhập vào ba cạnh của tam giác, 
# kiểm tra xem tam giác đó là loại tam giác nào: đều, vuông, cân, hay thường.

# Nhập giá trị của ba cạnh từ người dùng
a = float(input("Nhập cạnh a: "))
b = float(input("Nhập cạnh b: "))
c = float(input("Nhập cạnh c: "))

# Kiểm tra xem ba cạnh có tạo thành một tam giác hợp lệ không
if a + b >= c and b + c >= a and c + a >= b:
    # Tam giác hợp lệ
    # Kiểm tra xem tam giác là loại nào
    if a == b == c:
        # Tam giác đều
        print("Tam giác đều")
    elif a**2 + b**2 == c**2 or b**2 + c**2 == a**2 or c**2 + a**2 == b**2:
        # Tam giác vuông
        print("Tam giác vuông")
    elif a == b or b == c or c == a:
        # Tam giác cân
        print("Tam giác cân")
    else:
        # Tam giác thường
        print("Tam giác thường")
else:
    # Tam giác không hợp lệ
    print("Không phải tam giác")
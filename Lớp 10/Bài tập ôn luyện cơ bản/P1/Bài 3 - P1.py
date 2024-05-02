# Viết chương trình nhập vào x, tính y = x-1 nếu x>=1, ngược lại y = 1-x

# Nhập giá trị của x từ người dùng
x = float(input("Nhập x: "))
# Tính y tùy thuộc vào điều kiện của x
if x >= 1:
    y = x - 1
else:
    y = 1 - x
# In kết quả ra màn hình
print("Giá trị của y là:", y)
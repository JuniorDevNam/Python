'''Bài 8: VCT tìm ước chung lớn nhất và bội chung nhỏ nhất của hai số nhập vào từ bàn phím?'''

# Hàm để tìm ước chung lớn nhất của hai số a và b
def ucln(a, b):
    # Nếu a hoặc b là số âm, đổi dấu thành dương
    if a < 0:
        a = -a
    if b < 0:
        b = -b
    # Nếu a hoặc b là 0, trả về số còn lại
    if a == 0:
        return b
    if b == 0:
        return a
    # Lặp cho đến khi một trong hai số bằng 0
    while a != 0 and b != 0:
        # Tìm phần dư của a chia cho b
        r = a % b
        # Gán a = b và b = r
        a = b
        b = r
    # Trả về số khác 0 cuối cùng làm kết quả
    return a + b

# Hàm để tìm bội chung nhỏ nhất của hai số a và b
def bcnn(a, b):
    # Nếu a hoặc b là số âm, đổi dấu thành dương
    if a < 0:
        a = -a
    if b < 0:
        b = -b
    # Nếu a hoặc b là 0, trả về 0
    if a == 0 or b == 0:
        return 0
    # Tính tích của a và b
    p = a * b
    # Tính ước chung lớn nhất của a và b
    u = ucln(a, b)
    # Trả về thương của p và u làm kết quả
    return p // u

# Nhập hai số từ bàn phím
a = int(input("Nhập số thứ nhất: "))
b = int(input("Nhập số thứ hai: "))
# In ra kết quả
print("Ước chung lớn nhất của",a,"và",b,"là:",ucln(a,b))
print("Bội chung nhỏ nhất của",a,"và",b,"là:",bcnn(a,b))


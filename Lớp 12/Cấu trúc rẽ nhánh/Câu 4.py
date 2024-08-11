# Bài 4: Viết chương trình nhập vào ba cạnh của tam giác, 
# kiểm tra xem tam giác đó là loại tam giác nào: đều, vuông, cân, hay thường.

def tam_giac(a, b, c):
    # Kiểm tra xem ba cạnh có tạo thành tam giác không
    if a + b > c and a + c > b and b + c > a:
        # Kiểm tra tam giác đều
        if a == b == c:
            return "Tam giác đều"
        # Kiểm tra tam giác vuông (Pytago)
        elif a**2 + b**2 == c**2 or a**2 + c**2 == b**2 or b**2 + c**2 == a**2:
            return "Tam giác vuông"
        # Kiểm tra tam giác cân
        elif a == b or a == c or b == c:
            return "Tam giác cân"
        else:
            return "Tam giác thường"
    else:
        return "Không phải là tam giác"
a = int(input("Nhập cạnh a: "))
b = int(input("Nhập cạnh b: "))
c = int(input("Nhập cạnh c: "))
print("Loại tam giác là: {}".format(tam_giac(a,b,c)))
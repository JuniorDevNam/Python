# Nhập từ bàn phím 3 số nguyên a, b, c bất kỳ
# Kiểm tra xem 3 số a, b, c có tạo thành 1 tam giác hay không? 
# Nếu có tính chu vi và diện tích của tam giác đó.

from math import sqrt

# Nhập 3 số nguyên a,b,c bất kỳ
a = int(input("Nhập số a: "))
b = int(input("Nhập số b: "))
c = int(input("Nhập số c: "))

# Kiểm tra a,b,c có tạo thành 1 tam giác
# Bất đẳng thức tam giác
check1 = a + b > c
check2 = a + c > b
check3 = b + c > a
checkBatdangthuc = [check1, check2, check3]
# Thuật toán
while False in checkBatdangthuc:
    print("a, b, c không thỏa mãn bất đẳng thức tam giác")
    print("a, b, c không tạo được thành 1 tam giác")
    a = int(input("Hãy nhập lại a: "))
    b = int(input("Hãy nhập lại b: "))
    c = int(input("Hãy nhập lại c: "))
# Thông báo tạo được tam giác
print("a, b, c thỏa mãn bất đẳng thức tam giác")
print("a, b, c tạo được thành 1 tam giác")
# Chu vi tam giác
chuVi = a + b + c
print("Chu vi của tam giác đó là:",chuVi)
# Diện tích tam giác
nuaChuvi = chuVi/2
dienTich = sqrt(nuaChuvi*(nuaChuvi-a)*(nuaChuvi-b)*(nuaChuvi-c))
print("Diện tích của tam giác là:",dienTich)
# Bài 4: Nhập vào hai số m, n, xuất ra dãy số bội 3 từ m đến n.
m = int(input("Nhập số m: "))
n = int(input("Nhập số n: "))
for i in range(m if m % 3 == 0 else m + (3 - m % 3),(n if n % 3 == 0 else n - (n % 3))+1,3):
    print(i, end = " ")
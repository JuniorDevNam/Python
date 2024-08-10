# Bài 3: Viết chương trình nhập vào hai số m, n, xuất ra dãy số chẵn từ m đến n.
m = int(input("Nhập số m: "))
n = int(input("Nhập số n: "))
for i in range(m, n+1):
    if i%2 == 0:
        print(i, end=" ")
# Bài 5: Nhập vào số nguyen dương n, tính và xuất ra tổng S = 1 + 2 + .....+n.
n = int(input("Nhập số nguyên dương n: "))
t = 0
for i in range(1,n+1):
    t += i
print(t)
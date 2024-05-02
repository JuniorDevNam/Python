'''Nhập vào số nguyen dương n, tính và xuất ra tổng S = 1 + 2 + .....+n.'''

n = int(input("Nhập số nguyên dương n: "))
while n < 0:
    print("Tôi bảo nhập số nguyên dương cơ mà")
    n = int(input("Nhập số nguyên dương n: "))
S = 0
for x in range(1,n+1):
    S = S + x
print("Tổng là:",S)
# Bài 11: VCT  xuất các số nguyên tố từ n đến m.
n = int(input('Nhập số n: '))
m = int(input("Nhập số m: "))
def nt(x):
    if x < 1:
        return 0
    d = 0
    for i in range(2,n):
        if x%i == 0:
            d += 1
        if d >= 1:
            return 0
    else:
        return 1
for y in range(n,m+1):
    if nt(y):
        print(y, end = " ")
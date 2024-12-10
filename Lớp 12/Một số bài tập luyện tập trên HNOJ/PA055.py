'''
Cho hai số l và r.
Đếm số lượng số nguyên tố có tổng chữ số không vượt quá 10 trong khoảng [l;r]
https://hnoj.edu.vn/problem/pa055
'''
def so_nguyen_to(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True
l, r = map(int, input().split())
def tong_chu_so(num):
    tong = 0
    for x in str(num):
        tong += int(x)
    return tong
count = 0
for x in range(l, r+1):
    if so_nguyen_to(x):
        if tong_chu_so(x) <= 10:
            count += 1
print(count)
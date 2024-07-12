'''
Đề bài
Viết chương trình con để tính n! = 1.2...n.  Áp dụng tính tổng m biểu thức tổ hợp chập k của n với Ckn = n!/(k!.(n-k)!) 

Dữ liệu vào
Dòng 1 là số nguyên m; m dòng tiếp theo, mỗi dòng gồm 2 số theo thứ tự là n và k

Dữ liệu ra
Tổng của m biểu thức trên

Ví dụ
Input #1 
3
6 4
3 2
5 2
Output #1 
28

Input #2 
2
4 2
4 3
Output #2 
10
'''
def giai_thua(so):
    r = 1
    for _ in range(1,so+1):
        r *= _
    return r
def chinh_hop(k,n):
    return giai_thua(n)/(giai_thua(k)*giai_thua((n-k)))
# Đọc dữ liệu vào
m = int(input())
total_sum = 0

# Xử lý m biểu thức
for _ in range(m):
    n, k = map(int, input().split())
    total_sum += chinh_hop(k, n)

print(total_sum)
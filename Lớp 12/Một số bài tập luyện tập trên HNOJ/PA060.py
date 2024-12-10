'''
https://hnoj.edu.vn/problem/pa060
Cho một số nguyên dương n. 
Hãy liệt kê tất cả số nguyên tố nhỏ hơn hoặc bằng n.
In ra tất cả các số nguyên tố không vượt quá n theo thứ tự tăng dần trên cùng một dòng.
'''
def so_nguyen_to(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True
n = int(input())
if n == 2:
    print(2)
if n > 2:
    print(2, end=" ")
    for x in range(3,n+1,2):
        if so_nguyen_to(x):
            print(x,end=" ")
'''
Cho số nguyên dương n
Hãy xây dựng tam giác cân n dòng sử dụng dấu *.
https://hnoj.edu.vn/problem/pa053
'''
n = int(input())
for i in range(1, n+1):
    print(" "*(n-i), end="")
    print("*"*(2*i - 1))
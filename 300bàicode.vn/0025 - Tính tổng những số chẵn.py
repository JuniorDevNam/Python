'''
Đề bài
Viết chương trình nhập vào 1 số nguyên dương n. Tính tổng những số chẵn từ 1 đến n.

Dữ liệu vào
Một số nguyên dương n.

Dữ liệu ra
tổng các số chẵn từ 1 đến n

Ví dụ
Input #1 
13
Output #1 
42

Input #2 
21
Output #2 
110
Nguồn
https://www.facebook.com/300baicode.vn/posts/117067620748311
'''
n = int(input())
start = n if n % 2 == 0 else n - n % 2
sum = 0
for i in range(2 ,start + 1, 2):
    sum += i
print(sum)
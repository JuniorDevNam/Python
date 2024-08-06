'''
Đề bài
Viết chương trình nhập vào 1 số nguyên dương n. Tính tổng những số chia hết cho 3 và 5 từ 1 đến n

Dữ liệu vào
Một số nguyên dương n

Dữ liệu ra
Tổng các số chia hết cho 3 và 5 từ 1 đến n

Ví dụ
Input #1 
13
Output #1 
0

Input #2 
21
Output #2 
15
Nguồn
https://www.facebook.com/300baicode.vn/posts/117067670748306
'''
n = int(input())
start = n if n%5 == 0 else n - n%5
sum = 0
for x in range(5,start + 1,5):
    if x%3 == 0:
        sum += x
print(sum)
'''
Đề bài
Viết chương trình nhập vào 1 số nguyên dương n. Đếm xem n có bao nhiêu ước


Dữ liệu vào
Một số nguyên dương n


Dữ liệu ra
Số ước của n


Ví dụ
Input #1 

13
Output #1 

2
Input #2 

21
Output #2 

4
Nguồn
https://www.facebook.com/300baicode.vn/posts/117067720748301
'''
n = int(input())
uoc = 0
for x in range(1, n+1):
    if n%x == 0:
        uoc += 1
print(uoc)
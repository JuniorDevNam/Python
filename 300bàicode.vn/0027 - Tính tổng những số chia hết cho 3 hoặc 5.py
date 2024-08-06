'''
Đề bài
Viết chương trình nhập vào 1 số nguyên dương n. Tính tổng những số chia hết cho 3 hoặc 5 từ 1 đến n

Dữ liệu vào
Một số nguyên dương n

Dữ liệu ra
Tổng các số chia hết cho 3 hoặc 5 từ 1 đến n;

Ví dụ
Input #1 
13
Output #1 
45

Input #2 
21
Output #2 
119
Nguồn
https://www.facebook.com/300baicode.vn/posts/117067700748303
'''
import time
from time import gmtime, strftime

start_time = time.time()  # Thời điểm bắt đầu

# Thực hiện các công việc của chương trình ở đây
n = int(input())

total = 0
for i in range(1, n + 1):
    if i % 3 == 0 or i % 5 == 0:
        total += i
print(total)


end_time = time.time()  # Thời điểm kết thúc
elapsed_time = end_time - start_time

print(f"Thời gian chạy: {elapsed_time:.2f} giây")
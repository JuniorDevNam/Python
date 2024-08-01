'''
Đề bài
Viết chương trình nhập vào 1 số nguyên dương n. In ra số lượng số chia hết cho 3 trong các số từ 1 đến n

Dữ liệu vào
Một số nguyên dương n

Dữ liệu ra
Số lượng số chia hết cho 3 từ 1 đến n

Ví dụ
Input #1 
13
Output #1 
4

Input #2 
21
Output #2 
7
'''
n = int(input())
count = 0
start = n if n % 3 == 0 else n - n % 3
for i in range(3, start + 1, 3):
    count += 1
print(count)
'''
Một con Robot nhảy từ A đến B với khoảng cách là N (m)
Biết rằng thỏ có 2 cách nhảy là nhảy ngắn a(m) và nhảy dài b (m)
Hãy tính số bước nhảy sao cho thỏ đến được B với ít số bước nhất
Khoảng cách số bước không được vượt quá B mà phải vừa đủ
Nhập input vào từ file 'Robot.INP' và xuất kết quả ra 'Robot.OUT'
N, a, b cách nhau 1 khoảng trắng trên cùng 1 dòng trong file input
'''

#Lời giải đầy đủ và chính xác dựa vào Bing AI

import sys
from os.path import join

input_file = join(sys.path[0], 'Robot.INP')
output_file = join(sys.path[0], 'Robot.OUT')

with open(input_file, 'r') as f:
    N, a, b = map(int, f.readline().split())

steps = 0
while N > 0:
    if N >= b:
        N -= b
        steps += 1
    elif N >= a:
        N -= a
        steps += 1
    else:
        break

with open(output_file, 'w') as f:
    f.write(str(steps))
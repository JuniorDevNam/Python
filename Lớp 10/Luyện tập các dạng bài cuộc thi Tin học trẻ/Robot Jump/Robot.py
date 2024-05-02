'''
Một con Robot nhảy từ A đến B với khoảng cách là N (m)
Biết rằng thỏ có 2 cách nhảy là nhảy ngắn a(m) và nhảy dài b (m)
Hãy tính số bước nhảy sao cho thỏ đến được B với ít số bước nhất
Khoảng cách số bước không được vượt quá B mà phải vừa đủ
Nhập input vào từ file 'Robot.INP' và xuất kết quả ra 'Robot.OUT'
N, a, b cách nhau 1 khoảng trắng trên cùng 1 dòng trong file input
'''

import sys
from os.path import join

input_file = join(sys.path[0], 'Robot.INP')
output_file = join(sys.path[0], 'Robot.OUT')
sys.stdin = open(input_file, 'r') # mở file để đọc
sys.stdout = open(output_file, 'w') # mở file để ghi

#Với bài này, thuật toán chính xác, nhưng 1 yêu cầu của đề bài là
#N, a, b phải cùng 1 dòng và cách nhau 1 khoảng trắng trong file input đã không được thực hiện
#Do stdin và stdout không phù hợp để sử dụng cho điều này
#stdin và stdout hoạt động khi các số N, a, b mỗi giá trị 1 hàng lần lượt từ trên xuống
N = int(input())
a = int(input())
b = int(input())

def nam_lam(N, a, b):
    sobuocA = N//a
    sobuocB = N//b
    if sobuocA > sobuocB:
        return sobuocB
    else:
        if sobuocA < sobuocB:
            return sobuocA

def bing_ai(N, a, b):
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
    return str(steps)

print("Nam: ",nam_lam(N, a, b))
print("Bing AI: ",bing_ai(N, a, b))

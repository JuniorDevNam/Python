'''
Đề bài
Viết chương trình tính tiền taxi căn cứ vào đoạn đường đi, biết rằng

1 km đầu giá 12000đ
km thứ 2 đến km thứ 30 giá 10000đ
km thứ 31 trở đi tính 9000đ
Vd:
+ km=3 thìTien=1*12000+(3-1)*10000=12000+20000=32000
+ km=40 thì Tien=12000+29*10000+(40-30)*9000=392000

Dữ liệu vào
Một số nguyên n là số km đã đi.

Dữ liệu ra
Số tiền cần trả

Ví dụ
Input #1 

67
Output #1 

635000
Input #2 

87
Output #2 

815000
'''
n = int(input())
if n == 1:
    tien = 12000
elif 1 < n < 30:
    tien = 12000+(n-1)*10000
elif n >= 31:
    tien = 12000+29*10000+(n-30)*9000

print(tien)
'''
Đề bài
Viết chương trình nhập vào số KW/h điện tiêu thụ trong 1 tháng 
và tính tiền điện sử dụng trong 1 tháng đó. 
Biết rằng, 50 KW/h đầu được tính với giá 600đ mỗi KW/h, 
50 KW/h tiếp theo được tính với giá 800đ mỗi KW/h, 
100 KW/h tiếp theo được tính với giá 1100đ mỗi KW/h, 
những KW/h tiếp theo được tính với giá 1500đ mỗi KW/h.

Vd:
+ Số điện = 40 thì số tiền = 40*600=24000
+ Số điện = 70 thì số tiền = 50*600 + (70-50)*800=46000
+ Số điện = 110 thì số tiền = 50*600 + 50*800 + (110-50-50)*1100=81000
+ Số điện = 230 thì số tiền = 50*600 + 50*800 + 100*1100 + (230-50-50-100)*1500=225000

Dữ liệu vào
Một số nguyên n là số KW/h điện đã sử dụng

Dữ liệu ra
Số tiền cần trả

Ví dụ
Input #1 

280
Output #1 

300000
'''
n = int(input())
if n <= 50:
    tien = n*600
elif 50 < n <= 100:
    tien = 50*600 + (n-50)*800
elif 100 < n <= 200:
    tien = 50*600 + 50*800 + (n-100)*1100
elif n > 200:
    tien = 50*600 + 50*800 + 100*1100 + (n-200)*1500

print(tien)
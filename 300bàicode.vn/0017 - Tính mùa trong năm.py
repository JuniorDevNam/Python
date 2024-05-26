'''
Đề bài
Nhập một tháng (tây), cho biết tháng đó thuộc mùa nào (Xuân, Hạ, Thu, Ðông), biết rằng tháng 2, 3, 4 là mùa Xuân, tháng 5, 6, 7: mùa Hạ, tháng 8, 9, 10: mùa Thu, và tháng 11, 12, 1: mùa Ðông.

Dữ liệu vào
Một số nguyên t là một tháng trong năm.

Dữ liệu ra
Kết quả tháng đó thuộc mùa nào trong năm

Ví dụ
Input #1 
2
Output #1 
Mua Xuan

Input #2 
8
Output #2 
Mua Thu
'''
t = int(input())
if t in [2, 3, 4]:
    print("Mua Xuan")
elif t in [5, 6, 7]:
    print("Mua Ha")
elif t in [8, 9, 10]:
    print("Mua Thu")
elif t in [11, 12, 1]:
    print("Mua Dong")
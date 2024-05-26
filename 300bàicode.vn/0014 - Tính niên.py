'''Đề bài
Cho tuổi của một người (0<tuổi<=150), trả lời:

“Thieu nhi” nếu 0< tuổi<=11

“Thieu nien” nếu 11< tuổi <=25

“Trung nien” nếu 25< tuổi <=50

“Lao nien” nếu tuổi >50

Dữ liệu vào
Một số nguyên t là tuổi của một người

Dữ liệu ra
Kết quả theo mô tả trên

Ví dụ
Input #1 
31
Output #1 
Trung nien

Input #2 
8
Output #2 
Thieu nhi
'''
t = int(input())
if 0 < t <= 11:
    print("Thieu nhi")
elif 11 < t <= 25:
    print("Thieu nien")
elif 25 < t <= 50:
    print("Trung nien")
elif t > 50:
    print("Lao nien")
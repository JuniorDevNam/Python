'''
Đề bài
Viết chương trình nhập vào 1 tháng và năm, cho biết tháng đó có bao nhiêu ngày (Năm nhuận là năm chia hết cho 400 hoặc chia hết cho 4 nhưng không chia hết cho 100).

Dữ liệu vào
Hai số nguyên tháng và năm cách nhau bởi dấu cách

Dữ liệu ra
Kết quả tháng đó có bao nhiêu ngày


Ví dụ
Input #1 
1 2025
Output #1 
31

Input #2 
4 2030
Output #2 
30
'''
t, n = map(int,input().split())
if t in [1, 3, 5, 7, 8, 10, 12]:
    print("31")
elif t == 2:
    if n%4 == 0 and n%100 != 0:
        print("29")
    else:
        print("28")
else:
    print("30")
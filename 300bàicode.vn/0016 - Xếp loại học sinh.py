'''
Đề bài
Viết chương trình nhập vào điểm trung bình học kỳ I và trung bình học kỳ II, tính trung bình cả năm theo công thức:  TBCN=(TBHKI+TBHKII*2)/3. Xếp lọai theo cách:

“Gioi” nếu TBCN>=8

“Kha” nếu 6.5<=TBCN <8

“Trung binh” nếu 5.0<=TBCN <6.5

“Yeu” nếu 3.5<=TBCN <5

“Kem” nếu TBCN<3.5

Dữ liệu vào
Một dòng có 2 số thực cách nhau bởi dấu cách theo thứ tự là TBHKI và TBHKII

Dữ liệu ra
Dòng đầu là TBCN, làm tròn đến 1 chữ số thập phân; dòng thứ hai là xếp loại


Ví dụ
Input #1 
8 9
Output #1 
8.7
Gioi

Input #2 
4 7
Output #2 
6.0
Trung binh
'''

tbhk1, tbhk2 = map(float, input().split())
tbcn = (tbhk1 + tbhk2*2)/3
print(f'{tbcn:.1f}')
if tbcn >= 8:
    print("Gioi")
elif 6.5 <= tbcn < 8:
    print("Kha")
elif 5.0 <= tbcn < 6.5:
    print("Trung binh")
elif 3.5 <= tbcn < 5:
    print("Yeu")
elif tbcn < 3.5:
    print("Kem")
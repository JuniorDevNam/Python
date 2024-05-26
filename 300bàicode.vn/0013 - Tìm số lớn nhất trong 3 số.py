'''Đề bài
Viết chương trình nhập vào 3 số nguyên a, b, c; in ra số lớn nhất, nếu 3 số bằng nhau thì in dấu "="


Dữ liệu vào
Một dòng có 3 số nguyên cách nhau bởi dấu cách theo thứ tự là a, b và c


Dữ liệu ra
Số lớn nhất trong 3 số a, b, c hoặc dấu =

Ví dụ
Input #1 
-21 -46 -3
Output #1 
-3
Input #2 
4 44 -14
Output #2 
44
'''
a, b, c = map(int, input().split())
if a == b == c:
    print("=")
elif max([a,b,c]):
    print(max([a,b,c]))
    
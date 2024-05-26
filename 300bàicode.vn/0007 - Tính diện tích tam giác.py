'''Đề bài
Viết chương trình tính diện tích tam giác có chiều dài cạnh đáy a và chiều cao h tương ứng là các số nguyên theo công thức s=a*h/2.

Dữ liệu vào
Một dòng có 2 số nguyên cách nhau bởi dấu cách theo thứ tự là a và h.

Dữ liệu ra
Là diện tích làm tròn đến 2 chữ số thập phân

Ví dụ
Input #1 
6 4
Output #1 
12.00
Input #2 
10 5
Output #2 
25.00
'''

a, h = map(int,input().split())
s=a*h/2
print(f'{s:.2f}')
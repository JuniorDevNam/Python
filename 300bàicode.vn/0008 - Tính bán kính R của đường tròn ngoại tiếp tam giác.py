'''Đề bài
Viết chương trình tính bán kính R của đường tròn ngoại tiếp tam giác có ba cạnh a,b,c  là các số nguyên theo công thức R=(a*b*c)/(4*S), với S là diện tích tam giác (3 số a, b, c bảo đảm là 3 cạnh của 1 tam giác).

Dữ liệu vào
Một dòng có 3 số nguyên cách nhau bởi dấu cách theo thứ tự là a, b và c (đảm bảo là 3 cạnh của một tam giác).

Dữ liệu ra
Là R làm tròn đến 3 chữ số thập phân

Ví dụ
Input #1 
2 3 4
Output #1 
2.066
Input #2 
3 4 5
Output #2 
2.500'''

a, b, c = map(int, input().split())
p = (a + b + c)/2
S = (p*(p-a)*(p-b)*(p-c))**0.5
R = (a*b*c)/(4*S)
print(f'{R:.3f}')
'''
Đề bài
Viết chương trình tính chu vi (cv) và diện tích (s) một tam giác có 3 cạnh a, b, c 
là các số nguyên theo công thức cv=a+b+c, s=sqrt(p*(p-a)*(p-b)*(p-c)) 
với p=cv/2 (3 số a, b, c bảo đảm là 3 cạnh của 1 tam giác).


Dữ liệu vào
Gồm 1 dòng có 3 số nguyên cách nhau bởi dấu cách theo thứ tự là a, b và c.


Dữ liệu ra
Là chu vi và diện tích nằm trên cùng một dòng, cách nhau bởi dấu cách, chu vi làm tròn đến 1 chữ số thập phân, diện tích làm tròn đến 3 chữ số thập phân.


Ví dụ
Input #1 

2 3 4
Output #1 

9.0 2.905
'''
from math import sqrt
input = input()
a, b, c = map(float ,input.split())
cv = a + b + c
p = cv/2
s = sqrt(p*(p-a)*(p-b)*(p-c))
print(round(cv,1), round(s,3))
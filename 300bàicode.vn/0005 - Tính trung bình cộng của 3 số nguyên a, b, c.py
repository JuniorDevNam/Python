'''
Đề bài
Viết chương trình tính trung bình cộng của 3 số nguyên a, b, c theo công thức TBC=(a+b+c)/3


Dữ liệu vào
Một dòng có 3 số nguyên cách nhau bởi dấu cách theo thứ tự là a, b và c.


Dữ liệu ra
Là số trung bình cộng của a, b, c làm tròn đến 1 chữ số thập phân.


Ví dụ
Input #1 

-21 -46 -3
Output #1 

-23.3
'''

input = input()
a, b, c = map(int, input.split())
tbc = (a+b+c)/3
print(round(tbc,1))
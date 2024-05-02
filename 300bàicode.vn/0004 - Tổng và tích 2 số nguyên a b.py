'''
Đề bài
Viết chương trình tính tổng và tích 2 số nguyên a và b


Dữ liệu vào
Một  dòng có 2 số nguyên cách nhau bởi dấu cách theo thứ tự là a và b


Dữ liệu ra
Tổng và tích nằm trên cùng một dòng, cách nhau bởi dấu cách.
'''

input = input()
a, b = map(int, input.split())
print(a+b, a*b)
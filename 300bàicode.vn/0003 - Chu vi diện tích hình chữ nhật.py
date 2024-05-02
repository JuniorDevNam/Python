'''
Đề bài
Viết chương trình tính chu vi và diện tích hình chữ nhật, 
với chiều dài a và chiều rộng b là các số tự nhiên theo công thức cv=(a+b)*2, dt=a*b.


Dữ liệu vào
Gồm 1 dòng có 2 số nguyên a, b cách nhau bởi dấu cách theo thứ tự là chiều dài và chiều rộng


Dữ liệu ra
Là chu vi và diện tích nằm trên cùng một dòng, cách nhau bởi dấu cách.
'''
input = input()
a, b = map(int, input.split())

cv = (a+b)*2
dt = a*b
print(cv, dt)
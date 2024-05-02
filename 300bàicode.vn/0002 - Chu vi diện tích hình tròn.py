'''Đề bài
Viết chương trình tính chu vi và diện tích hình tròn, 
với bán kính r là số nguyên theo công thức cv=r*2*3.14, dt=r*r*3.14.


Dữ liệu vào
Một số nguyên dương r là bán kính hình tròn.


Dữ liệu ra
Là chu vi và diện tích của hình tròn nằm trên cùng một dòng,
cách nhau bởi dấu cách, làm tròn đến 2 chữ số thập phân.
'''

r = int(input())
cv = r*2*3.14
dt = r*r*3.14
print(round(cv,2), round(dt,2))


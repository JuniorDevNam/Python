# Viết chương trình  tìm  các số nguyên a, b, c, d khác nhau 
# trong khoảng 0 tới 10 thỏa mãn điều kiện:
# a*d*d= b*c*c*c

import random

#Ta đặt random cho b, c, d
#a ở đây sẽ là số cần tìm tùy biến theo thuật toán 
# để thỏa mãn a*d*d= b*c*c*c
b = random.randint(0,10)
c = random.randint(0,10)
d = random.randint(0,10)
#Check trùng random b, c, d và random lại
while b == c or b == d or d == c: 
    b = random.randint(0,10)
    c = random.randint(0,10)
    d = random.randint(0,10)
loaiTrubcd = [b, c, d] #Lấy danh sách b, c, d sau khi random xong
#Test xem kết quả của danh sách loaiTrubcd:
#print(loaiTrubcd)
num = []
for i in range(11):
    num += (i,) #Lấy danh sách tất cả các số từ 0 đến 10 
#Test xem kết quả của danh sách num:
#print(num)
A = set(num) ^ set(loaiTrubcd) #Danh sách các số còn lại loại trừ b, c, d
                            # Mục đích là để tránh trùng a với b, c, d
#Test xem kết quả của danh sách A
#print(A)
#Thuật toán tìm a
for a in A:
    check = a*d*d == b*c*c*c
    if check == True:
        break
print("Các số nguyên a, b, c, d khác nhau trong khoảng 0 - 10 thỏa mãn điều kiện a*d*d= b*c*c*c là:",a, b, c, d)
# Thuật toán random này sẽ không có kết quả giá trị cụ thể
# Mà ta phải check điều kiện của đề bài cho so với giá trị trả về

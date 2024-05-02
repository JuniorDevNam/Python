import random
import math
# Nhập vào 1 danh sách A gồm N phân tử
# Nhập N:
N = int(input("Nhập số phân tử N cho A: "))
# Tạo danh sách A có N phân tử gồm những số nguyên ngẫu nhiên từ khoảng -20 đến 20
A = [random.randint(-20, 20) for i in range(N)] # Gioi han random co the thay doi
# Xuất danh sách A:
print("Danh sách A hiện tại gồm:",A)
# 6. Tìm các số chính phương trong A
# Số chính phương là các cố có căn bậc 2 là số nguyên
# Số chính phương luôn hơn hơn 0
A_chinhPhuong = [] #Khởi tạo danh sách số chính phương
chinhPhuong = False #Biến logic
for x in A:
    if x > 0: # Kiểm tra x có dương?
        can2x = math.sqrt(x)
        can2xint = int(can2x)
        if can2x == can2xint: #Kết quả căn bậc 2 của x liệu có bằng số nguyên kết quả căn bậc 2 của x
            A_chinhPhuong.append(x)
            chinhPhuong = True
if chinhPhuong == True:
    print("6. Các số chính phương trong A là:",A_chinhPhuong)
if chinhPhuong == False:
    print("6. A không có số chính phương")
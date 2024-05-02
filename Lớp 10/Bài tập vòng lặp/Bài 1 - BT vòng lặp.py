# Cho dãy số vô hạn 12, 15, 18, 21,...
# Viết chương trình in ra số hạng thứ 2023

#Có công thức tìm số của vị trí số hạng:
#Số hạng thứ n = (n-1)*Khoảng cách + Số đầu

#Ta thấy dãy số vô hạn 12, 15, 18, 21,.. có khoảng cách là 3 
#Suy ra số hạng thứ 2023 là = (2023-1)*3+12

soHang2023 = (2023-1)*3+12

print("Cách 1: Số hạng thứ 2023 của dãy số vô hạn 12, 15, 18, 21,... là:",soHang2023)

#Cách 2:
# Dãy số này có quy luật là mỗi số hạng bằng số hạng trước đó cộng với 3
# Ta có thể sử dụng vòng lặp vô hạn while

# Khởi tạo số hạng đầu tiên
a = 12
# Khởi tạo biến đếm
count = 1
# Sử dụng vòng lặp for để tạo dãy số vô hạn
while count < 2023:
    # Tăng số hạng lên 3 đơn vị
    a += 3
    # Tăng biến đếm lên một đơn vị
    count += 1
    # Kiểm tra nếu biến đếm bằng 2023 thì thoát khỏi vòng lặp
    if count == 2023:
        break
# Xuất kết quả:
print("Cách 2: Số hạng thứ 2023 của dãy số vô hạn 12, 15, 18, 21,... là:",a)

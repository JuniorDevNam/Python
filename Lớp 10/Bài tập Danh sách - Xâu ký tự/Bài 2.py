# Giả sử có 1 giá trị N, nếu chúng ta muốn đổi N xu và chúng ta có nguồn cung vô hạn 
# với mỗi đồng xu có giá trị S={ S1; S2...; Sn} 
# Chúng ta có thể thực hiện bao nhiêu cách đổi tiền, thứ tự của các đồng xu không quan trọng.
# Ví dụ: Đôi N=4 và S={1,2,3} thì có 4 cách đối là {1,1,1,1}, {1,1,2}, {2,2}, {1, 3}
#       N=10 và S={2,3,5,6} thì có 5 cách là {2,2,2,2,2}; {2,2,3,3},{2,2,6}, {2,3,5}, {5,5}

import random

n = int(input("Nhập số tiền N: ")) # Số tiền N xu
m = int(input("Nhập số phân tử sẽ có trong danh sách S: ")) # Số phân tử sẽ có trong S

#Khởi tạo s
#Cách 1: Random giá trị xu trong khoảng 1 đến n+1 với m lần 
#Không dùng đến vì vậy đặt nó vào trạng thái comment
#s = [random.randint(1,n+1) for i in range(m)] 

#Cách 2: Nhập giá trị xu từ bàn phím với m lần bằng vòng lặp
s = [] #Khai triển 1 danh sách s rỗng
#Tạo 1 vòng lặp với m lần và nhập từng số 1 với bàn phím
for i in range(m):
    s.append(int(input("Nhập giá trị xu thứ " + str(i+1) + ":" )))

#Xuất ra màn hình các giá trị
print("Ta có giá trị N xu là:",n,"xu")
print("Ta có số phân tử trong list S là:",m,"phân tử")
print("Ta có các đồng xu có giá trị là S = ",s)

#Thiết lập 1 hàm đổi xu
def doiXu(S, m, n): #hàm doiXu với tham số lần lượt S, m, n
    
    # bangGiaTri[i] sẽ là nơi lưu trữ các số của giải pháp cho giá trị i.
    # Khởi tạo tất cả các giá trị trong list là 0
    bangGiaTri = [0 for k in range(n+1)] # Với bước này, mọi k trong số lần lặp n+1 sẽ là 0
    # Lý do chọn range là n+1 bởi vì phần tử đầu tiên [0] sẽ được dùng để đếm số cách đổi tiền
    bangGiaTri[0] = 1 # Gán dữ liệu "1" vào phân tử đầu tiên [0] trong list
    
    # Chọn từng đồng xu một và cập nhật giá trị cho bangGiaTri[] sau khi chỉ số lớn hơn hoặc bằng giá trị của đồng xu đã chọn
    for i in range(0,m): # xét i trong khoảng 0 đến m 
        for j in range(S[i],n+1): # xét j trong khoảng từ phân từ i của danh sách S đến n + 1
            bangGiaTri[j] += bangGiaTri[j-S[i]] # phân từ j trong bangGiaTri[] cộng thêm giá trị của phân tử mà kết quả
                                                # bằng j trừ đi giá trị của phân tử i trong S
 
    return bangGiaTri[n] # trả về phân tử n trong bangGiaTri[]

soLanDoi = doiXu(s, m, n) # Khai báo biến với dữ liệu là kết quả của thuật toán hàm đã định nghĩa
                            #với tham số đã nhập vào

print("Với",n,"xu, ta tìm được",soLanDoi,"cách đổi tiền")
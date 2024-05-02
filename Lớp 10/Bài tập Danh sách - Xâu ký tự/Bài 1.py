import random
import math

# Nhập vào 1 danh sách A gồm N phân tử

# Nhập N:
N = int(input("Nhập số phân tử N cho A: "))
# Tạo danh sách A có N phân tử gồm những số nguyên ngẫu nhiên từ khoảng -20 đến 20
A = [random.randint(-20, 20) for i in range(N)] # Gioi han random co the thay doi
# Xuất danh sách A:
print("Danh sách A hiện tại gồm:",A)

# 1. Sắp xếp A theo thứ tự tăng dần
A_tangDan = sorted(A)
print("1. Danh sách A theo thứ tự tăng dần là:",A_tangDan)

# 2. Loại bỏ bớt các phần tử giống nhau sao cho mỗi giá trị chỉ xuất hiện 1 lần duy nhất
#dict.fromkeys() sẽ là 1 danh sách từ điển nơi mà các keys là các phần từ duy nhất trong danh sách
A_loc = sorted(dict.fromkeys(A)) #Sắp xếp lại thứ tự từ điển
# Xuất kết quả
print("2. Danh sách A đã lược bớt giá trị lặp là:",A_loc)

# 3. Tìm số lớn nhất, nhỏ nhất trong A
A_max = max(A) #Số lớn nhất
A_min = min(A) #Số bé nhất
# Xuất kết quả:
print("3.1. Số lớn nhất trong A là:",A_max) 
print("3.2. Số bé nhất trong A là:",A_min)

# 4. Tìm số chẵn dương lớn nhất
A_chanDuong = [] #Khởi tạo danh sách số chẵn dương
chanDuong = False #1 biến lôgic kích hoạt điều kiện
for x in A_loc: #Xét các giá trị trong danh sách đã lọc số lặp
    if x % 2 == 0 and x > 0: #Điều kiện số chẵn dương
        A_chanDuong.append(x) #Thêm x vào danh sách
        chanDuong = True
if chanDuong == True: #điều kiện khi có số chẵn dương
    maxChanduong = max(A_chanDuong) #Số chẵn dương lớn nhất
    print("4. Số chẵn dương lớn nhất trong A là:",maxChanduong) #Xuất kết quả
else: #điều kiện khi không có số chẵn dương
    print("4. A không có số chẵn dương.") 

# 5. Tìm số âm lẻ nhỏ nhất trong A
A_amLe = [] #Khởi tạo danh sách số âm lẻ
leAm = False #Biến logic
for x in A_loc:
    if x % 2 != 0 and x < 0: #Điều kiện số lẻ âm
        A_amLe.append(x) #Thêm x vào danh sách
        leAm = True
if leAm == True:
    minLeAm = min(A_amLe) #Số lẻ âm nhỏ nhất
    print("5. Số âm lẻ nhỏ nhất trong A là:",minLeAm) #Xuất kết quả
else:
    print("5. A không có số lẻ âm.")

# 6. Tìm các số chính phương trong A
# Số chính phương là các cố có căn bậc 2 là số nguyên
# Số chính phương luôn hơn hơn 0
A_chinhPhuong = [] #Khởi tạo danh sách số chính phương
chinhPhuong = False #Biến logic
for x in A_loc:
    if x > 0: # Kiểm tra x có dương?
        can2x = math.sqrt(x)
        can2xint = int(can2x)
        if can2x == can2xint: #Kết quả căn bậc 2 của x liệu có bằng số nguyên kết quả căn bậc 2 của x
            A_chinhPhuong.append(x)
            chinhPhuong = True
if chinhPhuong == True:
    print("6. Các số chính phương trong A là:",A_chinhPhuong)
else:
    print("6. A không có số chính phương")

# 7. Tìm các số nguyên tố trong A
# Số nguyên tố là các số chỉ chia hết cho 1 và chính nó
A_nguyenTo = [] #Khởi tạo danh sách số nguyên tố
for x in A_loc:
    soNguyenTo = True #Giả sử x là số nguyên tố
    if x < 1: #Nếu x nhỏ hơn 1 thì không phải số nguyên tố
        soNguyenTo = False
    else: #Nếu x đã qua được điều kiện lớn hơn 1, tiếp tục xét x
        for i in range(2,int(math.sqrt(x))): #Duyệt các số từ 2 đến căn bậc 2 của x
            if x % i == 0: #Nếu x chia hết cho 1 số bất kỳ trong khoảng 2 đến căn 2 x
                soNguyenTo = False
                break #Kết thúc vòng lặp
    #Nếu x là số nguyên tố thì thêm vào danh sách
    if soNguyenTo == True:
        A_nguyenTo.append(x)
if soNguyenTo == False:
    print("7. A không có số nguyên tố")
else:
    print("7. A có các số nguyên tố là:",A_nguyenTo)

# 8. Tính trung bình cộng của các phân tử trong danh sách A
# sum() sẽ tính tổng của tất cả các phần tử có trong danh sách A
# len() sẽ đếm có bao nhiêu phần tử có trong danh sách A
trungBinhCong = sum(A) / len(A)
# Xuất kết quả
print("8. Trung bình cộng của dãy A là:",trungBinhCong)

# 9. Tìm các số lớn hơn giá trị trung bình và in ra vị trí của các số đó
largerthanaverage = [] #Khởi tạo danh sách các giá trị lớn hơn trung bình cộng
viTri = [] #Khởi tạo danh sách các vị trí lần lượt của số lớn hơn trung bình cộng
soLonHonTrungBinh = False #Biến logic
for vitri, x in enumerate(A): #Sử dụng hàm enumerate() để lấy chỉ số và giá trị của từng phần tử
    if x > trungBinhCong:
        largerthanaverage.append(x)
        viTri.append(vitri)
        soLonHonTrungBinh = True
if soLonHonTrungBinh == True:
    print("Các số lớn hơn số trung bình lần lượt là:",largerthanaverage,"tương ứng với các vị trí trong dãy A là:",viTri)
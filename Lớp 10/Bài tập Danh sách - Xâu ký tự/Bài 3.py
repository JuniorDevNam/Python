#Nhập vào B 1 chuỗi ký tự
B = str(input("Nhập 1 chuỗi ký tự B: "))

#Xuất ra màn hình chuỗi B
print("Chuỗi ký tự B là: ",B)

# 1. Kiểm tra B có ký tự số hay không?
chuSo = any(x.isnumeric() for x in B)
if chuSo == True:
  print("1. B có chứa ký tự số")
else:
  print("1. B không chứa ký tự số")
   
# 2. Kiểm tra B có ký tự in hoa không?
# Sử dụng hàm any() để duyệt ký tự
# Sau đó dùng .isupper() để check in hoa
inHoa = any(x.isupper() for x in B)
if inHoa == True:
  print("2. B có ký tự in hoa")
else:
  print("2. B không có ký tự in hoa")

# 3. Nhập vào ký 1 tự C bất kỳ rồi kiểm tra xem có C trong B hay không
# Nhập 1 ký tự C:
C = str(input("Nhập MỘT ký tự bất kỳ C: "))
print("Ký tự C bạn đã nhập là:",C) #Xuất C ra màn hình
#Check C có trong B:
if C in B:
  print("3. Ký tự C có trong chuỗi B")
else:
  print("3. Ký tự C không có trong chuỗi B")

# 4. Kiểm tra B có phải là xâu đối xứng hay không?
# Ta sử dụng hàm reversed()
# Hàm reversed() trả về một đối tượng lặp ngược các phần tử của một chuỗi
r = "".join(reversed(B)) #Nối các phân tử đã lặp ngược lại thành 1 chuỗi
if B == r: #So sánh đối xứng B với r
  print("4. Xâu B:",B,"là xâu đối xứng")
else:
  print("4. Xâu B:",B,"không phải là xâu đối xứng")

# 5. Chuẩn hóa xâu
# Xâu chuẩn hóa là xâu không có chứa dấu cách ở đầu và cuối câu, 
# giữa các ký tự chỉ có duy nhất 1 dấu cách
# Sử dụng hàm .strip()
chuanHoaXau = B.strip()
print("Chuỗi B (",B,") khi đã được chuẩn hóa xâu là:",chuanHoaXau)

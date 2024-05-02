# Nhập vào số lương và giờ làm việc trong tháng của một nhân viên, 
# sau đó tính tiền thưởng của nhân viên đó theo quy tắc sau:
# Nếu giờ làm việc >= 200 thì thưởng = 20% lương
# Nếu giờ làm việc >=100 và <200 thì thưởng = 10% lương
# Trường hợp còn lại thì thưởng = 0

# Nhập số lương và giờ làm việc
luong = int(input("Nhập số lương: "))
gio = float(input("Giờ làm việc: "))

# Kiểm tra giờ làm việc và tính tiền thưởng
if gio >= 200:
  luongthuong2 = 20/100*luong
  print("Tiền thưởng là:",luongthuong2,"đồng")

if gio >= 100 and gio < 200:
  luongthuong1 = 10/100*luong
  print("Tiền thưởng là:",luongthuong1,"đồng")

if gio < 100:
  luongthuong0 = 0
  print("Tiền thường là:",luongthuong0,"đồng")
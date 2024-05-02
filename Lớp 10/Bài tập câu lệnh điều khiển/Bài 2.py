# Nhập vào điểm trung bình (ĐTB) và xét học bổng đối với điểm trung bình đó theo quy tắc:
# ĐTB >=9 thì học bổng là 5.000.000 đ
# 8 <= ĐTB < 9 thì học bổng là 3.000.000đ
# 7<= ĐTB < 8 thì học bổng là: 1.000.000đ
# Trường hợp còn lại là 0 đồng

# Nhập ĐTB
dtb = float(input("Nhập điểm trung bình: "))

# Xét học bổng
if dtb >= 9:
  hocbong = 5000000
  print("Học bổng là:",hocbong,"đồng")
if 8 <= dtb < 9:
  hocbong = 3000000
  print("Học bổng là:",hocbong,"đồng")
if 7 <= dtb < 8:
  hocbong = 1000000
  print("Học bổng là:",hocbong,"đồng")
if dtb < 7:
  hocbong = 0
  print("Học bổng là:",hocbong,"đồng")
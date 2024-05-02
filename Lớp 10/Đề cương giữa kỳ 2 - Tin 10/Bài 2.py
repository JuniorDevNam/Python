# Nhập vào số điện tiêu thụ của gia đình bạn và viết chương trình tính số tiền phải trả biết:
#- 100 số đầu giá: 2000đ/số.
#- 50 số tiếp theo giá: 2500đ/số
#- 50 số tiếp theo giá: 3000đ/số
#- Các số tiếp theo tính giá: 4000đ/số.

n = int(input("Nhập số điện tiêu thụ: "))
if n<= 100:
 t = n*2000
elif n <= 150:
  t = 100*2000+(n-100)*2500
elif n <= 200:
  t = 100*2000+50*2500+(n-150)*3000
else:
  t = 100*2000+50*2500+50*3000+(n-200)*4000
print("Số tiền điện phải trả là:",t,"nghìn đồng")
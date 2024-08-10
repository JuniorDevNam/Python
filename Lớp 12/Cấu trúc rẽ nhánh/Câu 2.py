'''
Bài 2: Viết chương trình nhập vào số kw điện, tính và xuất ra số tiền phải trả (T) theo công thức sau:
          - Nếu kw <=100 thì Tính 2000 đ cho 1kw
          - Nếu 100<kw<=200 thì những kw vượt 100 tính 2500 đ cho 1 kw
'''
kw = int(input("Nhập vào số kw điện: "))
if kw <= 100: tien = kw*2000
elif 100 < kw <= 200: tien = 100*2000 + (kw-100)*2500
print("Số tiền phải trả là {}đ".format(tien))
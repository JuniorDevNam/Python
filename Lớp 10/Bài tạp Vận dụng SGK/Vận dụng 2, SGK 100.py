import sys
import math

# Input a,b,c
# Có thể dùng 3, 4, 5 để test do nó thỏa mãn lớn hơn 0 và bất đẳng thức
a = float(input("Nhập số thực dương a: "))
b = float(input("Nhập số thực dương b: "))
c = float(input("Nhập số thực dương c: "))
#Check "a,b,c > 0?"
print("1. Kiểm tra a,b,c > 0")
if a < 0 or b < 0 or c < 0:
  # Khi không thỏa mãn, chương trình sẽ bị dừng và hiện thông báo lỗi như dưới:
  sys.exit("a,b,c có số không thỏa mãn a,b,c > 0, xin nhập lại")
else:
  print("a thỏa mãn")
  print("b thỏa mãn")
  print("c thỏa mãn")
#Check Bất đẳng thức tam giác
print(" ")
print("2. Kiểm tra Bất đẳng thức tam giác")
if a + b < c or a + c < b or b + c < a:
  # Khi không thỏa mãn, chương trình sẽ bị dừng và hiện thông báo lỗi như dưới:
  sys.exit("a,b,c không thỏa mãn bất đẳng thức tam giác, xin nhập lại")
else:
  print("a, b, c thỏa mãn bất đẳng thức tam giác")
  print(" ")
chuvi = a + b + c
print("Chu vi của tam giác là: ",chuvi)
# p là nửa chu vi tam giác
p = float(chuvi/2)

dientich = math.sqrt(p*(p-a)*(p-b)*(p-c))
print("Diện tích của tam giác là: ",dientich)


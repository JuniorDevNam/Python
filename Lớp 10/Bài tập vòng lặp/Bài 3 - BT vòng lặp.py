# Nhập vào 1 số N
# Kiểm tra xem N có phải số nguyên tố hay không?
# Số nguyên tố là số chỉ có 2 ước duy nhất là 1 và chính nó

from math import sqrt

#Nhập N:
N = int(input("Nhập số N nguyên dương: "))
while N<2:
    N = int(input("Để kiểm tra số nguyên tố, cần phải nhập 1 số lớn hơn 1: "))

#Biến check nguyên tố:
laNguyenTo = True
canBacHaiN = int(sqrt(N)) #Căn bậc 2 của N

#Thuật toán:
for i in range(2,canBacHaiN+1): 
  if N%i == 0:
     laNguyenTo = False
     print(N,"không phải là số nguyên tố")
     break

if laNguyenTo == True:
   print(N,"là số nguyên tố")
   
# Nhập vào 1 số nguyên N từ bàn phím:
# Kiểm tra và in ra N có phải là số nguyên không?
# Kiểm tra tính chẵn lẻ của N.
# N có phải là số chẵn dương hay không?
# N có phải là số lẻ âm hay không?
# N có phải là số chính phương hay không?
# Nếu 0< N< 1000 thì kiểm tra N có phải số đặc biệt không? 
# số đặc biệt là số nguyên có tổng lập phương các chữ số bằng chính nó. 
# VD số 153 là số đặc biệt vì: 153 =  1^3 + 5^3 + 3^3

from math import sqrt

#Nhập số nguyên N
N = float(input("Nhập số bất kỳ N: "))

#N có phải số nguyên?
if N%1 == 0:
  N = int(N)
  print(N,"là số nguyên")
else:
  print(N,"không phải số nguyên")

#N chẵn hay lẻ?, chẵn dương?, lẻ âm?
if N%2 == 0:
  print(N,"là số chẵn")
  if N >= 0:
    print(N,"là số chẵn dương")
  else:
    print(N,"không phải là số chẵn dương")
else:
  print(N,"là số lẻ")
  if N < 0:
    print(N,"là số lẻ âm")
  else:
    print(N,"không phải là số lẻ âm")

#N có phải số chính phương?
if N > 0 and sqrt(N)%1 == 0:
    print(N,"là số chính phương")
else:
    print(N,"không phải là số chính phương")

#N có phải số đặc biệt?
while not 0 < N < 1000:
  N = float(input("N không thỏa mãn 0 < N < 1000, xin hãy nhập số khác:"))
while N%1 != 0:
  N = float(input("N không phải là số nguyên, xin nhập lại:"))

N = int(N)

donVi = N%10
chuc = N//10%10
tram = N//100%10
checkDacBiet = donVi**3 + chuc**3 + tram**3

print(N,"gồm Trăm =",tram,", Chục =",chuc,", Đơn vị =",donVi)

if checkDacBiet == N:
  print(N,"là số đặc biệt")
else:
  print(N,"không phải là số đặc biệt")
#Viết chương trình phân tích một số nguyên N thành tích các thừa số nguyên tố.
#VD:	 Nhập N=15 thì kết quả in ra là: 15=3x5
#             N= 16 thì kết quả in ra là: 16= 2x2x2x2

N = int(input("Nhập số nguyên N: "))
while N<2:
  N = int(input("Cần số nguyên N lớn hơn 2, xin nhập lại: "))

giatri = N
thuaSoNguyenTo = []

for i in range(2,N+1):
  while N%i == 0:
    thuaSoNguyenTo += (i,) #Tương đương thuaSoNguyenTo.append
    N = N/i

print("N =",giatri,"gồm tích thừa số nguyên tố là:", thuaSoNguyenTo)


# Viết chương trình in ra tất cả các số nguyên tố
# trong khoảng từ 2 đến N với N được nhập từ bàn phím

from math import sqrt

# Nhập N:
N = int(input("Nhập số N: "))
while N<2:
    N = int(input("N phải lớn hơn 1, xin nhập lại: "))

# Lấy tất cả các số từ 2 đến N
num = []
for n in range(2,N+1):
    num += (n,) #num.append
#Test:
#print("Danh sách từ 2 đến",N,"là:",num)

# Check số nguyên tố và loại khỏi danh sách những sô không phải số nguyên tố
khongPhaiSoNguyenTo = []
for i in num:
    canBacHai = int(sqrt(i))
    #Test:
    #print("Căn của",i,"là:",canBacHai)
    for s in range(2,canBacHai+1):
        if i%s == 0:
            khongPhaiSoNguyenTo += (i,)

soNguyenTo = set(num) ^ set(khongPhaiSoNguyenTo)

print("Các số nguyên tố từ 2 đến N (",N,") là:",soNguyenTo)
     
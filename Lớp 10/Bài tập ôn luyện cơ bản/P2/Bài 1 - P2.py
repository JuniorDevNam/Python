'''Viết chương trình nhập vào số nguyên n, xuất ra dãy số từ 1 đến n.'''


#Xuất dãy số 1 đến n
n = int(input("Nhập số nguyên n: "))
S = []
for k in range(1,n+1):
    S.append(k)
print(S) 


#Tính tổng 1 đến n
tong = 0
for x in range(1,n+1):
    tong = tong + x
print(tong)

#Đếm
#Ví dụ
s = 0
so = []
for x in range(1,n+1):
    if x%2 == 0:
        s = s + 1
        so.append(x)
print("Có",s,"số chẵn và đó là",so)
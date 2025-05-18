n = int(input())
A = list(map(int,input().split()))

#Cách 1: 60% điểm
so_lg, temp, temp2, bat_dau = 1, 1, 0, 0
for i in range(1,n):
    if A[i-1]*A[i] < 0:
        temp += 1
    else:
        if temp > so_lg:
            so_lg = temp
            bat_dau = temp2
        temp = 1
        temp2 = i
if temp > so_lg:
    so_lg = temp
    bat_dau = temp2
kq = A[bat_dau:bat_dau+so_lg]
print("{}\n{}".format(so_lg," ".join(str(x) for x in kq)))


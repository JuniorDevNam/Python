import sys, os
filein = os.path.join(sys.path[0],'bai10.inp')
fileout = os.path.join(sys.path[0],'bai10.out')
with open(filein, 'r') as file:
    i = file.readlines()
T = int(i[0])
np = (i[x] for x in range(1,T+1))
def giaithua(num):
    if num == 0 or num == 1:
        return 1
    else:
        return num * giaithua(num - 1)
kq = []
for x in np:
    N, P = map(int,x.split())
    ans = 0
    Nphay = giaithua(N)
    if N < P:
        kq.append(ans)
    else:
        for j in range(P, N+1, P):
            x = j
            while x % P == 0:
                ans += 1
                x //= P
        kq.append(ans)
with open(fileout, 'w') as file:
    file.write('\n'.join(str(x) for x in kq))
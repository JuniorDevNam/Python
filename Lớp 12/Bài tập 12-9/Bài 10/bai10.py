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
t = 1
for x in np:
    N, P = map(int,x.split())
    Nphay = giaithua(N)
    while 
from os.path import join
from sys import path
filein = join(path[0],"bai3.inp")
fileout = join(path[0],'bai3.out')
with open(filein, 'r') as file:
    i = file.readlines()
T = int(i[0])
kq = []
def xu_ly(N,A):
    if N < 2:
        return '0'
    lsum=0
    rsum = 0
    for i in range(N//2):
        lsum += A[i]
    for i in range(N//2, N):
        rsum += A[i]
    return lsum*rsum
for x in range(1,len(i),2):
    N, A = int(i[x]), list(map(int,i[x+1].split()))
    kq.append(xu_ly(N,A))
with open(fileout,'w') as file:
    file.write('\n'.join(str(x) for x in kq))
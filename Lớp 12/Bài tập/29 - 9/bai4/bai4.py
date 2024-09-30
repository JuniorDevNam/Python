from os.path import join
from sys import path
filein = join(path[0],'bai4.inp')
fileout = join(path[0],'bai4.out')
with open(filein, 'r') as file:
    i = file.readlines()
T = int(i[0])
kq = []
def xu_ly(N, A):
    cap = 0
    for i in range(N):
        for j in range(i+1,N):
            if i*A[i] > j*A[j]:
                cap += 1
    return cap
for x in range(1,len(i),2):
    N, A = int(i[x]), list(int,i[x+1].split())
    kq.append(xu_ly(N, A))
with open(fileout,'w') as file:
    file.write('\n'.join(str(x) for x in kq))
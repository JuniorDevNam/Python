from os.path import join
from sys import path
filein = join(path[0],'bai2.inp')
fileout = join(path[0],'bai2.out')
with open(filein,'r') as file:
    i = file.readlines()
T, kq = int(i[0]), []
def xu_ly(N,A):
    chan, le = [], []
    for i in A:
        if i % 2 == 0:
            chan.append(i)
        else:
            le.append(i)
    chan.sort()
    le.sort()
    return " ".join(str(x) for x in chan + le)
for x in range(1,len(i),2):
    N, A = int(i[x]), list(map(int,i[x+1].split()))
    kq.append(xu_ly(N,A))
with open(fileout, 'w') as file:
    file.write('\n'.join(str(x) for x in kq))
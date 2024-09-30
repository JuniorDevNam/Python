from os.path import join
from sys import path
filein = join(path[0],'bai1.inp')
fileout = join(path[0],'bai1.out')
with open (filein,'r') as file:
    i = file.readlines()
slg = int(i[0])
kq= []
def xu_ly(N,K,day_so):
    dem = 0
    for i in day_so:
        for c in str(i):
            if str(K) == c:
                dem += 1
    return dem
for x in range(1,len(i),2):
    N, K = map(int,i[x].strip().split())
    day_so = list(map(int,i[x+1].strip().split()))
    kq.append(xu_ly(N,K,day_so))
with open ( fileout,'w') as file:
    file.write("\n".join(str(x) for x in kq))



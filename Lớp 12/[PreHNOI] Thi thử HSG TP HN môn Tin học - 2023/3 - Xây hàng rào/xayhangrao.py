import sys, os
filein = os.path.join(sys.path[0],'xayhangrao.inp')
fileout = os.path.join(sys.path[0],'xayhangrao.out')
with open(filein, 'r') as file:
    i = file.readlines()
n, q = map(int,i[0].strip().split())
A = list(map(int,i[1].strip().split()))
B = list(map(int,i[2].strip().split()))
k = list(map(int,i[3].strip().split()))
A = sorted(A, reverse=True)
B = sorted(B, reverse=True)
kq = []
for i in range(q):
    x = k[i]
    max = sum(A[:x])
    kq.append(max)
with open(fileout, 'w') as file:
    file.write(str(" ".join(str(x) for x in kq)))
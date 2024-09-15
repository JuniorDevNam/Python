import sys, os
filein = os.path.join(sys.path[0],'bai3.inp')
fileout = os.path.join(sys.path[0],'bai3.out')
with open(filein, 'r') as file:
    i = file.readlines()
T = int(i[0])
nx = (i[x] for x in range(1,T+1))

tgkd, tgk = 0, 0

dskq = []
for _ in nx:
    N, X = map(int,_.split())
    tgkd = X*(N-1)
    tgk = 10*(N-1)
    kq = tgk - tgkd
    if kq < 0:
        kq = 0
    dskq.append(kq)
with open(fileout, 'w') as file:
    file.write('\n'.join(str(x) for x in dskq))
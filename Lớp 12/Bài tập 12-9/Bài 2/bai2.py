import sys, os
filein = os.path.join(sys.path[0],'bai2.inp')
fileout = os.path.join(sys.path[0],'bai2.out')
with open(filein, 'r') as file:
    i = file.readlines()
T = int(i[0].strip())
n = (int(i[x]) for x in range(1,T+1))
xx = [6, 5, 4, 3, 2, 1]
kq = []
for y in n:
    kq.append(xx[y-1])
with open(fileout, 'w') as file:
    file.write('\n'.join(str(x) for x in kq))
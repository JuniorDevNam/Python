import sys, os
filein = os.path.join(sys.path[0],'bai4.inp')
fileout = os.path.join(sys.path[0],'bai4.out')
with open(filein, 'r') as file:
    i = file.readlines()
T = int(i[0])
N = (int(i[x]) for x in range(1,T+1))
s, kq = 0, []
for x in N:
    s += x%2
    x //= 2
    if s%2 != 0:
        kq.append('odd')
    else: kq.append('even')
with open(fileout, 'w') as file:
    file.write('\n'.join(str(x) for x in kq))
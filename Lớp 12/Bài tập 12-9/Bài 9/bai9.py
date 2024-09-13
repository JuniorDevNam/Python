import sys, os
filein = os.path.join(sys.path[0],'bai9.inp')
fileout = os.path.join(sys.path[0],'bai9.out')
with open(filein, 'r') as file:
    i = file.readlines()
T = int(i[0])
N = (i[x].strip() for x in range(1,T+1))
kq = []
def thaotac(num):
    a = 0
    if len(str(num)) >= 2:
        for i in str(num):
            a += int(i)
        return thaotac(a)
    else:    
        return num
for x in N:
    kq.append(thaotac(x))
with open(fileout, 'w') as file:
    file.write('\n'.join(str(x) for x in kq))

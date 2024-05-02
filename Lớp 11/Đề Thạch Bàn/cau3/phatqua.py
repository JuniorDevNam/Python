from os.path import join
import sys
inp = join(sys.path[0],'phatqua.inp')
out = join(sys.path[0],'phatqua.out')

qua = open(inp,'r').read().split()
A = int(qua[0])
B = int(qua[1])
count = 0
for i in range(1,A+B):
    if A%i == 0 and B%i == 0:
        count += 1

with open(out,'w') as o:
    o.write(str(count))
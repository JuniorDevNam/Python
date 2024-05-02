from sys import path
from os.path import join
inp = join(path[0],'cau5.inp')
out = join(path[0],'cau5.out')
with open(inp,'r') as i:
    a = i.read()
b = list(map(int,a.split()))
c = []
for x in range(len(b)):
    if b[x] == min(b):
        c.append(x+1)
c = " ".join(str(x) for x in c)
with open(out,'w') as o:
    o.write(f'{min(b)}\n{c}')
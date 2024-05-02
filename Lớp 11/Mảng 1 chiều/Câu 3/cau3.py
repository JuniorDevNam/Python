from sys import path
from os.path import join as j
inp = j(path[0],'cau3.inp')
out = j(path[0],'cau3.out')
with open(inp,'r') as i:
    v = i.read()
b = list(map(int,v.split()))
a = []
for x in range(len(b)):
    if b[x] == max(b):
        a.append(x+1)
a = " ".join(str(i) for i in a)
with open(out,'w') as o:
    o.write(f'{max(b)}\n{a}')
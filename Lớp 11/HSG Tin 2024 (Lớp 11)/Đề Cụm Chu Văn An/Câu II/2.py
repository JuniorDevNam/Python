from sys import path as dir
from os.path import join
inp = join(dir[0],"TTD.INP")
out = join(dir[0],"TTD.OUT")

with open(inp,'r') as i:
    s = i.read()
s = list(map(int,s.split()))
t = 0
for x in range(1,s[0]+1,2):
    t = t + s[1]
with open(out,'w') as o:
    o.write(str(t))
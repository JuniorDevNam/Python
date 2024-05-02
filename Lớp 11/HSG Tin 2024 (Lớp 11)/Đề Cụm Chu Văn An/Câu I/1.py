from sys import path as dir
from os.path import join

inp = join(dir[0],"TH.INP")
out = join(dir[0],"TH.OUT")
with open(inp, 'r') as i:
    s = i.read()
s = list(map(int,s.split()))
r = str(abs(s[0]-s[1]))
with open(out,'w') as o:
    o.write(r)

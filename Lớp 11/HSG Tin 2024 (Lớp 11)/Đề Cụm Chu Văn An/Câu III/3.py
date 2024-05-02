from sys import path as dir
from os.path import join
inp = join(dir[0],"XKT.INP")
out = join(dir[0],"XKT.OUT")

with open(inp,'r') as i:
    s = i.readlines()
dem_kt = {}
r = ""
for x in range(1,int(s[0])+1):
    for c in s[x]:
        dem_kt[c] = dem_kt.get(c, 0) + 1
    for c, count in dem_kt.items(): 
        if count == 2:
            if c not in r:
                r = r + c
    dem_kt = {}
with open(out,'w') as o:
    o.write(r)
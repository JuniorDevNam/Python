import sys, os
filein = os.path.join(sys.path[0],"BS.INP")
fileout = os.path.join(sys.path[0],"BS.OUT")
with open(filein,'r') as o:
    s = list(map(int,o.read().split()))
n, x = s[0], s[1]
r = 0
for i in range(1,n+1):
    for j in range(1,n+1):
        if i*j == x:
            r += 1
with open(fileout,'w') as o:
    o.write(str(r))
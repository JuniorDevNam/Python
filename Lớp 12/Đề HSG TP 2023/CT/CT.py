import os, sys
filein = os.path.join(sys.path[0],"CT.INP")
fileout = os.path.join(sys.path[0]."CT.OUT")
with open(filein,'r') as o:
    s = o.readlines()
N, A = s[0], list(map(int,s[1].strip().split()))
tongtien = sum(A)
chiadoi = tongtien//2

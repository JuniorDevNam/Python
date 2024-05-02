from sys import path
from os.path import join
inp = join(path[0],'cau6.inp')
out = join(path[0],'cau6.out')
with open(inp,'r') as i:
    a = i.readlines()
r = a[1].split()

'''
Ý tưởng và Thuật toán như Câu 2 nhưng thay vì max thì là min (đề bài yêu cầu)
'''
from sys import path
from os.path import join
inp = join(path[0],'cau4.inp')
out = join(path[0],'cau4.out')
with open(inp,'r') as i:
    v = i.readlines()
n = int(v[0])
a = list(map(int,v[1].split()))
for x in range(n):
    if a[x] == min(a):
        r = x + 1
        break
with open(out,'w') as o:
    o.write(f'{min(a)}\n{r}')
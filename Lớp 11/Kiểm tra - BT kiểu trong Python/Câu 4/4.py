'''
Đề bài 4 - Tìm chuỗi con dài nhất trong chuỗi
Dữ liệu vào - 4.inp:
- Chuỗi đầu vào
Dữ liệu ra - 4.out:
- Chuỗi con dài nhất trong chuỗi
'''
from os.path import join
from sys import path
def kt_cdn(s):
    a = s.split()
    b = []
    c = len(max(a, key= len ))
    for x in a:
        if len(x) == c:
            b.append(x)
    b = ", ".join(str(d) for d in b)
    return b

inp = join(path[0],'4.inp')
out = join(path[0],'4.out')
with open(inp,'r',encoding='utf-8') as i:
    s = i.read()
with open(out,'w',encoding='utf-8') as o:
    o.write(kt_cdn(s))
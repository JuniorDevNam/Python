'''
Đề bài 3 - Đảo ngược chuỗi
Dữ liệu vào - 3.inp:
- Chuỗi đầu vào
Dữ liệu ra - 3.out:
- Chuỗi đã được đảo ngược
'''
from os.path import join
from sys import path
inp = join(path[0],'3.inp')
out = join(path[0],'3.out')
with open(inp,'r',encoding='utf-8') as i:
    s = i.read()
r = s[::-1]
with open(out,'w',encoding='utf-8') as o:
    o.write(r)
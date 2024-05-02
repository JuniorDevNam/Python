'''
Đề bài 6 - Loại bỏ khoảng trắng đầu và cuối của một chuỗi.

Thuật toán:
- Sử dụng hàm strip() để cắt các khoảng trắng của chuỗi
'''
from os.path import join
from sys import path
inp = join(path[0],'6.inp')
out = join(path[0],'6.out')

with open(inp,'r',encoding='utf-8') as i:
    s = i.read()
stripped = s.strip()
with open(out,'w',encoding='utf-8') as o:
    o.write(stripped)

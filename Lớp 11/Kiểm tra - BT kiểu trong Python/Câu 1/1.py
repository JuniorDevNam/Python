'''
Đề bài 1 - Tạo một chuỗi và in ra màn hình.
Dữ liệu vào - 1.inp:
- Chuỗi đầu vào
Dữ liệu ra - in lên màn hình với print()
'''
from os.path import join
from sys import path
inp = join(path[0],'1.inp')
with open(inp,'r',encoding='utf-8') as i:
    r = i.read()
print(r)
'''
Đề bài 7 - Chuyển một chuỗi sang viết hoa hoặc viết thường.
Dữ liệu vào - 7.inp:
- Dòng 1 là chuỗi viết thường.
- Dòng 2 là chuỗi viết hoa.
Dữ liệu ra - 7.out:
- Dòng 1 là chuỗi thường đã được chuyển thành hoa.
- Dòng 2 ngược lại.

Thuật toán:
- Hàm upper() và hàm lower()
'''
from os.path import join
from sys import path
inp = join(path[0],'7.inp')
out = join(path[0],'7.out')

def hoa(s):
    r = s.upper()
    return r
def thuong(s):
    r = s.lower()
    return r

with open(inp,'r',encoding='utf-8') as i:
    s = i.readlines()
with open(out,'w',encoding='utf-8') as o:
    o.write(f'{hoa(str(s[0]))}{thuong(str(s[1]))}')
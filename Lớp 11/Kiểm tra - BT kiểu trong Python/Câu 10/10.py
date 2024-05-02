'''
Đề bài 10 - Tìm số lần xuất hiện của một chuỗi con trong một chuỗi khác
Dữ liệu vào - 10.inp
- Chuỗi dữ liệu vào
Dữ liệu vào - 10_1.inp
- Chuỗi con cần tìm số lần xuất hiện trong chuỗi đầu vào
Dữ liệu ra - 10.out: Số lần từ đó xuất hiện

Thuật toán:
- Hàm count()
'''
from os.path import join
from sys import path
inp = join(path[0],'10.inp')
inp2 = join(path[0],'10_1.inp')
out = join(path[0],'10.out')
def kt_chuoi(s, c):
    return s.count(c)

with open(inp,'r',encoding='utf-8') as i:
    #s = i.read()
    #Trong phần nhập dữ liệu vào đang nhập 1 lời bài hát với nhiều dòng nên là dùng hàm dưới đây:
    s = i.readlines()
s = " ".join(str(x) for x in s)
with open(inp2,'r',encoding='utf-8') as i:
    c = i.read()
c = c.replace("\n","")
with open(out,'w',encoding='utf-8') as o:
    o.write(f'\'{c}\' xuất hiện: {kt_chuoi(s,c)}')
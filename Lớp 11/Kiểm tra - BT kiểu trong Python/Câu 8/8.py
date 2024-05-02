'''
Đề bài 8 - Tách một chuỗi dựa trên ký tự hoặc chuỗi trắng.
Dữ liệu vào - 8.inp:
- Dòng 1: Đây là trường hợp tách chuỗi với ký tự trắng
- Dòng 2: Ký tự trắng
Dữ liệu vào - 8_2.inp:
- Dòng 1: Đây là trường hợp tách chuỗi với một ký tự được chỉ định
- Dòng 2: Ký tự được chỉ định: "a"

Thuật toán:
- Viết 1 hàm tự định nghĩa
    + Sử dụng split()
    + Đọc dữ liệu đầu vào rồi xét 2 trường hợp trên
- Trả về kết quả và ghi ra file xuất
'''
from os.path import join
from sys import path
inp = join(path[0],'8.inp')
inp2 = join(path[0],'8_2.inp')
out = join(path[0],'8.out')

def tach(s):
    chuoi = str(s[0])
    chuoi = chuoi.replace("\n","")
    k = str(s[1])
    r = chuoi.split(k)
    return r


with open(inp,'r',encoding='utf-8') as i1:
    s1 = i1.readlines()
    
with open(inp2,'r',encoding='utf-8') as i2:
    s2 = i2.readlines()

with open(out,'w',encoding='utf-8') as o:
    o.write(f'{tach(s1)}\n{tach(s2)}')
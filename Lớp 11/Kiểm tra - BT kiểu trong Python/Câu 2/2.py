'''
Đề bài 2 - Tìm tần suất xuất hiện của một ký tự trong chuỗi.
Dữ liệu vào - 2.inp:
- Dòng 1 là chuỗi đầu vào
- Dòng 2 là ký tự cần đếm tần suất xuất hiện trong chuỗi
Dữ liệu ra - 2.out:
- Số lần mà ký tự đó xuất hiện trong chuỗi
'''
from os.path import join
from sys import path
inp = join(path[0],'2.inp')
out = join(path[0],'2.out')
with open(inp,'r',encoding='utf-8') as i:
    a = i.readlines()
string = str(a[0])
char = str(a[1])
count = string.count(char)
with open(out,'w') as o:
    o.write(str(count))



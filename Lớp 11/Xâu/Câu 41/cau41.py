'''
Ý tưởng:
Đọc dữ liệu từ file
Sử dụng hàm upper() để chuyển xâu thường thành xâu hoa
Ghi kết quả ra file
'''
from sys import path
from os.path import join
inp = join(path[0],'cau41.inp')
out = join(path[0],'cau41.out')
with open(inp,'r') as i:
    a = i.read()
r = a.upper()
with open(out,'w') as o:
    o.write(r)
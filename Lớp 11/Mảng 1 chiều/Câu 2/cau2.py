'''
Ý tưởng, Thuật toán:
- Hàm readlines để đọc các dòng dữ liệu trong file input
- Dòng 1 chuyển sang dạng số nguyên n
- Tách dòng hai thành mảng giá trị số nguyên l
    + split
    + list
    + map
    + int
- Vòng lặp xét với range = n vì n bằng len(l) theo đề bài cho
    + Nếu tại vị trí x trong mảng l bằng max(l)
        * Khởi tạo biến p bằng x + 1
        * đây là vị trí của phần tử lớn nhất đầu tiên trong mảng
        * break - dừng vòng lặp
- Ghi kết quả ra file output
'''
from sys import path
from os.path import join
inp = join(path[0],'cau2.inp')
with open(inp,'r') as i:
    v = i.readlines()
out = join(path[0],'cau2.out')
n = int(v[0])
l = list(map(int, v[1].split()))
for i in range(n):
    if l[i] == max(l):
        p = i + 1
        break
with open(out,'w') as o:
    o.write(f'{max(l)}\n{p}')
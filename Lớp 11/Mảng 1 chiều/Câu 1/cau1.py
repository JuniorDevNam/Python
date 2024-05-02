'''
Ý tưởng và thuật toán
- Đọc và ghi dãy số dữ liệu nhập vào từ tệp bằng with open
- Tách thành mảng giá trị số thực
    + split
    + list
    + map
    + float
- Tính tổng mảng và chia cho số phần tử mà mảng có để tìm trung bình cộng
    + sum
    + len
- Duyệt mảng để tìm các giá trị lớn hơn giá trị trung bình
    + vòng lặp for
- Tạo một biến đếm để đếm số giá trị đó
'''
from sys import path
from os.path import join
inp = join(path[0],'cau1.inp')
out = join(path[0],'cau1.out')
count = 0
with open(inp,'r') as i:
    v = i.read()
t = list(map(float,v.split()))
t.sort(reverse=True)
tbc = round(sum(t)/(len(t)),1)

for x in t:
    if x > tbc:
        count += 1
    else:
        break

with open(out,'w') as o:
    o.write(f'{tbc}\n{count}')

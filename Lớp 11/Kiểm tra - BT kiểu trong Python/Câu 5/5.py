'''
Đề bài 5 - Tìm chuỗi con xuất hiện nhiều nhất trong một chuỗi.
Dữ liệu vào - 5.inp:
- Chuỗi đầu vào
Dữ liệu ra - 5.out:
- Chuỗi con xuất hiện nhiều nhất trong chuỗi
Thuật toán:
- Sử dụng từ điển (dictionary) để đếm số lần xuất hiện của một từ
    + {} biểu thị cho 1 từ điển
    + Hàm get()
- Sử dụng hàm max() để tìm trong từ điển từ có tần suất nhiều nhất
'''
from os.path import join
from sys import path
inp = join(path[0],'5.inp')
out = join(path[0],'5.out')

def kt_cxhnn(s):
    a = s.split()
    b = {}
    for x in a:
        #Dòng này cập nhật từ điển "b". Nếu từ đã tồn tại trong từ điển, nó sẽ tăng giá trị tương ứng lên 1. Nếu không, nó sẽ thêm từ vào từ điển với giá trị ban đầu là 0 và sau đó tăng lên 1 nếu nó có lặp lại.
        b[x] = b.get(x, 0) + 1
    r = max(b, key=b.get)
    return r

with open(inp,'r',encoding='utf-8') as i:
    #s = i.read()
    #Trong phần nhập dữ liệu vào đang nhập 1 lời bài hát với nhiều dòng nên là dùng hàm dưới đây:
    s = i.readlines()
s = " ".join(str(x) for x in s)
with open(out,'w',encoding='utf-8') as o:
    o.write(kt_cxhnn(s))
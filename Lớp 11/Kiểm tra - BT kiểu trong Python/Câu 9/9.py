'''
Đề bài 9 - Kiểm tra xem chuỗi có phải là palindrome hay không
Chuỗi Palindrome - Chuỗi đối xứng

Thuật toán:
- Sử dụng phương thức kiểm tra đối xứng:
    + A[::] == A[::-1]
    + Chuỗi A[::-1] tương đương với việc lấy chuỗi a và đảo ngược thứ tự của các ký tự
'''
from os.path import join
from sys import path
inp = join(path[0],'9.inp')
out = join(path[0],'9.out')

def kt_dx(s):
    return s == s[::-1]


with open(inp,'r',encoding='utf-8') as i:
    s = i.readlines()
with open(out,'w',encoding='utf-8') as o: #Reset kết quả bên file ouput
    o.write("")
with open(out,'a',encoding='utf-8') as o: #Sử dụng phương thức thêm kết quả nên sẽ không ghi đè kết quả cũ -> Cần reset kết quả cũ của lần chạy trước
    for x in s:
        x = x.replace("\n","")
        if kt_dx(x):
            r = f"Chuỗi {x} là palindrome."
            o.write(r + "\n")
        else:
            r = f"Chuỗi {x} không phải là palindrome."
            o.write(r + "\n")
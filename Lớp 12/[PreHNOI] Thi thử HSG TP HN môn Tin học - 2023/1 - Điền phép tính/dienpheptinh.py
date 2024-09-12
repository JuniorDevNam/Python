import sys, os
filein = os.path.join(sys.path[0],'dienpheptinh.inp')
fileout = os.path.join(sys.path[0],'dienpheptinh.out')
with open(filein, 'r') as file:
    i = file.readlines()
A, B = int(i[0].strip()), int(i[1].strip())
pheptinh, a, b, c, d = ['+','-','*'], '', 0, [], []
for i in pheptinh:
    for j in pheptinh:
        a = f'A{i}A{j}A'
        b = eval(a)
        c.append(b)
        d.append([i,j])

def ketqua(pos):
    with open(fileout, 'w') as file:
        file.write(str("\n".join(kq for kq in d[pos])))
for x in range(len(c)):
    if c[x] == B:
        ketqua(x)
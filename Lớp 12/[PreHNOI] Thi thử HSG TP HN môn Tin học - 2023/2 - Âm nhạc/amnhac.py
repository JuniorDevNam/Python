import sys, os

filein = os.path.join(sys.path[0], 'amnhac.inp')
fileout = os.path.join(sys.path[0], 'amnhac.out')

with open(filein, 'r') as file:
    i = file.readlines()

N, K = int(i[0].strip().split()[0]), int(i[0].strip().split()[1])
S = i[1].strip()
T = S * K

t, a, b, d = '', 0, 0, ''
for i in range(N):
    if i == 0:
        d = T[i + 1]
        t = T.replace(T[i], d)
        a = t.count(d)
        if a > b:
            b = a
    elif i == N - 1:
        d = T[i - 1]
        t = T.replace(T[i], d)
        a = t.count(d)
        if a > b:
            b = a
    else:
        d = T[i + 1]
        t = T.replace(T[i], d)
        a = t.count(d)
        if a > b:
            b = a
        d = T[i - 1]
        t = T.replace(T[i], d)
        a = t.count(d)
        if a > b:
            b = a

with open(fileout, 'w') as file:
    file.write(str(b))

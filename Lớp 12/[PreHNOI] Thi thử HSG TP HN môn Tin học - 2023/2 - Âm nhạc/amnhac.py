import sys, os
filein = os.path.join(sys.path[0], 'amnhac.inp')
fileout = os.path.join(sys.path[0], 'amnhac.out')
with open(filein, 'r') as file:
    i = file.readlines()

N, K = int(i[0].strip().split()[0]), int(i[0].strip().split()[1])
S = i[1]
T = S * K
#print(N,T)
t, b, d = '', [], ''

t = T.replace(T[0], T[1])
b.append(t.count(T[1]))

t2 = T.replace(T[N-1], T[N-2])
b.append(t2.count(T[N-2]))

for i in range(1,N-2):
    d = T[i+1]
    c = T[i-1]
    t = T.replace(T[i], d)
    t3 = T.replace(T[i], c)
    b.append(t.count(d))
    b.append(t.count(c))

with open(fileout, 'w') as file:
    file.write(str(max(b)))

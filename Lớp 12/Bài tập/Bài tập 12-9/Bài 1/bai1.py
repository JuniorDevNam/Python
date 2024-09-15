import sys, os
filein = os.path.join(sys.path[0],'bai1.inp')
fileout = os.path.join(sys.path[0],'bai1.out')
with open(filein, 'r') as file:
    i = file.readlines()
T = int(i[0].strip())
n = [i[x] for x in range(1,T+1)]
z = []
for x in n:
    if '0' in x:
        y = x.replace('0','5')
        z.append(y)
    else:
        z.append(x)
with open(fileout, 'w') as file:
    file.write("".join(str(x) for x in z))

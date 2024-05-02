from os.path import join
import sys
inp = open(join(sys.path[0],'dauvao.inp'))
ds=inp.readlines()
dsmay = ds[0].split()
so = ds[1]
print(dsmay,so)
count = 0
for i in str(so):
    if i in dsmay:
        count += 1
print(count)
r = 0
for x in dsmay:
    if count == int(x):
        r += 1
if r == 1:
    print("YES")
else:
    print("NO")
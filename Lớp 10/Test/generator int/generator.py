import random
from sys import path
from os.path import join
inp = join(path[0],'inp.inp')
with open(inp,'r') as i:
    v = i.readlines()
out = join(path[0],'out.out')

n = int(v[0])
f = int(v[1])
t = int(v[2])

daily_temperatures = []
for i in range(n):
    x = random.randint(f, t)
    daily_temperatures.append(x)
daily_temperatures = ' '.join(map(str, daily_temperatures))

with open(out,'w') as o:
    o.write(daily_temperatures)
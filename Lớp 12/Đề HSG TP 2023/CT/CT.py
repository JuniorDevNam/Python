import os, sys
#from collections import Counter
filein = os.path.join(sys.path[0],"CT.INP")
with open(filein,'r') as o:
    s = o.readlines()

def result(string):
    fileout = os.path.join(sys.path[0],"CT.OUT")
    with open(fileout, 'w') as file:
        file.write(str(string))

N, A = int(s[0].strip()), list(map(int,s[1].strip().split()))
maxtien = sum(A)/2
target = sum(A)//2
a, b, gtA = 0, 0, []
if maxtien == target:
    result(int(maxtien))
else:
    for i in range(N-1):
        a = A[i]
        for j in range(i+1,N):
            b = a + A[j]
            if b < maxtien:
                gtA.append(b)
    count = {}

    for num in gtA:
        if num in count:
            count[num] += 1
        else:
            count[num] = 1
    max_value = max([key for key, value in count.items() if value == 2], default=None)
    result(max_value)









from random import randint
import sys, os
sys.stdout = open(os.path.join(sys.path[0],'ngaunhien.out'),'w')
N = int(input())
K = int(input())
A = []
i = 0
while i < N:
    x = randint(1,K)
    A.append(x)
    i += 1
print(" ".join(str(x) for x in A))
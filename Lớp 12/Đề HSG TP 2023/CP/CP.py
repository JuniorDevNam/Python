import os, sys
filein = os.path.join(sys.path[0],"CP.INP")

def snt(n):
    if n <= 1:
        return False
    for x in range(2, int(n**0.5) + 1):
        if n % x == 0:
            return False
    return True

def scp(n):
    return n**0.5 == int(n**0.5)
def ketqua(kq):
    fileout = 
s = list(map(int, input().strip().split()))
a, b = s[0], s[1]
scp_list, scpdb = [], 0

for i in range(a, b + 1):
    if scp(i):
        scp_list.append(i)

for x in scp_list:
    if snt(int(x**0.5)):
        scpdb += 1

print(scpdb)
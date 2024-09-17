import sys, os
filein = os.path.join(sys.path[0],'chiamang.inp')
fileout = os.path.join(sys.path[0],'chiamang.out')
with open(filein,'r') as file:
    i = file.readlines()
def ketqua(kq):
    with open(fileout, 'w') as file:
        file.write(str(kq))
n = int(i[0].strip())
nums = [int(i[x]) for x in range(1,n+1)]
half = sum(nums/2)
a, kq = 0, 0
if half != int(half):
    ketqua(kq)
for i in range(n):
    a+=nums[i]
    if a == half:
        ketqua(i)
        break


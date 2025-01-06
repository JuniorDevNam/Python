import sys, os
import time
input_file = os.path.join(sys.path[0],'daycon.inp')
output_file = os.path.join(sys.path[0],'daycon.out')
sys.stdin = open(input_file, 'r')
sys.stdout = open(output_file, 'w')
start_time = time.time()
N = int(input())
A = list(map(int,input().split()))
def snt(n):
    if n < 2:
        return False
    if n == 2:
        return True
    if n > 2:
        cnt = 0
        for x in range(2,int(n**0.5)+1):
            if n % x == 0:
                cnt += 1
                break
        if cnt == 0:
            return True
        else:
            return False
vi_tri = []
for x in range(N):
    if snt(A[x]) == True:
        vi_tri.append(x)
length = 9*10**9
e = len(vi_tri)
for i in range(e):
    for j in range(i+1,e):
        l = len(A[vi_tri[i]:vi_tri[j]+1])
        if l < length:
            length = l
print(l)
end_time = time.time()
print(f"{end_time - start_time} giây")
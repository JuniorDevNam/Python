import sys, os
input_file =os.path.join(sys.path[0],'TICHLIENTIEP.INP')
output_file =os.path.join(sys.path[0],'TICHLIENTIEP.OUT')
sys.stdin = open(input_file,'r')
sys.stdout = open(output_file,'w')
ans = -1
N = int(input())
i = 1
while i * (i + 1) <= N:
    if i * (i + 1) == N:
        ans = i
        break
    i += 1
print(ans)
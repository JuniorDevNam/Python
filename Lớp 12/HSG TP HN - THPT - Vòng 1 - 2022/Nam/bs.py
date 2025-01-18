import sys, os
input_file = os.path.join(sys.path[0],'bs.inp')
output_file = os.path.join(sys.path[0],'bs.out')
sys.stdin = open(input_file, 'r')
sys.stdout = open(output_file, 'w')
n, x = map(int,input().split())
cnt = 0
for i in range(1,n+1):
    if x % i == 0:
        j = x // i
        if j <= n:
            cnt += 1
print(cnt)

        
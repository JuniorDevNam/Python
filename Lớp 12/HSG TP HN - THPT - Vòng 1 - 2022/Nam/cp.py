import sys, os
input_file = os.path.join(sys.path[0],'cp.inp')
output_file = os.path.join(sys.path[0],'cp.out')
sys.stdin = open(input_file, 'r')
sys.stdout = open(output_file, 'w')

a, b = map(int,input().split())

max_val = int(b**0.5)
is_prime = [True] * (max_val+1)
is_prime[0] = is_prime[1] = False

for i in range(3, int(max_val**0.5) + 1,2):
    if is_prime[i] == True:
        for j in range(i*i,max_val+1,i):
            is_prime[j] = False
            
cnt = 0
for x in range(a,b+1):
    sqrt = int(x**0.5)
    if sqrt*sqrt == x and is_prime[sqrt]:
            cnt += 1
print(cnt)

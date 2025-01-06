import time
start_time = time.time()

import sys, os
input_file = os.path.join(sys.path[0],'daycon.inp')
output_file = os.path.join(sys.path[0],'daycon.out')
sys.stdin = open(input_file, 'r')
sys.stdout = open(output_file, 'w')

def snt(n):
    if n < 2:
        return False
    for x in range(2, int(n**0.5) + 1):
        if n % x == 0:
            return False
    return True

N = int(input())
A = list(map(int, input().split()))

is_prime = [snt(i) for i in range(max(A)+1)]

vi_tri = [i for i in range(N) if A[i] >= 0 and is_prime[A[i]]]

if len(vi_tri) < 2:
    print(-1)
else:
    min_length = float('inf')
    for i in range(len(vi_tri) - 1):
        min_length = min(min_length, vi_tri[i + 1] - vi_tri[i] + 1)
    print(min_length)

end_time = time.time()
print(f"{end_time - start_time} giây")
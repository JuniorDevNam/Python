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
    if n in (2, 3):
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
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
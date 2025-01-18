import time
start_time = time.time()

import sys, os
input_file = os.path.join(sys.path[0], 'daycon.inp')
output_file = os.path.join(sys.path[0], 'daycon.out')
sys.stdin = open(input_file, 'r')
sys.stdout = open(output_file, 'w')


N = int(input())
A = list(map(int, input().split()))

max_val = max(A)
is_prime = [True] * (max_val + 1)
is_prime[0] = is_prime[1] = False

#Thuật toán sàng Eratosthenes
for i in range(2, int(max_val**0.5) + 1):
    if is_prime[i]:
        for j in range(i * i, max_val + 1, i):
            is_prime[j] = False

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
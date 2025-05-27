import sys, os
input_file = os.path.join(sys.path[0], "muasam.INP")
output_file = os.path.join(sys.path[0], "muasam.OUT")
sys.stdin = open(input_file, 'r')
sys.stdout = open(output_file, 'w')
N, L, R = map(int, input().split())
A = list(map(int, input().split()))
A.sort()
As = list(set(A))
r, broke = 0, False
for i in range(N):
    for j in range(i+1, N):
        r = A[i] + A[j]
        if L <= r <= R:
            broke = True
            break
    if broke:
        break
print(r)
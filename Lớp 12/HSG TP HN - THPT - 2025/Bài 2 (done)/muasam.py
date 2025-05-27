import sys, os
input_file = os.path.join(sys.path[0], "muasam.INP")
output_file = os.path.join(sys.path[0], "muasam.OUT")
sys.stdin = open(input_file, 'r')
sys.stdout = open(output_file, 'w')
N, L, R = map(int, input().split())
A = list(map(int, input().split()))
A.sort()
found = False
for i in range(N):
    for j in range(i+1, N):
        s = A[i] + A[j]
        if L <= s <= R:
            print(s)
            found = True
            break
    if found:
        break
if not found:
    print(-1)
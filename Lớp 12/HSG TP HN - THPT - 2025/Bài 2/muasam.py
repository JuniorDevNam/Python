
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
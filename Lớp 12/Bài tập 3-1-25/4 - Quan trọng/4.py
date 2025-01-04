N = int(input())
A = list(map(int, input().split()))
B = []
for i in range(N):
    for j in range(i+1,N):
        if A[i] == A[j]:
            B.append(A[i:j+1])
print(sum(max(B)))

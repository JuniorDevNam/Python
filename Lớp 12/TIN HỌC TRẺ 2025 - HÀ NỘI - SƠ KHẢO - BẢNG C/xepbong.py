from itertools import permutations

n, a, b, c, w = map(int, input().split())
f1_flat = list(map(int, input().split()))
f2_flat = list(map(int, input().split()))
f3_flat = list(map(int, input().split()))
f_flat = list(map(int, input().split()))

# Chuyển f1, f2, f3 thành ma trận n x n
f1 = [f1_flat[i*n:(i+1)*n] for i in range(n)]
f2 = [f2_flat[i*n:(i+1)*n] for i in range(n)]
f3 = [f3_flat[i*n:(i+1)*n] for i in range(n)]

# Chuyển f thành mảng 3 chiều
f = [[[0]*n for _ in range(n)] for _ in range(n)]
idx = 0
for i in range(n):
    for j in range(n):
        for k in range(n):
            f[i][j][k] = f_flat[idx]
            idx += 1

max_score = 0
for perm_r in permutations(range(n)):
    for perm_y in permutations(range(n)):
        used_y = set()
        valid = True
        score = 0
        for i in range(n):
            j = perm_r[i]
            k = perm_y[i]
            if k in used_y:
                valid = False
                break
            used_y.add(k)
            score += a * f1[i][j]
            score += b * f2[i][k]
            score += c * f3[j][k]
            score += w * f[i][j][k]
        if valid:
            max_score = max(max_score, score)

print(max_score)
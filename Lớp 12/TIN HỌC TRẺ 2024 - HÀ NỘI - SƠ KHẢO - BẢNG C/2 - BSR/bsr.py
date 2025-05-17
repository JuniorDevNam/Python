import os, sys
input_file = os.path.join(sys.path[0], "bsr.INP")
sys.stdin = open(input_file, 'r')

m, n = map(int, input().split())
table = [ list(map(int, input().split())) for _ in range(m) ]
prefix = [[0] * (n) for _ in range(m)]
count = 0
for r in range(m):
    for c in range(n):
        prefix[r][c] = table[r][c]
        if r > 0:
            prefix[r][c] += prefix[r-1][c]
        if c > 0:
            prefix[r][c] += prefix[r][c-1]
        if r > 0 and c > 0:
            prefix[r][c] -= prefix[r-1][c-1]
def tinh_tong(c1, r1, c2, r2):
    if r1 == 0 and c1 == 0:
        return prefix[r2][c2]
    if r1 == 0:
        return prefix[r2][c2] - prefix[r2][c1-1]
    if c1 == 0:
        return prefix[r2][c2] - prefix[r1-1][c2]
    return prefix[r2][c2] - prefix[r1-1][c2] - prefix[r2][c1-1] + prefix[r1-1][c1-1]

for x1 in range(m):
    for y1 in range(n):
        for x2 in range(x1, m):
            for y2 in range(y1, n):
                if tinh_tong(y1, x1, y2, x2) % 9 == 0:
                    count += 1
print(count)

    
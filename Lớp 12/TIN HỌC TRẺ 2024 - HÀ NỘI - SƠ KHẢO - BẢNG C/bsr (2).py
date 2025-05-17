import os, sys
input_file = os.path.join(sys.path[0], "bsr.INP")
sys.stdin = open(input_file, 'r')


m, n = map(int, input().split())
table = [list(map(int, input().split())) for _ in range(m)]
count = 0

for row1 in range(m):
    sums = [0] * n
    for row2 in range(row1, m):
        for col in range(n):
            sums[col] += table[row2][col]
        prefix = [0]
        for val in sums:
            prefix.append((prefix[-1] + val) % 9)
        freq = {}
        for p in prefix:
            freq[p] = freq.get(p, 0) + 1
        for v in freq.values():
            count += v * (v - 1) // 2

print(count)
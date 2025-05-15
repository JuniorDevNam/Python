m, n = map(int, input().split())
table = [list(map(int, input().split())) for _ in range(m)]
count = 0

for x1 in range(m):
    arr = [0] * n #tổng các phần tử từ hàng x1 đến hàng x2
    for x2 in range(x1, m):
        for col in range(n):
            arr[col] += table[x2][col]
        prefix = 0
        freq = {0: 1}
        for val in arr:
            prefix = (prefix + val) % 9
            count += freq.get(prefix, 0)
            freq[prefix] = freq.get(prefix, 0) + 1

print(count)
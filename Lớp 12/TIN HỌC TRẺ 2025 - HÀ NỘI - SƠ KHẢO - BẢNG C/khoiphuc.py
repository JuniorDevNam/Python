from itertools import product

m, n = map(int, input().split())
bang = [list(input().strip()) for _ in range(m)]

# Tìm vị trí các dấu *
sao = [(i, j) for i in range(m) for j in range(n) if bang[i][j] == '*']
k = len(sao)
min_W = 10**18

for values in product('01', repeat=k):
    # Tạo bản sao bảng
    temp = [row[:] for row in bang]
    # Điền giá trị cho các vị trí *
    for idx, (i, j) in enumerate(sao):
        temp[i][j] = values[idx]
    # Tính W
    W = 0
    for i in range(m):
        so_0 = temp[i].count('0')
        so_1 = temp[i].count('1')
        W = max(W, abs(so_0 - so_1))
    for j in range(n):
        so_0 = sum(temp[i][j] == '0' for i in range(m))
        so_1 = sum(temp[i][j] == '1' for i in range(m))
        W = max(W, abs(so_0 - so_1))
    min_W = min(min_W, W)

print(min_W)
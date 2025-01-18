import sys, os

# Đọc file input/output
def read_input_output():
    input_file = os.path.join(sys.path[0], 'khudancu.inp')
    output_file = os.path.join(sys.path[0], 'khudancu.out')
    sys.stdin = open(input_file, 'r')
    sys.stdout = open(output_file, 'w')
def dfs(grid, x, y, visited):
    if x < 0 or x >= len(grid) or y < 0 or y >= len(grid[0]) or visited[x][y]:
        return
    visited[x][y] = True
    # Duyệt các ô lân cận (trái, phải, trên, dưới)
    dfs(grid, x + 1, y, visited)
    dfs(grid, x - 1, y, visited)
    dfs(grid, x, y + 1, visited)
    dfs(grid, x, y - 1, visited)
# Hàm chính
def main():
    read_input_output()
    M, N, D, K = map(int, input().split())
    grid = [input().strip() for _ in range(M)]

    Mall = []
    P = set()

    # Duyệt toàn bộ lưới để tìm 'M' và 'P'
    for x in range(M):
        for y, char in enumerate(grid[x]):
            if char == 'M':
                Mall.append((x, y))
            elif char == 'P':
                P.add((x, y))

    # Tập hợp các tọa độ trong phạm vi Manhattan D
    All_D_poss = [
        (dx, dy)
        for dx in range(-D, D + 1)
        for dy in range(-D, D + 1)
        if abs(dx) + abs(dy) <= D
    ]

    # Đếm số lượng P bị ảnh hưởng bởi ít nhất K M
    cnt = 0
    for px, py in P:
        influence_count = 0
        for dx, dy in All_D_poss:
            mx, my = px + dx, py + dy
            if 0 <= mx < M and 0 <= my < N and grid[mx][my] == 'M':
                influence_count += 1
                if influence_count >= K:  # Không cần kiểm tra thêm
                    cnt += 1
                    break

    print(cnt)

if __name__ == "__main__":
    main()
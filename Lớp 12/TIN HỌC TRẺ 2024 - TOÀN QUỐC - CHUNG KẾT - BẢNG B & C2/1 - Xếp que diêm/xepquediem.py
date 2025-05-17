N = int(input())

que = [6, 2, 5, 5, 4, 5, 6, 4, 7, 6]
so_que = 0
for i in str(N):
    so_que += que[int(i)]

# Số bé nhất có cùng số que
found_min = False
for d1 in range(1, 10):
    for d2 in range(0, 10):
        for d3 in range(0, 10):
            if que[d1] + que[d2] + que[d3] == so_que:
                print(f"{d1}{d2}{d3}")
                found_min = True
                break
        if found_min:
            break
    if found_min:
        break

# Số lớn nhất có cùng số que
found_max = False
for d1 in range(9, 0, -1):
    for d2 in range(9, -1, -1):
        for d3 in range(9, -1, -1):
            if que[d1] + que[d2] + que[d3] == so_que:
                print(f"{d1}{d2}{d3}")
                found_max = True
                break
        if found_max:
            break
    if found_max:
        break
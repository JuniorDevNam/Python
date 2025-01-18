import sys, os
from collections import defaultdict

input_file = os.path.join(sys.path[0], 'khudancu.inp')
output_file = os.path.join(sys.path[0], 'khudancu.out')
sys.stdin = open(input_file, 'r')
sys.stdout = open(output_file, 'w')

M, N, D, K = map(int, input().split())
MN = [input().strip() for _ in range(M)]

P = set()
Mall = []
P_in_rangeD_Mall = defaultdict(int)

# Tất cả các tọa độ D tồn tại
All_D_poss = set()
for i in range(1, D + 1):
    All_D_poss.update([(i, i), (-i, i), (i, -i), (-i, -i), (i, 0), (-i, 0), (0, i), (0, -i)])

# Vị trí P và M

for x in range(M):
    string = MN[x]

    first_y_posM = string.find('M')
    end_y_posM = string.rfind('M')

    first_y_posP = string.find('P')
    end_y_posP = string.rfind('P')

    if first_y_posM == end_y_posM:
        Mall.append((x,first_y_posM))
    elif first_y_posM != end_y_posM:
        for y in range(first_y_posM, end_y_posM +1):
            if string[y] == 'M':
                Mall.append((x,y))

    if first_y_posP == end_y_posP:
        P.add((x,first_y_posP))
    elif first_y_posP != end_y_posP:
        for y in range(first_y_posP, end_y_posP+1):
            if string[y] == 'P':
                P.add((x,y))
    

# Kiểm tra những P trong phạm vi D của M
for m in Mall:
    for d in All_D_poss:
        md = (m[0] + d[0], m[1] + d[1])
        if md in P:
            P_in_rangeD_Mall[md] += 1

# Đếm
cnt = sum(1 for value in P_in_rangeD_Mall.values() if value >= K)
print(cnt)
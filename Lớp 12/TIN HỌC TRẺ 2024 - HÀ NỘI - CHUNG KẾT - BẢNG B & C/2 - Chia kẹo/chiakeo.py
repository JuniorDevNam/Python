import os, sys, bisect
input_file = os.path.join(sys.path[0], "chiakeo.inp")
output_file = os.path.join(sys.path[0], "chiakeo.out")
sys.stdin = open(input_file, "r")
sys.stdout = open(output_file, "w")

#N - số lượng học sinh
#Q - số lượt phát kẹo
N, Q = map(int, input().split())
#A - danh sách học sinh
A = list(map(int, input().split()))
#K - các cách phát kẹo
K = [list(map(int, input().split())) for _ in range(Q)]
#S - số kẹo của từng học sinh
S = [0] * N

#tiền xử lý: vị trí của các học sinh thỏa mãn điều kiện x trong các lượt phát kẹo
cac_x = set(k[2] for k in K)
x_tm = {}
for x in cac_x:
    x_tm[x] = []
    for i in range(N):
        if A[i] % x == 0:
            x_tm[x].append(i)

for l, r, x, v in K:
    dieu_kien = x_tm[x]
    #tìm đầu mút trái và đầu mút phải trong list
    trai = bisect.bisect_left(dieu_kien, l - 1)
    phai = bisect.bisect_right(dieu_kien, r - 1)
    for j in dieu_kien[trai:phai]:
        S[j] += v
print(*S)
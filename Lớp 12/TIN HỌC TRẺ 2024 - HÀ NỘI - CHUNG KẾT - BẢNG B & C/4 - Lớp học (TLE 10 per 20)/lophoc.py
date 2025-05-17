import sys, os
input_file = os.path.join(sys.path[0],"lophoc.inp")
output_file = os.path.join(sys.path[0],"lophoc.out")
sys.stdin = open(input_file, "r")
sys.stdout = open(output_file, "w")

n = int(input()) # n học sinh
doc = list(map(int, input().split())) # năng lực đọc của n học sinh
van = list(map(int, input().split())) # năng lực viết của n học sinh
toan = list(map(int, input().split())) # năng lực toán của n học sinh
MOD = 10**9 + 7
Q = 0
for i in range(n):
    for j in range(i + 1, n):
        x = toan[i] + toan[j]
        y = min(abs(doc[i] - doc[j]), abs(van[i] - van[j]))
        Q = (Q + x * y) % MOD
print(Q)
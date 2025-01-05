import sys, os
input_file = os.path.join(sys.path[0],'choigame.inp')
output_file = os.path.join(sys.path[0],'choigame.out')
sys.stdin = open(input_file, 'r')
sys.stdout = open(output_file, 'w')
N, K = map(int,input().split())
H = list(map(int,input().split()))
Hk = [1 for _ in range(N)]
for i in range(1,N):
    if abs(H[i-1] - H[i]) > K and H[i-1] < H[i]:
        Hk[i] = 0
print(" ".join(str(x) for x in Hk))
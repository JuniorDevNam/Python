import sys, os
input_file = os.path.join(sys.path[0],'MECUNG.INP')
output_file = os.path.join(sys.path[0],'MECUNG.OUT')
sys.stdin = open(input_file,'r')
sys.stdout = open(output_file, 'w')
N, M = int(input().split())
m = []
for _ in range(N):
    n = str(input())
    m.append(n)
def check_start_valid(N, M, m):
    start_dest = []
    for i in range(1,N+1):
        for j in range(1,M+1):
            if m[i][j] != "#" or m[i][j] != "e":
                start_dest.append((i,j))
def check_win(N, M, start_i, start_j, m):

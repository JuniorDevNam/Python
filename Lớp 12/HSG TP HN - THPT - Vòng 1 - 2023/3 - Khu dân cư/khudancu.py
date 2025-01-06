import sys, os
input_file = os.path.join(sys.path[0],'khudancu.inp')
output_file = os.path.join(sys.path[0],'khudancu.out')
sys.stdin = open(input_file, 'r')
sys.stdout = open(output_file, 'w')
M, N, D, K = map(int,input().split())
MN = [input() for _ in range(M)]
P = []
Mall = []
P_in_rangeD_Mall = []
All_D_poss = []
for i in range(1,D+1):
    All_D_poss.append((i,i))
    All_D_poss.append((-i,i))
    All_D_poss.append((i,-i))
    All_D_poss.append((-i,-i))
    All_D_poss.append((i,0))
    All_D_poss.append((-i,0))
    All_D_poss.append((0,i))
    All_D_poss.append((0,-i))
for x in range(M):
    for y in range(N):
        if MN[x][y] == 'P':
            P.append((x,y))
        if MN[x][y] == 'M':
            Mall.append((x,y))
for m in Mall:
    for d in All_D_poss:
        md = tuple(a + b for a, b in zip(m,d))
        if md in P:
            P_in_rangeD_Mall.append(md)
ud = set(P_in_rangeD_Mall)
cd = {item: P_in_rangeD_Mall.count(item) for item in ud}
#print(All_D_poss,'\n',P,'\n',P_in_rangeD_Mall,'\n',ud,'\n',cd)
cnt = 0
for city, value in cd.items():
    if value >= K:
        cnt += 1
print(cnt)

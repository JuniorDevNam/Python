import sys, os
input_file = os.path.join(sys.path[0],'chiahet2.inp')
output_file = os.path.join(sys.path[0],'chiahet2.out')
sys.stdin = open(input_file, 'r')
sys.stdout = open(output_file, 'w')
T = int(input())
Ti = [list(map(int,input().split())) for _ in range(T)]

for i in range(T):
    N, X = Ti[i][0], Ti[i][1]
    mu = N-1
    s = 2**X
    start = 1*10**mu
    end = 9*10**mu + int('9'*(mu))
    cnt = 0
    c = 0
    while c < end:
        if start % s == 0:
            break
        else:
            start += 2
        c += 1
    for j in range(start,end,s):
        if j%s == 0:
            cnt += 1
    print(cnt)
        

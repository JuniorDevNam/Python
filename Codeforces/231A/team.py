#Accepted

n = int(input())
A = [list(map(int,input().split())) for _ in range(n)]
cnt = 0
for s in A:
    if s.count(1) >= 2:
       cnt += 1
print(cnt) 
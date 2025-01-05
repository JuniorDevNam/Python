#Accepted

n = int(input())
A = [str(input()) for _ in range(n)]
for s in A:
    if len(s) <= 10:
        print(s)
    else:
        so = len(s) - 2
        s = s[0] + str(so) + s[-1]
        print(s)
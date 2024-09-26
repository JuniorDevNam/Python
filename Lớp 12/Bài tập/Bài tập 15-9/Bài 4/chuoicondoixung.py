n = int(input('n: '))
S = str(input('S: '))
half = n // 2
kq = []
if S == S[::-1]:
    print(n)
else:
    for x in range(n):
        for i in range(n, x, -1):
            if S[x:i] == S[x:i][::-1]:
                kq.append(len(S[x:i]))
    print(max(kq))
L, R = map(int, input().split())
cnt = 0
while L <= R:
    uoc = [1]
    for x in range(2,L):
        if L % x == 0 and (x not in uoc):
            uoc.append(x)
            if int(L / x) not in uoc and int(L / x) != L:
                uoc.append(int(L/x))
    print(L,uoc)
    if sum(uoc) > L:
        cnt += 1
    L += 1
print(cnt)
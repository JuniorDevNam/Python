N = int(input('N: '))
t = 2
c = [(t*(N-3)+t)]
def tho(s,t):
    r = t * (N-s) + t
    return r
for i in range(3,N):
    s = i+4
    print(i,s)
    if s <= N:
        c.append(tho(s,t))
    else:
        break
print(c,sum(c))
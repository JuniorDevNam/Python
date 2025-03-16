A = int(input())
N = int(input())
K = A//2
lim = 0
count = 1
ds = []
while lim < N:
    c1 = A*count
    c2 = c1 - K
    c3 = c2 + A
    c4 = c3 - K
    ds.append(int(str(c1)[-1]))
    ds.append(int(str(c2)[-1]))
    ds.append(int(str(c3)[-1]))
    ds.append(int(str(c4)[-1]))
    lim += 4
    count += 1
kq = sum(ds[:N])
print(kq)
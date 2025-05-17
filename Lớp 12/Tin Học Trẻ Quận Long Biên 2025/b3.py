n = list(map(int,input().split()))
cp = []
for i in range(len(n)+1):
   cp.append(i*i)
for j in cp:
    if j not in n:
        print(j)
        break
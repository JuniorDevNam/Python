X = str(input('X: '))
Y = str(input('Y: '))

#cách 1
vi_tri, gioi_han = [[],[]], len(X) - len(Y)
for i in range(len(X)):
    if X[i] == Y[0] and i <= gioi_han:
        vi_tri[0].append(i)
for x in vi_tri[0]:
    for y in range(len(Y)):
        if X[x+y] == Y[y]:
            vi_tri[1].append(x+y)
    if len(vi_tri[1]) != len(Y):
        vi_tri[1].clear()
print(' '.join(str(x) for x in vi_tri[1]))

#cách 2
lx=len(X) 
ly=len(Y) 
for i in range(lx):
    s=X[i:i+ly]
    if(s==Y):
        print(i+1,end=' ')
print(' ')
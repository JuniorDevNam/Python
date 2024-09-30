n,v = int(input('n: ')), int(input('v: '))
t, x = v, v
if v >= (n-1):
    print(n-1)
else:
    for i in range(2,n):
        if v >= n-i:
            print(t+i)
            break
        else:
            t += i
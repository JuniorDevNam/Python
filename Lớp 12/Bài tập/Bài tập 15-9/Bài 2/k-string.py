k = int(input("k:"))
s = str(input('s:'))
count, n, t = {}, len(s), ''
if n%k != 0:
    print('-1')
else:
    for i in s:
        if i in count:
            count[i] += 1
        else:
            count[i] = 1
    for key, value in count.items():
        if value % k != 0:
            print('-1')
        else:
            t += (key*int(value // k))
    print(t)
                
                
            
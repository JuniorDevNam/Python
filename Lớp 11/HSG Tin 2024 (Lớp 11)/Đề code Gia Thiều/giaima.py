N = int(input("n: "))
n = list(str(N))
n.sort(reverse=True)
s = 0
if n[-1] == "0":
    for x in n:
        s = s + int(x)
    if s%3 == 0:
        r = int(''.join(n))
        print(r)
    else:
        print('-1')
else:
    print('-1')
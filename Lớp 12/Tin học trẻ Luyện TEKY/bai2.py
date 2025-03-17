a = int(input())
b = int(input())
c = int(input())
phut = 0
c1 = a + b > c
c2 = a + c > b
c3 = b + c > a
if c1 and c2 and c3:
    print(phut)
else:
    if c1 == False:
        r = c - (a+b) + 1
        phut += r
    if c2 == False:
        r = b - (a+c) + 1
        phut += r
    if c3 == False:
        r = a - (b+c) + 1
        phut += r
    print(phut)
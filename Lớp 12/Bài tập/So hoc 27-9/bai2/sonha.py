n = int(input('n: '))
y = 1
s = 0
while y <= n:
    if y % 2 != 0:
        s += y
    y += 2
print(s) 
n = 1
count = 0
while n <= 100:
    count = count + 1
    if count%10 == 0:
        print(n)
    else:
        print(n, end = " ")
    n = n + 1
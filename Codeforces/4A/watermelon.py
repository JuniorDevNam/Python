#Get WA at Test 5

w = int(input())
half = w/2
if half == int(half):
    for i in range(0,int(half)+1):
        if int(half-i) % 2 == 0 and int(half+i) % 2 == 0:
            print('YES')
            break
    else:
        print('NO')
else:
    print('NO')

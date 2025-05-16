import os, sys
input_file = os.path.join(sys.path[0],"khoaso.INP")
sys.stdin = open(input_file, 'r')

khoaso = list(map(int, input().split()))
password = (2,0,2,5)
count = 0
for i in range(len(khoaso)):
    if khoaso[i] == password[0]:
        count += 0
    else:
        if khoaso[i] <= 5:
            count += abs(khoaso[i] - password[i])
        else:
            count += (10 - abs(khoaso[i] - password[i]))
print(count)

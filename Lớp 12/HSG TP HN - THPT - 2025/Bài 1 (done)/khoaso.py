import os, sys
input_file = os.path.join(sys.path[0],"khoaso.INP")
output_file = os.path.join(sys.path[0], "khoaso.OUT")
sys.stdin = open(input_file, 'r')
sys.stdout = open(output_file, 'w')
khoaso = list(map(int, input().split()))
password = (2,0,2,5)
count = 0
for i in range(len(khoaso)):
    count += min(abs(khoaso[i] - password[i]), 10 - abs(khoaso[i] - password[i]))
print(count)
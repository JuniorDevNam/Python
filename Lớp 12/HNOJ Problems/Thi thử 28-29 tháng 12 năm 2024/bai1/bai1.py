import sys, os
input_file =os.path.join(sys.path[0],'TICHLIENTIEP.INP')
output_file =os.path.join(sys.path[0],'TICHLIENTIEP.OUT')
sys.stdin = open(input_file,'r')
sys.stdout = open(output_file,'w')
n = int(input())
delta = 1 - 4*(n)
x1 = (-1 - (delta**0.5))/2
x2 = (-1 + (delta**0.5))/2
print(x1,x2)
if delta >= 0:
    if x1 == x2:
        print(x1)
    elif x1 >= 0:
        print(x1)
    else:
        print(x2)
else:
    print(-1)
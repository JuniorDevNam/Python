import sys, os
input_file = os.path.join(sys.path[0],"timboso.inp")
output_file = os.path.join(sys.path[0],"timboso.out")
sys.stdin = open(input_file, "r")
sys.stdout = open(output_file, "w")

N = int(input())
if N == 1:
    print(0)
    exit()
for a in range(int(N**0.5), 0, -1):
    if N % a == 0:
        b = N // a
        c = abs(a - b)
        print(c)
        break
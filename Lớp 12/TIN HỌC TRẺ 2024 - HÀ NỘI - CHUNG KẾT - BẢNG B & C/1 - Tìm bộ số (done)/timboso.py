import sys, os
input_file = os.path.join(sys.path[0],"timboso.inp")
output_file = os.path.join(sys.path[0],"timboso.out")
sys.stdin = open(input_file, "r")
sys.stdout = open(output_file, "w")

N = int(input())

a = int(N**0.5)
b = N // a
c = abs(a - b)
print(c)
import sys, os
input_file = os.path.join(sys.path[0],'mahoaxau.inp')
output_file = os.path.join(sys.path[0],'mahoaxau.out')
sys.stdin = open(input_file, 'r')
sys.stdout = open(output_file, 'w')

S = str(input())
K = int(input())
A = str(input())
B = str(input())

mp = {A[x]: B[x] for x in range(26)}
c = [[] for _ in range(26)]

for i in range(26):
    c[i].append(i)
    chu = mp[chr(ord('a')+i)]
    while ord(chu) - ord('a') != i:
        c[i].append(ord(chu) - ord('a'))
        chu = mp[chu]
f = {}
for j in range(26):
    pos = K % len(c[j])
    f[chr(ord('a') + j)] = chr(c[j][pos] + ord('a'))
result = ''.join(f[char] for char in S)
print(result)


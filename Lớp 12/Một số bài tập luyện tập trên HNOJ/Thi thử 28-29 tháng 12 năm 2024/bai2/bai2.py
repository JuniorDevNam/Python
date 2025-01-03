import sys,os
input_file = os.path.join(sys.path[0],'MAHOAXAU.INP')
output_file = os.path.join(sys.path[0],'MAHOAXAU.OUT')

sys.stdin = open(input_file, 'r')
sys.stdout = open(output_file, 'w')
S = str(input())
K = int(input())
A = str(input())
B = str(input())
c = [[] for _ in range(26)]
mp = {A[i]: B[i] for i in range(26)}
f = {}

#Dựng vectơ c[i]
for i in range(26):
    c[i].append(i)
    chu = mp[chr(ord('a') + i)] #Duyệt chữ trong map
    #ord từ a đến z là 97 đến 122
    while ord(chu) - ord('a') != i: 
        c[i].append(ord(chu) - ord('a'))
        chu = mp[chu]

# Calculate new positions after k transformations
for i in range(26):
        pos = K % len(c[i])
        f[chr(ord('a') + i)] = chr(c[i][pos] + ord('a'))

    # Output the transformed string
result = ''.join(f[char] for char in S)
print(result)


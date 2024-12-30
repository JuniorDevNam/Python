import sys,os
input_file = os.path.join(sys.path[0],'MAHOAXAU.INP')
output_file = os.path.join(sys.path[0],'MAHOAXAU.OUT')

sys.stdin = open(input_file, 'r')
sys.stdout = open(output_file, 'w')
S = str(input())
K = int(input())
A = str(input())
B = str(input())
def encoding(string):
    kq = string[:]
    for char in string:
        vt = A.find(char)
        kq
    return kq
for _ in range(K):
    S = encoding(S)
print(S.strip().replace('\n', ''))

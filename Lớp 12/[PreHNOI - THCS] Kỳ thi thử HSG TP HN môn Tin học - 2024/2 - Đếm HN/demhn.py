import sys, os
input_file = os.path.join(sys.path[0],'demhn.inp')
output_file = os.path.join(sys.path[0],'demhn.out')
sys.stdin = open(input_file, 'r')
sys.stdout = open(output_file, 'w')
X = str(input())
K = int(input())
x = X*K
cnt = 0
i = 0
while i < len(x):
    if x[i] == 'H':
        j=i+1
        while j < len(x):
            if x[j] == 'N':
                cnt += 1
            j += 1
    i += 1
    
print(cnt)
#subtask 1,2 - 70%
        
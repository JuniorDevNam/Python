import sys, os
input_file = os.path.join(sys.path[0],'TRUNGBINHCONG.INP')
output_file = os.path.join(sys.path[0],'TRUNGBINHCONG.OUT')
sys.stdin = open(input_file, 'r')
sys.stdout = open(output_file, 'w')
n = int(input())
a = list(map(int,input().split()))
b = list(map(int,input().split()))
count = 0
if sum(a)/len(a) <= sum(b)/len(b):
    count += 1
for k in range(1,n):
    subarray1 = a[:k]
    subarray1_2 = a[k:]
    #print(subarray1,subarray1_2)
    for i in range(1,k+1):
        subarray2 = b[:i]
        subarray2_2 = b[i:]
        #print(subarray2,subarray2_2)
        if sum(subarray1)/len(subarray1) <= sum(subarray2)/len(subarray2) and sum(subarray1_2)/len(subarray1_2) <= sum(subarray2_2)/len(subarray2_2):
            count += 1
print(count)
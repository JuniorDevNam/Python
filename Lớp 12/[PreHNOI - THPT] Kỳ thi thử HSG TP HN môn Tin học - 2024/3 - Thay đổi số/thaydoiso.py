import sys, os
input_file = os.path.join(sys.path[0],'thaydoiso.inp')
output_file = os.path.join(sys.path[0],'thaydoiso.out')
sys.stdin = open(input_file, 'r')
sys.stdout = open(output_file, 'w')

n = int(input())
a = list(map(int,input().split()))
a.sort()

from math import gcd
def gcd_array(arr):
    result = arr[0]
    for num in arr[1:]:
        result = gcd(result, num)
        if result == 1:
            break
    return result
#subtask 1:
if n == 3:
    print(max(a))
#subtask 2
elif 3 < n <= 1000:
    a[0] = a[1] = gcd(a[2],a[3])
    uoc = {}
    print(a)
    for i in range(n):
        for j in range(i+1,n-1):
            u = gcd(a[i], a[j])
            if u in uoc:
                uoc[u] += 1
            else:
                uoc[u] = 1
    result = 0
    for key, value in uoc.items():
        if value >= n:
            if int(key) > result:
                result = int(key)
    print(result)
else:
    
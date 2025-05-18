import sys,os
from math import gcd
from functools import reduce
input_file = os.path.join(sys.path[0],'THAYDOISO.INP')
output_file = os.path.join(sys.path[0],'THAYDOISO.OUT')

sys.stdin = open(input_file, 'r')
sys.stdout = open(output_file, 'w')

n = int(input())
arr = list(map(int, input().strip().split()))
arr.sort()
uoc = []
if n == 3: #subtask 1
    print(gcd(arr[2],arr[2]))
elif 3 < n <= 1000: #subtask 2
    for i in range(2,n):
        for j in range(i+1,n-1):
            uoc.append(gcd(arr[j], arr[i]))
    print(uoc[0])
elif n > 1000: #subtask 3-4
    steps = n // 1000
    arr2 = [arr[2::steps]]
    print(reduce(gcd, arr2))
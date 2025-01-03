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
def gcd_of_array(arr):
    return reduce(gcd, arr)
if n == 3:  
    print(arr[2])
else: 
    arr2=arr[2::]
    print(gcd_of_array(arr2))
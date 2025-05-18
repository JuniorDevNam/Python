'''
https://hnoj.edu.vn/problem/pa059
'''
from math import gcd as ucln
from functools import reduce
n = int(input())
n2 = list(map(int,input().split()))
def find_gcd_of_list(numbers):
    return reduce(ucln, numbers)
print(find_gcd_of_list(n2))

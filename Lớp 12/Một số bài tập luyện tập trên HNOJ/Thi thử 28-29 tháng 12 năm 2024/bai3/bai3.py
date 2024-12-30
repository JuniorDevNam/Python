import sys,os
input_file = os.path.join(sys.path[0],'THAYDOISO.INP')
output_file = os.path.join(sys.path[0],'THAYDOISO.OUT')

sys.stdin = open(input_file, 'r')
sys.stdout = open(output_file, 'w')

def gcd(a, b):
    while b:
        a, b = b, a % b
    return a
n = int(input())
arr = list(map(int, input().strip().split()))
def find_max_gcd(arr):
    n = len(arr)
    if n == 1:
        return arr[0]
    
    prefix_gcd = [0] * n
    suffix_gcd = [0] * n
    
    prefix_gcd[0] = arr[0]
    for i in range(1, n):
        prefix_gcd[i] = gcd(prefix_gcd[i-1], arr[i])
    
    suffix_gcd[n-1] = arr[n-1]
    for i in range(n-2, -1, -1):
        suffix_gcd[i] = gcd(suffix_gcd[i+1], arr[i])
    
    max_gcd = max(suffix_gcd[1], prefix_gcd[n-2])
    
    for i in range(1, n-1):
        max_gcd = max(max_gcd, gcd(prefix_gcd[i-1], suffix_gcd[i+1]))
    
    return max_gcd
print(find_max_gcd(arr))
import os,sys
input_file = os.path.join(sys.path[0],"denlong.INP")
sys.stdin = open(input_file, 'r')

n, k, x = map(int, input().split())
a = list(map(int, input().split()))
freq = {}
left = -1
x1, k1 = 0, 0
for right in range(n):
    if a[right] not in freq:
        freq[a[right]] = 0
    freq[a[right]] += 1
    if len(freq) > k:
        left += 1
        freq[a[left]] -= 1
        if freq[a[left]] == 0:
            del freq[a[left]]
        

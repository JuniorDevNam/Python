import sys, os
input_file = os.path.join(sys.path[0],'domi.inp')
output_file = os.path.join(sys.path[0],'domi.out')
sys.stdin = open(input_file, 'r')
sys.stdout = open(output_file, 'w')
n = int(input())
a = list(map(int,input().split()))
def count_domi(n, arr):
    count = 0

    for i in range(n):
        freq = {}
        max_freq = 0
        for j in range(i, n):
            if arr[j] in freq:
                freq[arr[j]] += 1
            else:
                freq[arr[j]] = 1
            
            max_freq = max(max_freq, freq[arr[j]])
            
            # Kiểm tra điều kiện không dominative
            if max_freq <= (j - i + 1) // 2:
                count += 1
            else:
                break

    return count
print(count_domi(n, a))
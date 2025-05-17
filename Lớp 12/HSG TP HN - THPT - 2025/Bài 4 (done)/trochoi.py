import os, sys
input_file = os.path.join(sys.path[0], "trochoi.INP")
sys.stdin = open(input_file, 'r')
n, q = map(int, input().split())
a = list(map(int, input().split()))
k = list(map(int, input().split()))
bestchooses = []
current = 0

for i in range(n):
    if a[i] < 0:
        bestchooses.append(current)
        current = 0
    else:
        current += a[i]
bestchooses.append(current)  # Thêm đoạn cuối nếu không kết thúc bằng số âm
bestchooses.sort(reverse=True)
prefix_sum = [0]
for i in bestchooses:
    prefix_sum.append(prefix_sum[-1] + i)
for j in range(q):
    if k[j] > len(bestchooses):
        print(prefix_sum[-1])
    else:
        print(prefix_sum[k[j]])
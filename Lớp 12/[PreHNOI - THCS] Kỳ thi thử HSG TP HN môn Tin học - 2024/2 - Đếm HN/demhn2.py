import sys, os
input_file = os.path.join(sys.path[0],'demhn.inp')
output_file = os.path.join(sys.path[0],'demhn.out')
sys.stdin = open(input_file, 'r')
sys.stdout = open(output_file, 'w')
X = input().strip()
K = int(input().strip())

# Đếm số lần xuất hiện của 'H' và 'N' trong chuỗi X
count_H = 0
count_pairs = 0

# Duyệt qua từng ký tự trong chuỗi X
for char in X:
    if char == 'H':
        count_H += 1
    elif char == 'N':
        count_pairs += count_H

# Tổng số cặp 'H' và 'N' trong chuỗi X*K
total_pairs = count_pairs * K + count_H * (count_pairs * (K - 1) * K // 2)

print(total_pairs)
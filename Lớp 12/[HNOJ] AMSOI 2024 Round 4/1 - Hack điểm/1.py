N = int(input())
A = list(map(int, input().split()))
A.sort()

# Tính tổng ban đầu
total = sum(A)
target = 4.5 * N  # Tổng cần đạt

# Đếm số phần tử cần thay đổi
i = 0
while total < target:
    total += 5 - A[i]
    i += 1

print(i)

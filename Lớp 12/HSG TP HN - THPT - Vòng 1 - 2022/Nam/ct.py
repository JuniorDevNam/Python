import sys, os
input_file = os.path.join(sys.path[0],'cp.inp')
output_file = os.path.join(sys.path[0],'cp.out')
sys.stdin = open(input_file, 'r')
sys.stdout = open(output_file, 'w')

# Đọc dữ liệu từ tệp
n = int(input())
values = list(map(int, input().split()))

# Tính tổng giá trị của tất cả các tờ tiền
total_sum = sum(values)

# Tìm tổng giá trị lớn nhất không vượt quá một nửa tổng giá trị
half_sum = total_sum // 2
max_value = total_sum / 2
if half_sum == max_value:
    print(half_sum)
else:
    # Khởi tạo mảng dp
    dp = [0] * (half_sum + 1)

    # Cập nhật mảng dp
    for value in values:
        for j in range(half_sum, value - 1, -1):
            dp[j] = max(dp[j], dp[j - value] + value)

    # Giá trị lớn nhất mà mỗi người có thể nhận được
    max_value = dp[half_sum]

    # Ghi kết quả ra tệp
    print(max_value)
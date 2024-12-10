import time

# Phương pháp 1: Sử dụng slicing
n1 = "1234567890" * 1000000  # Chuỗi dài để kiểm tra hiệu suất
start_time = time.time()
n2 = n1[::-1]
end_time = time.time()
print(f"Phương pháp slicing: {end_time - start_time} giây")

# Phương pháp 2: Sử dụng vòng lặp for
start_time = time.time()
n2 = ""
for x in range(1, len(n1) + 1):
    n2 += n1[-x]
end_time = time.time()
print(f"Phương pháp vòng lặp for: {end_time - start_time} giây")
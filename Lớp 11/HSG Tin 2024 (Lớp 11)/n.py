import sys
n = int(input("N (2 <= N <= 20): "))
if n < 2 or n > 20:
    print("N không đúng yêu cầu")
    sys.exit(0)
a = str(input("Nhập dãy số bất kỳ được ngăn cách bởi khoảng trắng, với điều kiện các số các số không vượt quá N: "))
A = a.split()
A = list(map(float, A))
A = list(map(lambda x: round(x, 2), A)) #hàm ẩn danh với 1 biểu thức, làm tròn float đến hàng thập phân thứ 2
# Sắp xếp danh sách theo thứ tự tăng dần
A.sort()
# Tính tích lớn nhất và nhỏ nhất
tich_max = max([A[0] * A[1], A[-1] * A[-2]])
if tich_max == A[0] * A[1]:
    tmax = f"{A[0]} {A[1]}"
else:
    tmax = f"{A[-1]} {A[-2]}"

tich_min = min([A[0] * A[1], A[-1] * A[-2], A[0] * A[-1]])
if tich_min == A[0] * A[1]:
    tmin = f"{A[0]} {A[1]}"
elif tich_min == A[-1] * A[-2]:
    tmin = f"{A[-1]} {A[-2]}"
else:
    tmin = f"{A[0]} {A[-1]}"

print("N = ",n)
print(a)
print(tmax)
print(tmin)




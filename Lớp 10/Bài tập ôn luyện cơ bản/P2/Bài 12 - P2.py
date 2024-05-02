'''xuất các số hoàn hảo từ n đến m'''
# Hàm kiểm tra số hoàn hảo
def so_hoan_hao(x):
    # Nếu x nhỏ hơn 1 thì không phải là số hoàn hảo
    if x < 1:
        return False
    # Tính tổng các ước số nhỏ hơn x
    tong_uoc_so = 0
    for i in range(1, x):
        if x % i == 0:
            tong_uoc_so += i
    # Nếu tổng bằng x thì là số hoàn hảo
    if tong_uoc_so == x:
        return True
    # Ngược lại không phải là số hoàn hảo
    else:
        return False
# Nhập n và m
n = int(input("Nhập n: "))
m = int(input("Nhập m: "))
while m < n:
    print("m bé hơn n, không thỏa mãn đề bài")
    n = int(input("nhập số n:"))
    m = int(input("nhập số m:"))
perfect_num = []
# Xuất các số hoàn hảo từ n đến m
for i in range(n, m + 1):
    if so_hoan_hao(i):
        perfect_num.append(i)
print("Các số hoàn hảo từ", n, "đến", m, "là:",perfect_num)
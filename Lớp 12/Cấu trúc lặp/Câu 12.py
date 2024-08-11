# Bài 12: VCT xuất các số hoàn hảo từ n đến m.

def so_hoan_hao(x):
    tong = 0
    for _ in range(1,x):
        if x % _ == 0:
            tong += _
    if tong == x:
        return True
    else:
        return False
    
n = int(input("Nhập số n: "))
m = int(input("Nhập số m: "))
so = [i for i in range(n,m+1) if so_hoan_hao(i)]
print(so)

# Nhập số nguyên dương n, tính n!, biết n! = 1.2.3.4.5......n
n = int(input("Nhập số nguyên dương n: "))
gt = 1
for i in range(1,n+1):
    gt *= i
print(gt)

#đệ quy
def giai_thua(n):
    if n == 0:
        return 1
    else:
        return n*giai_thua(n-1)
print(giai_thua(n))
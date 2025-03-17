n = int(input())
k = int(input())
ngay = 1
if k > n:
    print(ngay)
else:
    while k < n:
        ngay += 1
        k = k + k*2
    print(ngay)
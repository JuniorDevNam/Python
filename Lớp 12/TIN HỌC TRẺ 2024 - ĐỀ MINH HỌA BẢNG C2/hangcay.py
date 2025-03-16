n, q = map(int,input().split())
cay = list(map(int,input().split()))
p = [input() for _ in range(q)]

for x in p:
    l, r = int(x[0]), int(x[-1])
    tong_hieu = 0
    #lọc cây thỏa mãn khoảng [l, r]
    cay1 = []
    for i in cay:
        if l <= i <= r:
            cay1.append(i)
    #duyệt hàng cây mới
    for j in range(1,len(cay1)):
        tong_hieu += abs(cay1[j]-cay1[j-1])
    print(tong_hieu)
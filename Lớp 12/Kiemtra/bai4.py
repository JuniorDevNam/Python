N = int(input("N: "))
A = list(map(int,input("Nhập dãy số gồm N phần tử cách nhau bởi khoảng trắng: ").split()))
kq = {}
for x in A.sort():
    if x in kq:
        kq[x] += 1
    else:
        kq[x] = 1
for keys, values in kq.items():
    print(str(keys)+":",values)

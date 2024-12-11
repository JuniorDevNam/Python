S = input("Nhập chuỗi S: ")
kq = {}

for x in S:
    if x in kq:
        kq[x] += 1
    else:
        kq[x] = 1
for key, value in kq.items():
    print(str(key)+":",value)
n = int(input("Nhập số n: "))
A = []
for x in range(n+1):
    if x%2 == 0:
        A.append(x)
print(A)
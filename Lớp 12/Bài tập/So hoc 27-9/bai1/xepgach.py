N, A, B = int(input("N: ")), int(input("A: ")), int(input("B: "))
t = A
s = A
for i in range(N-1):
    t = t+B
    s += t
print(s)
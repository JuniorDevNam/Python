a = str(input("a: "))
A = []
A = a.split()
A = list(map(int, A))
tbc = sum(A)/len(A)
print(tbc)
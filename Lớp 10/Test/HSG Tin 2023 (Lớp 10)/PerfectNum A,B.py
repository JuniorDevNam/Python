A = int(input("A: "))
B = int(input("B: "))
tongso = 0
sum = 0
for x in range(A,B):
    for i in range(1,x/2):
        if x%i == 0:
            sum = sum + i
    if sum == x:
        tongso = tongso + 1
print(tongso)
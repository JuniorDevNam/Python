n = int(input("n: "))
F = [1, 1]
for i in range(2,n+1):
    # Sai: F[i] = F[i-1] + F[i-2]
    #Đúng:
    F.append(F[i-1] + F[i-2])
if F[n]%100 != 0:
    print((F[n]%100)*100)
else:
    print("F[n] =",F[n],"chia hết cho 100")
# Nhập vào 1 số nguyên N
# In ra tất cả các ước của số nguyên N đó

#Nhập N:
N = int(input("Nhập số nguyên N: "))

#List ước của N:
uocN = []

for n in range(1,N+1):
    if N%n == 0:
        uocN += (n,) #Tương đương uocN.append

print("Các ước của số nguyên N là:",uocN)
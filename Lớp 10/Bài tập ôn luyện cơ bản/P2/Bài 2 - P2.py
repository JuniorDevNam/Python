'''Viết chương trình nhập vào số n, 
xuất ra dãy số chẵn trong khoảng 1 đến n.'''

n = int(input("Nhập số tự nhiên n: "))
S = []
for k in range (1,n+1):
    if k%2==0:
        S.append(k)
print(S)
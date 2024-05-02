'''Nhập vào số nguyên dương n, 
tính và xuất ra tổng S = 2 + 4 + ...+ (n-k) với k=1 hay 0. 
Tức là tổng dãy số chẵn trong khoảng 1 đến n.'''

n = int(input("Nhập số nguyên dương n: "))
while n < 0:
    print("Xin hãy nhập số nguyên dương.")
    n = int(input("Nhập số nguyên dương n: "))
S = 0
for x in range(1,n+1):
    if x%2==0:
        S = S+x
print("Tổng là:",S)
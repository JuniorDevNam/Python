# Bài 6: Nhập vào số nguyên dương n,
# tính và xuất ra tổng S = 2 + 4 + ...+ (n-k) với k=1 hay 0. 
# Tức là tổng dãy số chẵn trong khoảng 1 đến n.
n = int(input("Nhập số n: "))
S = 0
for i in range(2,(n if n%2 == 0 else n - (n%2))+1,2):
    S += i
print(S)
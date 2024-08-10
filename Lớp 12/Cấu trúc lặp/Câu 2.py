# Bài 2: Viết chương trình nhập vào số n, xuất ra dãy số chẵn trong khoảng 1 đến n.
n = int(input("Nhập số n: "))
start = n if n%2 == 0 else n - n%2
for i in range(2,start+1,2): print(i, end = " ")
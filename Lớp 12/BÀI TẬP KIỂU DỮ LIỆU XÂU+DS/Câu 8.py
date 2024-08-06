# Viết chương trình nhập vào mảng gồm n số nguyên dương, 
# hãy xuất ra màn hình tổng của các số lẻ trong mảng đó, với n>2

#test: 1, 4, 2, 6, 3, 5, 7, 13, 23, 55, 73, 9, 21 (số lượng n: 13)
#ket qua: 210 (1+3+5+7+13+23+55+73+9+21)

n = int(input("Nhập n số nguyên dương: "))
ds = [int(input(f"Nhập số nguyên dương thứ {x+1}: ")) for x in range(n)]
so_le = [x for x in ds if x%2 != 0]
print(sum(so_le))
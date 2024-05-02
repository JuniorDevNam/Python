n = int(input("Nhập năm: "))

if n%400 == 0 or (n%4 == 0 and n%100 != 0):
    print(n,"là năm nhuận")
else:
    print(n,"không phải năm nhuận")
#Bài 3: Viết chương trình nhập vào x, tính y = x-1 nếu x>=1, ngược lại y = 1-x
x = float(input("Nhập số x: "))
if x >= 1: y = x-1 
elif x < 1: y = 1-x
print(y)
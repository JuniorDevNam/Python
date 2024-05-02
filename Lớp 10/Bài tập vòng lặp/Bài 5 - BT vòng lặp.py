# Nhập 2 số nguyên dương a, b
# Viết chương trình tìm ước chung lớn nhất và bội chung nhỏ nhất của a và b

#Nhập a, b nguyên dương
a = int(input("Nhập số nguyên dương a: "))
while a<1:
    a = int(input("Cần 1 số nguyên dương, xin hãy nhập lại a: "))
b = int(input("Nhập số nguyên dương b: "))
while b<1:
    b = int(input("Cần 1 số nguyên dương, xin hãy nhập lại b: "))

#Tìm ước chung lớn nhất:
ucln = 1
for i in range(min(a,b),0,-1):
    if a%i == 0 and b%i == 0:
        ucln = i
        break
print("Ước số chung lớn nhất của",a,"và",b,"là:",ucln)

#Tìm bội chung nhỏ nhất:
#Bội chung nhỏ nhất có thể được xác định là tích của 2 số chia cho ước số chung lớn nhất
#Vì vậy ta có công thức:
bcnn = a*b/ucln

print("Bội số chung nhỏ nhất của",a,"và",b,"là:",bcnn)


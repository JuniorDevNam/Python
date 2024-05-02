'''Nhập vào số a và số nguyên dương n, tính a mũ n. '''

a = float(input("Nhập số a: "))
n = int(input("Nhập số nguyên dương n: "))
while n < 0:
    print("Xin hãy nhập số nguyên dương.")
    n = int(input("Nhập số nguyên dương n: "))
a_mu_n = a**n
print("a =",a)
print("n =",n)
print("a^n =",a_mu_n)
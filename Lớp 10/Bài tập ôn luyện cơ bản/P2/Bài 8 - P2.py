'''Nhập số nguyên dương n, tính n!, biết n! = 1.2.3.4.5......n'''
#mẹ cái đề bài n! thì phạm vào tính toán của python r

n = int(input("Nhập số nguyên dương n: "))
while n < 0:
    print("Xin hãy nhập số nguyên dương.")
    n = int(input("Nhập số nguyên dương n: "))
n_dau_cham_than = 1
for x in range(1,n+1):
    n_dau_cham_than = n_dau_cham_than * x
print("n =",n)
print("n! =",n_dau_cham_than)
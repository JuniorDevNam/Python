'''Nhập số nguyên dương n, 
kiểm tra xem n có phải số nguyên tố trong tập số nguyên dương hay không'''

n = int(input("Nhập số nguyên dương n: "))
while n < 0:
    print("Xin hãy nhập số nguyên dương.")
    n = int(input("Nhập số nguyên dương n: "))
for x in range(2,n):
    if n%x==0:
        print("Không phải số nguyên tố")
        break
else:
    print("Là số nguyên tố")
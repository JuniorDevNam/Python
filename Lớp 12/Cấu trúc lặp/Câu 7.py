# Bài 7: Nhập số nguyên dương n, 
# kiểm tra xem n có phải số nguyên tố trong tập số nguyên dương hay không
n = int(input("Nhập số nguyên dương n: "))
if n < 1:
    print("NO")
d = 0
for x in range(2,n):
    if n%x == 0:
        d += 1
    if d >= 1:
        print("NO")
        break
else:
    print("YES")
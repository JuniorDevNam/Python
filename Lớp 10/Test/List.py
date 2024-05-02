# Nhập N nguyên dương
N = int(input("Nhập N nguyên dương: "))
while N<1:
    N = int(input("Xin hãy nhập N nguyên dương: "))

# List rỗng chứa số lẻ
soLe = []

# Thuật toán:
for i in range(1, N+1):
    if i%2 == 1:
        soLe += (i,) # Lần lượt gán biến vào list

print("Các số lẻ từ 1 đến N đã nhập (",N,") là:",soLe)
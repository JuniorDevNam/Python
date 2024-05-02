# Viết chương trình tổng các số chẵn từ 1 đến N
# Với N là số tự nhiên được nhập từ bàn phím

#Nhập N:
N = int(input("Nhập số N: "))
while N<1:
    N = int(input("Cần nhập số tự nhiên N (N>0): "))

#Biến số & Biến tổng
so = 1
tong = 0
#Vòng lặp
while so < N + 1:
    so = so + 1
    if so%2 == 0:
        tong = tong + so
    
print("Tổng các số chẵn từ 1 đến N đã nhập là:",tong)
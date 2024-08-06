# Viết chương trình nhập vào bàn phím số nguyên dương n, xuất ra màn hình dãy số Fibonaxi. 
# Biết rằng dãy Fibonaxi có dạng như sau: F0 = 1, F1 = 1, Fn = Fn-1 + Fn-2 với n>1

n = int(input("Nhập số nguyên dương n: "))
fibon = [1,1]
for i in range(2,n+1):
    fn = fibon[i-1] + fibon[i-2]
    fibon.append(fn)
print(fibon)

#test: n = 10
#ket qua: [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
def min_leftover_bricks(n):
    primes = [] #Tạo 1 danh sách các số nguyên tố từ 2 đến n
    isprime = False
    for x in range(2, n+1):
        for i in range(2, x):
            if x%i == 0:
                isprime = False
                break
            else:
                isprime = True
                break
        if isprime == True:
            primes.append(x)
    min_leftover = n #Số gạch tối thiểu
    for i in range(len(primes) - 1): #Với i trong khoảng số thứ tự phần tử list primes - 1 (bỏ n)
        p = primes[i]
        q = primes[i + 1]
        if p * q <= n:
            side = str(p)+" x "+str(q)
            leftover = n - p * q
            if leftover < min_leftover:
                min_leftover = leftover
    result = min_leftover            
    return "ta xếp hình chữ nhật với 2 cạnh là "+side+" và dư "+str(result)+" viên gạch."

#Nhập số nguyên dương t truy vấn
t = int(input("Nhập số lần truy vấn t: "))
for x in range(t):
    n = int(input("Nhập số viên gạch lần truy vấn thứ "+str(x+1)+": "))
    print("Với",n,"viên gạch,",min_leftover_bricks(n))





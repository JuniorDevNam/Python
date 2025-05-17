#Tiền sơn
son = 1200000
n = int(input())
tien = 0
while n > 0:
    if n % 10 == 0 and len(str(n-1)) < len(str(n)):
        tien += (len(str(n))*son)
        n -= 1
    else:
        tien += (len(str(n))*son)*int(str(n)[0])
        n -= int(str(n)[0]+"0"*(len(str(n))-1))
print(tien)
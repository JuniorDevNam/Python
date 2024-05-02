#Ước chung lớn nhất của hai số nguyên a và b là số nguyên dương lớn nhất mà a và b chia hết. 
#Bội số chung nhỏ nhất của hai số nguyên a và b là số nguyên dương nhỏ nhất chia hết cho cả a và b.

a = int(input("A: "))
b = int(input("B: "))
def ucln(a, b):
    #nếu a hoặc b bằng 0 trả về số còn lại
    if a == 0:
        return b
    if b == 0:
        return a
    #chạy vòng lặp các số từ 0 đến số lớn nhất xem liệu số đó cả a và b có chia hết
    if a > b:
        r = a
    elif b > a:
        r = b
    else:
        r = a
    l = []
    for x in range(1,r+1):
        if a%x == 0 and b%x == 0:
            l.append(x)
    return max(l)
def bcnn(a, b):
    #nếu a hoặc b = 0, trả về 0
    if a == 0 or b == 0:
        return 0
    #tích của a và b
    t = a*b
    #vòg lặp chạy từ số bé nhất trong 2 số đến tích 2 số
    if a > b:
        r = b
    elif b > a:
        r = a
    else:
        r = a
    l = []
    for x in range(r, t+1):
        if x%a == 0 and x%b == 0:
            l.append(x)
    return min(l)

print(f"ƯCLN{a,b} = {ucln(a,b)}")
print(f"BCNN{a,b} = {bcnn(a,b)}")
# Bài 8: VCT tìm ước chung lớn nhất và bội chung nhỏ nhất của hai số nhập vào từ bàn phím?
a = int(input("Nhập số a: "))
b = int(input("Nhập số b: "))

def ucln(a,b):
    if a == 1 or b == 1:
        return int(1)
    if a > b:
        if a % b == 0:
            return b
        else:
            yield (i for i in range(b-1,0,-1) if b%i == 0)
    if b > a:
        if b % a == 0:
            return a
        else:
            yield (i for i in range(a-1,0,-1) if a%i == 0)

def bcnn(a,b):
    if a == 1 or b == 1:
        yield (x for x in [a,b] if x != 1)
    if a > b:
        if a % b == 0:
            return a
        else:
            yield (i for i in range(b,a*b+1) if i%b == 0 and i%a == 0)
    if b > a:
        if b % a == 0:
            return b
        else:
            yield (i for i in range(b,a*b+1) if i%b == 0 and i%a == 0)
                
print("UcLN của {} và {} là {}".format(a,b,ucln(a,b)))
print("BCNN của {} và {} là {}".format(a,b,bcnn(a,b)))
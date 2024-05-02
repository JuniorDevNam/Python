from math import comb
a = input('Nhập a: ')
b = input('Nhập b: ')
n = input('Nhập số luỹ thừa: ')
print(f"Bạn đã nhập a = {a}")
print(f"Bạn đã nhập b = {b}")
if n.isdigit():
    n = int(n)
    print(f"Bạn đã nhập n = {n}")
    if n < 0:
        quit(f"Chương trình này không hỗ trợ luỹ thừa âm (luỹ thừa bạn đã nhập là {n}).")
else:
    try:
        float(n)
        quit(f"Chương trình này không hỗ trợ luỹ thừa là số thực (luỹ thừa bạn đã nhập là {n})")
    except ValueError:
        quit(f"Chương trình này không hỗ trợ luỹ thừa là 1 ký tự hoặc xâu ký tự. (luỹ thừa bạn đã nhập là {n})")
k = n
h = 0
A = []
N = []
def superscripts(num):
    numsup = ["\u2070","\u00b9","\u00b2","\u00b3","\u2074","\u2075","\u2076","\u2077","\u2078","\u2079"]
    if 0 <= num < 10:
        for x in range(10):
            if num == x:
                return numsup[x]
    elif num >= 10:
        uni = []
        digits = [int(digit) for digit in str(num)]
        for n in digits:
            for x in range(10):
                if n == x:
                    s = numsup[x]
                    uni.append(s)
        result = str("".join(uni))
        return result
def subscripts(num):
    numsub = ["\u2080","\u2081","\u2082","\u2083","\u2084","\u2085","\u2086","\u2087","\u2088","\u2089"]
    if 0 <= num < 10:
        for x in range(10):
            if num == x:
                return numsub[x]
    elif num >= 10:
        uni = []
        digits = [int(digit) for digit in str(num)]
        for n in digits:
            for x in range(10):
                if n == x:
                    s = numsub[x]
                    uni.append(s)
        result = str("".join(uni))
        return result
print(f"Biểu thức được tạo là: ({str(a)} + {str(b)}){superscripts(n)}")
if a.isdigit() and b.isdigit():
    a = int(a)
    b = int(b)
    for x in range(n+1):
        s = comb(n, k)*(a**(n-h))*(b**(n-k))
        if k == n:
            S = f"C{subscripts(n)}{superscripts(h)}{str(a)}{superscripts(n)}"
        if h == n:
            S = f"C{subscripts(n)}{superscripts(h)}{str(b)}{superscripts(n)}"
        if k != n and h != n:
            S = f"C{subscripts(n)}{superscripts(h)}{str(a)}{superscripts(n-h)}{str(b)}{superscripts(n-k)}"
        A.append(s)
        N.append(S)
        k = k - 1
        h = h + 1
else:
    for x in range(n+1):
        if k == n:
            S = f"C{subscripts(n)}{superscripts(h)}{str(a)}{superscripts(n)}"
        if h == n:
            S = f"C{subscripts(n)}{superscripts(h)}{str(b)}{superscripts(n)}"
        if k != n and h != n:
            S = f"C{subscripts(n)}{superscripts(h)}{str(a)}{superscripts(n-h)}{str(b)}{superscripts(n-k)}"
        N.append(S)
        k = k - 1
        h = h + 1
print(N)
print(A)
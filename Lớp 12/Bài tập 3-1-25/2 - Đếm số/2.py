
A, B, C = map(int, input().split())

def run(A, B, C, steps=1, reverse=False):
    count = 0
    if reverse:
        for x in range(A, B+1,steps):
            if x % C == 0:
                count += 1
    else:
        for x in range(A, B+1,steps):
            if x % C != 0:
                count += 1
    return count
allX = 1+B-A
if C == 1:
    print(0)
if C == 5:
    a = str(A)
    a.replace(a[-1],'0')
    kq = allX - run(int(a),B,5,reverse=True)
    print(kq)
else:
    print(run(A, B, C))
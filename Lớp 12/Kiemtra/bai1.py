N = int(input("N: "))
if len(str(N)) == 1:
    if int(str(N)[-1]) < 5:
        print(0)
    if int(str(N)[-1]) >= 5:
        print(10)
else:
    if int(str(N)[-1]) < 5:
        kq = str(N).replace(str(N)[-1],'0')
        print(kq)
    if int(str(N)[-1]) >= 5:
        n = str(N)[-2]+str(N)[-1]
        n2 = str(int(str(N)[-2])+1)+"0"
        kq = str(N).replace(n,n2)
        print(kq)
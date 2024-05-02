N = int(input("N: "))

def prime(N):
    if N<2:
        return "No"
    elif N == 2:
        return "Yes"
    elif N > 2:
        for x in range(2,N):
            if N%x == 0:
                return "No"
            else:
                return "Yes"

print("SNT?  -  ",prime(N))
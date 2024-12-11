N = int(input("N: "))
def check_hop_so(num):
    if num <= 2:
        return False
    for x in range(2,int(num**0.5)+1):
        if num % x == 0:
            return True
    return False

for x in range(4,N+1,2):
    y = N - x
    if check_hop_so(y):
        print(x,y)
        break

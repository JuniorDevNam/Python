n = int(input())
r = []
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True
if n % 2 == 0:
    a = n//2
    b = n//2
else:
    a = (n//2)-1
    b = (n//2)+1
count = 0
while not is_prime(a) and not is_prime(b):
    a -= 1
    b += 1
while is_prime(a) and is_prime(b):
    r.append((a, b))
    count += 1 
    a -= 2
    b += 2
print(count)
for i in range(len(r)):
    print(r[i][0], r[i][1])
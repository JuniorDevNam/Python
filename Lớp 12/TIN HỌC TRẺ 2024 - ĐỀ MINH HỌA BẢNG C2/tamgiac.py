T = int(input())
n = [int(input()) for _ in range(T)]

# số nguyên tố:
N = max(n)*2
primes = [True] * (N+1)
primes[0] = primes[1] = False
for _ in range(2, int(N**0.5) + 1):
    if primes[_]:
        for j in range(_*_, N+1, _):
            primes[j] = False

for x in n:
    count = 0
    for i in range(1, x-1):
        for j in range(i+1, x):
            for k in range(j+1, x+1):
                c1 = i + j
                c2 = i + k
                c3 = j + k
                prime_count = sum([primes[c1],primes[c2],primes[c3]])
                if prime_count == 3 or prime_count == 0:
                    count += 1
    print(count)
import math

def simple_sieve(limit):
    prime = [True] * (limit + 1)
    p = 2
    while p * p <= limit:
        if prime[p]:
            for i in range(p * p, limit + 1, p):
                prime[i] = False
        p += 1
    prime_numbers = []
    for p in range(2, limit + 1):
        if prime[p]:
            prime_numbers.append(p)
    return prime_numbers

def segmented_sieve(n):
    limit = int(math.sqrt(n)) + 1
    prime_numbers = simple_sieve(limit)
    low = limit
    high = 2 * limit
    while low < n:
        if high >= n:
            high = n
        mark = [True] * (limit + 1)
        for i in range(len(prime_numbers)):
            loLim = max(prime_numbers[i] * prime_numbers[i], low + (prime_numbers[i] - low % prime_numbers[i]) % prime_numbers[i])
            for j in range(loLim, high, prime_numbers[i]):
                mark[j - low] = False
        for i in range(low, high):
            if mark[i - low]:
                print(i, end=" ")
        low = low + limit
        high = high + limit

n = 10000000000
segmented_sieve(n
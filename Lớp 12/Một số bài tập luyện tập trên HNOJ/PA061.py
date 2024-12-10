def is_prime(num):
    if num <= 1:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

def count_twin_primes(n):
    twin_primes = []
    for i in range(2, n - 1):
        if is_prime(i) and is_prime(i + 2):
            twin_primes.append((i, i + 2))
    return len(twin_primes)

# Ví dụ sử dụng
n = int(input("Nhập số nguyên dương n: "))
result = count_twin_primes(n)
print(f"Số lượng các cặp số sinh đôi khác nhau mà các số đều không vượt quá {n} là {result}.")
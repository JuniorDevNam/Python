a, b, c, k, n = map(int, input().split())

def fib3(n):
    dp = [0] * (n + 1)
    if n >= 0:
        dp[0] = 0
    if n >= 1:
        dp[1] = 1
    if n >= 2:
        dp[2] = 1
    for i in range(3, n + 1):
        if i % 3 == 1:
            dp[i] = (a * dp[i - 1] + b * dp[i - 2] + c * dp[i - 3]) % k
        elif i % 3 == 2:
            dp[i] = (b * dp[i - 1] + c * dp[i - 2] + a * dp[i - 3]) % k
        else:
            dp[i] = (c * dp[i - 1] + a * dp[i - 2] + b * dp[i - 3]) % k
    return dp[n]

print(fib3(n))
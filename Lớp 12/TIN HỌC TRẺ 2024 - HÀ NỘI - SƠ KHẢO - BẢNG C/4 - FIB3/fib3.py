a, b, c, k, n = map(int, input().split())

if n == 0:
    print(0)
elif n == 1 or n == 2:
    print(1)
else:
    dp = [0, 1, 1]
    for i in range(3, n + 1):
        if i % 3 == 1:
            val = (a * dp[2] + b * dp[1] + c * dp[0]) % k
        elif i % 3 == 2:
            val = (b * dp[2] + c * dp[1] + a * dp[0]) % k
        else:
            val = (c * dp[2] + a * dp[1] + b * dp[0]) % k
        dp[0], dp[1], dp[2] = dp[1], dp[2], val
    print(dp[2])
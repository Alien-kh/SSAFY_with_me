def factorial(n):
    # dp 이용법 익혀보기
    dp = [1] * (n + 1)

    for i in range(2, n + 1):
        dp[i] = dp[i - 1] * i

    return dp[n]


N, M = map(int, input().split())
result = factorial(N) / (factorial(N-M) * factorial(M))
print(int(result))
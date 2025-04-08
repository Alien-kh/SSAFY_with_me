def factorial(n):
    # dp 이용법 익혀보기
    dp = [1] * (n + 1)

    for i in range(2, n + 1):
        dp[i] = dp[i - 1] * i

    return dp[n]


def combination(n, r):
    return factorial(n) // (factorial(r) * factorial(n - r))


T = int(input())

for _ in range(T):
    N, M = map(int, input().split())
    print(combination(M, N))
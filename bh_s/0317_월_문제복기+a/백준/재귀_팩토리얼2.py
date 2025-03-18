# 메모이제이션

memo = [1] * 1001


def factorial(n):
    if memo[n] != 1:
        return memo[n]
    for i in range(2, n + 1):
        memo[i] = memo[i - 1] * i
    return memo[n]


N = int(input())
print(factorial(N))
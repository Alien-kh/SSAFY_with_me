def gcd(a, b):
    while b != 0:
        k = a % b
        a = b
        b = k

    return a


def solve(num1, num2):
    return int(num1 * num2 / gcd(num1, num2))


n1, n2 = map(int, input().split())
result = solve(n1, n2)
print(result)

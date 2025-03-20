def fact(n):
    if n == 0 or n == 1:
        value = 1
    else:
        value = n * fact(n-1)

    return value


N = int(input())
print(fact(N))
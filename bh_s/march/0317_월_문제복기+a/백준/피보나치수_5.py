
def fibo(n):
    if n == 0:
        return 0
    elif n == 1 or n == 2:
        return 1
    elif n >= 3:
        return fibo(n-2) + fibo(n-1)


N = int(input())
print(fibo(N))
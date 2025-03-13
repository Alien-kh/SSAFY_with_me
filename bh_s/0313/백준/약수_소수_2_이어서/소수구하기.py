def is_prime(x):  # 소수 찾기
    if x < 2:
        return False
    if x == 2:
        return True
    if x % 2 == 0:
        return False
    for i in range(3, int(x ** 0.5) + 1, 2):
        if x % i == 0:
            return False
    return True


n, m = map(int, input().split())

# 범위 n ~ m 사이에서 소수를 출력
for i in range(n, m + 1):
    if is_prime(i):
        print(i)

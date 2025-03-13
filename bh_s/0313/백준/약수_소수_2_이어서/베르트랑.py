# def is_prime(x):  # 소수 찾기
#     if x < 2:
#         return False
#     if x == 2:
#         return True
#     if x % 2 == 0:
#         return False
#     for i in range(3, int(x ** 0.5) + 1, 2):
#         if x % i == 0:
#             return False
#     return True
#
#
# while True:
#     n = int(input())
#     if n == 0:
#         break
#     cnt = 0
#     for i in range(n+1, 2*n+1):
#         if is_prime(i):
#             cnt += 1
#
#     print(cnt)


def sieve_of_eratosthenes(limit):
    sieve = [True] * (limit + 1)
    sieve[0] = sieve[1] = False  # 0과 1은 소수가 아님

    for start in range(2, int(limit ** 0.5) + 1):
        if sieve[start]:
            for i in range(start * start, limit + 1, start):
                sieve[i] = False

    return sieve


while True:
    n = int(input())
    if n == 0:  # 0 입력이 들어오면 종료.
        break
    # 2n까지의 소수 구하기
    sieve = sieve_of_eratosthenes(2 * n)

    # n부터 2n까지의 소수 개수 세기
    count = 0
    for i in range(n + 1, 2 * n + 1):
        if sieve[i]:
            count += 1

    print(count)
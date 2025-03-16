def is_prime(x):
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


T = int(input())
n_list = [int(input()) for _ in range(T)]

# 최대값을 구한 후 한 번에 소수 리스트를 구함
max_n = max(n_list)
primes = [True] * (max_n + 1)
primes[0] = primes[1] = False  # 0과 1은 소수가 아님

# 에라토스테네스의 체를 사용하여 소수 구하기
for i in range(2, int(max_n ** 0.5) + 1):
    if primes[i]:
        for j in range(i * i, max_n + 1, i):
            primes[j] = False

# 소수 목록만 추출
prime_list = [i for i in range(2, max_n + 1) if primes[i]]

# 소수를 집합으로 만들어서 O(1)로 체크 가능하도록 함
prime_set = set(prime_list)

# 각 짝수에 대한 골드바흐 파티션 개수 구하기
for n in n_list:
    count = 0
    for p in prime_list:
        if p > n // 2:  # p + q (두 소수)가 n이고, p > n/2라면 q는 n/2 보다 반드시 작아야 한다.
            break
        if (n - p) in prime_set:
            count += 1
    print(count)

def is_prime(x):    # 소수 찾기
    if x < 2:
        return False
    if x == 2:
        return True
    if x % 2 == 0:  # 2를 제외한 짝수는 모두 소수가 아님.
        return False
    for i in range(3, int(x ** 0.5) + 1, 2):    # 루트(2)로 제곱근이 나오면 X
        if x % i == 0:
            return False
    return True


def find_v(d):
    if d <= 2:
        return 2
    if d % 2 == 0:  # d 값 자체에서도 확인
        d += 1
    while True:
        if is_prime(d):
            return d
        d += 2  # d가 홀수일때 2씩 더해서 봐야 할 수 자체를 줄인다.


N = int(input())
for _ in range(N):
    data = int(input())
    print(find_v(data))


def prime_factors(n):
    d = 2  # 가장 작은 소수인 2부터 시작
    while d * d <= n:  # d가 n의 제곱근 이하일 때만 검사
        while n % d == 0:
            print(d)
            n //= d
        d += 1
    if n > 1:  # 마지막에 남은 값이 소수라면 출력
        print(n)


num = int(input())
prime_factors(num)

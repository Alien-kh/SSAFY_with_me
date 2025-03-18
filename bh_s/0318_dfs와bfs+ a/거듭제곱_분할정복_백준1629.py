# 그냥 연산을 해서 print 하면 시간이 터진다.

def power_mod(a, b, c):
    result = 1  # 결과를 위한 변수 (여기에 곱할거임)
    while b > 0:
        if b % 2 == 1:  # b가 홀수이면
            # 현재 a 값을 결과에 곱하고, c로 나눈 나머지를 저장.
            result = (result * a) % c
        # a 를 제곱하고 c 로 나눈 나머지를 저장.
        a = (a * a) % c
        # b 를 나눠서 지수의 절반으로 줄인다.
        b //= 2
    return result


A, B, C = map(int, input().split())

print(power_mod(A, B, C))

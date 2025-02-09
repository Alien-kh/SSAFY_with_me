# swea 22795
T = int(input().strip())
for _ in range(T):
    lst = list(map(int, input().split()))
    a, b, c, d, e, f = lst  # 언패킹 (a~f는 여섯 부하의 키)
    maximum = max(lst)
    for x in range(maximum + 1, 1008):  # x는 일곱번째 부하의 키
        y = (a + b + c + d + e + f + x) / 7  # 일곱 부하의 평균값
        if y % 1 == 0:
            print(x)
            break

# 저번 A형 기출

T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    data = list(map(int, input().split()))

    max_v = max(data)
    cnt = 0
    sum_v = 0
    for i in data:
        if (max_v - i) % 2 == 1:  # 차이가 홀수라면
            cnt += 1
        sum_v += (max_v - i)  # 차이의 누적합 구하기
    min_v = 999999
    # 2x + y = sum_v
    # x : 짝수 일수, y : 홀수 일수
    for x in range((sum_v - cnt) // 2 + 1):
        y = sum_v - 2 * x
        if min_v > abs(x - y):
            min_v = abs(x - y)
            a, b = x, y  # 홀수 일수와 짝수 일수의 차이가 최소이면 저장 (계속 갱신하며)

    print(f'#{tc} {max(2 * a, 2 * b - 1)}')

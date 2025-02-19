def func():
    num = 0
    for s in range(max(data) + 1):  # 시간

        if s % M == 0 and s != 0:
            num += K
        num -= counts[s]
        if num <0:
            return f'#{tc} Impossible'
    return f'#{tc} Possible'


T = int(input())
for tc in range(1, T+1):
    N, M, K = map(int, input().strip().split())  # 사람수, M초당 K개의 붕어빵
    data = list(map(int, input().strip().split()))
    # 카운팅 정렬을 통해 M초에 오는 손님의 수 정리
    counts = [0] * (max(data) + 1)
    for i in data:
        counts[i] += 1

    # func()
    print(func())
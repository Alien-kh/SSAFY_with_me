T = int(input())

for tc in range(1, T + 1):
    N = int(input())
    carrots = list(map(int, input().split()))

    max_increase = 1  # 최소 연속 증가 개수는 1
    cnt_increase = 1  # 현재 연속 증가 개수

    for i in range(N - 1):
        if carrots[i] < carrots[i + 1]:
            cnt_increase += 1  # 연속 증가 중이면 개수 추가
        else:
            if cnt_increase > max_increase:  # 최대 증가 구간 갱신
                max_increase = cnt_increase
            cnt_increase = 1  # 증가가 끊기면 초기화

    # 마지막 증가 구간 고려 <- 여길 고려 못해서 계속 막혔음,,,
    if cnt_increase > max_increase:
        max_increase = cnt_increase

    print(f'#{tc} {max_increase}')

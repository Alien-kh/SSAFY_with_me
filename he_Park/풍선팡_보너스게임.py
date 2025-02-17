T = int(input().strip())
for tc in range(1, T+1):
    N = int(input().strip())
    arr = [list(map(int, input().strip().split())) for _ in range(N)]
    max_v = -1  # 나올 수 있는 최소값으로 초기화
    min_v = 21e8  # 나올 수 있는 최대값으로 초기화  # 21억(tip)
    # C언어 int 형태는 대략 21억이 최대값
    for r in range(N):
        for c in range(N):
            sum_v = arr[r][c]
            for d in [[-1, 0], [1, 0], [0, -1], [0, 1]]:
                for k in range(1, N):
                    dr = r + d[0] * k
                    dc = c + d[1] * k
                    if 0 <= dr < N and 0 <= dc < N:
                        sum_v += arr[dr][dc]
            if max_v < sum_v:
                max_v = sum_v
            if min_v > sum_v:
                min_v = sum_v
    print(f'#{tc} {max_v - min_v}')
T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().strip().split())
    arr = [list(map(int, input().strip().split())) for _ in range(N)]
    # 현재 위치 인덱스: r, c
    a = [[-1, 0], [1, 0], [0, -1], [0, 1]] #상하좌우
    b = [[-1, -1], [-1, 1], [1, 1], [1, -1]] #시계방향
    max_v = 0
    for r in range(N):
        for c in range(N):
            for i in [a, b]:
                sum_v = arr[r][c]
                for d in i:
                    for k in range(1, M):
                        dr = r + d[0] * k
                        dc = c + d[1] * k
                        if 0 <= dr < N and 0 <= dc < N:
                            sum_v += arr[dr][dc]
                if max_v < sum_v:
                    max_v = sum_v


    print(f'#{tc} {max_v}')

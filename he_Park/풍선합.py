T = int(input().strip())
for tc in range(1, T + 1):
    N, M = map(int, input().strip().split())
    arr = [list(map(int, input().split())) for _ in range(N)]

    max_v = 0
    for r in range(N):
        for c in range(M):
            s = arr[r][c]  # 현재 위치 꽃가루 개수
            cnt = s
            for dr, dc in [[-1, 0], [1, 0], [0, -1], [0, 1]]:  # 상하좌우
                for l in range(1, s+1):
                    nr = r + dr * l
                    nc = c + dc * l
                    if 0 <= nr < N and 0 <= nc < M:
                        cnt += arr[nr][nc]  # 상하좌우 s개의 합
            if max_v < cnt:
                max_v = cnt

    print(f'#{tc} {max_v}')
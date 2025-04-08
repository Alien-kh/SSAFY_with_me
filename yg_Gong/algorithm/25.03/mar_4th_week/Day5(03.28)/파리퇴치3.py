T = int(input())
for tc in range(1, T + 1):
    N, M = map(int, input().split())
    flies = [list(map(int, input().split())) for _ in range(N)]
    max_count = 0   # 최대 파리수
    sum_fly1 = 0     # +로 잡는 파리수
    sum_fly2 = 0    # x로 잡는 파리
    dr = [1,0,-1,0] #상우하좌
    dc = [0,1,0,-1]
    dx = [1,1,-1,-1]   # 좌상, 우상, 우하, 좌하
    dy = [-1,1,1,-1]

    for i in range(N):
        for j in range(N):
            sum_fly1 = flies[i][j]
            sum_fly2 = flies[i][j]

            for d in range(4):  # 방향
                for step in range(1,M):    #파리채 크기만큼 이동
                    # + 모양
                    pi = i + dr[d] * step
                    pj = j + dc[d] * step
                    # x 모양
                    xi = i + dx[d] * step
                    xj = j + dy[d] * step
                    if 0 <= pi < N and 0 <= pj < N:
                        sum_fly1 += flies[pi][pj]

                    if 0 <= xi < N and 0 <= xj < N:
                        sum_fly2 += flies[xi][xj]

            max_count = max(max_count, sum_fly1, sum_fly2)


    print(f'#{tc} {max_count}')
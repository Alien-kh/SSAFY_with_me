T = int(input())
for tc in range(1, T + 1):
    N = int(input())    # 달팽이 크기
    dx = [0, 1, 0, -1]  # 우 하 좌 상
    dy = [1, 0, -1, 0]

    snail = [[0] * N for _ in range(N)]
    num = 1 # 배열안에 넣어줄 값
    i = 0   # 방향 인덱스
    x,y = 0,0
    while num <= N * N:
        snail[x][y] = num
        num += 1

        nx = x + dx[i]
        ny = y + dy[i]

        if 0 <= nx < N and 0 <= ny < N and snail[nx][ny] == 0:
            x, y = nx, ny
        else:
            i = (i + 1) % 4
            x += dx[i]
            y += dy[i]

    print(f'#{tc}')
    for row in snail:
        print(*row)



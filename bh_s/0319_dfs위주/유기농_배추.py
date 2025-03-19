T = int(input())

for _ in range(T):
    M, N, K = map(int, input().split())
    field = [[0] * N for _ in range(M)] # 밭

    for _ in range(K):
        x, y = map(int, input().split())    # 배추 위치 x, y
        field[x][y] = 1

    def move_dfs(x, y):
        stack = [(x, y)]
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

        while stack:    # 스택이 차 있으면
            cx, cy = stack.pop()
            if 0 <= cx < M and 0 <= cy < N and field[cx][cy] == 1:  # 범위를 벗어나지 않으면서, 배추가 있으면!
                field[cx][cy] = 0  # 방문 처리

                for dx, dy in directions:
                    nx, ny = cx + dx, cy + dy   # 다음 이동 방향은 directions 안의 x , y + 현재 x, y
                    stack.append((nx, ny))

    worm_count = 0

    for i in range(M):
        for j in range(N):
            if field[i][j] == 1:  # 배추가 있는 경우
                move_dfs(i, j)  # 스택 기반 DFS 수행  -> 연결된 배추들 다 0으로 만들고 카운트 + 1
                worm_count += 1

    print(worm_count)
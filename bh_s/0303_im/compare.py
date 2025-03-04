def maze(r, c):
    stack = [(r, c)]
    while stack:
        r, c = stack.pop()  # 스택에서 좌표를 하나 꺼냄

        # 도착 지점(3)을 찾으면 1 반환
        if arr[r][c] == '3':
            return 1

        # 네 방향으로 이동
        for d in [[-1, 0], [1, 0], [0, -1], [0, 1]]:
            nr = r + d[0]
            nc = c + d[1]

            # 미로 범위 내에서 이동 가능하고 아직 방문하지 않은 곳
            if 0 <= nr < N and 0 <= nc < N and not visited[nr][nc] and arr[nr][nc] != '1':
                visited[nr][nc] = 1  # 방문 처리
                stack.append((nr, nc))  # 이동할 위치 스택에 추가

    return 0  # 도착지점에 도달할 수 없으면 0 반환

T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    arr = [list(input().strip()) for _ in range(N)]  # 미로 입력 받기
    visited = [[0] * N for _ in range(N)]
    
    # 시작 지점 '2' 찾기
    for i in range(N):
        for j in range(N):
            if arr[i][j] == '2':  # 시작 지점 찾으면
                s = i, j
                visited[i][j] = 1  # 방문 처리

    print(f'#{tc} {maze(*s)}')
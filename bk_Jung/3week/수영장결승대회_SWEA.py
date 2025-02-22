from collections import deque

def bfs(N, graph, start, end):
    sx, sy = start  # 시작 좌표
    ex, ey = end  # 목표 좌표

    # 방향 (상, 하, 좌, 우)
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    # 방문 체크 (3차원 배열: [x][y][t % 3])
    visited = [[[False] * 3 for _ in range(N)] for _ in range(N)]

    queue = deque()
    queue.append((sx, sy, 0))  # (x, y, time)
    visited[sx][sy][0] = True

    while queue:
        x, y, time = queue.popleft()

        # 목표 도착
        if (x, y) == (ex, ey):
            return time

        for k in range(4):
            nx, ny = x + dx[k], y + dy[k]

            if 0 <= nx < N and 0 <= ny < N and not visited[nx][ny][(time + 1) % 3]:
                # 섬(1)이면 이동 불가
                if graph[nx][ny] == 1:
                    continue

                # 소용돌이(2)일 때 대기 처리 개선
                next_time = time + 1
                if graph[nx][ny] == 2:
                    # 소용돌이가 비활성화될 때까지 기다림
                    wait_time = (3 - (next_time % 3)) % 3
                    next_time += wait_time

                # 정상 이동 가능
                visited[nx][ny][next_time % 3] = True
                queue.append((nx, ny, next_time))

    return -1  # 목표 지점 도달 불가


# 입력 처리
T = int(input())  # 테스트 케이스 수
for test_case in range(1, T + 1):
    N = int(input())  # 지도 크기
    graph = [list(map(int, input().split())) for _ in range(N)]
    sx, sy = map(int, input().split())  # 시작점
    ex, ey = map(int, input().split())  # 목표점

    result = bfs(N, graph, (sx, sy), (ex, ey))
    print(f'#{test_case} {result}')

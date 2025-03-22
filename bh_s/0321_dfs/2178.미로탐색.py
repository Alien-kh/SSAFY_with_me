dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]


def bfs():
    q = [(0, 0, 1)]
    while q:
        r, c, cnt = q.pop(0)

        # 도착 지점에 도달하면 최단 거리 반환
        if r == N - 1 and c == M - 1:
            return cnt

        for d in range(4):
            nr = r + dr[d]
            nc = c + dc[d]

            if 0 <= nr < N and 0 <= nc < M and data[nr][nc] == '1' and not visited[nr][nc]:
                visited[nr][nc] = True
                q.append((nr, nc, cnt + 1))

    return -1


N, M = map(int, input().split())
data = [list(input()) for _ in range(N)]
visited = [[False] * M for _ in range(N)]

# 시작점 방문 처리
visited[0][0] = True

result = bfs()
print(result)
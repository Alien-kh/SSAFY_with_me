# 나중에 다시 풀 땐 dfs 스택 써서 해보자
def bfs(r, c):
    global visited, cnt
    q = [(r, c)]
    while q:
        cr, cc = q.pop(0)
        for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            nr, nc = cr + dr, cc + dc
            if 0 <= nr < N and 0 <= nc < M:
                if not visited[nr][nc] and arr[nr][nc]:
                    q.append((nr, nc))
                    visited[nr][nc] = 1
    cnt += 1


T = int(input())
for tc in range(1, T + 1):
    M, N, K = map(int, input().split())
    arr = [[0] * M for _ in range(N)]
    visited = [[0] * M for _ in range(N)]
    for _ in range(K):
        x, y = map(int, input().split())
        arr[y][x] = 1
    cnt = 0
    for i in range(N):
        for j in range(M):
            if arr[i][j] and not visited[i][j]:
                visited[i][j] = 1
                bfs(i, j)
    print(cnt)
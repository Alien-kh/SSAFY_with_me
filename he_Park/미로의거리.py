def bfs(r, c, cnt):
    q = [(r, c, cnt)]
    visited = [[0]*N for _ in range(N)]

    while q:
        cr, cc, dist = q.pop(0)
        if arr[cr][cc] == '3':
            return dist - 1
        
        for d in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            nr = cr + d[0]
            nc = cc + d[1]
            if 0 <= nr < N and 0 <= nc < N:
                if arr[nr][nc] != '1' and not visited[nr][nc]:
                    q.append((nr, nc, dist + 1))
                    visited[nr][nc] = 1

    return 0

T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    arr = [list(input()) for _ in range(N)]
    for i in range(N):
        for j in range(N):
            if arr[i][j] == '2':
                result = bfs(i, j, 0)

    print(f'#{tc} {result}')
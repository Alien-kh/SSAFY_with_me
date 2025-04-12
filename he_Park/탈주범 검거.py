T = int(input())
for tc in range(1, T + 1):
    N, M, R, C, L = map(int, input().split())  # NxM (R행, C열) L시간
    arr = [list(map(int, input().split())) for _ in range(N)]
    visited= [[0] * M for _ in range(N)]

    up = [1, 2, 5, 6]
    down = [1, 2, 4, 7]
    left = [1, 3, 4, 5]
    right = [1, 3, 6, 7]

    dic = {1:(up, down, left, right), 2:(up, down), 3:(left, right),
           4: (up, right), 5: (down, right), 6: (left, down), 7: (up, left)}

    def bfs(r, c):
        q = [(r, c, 1)]
        visited[r][c] = 1

        while q:  # 더이상 q에 추가할 지점이 없거나,
            cr, cc, cnt = q.pop(0)

            if cnt == L:  # L시간이 경과하면 stop
                break

            for dr, dc, x in [(-1, 0, up), (1, 0, down), (0, -1, left), (0, 1, right)]:
                nr, nc = cr + dr, cc + dc
                if 0 <= nr < N and 0 <= nc < M and not visited[nr][nc]:
                    if x in dic[arr[cr][cc]] and arr[nr][nc] in x:
                        q.append((nr, nc, cnt + 1))
                        visited[nr][nc] = 1

    bfs(R, C)
    result = 0
    for i in visited:
        result += i.count(1)
    print(f'#{tc} {result}')
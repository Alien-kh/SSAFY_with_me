def dfs(r, c, cnt):
    global max_cnt
    for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
        nr = r + dr
        nc = c + dc
        if 0 <= nr < N and 0 <= nc < N and not visited[nr][nc]:
            if arr[r][c] > arr[nr][nc]:
                visited[nr][nc] = 1
                dfs(nr, nc, cnt + 1)
                visited[nr][nc] = 0
    else:
        if max_cnt < cnt:
            max_cnt = cnt
        return


T = int(input())
for tc in range(1, T+1):

    N, K = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]
    max_v = 0
    for row in arr:
        if max_v < max(row):
            max_v = max(row)  # 행렬의 최댓값 찾기

    max_cnt = 0  # 최종 정답(가장 긴 등산로의 길이)

    for x in range(N):
        for y in range(N):
            for z in range(1, K+1):  # 최대 K까지 깎을 수 있다.
                arr[x][y] -= z

                for i in range(N):
                    for j in range(N):
                        if arr[i][j] == max_v:  # 최댓값의 인덱스 구하기
                            visited = [[0] * N for _ in range(N)]
                            visited[i][j] = 1
                            dfs(i, j, 1)  # 상하좌우 이동
                           
                arr[x][y] += z  # 원상복귀

    print(f'#{tc} {max_cnt}')
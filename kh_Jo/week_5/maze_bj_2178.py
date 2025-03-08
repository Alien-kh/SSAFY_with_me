from collections import deque
def bfs(start, end):
    q = deque()
    visited = [[0] * M for _ in range(N)] # 미로와 똑같은 사이즈의 방문체크
    start_r, start_c = start
    visited[start_r][start_c] = 1
    q.append(start)
    destination = [[-1, 0], [1, 0], [0, 1], [0, -1]]
    while q:
        curr_r, curr_c = q.popleft()
        if (curr_r, curr_c) == end:
            return visited[curr_r][curr_c]
        for dr, dc in destination:
            nr = curr_r + dr
            nc = curr_c + dc
            if 0 <= nr < N and 0 <= nc < M and maze[nr][nc] == '1' and visited[nr][nc] == 0: # 범위 이내이고 1로 갈 수 있는 부분이고 방문한 적이 없다면
                q.append([nr, nc])

                visited[nr][nc] = visited[curr_r][curr_c]+1 # 이동할 때 1씩 더해주면서 방문도장 찍어줘야됨
            # else:
            #     return 0 # 만약 도착 못했을 떄를 대비한건데 문제에서는 항상 도착

N, M =  map(int, input().split())
maze = [input() for _ in range(N)] # input만 해준 이유는 띄어쓰기 없이 전달되기에
start = 0, 0 # 시작 위치는 고정
end = N-1, M - 1 #  끝자리도 고정
result = bfs(start, end)
print(result)
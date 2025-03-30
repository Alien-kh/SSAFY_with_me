from collections import deque


def bfs():
    q = deque()
    q.append((0,0))
    visited[0][0] = 1
    dx = [-1,1,0,0]
    dy = [0,0,-1,1]

    while q:
        x,y = q.popleft()
        now = graph[x][y]
        visited[x][y] = 1
        if now == -1:
            print('HaruHaru')
            return

        for k in range(4):
            for i in range(now):
                nx = x + dx[k] * now
                ny = y + dy[k] * now

                if -1 < nx < N and -1 < ny < N:
                    if not visited[nx][ny]:
                        q.append((nx,ny))
    
    print('Hing')
    return



N = int(input())
graph = [list(map(int,input().split())) for _ in range(N)]
visited = [[0] * N for _ in range(N)]
bfs()
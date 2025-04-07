from collections import deque

T  = int(input())
for tc in range(T):
    N,M,K = map(int,input().split())

    graph = [[0] * M for _ in range(N)]
    
    for i in range(K):
        x,y = map(int,input().split())
        graph[x][y] = 1

    dx = [-1,1,0,0]
    dy = [0,0,-1,1]
    cnt = 0

    for i in range(N):
        for j in range(M):
            if graph[i][j] == 1:
                graph[i][j] = 2
                q = deque()
                q.append((i,j))
                cnt += 1
                while q:
                    x,y = q.popleft()
                    for k in range(4):
                        nx = x + dx[k]
                        ny = y + dy[k]

                        if -1 < nx < N and -1 < ny < M:
                            if graph[nx][ny] == 1:
                                q.append((nx,ny))
                                graph[nx][ny] = 2
    
    print(cnt)


from collections import deque
import copy

def bfs():
    queue = deque()
    queue.append([0,0,0])
    visited[0][0][0] = 1

    dx = [-1,1,0,0]
    dy = [0,0,-1,1]

    while queue:
        x,y,w = queue.popleft()
        if x == N-1 and y == M-1:
            return visited[x][y][w]
        for k in range(4):
            nx = x + dx[k]
            ny = y + dy[k]

            if 0 <= nx < N and 0<= ny < M:
                if graph[nx][ny] == 0 and visited[nx][ny][w] == 0:
                    visited[nx][ny][w] = visited[x][y][w] + 1
                    queue.append([nx,ny,w])
                elif graph[nx][ny] == 1 and w == 0:
                    visited[nx][ny][w+1] = visited[x][y][w] + 1
                    queue.append((nx,ny,w+1))
    return -1

N,M = map(int,input().split())
graph = [list(map(int,input())) for _ in range(N)]

visited = [[[0] * 2 for _ in range(M)] for _ in range(N)]

print(bfs())

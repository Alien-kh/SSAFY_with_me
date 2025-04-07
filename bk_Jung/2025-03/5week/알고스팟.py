import heapq
import sys

def dijkstra():
    pq = []
    heapq.heappush(pq,(0,0,0)) # x,y,가중치
    distance[0][0] = 0

    dx = [-1,1,0,0]
    dy = [0,0,-1,1]

    while pq:
        x,y,dist = heapq.heappop(pq)

        if distance[x][y] < dist:
            continue
        if graph[x][y] == 1:
            dist += 1
        for k in range(4):
            nx = x + dx[k]
            ny = y + dy[k]
            if -1 < nx < N and -1 < ny < M:
                if distance[nx][ny] <= dist:
                    continue

                heapq.heappush(pq,(nx,ny,dist))
                distance[nx][ny] = dist


M,N = map(int,sys.stdin.readline().split())
INF = 21e9
graph = [list(map(int,sys.stdin.readline().rstrip())) for _ in range(N)]
distance = [[INF] * M for i in range(N)]
dijkstra()
print(distance[N-1][M-1])
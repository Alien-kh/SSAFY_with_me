import heapq

def dijkstra():
    pq = []
    heapq.heappush(pq,(graph[0][0],0,0)) # 거리,x,y 힙에 넣기
    distance[0][0] = graph[0][0]
    dx = [-1,1,0,0]
    dy = [0,0,-1,1]

    while pq:
        w,x,y = heapq.heappop(pq)

        if distance[x][y] < w:
            continue

        for k in range(4):
            nx = x + dx[k]
            ny = y + dy[k]

            if -1 < nx < N and -1 < ny < N:
                cost = graph[nx][ny] + w
                if cost < distance[nx][ny]:
                    heapq.heappush(pq,(cost,nx,ny))
                    distance[nx][ny] = cost

T = 0
while True:
    T += 1
    N = int(input())
    if N == 0:
        break
    INF = 21e9
    graph = [list(map(int,input().split())) for _ in range(N)]
    distance = [[INF] * N for _ in range(N)]

    dijkstra()

    print(f'Problem {T}: {distance[N-1][N-1]}')

    
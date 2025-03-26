import heapq
import sys


def dijkstra(start):
    pq = []
    heapq.heappush(pq,(0,start))
    distance[1][0] = 0

    while pq:
        dist, now = heapq.heappop(pq)

        if dist > distance[now][k-1]:
            continue

        for i in graph[now]:  # 갈수 있는 경로
            cost = dist + i[1] # 값은 현재 거리 + 다음 거리 가는데 드는 비용
            if distance[i[0]][k-1] <= cost:
                continue
            distance[i[0]][k-1] = cost
            distance[i[0]].sort()
            heapq.heappush(pq,(cost,i[0]))


n,m,k = map(int,sys.stdin.readline().split()) # n 도시 개수 m  도시 간선 K 최단경로 넘버
graph = [[] for _ in range(n+1)]
for i in range(m):
    a,b,w = map(int,sys.stdin.readline().split())
    graph[a].append((b,w)) # 도착 도시, 가중치

INF = 21e9
distance = [[INF for _ in range(k+1)] for _ in range(n+1)]
visited = [[0 for _ in range(n+1)] for _ in range(n+1)]

dijkstra(1)


for i in range(1,n+1):
    if distance[i][k-1] == INF:
        print(-1)
        continue
    print(distance[i][k-1])



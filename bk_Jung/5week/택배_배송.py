import heapq

def dijkstra(start):
    pq = []
    heapq.heappush(pq,(0,start))
    distance[start] = 0

    while pq:
        dist, now = heapq.heappop(pq)

        if dist > distance[now]:
            continue

        for i in graph[now]:
            cost = dist + i[1]
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(pq,(cost,i[0]))
 


N,M = map(int,input().split())
graph = [[] for _ in range(N+1)]

for i in range(M):
    a,b,w = map(int,input().split())
    graph[a].append((b,w))
    graph[b].append((a,w))
INF = 21e9
distance = [INF] * (N+1)

dijkstra(1)
print(distance[N])
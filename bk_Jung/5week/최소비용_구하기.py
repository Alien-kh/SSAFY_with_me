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


N = int(input())
M = int(input())
graph = [[] for _ in range(N+1)] 

for i in range(M):
    a,b,w = map(int,input().split())
    graph[a].append((b,w)) # 도착지점, 가중치 순서
start,end = map(int,input().split())
distance = [21e9] * (N+1)
dijkstra(start)

print(distance[end])
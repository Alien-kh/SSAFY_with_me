import heapq

def dijkstra(start):
    distance = [21e9] * (N+1) 
    pq = []
    heapq.heappush(pq,(0,start))
    distance[start] = 0

    while pq:
        dist , now = heapq.heappop(pq)

        if dist > distance[now]:
            continue

        for i in graph[now]:
            cost = dist + i[1]
            if distance[i[0]] > cost:
                distance[i[0]] = cost
                heapq.heappush(pq,(cost,i[0]))

    return distance

N,M,X = map(int,input().split())
graph = [[] for _ in range(N+1)]
for i in range(M):
    a,b,w = map(int,input().split())
    graph[a].append((b,w)) # 노드, 가중치를 a에 넣음


go_X = [0]

for i in range(1,N+1):
    d = dijkstra(i)
    go_X.append(d[X])

d2 = dijkstra(X)
max_result = 0
for i in range(1,N+1):
    if max_result < go_X[i] + d2[i]:
        max_result = go_X[i] + d2[i]

print(max_result)
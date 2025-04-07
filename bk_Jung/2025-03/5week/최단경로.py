import heapq


def dijkstra(start):
    q = []
    heapq.heappush(q,(0,start)) # q를 힙으로 처리 , 시작을 넣음
    distance[start] = 0 # 시작 거리는 0

    while q:
        dis, now = heapq.heappop(q) # 거리가 가장 짧은 노드 꺼냄
        print(q,dis,now)
        # 현재 노드가 이미 처리되었다면 무시
        # 해당 노드의 비용이 현재 distance 배열에 기록보다 크다면 무시
        if distance[now] < dis:
            continue
        # 현재 노드와 연결된 다른 인접한 노드들을 확인
        for i in graph[now]: # i -> 이동할수 있는 다음 노드
            cost = dis + i[1] # 다음 노드로 가는 비용
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q,(cost,i[0]))



INF = int(21e9)
V,E = map(int,input().split())
K = int(input())
graph = [[] for _ in range(V+1)]
distance = [INF] * (V+1)
for i in range(E):
    a,b,w = map(int,input().split())
    graph[a].append((b,w))

dijkstra(K)
for i in range(1,V+1):
    if distance[i] == INF:
        print('INF')
        continue
    print(distance[i])
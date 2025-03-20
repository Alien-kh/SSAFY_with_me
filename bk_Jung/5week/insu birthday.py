import heapq

def dijkstra_insu(start):
    q = []
    heapq.heappush(q,(0,start))
    distance_insu[start] = 0

    while q:
        dis, now = heapq.heappop(q)

        if distance_insu[now] < dis: # 저장된 거리보다 멀다면 다음 루프로
            continue

        for i in graph[now]:
            cost = dis + i[1] # 다음 노드의 거리를 더함
            if cost < distance_insu[i[0]]: # 더한게 저장된 거리보다 작다면
                distance_insu[i[0]] = cost # 거리 초기화
                heapq.heappush(q,(cost,i[0])) # 힙에 넣어줌

def dijkstra(start):
    distance = [INF] * (V+1)
    q = []
    heapq.heappush(q,(0,start))
    distance[start] = 0

    while q:
        dis, now = heapq.heappop(q)

        if distance[now] < dis:
            continue

        for i in graph[now]:
            cost = dis + i[1]
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q,(cost,i[0]))

    return distance[k]

T = int(input())
for tc in range(1,T+1):
    INF = int(21e9)
    V,E,k = map(int,input().split()) # k가 인수네 집
    graph = [[] for _ in range(V+1)]
    distance_insu = [INF] * (V+1)
    for i in range(E):
        a,b,w = map(int,input().split())
        graph[a].append((b,w))

    dijkstra_insu(k)
    max_result = 0
    for i in range(1,V+1):
        if i == k: # 인수네 집은 패스
            continue

        result = distance_insu[i] + dijkstra(i) # 현재 인수집 까지 가는 거리
        if max_result < result:
            max_result = result

    print(f'#{tc} {max_result}')
import heapq


def prim(start):
    visited[start] = 1
    route = []
    heap = list(graph[start])  # 원본 데이터 훼손 방지
    heapq.heapify(heap) # 리스트를 즉각적으로 힙으로 만들어줌
    res = 0

    while heap:
        weight, node = heapq.heappop(heap)
        if not visited[node]:  # 방문하지 않은 노드만 선택
            visited[node] = 1
            route.append(node)
            res += weight
            for edge in graph[node]:
                if not visited[edge[1]]:
                    heapq.heappush(heap, edge)

    return route, res
while True:
    all_light = 0
    v, e = map(int, input().split())
    if not v and not e:
        break
    graph = [[] for _ in range(v + 1)]
    visited = [0] * (v + 1)

    for i in range(1, e + 1):
        u, v, weight = map(int, input().split())
        all_light += weight
        graph[u].append([weight, v])
        graph[v].append([weight, u])

    # 실행 및 결과 출력
    result = prim(0)
    print(all_light - result[1])


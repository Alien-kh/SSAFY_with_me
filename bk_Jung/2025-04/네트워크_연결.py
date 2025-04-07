import heapq


def prim(start):
    visited[start] = 1
    heap = list(graph[start])
    heapq.heapify(heap)
    res = 0
    route = []
    while heap:
        weight,now = heapq.heappop(heap)
        if visited[now]:
            continue
        res += weight
        route.append(now)
        visited[now] = 1
        for edge in graph[now]:
            if not visited[edge[1]]:
                heapq.heappush(heap,edge)

    return res,route


N = int(input())
M = int(input())
graph = [[] for _ in range(N+1)]
for i in range(M):
    a,b,w = map(int,input().split())
    graph[a].append((w,b))
    graph[b].append((w,a))

visited = [0] * (N+1)

result = prim(1)
print(result[0])
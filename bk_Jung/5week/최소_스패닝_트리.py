import heapq
import sys

def prim(start):
    visited[start] = 1
    route = []
    heap = list(graph[start])  # 원본 데이터 훼손 방지
    heapq.heapify(heap)
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

# 입력 최적화
input = sys.stdin.read
data = input().split("\n")

v, e = map(int, data[0].split())
graph = [[] for _ in range(v + 1)]
visited = [0] * (v + 1)

for i in range(1, e + 1):
    if data[i].strip():  # 빈 줄 방지
        u, v, weight = map(int, data[i].split())
        graph[u].append([weight, v])
        graph[v].append([weight, u])

# 실행 및 결과 출력
result = prim(1)
print(result[1])  # 최소 신장 트리의 총 가중치 출력

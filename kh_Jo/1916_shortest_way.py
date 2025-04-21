# bj 최소비용 구하기
import heapq
INF = 21e8 # 그냥 비교용 큰 수
def dijkstra(start_node):
    pq = [(0,start_node)] # 시작 지점은 가중치 0
    dists = [INF] * (N+1)
    dists[start_node] = 0

    while pq:
        dist, node = heapq.heappop(pq)
        if dists[node] < dist:
            continue # 만약 이전의 더 낮은 가중치로 지점에 도착한 적이 있다면 넘어가기 여기서 dist[node] <=dist로 하면 무조건 최댓값이 떠서 실패한다. 실수하지 말기!
        for next_info in graph[node]:
            next_dist = next_info[1] # 다음 노드로 가는 가중치
            next_node = next_info[0]
            new_dist = dist+next_dist # 다음 노드로 가는 누적거리는 현재 거리 + 가중치
            if dists[next_node] <= new_dist:
                continue # 만약 더 가까이 간 적이 있다면 skip

            dists[next_node] = new_dist
            heapq.heappush(pq, (new_dist, next_node))
    return dists[end_node]# 무조건 도달 가능해서 결과값 존재

N = int(input()) # 도시의 개수 (정점)
M = int(input()) # 버스의 개수 (간선)
graph = [[] for _ in range(N+1)] # 0 번 정점은 버리기용
for _ in range(M):
   u, v, w = map(int, input().split()) # 시작 정점, 도착 정점, 비용
   graph[u].append((v, w))
start_node , end_node = map(int,input().split())

result = dijkstra(start_node)
print(result)
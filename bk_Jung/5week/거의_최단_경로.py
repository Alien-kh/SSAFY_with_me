import heapq
import sys

input = sys.stdin.readline

def dijkstra(S):
    pq = []
    heapq.heappush(pq, (0, S))
    distance = [INF] * N
    distance[S] = 0

    while pq:
        dist, now = heapq.heappop(pq)
        if distance[now] < dist:
            continue

        for nxt, cost in graph[now]:
            new_cost = dist + cost
            if distance[nxt] > new_cost:
                distance[nxt] = new_cost
                heapq.heappush(pq, (new_cost, nxt))
                parents[nxt] = [now]  # 최단 경로 부모 갱신
            elif distance[nxt] == new_cost:  # 최단 거리 같은 경우 추가
                parents[nxt].append(now)

    return distance

def mark_shortest_paths(D):
    """ 최단 경로에 해당하는 간선을 삭제 대상으로 표시 """
    queue = [D]
    while queue:
        now = queue.pop()
        for parent in parents[now]:
            if (parent, now) not in remove_edges:
                remove_edges.add((parent, now))
                queue.append(parent)

def almost_dijkstra(S):
    """ 최단 경로 제외 후 다시 다익스트라 실행 """
    pq = []
    heapq.heappush(pq, (0, S))
    distance = [INF] * N
    distance[S] = 0

    while pq:
        dist, now = heapq.heappop(pq)
        if distance[now] < dist:
            continue

        for nxt, cost in graph[now]:
            if (now, nxt) in remove_edges:  # 삭제 대상이면 무시
                continue

            new_cost = dist + cost
            if distance[nxt] > new_cost:
                distance[nxt] = new_cost
                heapq.heappush(pq, (new_cost, nxt))

    return distance

while True:
    N, M = map(int, input().split())
    if N == 0 and M == 0:  # 종료 조건
        break
    S, D = map(int, input().split())
    graph = [[] for _ in range(N)]
    
    for _ in range(M):
        a, b, w = map(int, input().split())
        graph[a].append((b, w))  # 단방향 그래프

    INF = int(1e9)
    parents = [[] for _ in range(N)]  # 최단 경로 부모 저장
    remove_edges = set()  # 삭제할 간선 저장

    init_distance = dijkstra(S)  # 1차 다익스트라 실행
    mark_shortest_paths(D)  # 최단 경로 간선 삭제 대상 등록
    almost_distance = almost_dijkstra(S)  # 2차 다익스트라 실행

    if almost_distance[D] == INF:
        print(-1)
    else:
        print(almost_distance[D])

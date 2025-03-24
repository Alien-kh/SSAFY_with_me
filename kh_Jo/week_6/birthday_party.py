
def dijkstra(start_node):
    pq = [(0, start_node)]  # (누적거리, 노드번호)
    dists = [INF] * (N+1)       # 각 정점까지의 최단 거리를 저장할 리스트
    dists[start_node] = 0   # 시작노드 최단거리는 0

    while pq:
        dist, node = heapq.heappop(pq)

        # 이미 더 작은 경로로 온 적이 있 다면 pass
        # 예제 그림: c로 가는 경로가 3 or 4
        if dists[node] > dist:
            continue

        for next_info in graph[node]:
            next_dist = next_info[0]  # 다음 노드로 가기위한 가중치
            next_node = next_info[1]  # 다음 노드 번호

            # 다음 노드로 가기 위한 누적 거리
            new_dist = dist + next_dist

            # 이미 같은 가중치거나, 더 작은 가중치로 온 적이 있디면 continue
            if dists[next_node] <= new_dist:
                continue

            # next_node 까지 도착하는 데 비용은 new_dist
            dists[next_node] = new_dist
            heapq.heappush(pq, (new_dist, next_node))

    return dists

import heapq
INF = int(21e8)  # 21억 (무한대를 의미한다라고 가정)
T = int(input())
for tc in range(1, T+1):
    N, M, X = map(int,(input().split())) # 1번부터 N번까지 노드 수, M 번은 간선 수 X 는 인수 집
    graph = [[] for _ in range(N + 1)]  # 인접 리스트로 구현
    for _ in range(M):
        u, v, w = map(int, input().split())
        graph[u].append((w, v))  # 단방향 그래프!!!
    result_lst = [[0]]
    for i in range(1, N+1):
        start_node = i  # 문제에 따라 다름



    # result_dists: 0에서 출발해서, 다른 노드들까지의 최단 거리를 모두 구한다.
        result_dists = dijkstra(i)

        result_lst.append(result_dists)

    max_length = -21e8
    for i in range(1, N+1):
        total_dist = result_lst[i][X] + result_lst[X][i]
        if max_length <= total_dist:
            max_length = total_dist
    print(f'#{tc} {max_length}')








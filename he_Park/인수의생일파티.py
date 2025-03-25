import sys
sys.stdin = open('input.txt')

def dijkstra(start_node):
    pq = [(0, start_node)]  # (누적거리, 노드번호)
    dists = [float('inf')] * (V+1)  # 각 정점까지의 최단 거리를 저장할 리스트
    dists[start_node] = 0  # 시작노드 최단거리는 0

    while pq:
        dist, node = heapq.heappop(pq)

        # 이미 더 작은 경로로 온 적이 있다면 pass
        if dists[node] < dist:
            continue

        for next_info in graph[node]:
            next_dist = next_info[0]  # 다음 노드로 가기 위한 가중치
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


T = int(input())
for tc in range(1, T + 1):
    V, E, X = map(int, input().split())  # V개의 집(1~V번), E개의 줄, X번 집
    graph = [[] for _ in range(V+1)]  # 인접 리스트  # 인덱스 번호 == 노드 번호

    for _ in range(E):  # E개의 간선
        s, e, w = map(int, input().split())  # 출발지, 도착지, 걸리는 시간
        graph[s].append((w, e))  # 단방향 그래프


    # result_dists: i에서 출발해서, 다른 노드들까지의 최단 거리를 모두 구한다.
    result_dists = [[]]
    for i in range(1, V+1):
        result_dists.append(dijkstra(i))
    max_v = 0
    for r in range(1, V+1):
        cnt = result_dists[r][X] + result_dists[X][r]
        if max_v < cnt:
            max_v = cnt

    print(f'#{tc} {max_v}')
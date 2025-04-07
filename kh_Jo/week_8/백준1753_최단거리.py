import heapq


def solve(start):
    pq = [(0, start)] # 우선 순위 큐, 앞에는 노드번호, 뒤에는 거리(가중치를 넣어 줄 예정)로 넣어줬는데 heapq,우선순위큐로
    # 나가려면 결국  앞에 가중치가 낮은 순서대로 큐에서 나와야 하기에 기준이 되는 가중치가 먼저 나와야 한다.
    dists = [int(21e8)] * (V+1)
    dists[start] = 0 # 시작지점은 에서 시작지점은 항상 0이니깐(거리가)
    while pq:
        dist, node = heapq.heappop(pq)
        if dists[node] < dist:
            continue # 만약 현재 거리, 가중치보다 기존의 거리가 더 짧다면 볼 필요 없음

        for next_node, next_dist in graph[node]: # 다음 번에 갈 노드와, 가중치를 뽑아내주기(여러 개 있다면 하나씩)
            new_dist = dist + next_dist # 다음 거리는 현재까지 가중치 + 다음 가중치
            if dists[next_node] <= new_dist:
                continue
            dists[next_node] = new_dist
            heapq.heappush(pq, (new_dist, next_node))
    return dists




V, E = map(int, input().split()) # V 는 정점 N 은 간선의 개수
S = int(input())  # S는 시작 지점
graph = [[] for _ in range(V + 1)] # V + 1 을 해준 이유는 1번 부터 시작하려고
for _ in range(E):
    u, v , w =  map(int,  input().split())
    graph[u].append((v, w)) # u는 출발지점 v는 도착지점 w 는 가중치
result = solve(S)
for i in result[1:]:
    if i == int(21e8):
        print('INF')
    else:
        print(i)
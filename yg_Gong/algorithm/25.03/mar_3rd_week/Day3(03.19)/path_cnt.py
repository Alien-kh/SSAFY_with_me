def dfs(node):
    global path_count

    # 도착 노드에 도달하면 경로 1개 완성
    if node == end:
        path_count += 1
        return

    # 현재 노드에서 인접 노드 탐색
    for next_node in graph[node]:
        if visited[next_node]:
            continue
        visited[next_node] = 1
        dfs(next_node)
        visited[next_node] = 0  # 돌아와서 방문 해제



T = int(input())  # 테스트케이스 수

for tc in range(1,T+1):
    N, M = map(int, input().split())  # 노드 수, 간선 수
    edges = list(map(int, input().split()))  # 간선 정보
    start, end = map(int, input().split())  # 출발, 도착 노드

    # 그래프 초기화
    graph = [[] for _ in range(N + 1)]
    for i in range(0, len(edges), 2):
        u, v = edges[i], edges[i + 1]
        graph[u].append(v)

    # 방문 여부 초기화
    visited = [0] * (N + 1)
    visited[start] = 1  # 출발 노드 방문 처리

    # 경로 수 초기화
    path_count = 0

    # DFS 실행
    dfs(start)

    # 결과 출력
    print(f'#{tc} {path_count}')

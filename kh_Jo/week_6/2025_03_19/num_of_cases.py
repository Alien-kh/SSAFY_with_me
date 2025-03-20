def dfs(node):
    global cnt

    if node == end:
        cnt += 1

    for next_node in graph[node]:
        if not visited[next_node]:
            visited[next_node] =1
            dfs(next_node)
            visited[next_node] = 0





T = int(input())
for tc in range(1, T+1):
    N, M = map(int,input().split()) # N 정점, M 간선 수
    graph = [[] for _ in range(N + 1)]  # 입접 리스트(N * N ([])
    arr = list(map(int,input().split()))
    visited = [0] * (N+1)
    for i in range(0, len(arr), 2):
        s, e = arr[i], arr[i+1]
        graph[s].append(e)
    # print(graph)
    cnt = 0
    start, end = map(int,input().split())
    dfs(start)
    print(f'#{tc} {cnt}')
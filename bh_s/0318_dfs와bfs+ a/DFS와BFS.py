# 그래프를 DFS로 탐색한 결과와 BFS로 탐색한 결과를 출력하는 프로그램을 작성하시오.
# 단, 방문할 수 있는 정점이 여러 개인 경우에는 정점 번호가 작은 것을 먼저 방문하고,
# 더 이상 방문할 수 있는 점이 없는 경우 종료한다. 정점 번호는 1번부터 N번까지이다.

# 스택을 이용한 DFS
def dfs(v, N, graph):
    visited = [0] * (N + 1)
    stack = [v]

    while stack:
        node = stack.pop()

        if visited[node] == 0:
            visited[node] = 1
            print(node, end=' ')

            # 인접 노드를 내림차순으로 정렬해 스택에 추가 (작은 번호 우선 탐색을 위해)
            for neighbor in sorted(graph[node], reverse=True):
                if visited[neighbor] == 0:
                    stack.append(neighbor)


# 큐를 이용한 BFS
def bfs(v, N, graph):
    visited = [0] * (N + 1)
    queue = [v]

    while queue:
        node = queue.pop(0)

        if visited[node] == 0:
            visited[node] = 1
            print(node, end=' ')

            # 인접 노드를 오름차순으로 정렬해 큐에 추가 (작은 번호 우선 탐색을 위해)
            for neighbor in sorted(graph[node]):
                if visited[neighbor] == 0:
                    queue.append(neighbor)


N, M, V = map(int, input().split())
graph = [[] for _ in range(N + 1)]

for _ in range(M):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

# 탐색 실행
dfs(V, N, graph)
print()
bfs(V, N, graph)

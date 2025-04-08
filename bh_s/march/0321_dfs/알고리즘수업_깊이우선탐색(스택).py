# 1. 입력 받기
N, M, R = map(int, input().split())  # 정점의 수 N, 간선의 수 M, 시작 정점 R
graph = [[] for _ in range(N + 1)]  # 1번부터 N번까지의 정점을 위한 그래프

# 2. 간선 정보 입력받기
for _ in range(M):
    u, v = map(int, input().split())  # 간선 u, v 입력
    graph[u].append(v)
    graph[v].append(u)

# 3. 방문 순서를 기록할 배열
visited = [False] * (N + 1)  # 방문 여부 체크
order = [0] * (N + 1)  # 방문 순서 기록
visit_count = 1  # 방문 순서 번호

# 4. 스택을 이용한 DFS 구현
def stack_dfs(start):
    global visit_count
    stack = [start]  # 시작 노드를 스택에 추가
    visited[start] = True  # 시작 노드 방문 처리

    while stack:
        node = stack.pop()  # 스택에서 가장 마지막에 들어온 노드를 꺼냄
        order[node] = visit_count  # 현재 노드의 방문 순서 기록
        visit_count += 1

        # 인접한 노드들 중에서 방문하지 않은 노드를 스택에 추가
        for neighbor in sorted(graph[node], reverse=True):  # 내림차순으로 방문 순서 정렬
            if not visited[neighbor]:
                visited[neighbor] = True
                stack.append(neighbor)

# 5. 스택을 이용한 DFS 수행
stack_dfs(R)

# 6. 결과 출력
for i in range(1, N + 1):
    print(order[i] if order[i] != 0 else 0)
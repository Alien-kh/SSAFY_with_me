import sys
sys.setrecursionlimit(200000)  # 깊이 우선 탐색의 재귀 깊이를 충분히 설정
input = sys.stdin.readline

# 1. 주어지는 정보 입력
N, M, R = map(int, input().split())
graph =[[] for _ in range(N+1)]

# 2. 간선 정보 입력
data = [list(map(int, input().split())) for _ in range(M)]
for u, v in data:   # 양방향이니까 서로의 인덱스에 접근해서 추가.
    graph[u].append(v)
    graph[v].append(u)

# 3. 방문 기록
visited = [0] * (N + 1) # 방문 여부를 기록
order = [0] * (N + 1)   # 방문 순서를 기록
visit_count = 1         # 방문 횟수(움직이는 횟수)

# 4. DFS 구현
def dfs(node):
    global visit_count
    visited[node] = True
    order[node] = visit_count
    visit_count += 1

    # 인접한 노드 중에 방문하지 않은 노드 가기.
    for next_node in sorted(graph[node]):
        if not visited[next_node]:
            dfs(next_node)


# 5. DFS 수행
dfs(R)

for i in range(1, N+1):
    print(order[i] if order[i] != 0 else 0)
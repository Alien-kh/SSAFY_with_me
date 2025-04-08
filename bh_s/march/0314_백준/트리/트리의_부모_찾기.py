def dfs(node):
    for next_node in tree[node]:
        if parent[next_node] == -1:  # 아직 방문하지 않은 노드라면
            parent[next_node] = node  # 부모 설정
            dfs(next_node)


N = int(input())  # 노드 개수
tree = [[] for _ in range(N + 1)]  # 트리 구조 초기화
parent = [-1] * (N + 1)  # 부모를 기록할 리스트

# 트리 간선 정보 입력
for _ in range(N - 1):
    u, v = map(int, input().split())
    tree[u].append(v)
    tree[v].append(u)

parent[1] = 0  # 루트 노드(1)의 부모는 0으로 설정 (특별한 값)

# DFS를 통해 부모 노드 구하기
dfs(1)

# 2번 노드부터 N번 노드까지 부모 출력
for i in range(2, N + 1):
    print(parent[i])
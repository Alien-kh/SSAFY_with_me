def dfs(v):
    visited[v] = True # 현재 노드 방문 기록
    for i in edge_list[v]:
        if not visited[i]: # 현재 노드 중 방문하지 않았던 노드로 DFS 재귀 실행
            dfs(i)

node_num, edge_num = map(int, input().split()) # 노드의 갯수와 엣지의 갯수
edge_list = [[] for _ in range(node_num+1)] # 빈 인접리스트 생성
visited = [False] * (node_num+1) # 방문리스트 생성

for _ in range(edge_num):
    node_start, node_end = map(int,input().split())
    edge_list[node_start].append(node_end)
    edge_list[node_end].append(node_start) # 양방향이기 때문

counts = 0

for i in range(1, node_num+1):
    if not visited[i]: # 방문하지 않았던 노드만 선택
        counts += 1 # 연결 요소 개수 값 1 증가
        dfs(i) # DFS 실행

print(counts)

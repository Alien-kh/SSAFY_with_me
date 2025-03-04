def dfs(edge_graph_list, v, visited):
    visited[v] = True # 방문했으니 True로 바꿈
    for i in edge_graph_list[v]:
        if not visited[i]: # 해당 노드에 방문하지 않았다면...
            dfs(edge_graph_list, i, visited) # 그 노드를 기준으로 다시 dfs 실행(재귀)

node_num = int(input())

edge_num = int(input())

edge_graph_list = [[] for _ in range(node_num + 1)] # 그래프 초기화

for _ in range(edge_num): # 엣지 입력
    a, b = list(map(int, input().split()))
    edge_graph_list[a].append(b)
    edge_graph_list[b].append(a) # 양방향 연결

visited = [False] * (node_num + 1) # visit 노드의 수는 공백인 0을 제외시킬거라 총 길이 +1 을 한다.
infected_pc = 0 # 감염된 pc 수

dfs(edge_graph_list, 1, visited) # 1번 pc가 고정 감염 숙주이므로 여기서부터 시작.

for i in range(len(visited)):
    if visited[i] == True:
        infected_pc += 1 # 감염된 상태라면 변수에 +1

print(infected_pc - 1) # 1번 컴퓨터는 최초 숙주이므로 바이러스에 걸리게되는 컴퓨터 수에서 제외
def dfs(graph,s,visited):
    global cycle,start
    for i in graph[s]: # 그래프 순회
        if i == start: # 만약 시작지점으로 돌아왔다면 -> 사이클 돌았다면
            cycle += 1 # 사이클 +1
            return 
        if not visited[i]: # 만약 방문 안했다면
            visited[i] = 1  # 방문 처리하고
            dfs(graph,i,visited)   # 재귀로 다음 노드 탐색

        
T = int(input())
for tc in range(T):
    N = int(input())
    arr = list(map(int,input().split()))
    graph = [[] for _ in range(N+1)]
    for i in range(1,N+1):
        graph[i].append(arr[i-1])
    
    cycle = 0 # 사이클 초기화
    visited = [0] * (N+1)
    for i in range(1,N+1):
        if not visited[i]:
            start = i
            dfs(graph,i,visited)

    print(cycle)
    

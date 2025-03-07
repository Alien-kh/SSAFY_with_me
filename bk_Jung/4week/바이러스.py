def dfs(s): # 재귀로 짠 dfs
    global cnt
    visited[s] = 1 # 시작점 방문처리
    for i in graph[s]: # 그래프 탐색
        if not visited[i]: # 방문하지 않았다면
            cnt += 1 # 카운트
            dfs(i) # 재귀 출발


N = int(input())
E = int(input())
graph = [[] for _ in range(N+1)]
visited = [0] * (N+1)
cnt = 0
for i in range(E):
    a,b = map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)

dfs(1)

print(cnt)
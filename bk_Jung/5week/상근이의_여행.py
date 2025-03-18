def dfs(s):
    global cnt
    visited[s] = 1
    cnt += 1
    for i in graph[s]:
        if not visited[i]:
            dfs(i)


T = int(input())
for tc in range(T):
    N,M = map(int,input().split())
    graph = [[] for _ in range(N+1)] 
    visited = [0] * (N+1)
    for i in range(M):
        a,b = map(int,input().split())
        graph[a].append(b)
        graph[b].append(a)

    cnt = 0
    dfs(1)
    print(cnt-1)
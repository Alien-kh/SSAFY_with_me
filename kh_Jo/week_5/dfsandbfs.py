from collections import deque
def dfs(start):
    s = deque() # 최대 1000개
    s.append(start)
    visited = [0] * (N+1) # 방문 체크
    visited[start] = 1
    check_dfs = [start]
    while s: # 스택이 비워질 떄 동안
        current = s[-1]
        found = False
        for v in sorted(adj_lst[current]): # 작은순대로 방문해야하니깐
            if not visited[v]:
                visited[v] = 1
                s.append(v)
                check_dfs.append(v)
                found = True

            break
        if not found:
            s.pop()
    return check_dfs

def bfs(start):
    q = deque()
    q.append(start)
    visited = [0] * (N+1)
    visited[start] = 1
    check_bfs = [start]
    while q:
        current = q.popleft()
        for i in sorted(adj_lst[current]):
            if  not visited[i]:
                q.append(i)
                visited[i] = 1
                check_bfs.append(i)

    return check_bfs


N, M, S = map(int, input().split())
adj_lst = [[] for _ in range(N+1)] # 1번부터 N 번까지 index 사용
for i in range(M): # 간선의 개수 만큼
    a, b= map(int, input().split())
    adj_lst[a].append(b)
    adj_lst[b].append(a)# 서로 연결됨
dfs_result = dfs(S)
bfs_result = bfs(S)
print(*dfs_result)
print(*bfs_result)
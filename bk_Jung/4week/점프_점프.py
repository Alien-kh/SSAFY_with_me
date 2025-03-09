def dfs(s,arr): # dfs 시작
    global cnt
    visited[s] = 1
    cnt+= 1
    now = arr[s] # 점프 거리
    if s + now < N: # 점프 할 위치가 방문 안했고 리스트 배열 안이라면 dfs 재귀 시작
        if not visited[s+now]:
            dfs(s+now,arr)
    
    if s - now > -1: # 이하동문
        if not visited[s-now]:
            dfs(s-now,arr)

N = int(input())
arr = list(map(int,input().split()))
s = int(input())
visited = [0] * (N)

cnt = 0
dfs(s-1,arr)

print(cnt)

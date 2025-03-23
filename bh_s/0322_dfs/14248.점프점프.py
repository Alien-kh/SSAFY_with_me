def dfs(x):
    global count
    visited[x] = 1
    count += 1

    # 왼쪽으로 점프
    left = x - a[x]
    if left >= 1 and not visited[left]:
        dfs(left)

    # 오른쪽으로 점프
    right = x + a[x]
    if right <= n and not visited[right]:
        dfs(right)

n = int(input())
a = [0] + list(map(int, input().split()))
s = int(input())

visited = [0] * (n + 1)
count = 0

# DFS 탐색 시작
dfs(s)

print(count)
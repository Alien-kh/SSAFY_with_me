'''
1 2 1 3 2 4 2 5 4 6 5 6 6 7 3 7
'''
def bfs(start):
    queue = [start]
    visited = [0] * (V + 1)
    visited[start] = 1
    print(start, end = ' ')

    while queue:
        current = queue.pop(0)  # 선입선출
        for i in range(V + 1):
            if adj[current][i] and not visited[i]:
                queue.append(i)
                visited[i] = 1
                print(i, end=' ')


def dfs(start):
    stack = [start]
    visited = [0] * (V+1)
    visited[start] = 1
    print(start, end = ' ')

    while stack:
        current = stack[-1]
        for i in range(V + 1):
            if adj[current][i] and not visited[i]:
                stack.append(i)
                visited[i] = 1
                print(i, end=' ')
                break
        else:
            stack.pop()



V, E = map(int, input().split())  # 7, 8
arr = list(map(int, input().split()))
adj = [[0] * ( V + 1 ) for _ in range(V + 1)]
for i in range(0, E *2, 2):
    a, b = arr[i], arr[i + 1]
    adj[a][b] = 1
    adj[b][a] = 1

for i in range(V + 1):
    print(adj[i])

# dfs(1)
bfs(1)
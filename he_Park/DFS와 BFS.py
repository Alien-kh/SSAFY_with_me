def dfs(start):
    stack = [start]
    visited = [0] * (N + 1)
    visited[start] = 1
    print(start, end=' ')
    while stack:
        current = stack[-1]
        for i in range(1, N+1):
            if edge[current][i] and not visited[i]:
                stack.append(i)
                visited[i] = 1
                print(i, end=' ')
                break
        else:
            stack.pop()

def bfs(start):
    q = [start]
    visited = [0] * (N + 1)
    visited[start] = 1

    while q:
        t = q.pop(0)
        print(t, end=' ')
        for i in range(1, N + 1):
            if edge[t][i] and not visited[i]:
                q.append(i)
                visited[i] = 1


N, E, V = map(int, input().split())
edge = [[0]*(N+1) for _ in range(N+1)]
for _ in range(E):
    a, b = map(int, input().split())
    edge[a][b] = 1
    edge[b][a] = 1

dfs(V)
print()
bfs(V)
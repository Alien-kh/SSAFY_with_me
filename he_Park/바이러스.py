from collections import deque

def bfs(node):
    queue = deque([node])
    visited[node] = True

    while queue:
        v = queue.popleft()
        for i in adj[v]:
            if not visited[i]:
                queue.append(i)
                visited[i] = True

num = int(input().strip())  # 컴퓨터 수
pair_num = int(input().strip())  # 연결된 컴퓨터 쌍 수
adj = [[] for _ in range(num + 1)]  # [[], [], ...]

for _ in range(pair_num):
    a, b = map(int, input().strip().split())
    adj[a].append(b)
    adj[b].append(a)

visited = [False] * (num + 1)
bfs(1)
print((sum(visited) - 1))